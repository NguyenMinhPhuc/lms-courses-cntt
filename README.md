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
Script sẽ quét toàn bộ các thư mục con, trích xuất metadata từ `index.html` và tự động cập nhật `courses.json` & `courses-data.js`.

---

## 📁 3. Quy Ước Cấu Trúc Khi Thêm Học Phần Mới

Khi muốn bổ sung một học phần mới vào hệ thống, chỉ cần tạo một thư mục con trong thư mục gốc theo cấu trúc:

```text
lms-courses-cntt/
├── nhap-mon-nganh/                # [Học phần 1]: Nhập môn CNTT (111106)
│   ├── index.html                 # Trang mặc định của học phần (Bắt buộc)
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
├── watch-courses.py               # Script theo dõi thư mục theo thời gian thực
├── start-portal.bat               # Khởi chạy cổng 1-click
└── template-lesson.md             # Template Accordion LMS chuẩn Moodle
```

### 💡 Lưu ý về file `index.html` trong thư mục học phần mới:
- Đặt thẻ `<title>Tên Học Phần | Khoa CNTT - Đại học Lạc Hồng</title>`
- Đặt thẻ `<meta name="description" content="Mô tả tóm tắt học phần...">`
- Hệ thống sẽ tự động trích xuất Tên môn, Mô tả, Mã học phần và phân loại thẻ (tags) để hiển thị lên thẻ bài học trên Portal.
