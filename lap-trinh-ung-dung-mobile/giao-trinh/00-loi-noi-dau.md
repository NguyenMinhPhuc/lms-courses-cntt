# Lời nói đầu

Giáo trình *Lập trình ứng dụng di động* được biên soạn cho học phần cùng tên (mã 111114) của Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, dành cho sinh viên học kỳ 6. Người học đã hoàn thành các học phần Thiết kế UI/UX, Thiết kế Web, Lập trình Frontend (React) và Lập trình Backend (Node.js/NestJS, SQL Server). Giáo trình không dạy lại những kiến thức đó; thay vào đó, nó chỉ ra cách đưa chúng lên điện thoại và nối chúng thành một sản phẩm hoàn chỉnh.

Nội dung được tổng hợp từ **tài liệu chính thức** của React Native, Expo, NestJS, Socket.IO và thư viện `mssql`, sắp xếp lại theo trình tự 12 buổi học của học phần. Khi một API hay câu lệnh có thể thay đổi theo phiên bản, giáo trình ghi rõ nguồn để người học tra lại tài liệu gốc.

## Cách tổ chức giáo trình

Mỗi chương tương ứng một buổi học và gồm:

- **Mục tiêu chương:** những gì bạn làm được sau khi học xong.
- **Nội dung lý thuyết:** giải thích khái niệm, kèm ví dụ trên ứng dụng mẫu **LHU Food** (đặt món căn tin).
- **Mã nguồn LHU Food:** các file hoàn chỉnh của chương để đối chiếu khi thực hành.
- **Tóm tắt, câu hỏi ôn tập và bài tập:** dùng để tự kiểm tra và luyện tập trước buổi học sau.
- **Bài tập hướng dẫn theo dự án LHU Food:** nhiệm vụ của buổi học gắn với các user story trong tài liệu SRS, gồm chuẩn bị môi trường, các bước triển khai, cách vibe coding (prompt mẫu và cách kiểm tra mã do AI sinh) và tiêu chí hoàn thành.
- **Tài liệu tham khảo:** đường dẫn tới tài liệu chính thức.

## Tài liệu đặc tả yêu cầu LHU Food (SRS)

Đi kèm giáo trình là phụ lục **Đặc tả yêu cầu phần mềm (SRS) dự án LHU Food** (file Word riêng). SRS mô tả ứng dụng, các actor và hành vi, toàn bộ user story của từng actor (phân biệt ứng dụng di động và ứng dụng web), các module và chức năng chi tiết, quy tắc nghiệp vụ, dữ liệu, danh mục API và yêu cầu phi chức năng. Mỗi bài tập hướng dẫn ghi rõ user story và mục SRS cần đọc; nhóm làm đề tài riêng dùng SRS làm mẫu để viết đặc tả cho đề tài của mình.

Giáo trình gồm **12 chương**, tương ứng 12 buổi học và 4 sprint của học phần: Chương 1–3 (Sprint 1: nền tảng), Chương 4–6 (Sprint 2: dữ liệu và người dùng), Chương 7–9 (Sprint 3: thiết bị và realtime), Chương 10–12 (Sprint 4: kiểm thử, triển khai và phát hành, báo cáo đồ án).

## Ba nguyên tắc xuyên suốt

1. **Vibe coding có kiểm soát.** Bạn được dùng Google Antigravity và GitHub Copilot Chat để sinh mã, nhưng phải hiểu, kiểm tra và giải thích được mọi dòng mã mình nộp. Prompt chính được ghi lại trong `PROMPTS.md`.
2. **Dữ liệu chỉ nằm trên Microsoft SQL Server.** Ứng dụng di động không có cơ sở dữ liệu trên thiết bị. Backend NestJS chỉ truy cập dữ liệu qua **stored procedure** có tham số, bằng thư viện `mssql`.
3. **Android là bắt buộc, iOS là phần mở rộng.** Mọi ví dụ được kiểm tra trên Android trước.

## Quy ước trình bày

- `Chữ đơn cách` dùng cho tên file, lệnh, tên hàm và mã nguồn.
- Lệnh terminal được chạy tại thư mục gốc của dự án, trừ khi có ghi chú khác.
- Mã nguồn dùng TypeScript cho ứng dụng và NestJS; T-SQL cho SQL Server.
- Các phiên bản thư viện thay đổi thường xuyên. Khi cài thư viện cho dự án Expo, luôn dùng `npx expo install <tên-gói>` để Expo chọn phiên bản tương thích.

*Bản thảo lưu hành nội bộ, Khoa Công nghệ Thông tin - Trường Đại học Lạc Hồng, 2026.*
