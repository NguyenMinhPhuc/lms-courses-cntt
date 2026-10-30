# Lời nói đầu

Giáo trình *Lập trình ứng dụng web* được biên soạn cho học phần cùng tên (mã 111102) của Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, dành cho sinh viên học kỳ 6. Người học đã hoàn thành các học phần Thiết kế UI/UX, Thiết kế Web (HTML, CSS, JavaScript), Lập trình Frontend (React) và Lập trình Backend (Node.js/NestJS, SQL Server). Giáo trình không dạy lại những kiến thức đó. Nó chỉ ra cách dùng chúng để **phân tích, xây dựng, kiểm thử và triển khai** một ứng dụng web hoàn chỉnh, rồi trình bày kết quả bằng một báo cáo kỹ thuật đúng quy định.

Nội dung được tổng hợp từ **tài liệu chính thức** của Next.js, React, Tailwind CSS, shadcn/ui, NestJS, Socket.IO, Vitest, Playwright, OWASP và Microsoft SQL Server, sắp xếp lại theo trình tự 12 buổi học. Khi một API hay câu lệnh có thể thay đổi theo phiên bản, giáo trình ghi rõ nguồn để người học tra lại tài liệu gốc.

## Học phần song hành với Lập trình ứng dụng di động

Học phần học cùng học kỳ với *Lập trình ứng dụng di động* (111114) và dùng chung đề tài **LHU Food** (đặt món căn tin trường). Hai học phần chia nhau một hệ thống:

- Ứng dụng di động (React Native, Expo) dành cho khách hàng đặt món.
- Ứng dụng web (Next.js) dành cho **quản lý căn tin** (trang quản trị), **nhân viên** (màn hình quầy thời gian thực) và web đặt món cơ bản cho khách.
- Một backend NestJS, một cơ sở dữ liệu Microsoft SQL Server cho cả hai.

Tài liệu **Đặc tả yêu cầu phần mềm (SRS) dự án LHU Food** và **Kế hoạch Agile & Product Backlog** dùng chung cho hai học phần. Giáo trình này dẫn chiếu tới SRS theo số mục (ví dụ "SRS mục 4.7" là tiêu chí chấp nhận của các user story). Phần backend dùng lại quy ước của giáo trình *Lập trình ứng dụng di động* (DatabaseService, RolesGuard, script CSDL theo phiên bản) và chỉ trình bày thêm phần dành riêng cho web.

## Cách tổ chức giáo trình

Mỗi chương tương ứng một buổi học và gồm:

- **Mục tiêu chương:** những gì bạn làm được sau khi học xong.
- **Nội dung lý thuyết:** giải thích khái niệm, kèm mã nguồn ví dụ trên web LHU Food.
- **Tóm tắt, câu hỏi ôn tập và bài tập:** dùng để tự kiểm tra trước buổi học sau.
- **Bài tập hướng dẫn theo dự án LHU Food:** nhiệm vụ của buổi học gắn với user story trong SRS, gồm chuẩn bị môi trường, các bước triển khai, cách vibe coding (prompt mẫu và cách kiểm tra mã do AI sinh) và tiêu chí hoàn thành.
- **Tài liệu tham khảo:** trình bày theo chuẩn IEEE, được trích dẫn bằng số trong ngoặc vuông tại đúng mục sử dụng.

Giáo trình gồm **12 chương** theo 4 sprint: Chương 1–3 (Sprint 1: nền tảng và giao diện, dùng API mẫu), Chương 4–6 (Sprint 2: người dùng và tương tác, dùng API mẫu), Chương 7–9 (Sprint 3: quản trị và realtime, chuyển sang backend của nhóm), Chương 10–12 (Sprint 4: chất lượng, triển khai, báo cáo và Demo Day chung).

## Bốn chuẩn đầu ra và cách giáo trình rèn luyện

| CLO | Nội dung | Rèn luyện ở |
|---|---|---|
| CLO1 | Phân tích các thành phần chức năng của ứng dụng web phù hợp với mô hình đã phân tích | Sitemap, ánh xạ route (Chương 2), ranh giới Server/Client (Chương 3–4), ma trận phân quyền (Chương 5), module quản trị (Chương 7), sơ đồ tuần tự (Chương 9) |
| CLO2 | Thực hiện các bài kiểm thử để kiểm tra các yêu cầu chức năng phù hợp với các mục tiêu dự án | Test case từ tiêu chí chấp nhận (Chương 3), giá trị biên (Chương 4), truy cập trái phép (Chương 5), luồng nghiệp vụ (Chương 6), kiểm thử tự động (Chương 10) |
| CLO3 | Viết báo cáo trình bày công việc đã thực hiện hợp lý và đúng quy định về định dạng | Báo cáo sprint (Chương 3, 6, 9), báo cáo đồ án (Chương 11) |
| CLO4 | Sắp xếp công việc cá nhân hoặc nhóm phù hợp với mục tiêu đề ra | Kế hoạch sprint (Chương 1), velocity (Chương 6), kế hoạch Sprint 4 (Chương 9), tổng kết tiến độ (Chương 11) |

## Ba nguyên tắc xuyên suốt

1. **Vibe coding có kiểm soát.** Bạn được dùng Google Antigravity và GitHub Copilot Chat để sinh mã, nhưng phải hiểu, kiểm tra và giải thích được mọi dòng mã mình nộp. Prompt chính được ghi lại trong `PROMPTS.md`. Không hiểu thì không merge.
2. **Next.js không kết nối cơ sở dữ liệu.** Mọi dữ liệu đi qua backend API; backend chỉ truy cập Microsoft SQL Server qua **stored procedure** có tham số.
3. **Phân tích trước, mã sau, kiểm thử để chứng minh.** Mỗi trang truy vết được tới một user story; mỗi tiêu chí chấp nhận có ít nhất một test case có kết quả.

## Quy ước trình bày

- `Chữ đơn cách` dùng cho tên file, lệnh, tên hàm và mã nguồn.
- Lệnh terminal chạy tại thư mục gốc của dự án web (`lhu-food-web`), trừ khi có ghi chú khác.
- Mã nguồn dùng TypeScript cho Next.js và NestJS; T-SQL cho SQL Server.
- Giáo trình viết theo Next.js 15 trở lên. Những điểm khác nhau giữa các phiên bản (ví dụ `middleware.ts` đổi tên thành `proxy.ts` từ Next.js 16) được ghi chú tại chỗ. Kiểm tra phiên bản bằng `npx next --version`.

*Bản thảo lưu hành nội bộ, Khoa Công nghệ Thông tin - Trường Đại học Lạc Hồng, 2026.*
