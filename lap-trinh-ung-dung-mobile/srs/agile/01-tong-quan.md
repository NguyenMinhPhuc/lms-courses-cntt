# 1. Tổng quan kế hoạch Agile

## 1.1. Tầm nhìn sản phẩm

**Dành cho** sinh viên và cán bộ, giảng viên Trường Đại học Lạc Hồng, **những người** mất nhiều thời gian xếp hàng ở căn tin trong giờ nghỉ ngắn, **LHU Food** là ứng dụng đặt món trên điện thoại **giúp** xem thực đơn, đặt trước và nhận thông báo ngay khi món sẵn sàng. **Khác với** việc gọi món và chờ tại quầy, LHU Food cho căn tin nhận đơn theo thời gian thực, kiểm soát số suất và nắm doanh thu hằng ngày.

Mục tiêu sản phẩm (SRS mục 2.2):

| Mã | Mục tiêu | Thước đo |
|---|---|---|
| G1 | Giảm thời gian xếp hàng | Đặt xong đơn 2–3 món trong dưới 1 phút |
| G2 | Khách biết chính xác khi nào lấy món | Thông báo "Sẵn sàng" đến điện thoại trong vài giây |
| G3 | Không bán quá số suất đã chuẩn bị | Không có đơn nào làm tồn kho âm, kể cả khi đặt đồng thời |
| G4 | Quản lý nắm tình hình kinh doanh | Báo cáo doanh thu theo ngày, món bán chạy |

## 1.2. Phạm vi release 1.0 và MVP

- **Release 1.0** (5 sprint, 10 tuần): toàn bộ user story Must và Should của SRS cho ứng dụng di động (Android bắt buộc), ứng dụng web quản trị và backend dùng chung.
- **MVP** (hết Sprint 2, tuần 4): một khách hàng đăng ký, đăng nhập, xem thực đơn, đặt món; nhân viên nhận đơn và chuyển trạng thái; khách xem trạng thái và hủy đơn. Hệ thống chặn đặt quá tồn kho. Đây là luồng giá trị nhỏ nhất dùng được thật ở căn tin.
- **Ngoài phạm vi release 1.0** (Won't-have, SRS mục 1.2 và 10.3): thanh toán trực tuyến, giao hàng tận nơi, push notification khi ứng dụng đã tắt, tích điểm, đa ngôn ngữ, hẹn giờ nhận món. Các mục này nằm trong backlog với nhãn *Release 2* để không bị mất ý tưởng.

## 1.3. Vai trò Scrum

| Vai trò | Người đảm nhận (đề xuất) | Trách nhiệm chính |
|---|---|---|
| Product Owner | Giảng viên phụ trách (đại diện yêu cầu của căn tin) | Sắp xếp backlog, chấp nhận story theo tiêu chí nghiệm thu, quyết định phạm vi release |
| Scrum Master | Một sinh viên trong nhóm, luân phiên mỗi sprint | Điều phối sự kiện Scrum, gỡ trở ngại, theo dõi burndown |
| Development Team | 4–5 sinh viên (mobile, backend/CSDL, web, kiểm thử) | Ước lượng, cam kết sprint, hiện thực và kiểm thử story |
| Stakeholder | Quản lý căn tin, bộ phận hỗ trợ triển khai của Khoa | Góp ý ở Sprint Review, hỗ trợ triển khai server |

## 1.4. Giả định lập kế hoạch

- Nhóm 5 người, mỗi người khoảng 10–12 giờ mỗi tuần cho dự án.
- **Velocity dự kiến 30–36 story point mỗi sprint.** Sau Sprint 1, Product Owner và nhóm điều chỉnh kế hoạch theo velocity thực tế.
- Story point là độ lớn tương đối (công sức, độ phức tạp, rủi ro), không quy đổi trực tiếp ra giờ.

| Điểm | Ý nghĩa | Ví dụ trong LHU Food |
|---|---|---|
| 1 | Rất nhỏ, làm và kiểm thử trong vài giờ | Kéo để tải lại thực đơn |
| 2 | Nhỏ, một màn hình hoặc một endpoint đơn giản | Đăng xuất, bật/tắt món |
| 3 | Vừa, một màn hình có gọi API và xử lý lỗi | Chi tiết món, lịch sử đơn |
| 5 | Lớn, nhiều thành phần (CSDL + API + màn hình) | Đăng ký có kiểm tra dữ liệu, bản đồ quầy |
| 8 | Rất lớn, có rủi ro kỹ thuật (giao dịch, đồng thời) | Đặt món có giao dịch và khóa tồn kho |
| 13 | Quá lớn cho một sprint, phải tách nhỏ trước khi đưa vào sprint | Thanh toán trực tuyến |

**MoSCoW:** Must-have (thiếu thì release không có giá trị), Should-have (quan trọng nhưng có cách tạm), Could-have (làm nếu còn năng lực, là mục tiêu kéo dài của sprint), Won't-have (không làm trong release này).

## 1.5. Quy ước mã

- `US-G..`, `US-C..`, `US-S..`, `US-A..`, `US-SYS..`: giữ nguyên mã user story của SRS (khách vãng lai, khách hàng, nhân viên, quản lý, hệ thống) để truy vết.
- `TS-..`: technical story (enabler) bổ sung cho Scrum: hạ tầng, kiểm thử, phát hành; không có trong danh sách user story của SRS nhưng cần để giao được sản phẩm.
- `W-..`: hạng mục Won't-have.
- Một story SRS quá lớn được tách bằng hậu tố `a`, `b` (ví dụ US-S02a danh sách đơn, US-S02b cập nhật realtime).

## 1.6. Lịch sự kiện trong một sprint 2 tuần

| Thời điểm | Sự kiện | Thời lượng | Kết quả |
|---|---|---|---|
| Ngày 1 (thứ Hai tuần 1) | Sprint Planning | 2 giờ | Sprint Goal, Sprint Backlog đã cam kết |
| Mỗi ngày làm việc | Daily Scrum (trực tiếp hoặc trên nhóm chat) | 15 phút | Hôm qua, hôm nay, trở ngại |
| Giữa tuần 2 | Backlog Refinement | 1 giờ | Story sprint sau đạt Definition of Ready |
| Ngày 10 (thứ Sáu tuần 2) | Sprint Review | 1 giờ | Demo trên điện thoại Android thật, Product Owner chấp nhận story |
| Ngày 10, sau Review | Sprint Retrospective | 45 phút | 1–2 hành động cải tiến cho sprint sau |

## 1.7. Definition of Ready (DoR)

Một story được đưa vào Sprint Planning khi:

- ☐ Viết đúng mẫu As a / I want / So that, gắn Epic.
- ☐ Có tiêu chí nghiệm thu kiểm tra được.
- ☐ Đã ước lượng story point, không lớn hơn 8.
- ☐ Xác định API và stored procedure liên quan (theo SRS mục 5 và 8), phụ thuộc đã xong hoặc cùng sprint.
- ☐ Có thiết kế màn hình (Figma hoặc phác thảo) nếu có giao diện.

## 1.8. Definition of Done (DoD)

Một story được tính là xong khi:

- ☐ Đạt mọi tiêu chí nghiệm thu, Product Owner chấp nhận ở Sprint Review.
- ☐ Chạy trên Android thật (ứng dụng di động) hoặc trình duyệt (web); không có màn hình đỏ.
- ☐ Truy cập dữ liệu chỉ qua stored procedure; script CSDL dựng lại được từ đầu.
- ☐ Có test tự động cho logic chính (từ Sprint 5 áp dụng cho mọi story Must) hoặc kịch bản kiểm thử thủ công đã chạy.
- ☐ Mã được review qua pull request, merge vào `main`; prompt chính ghi trong `PROMPTS.md`; người viết giải thích được mã.
- ☐ Cập nhật tài liệu liên quan (README, Swagger, sơ đồ).
