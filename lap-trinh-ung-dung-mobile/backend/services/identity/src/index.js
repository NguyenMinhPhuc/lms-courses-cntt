// identity-service: đăng ký, đăng nhập, refresh token, hồ sơ, ảnh đại diện, quản lý tài khoản (SRS M01, M07, F11.4).
const bcrypt = require('bcryptjs');
const { createService, config, sql, z, schemas, auth, errors, imageUpload } = require('@lhufood/shared');

const { id, page, pageSize, booleanish } = schemas;
const tags = [
  { name: 'Auth', description: 'Đăng ký, đăng nhập, làm mới token, đăng xuất (SRS F01.1–F01.4)' },
  { name: 'Users', description: 'Hồ sơ và ảnh đại diện của người dùng đang đăng nhập (F07.1, F07.2)' },
  { name: 'Admin - Users', description: 'Quản lý tài khoản nhân viên (F11.4), chỉ quản lý' },
];

const email = z.string().trim().toLowerCase().email('Email không đúng định dạng').max(255);
const password = z.string().min(8, 'Mật khẩu tối thiểu 8 ký tự').max(100);
const fullName = z.string().trim().min(2, 'Họ tên tối thiểu 2 ký tự').max(100, 'Họ tên tối đa 100 ký tự');

const avatarUpload = imageUpload({ folder: 'avatars', maxMb: 2, namePrefix: (req) => `u${req.user.sub}` });

function routes({ db }) {
  const getUser = (userId) => db.execute('sp_User_GetById', { UserId: { type: sql.Int, value: userId } }).then((r) => r[0]);

  async function issueTokens(user) {
    const accessToken = auth.signAccessToken(user);
    const refreshToken = auth.signRefreshToken(user);
    await db.execute('sp_RefreshToken_Save', {
      UserId: { type: sql.Int, value: user.userId },
      TokenHash: { type: sql.Char(64), value: auth.sha256(refreshToken) },
      ExpiresAt: { type: sql.DateTime2, value: new Date(Date.now() + config.jwt.refreshExpiresDays * 86400000) },
    });
    return { accessToken, refreshToken, role: user.role };
  }

  const userExample = {
    userId: 3, fullName: 'Nguyễn Văn A', email: 'sv@lhufood.local', role: 'customer',
    avatarUrl: null, isLocked: false, createdAt: '2026-10-30T08:00:00.000Z',
  };

  return [
    {
      method: 'post', path: '/auth/register', tags: ['Auth'],
      summary: 'Đăng ký tài khoản khách hàng',
      description: 'US-G04. Email trùng trả 409. Mật khẩu được băm bằng bcrypt.',
      body: z.object({ fullName, email, password }),
      errors: [409], example: { userId: 12 },
      handler: async ({ body }) => {
        const passwordHash = await bcrypt.hash(body.password, 10);
        const [row] = await db.execute('sp_User_Register', {
          FullName: { type: sql.NVarChar(100), value: body.fullName },
          Email: { type: sql.NVarChar(255), value: body.email },
          PasswordHash: { type: sql.NVarChar(255), value: passwordHash },
        });
        return row;
      },
    },
    {
      method: 'post', path: '/auth/login', tags: ['Auth'], status: 200,
      summary: 'Đăng nhập',
      description: 'US-G05, US-S01. Sai email hoặc mật khẩu đều trả một thông báo chung (BR-03). Tài khoản bị khóa trả 403.',
      body: z.object({ email, password: z.string().min(1, 'Nhập mật khẩu') }),
      errors: [401, 403],
      example: { accessToken: 'eyJhbGciOi...', refreshToken: 'eyJhbGciOi...', role: 'customer', user: userExample },
      handler: async ({ body }) => {
        const [row] = await db.execute('sp_User_GetByEmail', { Email: { type: sql.NVarChar(255), value: body.email } });
        if (!row || !(await bcrypt.compare(body.password, row.PasswordHash))) {
          throw errors.unauthorized('Email hoặc mật khẩu không đúng');
        }
        if (row.IsLocked) throw errors.forbidden('Tài khoản đã bị khóa, vui lòng liên hệ quản lý căn tin');
        const user = { userId: row.UserId, role: row.Role };
        const tokens = await issueTokens(user);
        return {
          ...tokens,
          user: { userId: row.UserId, fullName: row.FullName, email: row.Email, role: row.Role, avatarUrl: row.AvatarUrl },
        };
      },
    },
    {
      method: 'post', path: '/auth/refresh', tags: ['Auth'], status: 200,
      summary: 'Làm mới token (xoay vòng)',
      description: 'US-C14. Mỗi refresh token chỉ dùng một lần; trả cặp token mới. Token đã dùng, hết hạn, bị thu hồi hoặc tài khoản bị khóa trả 401.',
      body: z.object({ refreshToken: z.string().min(1) }),
      errors: [401],
      example: { accessToken: 'eyJhbGciOi...', refreshToken: 'eyJhbGciOi...', role: 'customer' },
      handler: async ({ body }) => {
        try {
          auth.verifyRefreshToken(body.refreshToken);
        } catch {
          throw errors.unauthorized('Refresh token không hợp lệ hoặc đã hết hạn');
        }
        const [row] = await db.execute('sp_RefreshToken_Use', {
          TokenHash: { type: sql.Char(64), value: auth.sha256(body.refreshToken) },
        });
        if (!row) throw errors.unauthorized('Refresh token đã được dùng hoặc bị thu hồi');
        const user = await getUser(row.userId); // đọc lại vai trò hiện tại (có thể đã đổi)
        return issueTokens({ userId: user.userId, role: user.role });
      },
    },
    {
      method: 'post', path: '/auth/logout', tags: ['Auth'], status: 200,
      summary: 'Đăng xuất (thu hồi refresh token)',
      description: 'US-C13. Luôn trả thành công để ứng dụng xóa token cục bộ.',
      body: z.object({ refreshToken: z.string().min(1) }),
      example: { success: true },
      handler: async ({ body }) => {
        await db.execute('sp_RefreshToken_Revoke', {
          TokenHash: { type: sql.Char(64), value: auth.sha256(body.refreshToken) },
        });
        return { success: true };
      },
    },
    {
      method: 'get', path: '/users/me', tags: ['Users'], auth: true,
      summary: 'Hồ sơ người dùng đang đăng nhập', example: userExample,
      handler: ({ user }) => getUser(user.sub),
    },
    {
      method: 'patch', path: '/users/me', tags: ['Users'], auth: true,
      summary: 'Cập nhật họ tên', body: z.object({ fullName }), example: userExample,
      handler: async ({ user, body }) => {
        const [row] = await db.execute('sp_User_UpdateProfile', {
          UserId: { type: sql.Int, value: user.sub },
          FullName: { type: sql.NVarChar(100), value: body.fullName },
        });
        return row;
      },
    },
    {
      method: 'post', path: '/users/me/avatar', tags: ['Users'], auth: true, status: 200,
      summary: 'Đổi ảnh đại diện (multipart, trường "file")',
      description: 'US-C12. Không tự đặt header Content-Type ở client; fetch tự sinh boundary (Chương 8).',
      upload: avatarUpload, errors: [413], example: { avatarUrl: '/uploads/avatars/u3-1730275200000-a1b2c3.jpg' },
      handler: async ({ user, file }) => {
        const [row] = await db.execute('sp_User_UpdateAvatar', {
          UserId: { type: sql.Int, value: user.sub },
          AvatarUrl: { type: sql.NVarChar(500), value: avatarUpload.publicUrl(file) },
        });
        return row;
      },
    },
    {
      method: 'get', path: '/admin/users', tags: ['Admin - Users'], auth: ['admin'],
      summary: 'Danh sách tài khoản',
      query: z.object({
        role: z.enum(auth.ROLES).optional(),
        keyword: z.string().trim().max(100).optional(),
        page, pageSize: pageSize(100, 20),
      }),
      example: [userExample],
      handler: ({ query }) =>
        db.execute('sp_User_GetList', {
          Role: { type: sql.NVarChar(20), value: query.role },
          Keyword: { type: sql.NVarChar(100), value: query.keyword || null },
          Page: { type: sql.Int, value: query.page },
          PageSize: { type: sql.Int, value: query.pageSize },
        }),
    },
    {
      method: 'post', path: '/admin/users', tags: ['Admin - Users'], auth: ['admin'],
      summary: 'Tạo tài khoản nhân viên hoặc quản lý',
      body: z.object({ fullName, email, password, role: z.enum(['staff', 'admin']).default('staff') }),
      errors: [409], example: { userId: 7, fullName: 'Trần Thị B', email: 'b.tran@lhufood.local', role: 'staff' },
      handler: async ({ body }) => {
        const [row] = await db.execute('sp_User_CreateStaff', {
          FullName: { type: sql.NVarChar(100), value: body.fullName },
          Email: { type: sql.NVarChar(255), value: body.email },
          PasswordHash: { type: sql.NVarChar(255), value: await bcrypt.hash(body.password, 10) },
          Role: { type: sql.NVarChar(20), value: body.role },
        });
        return row;
      },
    },
    {
      method: 'patch', path: '/admin/users/:id/lock', tags: ['Admin - Users'], auth: ['admin'],
      summary: 'Khóa hoặc mở khóa tài khoản',
      description: 'Khóa thì thu hồi mọi refresh token của tài khoản đó (access token còn hiệu lực tối đa đến khi hết hạn).',
      params: z.object({ id: id('Mã người dùng') }),
      body: z.object({ locked: booleanish }),
      errors: [404], example: { ...userExample, isLocked: true },
      handler: async ({ params, body, user }) => {
        if (params.id === user.sub && body.locked) throw errors.badRequest('Không thể tự khóa tài khoản của mình');
        const [row] = await db.execute('sp_User_SetLocked', {
          UserId: { type: sql.Int, value: params.id },
          IsLocked: { type: sql.Bit, value: body.locked },
        });
        return row;
      },
    },
  ];
}

createService({
  name: 'identity-service',
  port: config.ports.identity,
  title: 'LHU Food - Identity Service',
  description: 'Tài khoản, xác thực JWT (access 15 phút + refresh xoay vòng), hồ sơ, ảnh đại diện.',
  tags,
  uploadFolders: ['avatars'],
  routes,
});
