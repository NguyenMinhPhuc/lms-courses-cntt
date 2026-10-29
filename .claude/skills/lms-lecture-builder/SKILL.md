---
name: lms-lecture-builder
description: Soạn và chuẩn hóa nội dung học phần cho LMS Moodle của Khoa CNTT - Đại học Lạc Hồng từ tài liệu thô (PDF, DOCX, slide, đề cương) hoặc chỉ từ outline/đề cương khi chưa có slide. Tạo dàn ý chi tiết, bài học dạng accordion HTML 4 phần (bai-XX.md + bai-XX.html), slide bài giảng (ghi chú Markdown + PowerPoint .pptx), ngân hàng câu hỏi Aiken, đề cương, trang đánh giá và landing page theo cấu trúc thư mục của repo. Dùng khi người dùng yêu cầu soạn bài giảng, làm slide, tạo bài học/học phần mới, chuyển tài liệu thành nội dung LMS/Moodle, tạo quiz Aiken, hoặc kiểm tra một học phần đã đủ thành phần chưa.
---

# LMS Lecture Builder (Khoa CNTT - LHU)

Skill này biến tài liệu của giảng viên thành một thư mục học phần hoàn chỉnh, dán được thẳng vào Moodle (`learn.lhu.edu.vn`) và hiển thị được trên portal của repo.

Học phần mẫu: `nhap-mon-nganh/` (nội dung có slide nguồn) và `kiem-thu-phan-mem/` (lý thuyết viết trực tiếp trong khối 2, có trang đề cương và đánh giá sinh tự động). Khi phân vân về định dạng, mở file tương ứng trong hai thư mục đó làm chuẩn.

## Xác định chế độ làm việc

- **Có tài liệu nguồn** (slide, giáo trình): soạn nội dung bám theo tài liệu, bỏ qua bước 2b.
- **Chỉ có outline hoặc đề cương:** bắt buộc làm bước 2b. Viết dàn ý chi tiết, **dừng lại chờ giảng viên duyệt** rồi mới viết bài. Kiến thức chuyên môn lúc này do Claude soạn, nên phải chính xác và phù hợp trình độ sinh viên. Không được bịa thông tin hành chính.

## Quy trình

Làm theo thứ tự, mỗi bước xong mới sang bước sau:

1. **Thu thập đầu vào.** Xác định tên học phần, mã học phần, số tín chỉ (LT/TH), số buổi, CLO, tỷ trọng đánh giá, giảng viên. Nếu thiếu thông tin bắt buộc, hỏi người dùng; không tự bịa mã học phần, link Moodle, link diễn đàn hay số liệu về Khoa. Ghi vào `<hoc-phan>/course.json` (mẫu: `templates/course.example.json`), bật `"coursePages": true` và `"slides": true` nếu cần làm slide.
2. **Đọc tài liệu nguồn** trong thư mục học phần (PDF, DOCX, slide, outline).
   - **2b. Dàn ý chi tiết (khi chỉ có outline):** tạo `<hoc-phan>/dan-y-chi-tiet.md` theo [references/detailed-outline.md](references/detailed-outline.md). Trình bày tóm tắt cho giảng viên và **chờ xác nhận**. Chỉ sang bước 3 khi giảng viên đồng ý hoặc đã sửa xong dàn ý.
3. **Đề cương:** tạo `thong-tin-hoc-phan.md`, `danh-gia-hoc-phan.md` và `README.md` của học phần (danh sách bài, CLO, thang điểm, rubric).
4. **Từng bài học:** tạo `bai-XX.md` theo [references/lesson-structure.md](references/lesson-structure.md), văn phong theo [references/writing-style.md](references/writing-style.md). Khi không có slide nguồn, viết lý thuyết trực tiếp trong khối 2 (các hộp 2.1, 2.2…).
5. **Slide (khi `"slides": true`):** từ `bai-XX.md` đã duyệt, viết `Slides/bai-XX.markdown` theo [references/slides.md](references/slides.md), rồi chạy `uv run --with python-pptx python build-slides.py <hoc-phan>` để sinh `Slides/bai-XX.pptx`. Không viết tay file `.pptx`.
6. **Quiz:** tạo `quiz/quiz-bai-XX-aiken.txt` theo [references/quiz-aiken.md](references/quiz-aiken.md), sau đó chạy `uv run python build-quiz.py <hoc-phan> --balance`. Script này chia đều vị trí đáp án, ghép file tổng hợp và sinh `quiz/index.html` (trang cho giảng viên tải file Aiken để import Moodle). Không ghép tay. Mỗi file quiz là nguồn cho **hai** đầu ra:
   - **Import Moodle:** giảng viên tải file `.txt` ở `quiz/index.html` (link "Ngân hàng câu hỏi" trên thẻ học phần ở portal).
   - **Luyện tập trên web:** `build-lessons.py` nhúng đề vào cuối `bai-XX.html`. Sinh viên làm bài trực tiếp, chỉ được báo số câu đúng/sai/bỏ trống; không lưu kết quả, không hiển thị đáp án. Câu hỏi **không** được liệt kê trong nội dung bài học. Sau khi sửa quiz phải build lại trang bài học.
7. **Trang web:**
   - `bai-XX.html`, `thong-tin-hoc-phan.html`, `danh-gia-hoc-phan.html`: **không viết tay**. Chạy `uv run python build-lessons.py <hoc-phan>`.
   - `index.html` (landing page): sao chép từ học phần mẫu rồi sửa nội dung; giữ `<title>` và `<meta name="description">`.
   - Hook trong `.claude/settings.json` tự build lại khi sửa `bai-XX.md`, đề cương, đánh giá, quiz hoặc `Slides/bai-XX.markdown`, nhưng vẫn chạy lại các lệnh build trước khi kiểm tra.
7b. **Giáo trình nội bộ (khi giảng viên yêu cầu):** mỗi bài một chương trong `<hoc-phan>/giao-trinh/chuong-XX.md` (kèm `00-loi-noi-dau.md`), mở rộng từ `bai-XX.md` đã duyệt: mục tiêu, lý thuyết chi tiết, mã nguồn ví dụ đầy đủ, tóm tắt, câu hỏi ôn tập, bài tập, tài liệu tham khảo chính thức. Chỉ dùng Markdown mà `build-textbook.py` hỗ trợ (tiêu đề, đoạn, danh sách, bảng, khối code, trích dẫn). Xuất Word: `uv run --with python-docx python build-textbook.py <hoc-phan>`; mở trong Word và cập nhật mục lục. Nội dung giáo trình phải khớp với bài học và slide; sửa một nơi thì sửa cả nơi kia.
8. **Đăng ký portal:** chạy `uv run python scan-courses.py` ở gốc repo để cập nhật `courses.json` và `courses-data.js`.
9. **Tự kiểm tra:** chạy `uv run python validate-course.py <hoc-phan>`. Sửa hết mọi `[LỖI]` rồi chạy lại. Báo cho người dùng các `[CẢNH BÁO]` còn lại, đặc biệt là placeholder chưa điền và link chép từ template. Những mục script không tự kiểm được thì xem [references/course-checklist.md](references/course-checklist.md).

Khi người dùng chỉ yêu cầu một phần (ví dụ "soạn bài 3", "làm slide bài 2" hoặc "tạo quiz bài 5"), chỉ làm bước tương ứng nhưng vẫn tuân thủ định dạng. Với học phần nhiều buổi, nên làm theo đợt (ví dụ bài 1–3) và để giảng viên duyệt trước khi làm tiếp.

## Quy tắc bắt buộc

- **Không bịa link.** Link Moodle (quiz, assign), diễn đàn, Gamma, YouTube chưa có thì để placeholder dạng `{{LINK_QUIZ_BAI_XX}}` và liệt kê lại cuối câu trả lời. Link trong `template-lesson.md` chỉ là ví dụ của học phần khác, không được tái sử dụng.
- **Không bịa dữ kiện** về trường, khoa, chuẩn ABET, số liệu việc làm. Chỉ dùng thông tin có trong tài liệu nguồn hoặc người dùng cung cấp.
- **Một nguồn nội dung:** slide và quiz phải bám theo `bai-XX.md`. Sửa nội dung thì sửa `bai-XX.md` trước, rồi cập nhật slide và quiz theo.
- **HTML dán được vào Moodle:** chỉ dùng inline style, thẻ `<details>/<summary>`, không `<script>`, không class Tailwind trong file `.md`. Tailwind/JS chỉ được dùng ở khung trang `.html`.
- **Mã hóa UTF-8** cho mọi file (tiếng Việt có dấu).
- **Đặt tên file** đúng quy ước: `bai-01.md`, `bai-01.html`, `Slides/bai-01.markdown`, `Slides/bai-01.pptx`, `quiz/quiz-bai-01-aiken.txt` (số 2 chữ số).
