# LMS Courses CNTT - Cổng Học Phần Khoa Công Nghệ Thông Tin (LHU)

Hệ thống quản lý và tổng hợp các học phần thuộc Khoa Công nghệ Thông tin - Trường Đại học Lạc Hồng (LHU). Đào tạo theo chuẩn kiểm định quốc tế **ABET (Hoa Kỳ)**, tiên phong phương pháp **AI-First & Vibe Coding**.

---

## 🌟 1. Trang Tổng Hợp Các Học Phần (Master Course Portal)
- **Trang chủ cổng học phần:** [`index.html`](file:///d:/Projects/CongTy/gitproject/lms-courses-cntt/index.html) (tại thư mục gốc).
- **Cơ chế tự động nhận diện:** Khi thêm bất kỳ thư mục học phần mới nào có chứa file `index.html`, trang tổng hợp sẽ **tự động quét và hiển thị lên danh sách** mà không cần chỉnh sửa mã nguồn của trang tổng hợp.

---

## 🚀 2. Cách Chạy Cổng Học Phần Tự Động Nhận Diện

### Cách 1: Khởi động 1-Click bằng file `.bat` (Khuyên dùng trên Windows)
- Click đúp vào file **[`start-portal.bat`](file:///d:/Projects/CongTy/gitproject/lms-courses-cntt/start-portal.bat)**.
- Hệ thống sẽ tự động quét thư mục và mở trình duyệt tại `http://localhost:8000/index.html`.
- Khi bạn thêm một thư mục mới (ví dụ `lap-trinh-web/`), chỉ cần nhấn F5 (Tải lại trang) là học phần mới tự động xuất hiện!

### Cách 2: Mở trực tiếp file `index.html` trong trình duyệt
- Mở file [`index.html`](file:///d:/Projects/CongTy/gitproject/lms-courses-cntt/index.html) bằng Chrome hoặc Edge.
- Nhấp nút **"Chọn thư mục để quét"** (sử dụng Native File System Access API), chọn thư mục `lms-courses-cntt`. Trình duyệt sẽ duyệt tự động toàn bộ cây thư mục và lưu vào bộ nhớ cache.

### Cách 3: Chạy script quét thủ công
```bash
uv run python scan-courses.py
```
Script sẽ quét toàn bộ các thư mục con, trích xuất metadata từ `index.html` (ưu tiên `course.json` nếu có) và tự động cập nhật `courses.json` & `courses-data.js`.

---

## 🛠️ 2b. Build & Kiểm tra Học phần

| Lệnh | Tác dụng |
| :--- | :--- |
| `uv run python build-lessons.py <hoc-phan>` | Sinh `bai-XX.html` từ `bai-XX.md` theo khung `templates/lesson-page.html`. Bỏ tên thư mục để build mọi học phần có `course.json`. |
| `uv run python build-lessons.py --check <hoc-phan>` | Chỉ kiểm tra `.html` có khớp `.md` không, không ghi file. |
| `uv run --with python-pptx python build-slides.py <hoc-phan> [XX]` | Sinh `Slides/bai-XX.pptx` từ ghi chú slide `Slides/bai-XX.markdown` (khi `course.json` có `"slides": true`). |
| `uv run --with python-docx python build-textbook.py <hoc-phan>` | Ghép giáo trình nội bộ `<hoc-phan>/giao-trinh/*.md` thành file Word có trang bìa và mục lục (mở bằng Word, nhấn F9 ở mục lục để cập nhật số trang). |
| `uv run python build-quiz.py <hoc-phan> [--balance]` | Ghép các file `quiz-bai-XX-aiken.txt` thành file tổng hợp và sinh trang tải `quiz/index.html` cho giảng viên; `--balance` chia đều vị trí đáp án đúng A/B/C/D (không đổi nội dung). |
| `uv run python validate-course.py <hoc-phan>` | Kiểm tra đủ file, 4 khối accordion, cú pháp quiz Aiken, link mẫu chép nhầm, placeholder chưa điền. |

Quy trình: chỉ sửa `bai-XX.md` / file quiz → chạy `build-lessons.py` và `build-quiz.py` → chạy `validate-course.py` → chạy `scan-courses.py`.

Trang `bai-XX.html` có khung **Luyện tập trắc nghiệm** sinh từ file quiz của bài: sinh viên làm trực tiếp, chỉ được báo số câu đúng/sai, không lưu kết quả và không hiển thị đáp án. Giảng viên tải file Aiken để import Moodle qua link **Ngân hàng câu hỏi** trên thẻ học phần.

Khi làm việc với Claude Code, hook trong `.claude/settings.json` tự chạy `build-lessons.py` / `build-quiz.py` ngay sau khi Claude sửa `bai-XX.md`, `thong-tin-hoc-phan.md`, `danh-gia-hoc-phan.md` hoặc file quiz.

Skill soạn bài giảng cho Claude Code nằm tại `.claude/skills/lms-lecture-builder/`, được kích hoạt khi yêu cầu Claude soạn bài/học phần LMS. Skill làm được cả khi chỉ có outline/đề cương (soạn dàn ý chi tiết để giảng viên duyệt trước) và làm slide PowerPoint.

📘 **Hướng dẫn từng bước cho giảng viên:** [`huong-dan-soan-bai-giang.html`](huong-dan-soan-bai-giang.html) (có nút truy cập trên trang chủ portal).

---

## 📁 3. Quy Ước Cấu Trúc Khi Thêm Học Phần Mới

Khi muốn bổ sung một học phần mới vào hệ thống, chỉ cần tạo một thư mục con trong thư mục gốc theo cấu trúc:

```text
lms-courses-cntt/
├── nhap-mon-nganh/                # [Học phần 1]: Nhập môn CNTT (111106)
│   ├── index.html                 # Trang mặc định của học phần (Bắt buộc)
│   ├── course.json                # Mã, tín chỉ, giảng viên... (dùng cho build & portal)
│   ├── course-landingpage.html    # Trang landing page chi tiết học phần
│   ├── thong-tin-hoc-phan.html    # Đề cương chi tiết (4 Accordion LMS)
│   ├── danh-gia-hoc-phan.html     # Chuyên đề Đánh giá học phần & Rubrics
│   ├── bai-01.html ... bai-09.html
│   └── quiz/                      # Ngân hàng câu hỏi Aiken
│
├── [ten-hoc-phan-moi]/            # [Học phần mới]: Ví dụ lap-trinh-web, co-so-du-lieu
│   ├── index.html                 # Trang mặc định của học phần (Bắt buộc)
│   ├── thong-tin-hoc-phan.html    # (Tùy chọn)
│   └── ...
│
├── index.html                     # TRANG TỔNG HỢP CÁC HỌC PHẦN (PORTAL GỐC)
├── courses.json                   # Cơ sở dữ liệu danh mục học phần
├── courses-data.js                # Dữ liệu dự phòng cho giao thức file:///
├── scan-courses.py                # Script tự động quét và phân tích thư mục
├── build-lessons.py               # Sinh bai-XX.html từ bai-XX.md
├── build-quiz.py                  # Ghép & cân bằng ngân hàng câu hỏi Aiken
├── build-slides.py                # Sinh slide .pptx từ ghi chú slide Markdown
├── build-textbook.py              # Ghép giáo trình Markdown thành file Word
├── huong-dan-soan-bai-giang.html  # Trang hướng dẫn quy trình soạn bài giảng
├── validate-course.py             # Kiểm tra học phần đủ thành phần & đúng định dạng
├── templates/                     # Khung trang bài học + mẫu course.json
├── watch-courses.py               # Script theo dõi thư mục theo thời gian thực
├── start-portal.bat               # Khởi chạy cổng 1-click
└── template-lesson.md             # Template Accordion LMS chuẩn Moodle
```

### 💡 Lưu ý về file `index.html` trong thư mục học phần mới:
- Đặt thẻ `<title>Tên Học Phần | Khoa CNTT - Đại học Lạc Hồng</title>`
- Đặt thẻ `<meta name="description" content="Mô tả tóm tắt học phần...">`
- Hệ thống sẽ tự động trích xuất Tên môn, Mô tả, Mã học phần và phân loại thẻ (tags) để hiển thị lên thẻ bài học trên Portal.
