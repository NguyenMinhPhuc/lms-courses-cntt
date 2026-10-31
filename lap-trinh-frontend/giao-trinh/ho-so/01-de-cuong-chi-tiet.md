# Đề cương chi tiết giáo trình

> Bước 1 của Điều 7 khoản 2 Thông tư 62/2026/TT-BGDĐT. **Dự thảo chờ duyệt**: chỉ biên soạn chương sau khi chủ biên duyệt đề cương này. Các chỗ `{{...}}` cần chủ biên cung cấp.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Tên giáo trình | Lập trình Front-End |
| Loại tài liệu | {{Giáo trình / Tài liệu học tập}} |
| Học phần | Lập trình Front-End (111100), 3 tín chỉ; 60 tiết (15 LT + 45 TH) theo kế hoạch đào tạo khóa 2024 |
| Đối tượng người học | Sinh viên Công nghệ Thông tin học kỳ 4 {{xác nhận học phần tiên quyết}} |
| Chủ biên | {{Họ tên, học hàm, học vị, đơn vị}} |
| Người biên soạn | {{Họ tên}} |
| Ngôn ngữ | Tiếng Việt |
| Hình thức khai thác | Bản số (Word/PDF) và bản in; kèm bài học LMS, quiz, thư viện prompt, đặc tả dự án Smart Event Hub |
| Căn cứ | `noi-dung-mon-hoc/De_cuong_Giang_day_Lap_trinh_Front_End.docx`; Thông tư 62/2026/TT-BGDĐT; {{quy định nội bộ của Trường, nếu có}} |

## 2. Mục tiêu của giáo trình

Hướng dẫn người học xây dựng một ứng dụng Front-End hoàn chỉnh với Next.js và TypeScript: từ wireframe, kiến trúc component, routing, giao diện với thư viện UI, quản lý trạng thái, kết nối REST API, form và lưu trữ phía client, đến tối ưu, triển khai và báo cáo; có dùng AI hỗ trợ lập trình (vibe coding) và kiểm duyệt mã do AI sinh. {{Chủ biên xác nhận hoặc chỉnh sửa.}}

## 3. Ma trận chương – chuẩn đầu ra học phần

CLO lấy từ bảng PI – CLO của Khoa (`templates/_KeHoach-Cac mon doc đánh giá các học phần.xlsx`, mã 111100, khóa 2024).

| CLO | Nội dung | PI | Chương rèn luyện chính |
|---|---|---|---|
| CLO1 | Mô hình hóa (wireframe) các phương án đề ra bằng các công cụ hiện đại | PI 1.4 | 2, 4 |
| CLO2 | Áp dụng kiến thức về HTML, CSS, JavaScript để xây dựng giao diện đáp ứng yêu cầu | PI 2.3 | 1, 3, 4, 5, 6, 8, 9, 10 |
| CLO3 | Viết báo cáo trình bày nội dung các công việc đã thực hiện bằng văn bản một cách hợp lý và đúng quy định về định dạng | PI 3.1 | 7, Phụ lục A |
| CLO4 | Sử dụng kỹ năng trong việc sắp xếp công việc cá nhân hoặc nhóm phù hợp với mục tiêu công việc đề ra | PI 5.1 | 7 (Git, phân công), 11 (CI/CD), Phụ lục A |

README của học phần diễn đạt CLO rộng hơn (nêu cụ thể Next.js, Ant Design, CI/CD). Giáo trình dùng câu chữ chính thức ở bảng trên.

## 4. Nội dung chi tiết

Dự án mẫu xuyên suốt: **Smart Event Hub** (đặt vé và quản lý sự kiện, dùng REST API có sẵn, đặc tả ở `documentation/dac-ta-du-an-smart-event-hub.md`). Mỗi chương ứng với một buổi học và kết thúc bằng mục "Vibe coding: prompt mẫu và cách kiểm duyệt mã AI" như bài giảng.

**Phần I. Nền tảng và mô hình hóa giao diện**

### Chương 1. SCSS nâng cao, TypeScript căn bản và thiết lập vibe coding (bài 01)
- 1.1. SCSS nâng cao: biến, lồng, mixin, breakpoint
- 1.2. Quy ước đặt tên BEM và CSS Modules trong Next.js
- 1.3. TypeScript căn bản cho React
- 1.4. Ví dụ: component EventCard responsive
- 1.5. Vibe coding: prompt mẫu và kiểm duyệt mã AI

### Chương 2. Wireframe, mô hình hóa giao diện và từ Figma đến component (bài 02)
- 2.1. Tư duy wireframe: phân rã giao diện thành khối bố cục
- 2.2. Mô hình hóa giao diện theo Atomic Design
- 2.3. Quy trình chuyển wireframe/Figma sang Next.js với AI thị giác
- 2.4. Làm sạch mã AI: bỏ inline style và magic number
- 2.5. Vibe coding: prompt mẫu và kiểm duyệt mã AI

**Phần II. Next.js: routing và kiến trúc component**

### Chương 3. App Router: cấu trúc thư mục và routing (bài 03)
- 3.1. Kiến trúc App Router và các file đặc biệt
- 3.2. Server Components và Client Components
- 3.3. Index, nested routes, route groups và private routes
- 3.4. Điều hướng, loading, error và trang 404
- 3.5. Vibe coding: prompt mẫu và kiểm duyệt mã AI

### Chương 4. Dynamic routing và component tái sử dụng (bài 04)
- 4.1. Dynamic segments: `[id]`, `[...slug]`, `[[...slug]]`
- 4.2. `params` và `searchParams` trong Server Component
- 4.3. Navigation hooks trong Client Component
- 4.4. Dữ liệu giả có kiểu dữ liệu chặt chẽ
- 4.5. Component tái sử dụng: composition, variant mapping, polymorphic
- 4.6. Vibe coding: prompt mẫu và kiểm duyệt mã AI

**Phần III. Giao diện chuyên nghiệp và quản lý trạng thái**

### Chương 5. Thư viện UI và tùy biến theme (bài 05)
- 5.1. Chọn thư viện UI: Ant Design, Bootstrap hay Tailwind CSS
- 5.2. Tích hợp Ant Design vào Next.js App Router
- 5.3. Tùy biến theme bằng design token và SCSS Module
- 5.4. Hệ lưới và các component nâng cao
- 5.5. Bảng quản lý: lọc, sắp xếp, phân trang
- 5.6. Vibe coding: prompt mẫu và kiểm duyệt mã AI

### Chương 6. Logic và quản lý trạng thái với React Hooks (bài 06)
- 6.1. Khi nào cần `'use client'`
- 6.2. `useState` và `useReducer`
- 6.3. `useEffect`: side effect, dependency array, cleanup
- 6.4. `useMemo`, `useCallback` và tối ưu re-render
- 6.5. Nâng state (state lifting) và debounce
- 6.6. Vibe coding: prompt mẫu và kiểm duyệt mã AI

### Chương 7. Chuẩn bị bàn giao giữa kỳ: build, README và Git (bài 07)
- 7.1. Kiểm tra bản build production: vì sao dev chạy được mà build lỗi
- 7.2. Làm sạch mã trước khi báo cáo
- 7.3. Cấu trúc README chuẩn cho đồ án
- 7.4. Conventional Commits và minh chứng đóng góp trên Git
- 7.5. Vibe coding: prompt mẫu và kiểm duyệt mã AI

**Phần IV. Dữ liệu, form và lưu trữ phía client**

### Chương 8. Lấy dữ liệu và tích hợp REST API (bài 08)
- 8.1. Lấy dữ liệu trong Server Component và Client Component
- 8.2. API an toàn kiểu: generic response, DTO, ViewModel
- 8.3. Tầng service với Axios: dữ liệu danh sách
- 8.4. Dữ liệu đơn: trang chi tiết, 404, loading, error
- 8.5. Lấy dữ liệu phía client: danh mục, đặt vé, trạng thái tải
- 8.6. Vibe coding: prompt mẫu và kiểm duyệt mã AI

### Chương 9. Kiểm tra form, Web Storage và trạng thái giao diện phức tạp (bài 09)
- 9.1. React Hook Form và Zod
- 9.2. Ví dụ: form đăng nhập với React Hook Form, Zod và Ant Design
- 9.3. Schema phức tạp với `.refine()`: form tạo sự kiện
- 9.4. Web Storage API và an toàn hydration
- 9.5. Trạng thái giao diện phức tạp: danh sách yêu thích đồng bộ nhiều component
- 9.6. Vibe coding: prompt mẫu và kiểm duyệt mã AI

**Phần V. Dự án thực tế: tối ưu và triển khai**

### Chương 10. Refactoring, tối ưu và hoàn thiện responsive (bài 10)
- 10.1. Code smell và refactoring có AI hỗ trợ
- 10.2. TypeScript strict và dọn console
- 10.3. Quy chuẩn breakpoint, sửa tràn ngang
- 10.4. Chuyển thanh lọc sang drawer trên di động
- 10.5. Xử lý dứt điểm cảnh báo console
- 10.6. Vibe coding: prompt mẫu và kiểm duyệt mã AI

### Chương 11. CI/CD, triển khai Vercel, SEO và hiệu năng (bài 11)
- 11.1. CI/CD với Vercel và quản trị biến môi trường
- 11.2. SEO với Metadata API: metadata tĩnh
- 11.3. Metadata động với `generateMetadata`
- 11.4. Hiệu năng: `next/image`, `next/dynamic`, Lighthouse
- 11.5. Vibe coding: prompt mẫu và kiểm duyệt mã AI

### Phụ lục A. Hackathon và báo cáo cuối kỳ (bài 12)
Chương trình buổi Hackathon; checklist sản phẩm nộp; kịch bản thuyết trình và demo 8 phút; chuẩn bị phản biện cá nhân; rubric 6 tiêu chí và công thức điểm.

### Phụ lục B. Mã nguồn đầy đủ
Các đoạn mã dài hơn 40 dòng của dự án Smart Event Hub (theo quy ước của giáo trình Mobile, Web).

**Thực hành mỗi chương:** câu hỏi ôn tập, bài tập; bài tập hướng dẫn `bt-XX` lấy từ mục "Thực hành trên lớp" của bài giảng, áp dụng trên Smart Event Hub.

## 5. Cân đối lý thuyết – thực hành

Học phần 15 LT + 45 TH: đề xuất khoảng **40% lý thuyết, 60% ví dụ mã nguồn, bài tập, bài tập hướng dẫn**.

## 6. Tài liệu tham khảo chính (đề xuất)

- Tài liệu gốc của học phần: `noi-dung-mon-hoc/Buoi_1…11_Lap_trinh_Front_End.docx`, `De_cuong_Giang_day_Lap_trinh_Front_End.docx`, `Rubric_Cham_Hackathon_Lap_trinh_Front_End.docx` {{tác giả}}.
- Vercel, *Next.js Documentation* (App Router). [Online]. Available: https://nextjs.org/docs
- Meta, *React Documentation*. [Online]. Available: https://react.dev
- Microsoft, *TypeScript Handbook*. [Online]. Available: https://www.typescriptlang.org/docs/handbook/
- *Sass Documentation*. [Online]. Available: https://sass-lang.com/documentation/
- Ant Group, *Ant Design Documentation*. [Online]. Available: https://ant.design
- *React Hook Form* và *Zod* documentation; *Axios* documentation.
- B. Frost, *Atomic Design*. Pittsburgh, PA: Brad Frost, 2016.

Mỗi chương sẽ ghi URL cụ thể và ngày truy cập; phiên bản Next.js ghi rõ (bài giảng hiện viết theo Next.js 15, giáo trình Web của Khoa đã ghi chú khác biệt Next.js 16).

## 7. Học liệu đi kèm

Bài học LMS `bai-01`…`bai-12`, ngân hàng câu hỏi (`quiz/`), chủ đề thảo luận (`discussion/`), bài tập (`assignment/`), thư viện prompt (`resources/`), rubric (`assessment/`), đặc tả dự án Smart Event Hub (`documentation/`).

## 8. Phân công và tiến độ

| Công việc | Người phụ trách | Thời hạn |
|---|---|---|
| Duyệt đề cương | {{...}} | {{...}} |
| Biên soạn chương 1–4 | {{...}} | {{...}} |
| Biên soạn chương 5–8 | {{...}} | {{...}} |
| Biên soạn chương 9–11, phụ lục | {{...}} | {{...}} |
| Lấy ý kiến góp ý | {{...}} | {{...}} |
| Hoàn thiện, lập hồ sơ thẩm định | {{...}} | {{...}} |

## 9. Điểm cần chủ biên quyết định

1. Học phần chưa có `course.json` nên chưa xuất hiện trên portal và chưa dùng được bộ công cụ build, validate. Có tạo `course.json` (mã 111100) không?
2. Tác giả của các file `Buoi_*.docx` để ghi nguồn đúng.
3. Giữ chương 7 (nội dung buổi giữa kỳ) như một chương kỹ thuật hay gộp vào phụ lục.
4. Loại tài liệu: Giáo trình hay Tài liệu học tập.
