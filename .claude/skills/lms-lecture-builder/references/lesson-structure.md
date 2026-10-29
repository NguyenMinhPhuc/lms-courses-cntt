# Cấu trúc một bài học (bai-XX.md)

Mã HTML chuẩn nằm ở `template-lesson.md` (gốc repo). Sao chép nguyên khung style của file đó; chỉ thay nội dung. Ví dụ hoàn chỉnh: `nhap-mon-nganh/bai-01.md`.

File `.md` chỉ chứa 4 khối `<details>` (không có `<html>`, `<head>`, tiêu đề markdown).

## 4 khối bắt buộc

| # | Tiêu đề summary | Màu viền / nền | Trạng thái |
|---|---|---|---|
| 1 | `📘 1. Tổng quan bài học` | `#007bff` / `#e7f1ff` | `open` |
| 2 | `📚 2. Học liệu chính` | `#fd7e14` / `#fff5eb` | đóng |
| 3 | `💡 3. Hoạt động &amp; Thực hành trên lớp` | `#28a745` / `#eafaf1` | đóng |
| 4 | `🆘 4. Góc trợ giúp và mở rộng` | `#6f42c1` / `#f3e5f5` | đóng |

### Khối 1 - Tổng quan bài học
- Dòng tiêu đề: `BÀI XX - <Tên bài> (<số> tiết)`.
- **Mục tiêu:** 1-2 câu, dùng động từ Bloom đo được (trình bày, giải thích, phân tích, áp dụng, đánh giá, xây dựng). Gắn với CLO của học phần khi có.
- **Nội dung:** 4 ý chính dạng `<li><strong>Ý chính N - Tên:</strong> ...</li>`.
- **Kết quả cần đạt:** sinh viên làm được gì sau buổi học.
- Mở đầu bằng một câu hỏi hoặc tình huống thực tế (hook) trước phần Mục tiêu nếu tài liệu nguồn có chất liệu phù hợp.

### Khối 2 - Học liệu chính
Gồm các nhóm theo thứ tự (bỏ nhóm không có dữ liệu, không bịa):
1. `📄 Slide bài giảng Bài XX` - link slide chính.
2. `📑 Danh sách slide / trang tham khảo`.
3. `🎥 Video hướng dẫn chi tiết` - thẻ `<a class="nomediaplugin">` để Moodle không tự nhúng player.
4. `📖 Tài liệu đọc thêm` - giáo trình nội bộ (thẻ `<div>`), link ngoài (thẻ `<a>`).

Nếu bài cần trình bày nội dung lý thuyết trực tiếp (không có slide), thêm các hộp `2.1, 2.2...` như `kiem-thu-phan-mem/Moodle_HTML/01_*.html`: mỗi hộp gồm khái niệm, giải thích ngắn và **ít nhất một ví dụ thực tế**. Mỗi hộp không quá ~300 từ.

### Khối 3 - Hoạt động & Thực hành
Ba thẻ hoạt động, mỗi thẻ có tiêu đề, mô tả, nút link:
- `💬 Diễn đàn thảo luận` - một câu hỏi mở cụ thể, yêu cầu sinh viên phân tích hoặc liên hệ bản thân (không hỏi kiểu "em nghĩ sao về...").
- `📝 Trắc nghiệm nhanh (Quiz)` - mô tả phạm vi 10 câu, link quiz Moodle.
- `📤 Thực hành trên lớp` - nhiệm vụ cụ thể, sản phẩm nộp, link assign.

### Khối 4 - Góc trợ giúp và mở rộng
- **Hỗ trợ kỹ thuật:** lỗi/khó khăn sinh viên hay gặp ở bài này và cách xử lý.
- **Kiến thức mở rộng:** chủ đề hoặc nguồn để sinh viên khá giỏi tự tìm hiểu thêm.

## File bai-XX.html
Không sửa tay. Script `build-lessons.py` sinh file này từ `bai-XX.md` + `templates/lesson-page.html` + `course.json` (tiêu đề, mã học phần, nút bài trước/sau). Muốn đổi giao diện trang bài học thì sửa `templates/lesson-page.html` rồi build lại.

Tên bài trên trang web lấy từ dòng `<strong>BÀI XX - Tên bài (N tiết)</strong>` trong khối 1. Nếu tên quá dài, khai báo tên ngắn trong `lessonTitles` của `course.json`.
