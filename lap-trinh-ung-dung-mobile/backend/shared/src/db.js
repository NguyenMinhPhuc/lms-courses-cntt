// Truy cập SQL Server. Cách DUY NHẤT để đọc/ghi dữ liệu là gọi stored procedure có tham số
// (quy tắc của học phần): không có câu SQL viết trực tiếp, không dùng ORM.
const sql = require('mssql');
const config = require('./config');
const { HttpError } = require('./errors');

// Mã lỗi THROW trong thủ tục → mã HTTP (quy ước Chương 5)
const SQL_TO_HTTP = { 50400: 400, 50401: 401, 50403: 403, 50404: 404, 50409: 409 };

let poolPromise = null;

function getPool() {
  if (!poolPromise) {
    const pool = new sql.ConnectionPool({
      server: config.db.server,
      port: config.db.port,
      database: config.db.database,
      user: config.db.user,
      password: config.db.password,
      pool: { max: 10, min: 0, idleTimeoutMillis: 30000 },
      options: {
        encrypt: config.db.encrypt,
        trustServerCertificate: config.db.trustServerCertificate,
        enableArithAbort: true,
        // Thủ tục lưu giờ theo SYSDATETIME() (giờ của SQL Server, như giáo trình). useUTC: false để mssql
        // hiểu DATETIME2 là giờ địa phương của máy chạy service; JSON trả về ISO UTC đúng.
        // Yêu cầu: máy chạy service cùng múi giờ với SQL Server (Việt Nam, UTC+7).
        useUTC: false,
      },
    });
    poolPromise = pool.connect().catch((err) => {
      poolPromise = null; // lần gọi sau thử kết nối lại
      throw err;
    });
  }
  return poolPromise;
}

function mapError(err, procedure) {
  const status = SQL_TO_HTTP[err?.number];
  if (status) return new HttpError(status, err.message);
  err.procedure = procedure;
  return err;
}

async function run(procedure, params) {
  const pool = await getPool();
  const request = pool.request();
  for (const [name, p] of Object.entries(params || {})) {
    request.input(name, p.type, p.value === undefined ? null : p.value);
  }
  try {
    return await request.execute(procedure);
  } catch (err) {
    throw mapError(err, procedure);
  }
}

/** Chạy thủ tục, trả về tập kết quả đầu tiên (mảng dòng). */
async function execute(procedure, params) {
  const result = await run(procedure, params);
  return result.recordset ?? [];
}

/** Chạy thủ tục trả về nhiều tập kết quả (ví dụ: đơn hàng + danh sách món). */
async function executeMulti(procedure, params) {
  const result = await run(procedure, params);
  return result.recordsets ?? [];
}

async function closePool() {
  if (poolPromise) {
    const pool = await poolPromise.catch(() => null);
    poolPromise = null;
    if (pool) await pool.close();
  }
}

module.exports = { sql, execute, executeMulti, getPool, closePool };
