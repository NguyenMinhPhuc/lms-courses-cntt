# 4. User stories

## 4.1. Quy ước

Mỗi user story viết theo mẫu: **Là** <actor>, **tôi muốn** <hành động>, **để** <giá trị nhận được>. Các cột:

- **Mã:** `US-<actor>-<số>`; G = Khách vãng lai, C = Khách hàng, S = Nhân viên, A = Quản lý, SYS = Hệ thống.
- **Nền tảng:** [M] chỉ ứng dụng di động; [W] chỉ ứng dụng web; [M+W] cả hai (backend dùng chung).
- **Ưu tiên:** Must (bắt buộc cho đồ án), Should (nên có), Could (mở rộng, cộng điểm sáng tạo).
- **Chương:** chương giáo trình hiện thực story (bài tập hướng dẫn cuối chương đó). "Web" nghĩa là thuộc học phần Lập trình ứng dụng Web.

Tiêu chí chấp nhận (acceptance criteria) viết theo dạng **Cho trước / Khi / Thì** ở mục 4.7 cho các story Must; đó cũng là đầu vào để viết test (Chương 10).

## 4.2. Khách vãng lai (A1)

| Mã | User story | Nền tảng | Ưu tiên | Chương |
|---|---|---|---|---|
| US-G01 | Là khách vãng lai, tôi muốn xem thực đơn theo danh mục, để biết căn tin hôm nay bán gì | M+W | Must | 2, 3, 5 |
| US-G02 | Là khách vãng lai, tôi muốn tìm món theo tên, để nhanh chóng thấy món mình muốn | M+W | Must | 4 |
| US-G03 | Là khách vãng lai, tôi muốn xem chi tiết một món (ảnh, mô tả, giá, còn/hết), để quyết định có đặt không | M+W | Must | 3, 5 |
| US-G04 | Là khách vãng lai, tôi muốn đăng ký tài khoản bằng email trường, để có thể đặt món | M+W | Must | 4, 6 |
| US-G05 | Là khách vãng lai, tôi muốn đăng nhập, để dùng các chức năng của khách hàng | M+W | Must | 6 |
| US-G06 | Là khách vãng lai, tôi muốn xem danh sách quầy trên bản đồ, để biết nơi nhận món | M | Should | 8 |
| US-G07 | Là khách vãng lai, tôi muốn kéo xuống để tải lại thực đơn, để thấy món vừa hết hoặc vừa có | M | Should | 5 |

## 4.3. Khách hàng (A2)

| Mã | User story | Nền tảng | Ưu tiên | Chương |
|---|---|---|---|---|
| US-C01 | Là khách hàng, tôi muốn thêm món vào giỏ (thêm trùng thì cộng dồn), để đặt nhiều món một lần | M+W | Must | 4 |
| US-C02 | Là khách hàng, tôi muốn tăng, giảm, xóa món trong giỏ và thấy tổng tiền, để kiểm soát chi phí | M+W | Must | 4 |
| US-C03 | Là khách hàng, tôi muốn giỏ hàng vẫn còn khi tắt và mở lại ứng dụng, để không phải chọn lại | M | Should | 7 |
| US-C04 | Là khách hàng, tôi muốn đặt món kèm ghi chú ("ít cay"), để căn tin chuẩn bị đúng ý | M+W | Must | 5, 7 |
| US-C05 | Là khách hàng, tôi muốn chọn quầy nhận món khi đặt, để đến đúng nơi | M+W | Should | 8 |
| US-C06 | Là khách hàng, tôi muốn xem lịch sử đơn hàng (mới nhất trước, cuộn vô hạn), để theo dõi các lần đặt | M+W | Must | 5 |
| US-C07 | Là khách hàng, tôi muốn xem chi tiết và trạng thái hiện tại của một đơn, để biết khi nào đi lấy món | M+W | Must | 7, 9 |
| US-C08 | Là khách hàng, tôi muốn hủy đơn của mình khi đơn chưa được chuẩn bị, để không mất món khi đổi ý | M+W | Must | 7 |
| US-C09 | Là khách hàng, tôi muốn nhận thông báo ngay khi đơn chuyển trạng thái, để không phải mở ứng dụng kiểm tra | M | Must | 9 |
| US-C10 | Là khách hàng, tôi muốn xem danh sách thông báo, số chưa đọc trên tab, bấm vào thì mở đúng đơn | M | Must | 9 |
| US-C11 | Là khách hàng, tôi muốn đánh dấu món yêu thích và xem lại danh sách, để đặt nhanh món quen | M+W | Should | 7 |
| US-C12 | Là khách hàng, tôi muốn đổi ảnh đại diện bằng camera hoặc thư viện ảnh, để cá nhân hóa tài khoản | M | Should | 8 |
| US-C13 | Là khách hàng, tôi muốn xem hồ sơ và đăng xuất, để bảo vệ tài khoản trên máy dùng chung | M+W | Must | 6 |
| US-C14 | Là khách hàng, tôi muốn giữ đăng nhập khi mở lại ứng dụng, để không phải đăng nhập mỗi lần | M | Must | 6 |
| US-C15 | Là khách hàng, tôi muốn tìm quầy gần vị trí hiện tại, để chọn nơi nhận thuận tiện | M | Could | 8 |
| US-C16 | Là khách hàng, tôi muốn đặt lại một đơn cũ bằng một nút, để tiết kiệm thời gian | M+W | Could | 7 |
| US-C17 | Là khách hàng, tôi muốn đánh giá món đã nhận (sao, nhận xét, ảnh), để góp ý cho căn tin | M | Could | 8 |
| US-C18 | Là khách hàng, tôi muốn bật/tắt nhận thông báo trong ứng dụng, để không bị làm phiền | M | Could | 9 |

## 4.4. Nhân viên căn tin (A3)

| Mã | User story | Nền tảng | Ưu tiên | Chương |
|---|---|---|---|---|
| US-S01 | Là nhân viên, tôi muốn đăng nhập và thấy giao diện dành cho nhân viên, để làm việc mà không thấy chức năng của khách | M+W | Must | 6 |
| US-S02 | Là nhân viên, tôi muốn thấy đơn mới xuất hiện ngay (kèm âm báo), để chuẩn bị kịp thời | M+W | Must | 9 |
| US-S03 | Là nhân viên, tôi muốn chuyển trạng thái đơn theo đúng trình tự, để khách biết tiến độ | M+W | Must | 9 |
| US-S04 | Là nhân viên, tôi muốn đánh dấu một món hết/còn bán, để khách không đặt món đã hết | M+W | Should | 7 |
| US-S05 | Là nhân viên, tôi muốn cập nhật số suất còn lại của từng món trong ngày, để hệ thống tự chặn khi hết | W | Should | 7, Web |
| US-S06 | Là nhân viên, tôi muốn lọc đơn theo trạng thái (chờ, đang làm, sẵn sàng), để tập trung vào việc đang làm | M+W | Should | 9 |
| US-S07 | Là nhân viên, tôi muốn hủy đơn không phục vụ được và ghi lý do, để khách được báo rõ ràng | W | Could | Web |
| US-S08 | Là nhân viên, tôi muốn xem doanh thu hôm nay và món bán chạy, để báo cáo cuối ca | M+W | Should | 7 |

## 4.5. Quản lý căn tin (A4)

| Mã | User story | Nền tảng | Ưu tiên | Chương |
|---|---|---|---|---|
| US-A01 | Là quản lý, tôi muốn thêm, sửa, xóa danh mục, để tổ chức thực đơn | W | Must | Web |
| US-A02 | Là quản lý, tôi muốn thêm, sửa món, tải ảnh món và ngừng bán món, để cập nhật thực đơn | W | Must | Web |
| US-A03 | Là quản lý, tôi muốn quản lý danh sách quầy và tọa độ, để bản đồ trên ứng dụng chính xác | W | Should | Web |
| US-A04 | Là quản lý, tôi muốn tạo, khóa, mở khóa tài khoản nhân viên, để kiểm soát người được xử lý đơn | W | Must | Web |
| US-A05 | Là quản lý, tôi muốn xem doanh thu theo khoảng ngày và món bán chạy, để lập kế hoạch nấu | W | Must | 7, Web |
| US-A06 | Là quản lý, tôi muốn xem số đơn theo trạng thái và tỉ lệ đơn bị hủy, để đánh giá vận hành | W | Could | Web |
| US-A07 | Là quản lý, tôi muốn xem tình trạng hệ thống (API, CSDL), để phát hiện sự cố sớm | W | Could | 11, Web |

## 4.6. Hệ thống (A5)

| Mã | User story | Nền tảng | Ưu tiên | Chương |
|---|---|---|---|---|
| US-SYS01 | Hệ thống phải từ chối kết nối socket không có token hợp lệ, để không lộ thông báo | Backend | Must | 9 |
| US-SYS02 | Hệ thống phải lưu thông báo vào SQL Server trước khi gửi socket, để người đang tắt ứng dụng vẫn xem lại được | Backend | Must | 9 |
| US-SYS03 | Hệ thống phải chặn đặt quá tồn kho, kể cả khi nhiều người đặt cùng lúc | Backend | Must | 7, 10 |
| US-SYS04 | Hệ thống phải chạy như dịch vụ nền trên server Khoa và có endpoint kiểm tra sức khỏe | Backend | Must | 11 |
| US-SYS05 | Hệ thống phải ghi log lỗi không thuộc nghiệp vụ, để nhóm tìm nguyên nhân sự cố | Backend | Should | 11 |

## 4.7. Tiêu chí chấp nhận (story Must)

**US-G01 - Xem thực đơn theo danh mục**

- Cho trước có 3 danh mục và 10 món đang bán; khi mở Trang chủ thì thấy thanh danh mục và danh sách món, mỗi món có tên, giá định dạng "35.000 đ", ảnh.
- Khi chọn một danh mục thì chỉ thấy món thuộc danh mục đó.
- Khi API lỗi hoặc mất mạng thì thấy thông báo "Không tải được thực đơn" và nút Thử lại; không có màn hình đỏ.

**US-G02 - Tìm món**

- Khi gõ "cơm" thì danh sách chỉ còn món có tên chứa "cơm", không phân biệt hoa thường; gõ tiếng Việt có dấu vẫn đúng.
- Khi không có kết quả thì hiện "Không tìm thấy món phù hợp".

**US-G03 - Chi tiết món**

- Khi bấm một món thì mở màn hình chi tiết qua route `product/[id]`; nút Back của Android quay về danh sách.
- Món đã hết (`IsAvailable = 0` hoặc `Stock = 0`) hiển thị nhãn "Hết món" và nút "Thêm vào giỏ" bị vô hiệu.

**US-G04 - Đăng ký**

- Form gồm họ tên, email, mật khẩu, nhập lại mật khẩu; kiểm tra bằng Zod: email đúng định dạng, mật khẩu tối thiểu 8 ký tự, hai mật khẩu trùng nhau; lỗi hiện dưới từng ô bằng tiếng Việt.
- Email đã tồn tại thì API trả 409 (thủ tục `THROW 50409`), ứng dụng hiện "Email đã được sử dụng".
- Mật khẩu được băm bằng bcrypt ở backend; CSDL không chứa mật khẩu gốc.

**US-G05 - Đăng nhập**

- Sai email hoặc mật khẩu thì hiện một thông báo chung "Email hoặc mật khẩu không đúng".
- Đăng nhập đúng thì lưu token bằng SecureStore và chuyển về màn hình trước đó (hoặc Trang chủ).

**US-C01, US-C02 - Giỏ hàng**

- Thêm cùng một món hai lần thì giỏ có một dòng, số lượng 2.
- Giảm số lượng về 0 thì món bị xóa khỏi giỏ.
- Tổng tiền bằng tổng (giá × số lượng); badge trên tab Giỏ hàng hiển thị tổng số suất.

**US-C04 - Đặt món**

- Cho trước giỏ có món còn hàng; khi bấm Đặt món thì API tạo đơn trạng thái `pending`, trừ tồn kho, trả mã đơn; giỏ được xóa; ứng dụng mở màn hình chi tiết đơn.
- Giá trong đơn lấy từ bảng `Products` tại thời điểm đặt, không lấy giá ứng dụng gửi lên.
- Khi có món không đủ số lượng thì API trả 409, không tạo đơn, không trừ tồn kho của bất kỳ món nào, ứng dụng hiện "Có món đã hết hoặc không đủ số lượng".
- Nút Đặt món bị vô hiệu trong lúc đang gửi để tránh đặt hai lần.

**US-C06 - Lịch sử đơn**

- Danh sách mới nhất trước, mỗi dòng có mã đơn, thời gian, tổng tiền, trạng thái bằng chữ (không chỉ màu).
- Cuộn gần cuối thì tải thêm trang tiếp theo; kéo xuống để tải lại.

**US-C07 - Chi tiết đơn**

- Hiển thị từng món, số lượng, đơn giá tại thời điểm đặt, tổng tiền, ghi chú, quầy nhận, trạng thái.
- Khi nhận sự kiện `order:status` của đơn đang xem thì trạng thái cập nhật mà không cần tải lại thủ công.

**US-C08 - Hủy đơn**

- Nút Hủy chỉ hiện khi đơn `pending`; có hộp thoại xác nhận.
- Hủy thành công thì đơn chuyển `cancelled` và tồn kho được hoàn lại.
- Hủy đơn của người khác hoặc đơn đã `preparing` thì API trả 409.

**US-C09, US-C10 - Thông báo**

- Khi nhân viên chuyển đơn sang `ready` thì trong vài giây điện thoại của khách hiện thông báo "Đơn #12 đã sẵn sàng"; bấm vào mở chi tiết đơn #12.
- Khi ứng dụng đã tắt rồi mở lại thì thông báo vẫn có trong danh sách (đọc từ SQL Server).
- Badge số chưa đọc giảm khi mở một thông báo.

**US-C13, US-C14 - Hồ sơ, đăng xuất, giữ đăng nhập**

- Mở lại ứng dụng khi refresh token còn hạn thì vào thẳng Trang chủ đã đăng nhập.
- Đăng xuất thì thu hồi refresh token ở server, xóa token trên máy, xóa giỏ hàng, về màn hình Đăng nhập.

**US-S01 - Giao diện nhân viên**

- Tài khoản `staff` sau đăng nhập thấy tab "Đơn mới" thay cho tab "Giỏ hàng"; tài khoản `customer` không truy cập được màn hình nhân viên kể cả khi gõ đường dẫn.
- API của nhân viên trả 403 khi gọi bằng token `customer`.

**US-S02, US-S03 - Nhận đơn và cập nhật trạng thái**

- Khi khách đặt đơn thì danh sách "Đơn mới" của mọi nhân viên đang mở ứng dụng tự xuất hiện đơn đó.
- Chỉ cho phép chuyển trạng thái theo trình tự `pending → preparing → ready → completed`; chuyển sai trình tự thì API trả 409.
- Mỗi lần chuyển trạng thái tạo một thông báo cho khách và gửi `order:status`.

**US-A01, US-A02, US-A04 - Quản trị (web)**

- Chỉ tài khoản `admin` truy cập được trang quản trị; API quản trị trả 403 với vai trò khác.
- Không xóa được danh mục còn món (409); món đã có trong đơn chỉ được "ngừng bán", không xóa hẳn.
- Tài khoản nhân viên bị khóa không đăng nhập được và không làm mới được token.

**US-A05 - Báo cáo**

- Báo cáo doanh thu theo khoảng ngày không tính đơn `cancelled`; số liệu khớp với truy vấn trực tiếp trên CSDL.

**US-SYS03 - Chặn đặt quá tồn kho**

- Cho trước món còn 1 suất; khi hai khách cùng đặt 1 suất gần như đồng thời thì đúng một đơn thành công, đơn còn lại nhận 409; tồn kho bằng 0, không âm.
