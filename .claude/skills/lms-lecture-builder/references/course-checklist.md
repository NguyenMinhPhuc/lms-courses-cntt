# Checklist một học phần hoàn chỉnh

Thư mục học phần: `<ten-hoc-phan>/` ở gốc repo, tên viết thường không dấu, nối bằng gạch ngang.

| Thành phần | File | Ghi chú |
|---|---|---|
| Thông tin học phần | `course.json` | Mẫu ở `templates/course.example.json`; dùng cho build và portal |
| Tài liệu hướng dẫn | `README.md` | Thông tin HP, CLO, thang điểm, bảng danh sách bài, hướng dẫn import Moodle |
| Đề cương | `thong-tin-hoc-phan.md` + `.html` | Accordion; `.md` dán Moodle, `.html` xem web |
| Đánh giá | `danh-gia-hoc-phan.md` + `.html` | Hình thức đánh giá, tỉ trọng, rubric |
| Bài học | `bai-01.md` ... `bai-NN.md` + `.html` | Mỗi bài 4 khối accordion |
| Học liệu | Khối 2 của từng bài | Slide, video, tài liệu đọc thêm |
| Thảo luận | Khối 3 của từng bài | 1 chủ đề diễn đàn/bài |
| Bài tập | Khối 3 của từng bài | 1 nhiệm vụ thực hành/bài |
| Quiz | `quiz/quiz-bai-XX-aiken.txt` + file tổng hợp | ≥ 10 câu/bài |
| Dàn ý chi tiết | `dan-y-chi-tiet.md` | Chỉ khi soạn từ outline; giảng viên đã duyệt |
| Slide | `Slides/bai-XX.markdown` + `Slides/bai-XX.pptx` | Khi `"slides": true`; `.pptx` sinh bằng `build-slides.py` trên `templates/Template-slide.pptx`; có hình minh họa trong `Slides/images/`, không còn khung chờ hình |
| Landing page | `index.html` | Bắt buộc để portal nhận diện |

## `index.html` - để portal tự nhận diện
`scan-courses.py` đọc các thông tin sau, nên phải có:
- `<title>Tên Học Phần | Khoa CNTT - Đại học Lạc Hồng</title>`
- `<meta name="description" content="Mô tả ngắn học phần">`
- Chuỗi `Mã học phần: 123456` và `3 tín chỉ` xuất hiện trong trang.

## Kiểm tra trước khi báo hoàn thành
`validate-course.py` tự kiểm: đủ file, 4 khối accordion, `.html` đồng bộ `.md`, cú pháp Aiken, số câu ≥ 10, phân bố đáp án, link mẫu từ `template-lesson.md`, placeholder `{{...}}`.

Phần phải tự đọc lại:
- [ ] Số bài khớp số buổi trong đề cương.
- [ ] Đáp án quiz đúng về nội dung (script chỉ kiểm cú pháp).
- [ ] Văn phong đúng [writing-style.md](writing-style.md).
- [ ] Đã chạy `uv run python scan-courses.py` và học phần xuất hiện trong `courses.json`.
