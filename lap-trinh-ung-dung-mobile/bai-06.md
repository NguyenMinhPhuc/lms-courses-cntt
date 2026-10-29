<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 06 - Xác thực &amp; bảo mật ứng dụng (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Hiện tại ai mở được LHU Food cũng đặt được hàng, và đơn hàng không biết thuộc về ai. Nhân viên căn tin và khách hàng dùng chung một app nhưng phải thấy các màn hình khác nhau. Làm sao để app "biết bạn là ai" sau mỗi lần mở, mà không lưu mật khẩu trên điện thoại?</em></p>
        <p><strong>Mục tiêu:</strong> Triển khai được đăng ký/đăng nhập bằng JWT ở cả API và ứng dụng; lưu trữ token an toàn; bảo vệ được màn hình và API theo trạng thái đăng nhập và vai trò.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Luồng xác thực JWT:</strong> đăng ký, đăng nhập, access token và refresh token; băm mật khẩu bằng bcrypt ở backend; dữ liệu người dùng đọc/ghi qua stored procedure.</li>
            <li><strong>Ý chính 2 - Lưu token đúng chỗ:</strong> Expo SecureStore cho token, AsyncStorage cho thiết lập không nhạy cảm; không bao giờ lưu mật khẩu.</li>
            <li><strong>Ý chính 3 - Bảo vệ route và phân quyền:</strong> chuyển hướng khi chưa đăng nhập trong Expo Router; Guard kiểm tra token và vai trò trong NestJS.</li>
            <li><strong>Ý chính 4 - Rủi ro bảo mật trên mobile:</strong> khóa bí mật trong bundle, log nhạy cảm, chỉ kiểm tra quyền ở app; tài khoản SQL Server chỉ có quyền <code>EXECUTE</code>.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> LHU Food có đăng ký/đăng nhập, tự đăng nhập lại khi mở app, phân quyền khách hàng/nhân viên; nhóm hoàn thành <strong>Checkpoint Sprint 2</strong> và nộp bản nháp báo cáo vai trò cá nhân.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO4.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Luồng xác thực JWT giữa app và NestJS</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>1. App gửi email + mật khẩu       → POST /auth/login
2. API gọi sp_User_GetByEmail, so mật khẩu với PasswordHash bằng bcrypt
3. API trả về accessToken (ngắn hạn, ~15 phút) + refreshToken (dài hạn, ~7 ngày)
4. App lưu token vào SecureStore
5. Mỗi request sau đó gửi header:  Authorization: Bearer &lt;accessToken&gt;
6. accessToken hết hạn → app gọi POST /auth/refresh bằng refreshToken để lấy token mới</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>JWT</strong> là chuỗi đã ký, chứa thông tin như mã người dùng và vai trò. Server kiểm tra chữ ký nên không cần tra CSDL ở mỗi request.</li>
                <li><strong>Access token ngắn hạn</strong> giảm thiệt hại nếu bị lộ; <strong>refresh token</strong> giúp người dùng không phải đăng nhập lại liên tục.</li>
                <li><strong>Mật khẩu</strong> được băm bằng <code>bcrypt</code> trong NestJS trước khi gọi thủ tục; CSDL chỉ lưu <code>PasswordHash</code>, không bao giờ lưu mật khẩu gốc.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Bảng Users và stored procedure</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>CREATE TABLE Users (
  UserId       INT IDENTITY(1,1) PRIMARY KEY,
  FullName     NVARCHAR(100) NOT NULL,
  Email        NVARCHAR(255) NOT NULL UNIQUE,
  PasswordHash NVARCHAR(255) NOT NULL,
  Role         NVARCHAR(20)  NOT NULL DEFAULT N'customer'
               CHECK (Role IN (N'customer', N'staff')),
  CreatedAt    DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);
GO

CREATE OR ALTER PROCEDURE sp_User_Register
  @FullName NVARCHAR(100), @Email NVARCHAR(255), @PasswordHash NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  IF EXISTS (SELECT 1 FROM Users WHERE Email = @Email)
    THROW 50409, N'Email đã được sử dụng', 1;

  INSERT INTO Users (FullName, Email, PasswordHash)
  VALUES (@FullName, @Email, @PasswordHash);

  SELECT CAST(SCOPE_IDENTITY() AS INT) AS userId;
END;
GO

CREATE OR ALTER PROCEDURE sp_User_GetByEmail
  @Email NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  SELECT UserId, FullName, Email, PasswordHash, Role FROM Users WHERE Email = @Email;
END;
GO</code></pre>
            <p style="margin-bottom: 0;">Refresh token cũng nên được lưu (dạng băm) qua thủ tục, ví dụ <code>sp_RefreshToken_Save</code> và <code>sp_RefreshToken_Revoke</code>, để có thể thu hồi khi người dùng đăng xuất. Bổ sung bảng <code>Users</code> vào ERD và thêm khóa ngoại <code>Orders.UserId</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Đăng nhập và Guard trong NestJS</h3>
            <p>Cài: <code>npm install @nestjs/jwt bcrypt</code> và <code>npm install -D @types/bcrypt</code>. Khóa bí mật JWT đặt trong <code>.env</code> của backend, không bao giờ đưa vào app.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// src/auth/auth.service.ts
async login(email: string, password: string) {
  const [user] = await this.db.execute&lt;UserRow&gt;('sp_User_GetByEmail', {
    Email: { type: sql.NVarChar(255), value: email },
  });
  if (!user || !(await bcrypt.compare(password, user.PasswordHash))) {
    throw new UnauthorizedException('Email hoặc mật khẩu không đúng');
  }
  const payload = { sub: user.UserId, role: user.Role };
  return {
    accessToken: await this.jwt.signAsync(payload, { expiresIn: '15m' }),
    refreshToken: await this.jwt.signAsync(payload, {
      secret: process.env.JWT_REFRESH_SECRET, expiresIn: '7d',
    }),
  };
}

async register(dto: RegisterDto) {
  const passwordHash = await bcrypt.hash(dto.password, 10);
  const [row] = await this.db.execute&lt;{ userId: number }&gt;('sp_User_Register', {
    FullName: { type: sql.NVarChar(100), value: dto.fullName },
    Email: { type: sql.NVarChar(255), value: dto.email },
    PasswordHash: { type: sql.NVarChar(255), value: passwordHash },
  });
  return row;
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// src/auth/auth.guard.ts  (theo mẫu trong tài liệu NestJS)
@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private jwt: JwtService) {}

  async canActivate(context: ExecutionContext): Promise&lt;boolean&gt; {
    const request = context.switchToHttp().getRequest();
    const [type, token] = request.headers.authorization?.split(' ') ?? [];
    if (type !== 'Bearer' || !token) throw new UnauthorizedException();
    try {
      request.user = await this.jwt.verifyAsync(token);
    } catch {
      throw new UnauthorizedException();
    }
    return true;
  }
}

// Dùng: chỉ người đã đăng nhập mới đặt hàng được
@UseGuards(AuthGuard)
@Post()
create(@Req() req, @Body() dto: CreateOrderDto) {
  return this.ordersService.create(req.user.sub, dto);
}</code></pre>
            <p style="margin-bottom: 0;"><strong>Phân quyền theo vai trò:</strong> tạo thêm <code>RolesGuard</code> đọc <code>request.user.role</code>; ví dụ chỉ <code>staff</code> được gọi <code>PATCH /orders/:id/status</code>. Mã người dùng lấy từ token (<code>req.user.sub</code>), <strong>không</strong> lấy từ body do app gửi lên.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Lưu token và bảo vệ màn hình trong app</h3>
            <p><strong>Expo SecureStore</strong> lưu dữ liệu đã mã hóa bằng kho khóa của hệ điều hành (Android Keystore, iOS Keychain). <strong>AsyncStorage</strong> lưu dạng văn bản thường, chỉ dùng cho thiết lập không nhạy cảm như chế độ sáng/tối. Cài: <code>npx expo install expo-secure-store</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// stores/auth.ts
import * as SecureStore from 'expo-secure-store';
import { create } from 'zustand';

type AuthState = {
  token: string | null;
  ready: boolean;
  signIn: (accessToken: string, refreshToken: string) =&gt; Promise&lt;void&gt;;
  signOut: () =&gt; Promise&lt;void&gt;;
  restore: () =&gt; Promise&lt;void&gt;;
};

export const useAuth = create&lt;AuthState&gt;((set) =&gt; ({
  token: null,
  ready: false,
  signIn: async (accessToken, refreshToken) =&gt; {
    await SecureStore.setItemAsync('accessToken', accessToken);
    await SecureStore.setItemAsync('refreshToken', refreshToken);
    set({ token: accessToken });
  },
  signOut: async () =&gt; {
    await SecureStore.deleteItemAsync('accessToken');
    await SecureStore.deleteItemAsync('refreshToken');
    set({ token: null });
  },
  restore: async () =&gt; {
    const token = await SecureStore.getItemAsync('accessToken');
    set({ token, ready: true });
  },
}));</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(tabs)/_layout.tsx: chưa đăng nhập thì chuyển sang màn hình đăng nhập
import { Redirect, Tabs } from 'expo-router';
import { useAuth } from '@/stores/auth';

export default function TabLayout() {
  const { token, ready } = useAuth();
  if (!ready) return null;                       // đang đọc token từ SecureStore
  if (!token) return &lt;Redirect href="/login" /&gt;;
  return &lt;Tabs&gt;{/* các tab như bài 03 */}&lt;/Tabs&gt;;
}

// lib/api.ts: tự gắn token vào mọi request
const token = useAuth.getState().token;
headers: { Authorization: token ? `Bearer ${token}` : '', ... }</code></pre>
            <p style="margin-bottom: 0;">Gọi <code>useAuth.getState().restore()</code> một lần khi app khởi động (trong <code>app/_layout.tsx</code>). Đăng nhập thành công thì dùng <code>router.replace('/')</code> để nút Back không quay về màn hình đăng nhập.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Rủi ro bảo mật thường gặp</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Rủi ro</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Cách phòng</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Đặt khóa bí mật JWT hoặc mật khẩu CSDL trong app (<code>EXPO_PUBLIC_...</code>)</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Bí mật chỉ nằm trong <code>.env</code> của backend; mọi thứ trong app đều có thể bị đọc ra từ file APK</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Chỉ ẩn nút "Quản lý" ở app mà API không kiểm tra quyền</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Luôn kiểm tra quyền ở API bằng Guard; app ẩn nút chỉ là để giao diện gọn</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>console.log</code> token, mật khẩu</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Không log dữ liệu nhạy cảm, kể cả khi đang gỡ lỗi</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">API dùng tài khoản <code>sa</code> của SQL Server</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Tạo tài khoản riêng chỉ có quyền chạy thủ tục: <code>GRANT EXECUTE ON SCHEMA::dbo TO lhufood_api;</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Thông báo lỗi tiết lộ "email không tồn tại"</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Dùng chung một câu "Email hoặc mật khẩu không đúng"</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;"><strong>Review bảo mật cho mã AI sinh ra:</strong> trước khi merge phần xác thực, kiểm tra lần lượt 5 dòng trong bảng trên. AI thường sinh mã chạy được nhưng hay đặt khóa bí mật ngay trong mã hoặc quên kiểm tra quyền ở server.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 06: Xác thực &amp; bảo mật ứng dụng</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.nestjs.com/security/authentication" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - Authentication</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đăng nhập, phát JWT và AuthGuard.</span>
            </a>
            <a href="https://docs.nestjs.com/security/authorization" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - Authorization</span><br>
                <span style="color: #6c757d; font-size: 13px;">Phân quyền theo vai trò với RolesGuard.</span>
            </a>
            <a href="https://docs.expo.dev/versions/latest/sdk/securestore/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - SecureStore</span><br>
                <span style="color: #6c757d; font-size: 13px;">Lưu dữ liệu nhạy cảm đã mã hóa trên thiết bị.</span>
            </a>
            <a href="https://docs.expo.dev/router/advanced/authentication/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo Router - Authentication</span><br>
                <span style="color: #6c757d; font-size: 13px;">Các cách bảo vệ màn hình theo trạng thái đăng nhập.</span>
            </a>
        </div>
    </div>
</details>

<details style="border: 1px solid #28a745; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #eafaf1; color: #28a745; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>💡 3. Hoạt động &amp; Thực hành trên lớp</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Đăng nhập LHU Food</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tạo bảng <code>Users</code>, các thủ tục ở mục 2.2; tạo tài khoản SQL Server riêng cho API, chỉ cấp quyền <code>EXECUTE</code>; đổi <code>.env</code> của API sang tài khoản này.</li>
                <li>Module <code>auth</code> trong NestJS: <code>POST /auth/register</code>, <code>POST /auth/login</code>; gắn <code>AuthGuard</code> cho <code>POST /orders</code>.</li>
                <li>App: màn hình Đăng nhập và Đăng ký (dùng form bài 04); store <code>auth</code> với SecureStore; <code>restore()</code> khi mở app.</li>
                <li>Bảo vệ nhóm <code>(tabs)</code> bằng <code>Redirect</code>; <code>lib/api.ts</code> tự gắn header <code>Authorization</code>.</li>
                <li>Nút Đăng xuất ở tab Tài khoản; kiểm tra: tắt app mở lại vẫn đăng nhập, đăng xuất rồi bấm Back không vào lại được.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Token hết hạn</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Xử lý khi API trả về <code>401</code>: app gọi <code>POST /auth/refresh</code> bằng refresh token, lưu token mới và gửi lại request ban đầu đúng một lần; nếu refresh cũng thất bại thì đăng xuất và về màn hình đăng nhập kèm thông báo "Phiên đăng nhập đã hết hạn".</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> đặt <code>expiresIn</code> của access token còn 1 phút để thử; sau 1 phút app vẫn hoạt động bình thường; xóa refresh token trong CSDL thì app tự về màn hình đăng nhập.</p>
            <a href="{{LINK_NOP_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🏁 Thử thách nhóm: Checkpoint Sprint 2</strong></p>
            <ul style="margin: 0 0 8px 0; color: #495057;">
                <li>Luồng nghiệp vụ chính của đề tài chạy với dữ liệu thật từ API và có đăng nhập, phân quyền.</li>
                <li>Demo trên Android + Sprint Review và Retrospective.</li>
                <li><strong>Mỗi thành viên</strong> nộp <strong>bản nháp báo cáo vai trò cá nhân</strong> (1 trang: nhiệm vụ đảm nhận, PR/commit tiêu biểu, khó khăn đã giải quyết) và <strong>tự trình bày 2 phút</strong> phần mình làm. Giảng viên góp ý để hoàn thiện cho cuối kỳ (CLO4).</li>
                <li>Nộp <code>PROMPTS.md</code> của sprint 2.</li>
            </ul>
            <a href="{{LINK_NOP_CHECKPOINT_2}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp Checkpoint 2</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Rà soát phần xác thực của nhóm theo bảng ở mục 2.5. Nhóm đã phát hiện và sửa rủi ro nào? Rủi ro nào AI sinh ra mà nhóm suýt bỏ qua?</p>
            <a href="{{LINK_DIEN_DAN_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập luồng JWT, băm mật khẩu, SecureStore, bảo vệ route và các rủi ro bảo mật.</p>
            <a href="{{LINK_QUIZ_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 06</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>API luôn trả 401:</strong> kiểm tra header có đúng dạng <code>Bearer &lt;token&gt;</code> (có dấu cách); khóa bí mật khi ký và khi kiểm tra phải giống nhau.</p>
        <p><strong>Màn hình nháy về trang đăng nhập rồi mới vào app:</strong> app chưa đọc xong token từ SecureStore đã kiểm tra; dùng cờ <code>ready</code> như mục 2.4.</p>
        <p><strong>Lỗi cài bcrypt trên Windows:</strong> bcrypt cần biên dịch mã native; nếu lỗi, dùng <code>bcryptjs</code> (cùng cách gọi <code>hash</code>/<code>compare</code>).</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu đăng nhập bằng vân tay/khuôn mặt với <code>expo-local-authentication</code> để mở khóa token đã lưu.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu ai đó lấy được file APK của nhóm và giải nén, họ đọc được những gì? Có thông tin nào giúp họ truy cập CSDL không?</p>
    </div>
</details>
