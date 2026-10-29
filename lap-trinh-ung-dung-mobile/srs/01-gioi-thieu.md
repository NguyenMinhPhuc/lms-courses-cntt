# 1. Giới thiệu

## 1.1. Mục đích tài liệu

Tài liệu này đặc tả yêu cầu phần mềm (Software Requirements Specification - SRS) cho hệ thống **LHU Food**, ứng dụng đặt món tại căn tin Trường Đại học Lạc Hồng. LHU Food là **dự án mẫu xuyên suốt** của học phần Lập trình ứng dụng di động (111114): mỗi chương giáo trình hiện thực một phần của hệ thống, và bài tập hướng dẫn cuối mỗi chương được thiết kế từ các user story trong tài liệu này.

Tài liệu dùng cho:

- **Sinh viên:** hiểu toàn bộ hệ thống trước khi code; chọn user story cho từng buổi; dùng làm ngữ cảnh khi làm việc với trợ lý AI (đưa vào `AGENTS.md`, `.github/copilot-instructions.md`).
- **Giảng viên:** đối chiếu sản phẩm với yêu cầu khi chấm checkpoint và Demo Day.
- **Nhóm làm đề tài riêng:** tham khảo cấu trúc để viết SRS cho đề tài của nhóm.

## 1.2. Phạm vi

LHU Food gồm ba thành phần dùng chung một backend:

| Thành phần | Công nghệ | Người dùng chính | Học phần thực hiện |
|---|---|---|---|
| **Ứng dụng di động** (mobile app) | React Native + Expo, Android bắt buộc, iOS mở rộng | Khách hàng, nhân viên căn tin | Lập trình ứng dụng di động (111114) |
| **Ứng dụng web** (web app) | React (trình duyệt) | Quản lý căn tin, nhân viên căn tin; khách hàng (đặt món cơ bản) | Lập trình ứng dụng Web (học song song) |
| **Backend** | NestJS, Socket.IO, Microsoft SQL Server | Hai ứng dụng trên | Dùng chung cho cả hai học phần |

Học phần 111114 bắt buộc hiện thực các user story gắn nhãn **[M]** và **[M+W]** (phía di động). User story gắn nhãn **[W]** thuộc phạm vi ứng dụng web; nhóm làm chung đề tài với học phần web dùng chúng cho ứng dụng web, nhưng backend phải hỗ trợ được cả hai.

Ngoài phạm vi: thanh toán trực tuyến, giao hàng tận nơi, tích điểm thành viên, đa ngôn ngữ. Các mục này có thể là hướng phát triển của nhóm (mục 10.3).

## 1.3. Thuật ngữ

| Thuật ngữ | Ý nghĩa |
|---|---|
| Món (Product) | Một món ăn hoặc đồ uống được bán tại căn tin |
| Danh mục (Category) | Nhóm món: Cơm, Bún – Phở, Đồ uống… |
| Quầy (Counter) | Điểm nhận món trong khuôn viên trường, có tọa độ trên bản đồ |
| Đơn hàng (Order) | Một lần đặt món của khách hàng, gồm nhiều dòng món |
| Tồn kho (Stock) | Số suất còn bán được của một món trong ngày |
| Trạng thái đơn | `pending` (chờ xác nhận), `preparing` (đang chuẩn bị), `ready` (sẵn sàng nhận), `completed` (đã nhận), `cancelled` (đã hủy) |
| Access token / refresh token | Token xác thực ngắn hạn / dài hạn (JWT), xem Chương 6 |
| Room | Nhóm kết nối Socket.IO do server quản lý, dùng để gửi thông báo đúng người |
| [M], [W], [M+W] | User story cho ứng dụng di động, ứng dụng web, hoặc cả hai |
| Must / Should / Could | Mức ưu tiên: bắt buộc / nên có / có thể có (phương pháp MoSCoW) |

## 1.4. Tài liệu liên quan

- Giáo trình *Lập trình ứng dụng di động*, Khoa CNTT - Trường Đại học Lạc Hồng (Chương 1–12).
- Đề cương học phần 111114 và trang Đánh giá học phần trên Moodle.
- Tài liệu chính thức: React Native, Expo, NestJS, Socket.IO, node-mssql, Microsoft SQL Server.

# 2. Mô tả tổng quan ứng dụng

## 2.1. Bối cảnh

Vào giờ nghỉ giữa các ca học, căn tin thường đông; sinh viên mất nhiều thời gian xếp hàng gọi món rồi chờ lấy món, trong khi thời gian nghỉ ngắn. Nhân viên căn tin ghi đơn bằng tay, khó biết trước số lượng cần chuẩn bị và khó báo cho khách khi món đã xong.

LHU Food cho phép sinh viên và cán bộ **xem thực đơn, đặt món trước trên điện thoại**, chọn quầy nhận, và **nhận thông báo ngay khi món sẵn sàng**. Nhân viên nhận đơn theo thời gian thực, cập nhật trạng thái và quản lý món hết hàng. Quản lý căn tin quản trị thực đơn, tài khoản nhân viên và xem báo cáo doanh thu trên web.

## 2.2. Mục tiêu sản phẩm

| Mã | Mục tiêu | Cách đo |
|---|---|---|
| G1 | Giảm thời gian xếp hàng của khách | Khách đặt xong một đơn 2–3 món trong dưới 1 phút |
| G2 | Khách biết chính xác khi nào lấy món | Thông báo "Sẵn sàng" đến điện thoại trong vài giây sau khi nhân viên cập nhật |
| G3 | Không bán quá số suất đã chuẩn bị | Không có đơn nào làm tồn kho âm, kể cả khi nhiều người đặt cùng lúc |
| G4 | Quản lý nắm được tình hình kinh doanh | Báo cáo doanh thu theo ngày, món bán chạy |

## 2.3. Kiến trúc tổng thể

```text
┌───────────────────────┐      ┌────────────────────────┐
│  Mobile app (Expo)    │      │  Web app (React)       │
│  Khách hàng, Nhân viên│      │  Quản lý, Nhân viên    │
└──────────┬────────────┘      └───────────┬────────────┘
           │   HTTPS/HTTP REST + Socket.IO (cùng cổng)
           └───────────────┬───────────────┘
                           ▼
          ┌────────────────────────────────────┐
          │ Backend NestJS (Windows Server Khoa)│
          │ - REST API, Swagger                 │
          │ - Gateway Socket.IO (room)          │
          │ - DatabaseService (mssql)           │
          └───────────────┬────────────────────┘
                          │ chỉ gọi stored procedure
                          ▼
          ┌────────────────────────────────────┐
          │ Microsoft SQL Server (LhuFood)      │
          │ bảng + stored procedure + giao dịch │
          └────────────────────────────────────┘
```

Nguyên tắc kiến trúc (ràng buộc bắt buộc của học phần):

1. **Dữ liệu chỉ nằm trên SQL Server.** Ứng dụng di động không có CSDL trên thiết bị; chỉ lưu token (SecureStore), giỏ hàng chưa đặt và thiết lập cá nhân (AsyncStorage).
2. **Backend chỉ truy cập dữ liệu qua stored procedure** có tham số bằng thư viện `mssql`; không viết câu SQL trực tiếp trong mã, không dùng ORM.
3. **Socket chỉ để báo tin.** Mọi thao tác ghi đi qua REST API và thủ tục; sự kiện socket được gửi sau khi dữ liệu đã lưu.
4. **Một backend cho hai ứng dụng.** API không giả định client là mobile hay web; phân quyền theo vai trò trong token.

## 2.4. Phân vai giữa ứng dụng di động và ứng dụng web

| Nhóm chức năng | Mobile app | Web app |
|---|---|---|
| Xem thực đơn, tìm món, chi tiết món | ✔ | ✔ |
| Đăng ký, đăng nhập, hồ sơ | ✔ | ✔ |
| Giỏ hàng, đặt món, lịch sử, hủy đơn | ✔ (chính) | ✔ (cơ bản) |
| Thông báo realtime cho khách | ✔ (bắt buộc) | Tùy chọn |
| Camera, ảnh đại diện, vị trí, bản đồ quầy | ✔ | |
| Nhận đơn mới, cập nhật trạng thái đơn | ✔ (chế độ nhân viên) | ✔ (màn hình quầy) |
| Đánh dấu món hết hàng, cập nhật tồn kho | ✔ (bật/tắt) | ✔ (đầy đủ) |
| Báo cáo doanh thu, món bán chạy | ✔ (xem nhanh) | ✔ (đầy đủ) |
| Quản trị danh mục, món, quầy, tài khoản nhân viên | | ✔ |

## 2.5. Giả định và ràng buộc

| Mã | Nội dung |
|---|---|
| C1 | Ứng dụng di động bắt buộc chạy trên Android (APK); iOS là phần mở rộng. |
| C2 | Backend và SQL Server triển khai trên Windows Server do Khoa cấp, với sự hỗ trợ của bộ phận triển khai. |
| C3 | Mỗi sinh viên dùng tài khoản Expo miễn phí; số lượt build EAS có giới hạn. |
| C4 | Chỉ người dùng đã đăng nhập mới đặt món; xem thực đơn không cần đăng nhập. |
| C5 | Hệ thống không xử lý thanh toán: khách thanh toán tại quầy khi nhận món. |
| C6 | Một đơn hàng được nhận tại một quầy; giá món tại thời điểm đặt được lưu vào đơn. |
| C7 | Trợ lý AI (Google Antigravity, GitHub Copilot Chat) được dùng để sinh mã; prompt chính ghi trong `PROMPTS.md`. |
