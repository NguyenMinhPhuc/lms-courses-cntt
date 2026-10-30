# Bài 08: Trang quản trị: CRUD, tải ảnh, báo cáo & biểu đồ
Sprint 3 · Quản trị & Realtime

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Trang quản trị CRUD theo một mẫu thống nhất
- Tải ảnh món có kiểm tra định dạng, dung lượng
- Báo cáo bằng biểu đồ, xuất CSV
- Kiểm thử ràng buộc nghiệp vụ quản trị
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1, CLO2.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Quản lý không mở SSMS, không đọc JSON
- Thêm món kèm ảnh trong một phút
- Nhìn biểu đồ là hiểu, bấm nút là có file Excel

---

## Slide 3: Mẫu trang CRUD
**Nội dung chính**:
```text
app/admin/products/
  page.tsx            danh sách
  new/page.tsx        tạo mới
  [id]/edit/page.tsx  sửa
  product-form.tsx    form dùng chung
  actions.ts          Server Actions
```

---

## Slide 4: saveProduct
**Nội dung chính**:
- Một action cho tạo và sửa: saveProduct.bind(null, id)
- requireRole('admin'), safeParse, fieldErrors
- revalidatePath('/admin/products') và '/menu'
- Không có nút Xóa món: chỉ ngừng bán (BR-16)

---

## Slide 5: Hộp thoại xác nhận
**Nội dung chính**:
- Thao tác không hoàn tác: xóa danh mục, khóa tài khoản
- AlertDialog ghi rõ hậu quả
- Thông báo ngắn sau khi lưu
**Hoạt động**: Liệt kê các thao tác cần xác nhận trong trang quản trị của nhóm

---

## Slide 6: Luồng tải ảnh
**Nội dung chính**:
```text
Trình duyệt ─FormData─▶ Server Action ─multipart─▶ API (Multer, trường "file")
                        kiểm tra loại, dung lượng      lưu file, sp_Product_UpdateImage
```

---

## Slide 7: uploadProductImage
**Nội dung chính**:
- Chỉ nhận JPG, PNG, WEBP; tối đa 2 MB
- Không tự đặt Content-Type: fetch tự sinh boundary
- serverActions.bodySizeLimit (mặc định 1 MB)
- images.remotePatterns cho next/image

---

## Slide 8: Xem trước và kiểm tra ba lớp
**Nội dung chính**:
- URL.createObjectURL để xem trước, revokeObjectURL khi đổi
- accept trên input: tiện cho người dùng
- Server Action: chặn sớm; API: chặn thật
- Không tin phần mở rộng tên file

---

## Slide 9: Trang báo cáo
**Nội dung chính**:
- Khoảng ngày trong URL: ?from=…&to=…
- Server Component gọi 3 API cùng lúc
- from > to: báo lỗi, không gọi API
- Biểu đồ là Client Component (Recharts)

---

## Slide 10: Chọn biểu đồ theo câu hỏi
**Nội dung chính**:
- Doanh thu theo ngày: cột hoặc đường
- Món bán chạy: cột ngang, giảm dần
- Tỉ lệ trạng thái: cột chồng 100% hoặc bảng phần trăm
- Một màu một chuỗi; có tiêu đề, đơn vị, bảng số liệu

---

## Slide 11: Xuất CSV
**Nội dung chính**:
- Route Handler GET /admin/reports/export
- requireRole('admin') dù đã có proxy
- BOM ﻿: Excel đọc đúng tiếng Việt
- Content-Disposition: attachment

---

## Slide 12: Tài khoản nhân viên (US-A04)
**Nội dung chính**:
- Danh sách lọc vai trò, tìm kiếm, phân trang URL
- Tạo staff: mật khẩu băm ở backend, không hiển thị lại
- Khóa/mở khóa có xác nhận; trạng thái bằng chữ

---

## Slide 13: Test case quản trị (CLO2)
**Nội dung chính**:
- TC-41 xóa danh mục còn món → 409
- TC-43 PDF đổi tên .jpg → từ chối
- TC-45 doanh thu web = SELECT SUM trên CSDL
- TC-47 khóa nhân viên đang đăng nhập → không làm mới token được
- TC-49 CSV mở Excel đúng dấu

---

## Slide 14: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: quản lý món + ảnh, báo cáo doanh thu, xuất CSV
- **Không hướng dẫn**: trang /admin/users, TC-47, TC-48
- **Nhóm**: hoàn thiện trang quản trị, mỗi ràng buộc một test case

---

## Slide 15: Tổng kết
**Nội dung chính**:
- Một mẫu CRUD cho mọi trang quản trị
- Ảnh: kiểm tra ba lớp, không tự đặt Content-Type
- Biểu đồ trả lời câu hỏi, số liệu khớp CSDL
- Buổi sau: màn hình quầy realtime, Checkpoint Sprint 3

---

## Slide 16: Tài liệu của buổi
**Đọc thêm**:
- SRS LHU Food: US-A01, A02, A04, A05, A06; BR-16; mục 8
- Next.js: serverActions, Route Handlers
- Recharts Guide; shadcn/ui Alert Dialog
**Ghi chú giảng viên**:
- Chuẩn bị sẵn một file PDF đổi tên .jpg và một ảnh 2,5 MB để demo TC-43, TC-44.
