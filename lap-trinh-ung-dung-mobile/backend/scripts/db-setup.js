// Dựng CSDL LHU Food: tạo database (nếu chưa có), chạy database/*.sql theo thứ tự số, tạo tài khoản mẫu.
// Chạy lại nhiều lần an toàn (script dùng IF NOT EXISTS / CREATE OR ALTER).
//
//   npm run db:setup                                  dựng CSDL + dữ liệu mẫu
//   npm run db:setup -- --create-login lhufood_api    thêm login chỉ có quyền EXECUTE (mật khẩu: biến DB_API_PASSWORD)
//
// Script cài đặt dùng câu lệnh quản trị (CREATE DATABASE, CREATE LOGIN) nên chạy bằng tài khoản quản trị
// (DB_ADMIN_USER). Bản thân các service KHÔNG viết SQL trực tiếp, chỉ gọi stored procedure.
const fs = require('fs');
const path = require('path');
const bcrypt = require('bcryptjs');
const sql = require('mssql');
const config = require('../shared/src/config');

const DB_DIR = path.join(config.root, 'database');
const NAME_RE = /^[A-Za-z0-9_]+$/;

function connection(database) {
  return {
    server: config.db.server,
    port: config.db.port,
    database,
    user: config.db.adminUser,
    password: config.db.adminPassword,
    requestTimeout: 120000,
    options: { encrypt: config.db.encrypt, trustServerCertificate: config.db.trustServerCertificate },
  };
}

const batches = (text) =>
  text
    .replace(/^﻿/, '')
    .split(/^\s*GO\s*$/im)
    .map((b) => b.trim())
    .filter(Boolean);

async function ensureDatabase() {
  const name = config.db.database;
  if (!NAME_RE.test(name)) throw new Error(`Tên CSDL không hợp lệ: ${name}`);
  const pool = await new sql.ConnectionPool(connection('master')).connect();
  try {
    const exists = await pool.request().input('name', sql.NVarChar(128), name).query('SELECT DB_ID(@name) AS id');
    if (exists.recordset[0].id === null) {
      await pool.request().batch(`CREATE DATABASE [${name}]`);
      console.log(`[+] Đã tạo CSDL ${name}`);
    } else {
      console.log(`[=] CSDL ${name} đã có, chạy lại script (an toàn)`);
    }
  } finally {
    await pool.close();
  }
}

// Thủ tục tên "sp_..." được SQL Server tìm trong master trước; trên một số server, CREATE OR ALTER
// với tên như vậy báo lỗi 208 "Invalid object name". Đổi thành: tạo thủ tục rỗng (nếu chưa có) rồi ALTER.
const CREATE_OR_ALTER = /^((?:\s*--[^\n]*\n)*)\s*CREATE\s+OR\s+ALTER\s+PROCEDURE\s+([^\s(]+)/i;

async function runBatch(pool, batch) {
  const m = batch.match(CREATE_OR_ALTER);
  if (!m) return pool.request().batch(batch);
  const name = m[2];
  await pool.request().batch(`IF OBJECT_ID(N'${name}', N'P') IS NULL EXEC(N'CREATE PROCEDURE ${name} AS RETURN 0');`);
  return pool.request().batch(batch.replace(CREATE_OR_ALTER, `$1ALTER PROCEDURE ${name}`));
}

async function runScripts(pool) {
  const files = fs.readdirSync(DB_DIR).filter((f) => /^\d+.*\.sql$/i.test(f)).sort();
  for (const file of files) {
    const parts = batches(fs.readFileSync(path.join(DB_DIR, file), 'utf8'));
    for (const [i, batch] of parts.entries()) {
      try {
        await runBatch(pool, batch);
      } catch (err) {
        throw new Error(`${file} (khối ${i + 1}/${parts.length}): ${err.message}`);
      }
    }
    console.log(`[+] ${file} (${parts.length} khối)`);
  }
}

async function seedUsers(pool) {
  const accounts = [
    { fullName: 'Quản lý căn tin', email: process.env.SEED_ADMIN_EMAIL || 'admin@lhufood.local', password: process.env.SEED_ADMIN_PASSWORD || 'Admin@123', role: 'admin' },
    { fullName: 'Nhân viên căn tin', email: process.env.SEED_STAFF_EMAIL || 'staff@lhufood.local', password: process.env.SEED_STAFF_PASSWORD || 'Staff@123', role: 'staff' },
    { fullName: 'Sinh viên mẫu', email: process.env.SEED_CUSTOMER_EMAIL || 'sv@lhufood.local', password: process.env.SEED_CUSTOMER_PASSWORD || 'Sinhvien@123', role: 'customer' },
  ];
  for (const a of accounts) {
    const found = await pool.request().input('Email', sql.NVarChar(255), a.email).execute('sp_User_GetByEmail');
    if (found.recordset.length) {
      console.log(`[=] Tài khoản ${a.role}: ${a.email} (đã có)`);
      continue;
    }
    await pool
      .request()
      .input('FullName', sql.NVarChar(100), a.fullName)
      .input('Email', sql.NVarChar(255), a.email)
      .input('PasswordHash', sql.NVarChar(255), await bcrypt.hash(a.password, 10))
      .input('Role', sql.NVarChar(20), a.role)
      .execute('sp_User_CreateStaff');
    console.log(`[+] Tài khoản ${a.role}: ${a.email}`);
  }
}

async function createApiLogin(pool, login) {
  const password = process.env.DB_API_PASSWORD;
  if (!NAME_RE.test(login)) throw new Error(`Tên login không hợp lệ: ${login}`);
  if (!password) throw new Error('Đặt biến môi trường DB_API_PASSWORD (mật khẩu mạnh) trước khi tạo login');
  const quoted = password.replace(/'/g, "''");
  await pool.request().batch(`
    IF SUSER_ID(N'${login}') IS NULL CREATE LOGIN [${login}] WITH PASSWORD = N'${quoted}', CHECK_POLICY = ON;
    IF USER_ID(N'${login}') IS NULL CREATE USER [${login}] FOR LOGIN [${login}];
    GRANT EXECUTE ON SCHEMA::dbo TO [${login}];`);
  console.log(`[+] Login ${login}: chỉ có quyền EXECUTE trên schema dbo. Đổi DB_USER/DB_PASSWORD của các service sang login này.`);
}

async function main() {
  const args = process.argv.slice(2);
  const loginIndex = args.indexOf('--create-login');
  console.log(`SQL Server: ${config.db.server}:${config.db.port} · CSDL: ${config.db.database} · tài khoản cài đặt: ${config.db.adminUser}`);
  if (!config.db.adminPassword) throw new Error('Chưa có mật khẩu: điền DB_PASSWORD (hoặc DB_ADMIN_PASSWORD) trong backend/.env');

  await ensureDatabase();
  const pool = await new sql.ConnectionPool(connection(config.db.database)).connect();
  try {
    await runScripts(pool);
    await seedUsers(pool);
    if (loginIndex >= 0) await createApiLogin(pool, args[loginIndex + 1] || 'lhufood_api');
    const summary = await pool.request().batch(`
      SELECT (SELECT COUNT(*) FROM sys.tables) AS tables,
             (SELECT COUNT(*) FROM sys.procedures WHERE name LIKE 'sp[_]%') AS procedures,
             (SELECT COUNT(*) FROM dbo.Products) AS products,
             (SELECT COUNT(*) FROM dbo.Users) AS users`);
    const s = summary.recordset[0];
    console.log(`[✓] Xong: ${s.tables} bảng, ${s.procedures} thủ tục, ${s.products} món, ${s.users} tài khoản.`);
  } finally {
    await pool.close();
  }
}

main().catch((err) => {
  console.error(`[LỖI] ${err.message}`);
  process.exit(1);
});
