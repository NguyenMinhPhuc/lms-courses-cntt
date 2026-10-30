# Bài 06: Xác thực & bảo mật ứng dụng
JWT, SecureStore, bảo vệ route · Checkpoint Sprint 2

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Triển khai đăng ký, đăng nhập bằng JWT ở API và ứng dụng
- Lưu token an toàn bằng Expo SecureStore
- Bảo vệ màn hình và API theo đăng nhập và vai trò
- Nhận diện các rủi ro bảo mật thường gặp trên mobile
**Ghi chú giảng viên**:
- 2 tiết lý thuyết, 3 tiết thực hành. CLO1, CLO4. Cuối buổi là Checkpoint Sprint 2.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Ai mở được app cũng đặt được hàng, đơn hàng không biết của ai
- Khách hàng và nhân viên căn tin cần thấy màn hình khác nhau
- App "biết bạn là ai" sau mỗi lần mở, nhưng không lưu mật khẩu?

---

## Slide 3: Luồng xác thực JWT
**Nội dung chính**:
- 1. App gửi email + mật khẩu → `POST /auth/login`
- 2. API gọi `sp_User_GetByEmail`, so mật khẩu bằng bcrypt
- 3. API trả accessToken (~15 phút) + refreshToken (~7 ngày)
- 4. App lưu token vào SecureStore
- 5. Mỗi request: `Authorization: Bearer <accessToken>`
- 6. Hết hạn → `POST /auth/refresh`

---

## Slide 4: Mật khẩu và token
**Nội dung chính**:
- Mật khẩu băm bằng **bcrypt** ở NestJS, CSDL chỉ lưu `PasswordHash`
- JWT đã ký: server kiểm tra chữ ký, không cần tra CSDL mỗi request
- Access token ngắn hạn → giảm thiệt hại khi bị lộ
- Refresh token lưu (dạng băm) qua thủ tục để thu hồi khi đăng xuất

---

## Slide 5: Bảng Users và thủ tục đăng ký
**Nội dung chính**:
```sql
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
```
- Cột `Role` có `CHECK (Role IN (N'customer', N'staff'))`

---

## Slide 6: Đăng nhập trong NestJS
**Nội dung chính**:
```ts
const [user] = await this.db.execute<UserRow>('sp_User_GetByEmail', {
  Email: { type: sql.NVarChar(255), value: email },
});
if (!user || !(await bcrypt.compare(password, user.PasswordHash))) {
  throw new UnauthorizedException('Email hoặc mật khẩu không đúng');
}
const payload = { sub: user.UserId, role: user.Role };
return { accessToken: await this.jwt.signAsync(payload, { expiresIn: '15m' }) };
```

---

## Slide 7: AuthGuard và RolesGuard
**Nội dung chính**:
- AuthGuard đọc header `Bearer`, `verifyAsync`, gán `request.user`
- `@UseGuards(AuthGuard)` cho API cần đăng nhập
- RolesGuard: chỉ `staff` được đổi trạng thái đơn
- Mã người dùng lấy từ token (`req.user.sub`), **không** lấy từ body
**Ghi chú giảng viên**:
- Mã AuthGuard đầy đủ theo mẫu tài liệu NestJS ở mục 2.3 của bài học.

---

## Slide 8: SecureStore và AsyncStorage
**Nội dung chính**:
- **SecureStore**: mã hóa bằng Android Keystore / iOS Keychain → token
- **AsyncStorage**: văn bản thường → thiết lập không nhạy cảm
- Không bao giờ lưu mật khẩu trên điện thoại
```ts
await SecureStore.setItemAsync('accessToken', token);
const token = await SecureStore.getItemAsync('accessToken');
await SecureStore.deleteItemAsync('accessToken');
```

---

## Slide 9: Bảo vệ màn hình bằng Redirect
**Nội dung chính**:
```tsx
export default function TabLayout() {
  const { token, ready } = useAuth();
  if (!ready) return null;
  if (!token) return <Redirect href="/login" />;
  return <Tabs>{/* các tab */}</Tabs>;
}
```
- Cờ `ready` tránh nháy về màn hình đăng nhập khi mở app
- Đăng nhập xong: `router.replace('/')`

---

## Slide 10: Rủi ro bảo mật thường gặp
**Nội dung chính**:
- Khóa bí mật trong biến `EXPO_PUBLIC_` → đọc được từ APK
- Chỉ ẩn nút ở app, API không kiểm tra quyền
- `console.log` token, mật khẩu
- API dùng tài khoản `sa`
- Thông báo lỗi tiết lộ "email không tồn tại"
**Hoạt động**: Mỗi nhóm rà phần xác thực của mình theo 5 dòng này

---

## Slide 11: Tài khoản SQL Server chỉ có quyền EXECUTE
**Nội dung chính**:
```sql
CREATE LOGIN lhufood_api WITH PASSWORD = '<mật khẩu mạnh>';
CREATE USER lhufood_api FOR LOGIN lhufood_api;
GRANT EXECUTE ON SCHEMA::dbo TO lhufood_api;
```
- API không đọc/ghi bảng trực tiếp, chỉ chạy được thủ tục
**Ghi chú giảng viên**:
- Bài 11 tạo tài khoản này trên Windows Server của Khoa.

---

## Slide 12: Thực hành có hướng dẫn
**Nội dung chính**:
- Bảng Users, thủ tục; tài khoản SQL chỉ có quyền EXECUTE
- NestJS: `/auth/register`, `/auth/login`, AuthGuard cho `POST /orders`
- App: màn hình Đăng nhập/Đăng ký, store auth với SecureStore
- Redirect cho nhóm (tabs); `lib/api.ts` gắn header Authorization; Đăng xuất

---

## Slide 13: Thực hành không hướng dẫn
**Nội dung chính**:
- API trả 401 → gọi `/auth/refresh`, lưu token mới, gửi lại request **một lần**
- Refresh thất bại → đăng xuất, báo "Phiên đăng nhập đã hết hạn"
- Thử bằng access token hết hạn sau 1 phút

---

## Slide 14: Checkpoint Sprint 2
**Nội dung chính**:
- Luồng nghiệp vụ chính chạy với dữ liệu thật, có đăng nhập và phân quyền
- Demo trên Android + Sprint Review và Retrospective
- **Mỗi thành viên**: bản nháp báo cáo vai trò cá nhân + tự trình bày 2 phút
- Nộp `PROMPTS.md` của sprint 2
**Ghi chú giảng viên**:
- Góp ý báo cáo vai trò để sinh viên hoàn thiện cho phần chấm CLO4 cuối kỳ.

---

## Slide 15: Tóm tắt
**Nội dung chính**:
- Mật khẩu băm ở backend; CSDL chỉ lưu hash; mọi truy cập qua thủ tục
- Access token ngắn, refresh token dài; token lưu ở SecureStore
- Kiểm tra quyền ở API, không chỉ ẩn nút ở app
- Bí mật không bao giờ nằm trong ứng dụng
**Hoạt động**: Làm quiz Bài 06 ở cuối trang bài học

---

## Slide 16: Tài liệu của buổi
**Đọc thêm**:
- Giáo trình nội bộ, Chương 6: Xác thực và bảo mật ứng dụng
- Bài tập hướng dẫn theo dự án LHU Food (cuối Chương 6)
- SRS LHU Food: mục 5.2 (F01.1–F01.5), 4.7, BR-01…BR-06
- Kế hoạch Agile & Product Backlog (Definition of Done, tiêu chí nghiệm thu)
**Ghi chú giảng viên**:
- Các file Word/Excel nằm ở mục Tài liệu của bài trên LMS và trang học phần (giao-trinh/, srs/, rubric/).
