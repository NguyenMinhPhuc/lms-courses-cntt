# 3. Actor và hành vi

## 3.1. Danh sách actor

| Mã | Actor | Loại | Mô tả | Nền tảng | Vai trò trong hệ thống (`Role`) |
|---|---|---|---|---|---|
| A1 | Khách vãng lai (Guest) | Người | Người chưa đăng nhập, muốn xem thực đơn | Mobile, Web | Không có token |
| A2 | Khách hàng (Customer) | Người | Sinh viên, cán bộ đã có tài khoản, đặt món để nhận tại quầy | Mobile (chính), Web | `customer` |
| A3 | Nhân viên căn tin (Staff) | Người | Nhận và chuẩn bị đơn, cập nhật trạng thái, quản lý món hết hàng | Mobile, Web | `staff` |
| A4 | Quản lý căn tin (Admin) | Người | Quản trị thực đơn, quầy, tài khoản nhân viên; xem báo cáo | Web | `admin` |
| A5 | Hệ thống thông báo | Hệ thống | Gateway Socket.IO trong backend, gửi sự kiện tới đúng room | Backend | Không áp dụng |
| A6 | Dịch vụ bản đồ | Hệ thống ngoài | Google Maps (Android) / Apple Maps (iOS) hiển thị bản đồ quầy | Mobile | Không áp dụng |

Quan hệ kế thừa: Khách hàng có mọi hành vi của Khách vãng lai. Quản lý căn tin có mọi hành vi của Nhân viên căn tin.

Ghi chú về vai trò `admin`: giáo trình (Chương 6) khai báo `Role IN (N'customer', N'staff')`. Nhóm làm ứng dụng web bổ sung giá trị `admin` bằng một script mới (ví dụ `database/10-admin-role.sql`) sửa ràng buộc `CHECK`, theo quy tắc "thêm file mới, không sửa file cũ" (Chương 7).

## 3.2. Hành vi của từng actor

### 3.2.1. A1 - Khách vãng lai

| Hành vi | Mô tả | Nền tảng |
|---|---|---|
| Xem thực đơn | Duyệt món theo danh mục, xem giá, ảnh, trạng thái còn/hết | M+W |
| Tìm món | Nhập tên món, lọc danh sách | M+W |
| Xem chi tiết món | Mô tả, giá, ảnh lớn, số suất còn | M+W |
| Xem quầy | Danh sách quầy và vị trí trên bản đồ | M |
| Đăng ký | Tạo tài khoản khách hàng bằng họ tên, email, mật khẩu | M+W |
| Đăng nhập | Đăng nhập bằng email và mật khẩu, nhận token | M+W |

Khi khách vãng lai bấm "Thêm vào giỏ" hoặc "Đặt món", ứng dụng chuyển tới màn hình Đăng nhập, sau khi đăng nhập thì quay lại màn hình trước đó.

Ghi chú hiện thực trên mobile: Chương 6 bảo vệ toàn bộ nhóm `(tabs)` bằng `Redirect` (phải đăng nhập mới vào ứng dụng) để đơn giản. Đó là mức tối thiểu chấp nhận được. Mức đầy đủ của SRS (khách vãng lai xem được thực đơn, chỉ chặn ở Giỏ hàng, Đơn hàng, Tài khoản) là bước nâng cao trong bài tập hướng dẫn Chương 6. Ứng dụng web nên làm theo mức đầy đủ.

### 3.2.2. A2 - Khách hàng

| Hành vi | Mô tả | Nền tảng |
|---|---|---|
| Quản lý giỏ hàng | Thêm, tăng giảm, xóa món; xem tổng tiền; giỏ được giữ khi tắt ứng dụng | M+W |
| Đặt món | Gửi giỏ hàng kèm ghi chú và quầy nhận; nhận mã đơn | M+W |
| Theo dõi đơn | Xem lịch sử, chi tiết, trạng thái hiện tại của đơn | M+W |
| Hủy đơn | Hủy đơn của mình khi đơn còn `pending` | M+W |
| Nhận thông báo | Nhận thông báo realtime khi trạng thái đơn thay đổi; xem danh sách thông báo | M (bắt buộc), W (tùy chọn) |
| Yêu thích | Đánh dấu, bỏ đánh dấu, xem danh sách món yêu thích | M+W |
| Quản lý hồ sơ | Xem thông tin, đổi ảnh đại diện (camera hoặc thư viện ảnh), đăng xuất | M (ảnh), M+W (còn lại) |
| Tìm quầy | Xem quầy trên bản đồ, quầy gần vị trí hiện tại | M |
| Đánh giá món (mở rộng) | Chấm sao, viết nhận xét, đính kèm ảnh cho món đã nhận | M |

### 3.2.3. A3 - Nhân viên căn tin

| Hành vi | Mô tả | Nền tảng |
|---|---|---|
| Đăng nhập chế độ nhân viên | Cùng màn hình đăng nhập; giao diện theo vai trò `staff` | M+W |
| Nhận đơn mới | Danh sách đơn mới tự cập nhật khi có đơn (`order:new`), có âm báo | M+W |
| Cập nhật trạng thái đơn | `pending → preparing → ready → completed` | M+W |
| Từ chối/hủy đơn | Hủy đơn không phục vụ được, kèm lý do | W |
| Quản lý món trong ngày | Bật/tắt "còn bán"; cập nhật số suất tồn kho | M (bật/tắt), W (đầy đủ) |
| Xem báo cáo nhanh | Doanh thu hôm nay, món bán chạy | M+W |

### 3.2.4. A4 - Quản lý căn tin

| Hành vi | Mô tả | Nền tảng |
|---|---|---|
| Quản lý danh mục | Thêm, sửa, xóa (khi chưa có món), sắp xếp danh mục | W |
| Quản lý món | Thêm, sửa, ngừng bán món; tải ảnh món | W |
| Quản lý quầy | Thêm, sửa quầy và tọa độ | W |
| Quản lý tài khoản nhân viên | Tạo tài khoản `staff`, khóa/mở khóa, đặt lại mật khẩu | W |
| Xem báo cáo | Doanh thu theo khoảng ngày, món bán chạy, số đơn theo trạng thái | W |
| Theo dõi hệ thống | Xem tình trạng API (`/health`) | W |

### 3.2.5. A5 - Hệ thống thông báo

| Hành vi | Khi nào | Gửi tới |
|---|---|---|
| Xác thực kết nối | Client kết nối kèm access token trong `auth` | - |
| Đưa kết nối vào room | Sau khi xác thực | `user:<userId>`; thêm `staff` nếu vai trò là `staff`/`admin` |
| Gửi `order:new` | Sau khi `sp_Order_Create` thành công | Room `staff` |
| Gửi `order:status` | Sau khi `sp_Order_UpdateStatus` hoặc hủy đơn thành công, và đã lưu thông báo | Room `user:<userId>` của chủ đơn |
| Gửi `product:availability` (mở rộng) | Khi món được bật/tắt còn bán | Mọi client đang xem thực đơn |

### 3.2.6. A6 - Dịch vụ bản đồ

Cung cấp bản đồ nền, ghim (marker) vị trí quầy và vị trí người dùng. Trên Android bản build cần Google Maps API key (Chương 8, Chương 11). Hệ thống không gửi dữ liệu cá nhân của người dùng cho dịch vụ bản đồ ngoài những gì thư viện bản đồ cần để hiển thị.

## 3.3. Sơ đồ use case tổng quát

```text
                 ┌──────────────────── LHU Food ────────────────────┐
 Khách vãng lai ─┤ Xem thực đơn · Tìm món · Xem chi tiết · Xem quầy  │
       │         │ Đăng ký · Đăng nhập                               │
       ▼ (kế thừa)                                                   │
  Khách hàng ────┤ Giỏ hàng · Đặt món · Theo dõi đơn · Hủy đơn       │
                 │ Thông báo · Yêu thích · Hồ sơ, ảnh · Đánh giá     │
 Nhân viên ──────┤ Nhận đơn mới · Cập nhật trạng thái · Món hết hàng │
       ▼ (kế thừa)│ Báo cáo nhanh                                    │
  Quản lý ───────┤ Quản lý danh mục, món, quầy, nhân viên · Báo cáo  │
                 └──────────────────────────────────────────────────┘
  Hệ thống thông báo (Socket.IO) ── gửi order:new, order:status
  Dịch vụ bản đồ ── hiển thị quầy, vị trí
```

Nhóm vẽ lại sơ đồ use case bằng công cụ đồ họa (draw.io) cho đề tài của mình; đây là một phần minh chứng CLO3.
