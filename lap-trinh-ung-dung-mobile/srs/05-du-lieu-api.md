# 6. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nơi kiểm tra |
|---|---|---|
| BR-01 | Email là duy nhất trong hệ thống | Ràng buộc `UNIQUE`, `sp_User_Register` (50409) |
| BR-02 | Mật khẩu tối thiểu 8 ký tự, lưu dạng băm bcrypt | Zod (app), DTO và bcrypt (API) |
| BR-03 | Đăng nhập sai chỉ báo một thông báo chung, không tiết lộ email có tồn tại hay không | AuthService |
| BR-04 | Access token hết hạn sau 15 phút; refresh token dài hạn, được xoay vòng mỗi lần dùng và thu hồi khi đăng xuất | AuthService, `sp_RefreshToken_*` |
| BR-05 | Tài khoản bị khóa không đăng nhập và không làm mới token được | `sp_User_GetByEmail`, `sp_RefreshToken_Use` |
| BR-06 | Mã người dùng luôn lấy từ token (`req.user.sub`), không lấy từ body hay query | Controller |
| BR-07 | Giỏ hàng chỉ là ý định mua; giá và tồn kho được server kiểm tra lại khi đặt | `sp_Order_Create` |
| BR-08 | Giá trong đơn là giá tại thời điểm đặt (`OrderItems.UnitPrice`) | `sp_Order_Create` |
| BR-09 | Không đặt món ngừng bán hoặc vượt tồn kho; đặt hàng là một giao dịch, lỗi thì không lưu gì | `sp_Order_Create` (50409) |
| BR-10 | Số lượng mỗi món > 0; món trùng trong một đơn được gộp | `sp_Order_Create` (50400) |
| BR-11 | Khách chỉ hủy đơn của mình khi đơn `pending`; hủy thì hoàn tồn kho | `sp_Order_Cancel` (50409) |
| BR-12 | Ứng dụng chỉ xin quyền camera, vị trí, thông báo khi người dùng dùng tính năng cần quyền đó, và vẫn chạy được khi bị từ chối | Ứng dụng |
| BR-13 | Ảnh tải lên chỉ nhận định dạng ảnh, dung lượng có giới hạn; CSDL chỉ lưu đường dẫn | `FileInterceptor`, thủ tục |
| BR-14 | Thông báo được lưu vào SQL Server trước, rồi mới gửi qua socket | Service đơn hàng |
| BR-15 | Trạng thái đơn chỉ chuyển theo sơ đồ ở mục 6.1 | `sp_Order_UpdateStatus` (50409) |
| BR-16 | Món đã xuất hiện trong đơn không bị xóa hẳn, chỉ ngừng bán | Thủ tục quản trị |
| BR-17 | Báo cáo doanh thu không tính đơn `cancelled` | `sp_Report_*` |

## 6.1. Sơ đồ trạng thái đơn hàng

```text
            đặt món (khách)
                 │
                 ▼
          ┌─────────────┐  khách hủy / nhân viên hủy (W)  ┌─────────────┐
          │   pending   │ ───────────────────────────────▶│  cancelled  │
          └──────┬──────┘                                  └─────────────┘
   nhân viên nhận │
                 ▼
          ┌─────────────┐
          │  preparing  │
          └──────┬──────┘
   nhân viên báo  │ xong
                 ▼
          ┌─────────────┐
          │    ready    │ ── gửi thông báo "Đơn đã sẵn sàng"
          └──────┬──────┘
   khách nhận món │
                 ▼
          ┌─────────────┐
          │  completed  │
          └─────────────┘
```

Mỗi mũi tên tạo một bản ghi `Notifications` cho chủ đơn và một sự kiện `order:status`.

# 7. Dữ liệu

## 7.1. Các bảng

| Bảng | Cột chính | Ghi chú | Chương |
|---|---|---|---|
| Categories | CategoryId, Name | Tên duy nhất | 5 |
| Products | ProductId, CategoryId, Name, Description, Price, ImageUrl, IsAvailable, Stock | `Price >= 0`, `Stock >= 0` | 5, 7 |
| Users | UserId, FullName, Email, PasswordHash, Role, AvatarUrl, CreatedAt | `Role`: customer, staff (+ admin cho web); `IsLocked` (đề xuất) | 6, 8 |
| RefreshTokens | TokenId, UserId, TokenHash (SHA-256), ExpiresAt, RevokedAt | Xoay vòng, thu hồi | 6 |
| Orders | OrderId, UserId, Status, Note, CreatedAt; CounterId (đề xuất) | `CHECK` trạng thái | 5, 7 |
| OrderItems | OrderId, ProductId, Quantity, UnitPrice | Khóa chính (OrderId, ProductId) | 5 |
| Favorites | UserId, ProductId, CreatedAt | Khóa chính kép | 7 |
| Counters | CounterId, Name, Latitude, Longitude | `CHECK` tọa độ | 8 |
| Notifications | NotificationId, UserId, Title, Body, OrderId, IsRead, CreatedAt | Chỉ mục (UserId, IsRead, CreatedAt) | 9 |
| Reviews (mở rộng) | ReviewId, OrderId, ProductId, UserId, Rating, Comment, ImageUrl, CreatedAt | `Rating` 1–5, mỗi món/đơn một lần | 8 (mở rộng) |

## 7.2. Quan hệ

```text
Categories 1 ──< Products >── OrderItems >── 1 Orders >── 1 Users
                    │                          │             │
                    └──< Favorites >── Users   │             ├──< RefreshTokens
                    └──< Reviews  (mở rộng)    │             └──< Notifications
                                               └── Counters (mở rộng: Orders.CounterId)
```

ERD chính thức của nhóm vẽ bằng công cụ đồ họa và phải khớp CSDL thật trên server (Chương 12).

## 7.3. Script CSDL

| File | Nội dung | Chương |
|---|---|---|
| `01-tables.sql` | Categories, Products, Orders, OrderItems | 5 |
| `02-procedures.sql` | Thủ tục sản phẩm, đơn hàng | 5 |
| `03-auth.sql` | Users, RefreshTokens, thủ tục xác thực | 6 |
| `04-stock-reports.sql` | Tồn kho, ràng buộc, chỉ mục, giao dịch, báo cáo | 7 |
| `05-favorites.sql` | Favorites | 7 |
| `06-avatar.sql` | Users.AvatarUrl | 8 |
| `07-counters.sql` | Counters | 8 |
| `08-notifications.sql` | Notifications, cập nhật trạng thái đơn | 9 |
| `09-health.sql` | `sp_Health_Check` | 11 |
| `10-...sql` trở đi | Phần mở rộng của nhóm (quầy nhận, đánh giá, admin…) | Nhóm |
| `99-seed.sql` | Dữ liệu mẫu | 5, 7 |
| `tests/*.sql` | Kịch bản kiểm thử thủ tục, không chạy trên server thật | 10 |

# 8. Danh mục API

Tất cả API trả JSON. Lỗi nghiệp vụ: 400 (`50400`), 404 (`50404`), 409 (`50409`); chưa đăng nhập 401; sai vai trò 403. Tài liệu Swagger tại `/docs`.

| Phương thức và đường dẫn | Mô tả | Quyền | Thủ tục | Chức năng |
|---|---|---|---|---|
| `POST /auth/register` | Đăng ký | Công khai | `sp_User_Register` | F01.1 |
| `POST /auth/login` | Đăng nhập | Công khai | `sp_User_GetByEmail`, `sp_RefreshToken_Save` | F01.2 |
| `POST /auth/refresh` | Làm mới token | Công khai (refresh token) | `sp_RefreshToken_Use` | F01.3 |
| `POST /auth/logout` | Đăng xuất | Đăng nhập | `sp_RefreshToken_Revoke` | F01.4 |
| `GET /categories` | Danh mục | Công khai | `sp_Category_GetList` | F02.1 |
| `GET /products` | Danh sách món | Công khai | `sp_Product_GetList` | F02.2, F02.3 |
| `GET /products/:id` | Chi tiết món | Công khai | `sp_Product_GetById` | F02.4 |
| `POST /orders` | Đặt món | customer | `sp_Order_Create` | F04.1 |
| `GET /orders` | Lịch sử đơn của tôi | customer | `sp_Order_GetHistory` | F04.2 |
| `GET /orders/:id` | Chi tiết đơn | customer (của mình), staff | `sp_Order_GetById` | F04.3 |
| `POST /orders/:id/cancel` | Hủy đơn | customer | `sp_Order_Cancel` | F04.4 |
| `GET /favorites` | Danh sách yêu thích | customer | `sp_Favorite_GetList` | F05.2 |
| `POST /favorites/:productId` | Thêm yêu thích | customer | `sp_Favorite_Add` | F05.1 |
| `DELETE /favorites/:productId` | Bỏ yêu thích | customer | `sp_Favorite_Remove` | F05.1 |
| `GET /counters` | Danh sách quầy | Công khai | `sp_Counter_GetList` | F06.1 |
| `POST /users/me/avatar` | Đổi ảnh đại diện | Đăng nhập | `sp_User_UpdateAvatar` | F07.2 |
| `GET /notifications` | Danh sách thông báo | Đăng nhập | `sp_Notification_GetList` | F08.3 |
| `GET /notifications/unread-count` | Số chưa đọc | Đăng nhập | `sp_Notification_CountUnread` | F08.3 |
| `POST /notifications/:id/read` | Đánh dấu đã đọc | Đăng nhập | `sp_Notification_MarkRead` | F08.3 |
| `GET /orders/staff` | Đơn cần xử lý | staff | `sp_Order_GetListForStaff` | F09.1 |
| `PATCH /orders/:id/status` | Đổi trạng thái đơn | staff | `sp_Order_UpdateStatus` | F09.2 |
| `PATCH /products/:id/availability` | Bật/tắt còn bán | staff | `sp_Product_SetAvailability` | F09.3 |
| `PATCH /products/:id/stock` | Cập nhật tồn kho | staff | `sp_Product_UpdateStock` | F09.3 |
| `GET /reports/revenue` | Doanh thu theo ngày | staff, admin | `sp_Report_RevenueByDay` | F10.1 |
| `GET /reports/top-products` | Món bán chạy | staff, admin | `sp_Report_TopProducts` | F10.2 |
| `POST/PUT/DELETE /admin/...` | Quản trị danh mục, món, quầy, nhân viên | admin | `sp_Category_*`, `sp_Product_*`, `sp_Counter_*`, `sp_User_*` | F11 |
| `GET /health` | Kiểm tra sức khỏe | Công khai | `sp_Health_Check` | F12.3 |

**Sự kiện Socket.IO**

| Sự kiện | Hướng | Room | Dữ liệu |
|---|---|---|---|
| `order:new` | Server → client | `staff` | `{ orderId, createdAt, itemCount, total }` |
| `order:status` | Server → client | `user:<userId>` | `{ order: { orderId, status }, notification: { id, title, body } }` |
| `product:availability` (mở rộng) | Server → client | Tất cả | `{ productId, isAvailable, stock }` |

# 9. Yêu cầu phi chức năng

| Mã | Nhóm | Yêu cầu | Cách kiểm tra |
|---|---|---|---|
| NFR-01 | Nền tảng | Chạy trên Android 9 trở lên bằng APK; iOS là mở rộng | Cài APK trên máy người ngoài nhóm |
| NFR-02 | Hiệu năng | Danh sách 200 món cuộn mượt trên máy Android tầm trung; gõ tìm kiếm không giật | Profiler, số liệu trước/sau (Chương 10) |
| NFR-03 | Hiệu năng | API danh sách món phản hồi dưới 1 giây trong mạng Khoa | Swagger, log thời gian |
| NFR-04 | Realtime | Thông báo trạng thái đến điện thoại trong vài giây khi ứng dụng đang mở | Demo hai thiết bị |
| NFR-05 | Bảo mật | Không có bí mật trong mã ứng dụng hay biến `EXPO_PUBLIC_*`; token trong SecureStore; API dùng login SQL chỉ có quyền `EXECUTE` | Review mã, kiểm tra quyền SQL |
| NFR-06 | Toàn vẹn | Không có đơn làm tồn kho âm khi đặt đồng thời | Kịch bản kiểm thử thủ tục (Chương 10) |
| NFR-07 | Khả dụng | Ứng dụng không hiện màn hình đỏ khi mất mạng; có thông báo và nút Thử lại | Kiểm thử thủ công ở chế độ máy bay |
| NFR-08 | Truy cập | Nút chỉ có biểu tượng có `accessibilityLabel`; giao diện không vỡ ở cỡ chữ lớn | TalkBack, cài đặt cỡ chữ |
| NFR-09 | Vận hành | API tự chạy lại khi server khởi động lại; có `/health` và log lỗi | Khởi động lại dịch vụ |
| NFR-10 | Bảo trì | CSDL dựng lại được từ `database/`; README hướng dẫn chạy và triển khai; test chạy bằng `npm test` | Người ngoài nhóm làm theo README |
| NFR-11 | Quy trình | Mỗi PR có prompt chính trong `PROMPTS.md`; người tạo PR giải thích được mã | Review, Demo Day |

# 10. Truy vết và lộ trình

## 10.1. User story theo chương (ứng dụng di động)

| Chương | Sprint | User story bắt buộc trong bài tập hướng dẫn | Mở rộng |
|---|---|---|---|
| 1 | 1 | (Khởi tạo dự án, AGENTS.md, phân vai) | - |
| 2 | 1 | US-G01 (giao diện thực đơn, dữ liệu giả), US-G03 (giao diện chi tiết) | - |
| 3 | 1 | US-G01, US-G03 (điều hướng), khung US-C02, US-C06 | - |
| 4 | 2 | US-C01, US-C02, US-G02, US-G04 (form) | - |
| 5 | 2 | US-G01, US-G03, US-G07, US-C04 (bản đầu), US-C06 | - |
| 6 | 2 | US-G05, US-C13, US-C14, US-S01 | Khách vãng lai xem thực đơn |
| 7 | 3 | US-C04 (giao dịch), US-C08, US-C03, US-C11, US-S04, US-S08 | US-C16 |
| 8 | 3 | US-C12, US-G06 | US-C15, US-C05, US-C17 |
| 9 | 3 | US-C09, US-C10, US-S02, US-S03, US-SYS01, US-SYS02 | US-S06, US-C18 |
| 10 | 4 | Test cho US-C01, US-C02, US-C04, US-SYS03 | - |
| 11 | 4 | US-SYS04, US-SYS05 | - |
| 12 | 4 | Demo toàn bộ story Must | - |

## 10.2. Phần dành cho ứng dụng web

Nhóm làm chung đề tài với học phần Lập trình ứng dụng Web hiện thực trên web: US-A01–A07, US-S05, US-S07 và giao diện web cho các story [M+W]. Backend NestJS và CSDL là **một**; API quản trị bổ sung theo mục 8.

## 10.3. Hướng phát triển

- Thanh toán trực tuyến qua cổng thanh toán; hóa đơn điện tử.
- Push notification khi ứng dụng đã tắt (Expo Notifications, development build).
- Hẹn giờ nhận món theo khung giờ; giới hạn số đơn mỗi khung giờ.
- Gợi ý món dựa trên lịch sử đặt và món yêu thích.
