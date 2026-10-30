# Bài 07: Module quản trị trên backend của nhóm
Sprint 3 · Quản trị & Realtime

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Phân tích nghiệp vụ quản trị thành CSDL, thủ tục, API
- Script CSDL phiên bản mới, chạy lại an toàn
- API quản trị có phân quyền admin, Swagger
- Chuyển web sang backend nhóm, kiểm thử hồi quy
**Ghi chú giảng viên**:
- 2 tiết lý thuyết, 3 tiết thực hành. CLO1. Từ buổi này nhóm không dùng API mẫu nữa.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Hai sprint đầu web sống nhờ API mẫu
- Backend đồ án di động chưa biết "quản lý" là ai
- Việc đầu tiên: tìm xem backend còn thiếu gì

---

## Slide 3: Năm tầng của một story quản trị
**Nội dung chính**:
- Story → dữ liệu → stored procedure → API → trang web
- US-A01 danh mục: Categories → sp_Category_* → /admin/categories
- US-A04 tài khoản: Users (Role, IsLocked) → sp_User_SetLocked → /admin/users/:id/lock
**Hoạt động**: Nhóm điền bảng 5 tầng cho các story quản trị của đề tài

---

## Slide 4: Khoảng trống của backend hiện tại
**Nội dung chính**:
- Role chỉ có customer, staff: thiếu admin
- Chưa có cột khóa tài khoản
- Chưa có thủ tục thêm, sửa, xóa danh mục
- Counters thiếu mô tả, trạng thái hoạt động

---

## Slide 5: Script phiên bản mới
**Nội dung chính**:
- Không sửa file đã chạy, thêm file mới
- Giáo trình di động dùng 01–09 → web dùng 20-admin.sql
- Kiểm tra trước: COL_LENGTH, OBJECT_ID
- Chạy hai lần liên tiếp không lỗi

---

## Slide 6: Mở rộng vai trò và khóa tài khoản
**Nội dung chính**:
```sql
IF OBJECT_ID('dbo.CK_Users_Role') IS NULL ...
  ADD CONSTRAINT CK_Users_Role
  CHECK (Role IN (N'customer', N'staff', N'admin'));
IF COL_LENGTH('dbo.Users', 'IsLocked') IS NULL
  ALTER TABLE dbo.Users ADD IsLocked BIT NOT NULL DEFAULT 0;
```

---

## Slide 7: Thủ tục có ràng buộc
**Nội dung chính**:
```sql
IF EXISTS (SELECT 1 FROM dbo.Products WHERE CategoryId = @CategoryId)
  THROW 50409, N'Danh mục còn món, không xóa được', 1;
```
- Món đã bán chỉ ngừng bán (BR-16)
- Không tự khóa chính mình (50400)
- Khóa thì thu hồi refresh token

---

## Slide 8: Mã lỗi thống nhất
**Nội dung chính**:
- 50400 → 400: dữ liệu sai nghiệp vụ
- 50404 → 404: không tìm thấy
- 50409 → 409: xung đột, trùng
- Đặt ở thủ tục: web, mobile, Swagger đều bị kiểm tra như nhau

---

## Slide 9: API quản trị NestJS
**Nội dung chính**:
```ts
@Controller('admin/categories')
@UseGuards(AuthGuard, RolesGuard)
@Roles(['admin'])
export class AdminCategoriesController { ... }
```
- DTO + class-validator, ApiProperty cho Swagger

---

## Slide 10: Phân quyền admin
**Nội dung chính**:
- RolesGuard so khớp đúng tên vai trò
- Route nhân viên: @Roles(['staff', 'admin'])
- @Roles trên controller: getAllAndOverride
- Mã người thực hiện lấy từ token, không từ body

---

## Slide 11: Khóa tài khoản trong AuthService
**Nội dung chính**:
- sp_User_GetByEmail trả thêm IsLocked
- Đăng nhập khi bị khóa → 403
- Làm mới token cũng kiểm tra lại
- Tài khoản admin đầu tiên: script seed, mật khẩu đã băm

---

## Slide 12: So khớp hợp đồng API
**Nội dung chính**:
- Đường dẫn, tham số, kiểu trả về, tên trường, mã lỗi
- Ví dụ: lat/lng so với latitude/longitude
- Ưu tiên sửa backend (mobile cũng dùng)
- Hoặc hàm chuyển đổi trong lib/api.ts

---

## Slide 13: Kiểm thử hồi quy
**Nội dung chính**:
- Đổi API_URL là bước cuối
- Chạy lại TC Sprint 1–2 trên backend nhóm
- Trước đạt, giờ trượt = lỗi hồi quy → thẻ trên board
- Ghi cột "Kết quả trên backend nhóm"

---

## Slide 14: Lỗi AI hay mắc
**Nội dung chính**:
- Viết SQL ghép chuỗi trong controller thay vì gọi thủ tục
- Sửa file script cũ thay vì thêm file mới
- Dùng RAISERROR hoặc mã lỗi lạ → 500 thay vì 409
- Lấy userId từ body

---

## Slide 15: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: 20-admin.sql, AdminCategoriesController, trang /admin/categories
- **Không hướng dẫn**: thủ tục + API quản lý quầy, 4 lần gọi kiểm tra
- **Nhóm**: bảng 5 tầng, ERD quản trị, danh mục thủ tục, chuyển web sang backend nhóm

---

## Slide 16: Tổng kết
**Nội dung chính**:
- Phân tích khoảng trống trước khi code
- Ràng buộc nghiệp vụ nằm trong thủ tục
- Phân quyền admin ở API, Swagger là hợp đồng
- Buổi sau: trang quản trị CRUD, ảnh, báo cáo

---

## Slide 17: Tài liệu của buổi
**Đọc thêm**:
- SRS LHU Food: F09.3, F10, F11; US-A01…A04; BR-16; mục 8
- Giáo trình di động: Chương 5 (DatabaseService), 6 (RolesGuard), 7 (script phiên bản)
- NestJS: Authorization, OpenAPI; Microsoft Learn: THROW
**Ghi chú giảng viên**:
- Kiểm tra mỗi nhóm đã có backend chạy được trước buổi học; nhóm chưa có thì ghép tạm với API mẫu và lập kế hoạch bù.
