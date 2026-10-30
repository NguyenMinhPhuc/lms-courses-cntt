# Học phần: Lập trình ứng dụng di động (111114)

- **Thời lượng:** 60 tiết (15 lý thuyết + 45 thực hành), 12 buổi × 5 tiết
- **Học kỳ:** 6, học song song với *Lập trình ứng dụng Web*
- **Giảng viên phụ trách:** ThS. Nguyễn Minh Phúc · **Cùng tham gia:** Lê Minh Nhật, Lê Chân Thiện Tâm
- **Phương pháp:** PBL theo nhóm 4–5 sinh viên, 4 sprint; vibe coding có kiểm soát với Google Antigravity và GitHub Copilot Chat
- **Công nghệ:** React Native + Expo (Android bắt buộc, iOS mở rộng) · NestJS + Socket.IO · Microsoft SQL Server, truy cập **bắt buộc qua stored procedure** bằng `mssql` · triển khai trên Windows Server do Khoa cấp
- **Ví dụ xuyên suốt:** LHU Food, ứng dụng đặt món căn tin
- **Trang học phần:** [index.html](index.html) · **Đề cương:** [thong-tin-hoc-phan.html](thong-tin-hoc-phan.html) · **Đánh giá:** [danh-gia-hoc-phan.html](danh-gia-hoc-phan.html) · **Dàn ý chi tiết:** [dan-y-chi-tiet.md](dan-y-chi-tiet.md)

---

## 1. Chuẩn đầu ra (CLO)

| CLO | Mô tả | PLO / PI | Điểm cuối kỳ |
| :--- | :--- | :---: | :---: |
| CLO1 | Thiết kế các thành phần chức năng của ứng dụng di động đáp ứng các yêu cầu đặt ra | PLO2 / PI 2.4 | 3 |
| CLO2 | Thiết kế cơ sở dữ liệu đáp ứng cấu trúc dữ liệu phù hợp yêu cầu đặc tả | PLO2 / PI 2.5 | 2 |
| CLO3 | Sử dụng được các công cụ đồ họa để trình bày các ý tưởng thiết kế dữ liệu | PLO3 / PI 3.4 | 2 |
| CLO4 | Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng | PLO5 / PI 5.2 | 3 |

Sinh viên đạt CLO khi được ≥ 50% điểm của CLO; CLO đạt ở cấp lớp khi ≥ 75% số sinh viên đạt.

## 2. Đánh giá

| Thành phần | Tỷ trọng |
| :--- | :---: |
| Quá trình | 30% |
| Thực hành | 30% |
| Cuối kỳ: đồ án nhóm (thang 10, tách theo CLO) | 40% |

## 3. Danh sách bài học

| Buổi | Tên bài | Trạng thái | File |
| :---: | :--- | :---: | :---: |
| 01 | Tổng quan phát triển ứng dụng di động & khởi động dự án | ✅ Đã soạn | [bai-01.md](bai-01.md) · [slide](Slides/bai-01.pptx) |
| 02 | Core Components, Styling & Layout với Flexbox | ✅ Đã soạn | [bai-02.md](bai-02.md) · [slide](Slides/bai-02.pptx) |
| 03 | Điều hướng với Expo Router · Checkpoint Sprint 1 | ✅ Đã soạn | [bai-03.md](bai-03.md) · [slide](Slides/bai-03.pptx) |
| 04 | Quản lý trạng thái, danh sách & form | ✅ Đã soạn | [bai-04.md](bai-04.md) · [slide](Slides/bai-04.pptx) |
| 05 | Thiết kế CSDL, stored procedure, API NestJS & kết nối ứng dụng | ✅ Đã soạn | [bai-05.md](bai-05.md) · [slide](Slides/bai-05.pptx) |
| 06 | Xác thực & bảo mật ứng dụng · Checkpoint Sprint 2 | ✅ Đã soạn | [bai-06.md](bai-06.md) · [slide](Slides/bai-06.pptx) |
| 07 | CSDL SQL Server nâng cao & đồng bộ dữ liệu qua backend | ✅ Đã soạn | [bai-07.md](bai-07.md) · [slide](Slides/bai-07.pptx) |
| 08 | Tính năng thiết bị: Camera, Ảnh, Vị trí & Bản đồ | ✅ Đã soạn | [bai-08.md](bai-08.md) · [slide](Slides/bai-08.pptx) |
| 09 | Thông báo thời gian thực với Socket.IO · Checkpoint Sprint 3 | ✅ Đã soạn | [bai-09.md](bai-09.md) · [slide](Slides/bai-09.pptx) |
| 10 | Kiểm thử, gỡ lỗi & tối ưu hiệu năng | ✅ Đã soạn | [bai-10.md](bai-10.md) · [slide](Slides/bai-10.pptx) |
| 11 | Triển khai backend lên server Khoa, build & phát hành ứng dụng | ✅ Đã soạn | [bai-11.md](bai-11.md) · [slide](Slides/bai-11.pptx) |
| 12 | Demo Day: báo cáo đồ án & tổng kết · Cuối kỳ | ✅ Đã soạn | [bai-12.md](bai-12.md) · [slide](Slides/bai-12.pptx) |

## 4. Ngân hàng câu hỏi

- Giảng viên tải file Aiken để import Moodle tại [quiz/index.html](quiz/index.html).
- Sinh viên luyện tập trực tiếp ở cuối mỗi trang `bai-XX.html` (chỉ báo số câu đúng/sai, không lưu kết quả).

## 5. Giáo trình nội bộ

- Nguồn: [giao-trinh/](giao-trinh/) gồm `00-loi-noi-dau.md` và `chuong-01.md` … `chuong-12.md` (mỗi chương ứng với một buổi).
- Bài tập hướng dẫn theo dự án LHU Food: [giao-trinh/bai-tap-huong-dan/](giao-trinh/bai-tap-huong-dan/) `bt-01.md` … `bt-12.md`, được `build-textbook.py` chèn vào cuối chương tương ứng (trước Tài liệu tham khảo).
- Bản Word: [giao-trinh/Giao-trinh-lap-trinh-ung-dung-mobile.docx](giao-trinh/Giao-trinh-lap-trinh-ung-dung-mobile.docx) (160 trang, đủ chương 1–12 kèm bài tập hướng dẫn, tài liệu tham khảo chuẩn IEEE, watermark "Công nghệ thông tin - LHU").
- Tạo lại bản Word sau khi sửa: `uv run --with python-docx python build-textbook.py lap-trinh-ung-dung-mobile`, rồi mở file trong Word, chọn mục lục và nhấn F9 để cập nhật số trang.

## 6. Đặc tả yêu cầu dự án LHU Food (SRS)

- Nguồn: [srs/](srs/) gồm `01-gioi-thieu.md` (mô tả ứng dụng), `02-actor.md` (actor và hành vi), `03-user-stories.md` (user story theo actor, phân biệt mobile/web, tiêu chí chấp nhận), `04-module.md` (module và chức năng chi tiết, danh sách màn hình), `05-du-lieu-api.md` (quy tắc nghiệp vụ, dữ liệu, API, phi chức năng, truy vết).
- Bản Word: [srs/SRS-LHU-Food.docx](srs/SRS-LHU-Food.docx) (37 trang).
- Tạo lại: `uv run --with python-docx python build-textbook.py lap-trinh-ung-dung-mobile --srs`, rồi cập nhật mục lục trong Word.
- Kế hoạch Agile/Scrum chuyển từ SRS: [srs/agile-scrum.docx](srs/agile-scrum.docx) (12 Epic, 58 mục backlog, 5 sprint × 2 tuần, MVP hết Sprint 2). Nguồn Markdown: [srs/agile/](srs/agile/); file nhập Jira/Trello/Notion: [srs/agile/product-backlog.csv](srs/agile/product-backlog.csv). Tạo lại cả hai: `uv run --with python-docx python build-textbook.py lap-trinh-ung-dung-mobile --agile`.

## 6. Cập nhật nội dung

Chỉ sửa file nguồn (`bai-XX.md`, `Slides/bai-XX.markdown`, `quiz/*.txt`, `thong-tin-hoc-phan.md`, `danh-gia-hoc-phan.md`), sau đó chạy ở thư mục gốc repo:

```bash
uv run python build-lessons.py lap-trinh-ung-dung-mobile
uv run --with python-pptx python build-slides.py lap-trinh-ung-dung-mobile
uv run python build-quiz.py lap-trinh-ung-dung-mobile --balance
uv run python validate-course.py lap-trinh-ung-dung-mobile
```

## 7. Backend mẫu LHU Food (API cho sinh viên)

- Mã nguồn: [backend/](backend/) - Node.js microservice (API Gateway + identity, catalog, order, notification), SQL Server 2019+ chỉ qua stored procedure, JWT, Swagger UI, cache (Redis hoặc bộ nhớ), Socket.IO. Endpoint và định dạng dữ liệu khớp giáo trình Chương 5–11 và SRS.
- Hướng dẫn cài đặt, triển khai trên Windows Server và cách sinh viên dùng API: [backend/README.md](backend/README.md). Tài liệu API trực tiếp tại `<địa chỉ server>:3000/docs`.

## 8. Rubric chấm điểm theo CLO

- Nguồn duy nhất: [rubric/rubric.json](rubric/rubric.json): 4 CLO, 27 tiêu chí (mỗi tiêu chí chấm một vấn đề), 5 mức (A 100%, B 75%, C 50%, D 25%, 0), mô tả từng mức, gợi ý chấm, minh chứng cần có, phạm vi chấm nhóm/cá nhân.
- File Excel: [rubric/Rubric-111114.xlsx](rubric/Rubric-111114.xlsx) gồm Hướng dẫn, Rubric, Bảng điểm (60 dòng, kiểm tra dữ liệu, tự tính điểm CLO, tổng, Đạt/Chưa đạt) và Mức đạt CLO (tỷ lệ SV đạt, kết luận cấp lớp theo ngưỡng 75%).
- Công cụ chấm trên web: [cham-diem.html](cham-diem.html): nhập danh sách (dán từ Excel/CSV), chấm theo mức hoặc điểm lẻ, tiêu chí nhóm chấm một lần áp dụng cả nhóm (có chấm riêng từng SV), thống kê mức đạt CLO, xuất Excel theo tiêu chí và CLO. Dữ liệu lưu trong trình duyệt; sao lưu/khôi phục bằng JSON.
- Tạo lại sau khi sửa rubric.json: `uv run --with openpyxl python build-rubric.py lap-trinh-ung-dung-mobile` (hook tự chạy khi Claude sửa rubric.json).

