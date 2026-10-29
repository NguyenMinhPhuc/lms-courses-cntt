# 5. Phân tích module và chức năng

## 5.1. Tổng quan module

| Mã | Module | Mô tả | Actor | Nền tảng | Chương |
|---|---|---|---|---|---|
| M01 | Xác thực và tài khoản | Đăng ký, đăng nhập, làm mới token, đăng xuất, phân quyền theo vai trò | A1–A4 | M+W | 4, 6 |
| M02 | Thực đơn | Danh mục, danh sách món, tìm kiếm, chi tiết món | A1–A4 | M+W | 2–5 |
| M03 | Giỏ hàng | Giỏ hàng phía client, giữ khi tắt ứng dụng | A2 | M+W | 4, 7 |
| M04 | Đơn hàng | Đặt món có giao dịch, lịch sử, chi tiết, hủy đơn | A2, A3 | M+W | 5, 7 |
| M05 | Yêu thích | Đánh dấu, bỏ đánh dấu, danh sách món yêu thích | A2 | M+W | 7 |
| M06 | Quầy, vị trí và bản đồ | Danh sách quầy, bản đồ, vị trí người dùng, quầy gần nhất | A1, A2, A6 | M | 8 |
| M07 | Hồ sơ và tệp ảnh | Hồ sơ người dùng, ảnh đại diện, ảnh món, đánh giá có ảnh | A2, A4 | M (W cho ảnh món) | 8 |
| M08 | Thông báo thời gian thực | Gateway Socket.IO, lưu và hiển thị thông báo, badge | A2, A3, A5 | M (W tùy chọn) | 9 |
| M09 | Vận hành của nhân viên | Màn hình đơn mới, cập nhật trạng thái, món hết hàng, tồn kho | A3 | M+W | 7, 9 |
| M10 | Báo cáo | Doanh thu theo ngày, món bán chạy, thống kê đơn | A3, A4 | M+W | 7 |
| M11 | Quản trị | Quản lý danh mục, món, quầy, tài khoản nhân viên | A4 | W | Web |
| M12 | Hạ tầng và chất lượng | Kiểm thử, health check, log, triển khai, build, cập nhật OTA | Nhóm phát triển | Backend, M | 10, 11 |

Mỗi chức năng dưới đây mô tả: actor và nền tảng, user story liên quan, đầu vào, xử lý, đầu ra, quy tắc nghiệp vụ (mã BR ở mục 6), API, stored procedure và màn hình. Thủ tục đánh dấu "(đề xuất)" chưa có mã mẫu trong giáo trình; sinh viên tự viết theo quy ước Chương 5.

## 5.2. M01 - Xác thực và tài khoản

### F01.1. Đăng ký tài khoản khách hàng

- **Actor / nền tảng:** Khách vãng lai · M+W · **User story:** US-G04
- **Đầu vào:** họ tên (2–100 ký tự), email, mật khẩu (≥ 8 ký tự), nhập lại mật khẩu.
- **Xử lý:**
  1. Ứng dụng kiểm tra form bằng React Hook Form + Zod; lỗi hiển thị dưới từng ô.
  2. Gửi `POST /auth/register`; backend kiểm tra lại bằng DTO (class-validator).
  3. Backend băm mật khẩu bằng bcrypt, gọi `sp_User_Register` với `Role = customer`.
  4. Thủ tục kiểm tra email trùng, báo `THROW 50409` nếu đã tồn tại.
- **Đầu ra:** tài khoản mới; ứng dụng chuyển sang màn hình Đăng nhập (hoặc đăng nhập luôn).
- **Quy tắc:** BR-01, BR-02. Không bao giờ trả `PasswordHash` về client.
- **API / thủ tục:** `POST /auth/register` → `sp_User_Register`.
- **Màn hình:** Mobile `app/register.tsx`; Web trang Đăng ký.

### F01.2. Đăng nhập

- **Actor / nền tảng:** Khách vãng lai, Nhân viên, Quản lý · M+W · **User story:** US-G05, US-S01
- **Đầu vào:** email, mật khẩu.
- **Xử lý:** backend gọi `sp_User_GetByEmail`, so sánh bcrypt; tài khoản bị khóa thì từ chối; tạo access token (15 phút) và refresh token, lưu refresh token qua `sp_RefreshToken_Save`.
- **Đầu ra:** `{ accessToken, refreshToken, user: { userId, fullName, role, avatarUrl } }`. Mobile lưu token bằng SecureStore; web lưu theo hướng dẫn của học phần web.
- **Quy tắc:** BR-03 (thông báo lỗi chung), BR-04.
- **API / thủ tục:** `POST /auth/login` → `sp_User_GetByEmail`, `sp_RefreshToken_Save`.
- **Màn hình:** Mobile `app/login.tsx`; Web trang Đăng nhập.

### F01.3. Giữ đăng nhập và làm mới token

- **Actor / nền tảng:** Khách hàng, Nhân viên · M (W tương tự) · **User story:** US-C14
- **Xử lý:** khi mở ứng dụng, đọc token trong SecureStore; khi API trả 401 thì gọi `POST /auth/refresh` một lần, thủ tục `sp_RefreshToken_Use` kiểm tra và xoay vòng refresh token; thất bại thì đăng xuất.
- **Quy tắc:** BR-04, BR-05.
- **API / thủ tục:** `POST /auth/refresh` → `sp_RefreshToken_Use`, `sp_RefreshToken_Save`.

### F01.4. Đăng xuất

- **Actor / nền tảng:** mọi người dùng đã đăng nhập · M+W · **User story:** US-C13
- **Xử lý:** gọi `POST /auth/logout` để thu hồi refresh token (`sp_RefreshToken_Revoke`); xóa token trong SecureStore, xóa giỏ hàng, ngắt socket, về màn hình Đăng nhập.

### F01.5. Phân quyền theo vai trò

- **Actor / nền tảng:** hệ thống · M+W · **User story:** US-S01, US-A01
- **Xử lý:** `AuthGuard` kiểm tra access token cho mọi endpoint cần đăng nhập; `RolesGuard` với `@Roles(['staff'])` hoặc `@Roles(['admin'])` cho endpoint của nhân viên, quản lý. Ứng dụng dựa vào `role` để chọn bộ tab, nhưng **không** coi đó là lớp bảo vệ duy nhất.
- **Quy tắc:** BR-06 (`userId` luôn lấy từ token, không lấy từ body).

## 5.3. M02 - Thực đơn

### F02.1. Danh sách danh mục

- **Actor / nền tảng:** mọi actor · M+W · **User story:** US-G01
- **Đầu ra:** danh sách `{ categoryId, name }` sắp theo thứ tự hiển thị.
- **API / thủ tục:** `GET /categories` → `sp_Category_GetList`.
- **Màn hình:** thanh danh mục cuộn ngang ở Trang chủ (mobile), menu bên (web).

### F02.2. Danh sách món, lọc theo danh mục, phân trang

- **Actor / nền tảng:** mọi actor · M+W · **User story:** US-G01, US-G07
- **Đầu vào:** `categoryId` (tùy chọn), `page`, `pageSize`.
- **Xử lý:** thủ tục chỉ trả món `IsAvailable = 1` cho khách (nhân viên, quản lý xem được cả món ngừng bán); phân trang `OFFSET/FETCH`; chỉ mục theo `CategoryId` (Chương 7).
- **Đầu ra:** `{ productId, name, price, imageUrl, stock, isAvailable, categoryId }`.
- **API / thủ tục:** `GET /products?categoryId=&page=&pageSize=` → `sp_Product_GetList`.
- **Màn hình:** Mobile `app/(tabs)/index.tsx` (FlatList, kéo để tải lại, cuộn vô hạn); Web trang Thực đơn.

### F02.3. Tìm kiếm món

- **Actor / nền tảng:** mọi actor · M+W · **User story:** US-G02
- **Xử lý:** giai đoạn đầu lọc trên danh sách đã tải (Chương 4); khi dữ liệu lớn, thêm tham số `@Keyword` cho `sp_Product_GetList` dùng `LIKE N'%' + @Keyword + N'%'` (có tham số, không ghép chuỗi trong mã backend).
- **Quy tắc:** chờ người dùng ngừng gõ khoảng 300 ms trước khi gọi API (debounce).

### F02.4. Chi tiết món

- **Actor / nền tảng:** mọi actor · M+W · **User story:** US-G03
- **Đầu vào:** `productId`.
- **Đầu ra:** thông tin món, tồn kho, trạng thái còn bán; món không tồn tại thì 404 (`THROW 50404`).
- **API / thủ tục:** `GET /products/:id` → `sp_Product_GetById`.
- **Màn hình:** Mobile `app/product/[id].tsx`; Web trang chi tiết món.

## 5.4. M03 - Giỏ hàng

### F03.1. Thêm, tăng, giảm, xóa món

- **Actor / nền tảng:** Khách hàng · M+W · **User story:** US-C01, US-C02
- **Xử lý:** store Zustand `useCart` với `add`, `decrease`, `remove`, `clear`, `total`, `count` (Chương 4); cập nhật bất biến.
- **Quy tắc:** BR-07 (giỏ hàng chỉ là ý định mua; server kiểm tra lại giá và tồn kho khi đặt).
- **Màn hình:** nút "Thêm vào giỏ" ở thẻ món và chi tiết món; tab Giỏ hàng có badge số suất.

### F03.2. Giữ giỏ hàng khi tắt ứng dụng

- **Actor / nền tảng:** Khách hàng · M · **User story:** US-C03
- **Xử lý:** middleware `persist` của Zustand với AsyncStorage, chỉ lưu `items` (Chương 7); xóa khi đăng xuất hoặc đặt món thành công.

## 5.5. M04 - Đơn hàng

### F04.1. Đặt món

- **Actor / nền tảng:** Khách hàng · M+W · **User story:** US-C04, US-C05, US-SYS03
- **Đầu vào:** danh sách `{ productId, quantity }`, ghi chú (≤ 200 ký tự), `counterId` (khi làm US-C05).
- **Xử lý:**
  1. Ứng dụng gửi `POST /orders`; `userId` lấy từ token.
  2. `sp_Order_Create` kiểm tra JSON, gộp món trùng, kiểm tra số lượng > 0.
  3. Trong một giao dịch: khóa dòng món (`UPDLOCK, HOLDLOCK`), kiểm tra còn bán và đủ tồn kho; tạo `Orders`, `OrderItems` (lưu `UnitPrice` từ bảng `Products`), trừ `Stock`.
  4. Lỗi bất kỳ thì `ROLLBACK`, ném lại đúng mã lỗi.
  5. Thành công thì backend gửi `order:new` tới room `staff`.
- **Đầu ra:** `{ orderId }`; ứng dụng xóa giỏ, mở chi tiết đơn.
- **Quy tắc:** BR-07, BR-08, BR-09, BR-10.
- **API / thủ tục:** `POST /orders` → `sp_Order_Create`. Mở rộng US-C05: thêm cột `Orders.CounterId` và tham số `@CounterId` (script mới, đề xuất).

### F04.2. Lịch sử đơn hàng

- **Actor / nền tảng:** Khách hàng · M+W · **User story:** US-C06
- **Đầu vào:** `page`, `pageSize`.
- **Đầu ra:** `{ orderId, createdAt, status, total, itemCount }`, mới nhất trước.
- **API / thủ tục:** `GET /orders?page=` → `sp_Order_GetHistory` (đề xuất, bài tập Chương 5).
- **Màn hình:** Mobile `app/(tabs)/orders.tsx` (cuộn vô hạn, kéo để tải lại).

### F04.3. Chi tiết đơn hàng

- **Actor / nền tảng:** Khách hàng (đơn của mình), Nhân viên (mọi đơn) · M+W · **User story:** US-C07
- **Xử lý:** thủ tục trả hai tập kết quả: thông tin đơn và danh sách món; khách xem đơn của người khác thì 404.
- **API / thủ tục:** `GET /orders/:id` → `sp_Order_GetById` (đề xuất).
- **Màn hình:** Mobile `app/order/[id].tsx`; tự cập nhật khi nhận `order:status`.

### F04.4. Hủy đơn

- **Actor / nền tảng:** Khách hàng · M+W · **User story:** US-C08
- **Xử lý:** `sp_Order_Cancel` trong giao dịch: chỉ hủy đơn của chính người dùng và đang `pending`; chuyển `cancelled`, hoàn `Stock`; sau đó lưu thông báo và gửi `order:status`.
- **Quy tắc:** BR-11.
- **API / thủ tục:** `POST /orders/:id/cancel` → `sp_Order_Cancel`.

### F04.5. Đặt lại đơn cũ (mở rộng)

- **Actor / nền tảng:** Khách hàng · M+W · **User story:** US-C16
- **Xử lý:** từ chi tiết đơn, đưa lại các món vào giỏ (chỉ món còn bán, giá theo giá hiện tại); không tạo đơn ngay.

## 5.6. M05 - Yêu thích

### F05.1. Đánh dấu và bỏ đánh dấu

- **Actor / nền tảng:** Khách hàng · M+W · **User story:** US-C11
- **Xử lý:** optimistic update bằng TanStack Query (Chương 7): đổi biểu tượng ngay, lỗi thì hoàn tác.
- **API / thủ tục:** `POST /favorites/:productId` → `sp_Favorite_Add`; `DELETE /favorites/:productId` → `sp_Favorite_Remove`.
- **Quy tắc:** khóa chính `(UserId, ProductId)` chặn trùng; thêm lần hai không lỗi.

### F05.2. Danh sách yêu thích

- **API / thủ tục:** `GET /favorites` → `sp_Favorite_GetList`.
- **Màn hình:** mục Yêu thích trong tab Tài khoản (mobile).

## 5.7. M06 - Quầy, vị trí và bản đồ

### F06.1. Danh sách quầy và bản đồ

- **Actor / nền tảng:** Khách vãng lai, Khách hàng · M · **User story:** US-G06
- **Đầu ra:** `{ id, name, lat, lng }`; bản đồ `react-native-maps` có marker từng quầy.
- **API / thủ tục:** `GET /counters` → `sp_Counter_GetList`.
- **Màn hình:** `app/map.tsx`.

### F06.2. Vị trí hiện tại và quầy gần nhất

- **Actor / nền tảng:** Khách hàng · M · **User story:** US-C15
- **Xử lý:** xin quyền vị trí khi người dùng bấm "Quầy gần tôi" (không xin ngay khi mở ứng dụng); `expo-location` lấy tọa độ; tính khoảng cách (công thức haversine) phía ứng dụng; sắp xếp quầy theo khoảng cách.
- **Quy tắc:** BR-12 (xin quyền đúng lúc, có phương án khi bị từ chối).

### F06.3. Chọn quầy nhận khi đặt món

- **Actor / nền tảng:** Khách hàng · M+W · **User story:** US-C05
- **Xử lý:** màn hình Giỏ hàng có ô chọn quầy (mặc định quầy gần nhất hoặc quầy chọn lần trước, lưu AsyncStorage); gửi `counterId` khi đặt.

## 5.8. M07 - Hồ sơ và tệp ảnh

### F07.1. Xem hồ sơ

- **Actor / nền tảng:** mọi người dùng đã đăng nhập · M+W · **User story:** US-C13
- **Màn hình:** tab Tài khoản: ảnh đại diện, họ tên, email, vai trò; các mục Yêu thích, Thông báo, Đăng xuất.

### F07.2. Đổi ảnh đại diện

- **Actor / nền tảng:** Khách hàng · M · **User story:** US-C12
- **Xử lý:**
  1. Người dùng chọn "Chụp ảnh" hoặc "Chọn từ thư viện"; ứng dụng xin quyền tương ứng.
  2. `expo-image-picker` với `allowsEditing`, `aspect [1, 1]`, `quality 0.6`.
  3. Tải lên `POST /users/me/avatar` dạng `multipart/form-data` (dùng `fetch` trực tiếp, không đặt `Content-Type` thủ công).
  4. Backend lưu file vào `uploads/avatars`, gọi `sp_User_UpdateAvatar` lưu đường dẫn.
- **Quy tắc:** BR-13 (chỉ nhận ảnh, giới hạn dung lượng; CSDL chỉ lưu đường dẫn).

### F07.3. Ảnh món (web)

- **Actor / nền tảng:** Quản lý · W · **User story:** US-A02
- **API / thủ tục:** `POST /products/:id/image` → `sp_Product_UpdateImage`.

### F07.4. Đánh giá món kèm ảnh (mở rộng)

- **Actor / nền tảng:** Khách hàng · M · **User story:** US-C17
- **Xử lý:** chỉ đánh giá món thuộc đơn `completed` của mình, mỗi món trong một đơn một lần; bảng `Reviews` (đề xuất): `ReviewId`, `OrderId`, `ProductId`, `UserId`, `Rating` 1–5, `Comment`, `ImageUrl`, `CreatedAt`.
- **API / thủ tục (đề xuất):** `POST /reviews` → `sp_Review_Create`; `GET /products/:id/reviews` → `sp_Review_GetByProduct`.

## 5.9. M08 - Thông báo thời gian thực

### F08.1. Kết nối và xác thực socket

- **Actor / nền tảng:** Hệ thống thông báo · Backend + M · **User story:** US-SYS01
- **Xử lý:** client kết nối `io(EXPO_PUBLIC_API_URL, { auth: { token } })`; `handleConnection` của Gateway xác thực JWT, sai thì ngắt; đúng thì vào room `user:<id>`, thêm room `staff` với vai trò `staff`/`admin`. Khi token đổi (làm mới, đăng xuất), client kết nối lại.

### F08.2. Tạo và gửi thông báo trạng thái đơn

- **Actor / nền tảng:** Hệ thống thông báo · Backend · **User story:** US-SYS02, US-C09
- **Xử lý:** sau `sp_Order_UpdateStatus` (trả `userId` chủ đơn), gọi `sp_Notification_Create`, rồi `emit('order:status', { order, notification })` tới room `user:<userId>`.
- **Quy tắc:** BR-14 (lưu trước, gửi sau).

### F08.3. Hiển thị thông báo trong ứng dụng

- **Actor / nền tảng:** Khách hàng · M · **User story:** US-C09, US-C10, US-C18
- **Xử lý:** hook `useRealtime` nhận sự kiện, làm mới cache (`invalidateQueries`), hiện thông báo cục bộ bằng `expo-notifications`; bấm thông báo mở `/order/<id>`; làm mới danh sách khi kết nối lại.
- **API / thủ tục:** `GET /notifications?page=` → `sp_Notification_GetList`; `GET /notifications/unread-count` → `sp_Notification_CountUnread`; `POST /notifications/:id/read` → `sp_Notification_MarkRead`.
- **Màn hình:** tab Thông báo có badge.

## 5.10. M09 - Vận hành của nhân viên

### F09.1. Danh sách đơn cần xử lý

- **Actor / nền tảng:** Nhân viên · M+W · **User story:** US-S02, US-S06
- **Xử lý:** tải đơn `pending`, `preparing`, `ready` trong ngày; lọc theo trạng thái; nhận `order:new` thì thêm vào đầu danh sách và phát âm báo (thông báo cục bộ).
- **API / thủ tục:** `GET /orders/staff?status=` → `sp_Order_GetListForStaff` (đề xuất), `@Roles(['staff'])`.
- **Màn hình:** Mobile tab "Đơn mới" (`app/(staff)/orders.tsx`); Web màn hình quầy dạng bảng hoặc cột theo trạng thái.

### F09.2. Cập nhật trạng thái đơn

- **Actor / nền tảng:** Nhân viên · M+W · **User story:** US-S03
- **Đầu vào:** `orderId`, trạng thái mới.
- **Xử lý:** `sp_Order_UpdateStatus` kiểm tra chuyển trạng thái hợp lệ (BR-15), cập nhật, trả `userId`; tiếp theo F08.2. Phiên bản ở Chương 9 chỉ chặn đổi đơn đã kết thúc; kiểm tra đúng trình tự là bước bổ sung trong bài tập hướng dẫn Chương 9.
- **API / thủ tục:** `PATCH /orders/:id/status` → `sp_Order_UpdateStatus`.

### F09.3. Bật/tắt món còn bán, cập nhật tồn kho

- **Actor / nền tảng:** Nhân viên · M (bật/tắt), W (tồn kho) · **User story:** US-S04, US-S05
- **API / thủ tục (đề xuất):** `PATCH /products/:id/availability` → `sp_Product_SetAvailability`; `PATCH /products/:id/stock` → `sp_Product_UpdateStock` (`@Stock >= 0`).
- **Mở rộng:** gửi `product:availability` để màn hình thực đơn của khách cập nhật ngay.

## 5.11. M10 - Báo cáo

### F10.1. Doanh thu theo ngày

- **Actor / nền tảng:** Nhân viên (hôm nay), Quản lý (khoảng ngày) · M+W · **User story:** US-S08, US-A05
- **Đầu vào:** `from`, `to` (ngày).
- **Đầu ra:** `{ day, orderCount, revenue }`; không tính đơn `cancelled`.
- **API / thủ tục:** `GET /reports/revenue?from=&to=` → `sp_Report_RevenueByDay`.

### F10.2. Món bán chạy

- **API / thủ tục:** `GET /reports/top-products?from=&to=&top=` → `sp_Report_TopProducts`.
- **Màn hình:** Mobile thẻ tóm tắt trong chế độ nhân viên; Web trang Báo cáo có biểu đồ.

### F10.3. Thống kê đơn theo trạng thái (mở rộng)

- **User story:** US-A06 · **Thủ tục (đề xuất):** `sp_Report_OrderStatus` đếm đơn theo trạng thái và tỉ lệ hủy.

## 5.12. M11 - Quản trị (web)

### F11.1. Quản lý danh mục

- **Actor / nền tảng:** Quản lý · W · **User story:** US-A01
- **Thủ tục (đề xuất):** `sp_Category_Create`, `sp_Category_Update`, `sp_Category_Delete` (`THROW 50409` khi còn món).

### F11.2. Quản lý món

- **Actor / nền tảng:** Quản lý · W · **User story:** US-A02
- **Thủ tục (đề xuất):** `sp_Product_Create`, `sp_Product_Update`; "xóa" là đặt `IsAvailable = 0` (BR-16).

### F11.3. Quản lý quầy

- **Actor / nền tảng:** Quản lý · W · **User story:** US-A03
- **Thủ tục (đề xuất):** `sp_Counter_Create`, `sp_Counter_Update`; ràng buộc `CHECK` tọa độ (Chương 8).

### F11.4. Quản lý tài khoản nhân viên

- **Actor / nền tảng:** Quản lý · W · **User story:** US-A04
- **Xử lý:** tạo tài khoản `staff` với mật khẩu tạm; khóa/mở khóa (cột `IsLocked`, đề xuất); khóa tài khoản thì thu hồi mọi refresh token của tài khoản đó.
- **Thủ tục (đề xuất):** `sp_User_CreateStaff`, `sp_User_SetLocked`, `sp_User_GetList`.

## 5.13. M12 - Hạ tầng và chất lượng

| Chức năng | Mô tả | Chương |
|---|---|---|
| F12.1. Kiểm thử tự động | Jest + React Native Testing Library cho ứng dụng; script T-SQL cho thủ tục | 10 |
| F12.2. Bug log | `docs/bug-log.md` theo mẫu: tái hiện, mức độ, nguyên nhân, cách sửa, commit | 10 |
| F12.3. Health check | `GET /health` → `sp_Health_Check` | 11 |
| F12.4. Log lỗi backend | `Logger` của NestJS cho lỗi không thuộc nghiệp vụ | 11 |
| F12.5. Triển khai | Script `database/` chạy theo thứ tự; API chạy như dịch vụ nền trên Windows Server Khoa | 11 |
| F12.6. Build và cập nhật | EAS Build (APK `preview`, AAB `production`), EAS Update theo channel | 11 |

## 5.14. Danh sách màn hình

### 5.14.1. Ứng dụng di động

| Màn hình | Route (Expo Router) | Actor | Chức năng |
|---|---|---|---|
| Đăng nhập, Đăng ký | `app/login.tsx`, `app/register.tsx` | A1 | F01.1, F01.2 |
| Trang chủ (thực đơn) | `app/(tabs)/index.tsx` | A1, A2 | F02.1–F02.3 |
| Món theo danh mục | `app/category/[id].tsx` | A1, A2 | F02.2 |
| Chi tiết món | `app/product/[id].tsx` | A1, A2 | F02.4, F03.1, F05.1, F07.4 |
| Giỏ hàng | `app/(tabs)/cart.tsx` | A2 | F03, F04.1, F06.3 |
| Đơn hàng (lịch sử) | `app/(tabs)/orders.tsx` | A2 | F04.2 |
| Chi tiết đơn | `app/order/[id].tsx` | A2 | F04.3–F04.5 |
| Thông báo | `app/(tabs)/notifications.tsx` | A2 | F08.3 |
| Tài khoản | `app/(tabs)/account.tsx` | A2, A3 | F01.4, F05.2, F07.1, F07.2 |
| Bản đồ quầy | `app/map.tsx` | A1, A2 | F06.1, F06.2 |
| Đơn mới (nhân viên) | `app/(staff)/orders.tsx` | A3 | F09.1, F09.2 |
| Món trong ngày (nhân viên) | `app/(staff)/menu.tsx` | A3 | F09.3 |
| Báo cáo nhanh (nhân viên) | `app/(staff)/report.tsx` | A3 | F10.1, F10.2 |

### 5.14.2. Ứng dụng web

| Trang | Actor | Chức năng |
|---|---|---|
| Đăng nhập, Đăng ký | A1 | F01.1, F01.2 |
| Thực đơn, Chi tiết món, Giỏ hàng, Đơn của tôi | A1, A2 | F02, F03, F04 |
| Màn hình quầy (đơn theo trạng thái) | A3 | F09.1, F09.2 |
| Món và tồn kho trong ngày | A3 | F09.3 |
| Báo cáo | A3, A4 | F10 |
| Quản trị danh mục, món, quầy, nhân viên | A4 | F11 |
| Tình trạng hệ thống | A4 | F12.3 |
