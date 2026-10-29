# Chương 6. Xác thực và bảo mật ứng dụng

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Giải thích luồng xác thực bằng JWT với access token và refresh token.
- Lưu mật khẩu an toàn bằng bcrypt và quản lý tài khoản qua stored procedure.
- Xây dựng đăng ký, đăng nhập, Guard xác thực và phân quyền theo vai trò trong NestJS.
- Lưu token an toàn trên điện thoại và bảo vệ màn hình trong Expo Router.
- Nhận diện và phòng tránh các rủi ro bảo mật thường gặp của ứng dụng di động.

## 6.1. Xác thực và phân quyền

- **Xác thực (authentication):** xác định *bạn là ai*. Ví dụ: đăng nhập bằng email và mật khẩu.
- **Phân quyền (authorization):** xác định *bạn được làm gì*. Ví dụ: chỉ nhân viên căn tin được đổi trạng thái đơn.

Hai việc này phải được kiểm tra ở **API**. Ứng dụng chỉ ẩn/hiện nút cho gọn giao diện; nó không phải lớp bảo vệ, vì bất kỳ ai cũng có thể gửi request thẳng tới API mà không cần ứng dụng.

## 6.2. JWT, access token và refresh token

### 6.2.1. JWT là gì

**JSON Web Token (JWT)** là một chuỗi gồm ba phần ngăn cách bởi dấu chấm: header, payload và chữ ký. Payload chứa thông tin như mã người dùng (`sub`) và vai trò (`role`); chữ ký được tạo bằng khóa bí mật chỉ server biết. Khi nhận token, server kiểm tra chữ ký: nếu payload bị sửa, chữ ký sẽ không khớp.

Payload chỉ được **mã hóa base64**, không được mã hóa bí mật: ai có token đều đọc được nội dung. Vì vậy không đặt thông tin nhạy cảm (mật khẩu, số tài khoản) vào payload.

### 6.2.2. Hai loại token

| | Access token | Refresh token |
|---|---|---|
| Mục đích | Gửi kèm mọi request cần đăng nhập | Lấy access token mới khi access token hết hạn |
| Thời hạn | Ngắn (khoảng 15 phút) | Dài (khoảng 7 ngày) |
| Lưu trên server | Không | Có (dạng băm), để có thể thu hồi |
| Gửi đi | Header `Authorization: Bearer <token>` | Chỉ gửi tới `POST /auth/refresh` |

Access token ngắn hạn giới hạn thiệt hại nếu bị lộ. Refresh token được lưu trên server nên có thể **thu hồi** khi người dùng đăng xuất hoặc khi phát hiện bất thường.

### 6.2.3. Luồng đầy đủ

```text
1. Đăng nhập:  App → POST /auth/login {email, password}
2. API: sp_User_GetByEmail → bcrypt.compare(password, PasswordHash)
3. API ký accessToken + refreshToken; lưu băm refreshToken bằng sp_RefreshToken_Save
4. App lưu hai token vào SecureStore
5. Mỗi request: Authorization: Bearer <accessToken>  →  AuthGuard kiểm tra chữ ký
6. Access token hết hạn → API trả 401 → App gọi POST /auth/refresh {refreshToken}
7. API kiểm tra chữ ký và bản băm còn hiệu lực trong CSDL → cấp token mới
8. Đăng xuất: App → POST /auth/logout → API thu hồi refresh token; App xóa SecureStore
```

## 6.3. Lưu mật khẩu và tài khoản trên SQL Server

### 6.3.1. Băm mật khẩu bằng bcrypt

Mật khẩu **không bao giờ** được lưu dạng gốc. Backend băm mật khẩu bằng **bcrypt** trước khi gọi thủ tục:

- bcrypt tự thêm **salt** ngẫu nhiên, nên hai người cùng mật khẩu vẫn có hai chuỗi băm khác nhau.
- Tham số **cost** (ví dụ 10) làm việc băm chậm có chủ đích, khiến việc dò mật khẩu hàng loạt tốn rất nhiều thời gian.
- Khi đăng nhập, `bcrypt.compare(matKhauNhapVao, chuoiBam)` cho biết có khớp không; không có cách "giải băm".

Việc băm thực hiện ở NestJS; stored procedure chỉ nhận và lưu chuỗi băm.

### 6.3.2. Bảng và thủ tục

`database/03-auth.sql`:

```sql
CREATE TABLE Users (
  UserId       INT IDENTITY(1,1) PRIMARY KEY,
  FullName     NVARCHAR(100) NOT NULL,
  Email        NVARCHAR(255) NOT NULL UNIQUE,
  PasswordHash NVARCHAR(255) NOT NULL,
  Role         NVARCHAR(20)  NOT NULL DEFAULT N'customer'
               CHECK (Role IN (N'customer', N'staff')),
  CreatedAt    DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

ALTER TABLE Orders ADD CONSTRAINT FK_Orders_Users FOREIGN KEY (UserId) REFERENCES Users(UserId);

CREATE TABLE RefreshTokens (
  TokenId   INT IDENTITY(1,1) PRIMARY KEY,
  UserId    INT NOT NULL REFERENCES Users(UserId),
  TokenHash CHAR(64) NOT NULL UNIQUE,      -- SHA-256 dạng hex
  ExpiresAt DATETIME2 NOT NULL,
  RevokedAt DATETIME2 NULL
);
GO

CREATE OR ALTER PROCEDURE sp_User_Register
  @FullName NVARCHAR(100), @Email NVARCHAR(255), @PasswordHash NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  IF EXISTS (SELECT 1 FROM Users WHERE Email = @Email)
    THROW 50409, N'Email đã được sử dụng', 1;

  INSERT INTO Users (FullName, Email, PasswordHash) VALUES (@FullName, @Email, @PasswordHash);
  SELECT CAST(SCOPE_IDENTITY() AS INT) AS userId;
END;
GO

-- Thủ tục nội bộ cho backend: trả PasswordHash, không bao giờ gửi kết quả này cho ứng dụng
CREATE OR ALTER PROCEDURE sp_User_GetByEmail
  @Email NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  SELECT UserId, FullName, Email, PasswordHash, Role FROM Users WHERE Email = @Email;
END;
GO

CREATE OR ALTER PROCEDURE sp_RefreshToken_Save
  @UserId INT, @TokenHash CHAR(64), @ExpiresAt DATETIME2
AS
BEGIN
  SET NOCOUNT ON;
  INSERT INTO RefreshTokens (UserId, TokenHash, ExpiresAt) VALUES (@UserId, @TokenHash, @ExpiresAt);
END;
GO

CREATE OR ALTER PROCEDURE sp_RefreshToken_Use
  @TokenHash CHAR(64)
AS
BEGIN
  SET NOCOUNT ON;
  -- Mỗi refresh token chỉ dùng một lần: thu hồi bản cũ, trả về người dùng nếu còn hiệu lực
  UPDATE RefreshTokens SET RevokedAt = SYSDATETIME()
  OUTPUT inserted.UserId AS userId
  WHERE TokenHash = @TokenHash AND RevokedAt IS NULL AND ExpiresAt > SYSDATETIME();
END;
GO

CREATE OR ALTER PROCEDURE sp_RefreshToken_Revoke
  @TokenHash CHAR(64)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE RefreshTokens SET RevokedAt = SYSDATETIME() WHERE TokenHash = @TokenHash AND RevokedAt IS NULL;
END;
GO
```

Refresh token được lưu dưới dạng **băm SHA-256** chứ không phải bcrypt, vì backend cần **tìm** bản ghi theo chuỗi băm; bcrypt sinh chuỗi khác nhau mỗi lần nên không tra cứu được.

`sp_RefreshToken_Use` thực hiện **xoay vòng token**: mỗi refresh token chỉ dùng được một lần, sau đó API cấp cặp token mới. Nếu kẻ gian đánh cắp và dùng refresh token trước, người dùng thật sẽ bị đăng xuất và nhận ra bất thường.

## 6.4. Xác thực trong NestJS

### 6.4.1. Cài đặt và cấu hình

```bash
npm install @nestjs/jwt bcrypt
npm install -D @types/bcrypt
```

Thêm vào `.env` của backend:

```text
JWT_SECRET=<chuỗi ngẫu nhiên dài>
JWT_REFRESH_SECRET=<một chuỗi ngẫu nhiên khác>
```

Đăng ký `JwtModule` trong `AuthModule`:

```ts
JwtModule.registerAsync({
  global: true,
  useFactory: () => ({ secret: process.env.JWT_SECRET, signOptions: { expiresIn: '15m' } }),
}),
```

Nếu cài `bcrypt` trên Windows bị lỗi biên dịch, dùng `bcryptjs` (cùng hàm `hash`, `compare`).

### 6.4.2. AuthService

`src/auth/auth.service.ts`:

```ts
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';
import { createHash } from 'crypto';
import * as sql from 'mssql';
import { DatabaseService } from '../database/database.service';

type UserRow = { UserId: number; FullName: string; Email: string; PasswordHash: string; Role: string };
const sha256 = (value: string) => createHash('sha256').update(value).digest('hex');

@Injectable()
export class AuthService {
  constructor(private readonly db: DatabaseService, private readonly jwt: JwtService) {}

  async register(fullName: string, email: string, password: string) {
    const passwordHash = await bcrypt.hash(password, 10);
    const [row] = await this.db.execute<{ userId: number }>('sp_User_Register', {
      FullName: { type: sql.NVarChar(100), value: fullName },
      Email: { type: sql.NVarChar(255), value: email },
      PasswordHash: { type: sql.NVarChar(255), value: passwordHash },
    });
    return row;
  }

  async login(email: string, password: string) {
    const [user] = await this.db.execute<UserRow>('sp_User_GetByEmail', {
      Email: { type: sql.NVarChar(255), value: email },
    });
    if (!user || !(await bcrypt.compare(password, user.PasswordHash))) {
      throw new UnauthorizedException('Email hoặc mật khẩu không đúng');
    }
    return this.issueTokens(user.UserId, user.Role);
  }

  async refresh(refreshToken: string) {
    let payload: { sub: number; role: string };
    try {
      payload = await this.jwt.verifyAsync(refreshToken, { secret: process.env.JWT_REFRESH_SECRET });
    } catch {
      throw new UnauthorizedException();
    }
    const [row] = await this.db.execute<{ userId: number }>('sp_RefreshToken_Use', {
      TokenHash: { type: sql.Char(64), value: sha256(refreshToken) },
    });
    if (!row) throw new UnauthorizedException();
    return this.issueTokens(payload.sub, payload.role);
  }

  async logout(refreshToken: string) {
    await this.db.execute('sp_RefreshToken_Revoke', {
      TokenHash: { type: sql.Char(64), value: sha256(refreshToken) },
    });
  }

  private async issueTokens(userId: number, role: string) {
    const payload = { sub: userId, role };
    const accessToken = await this.jwt.signAsync(payload);
    const refreshToken = await this.jwt.signAsync(payload, {
      secret: process.env.JWT_REFRESH_SECRET,
      expiresIn: '7d',
    });
    await this.db.execute('sp_RefreshToken_Save', {
      UserId: { type: sql.Int, value: userId },
      TokenHash: { type: sql.Char(64), value: sha256(refreshToken) },
      ExpiresAt: { type: sql.DateTime2, value: new Date(Date.now() + 7 * 24 * 3600 * 1000) },
    });
    return { accessToken, refreshToken, role };
  }
}
```

Lưu ý: thông báo khi sai email và khi sai mật khẩu **giống nhau**, để không tiết lộ email nào đã đăng ký.

### 6.4.3. AuthGuard

Theo mẫu trong tài liệu NestJS:

```ts
import { CanActivate, ExecutionContext, Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private readonly jwt: JwtService) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const [type, token] = request.headers.authorization?.split(' ') ?? [];
    if (type !== 'Bearer' || !token) throw new UnauthorizedException();
    try {
      request.user = await this.jwt.verifyAsync(token);   // { sub, role, iat, exp }
    } catch {
      throw new UnauthorizedException();
    }
    return true;
  }
}
```

### 6.4.4. Phân quyền theo vai trò

```ts
// src/auth/roles.decorator.ts
import { Reflector } from '@nestjs/core';
export const Roles = Reflector.createDecorator<string[]>();

// src/auth/roles.guard.ts
@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private readonly reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const roles = this.reflector.get(Roles, context.getHandler());
    if (!roles) return true;
    const { user } = context.switchToHttp().getRequest();
    return roles.includes(user?.role);
  }
}
```

Sử dụng trong controller:

```ts
@Controller('orders')
@UseGuards(AuthGuard, RolesGuard)
export class OrdersController {
  constructor(private readonly orders: OrdersService) {}

  @Post()
  create(@Req() req, @Body() dto: CreateOrderDto) {
    return this.orders.create(req.user.sub, dto);   // userId lấy từ token
  }

  @Patch(':id/status')
  @Roles(['staff'])
  updateStatus(@Param('id', ParseIntPipe) id: number, @Body() dto: UpdateStatusDto) {
    return this.orders.updateStatus(id, dto.status);
  }
}
```

`AuthGuard` chạy trước để gán `request.user`; `RolesGuard` chạy sau để kiểm tra vai trò. **Mã người dùng luôn lấy từ token**, không lấy từ body hay tham số do ứng dụng gửi lên; nếu không, ai cũng có thể đặt hàng "thay" người khác.

## 6.5. Phía ứng dụng

### 6.5.1. SecureStore và AsyncStorage

| | Expo SecureStore | AsyncStorage |
|---|---|---|
| Lưu trữ | Mã hóa bằng Android Keystore / iOS Keychain | Văn bản thường |
| Dùng cho | Access token, refresh token | Thiết lập không nhạy cảm: giao diện sáng/tối, ngôn ngữ |
| Giới hạn | Phù hợp với chuỗi ngắn | Phù hợp với dữ liệu nhỏ |

Cài đặt: `npx expo install expo-secure-store`. **Không bao giờ lưu mật khẩu** trên điện thoại, kể cả để "ghi nhớ đăng nhập"; refresh token làm việc đó.

### 6.5.2. Store xác thực

`stores/auth.ts`:

```ts
import * as SecureStore from 'expo-secure-store';
import { create } from 'zustand';

type AuthState = {
  token: string | null;
  role: string | null;
  ready: boolean;
  signIn: (tokens: { accessToken: string; refreshToken: string; role: string }) => Promise<void>;
  setAccessToken: (accessToken: string, refreshToken: string) => Promise<void>;
  signOut: () => Promise<void>;
  restore: () => Promise<void>;
};

export const useAuth = create<AuthState>((set) => ({
  token: null,
  role: null,
  ready: false,
  signIn: async ({ accessToken, refreshToken, role }) => {
    await SecureStore.setItemAsync('accessToken', accessToken);
    await SecureStore.setItemAsync('refreshToken', refreshToken);
    await SecureStore.setItemAsync('role', role);
    set({ token: accessToken, role });
  },
  setAccessToken: async (accessToken, refreshToken) => {
    await SecureStore.setItemAsync('accessToken', accessToken);
    await SecureStore.setItemAsync('refreshToken', refreshToken);
    set({ token: accessToken });
  },
  signOut: async () => {
    await Promise.all(['accessToken', 'refreshToken', 'role'].map((k) => SecureStore.deleteItemAsync(k)));
    set({ token: null, role: null });
  },
  restore: async () => {
    const [token, role] = await Promise.all([
      SecureStore.getItemAsync('accessToken'),
      SecureStore.getItemAsync('role'),
    ]);
    set({ token, role, ready: true });
  },
}));
```

Gọi `useAuth.getState().restore()` một lần khi ứng dụng khởi động, ví dụ trong `useEffect` của `app/_layout.tsx`.

### 6.5.3. Gắn token vào request

Sửa `lib/api.ts` của Chương 5:

```ts
import { useAuth } from '@/stores/auth';

export async function api<T>(path: string, init?: RequestInit): Promise<T> {
  const token = useAuth.getState().token;
  const res = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...init?.headers,
    },
  });
  // ... xử lý lỗi như Chương 5
}
```

`useAuth.getState()` đọc store bên ngoài component, phù hợp cho hàm tiện ích như `api`.

### 6.5.4. Bảo vệ màn hình

`app/(tabs)/_layout.tsx`:

```tsx
import { Redirect, Tabs } from 'expo-router';
import { useAuth } from '@/stores/auth';

export default function TabLayout() {
  const token = useAuth((s) => s.token);
  const ready = useAuth((s) => s.ready);

  if (!ready) return null;                         // đang đọc token, tránh nháy màn hình đăng nhập
  if (!token) return <Redirect href="/login" />;

  return <Tabs>{/* các tab như Chương 3 */}</Tabs>;
}
```

Màn hình đăng nhập gọi API, lưu token rồi chuyển hướng bằng `router.replace('/')` để nút Back không quay lại màn hình đăng nhập. Phiên bản Expo Router mới có thêm cơ chế khai báo màn hình được bảo vệ; tham khảo mục Authentication trong tài liệu Expo Router.

### 6.5.5. Xử lý token hết hạn

Khi API trả `401`, ứng dụng nên:

1. Gọi `POST /auth/refresh` với refresh token trong SecureStore.
2. Thành công: lưu cặp token mới bằng `setAccessToken`, gửi lại request ban đầu **đúng một lần**.
3. Thất bại: `signOut()` và chuyển về màn hình đăng nhập với thông báo "Phiên đăng nhập đã hết hạn".
4. Nếu nhiều request cùng gặp `401`, chỉ gọi refresh **một lần** và cho các request còn lại chờ kết quả đó (lưu promise đang chạy vào một biến dùng chung).

Đây là nội dung bài thực hành không hướng dẫn của buổi 06; hãy tự cài đặt trước khi tham khảo lời giải của giảng viên.

## 6.6. Rủi ro bảo mật thường gặp

| Rủi ro | Hậu quả | Cách phòng |
|---|---|---|
| Đặt khóa bí mật, mật khẩu CSDL trong biến `EXPO_PUBLIC_` hoặc trong mã ứng dụng | Ai có file APK đều đọc được | Bí mật chỉ nằm trong `.env` của backend |
| Chỉ ẩn nút ở ứng dụng, API không kiểm tra quyền | Gọi thẳng API vẫn thao tác được | Guard ở API cho mọi endpoint cần bảo vệ |
| Lấy mã người dùng từ body request | Đặt hàng, xem đơn "thay" người khác | Lấy từ `req.user.sub` của token |
| `console.log` token, mật khẩu | Lộ qua log thiết bị, log server | Không log dữ liệu nhạy cảm |
| API dùng tài khoản `sa` của SQL Server | Lộ thông tin đăng nhập là mất toàn bộ CSDL | Tài khoản riêng, chỉ quyền `EXECUTE` |
| Thông báo "email không tồn tại" | Dò được danh sách email đã đăng ký | Một thông báo chung cho mọi trường hợp sai |

### 6.6.1. Tài khoản SQL Server chỉ có quyền EXECUTE

```sql
CREATE LOGIN lhufood_api WITH PASSWORD = '<mật khẩu mạnh>';
GO
USE LhuFood;
CREATE USER lhufood_api FOR LOGIN lhufood_api;
GRANT EXECUTE ON SCHEMA::dbo TO lhufood_api;
```

Tài khoản này chạy được mọi thủ tục trong schema `dbo` nhưng không `SELECT`, `INSERT` hay `DROP` trực tiếp được bảng nào. Nhờ quy tắc "chỉ truy cập qua stored procedure", đây là cấu hình đủ quyền mà vẫn an toàn.

### 6.6.2. Review bảo mật mã do AI sinh

Trước khi merge phần xác thực, kiểm tra lần lượt từng dòng trong bảng ở mục 6.6. Mã do trợ lý AI sinh thường chạy được nhưng hay mắc: đặt khóa bí mật cứng trong mã (`secret: 'abc123'`), lấy `userId` từ body, quên Guard ở một endpoint, hoặc trả nguyên đối tượng người dùng có `PasswordHash` về ứng dụng.

## 6.7. Checkpoint Sprint 2

Cuối buổi 06, mỗi nhóm:

- Demo luồng nghiệp vụ chính với dữ liệu thật từ API, có đăng nhập và phân quyền.
- Thực hiện Sprint Review và Retrospective.
- **Mỗi thành viên** nộp bản nháp báo cáo vai trò cá nhân (1 trang: nhiệm vụ đảm nhận, PR/commit tiêu biểu, khó khăn đã giải quyết, phần AI hỗ trợ) và tự trình bày 2 phút. Giảng viên góp ý để hoàn thiện cho đánh giá CLO4 cuối kỳ.
- Nộp `PROMPTS.md` của Sprint 2.

## Tóm tắt chương

- Xác thực và phân quyền luôn được kiểm tra ở API; ứng dụng chỉ điều chỉnh giao diện.
- JWT có chữ ký nhưng payload đọc được; access token ngắn hạn, refresh token dài hạn, được lưu băm và xoay vòng.
- Mật khẩu băm bằng bcrypt ở backend; tài khoản và refresh token đọc/ghi qua stored procedure.
- AuthGuard xác thực, RolesGuard phân quyền; mã người dùng lấy từ token.
- Token lưu trong SecureStore; màn hình được bảo vệ bằng `Redirect`; bí mật không bao giờ nằm trong ứng dụng; tài khoản SQL Server của API chỉ có quyền `EXECUTE`.

## Câu hỏi ôn tập

1. Phân biệt xác thực và phân quyền; cho ví dụ trong LHU Food.
2. Vì sao payload của JWT không được chứa thông tin nhạy cảm?
3. Vì sao refresh token được băm bằng SHA-256 mà mật khẩu lại băm bằng bcrypt?
4. Xoay vòng refresh token giúp phát hiện điều gì?
5. Vì sao lấy `userId` từ body request là một lỗ hổng?
6. Tài khoản SQL Server chỉ có quyền `EXECUTE` bảo vệ hệ thống trong tình huống nào?

## Bài tập

1. **Token hết hạn.** Cài đặt quy trình ở mục 6.5.5. Thử bằng cách đặt access token hết hạn sau 1 phút; sau đó thu hồi refresh token trong CSDL và kiểm tra ứng dụng tự về màn hình đăng nhập.
2. **Giao diện theo vai trò.** Với tài khoản `staff`, tab Đơn hàng hiển thị tất cả đơn mới và nút đổi trạng thái; với `customer`, chỉ hiển thị đơn của mình. API phải kiểm tra quyền tương ứng.
3. **Rà soát bảo mật.** Rà soát dự án của nhóm theo bảng ở mục 6.6; lập báo cáo ngắn gồm rủi ro đã phát hiện, cách sửa và commit tương ứng.

## Tài liệu tham khảo

- NestJS - Authentication: https://docs.nestjs.com/security/authentication
- NestJS - Authorization: https://docs.nestjs.com/security/authorization
- NestJS - Guards: https://docs.nestjs.com/guards
- Expo - SecureStore: https://docs.expo.dev/versions/latest/sdk/securestore/
- Expo Router - Authentication: https://docs.expo.dev/router/advanced/authentication/
- Microsoft Learn - GRANT Schema Permissions: https://learn.microsoft.com/sql/t-sql/statements/grant-schema-permissions-transact-sql
- OWASP Mobile Application Security: https://mas.owasp.org/
