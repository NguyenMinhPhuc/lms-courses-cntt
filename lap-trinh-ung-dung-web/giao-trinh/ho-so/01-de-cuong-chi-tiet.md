# Đề cương chi tiết giáo trình

> Đề cương lập **hồi cứu** từ bản thảo đã biên soạn (bước 1, Điều 7 khoản 2 Thông tư 62/2026/TT-BGDĐT), để làm căn cứ lấy ý kiến và thẩm định. Nội dung cấu trúc dưới đây sinh tự động từ các file chương; số trang ước tính theo 350 từ/trang.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Tên tài liệu | Giáo trình Lập trình ứng dụng web |
| Loại tài liệu | Giáo trình |
| Học phần | Lập trình ứng dụng web (111102), 3 tín chỉ; 60 tiết (15 LT + 45 TH) |
| Đối tượng người học | Sinh viên Công nghệ Thông tin học kỳ 6; đã học Thiết kế UI/UX, Thiết kế Web, Lập trình Frontend (React), Lập trình Backend |
| Chủ biên | {{Họ tên, học hàm, học vị, đơn vị}} |
| Người biên soạn | {{Họ tên}} (giảng viên phụ trách học phần theo course.json: ThS. Nguyễn Minh Phúc) |
| Ngôn ngữ | Tiếng Việt |
| Hình thức khai thác | Bản số (Word/PDF) và bản in; kèm học liệu số trên LMS |
| Căn cứ | Đề cương học phần; Thông tư 62/2026/TT-BGDĐT; {{quy định nội bộ của Trường về biên soạn giáo trình, nếu có}} |

## 2. Mục tiêu của tài liệu

{{Hai đến bốn câu do chủ biên xác nhận; tham khảo đoạn mở đầu của Lời nói đầu.}}

## 3. Ma trận chương – chuẩn đầu ra học phần

| CLO | Nội dung | Rèn luyện ở |
|---|---|---|
| CLO1 | Phân tích các thành phần chức năng của ứng dụng web phù hợp với mô hình đã phân tích | Sitemap, ánh xạ route (Chương 2), ranh giới Server/Client (Chương 3–4), ma trận phân quyền (Chương 5), module quản trị (Chương 7), sơ đồ tuần tự (Chương 9) |
| CLO2 | Thực hiện các bài kiểm thử để kiểm tra các yêu cầu chức năng phù hợp với các mục tiêu dự án | Test case từ tiêu chí chấp nhận (Chương 3), giá trị biên (Chương 4), truy cập trái phép (Chương 5), luồng nghiệp vụ (Chương 6), kiểm thử tự động (Chương 10) |
| CLO3 | Viết báo cáo trình bày công việc đã thực hiện hợp lý và đúng quy định về định dạng | Báo cáo sprint (Chương 3, 6, 9), báo cáo đồ án (Chương 11) |
| CLO4 | Sắp xếp công việc cá nhân hoặc nhóm phù hợp với mục tiêu đề ra | Kế hoạch sprint (Chương 1), velocity (Chương 6), kế hoạch Sprint 4 (Chương 9), tổng kết tiến độ (Chương 11) |

## 4. Nội dung chi tiết

### Chương 1. Ứng dụng web hiện đại với Next.js và khởi động dự án

**Mục tiêu:**

- So sánh các mô hình render web: CSR, SSR, SSG/ISR và React Server Components.
- Giải thích vai trò của Next.js App Router và cấu trúc thư mục `app/`.
- Tạo dự án Next.js với TypeScript, Tailwind CSS và ESLint.
- Phân tích phạm vi web của LHU Food từ SRS và truy vết trang tới user story.
- Lập kế hoạch Sprint 1, tổ chức board công việc và viết file quy ước cho trợ lý AI.

**Nội dung:**

- 1.1. Từ trang web đến ứng dụng web
  - 1.1.1. Ứng dụng web khác trang web ở đâu
  - 1.1.2. Các mô hình render
  - 1.1.3. React Server Components
- 1.2. Next.js App Router
  - 1.2.1. Tạo dự án
  - 1.2.2. Điều hướng theo thư mục
  - 1.2.3. App Router và Pages Router
  - 1.2.4. Next.js thay đổi theo phiên bản
- 1.3. Phân tích phạm vi web của LHU Food
  - 1.3.1. Kiến trúc tổng thể
  - 1.3.2. Phân vai giữa web và mobile
  - 1.3.3. Truy vết trang tới user story
  - 1.3.4. Backend theo từng sprint
- 1.4. Lập kế hoạch dự án
  - 1.4.1. Product Backlog dùng chung
  - 1.4.2. Kế hoạch Sprint 1 (CLO4)
  - 1.4.3. Phân vai và quy trình Git
- 1.5. Vibe coding với Next.js
  - 1.5.1. File quy ước cho trợ lý AI
  - 1.5.2. Lỗi AI hay mắc với Next.js

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-01`.
**Liên kết học liệu:** bài học `bai-01`, slide `Slides/bai-01.pptx`, quiz bài 01.
**Dung lượng ước tính:** khoảng 8 trang; tài liệu tham khảo: 4.

### Chương 2. Routing, layout và giao diện với Tailwind CSS

**Mục tiêu:**

- Phân tích chức năng của ứng dụng thành sơ đồ chức năng, sitemap và bảng ánh xạ route – chức năng – vai trò – API.
- Tổ chức route bằng thư mục, route group và route động của App Router.
- Dùng các file đặc biệt `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`.
- Xây dựng layout riêng cho khu vực khách và khu vực quản trị.
- Xây dựng giao diện responsive bằng Tailwind CSS và component shadcn/ui.

**Nội dung:**

- 2.1. Phân tích trước khi code
  - 2.1.1. Sơ đồ chức năng
  - 2.1.2. Sitemap và bảng ánh xạ route
- 2.2. Routing của App Router
  - 2.2.1. Cây thư mục của LHU Food
  - 2.2.2. Route group
  - 2.2.3. Route động
  - 2.2.4. Các file đặc biệt
  - 2.2.5. Điều hướng
- 2.3. Layout dùng chung và cây component
  - 2.3.1. Layout quản trị
  - 2.3.2. Cây component
- 2.4. Tailwind CSS
  - 2.4.1. Utility class
  - 2.4.2. Mobile-first và responsive
  - 2.4.3. Lưu ý khi viết class
- 2.5. shadcn/ui
  - 2.5.1. Khác thư viện UI thông thường
  - 2.5.2. Từ Figma đến mã bằng vibe coding

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-02`.
**Liên kết học liệu:** bài học `bai-02`, slide `Slides/bai-02.pptx`, quiz bài 02.
**Dung lượng ước tính:** khoảng 6 trang; tài liệu tham khảo: 7.

### Chương 3. Server Components và lấy dữ liệu từ API

**Mục tiêu:**

- Phân biệt Server Component và Client Component, xác định ranh giới `"use client"` trên một trang.
- Lấy dữ liệu từ API trong Server Component với biến môi trường và kiểu TypeScript.
- Chọn cách cache và thời gian `revalidate` phù hợp với mức thay đổi của dữ liệu.
- Xử lý trạng thái tải, lỗi và rỗng bằng `loading.tsx`, `Suspense`, `error.tsx`.
- Viết test case từ tiêu chí chấp nhận, viết báo cáo sprint và lập kế hoạch sprint tiếp theo.

**Nội dung:**

- 3.1. Server Component và Client Component
  - 3.1.1. So sánh
  - 3.1.2. Ranh giới "use client"
- 3.2. Lấy dữ liệu từ API
  - 3.2.1. Biến môi trường
  - 3.2.2. Kiểu dữ liệu và hàm gọi API tập trung
  - 3.2.3. Trang thực đơn
- 3.3. Cache và làm mới dữ liệu
  - 3.3.1. Mặc định từ Next.js 15
  - 3.3.2. Chọn thời gian theo mức thay đổi của dữ liệu
- 3.4. Trạng thái tải và lỗi
  - 3.4.1. File loading.tsx và streaming
  - 3.4.2. File error.tsx
- 3.5. Kiểm thử và báo cáo sprint
  - 3.5.1. Test case từ tiêu chí chấp nhận (CLO2)
  - 3.5.2. Báo cáo sprint (CLO3)
  - 3.5.3. Sprint Review và kế hoạch Sprint 2 (CLO4)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-03`.
**Liên kết học liệu:** bài học `bai-03`, slide `Slides/bai-03.pptx`, quiz bài 03.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 6.

### Chương 4. Client Components, trạng thái và form

**Mục tiêu:**

- Phân tích phần nào của trang cần chạy phía client và giữ phần đó nhỏ nhất.
- Phân biệt các loại trạng thái và quản lý giỏ hàng bằng Zustand có lưu vào `localStorage`.
- Nhận diện và xử lý lỗi hydration.
- Xây dựng form kiểm tra dữ liệu ở cả client và server bằng một schema Zod dùng chung.
- Gọi API ghi dữ liệu qua Server Action, xử lý lỗi 400/409, thiết kế test case giá trị biên.

**Nội dung:**

- 4.1. Client Component và "đảo tương tác"
  - 4.1.1. Khi nào cần Client Component
  - 4.1.2. Đảo tương tác
- 4.2. Trạng thái của ứng dụng web
  - 4.2.1. Ba loại trạng thái
  - 4.2.2. Giỏ hàng với Zustand
  - 4.2.3. Giá trong giỏ không phải giá tính tiền
- 4.3. Lỗi hydration
  - 4.3.1. Hydration là gì
  - 4.3.2. Giỏ hàng gây lỗi hydration thế nào
- 4.4. Form có kiểm tra dữ liệu
  - 4.4.1. Kiểm tra ở hai phía
  - 4.4.2. Server Action
  - 4.4.3. Form với React Hook Form
- 4.5. Ghi dữ liệu qua API và kiểm thử form
  - 4.5.1. Đặt món qua API mẫu
  - 4.5.2. Phân tích giá trị biên (CLO2)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-04`.
**Liên kết học liệu:** bài học `bai-04`, slide `Slides/bai-04.pptx`, quiz bài 04.
**Dung lượng ước tính:** khoảng 6 trang; tài liệu tham khảo: 6.

### Chương 5. Xác thực, phân quyền và bảo mật web

**Mục tiêu:**

- Phân biệt xác thực và phân quyền; mô tả luồng đăng nhập bằng JWT trên web.
- Lưu access token và refresh token trong cookie `httpOnly`, `Secure`, `SameSite`.
- Phân tích yêu cầu phân quyền thành ma trận vai trò × chức năng.
- Bảo vệ route bằng `proxy.ts` và kiểm tra lại quyền ở server qua Data Access Layer.
- Làm mới token, đăng xuất, gọi API kèm token từ server.
- Nhận diện các rủi ro bảo mật web phổ biến và viết test case truy cập trái phép.

**Nội dung:**

- 5.1. Xác thực và phân quyền
- 5.2. Luồng xác thực trên web và cookie httpOnly
  - 5.2.1. Luồng tổng quát
  - 5.2.2. Vì sao là cookie httpOnly
  - 5.2.3. Quản lý cookie phiên
  - 5.2.4. Đăng nhập bằng Server Action
- 5.3. Phân tích phân quyền
  - 5.3.1. Ma trận vai trò × chức năng (CLO1)
  - 5.3.2. Ẩn menu không phải là phân quyền
- 5.4. Bảo vệ route theo ba lớp
  - 5.4.1. Lớp 1: proxy.ts
  - 5.4.2. Vì sao không dừng ở proxy
  - 5.4.3. Lớp 2: Data Access Layer
  - 5.4.4. Lớp 3: API
- 5.5. Gọi API kèm token, làm mới token và đăng xuất
  - 5.5.1. Hàm gọi API có xác thực
  - 5.5.2. Làm mới token
  - 5.5.3. Đăng xuất
- 5.6. Rủi ro bảo mật web
  - 5.6.1. OWASP Top 10
  - 5.6.2. Server Action là endpoint công khai
- 5.7. Test case phân quyền và bảo mật (CLO2)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-05`.
**Liên kết học liệu:** bài học `bai-05`, slide `Slides/bai-05.pptx`, quiz bài 05.
**Dung lượng ước tính:** khoảng 8 trang; tài liệu tham khảo: 7.

### Chương 6. Server Actions, bảng dữ liệu và màn hình quầy

**Mục tiêu:**

- Thực hiện thao tác ghi dữ liệu bằng Server Actions với `useActionState`, `revalidatePath` và `useOptimistic`.
- Xây dựng bảng dữ liệu có sắp xếp, lọc và phân trang theo tham số URL bằng TanStack Table.
- Phân tích nghiệp vụ trạng thái đơn và xây dựng màn hình quầy đúng trình tự, xử lý xung đột 409.
- Kiểm thử luồng nghiệp vụ "khách đặt → nhân viên xử lý" theo tiêu chí chấp nhận.
- Tính velocity và lập kế hoạch sprint dựa trên số liệu thực tế.

**Nội dung:**

- 6.1. Server Actions
  - 6.1.1. Khái niệm
  - 6.1.2. Server Action của màn hình quầy
  - 6.1.3. Hook useActionState
  - 6.1.4. Hàm revalidatePath
  - 6.1.5. Hook useOptimistic
- 6.2. Bảng dữ liệu với TanStack Table
  - 6.2.1. Trạng thái bảng nằm ở đâu
  - 6.2.2. Server Component lấy dữ liệu
  - 6.2.3. Client Component hiển thị bảng
- 6.3. Màn hình quầy
  - 6.3.1. Phân tích nghiệp vụ trạng thái đơn (CLO1)
  - 6.3.2. Bố cục
  - 6.3.3. Thẻ đơn với cập nhật lạc quan
  - 6.3.4. Xung đột khi hai nhân viên cùng thao tác
- 6.4. Kiểm thử luồng nghiệp vụ và báo cáo Sprint 2
  - 6.4.1. Test case luồng "khách đặt → nhân viên xử lý" (CLO2)
  - 6.4.2. Velocity (CLO4)
  - 6.4.3. Báo cáo Sprint 2 (CLO3)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-06`.
**Liên kết học liệu:** bài học `bai-06`, slide `Slides/bai-06.pptx`, quiz bài 06.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 6.

### Chương 7. Module quản trị trên backend của nhóm

**Mục tiêu:**

- Phân tích nghiệp vụ quản trị từ SRS thành thay đổi CSDL, stored procedure, API và trang web.
- Tìm khoảng trống giữa backend hiện có và yêu cầu mới.
- Viết script CSDL phiên bản mới, chạy lại nhiều lần không lỗi.
- Viết stored procedure quản trị có ràng buộc nghiệp vụ và mã lỗi thống nhất.
- Xây dựng API quản trị trên NestJS có phân quyền `admin` và tài liệu Swagger.
- So khớp hợp đồng API, chuyển web sang backend của nhóm và kiểm thử hồi quy.

**Nội dung:**

- 7.1. Phân tích nghiệp vụ quản trị
  - 7.1.1. Năm tầng của một story quản trị
  - 7.1.2. Khoảng trống của backend hiện tại
- 7.2. Script CSDL theo phiên bản
  - 7.2.1. Quy tắc
  - 7.2.2. Mở rộng vai trò và khóa tài khoản
- 7.3. Stored procedure quản trị
  - 7.3.1. Ràng buộc nghiệp vụ trong thủ tục
  - 7.3.2. Mã lỗi thống nhất
  - 7.3.3. Danh mục stored procedure
- 7.4. API quản trị trên NestJS
  - 7.4.1. Controller và DTO
  - 7.4.2. Phân quyền admin
  - 7.4.3. Khóa tài khoản trong luồng xác thực
  - 7.4.4. Swagger là hợp đồng
- 7.5. Chuyển web sang backend của nhóm
  - 7.5.1. So khớp hợp đồng API
  - 7.5.2. Hai cách xử lý khác biệt
  - 7.5.3. Kiểm thử hồi quy
  - 7.5.4. Trang quản lý danh mục

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-07`.
**Liên kết học liệu:** bài học `bai-07`, slide `Slides/bai-07.pptx`, quiz bài 07.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 4.

### Chương 8. Trang quản trị: CRUD, tải ảnh, báo cáo và biểu đồ

**Mục tiêu:**

- Xây dựng trang quản trị CRUD theo một mẫu thống nhất với form dùng chung cho tạo và sửa.
- Tải ảnh lên API qua Server Action, kiểm tra định dạng và dung lượng ở nhiều lớp.
- Trình bày số liệu báo cáo bằng biểu đồ phù hợp với câu hỏi cần trả lời.
- Xuất dữ liệu thành file CSV mở được bằng Excel qua Route Handler.
- Xây dựng trang quản lý tài khoản nhân viên và kiểm thử các ràng buộc nghiệp vụ quản trị.

**Nội dung:**

- 8.1. Mẫu trang CRUD
  - 8.1.1. Một cấu trúc cho mọi trang quản trị
  - 8.1.2. Một Server Action cho tạo và sửa
  - 8.1.3. Xóa, ngừng bán và xác nhận
- 8.2. Tải ảnh món
  - 8.2.1. Luồng tải ảnh
  - 8.2.2. Server Action tải ảnh
  - 8.2.3. Cấu hình Next.js
  - 8.2.4. Xem trước và kiểm tra ba lớp
- 8.3. Báo cáo và biểu đồ
  - 8.3.1. Lấy dữ liệu báo cáo
  - 8.3.2. Chọn biểu đồ theo câu hỏi
  - 8.3.3. Biểu đồ với Recharts
  - 8.3.4. Số liệu phải khớp CSDL
- 8.4. Xuất CSV
- 8.5. Tài khoản nhân viên và test case quản trị
  - 8.5.1. Trang tài khoản nhân viên
  - 8.5.2. Test case quản trị (CLO2)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-08`.
**Liên kết học liệu:** bài học `bai-08`, slide `Slides/bai-08.pptx`, quiz bài 08.
**Dung lượng ước tính:** khoảng 6 trang; tài liệu tham khảo: 6.

### Chương 9. Màn hình quầy thời gian thực với Socket.IO

**Mục tiêu:**

- So sánh làm mới định kỳ (polling) và kết nối thời gian thực cho màn hình quầy.
- Tích hợp Socket.IO vào Client Component của Next.js với xác thực bằng access token.
- Xử lý kết nối lại, token hết hạn và làm mới dữ liệu sau khi mất kết nối.
- Phân tích luồng realtime giữa web, mobile và backend bằng sơ đồ tuần tự.
- Kiểm thử realtime với nhiều phiên; báo cáo Sprint 3 và điều chỉnh kế hoạch Sprint 4.

**Nội dung:**

- 9.1. Từ làm mới định kỳ đến thời gian thực
  - 9.1.1. Giới hạn của polling
  - 9.1.2. Socket.IO
  - 9.1.3. Hai quy tắc giữ nguyên trên web
- 9.2. Socket.IO trong Next.js
  - 9.2.1. Những điểm khác so với ứng dụng di động
  - 9.2.2. Route Handler cấp token cho socket
- 9.3. Màn hình quầy realtime
  - 9.3.1. Socket là chuông báo
  - 9.3.2. Phân tích các quyết định
  - 9.3.3. Backend nhóm cần bổ sung
- 9.4. Sơ đồ tuần tự
  - 9.4.1. Vì sao cần sơ đồ tuần tự
  - 9.4.2. Luồng đặt món và xử lý
- 9.5. Kiểm thử realtime và báo cáo Sprint 3
  - 9.5.1. Chuẩn bị
  - 9.5.2. Test case realtime (CLO2)
  - 9.5.3. Báo cáo Sprint 3 (CLO3)
  - 9.5.4. Điều chỉnh kế hoạch Sprint 4 (CLO4)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-09`.
**Liên kết học liệu:** bài học `bai-09`, slide `Slides/bai-09.pptx`, quiz bài 09.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 5.

### Chương 10. Kiểm thử ứng dụng web, hiệu năng và accessibility

**Mục tiêu:**

- Lập kế hoạch kiểm thử, chọn mức kiểm thử phù hợp cho từng yêu cầu và lập ma trận truy vết.
- Viết kiểm thử đơn vị, kiểm thử component và kiểm thử Server Action bằng Vitest và Testing Library.
- Viết kịch bản kiểm thử đầu-cuối nhiều vai trò bằng Playwright.
- Kiểm chứng giá trị của bộ test (kể cả test do AI sinh) bằng đột biến thủ công.
- Đo và cải thiện hiệu năng (Core Web Vitals), SEO và accessibility.
- Lập báo cáo kiểm thử làm Chương 5 của báo cáo đồ án.

**Nội dung:**

- 10.1. Kế hoạch kiểm thử
  - 10.1.1. Vì sao cần kiểm thử tự động
  - 10.1.2. Chọn mức kiểm thử
  - 10.1.3. Ma trận truy vết
  - 10.1.4. Nội dung kế hoạch kiểm thử
- 10.2. Vitest và Testing Library
  - 10.2.1. Cài đặt
  - 10.2.2. Kiểm thử đơn vị
  - 10.2.3. Kiểm thử component
  - 10.2.4. Kiểm thử Server Action với API giả
- 10.3. Kiểm thử đầu-cuối với Playwright
  - 10.3.1. Cài đặt và cấu hình
  - 10.3.2. Kịch bản nhiều vai trò
- 10.4. Kiểm chứng test do AI sinh
  - 10.4.1. Test "luôn đạt"
  - 10.4.2. Đột biến thủ công
- 10.5. Hiệu năng, SEO và accessibility
  - 10.5.1. Đo hiệu năng
  - 10.5.2. SEO
  - 10.5.3. Accessibility
- 10.6. Báo cáo kiểm thử (CLO2)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-10`.
**Liên kết học liệu:** bài học `bai-10`, slide `Slides/bai-10.pptx`, quiz bài 10.
**Dung lượng ước tính:** khoảng 8 trang; tài liệu tham khảo: 8.

### Chương 11. Triển khai lên Windows Server của Khoa và hoàn thiện báo cáo

**Mục tiêu:**

- Build ứng dụng Next.js cho môi trường production ở chế độ `standalone`.
- Phân biệt biến môi trường đọc lúc build và lúc chạy; cấu hình đúng cho server.
- Chạy web trên Windows Server của Khoa cùng backend nhóm; xử lý cookie `Secure`, CORS, reverse proxy.
- Kiểm tra sau triển khai theo danh sách và viết README triển khai.
- Hoàn thiện báo cáo đồ án đúng cấu trúc và quy định định dạng.
- Tổng kết kế hoạch và tiến độ bằng velocity và burndown.

**Nội dung:**

- 11.1. Từ máy phát triển đến server
  - 11.1.1. Kiến trúc khi triển khai
  - 11.1.2. Làm việc với bộ phận hỗ trợ
- 11.2. Build production
  - 11.2.1. Chế độ standalone
  - 11.2.2. Biến môi trường lúc build và lúc chạy
- 11.3. Chạy trên Windows Server
  - 11.3.1. Những việc cần đạt
  - 11.3.2. Cookie Secure
  - 11.3.3. Server Actions sau reverse proxy
  - 11.3.4. Endpoint kiểm tra sức khỏe
- 11.4. Kiểm tra sau triển khai
  - 11.4.1. Danh sách kiểm tra
  - 11.4.2. README triển khai
- 11.5. Viết báo cáo đồ án (CLO3)
  - 11.5.1. Từ báo cáo sprint đến báo cáo đồ án
  - 11.5.2. Quy định định dạng
  - 11.5.3. Lỗi trình bày hay gặp và cách sửa trong Word
  - 11.5.4. Viết hợp lý và có minh chứng
- 11.6. Tổng kết kế hoạch và tiến độ (CLO4)

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-11`.
**Liên kết học liệu:** bài học `bai-11`, slide `Slides/bai-11.pptx`, quiz bài 11.
**Dung lượng ước tính:** khoảng 8 trang; tài liệu tham khảo: 6.

### Chương 12. Demo Day chung và nộp báo cáo đồ án

**Mục tiêu:**

- Chuẩn bị và trình bày phần web của đồ án trong Demo Day chung với học phần di động.
- Xây dựng kịch bản demo xuyên suốt web và ứng dụng di động trên cùng backend, có cả trường hợp lỗi.
- Đối chiếu báo cáo đồ án với từng tiêu chí của rubric trước khi nộp.
- Chuẩn bị cho phần bảo vệ kỹ thuật: giải thích được mã do chính mình commit.
- Đánh giá sản phẩm của nhóm khác theo rubric và nhìn lại quá trình học.

**Nội dung:**

- 12.1. Demo Day chung
  - 12.1.1. Một hệ thống, hai học phần
  - 12.1.2. Cấu trúc phần trình bày web
  - 12.1.3. Kịch bản demo xuyên suốt
  - 12.1.4. Chuẩn bị và dự phòng
- 12.2. Đối chiếu báo cáo đồ án với rubric
  - 12.2.1. Rubric 27 tiêu chí
  - 12.2.2. Tự đối chiếu trước khi nộp
- 12.3. Bảo vệ kỹ thuật
  - 12.3.1. Hình thức
  - 12.3.2. Câu hỏi thường gặp ở phần web
- 12.4. Sản phẩm nộp cuối kỳ
- 12.5. Review chéo và nhìn lại học phần
  - 12.5.1. Review chéo
  - 12.5.2. Nhìn lại bốn chuẩn đầu ra
  - 12.5.3. Đi tiếp sau học phần

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-12`.
**Liên kết học liệu:** bài học `bai-12`, slide `Slides/bai-12.pptx`, quiz bài 12.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 2.

## 5. Cân đối lý thuyết – thực hành

Ước tính theo số từ: phần lý thuyết và ví dụ khoảng 72%, phần câu hỏi, bài tập và bài tập hướng dẫn khoảng 28% (chưa tính mã nguồn ví dụ). Học phần 60 tiết (15 LT + 45 TH).

## 6. Tài liệu tham khảo chính

- Vercel, “Server and Client Components,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/server-and-client-components
- Meta Open Source, “Server Components,” *React Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react.dev/reference/rsc/server-components
- Vercel, “Installation,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/installation
- Vercel, “Project Structure,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/project-structure
- Vercel, “Layouts and Pages,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/layouts-and-pages
- Vercel, “Route Groups,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/route-groups
- Vercel, “Dynamic Route Segments,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes
- Vercel, “Linking and Navigating,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/linking-and-navigating
- Tailwind Labs, “Styling with utility classes,” *Tailwind CSS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://tailwindcss.com/docs/styling-with-utility-classes
- Tailwind Labs, “Responsive design,” *Tailwind CSS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://tailwindcss.com/docs/responsive-design
- shadcn, “Installation: Next.js,” *shadcn/ui Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://ui.shadcn.com/docs/installation/next
- Vercel, “Environment Variables,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/guides/environment-variables
- Vercel, “page.js,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/page
- Vercel, “Fetching Data,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/fetching-data
- Vercel, “loading.js,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/loading
- … và 45 tài liệu khác, xem cuối mỗi chương.

## 7. Học liệu đi kèm

Xem mục "Học liệu đi kèm" trong Lời nói đầu.

## 8. Phân công và tiến độ

| Công việc | Người phụ trách | Thời hạn |
|---|---|---|
| Duyệt đề cương chi tiết | {{...}} | {{...}} |
| Rà soát bản thảo theo Điều 5 | {{...}} | {{...}} |
| Lấy ý kiến góp ý (phiếu 02) | {{...}} | {{...}} |
| Tiếp thu, hoàn thiện, lập hồ sơ thẩm định | {{...}} | {{...}} |
