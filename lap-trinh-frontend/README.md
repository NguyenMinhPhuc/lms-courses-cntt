# Học phần: Lập trình Front-End (Next.js, TypeScript & Vibe Coding)

- **Mã học phần:** Đang cập nhật
- **Khoa/Bộ môn phụ trách:** Khoa Công nghệ Thông tin - Trường Đại học Lạc Hồng (LHU)
- **Thời lượng:** 60 tiết (12 buổi × 5 tiết/buổi = 225 phút) – 30% lý thuyết (18 tiết), 70% thực hành & đánh giá (42 tiết)
- **Hình thức giảng dạy:** Lớp học đảo ngược (Flipped Classroom) + Học theo dự án (PBL), ứng dụng Vibe Coding với AI Assistant
- **Dự án xuyên suốt:** *Smart Event Hub* – Hệ thống Đặt vé & Quản lý Sự kiện trực tuyến (dùng RESTful API Backend/Swagger có sẵn), nhóm 3–4 sinh viên
- **Định dạng bài giảng:** theo template LMS trong [`.skill/skill.md`](../.skill/skill.md)
- **Landing page:** [index.html](index.html)
- **Đề cương chi tiết:** [thong-tin-hoc-phan.html](thong-tin-hoc-phan.html) | mã nguồn dán LMS: [thong-tin-hoc-phan.md](thong-tin-hoc-phan.md)
- **Chuyên đề Đánh giá học phần:** [danh-gia-hoc-phan.html](danh-gia-hoc-phan.html) | mã nguồn dán LMS: [danh-gia-hoc-phan.md](danh-gia-hoc-phan.md)
- **Tài liệu gốc (.docx):** [noi-dung-mon-hoc/](noi-dung-mon-hoc/)

---

## 1. Chuẩn đầu ra học phần (CLO)

| Mã CLO | Mô tả | PI (ABET) |
| :--- | :--- | :---: |
| **CLO1** | Phân tích yêu cầu, mô hình hóa UI/Wireframe và tổ chức kiến trúc component cho ứng dụng web. | PI 1.4 |
| **CLO2** | Xây dựng ứng dụng Front-End với Next.js, TypeScript, SCSS/Ant Design, quản lý state, kết nối REST API, dùng AI (Vibe Coding) có kiểm soát. | PI 2.3 |
| **CLO3** | Viết báo cáo kỹ thuật, thuyết trình và demo sản phẩm rõ ràng, chuyên nghiệp. | PI 3.1 |
| **CLO4** | Làm việc nhóm với Git (branch, PR, review), triển khai CI/CD lên Vercel và tối ưu SEO/Performance. | PI 5.1 |

## 2. Thang điểm

- **Quá trình (30%):** chuyên cần, quiz trước giờ học, bài tập trên lớp và bài tập về nhà (nộp qua Pull Request).
- **Giữa kỳ (30%) – Buổi 7:** báo cáo tiến độ 50% dự án (Wireframe, UI Ant Design/SCSS responsive, Routing & Component, Git).
- **Cuối kỳ (40%) – Buổi 12:** Thi Hackathon & Final Showcase theo rubric 6 tiêu chí. Điểm cá nhân = Điểm nhóm × 0.7 + Điểm phản biện cá nhân × 0.3.

## 3. Danh sách 12 bài học

| Buổi | Tên bài | Hình thức | Bài giảng |
| :---: | :--- | :---: | :---: |
| 01 | SCSS nâng cao, TypeScript căn bản & thiết lập Vibe Coding | Đảo ngược | [md](bai-01.md) · [html](bai-01.html) |
| 02 | Wireframe/Modeling UI & chuyển Figma thành Next.js Component | Đảo ngược | [md](bai-02.md) · [html](bai-02.html) |
| 03 | Next.js App Router: cấu trúc thư mục, Index & Nested Routing | Đảo ngược | [md](bai-03.md) · [html](bai-03.html) |
| 04 | Dynamic Routing & kiến trúc Reusable Components | Đảo ngược | [md](bai-04.md) · [html](bai-04.html) |
| 05 | Giao diện chuyên nghiệp với Ant Design, Bootstrap/Tailwind & tùy biến Theme | Đảo ngược | [md](bai-05.md) · [html](bai-05.html) |
| 06 | Logic & State Management với React Hooks | Đảo ngược | [md](bai-06.md) · [html](bai-06.html) |
| 07 | Kiểm tra giữa kỳ – Báo cáo tiến độ 50% dự án | Đánh giá 30% | [md](bai-07.md) · [html](bai-07.html) |
| 08 | Data Fetching & tích hợp RESTful API | Đảo ngược | [md](bai-08.md) · [html](bai-08.html) |
| 09 | Form Validation, Local Storage & Complex UI State | Đảo ngược | [md](bai-09.md) · [html](bai-09.html) |
| 10 | PBL 1 – Refactoring, Optimization & Responsive Polish | PBL | [md](bai-10.md) · [html](bai-10.html) |
| 11 | PBL 2 – CI/CD, Deploy Vercel, SEO & Performance | PBL | [md](bai-11.md) · [html](bai-11.html) |
| 12 | Thi Hackathon & Final Showcase | Đánh giá 40% | [md](bai-12.md) · [html](bai-12.html) |

## 4. Cấu trúc thư mục

```text
lap-trinh-frontend/
├── index.html                  # Landing page học phần (portal tự nhận diện)
├── thong-tin-hoc-phan.md/.html # Đề cương (4 Accordion LMS)
├── danh-gia-hoc-phan.md/.html  # Chuyên đề đánh giá & rubrics (4 Accordion LMS)
├── bai-01.md/.html … bai-12.md/.html
├── Moodle_HTML/                # Đoạn HTML 4 Accordion (inline style) dán thẳng vào Moodle: 00 đề cương, 01–12 bài học, 13 đánh giá
├── quiz/                       # QUIZ – ngân hàng câu hỏi Aiken (≥10 câu/bài) + file tổng hợp
├── discussion/                 # DISCUSSION – chủ đề diễn đàn & hoạt động nhóm
├── assignment/                 # ASSIGNMENT – bài tập & nhiệm vụ từng buổi
├── resources/                  # RESOURCES – tài liệu, công cụ, thư viện prompt
├── assessment/                 # ASSESSMENT – kế hoạch đánh giá, rubric, phiếu chấm
├── documentation/              # DOCUMENTATION – hướng dẫn sử dụng, đặc tả dự án
├── noi-dung-mon-hoc/           # Tài liệu gốc .docx
└── LHU_ASU_VI_Small_Ngang.png
```

> Các file `.html` (bài học, đề cương, đánh giá, tài liệu trong các thư mục con và `Moodle_HTML/`) được sinh từ file `.md` cùng tên. Khi sửa nội dung, hãy sửa file `.md` rồi build lại HTML.

## 5. Sử dụng trên LMS (Moodle)

| File Moodle | Nội dung |
| :--- | :--- |
| [00_Thong_tin_hoc_phan.html](Moodle_HTML/00_Thong_tin_hoc_phan.html) | Đề cương học phần |
| [01_SCSS_TypeScript_Vibe_Coding.html](Moodle_HTML/01_SCSS_TypeScript_Vibe_Coding.html) | Bài 01 |
| [02_Wireframe_Figma_to_NextJS.html](Moodle_HTML/02_Wireframe_Figma_to_NextJS.html) | Bài 02 |
| [03_NextJS_App_Router_Routing.html](Moodle_HTML/03_NextJS_App_Router_Routing.html) | Bài 03 |
| [04_Dynamic_Routing_Reusable_Components.html](Moodle_HTML/04_Dynamic_Routing_Reusable_Components.html) | Bài 04 |
| [05_Ant_Design_Custom_Theme.html](Moodle_HTML/05_Ant_Design_Custom_Theme.html) | Bài 05 |
| [06_State_Management_React_Hooks.html](Moodle_HTML/06_State_Management_React_Hooks.html) | Bài 06 |
| [07_Kiem_tra_giua_ky.html](Moodle_HTML/07_Kiem_tra_giua_ky.html) | Bài 07 – Giữa kỳ |
| [08_Data_Fetching_RESTful_API.html](Moodle_HTML/08_Data_Fetching_RESTful_API.html) | Bài 08 |
| [09_Form_Validation_Local_Storage.html](Moodle_HTML/09_Form_Validation_Local_Storage.html) | Bài 09 |
| [10_PBL1_Refactoring_Responsive.html](Moodle_HTML/10_PBL1_Refactoring_Responsive.html) | Bài 10 – PBL 1 |
| [11_PBL2_Deploy_Vercel_SEO.html](Moodle_HTML/11_PBL2_Deploy_Vercel_SEO.html) | Bài 11 – PBL 2 |
| [12_Hackathon_Final_Showcase.html](Moodle_HTML/12_Hackathon_Final_Showcase.html) | Bài 12 – Cuối kỳ |
| [13_Danh_gia_hoc_phan.html](Moodle_HTML/13_Danh_gia_hoc_phan.html) | Chuyên đề đánh giá & rubrics |

1. **Bài học, đề cương, đánh giá:** tạo **Page** trên Moodle, chuyển trình soạn thảo sang chế độ **HTML source (`<>`)**, dán toàn bộ nội dung file tương ứng trong `Moodle_HTML/`. Mỗi file gồm 4 khối Accordion (📘 Tổng quan · 📚 Học liệu chính · 💡 Hoạt động & Thực hành · 🆘 Trợ giúp & mở rộng), chỉ dùng inline style nên không bị Moodle lọc mất định dạng.
2. **Xem trước trên web:** mở `bai-XX.html` hoặc landing page `index.html`.
3. **Quiz:** *Question bank → Import → Aiken format*, chọn file `quiz/quiz-bai-XX-aiken.txt` (UTF-8). Chi tiết xem [documentation/huong-dan-su-dung.md](documentation/huong-dan-su-dung.md).
