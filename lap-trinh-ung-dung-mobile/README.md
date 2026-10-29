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
- Bản Word: [giao-trinh/Giao-trinh-lap-trinh-ung-dung-mobile.docx](giao-trinh/Giao-trinh-lap-trinh-ung-dung-mobile.docx) (135 trang, đủ chương 1–12, có trang bìa và mục lục).
- Tạo lại bản Word sau khi sửa: `uv run --with python-docx python build-textbook.py lap-trinh-ung-dung-mobile`, rồi mở file trong Word, chọn mục lục và nhấn F9 để cập nhật số trang.

## 6. Cập nhật nội dung

Chỉ sửa file nguồn (`bai-XX.md`, `Slides/bai-XX.markdown`, `quiz/*.txt`, `thong-tin-hoc-phan.md`, `danh-gia-hoc-phan.md`), sau đó chạy ở thư mục gốc repo:

```bash
uv run python build-lessons.py lap-trinh-ung-dung-mobile
uv run --with python-pptx python build-slides.py lap-trinh-ung-dung-mobile
uv run python build-quiz.py lap-trinh-ung-dung-mobile --balance
uv run python validate-course.py lap-trinh-ung-dung-mobile
```
