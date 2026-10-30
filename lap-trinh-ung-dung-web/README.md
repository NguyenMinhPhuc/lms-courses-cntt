# Lập trình ứng dụng web (111102)

Học phần 3 tín chỉ (60 tiết: 15 lý thuyết, 45 thực hành), Học kỳ 6, học song song với Lập trình ứng dụng di động (111114). Giảng viên phụ trách: ThS. Nguyễn Minh Phúc; cùng tham gia: Lê Minh Nhật, Hồ Ngọc Hoàng Long.

Sinh viên xây dựng phần web của dự án **LHU Food** bằng **Next.js (App Router)**, dùng chung đề tài, SRS và kế hoạch Agile với học phần di động: trang quản trị và màn hình quầy thời gian thực (bắt buộc), web đặt món cho khách (cơ bản). Sprint 1–2 gọi API mẫu của giảng viên; Sprint 3–4 nhóm tự xây module quản trị trên backend của nhóm (khuyến khích NestJS dùng chung với đồ án di động). Next.js không kết nối SQL Server trực tiếp; backend chỉ truy cập dữ liệu qua stored procedure.

## 1. Chuẩn đầu ra (đánh giá cuối kỳ bằng báo cáo, thang 10)

| CLO | Nội dung | PLO/PI | Trọng số | Đạt khi |
|---|---|---|:---:|:---:|
| CLO1 | Phân tích các thành phần chức năng của ứng dụng web phù hợp với mô hình đã phân tích | PLO2 / PI 2.4 | 4 | ≥ 2 |
| CLO2 | Thực hiện các bài kiểm thử để kiểm tra các yêu cầu chức năng phù hợp với các mục tiêu dự án | PLO4 / PI 4.1 | 2 | ≥ 1 |
| CLO3 | Viết báo cáo trình bày nội dung các công việc đã thực hiện hợp lý và đúng quy định về định dạng | PLO3 / PI 3.1 | 2 | ≥ 1 |
| CLO4 | Sử dụng kỹ năng sắp xếp công việc cá nhân hoặc nhóm phù hợp với mục tiêu đề ra | PLO5 / PI 5.1 | 2 | ≥ 1 |

Đánh giá: Quá trình 30% · Thực hành 30% · Cuối kỳ (báo cáo đồ án + Demo Day chung với học phần di động) 40%. CLO đạt ở cấp lớp khi ≥ 75% sinh viên đạt.

## 2. Danh sách bài học

| Buổi | Tên bài | Trạng thái | File |
| :---: | :--- | :---: | :---: |
| 01 | Ứng dụng web hiện đại với Next.js & khởi động dự án | ✅ Đã soạn | [bai-01.md](bai-01.md) · [slide](Slides/bai-01.pptx) |
| 02 | Routing, layout & giao diện với Tailwind CSS | ✅ Đã soạn | [bai-02.md](bai-02.md) · [slide](Slides/bai-02.pptx) |
| 03 | Server Components & lấy dữ liệu từ API · Checkpoint Sprint 1 | ✅ Đã soạn | [bai-03.md](bai-03.md) · [slide](Slides/bai-03.pptx) |
| 04 | Client Components, trạng thái & form | ✅ Đã soạn | [bai-04.md](bai-04.md) · [slide](Slides/bai-04.pptx) |
| 05 | Xác thực, phân quyền & bảo mật web | ✅ Đã soạn | [bai-05.md](bai-05.md) · [slide](Slides/bai-05.pptx) |
| 06 | Server Actions, bảng dữ liệu & màn hình quầy · Checkpoint Sprint 2 | ✅ Đã soạn | [bai-06.md](bai-06.md) · [slide](Slides/bai-06.pptx) |
| 07 | Module quản trị trên backend của nhóm | ✅ Đã soạn | [bai-07.md](bai-07.md) · [slide](Slides/bai-07.pptx) |
| 08 | Trang quản trị: CRUD, tải ảnh, báo cáo & biểu đồ | ✅ Đã soạn | [bai-08.md](bai-08.md) · [slide](Slides/bai-08.pptx) |
| 09 | Màn hình quầy thời gian thực với Socket.IO · Checkpoint Sprint 3 | ✅ Đã soạn | [bai-09.md](bai-09.md) · [slide](Slides/bai-09.pptx) |
| 10 | Kiểm thử ứng dụng web, hiệu năng & accessibility | ✅ Đã soạn | [bai-10.md](bai-10.md) · [slide](Slides/bai-10.pptx) |
| 11 | Triển khai lên Windows Server của Khoa & hoàn thiện báo cáo | ✅ Đã soạn | [bai-11.md](bai-11.md) · [slide](Slides/bai-11.pptx) |
| 12 | Demo Day chung & nộp báo cáo đồ án | ✅ Đã soạn | [bai-12.md](bai-12.md) · [slide](Slides/bai-12.pptx) |

## 3. Thành phần học phần

- [dan-y-chi-tiet.md](dan-y-chi-tiet.md): dàn ý chi tiết đã duyệt, lộ trình 4 sprint, cách rèn luyện từng CLO.
- [giao-trinh/](giao-trinh/): giáo trình nội bộ (lời nói đầu, 12 chương, bài tập hướng dẫn `bai-tap-huong-dan/bt-XX.md`) → [Giao-trinh-lap-trinh-ung-dung-web.docx](giao-trinh/Giao-trinh-lap-trinh-ung-dung-web.docx).
- [HK6-111102-Lập trình ứng dụng web.docx](HK6-111102-Lập%20trình%20ứng%20dụng%20web.docx): đề cương theo mẫu của Khoa (ô tô vàng là nội dung cần giảng viên xác nhận).
- [thong-tin-hoc-phan.md](thong-tin-hoc-phan.md) / [danh-gia-hoc-phan.md](danh-gia-hoc-phan.md): đề cương và đánh giá (kèm quy định định dạng và cấu trúc báo cáo đồ án).
- [quiz/](quiz/): đề Aiken từng bài và file tổng hợp; trang tải cho giảng viên [quiz/index.html](quiz/index.html).
- [Slides/](Slides/): slide nguồn Markdown và PowerPoint.
- [rubric/rubric.json](rubric/rubric.json): rubric 27 tiêu chí theo 4 CLO → [rubric/Rubric-111102.xlsx](rubric/Rubric-111102.xlsx) và công cụ chấm [cham-diem.html](cham-diem.html).
- Tài liệu dùng chung với học phần di động: [SRS LHU Food](../lap-trinh-ung-dung-mobile/srs/SRS-LHU-Food.docx), [Kế hoạch Agile & Product Backlog](../lap-trinh-ung-dung-mobile/srs/agile-scrum.docx); API mẫu: [../lap-trinh-ung-dung-mobile/backend/](../lap-trinh-ung-dung-mobile/backend/).

## 4. Tạo lại

```bash
uv run python build-lessons.py lap-trinh-ung-dung-web
uv run python build-quiz.py lap-trinh-ung-dung-web --balance
uv run --with python-pptx python build-slides.py lap-trinh-ung-dung-web
uv run --with openpyxl python build-rubric.py lap-trinh-ung-dung-web
uv run --with python-docx python build-textbook.py lap-trinh-ung-dung-web
uv run python validate-course.py lap-trinh-ung-dung-web
```
