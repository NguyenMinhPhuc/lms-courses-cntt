# Dàn ý chi tiết - Lập trình ứng dụng web (111102)

> **Trạng thái:** ĐÃ DUYỆT. Đã soạn đủ 4 giai đoạn: đề cương, đánh giá, rubric và 12 bài học (bài học, slide, quiz). Đã có giáo trình nội bộ (giao-trinh/) và đề cương theo mẫu Khoa (HK6-111102-Lập trình ứng dụng web.docx).

- **Mã học phần:** 111102.
- **Giảng viên phụ trách:** ThS. Nguyễn Minh Phúc.
- **Giảng viên cùng tham gia:** Lê Minh Nhật, Hồ Ngọc Hoàng Long.
- **Thời lượng:** 3 tín chỉ, 60 tiết = **15 tiết lý thuyết + 45 tiết thực hành**, 12 buổi × 5 tiết.
- **Học kỳ:** 6, học song song với *Lập trình ứng dụng di động* (111114).
- **Đối tượng:** sinh viên đã học Thiết kế UI/UX, Thiết kế Web (HTML/CSS/JS), Lập trình Frontend (React), Lập trình Backend (Node.js/NestJS, SQL Server).
- **Công nghệ chính:** **Next.js (App Router)** + TypeScript, Tailwind CSS + shadcn/ui, React Hook Form + Zod, TanStack Table, Recharts, Socket.IO client; kiểm thử Vitest + Testing Library + Playwright.
- **Nguyên tắc dữ liệu:** ứng dụng Next.js **không kết nối SQL Server trực tiếp**; mọi dữ liệu đi qua backend API, backend chỉ truy cập SQL Server qua **stored procedure**.
- **Backend (kết hợp):**
  - **Sprint 1–2:** gọi **API mẫu LHU Food của giảng viên** (gateway, Swagger, JWT, Socket.IO).
  - **Sprint 3–4:** nhóm **tự xây module quản trị** trên backend của nhóm. **Khuyến khích** dùng chung backend NestJS + SQL Server với đồ án di động, **không bắt buộc**; công nghệ backend nào cũng phải truy cập dữ liệu qua stored procedure.
- **Phạm vi web theo SRS LHU Food:** **bắt buộc** trang quản trị (US-A01…A07) và màn hình quầy (US-S02, S03, S05, S06, S07); **cơ bản** web đặt món cho khách (thực đơn, đăng nhập, đặt món, đơn của tôi).
- **Phương pháp:** PBL nhóm 4–5 sinh viên, 4 sprint × 3 buổi, vibe coding với **Google Antigravity** và **GitHub Copilot Chat** (ghi `PROMPTS.md`, không hiểu thì không merge).
- **Hạ tầng:** triển khai web và backend nhóm lên **Windows Server của Khoa**, có bộ phận hỗ trợ triển khai.
- **Tài liệu:** **giáo trình nội bộ riêng** cho học phần web; **dùng chung** SRS LHU Food và kế hoạch Agile & Product Backlog với học phần di động.
- **Demo Day:** **gộp chung với học phần di động** (buổi 12), chấm theo rubric của từng học phần.

---

## Chuẩn đầu ra học phần (CLO)

| CLO | Nội dung | PLO / PI | Trọng số | Đạt khi | Đánh giá |
|---|---|---|:---:|:---:|---|
| **CLO1** | Phân tích các thành phần chức năng của ứng dụng web phù hợp với mô hình đã phân tích | PLO2 / PI 2.4 | 4 | ≥ 2 | Cuối kỳ · Report · Check list |
| **CLO2** | Thực hiện các bài kiểm thử để kiểm tra các yêu cầu chức năng phù hợp với các mục tiêu dự án | PLO4 / PI 4.1 | 2 | ≥ 1 | Cuối kỳ · Report · Check list |
| **CLO3** | Viết báo cáo trình bày nội dung các công việc đã thực hiện bằng văn bản một cách hợp lý và đúng quy định về định dạng | PLO3 / PI 3.1 | 2 | ≥ 1 | Cuối kỳ · Report · Check list |
| **CLO4** | Sử dụng kỹ năng trong việc sắp xếp công việc cá nhân hoặc nhóm phù hợp với mục tiêu công việc đề ra | PLO5 / PI 5.1 | 2 | ≥ 1 | Cuối kỳ · Report · Check list |

Sinh viên đạt CLO khi được ít nhất 50% điểm của CLO; CLO đạt ở cấp lớp khi ít nhất 75% sinh viên đạt.

**Cách rèn luyện từng CLO trong 4 sprint:**

| CLO | Rèn luyện qua | Sản phẩm mỗi checkpoint (buổi 03, 06, 09) |
|---|---|---|
| CLO1 | Phân tích chức năng từ SRS → sơ đồ chức năng, sitemap, cây component, ánh xạ route ↔ chức năng ↔ API | Bảng phân tích thành phần của sprint |
| CLO2 | Viết test case từ tiêu chí nghiệm thu, chạy test thủ công và tự động, ghi kết quả | Bảng test case + kết quả chạy |
| CLO3 | Viết báo cáo theo mẫu định dạng thống nhất | Báo cáo sprint 1–2 trang |
| CLO4 | Lập Sprint Backlog, phân công, theo dõi tiến độ trên GitHub Projects/Jira | Kế hoạch sprint + board cập nhật |

## Đánh giá

| Thành phần | Tỷ trọng | Nội dung |
|---|:---:|---|
| **Quá trình** | 30% | Chuyên cần, quiz từng bài, `PROMPTS.md`, sản phẩm checkpoint (phân tích, test case, báo cáo sprint, kế hoạch sprint), review chéo |
| **Thực hành** | 30% | Bài thực hành không hướng dẫn của từng buổi; demo checkpoint buổi 03, 06, 09 |
| **Cuối kỳ: đồ án nhóm** | 40% | **Báo cáo đồ án (Report)** chấm bằng **checklist** theo 4 CLO, thang 10; Demo Day chung với học phần di động là nơi kiểm chứng sản phẩm và vai trò từng thành viên |

**Rubric cuối kỳ theo CLO (thang 10; rubric chi tiết theo mức như học phần di động, file `rubric/rubric.json`):**

| CLO | Điểm | Minh chứng trong báo cáo | Đạt khi |
|---|:---:|---|:---:|
| CLO1 | 4 | Phân tích thành phần chức năng web (sơ đồ chức năng, sitemap, ánh xạ route – chức năng – API, thiết kế component, module quản trị) khớp SRS và sản phẩm đã triển khai | ≥ 2 |
| CLO2 | 2 | Kế hoạch kiểm thử, test case truy vết tới yêu cầu, kết quả chạy (thủ công, Vitest, Playwright), lỗi và cách khắc phục | ≥ 1 |
| CLO3 | 2 | Báo cáo đủ cấu trúc, lập luận hợp lý, đúng quy định định dạng (trình bày, hình, bảng, tài liệu tham khảo) | ≥ 1 |
| CLO4 | 2 | Kế hoạch và tiến độ (backlog, sprint, phân công, board), đối chiếu kế hoạch với thực tế; phần cá nhân trong báo cáo vai trò | ≥ 1 |

---

## Cấu trúc mỗi buổi (5 tiết)

Phân bổ lý thuyết: buổi 01, 05, 07, 10 có **2 tiết LT**; buổi 02, 03, 04, 06, 08, 09, 11 có **1 tiết LT**; buổi 12 là Demo Day. Tổng **15 tiết LT + 45 tiết TH**.

| Phần | Buổi 1 tiết LT | Buổi 2 tiết LT | Hình thức |
|---|:---:|:---:|---|
| **Lý thuyết** | 1 tiết | 2 tiết | Giảng ngắn, demo trực tiếp |
| **Thực hành có hướng dẫn** | 2 tiết | 1,5 tiết | Làm theo giảng viên trên web LHU Food |
| **Thực hành không hướng dẫn** | 1,5 tiết | 1 tiết | Cá nhân tự làm bài tương tự theo đặc tả và tiêu chí hoàn thành |
| **Thử thách nhóm (PBL)** | 0,5 tiết + ở nhà | 0,5 tiết + ở nhà | Nhiệm vụ sprint của đồ án nhóm, nộp qua Pull Request |

---

## Lộ trình PBL: 4 sprint

| Sprint | Buổi | Mục tiêu sản phẩm | Backend | Sản phẩm phân tích, kiểm thử, báo cáo, kế hoạch | Checkpoint |
|---|---|---|---|---|---|
| **Sprint 1: Nền tảng & Giao diện** | 01–03 | Dự án Next.js, layout quản trị và khách, routing, trang thực đơn với dữ liệu thật | API mẫu (đọc) | Sơ đồ chức năng web, sitemap, kế hoạch Sprint 1, test case trang thực đơn, báo cáo sprint 1 | Buổi 03 |
| **Sprint 2: Người dùng & Tương tác** | 04–06 | Form, giỏ hàng, đặt món, đăng nhập, phân quyền, màn hình quầy | API mẫu (đọc + ghi) | Phân tích phân quyền theo vai trò, test case xác thực/phân quyền, báo cáo sprint 2 | Buổi 06 |
| **Sprint 3: Quản trị & Realtime** | 07–09 | Module quản trị trên backend nhóm, trang CRUD, báo cáo biểu đồ, màn hình quầy realtime | **Backend của nhóm** | Phân tích module quản trị, ERD phần quản trị, test case quản trị và realtime, báo cáo sprint 3 | Buổi 09 |
| **Sprint 4: Chất lượng & Phát hành** | 10–12 | Kiểm thử tự động, hiệu năng, triển khai lên server Khoa, báo cáo đồ án | Backend của nhóm | Báo cáo kiểm thử, báo cáo đồ án hoàn chỉnh | Buổi 12: Demo Day chung |

---

## Bài 01 - Ứng dụng web hiện đại với Next.js & khởi động dự án (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO1, CLO4
- **Mục tiêu (Bloom):** So sánh được các mô hình render web (CSR, SSR, SSG, React Server Components); phân tích được kiến trúc và phạm vi web của LHU Food từ SRS; lập được kế hoạch và phân vai cho dự án nhóm.
- **Ý chính:**
  1. Từ SPA React đến framework full-stack: CSR, SSR, SSG, ISR, React Server Components; khi nào cần Next.js (trang thực đơn cần SEO và tải nhanh, trang quản trị cần tương tác).
  2. Next.js App Router: thư mục `app/`, `page.tsx`, `layout.tsx`, Server Component mặc định, `"use client"`; dev server và build.
  3. Phân tích phạm vi web từ SRS: actor, user story [W] và [M+W], kiến trúc Next.js ↔ API ↔ SQL Server qua stored procedure; Next.js không kết nối CSDL.
  4. Lập kế hoạch dự án và vibe coding: Product Backlog từ kế hoạch Agile dùng chung, Sprint Backlog trên GitHub Projects/Jira, phân vai; `AGENTS.md`, prompt có ngữ cảnh, review mã AI sinh.
- **Thực hành có hướng dẫn:** cài Node LTS, tạo `lhu-food-web` bằng `create-next-app` (TypeScript, Tailwind, App Router); trang chủ; repo GitHub, `AGENTS.md`, commit đầu tiên; mở Swagger của API mẫu.
- **Thực hành không hướng dẫn:** trang "Hồ sơ cá nhân" nhiều trang con bằng App Router, đẩy lên GitHub.
- **Thử thách nhóm:** lập nhóm (dùng chung đề tài với đồ án di động), chọn story web từ backlog, lập **kế hoạch Sprint 1** và board công việc, bảng phân vai.
- **Slide dự kiến:** khoảng 18 slide.

## Bài 02 - Routing, layout & giao diện với Tailwind CSS (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1
- **Mục tiêu (Bloom):** Phân tích được chức năng thành sitemap và hệ thống route; xây dựng được route lồng nhau, layout dùng chung, route động; dựng được giao diện responsive bằng Tailwind và component dùng chung.
- **Ý chính:**
  1. Từ sơ đồ chức năng đến sitemap và route: ánh xạ chức năng SRS ↔ route ↔ vai trò được truy cập.
  2. Routing của App Router: route lồng nhau, route group `(admin)`, `(shop)`, route động `[id]`, `loading.tsx`, `error.tsx`, `not-found.tsx`, `Link`.
  3. Layout dùng chung (quản trị: sidebar, header; khách) và cây component; metadata cơ bản.
  4. Tailwind CSS và shadcn/ui: utility-first, responsive, component có sẵn; từ Figma đến mã bằng vibe coding.
- **Thực hành có hướng dẫn:** khung `(admin)/dashboard`, `(admin)/products`, `(shop)/menu`, `(shop)/product/[id]` với dữ liệu giả; sidebar responsive.
- **Thực hành không hướng dẫn:** lưới món + trang chi tiết theo route động, responsive 3 kích thước màn hình.
- **Thử thách nhóm:** sơ đồ chức năng web, sitemap và bảng ánh xạ route – chức năng – vai trò; khung route của web nhóm.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 03 - Server Components & lấy dữ liệu từ API (5 tiết: 1 LT / 4 TH) · Checkpoint Sprint 1
- **CLO liên quan:** CLO1, CLO2, CLO3, CLO4
- **Mục tiêu (Bloom):** Phân biệt được Server Component và Client Component; lấy được dữ liệu từ API với cache phù hợp; viết và chạy được test case cho trang đã làm; trình bày được kết quả sprint bằng báo cáo theo mẫu.
- **Ý chính:**
  1. Server Component và Client Component: chạy ở đâu, gửi gì xuống trình duyệt, ranh giới `"use client"`.
  2. Lấy dữ liệu bằng `fetch` từ API mẫu; biến môi trường phía server và `NEXT_PUBLIC_*`; kiểu TypeScript cho response; cache, `revalidate`, dữ liệu động.
  3. Streaming với `loading.tsx` và `Suspense`; `error.tsx` khi API lỗi.
  4. Kiểm thử và báo cáo sprint: viết test case từ tiêu chí nghiệm thu (US-G01, G03), chạy và ghi kết quả; báo cáo sprint theo mẫu định dạng; Sprint Review và kế hoạch Sprint 2.
- **Thực hành có hướng dẫn:** trang thực đơn và chi tiết món lấy từ API mẫu, lọc theo danh mục qua `searchParams`, tìm kiếm; bảng test case mẫu.
- **Thực hành không hướng dẫn:** trang danh sách quầy (`GET /counters`) có trạng thái tải, lỗi, rỗng, kèm 5 test case.
- **Checkpoint 1:** demo khung web với dữ liệu thật; nộp sơ đồ chức năng, sitemap, test case + kết quả, **báo cáo sprint 1**, kế hoạch Sprint 2.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 04 - Client Components, trạng thái & form (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu (Bloom):** Phân tích được phần nào của trang cần chạy phía client; xây dựng được giỏ hàng và form có kiểm tra dữ liệu ở cả client và server; kiểm thử được các giá trị biên của form.
- **Ý chính:**
  1. Client Component: state, sự kiện, hook; giữ phần tương tác nhỏ nhất ("đảo client" trong trang server).
  2. Trạng thái giỏ hàng phía web: Zustand + `localStorage`, tránh lỗi hydration.
  3. Form với React Hook Form + Zod; dùng chung schema Zod giữa form và Server Action.
  4. Gọi API ghi dữ liệu (đặt món qua API mẫu), hiển thị lỗi 400/409; bảng giá trị biên và test case cho form.
- **Thực hành có hướng dẫn:** giỏ hàng web, form đăng ký, trang đặt món qua API mẫu.
- **Thực hành không hướng dẫn:** form "Góp ý căn tin" có kiểm tra Zod, thông báo lỗi tiếng Việt, bảng giá trị biên.
- **Thử thách nhóm:** form chính và luồng nhập liệu của web nhóm, kèm test case.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 05 - Xác thực, phân quyền & bảo mật web (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu (Bloom):** Phân tích được yêu cầu phân quyền theo vai trò; triển khai được đăng nhập bằng JWT của backend với cookie `httpOnly`; kiểm thử được các tình huống truy cập trái phép.
- **Ý chính:**
  1. Luồng xác thực web: đăng nhập qua Server Action/Route Handler, access và refresh token trong cookie `httpOnly`, `Secure`, `SameSite`; không lưu token trong `localStorage`.
  2. Ma trận phân quyền vai trò × chức năng; middleware bảo vệ route; kiểm tra lại quyền ở server, không chỉ ẩn menu.
  3. Làm mới token, đăng xuất, gọi API từ server kèm token.
  4. Bảo mật web (XSS, CSRF, CORS, lộ biến `NEXT_PUBLIC_*`, OWASP Top 10 mức nhận diện) và test case bảo mật/phân quyền.
- **Thực hành có hướng dẫn:** đăng nhập, cookie, middleware chặn `/admin`, header hiển thị người dùng, đăng xuất.
- **Thực hành không hướng dẫn:** trang "Hồ sơ của tôi"; kiểm thử 4 tình huống truy cập trái phép và ghi kết quả.
- **Thử thách nhóm:** xác thực và phân quyền cho web nhóm; ma trận phân quyền.
- **Slide dự kiến:** khoảng 18 slide.

## Bài 06 - Server Actions, bảng dữ liệu & màn hình quầy (5 tiết: 1 LT / 4 TH) · Checkpoint Sprint 2
- **CLO liên quan:** CLO1, CLO2, CLO3, CLO4
- **Mục tiêu (Bloom):** Thực hiện được thao tác ghi dữ liệu bằng Server Actions; xây dựng được bảng dữ liệu và màn hình quầy; kiểm thử luồng nghiệp vụ; báo cáo kết quả sprint.
- **Ý chính:**
  1. Server Actions: `useActionState`, `revalidatePath`, xử lý lỗi; cập nhật lạc quan với `useOptimistic`.
  2. Bảng dữ liệu với TanStack Table: sắp xếp, lọc, phân trang theo tham số URL.
  3. Màn hình quầy (US-S02, S03, S06): đơn theo trạng thái, chuyển trạng thái đúng trình tự, xử lý 409.
  4. Kiểm thử luồng "khách đặt → nhân viên xử lý" theo tiêu chí nghiệm thu; báo cáo sprint 2; so sánh kế hoạch với thực tế (velocity).
- **Thực hành có hướng dẫn:** màn hình quầy dùng API mẫu với Server Actions; bảng món có lọc và phân trang.
- **Thực hành không hướng dẫn:** trang "Đơn của tôi" (lịch sử, chi tiết, hủy đơn pending).
- **Checkpoint 2:** demo luồng đặt món trên web → nhân viên xử lý; nộp ma trận phân quyền, test case + kết quả, **báo cáo sprint 2**, kế hoạch Sprint 3, bản nháp báo cáo vai trò cá nhân.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 07 - Module quản trị trên backend của nhóm (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO1
- **Mục tiêu (Bloom):** Phân tích được nghiệp vụ quản trị từ SRS thành CSDL, stored procedure và API; xây dựng được API quản trị có phân quyền admin; chuyển được web sang backend của nhóm.
- **Ý chính:**
  1. Phân tích nghiệp vụ quản trị (SRS F11, F09.3, F10): vai trò `admin`, khóa tài khoản, quầy, tồn kho; mở rộng ERD bằng script phiên bản mới.
  2. Stored procedure quản trị: CRUD có ràng buộc (không xóa danh mục còn món, món đã bán chỉ ngừng bán), báo cáo theo khoảng ngày, mã lỗi 50400/50404/50409.
  3. API quản trị: phân quyền admin, DTO, Swagger (NestJS khuyến khích; backend khác cũng phải gọi stored procedure).
  4. Chuyển web từ API mẫu sang backend nhóm: biến môi trường, so khớp hợp đồng API, kiểm thử hồi quy trang Sprint 1–2.
- **Thực hành có hướng dẫn:** thêm thủ tục và API quản lý danh mục (code-along), gọi từ Next.js.
- **Thực hành không hướng dẫn:** thủ tục + API quản lý quầy.
- **Thử thách nhóm:** module quản trị trên backend nhóm; ERD phần quản trị, danh mục stored procedure; web chuyển sang backend nhóm.
- **Slide dự kiến:** khoảng 18 slide.

## Bài 08 - Trang quản trị: CRUD, tải ảnh, báo cáo & biểu đồ (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu (Bloom):** Xây dựng được các trang quản trị CRUD hoàn chỉnh; tải được ảnh lên API; trình bày được số liệu bằng biểu đồ; kiểm thử được các ràng buộc nghiệp vụ quản trị.
- **Ý chính:**
  1. Mẫu trang CRUD: danh sách, tạo, sửa, ngừng bán; form dùng chung; Dialog xác nhận.
  2. Tải ảnh món: `FormData` qua Server Action/Route Handler tới API, xem trước, giới hạn định dạng và dung lượng.
  3. Báo cáo doanh thu, món bán chạy, tỉ lệ trạng thái bằng Recharts; chọn khoảng ngày; xuất CSV/Excel.
  4. Quản lý tài khoản nhân viên (US-A04); test case cho ràng buộc quản trị (xóa danh mục còn món, khóa tài khoản).
- **Thực hành có hướng dẫn:** trang quản lý món (CRUD + ảnh), trang báo cáo doanh thu có biểu đồ.
- **Thực hành không hướng dẫn:** trang quản lý tài khoản nhân viên (tạo, khóa, mở khóa).
- **Thử thách nhóm:** hoàn thiện trang quản trị của đề tài nhóm, kèm test case.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 09 - Màn hình quầy thời gian thực với Socket.IO (5 tiết: 1 LT / 4 TH) · Checkpoint Sprint 3
- **CLO liên quan:** CLO1, CLO2, CLO3, CLO4
- **Mục tiêu (Bloom):** Tích hợp được Socket.IO vào Client Component có xác thực; phân tích được luồng realtime bằng sơ đồ tuần tự; kiểm thử được realtime nhiều phiên; báo cáo kết quả sprint.
- **Ý chính:**
  1. Socket.IO trong Next.js: chỉ chạy ở Client Component, lấy token kết nối từ server, kết nối lại.
  2. Màn hình quầy realtime: `order:new` (âm báo), `order:updated` đồng bộ nhiều nhân viên; làm mới dữ liệu khi kết nối lại.
  3. Sơ đồ tuần tự luồng realtime web và mobile cùng backend.
  4. Kiểm thử realtime (nhiều tab, mất mạng, token hết hạn); báo cáo sprint 3; điều chỉnh kế hoạch Sprint 4.
- **Thực hành có hướng dẫn:** màn hình quầy nhận `order:new`, cập nhật không tải lại trang, phát âm báo.
- **Thực hành không hướng dẫn:** dashboard tự cập nhật số đơn theo trạng thái.
- **Checkpoint 3:** demo quản trị + màn hình quầy realtime (web và mobile cùng backend); nộp phân tích module quản trị, sơ đồ tuần tự, test case + kết quả, **báo cáo sprint 3**, kế hoạch Sprint 4.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 10 - Kiểm thử ứng dụng web, hiệu năng & accessibility (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO2
- **Mục tiêu (Bloom):** Lập được kế hoạch kiểm thử; thực hiện được kiểm thử đơn vị, component và đầu-cuối truy vết tới yêu cầu; đo và cải thiện được hiệu năng, accessibility; lập được báo cáo kiểm thử.
- **Ý chính:**
  1. Kế hoạch kiểm thử và ma trận truy vết yêu cầu ↔ test case ↔ kết quả (liên hệ học phần Kiểm thử phần mềm).
  2. Vitest + Testing Library cho hàm, component, Server Action; mock API.
  3. Playwright: kịch bản đầu-cuối (đăng nhập → đặt món → nhân viên xử lý), báo cáo HTML; kiểm chứng test do AI sinh (mutation thủ công).
  4. Hiệu năng (Lighthouse, Core Web Vitals, `next/image`), SEO (metadata, sitemap), accessibility (nhãn form, bàn phím, tương phản).
- **Thực hành có hướng dẫn:** test cho giỏ hàng và form; một kịch bản Playwright; đo Lighthouse trước/sau tối ưu.
- **Thực hành không hướng dẫn:** 5 test có giá trị cho module tự chọn + mutation thủ công.
- **Thử thách nhóm:** bộ test luồng chính, **báo cáo kiểm thử** (kế hoạch, ma trận truy vết, kết quả, lỗi và khắc phục).
- **Slide dự kiến:** khoảng 18 slide.

## Bài 11 - Triển khai lên Windows Server của Khoa & hoàn thiện báo cáo (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO3, CLO4
- **Mục tiêu (Bloom):** Triển khai được ứng dụng Next.js cùng backend lên Windows Server; viết được tài liệu triển khai; hoàn thiện được báo cáo đồ án đúng quy định định dạng; đối chiếu được kế hoạch với tiến độ thực tế.
- **Ý chính:**
  1. Build production: `next build`, chế độ `standalone`, biến môi trường theo môi trường.
  2. Chạy Next.js như dịch vụ nền trên Windows Server (theo bộ phận hỗ trợ), reverse proxy/HTTPS, CORS và cookie `Secure` với backend nhóm.
  3. Viết báo cáo kỹ thuật: cấu trúc báo cáo đồ án, quy định định dạng (trình bày, đánh số hình/bảng, trích dẫn tài liệu), viết hợp lý và có minh chứng.
  4. Tổng kết kế hoạch: burndown, velocity, kế hoạch so với thực tế, bài học quản lý công việc.
- **Thực hành có hướng dẫn:** triển khai web LHU Food mẫu lên server mẫu; README triển khai.
- **Thực hành không hướng dẫn:** chương "Triển khai" của báo cáo nhóm đúng mẫu định dạng.
- **Thử thách nhóm:** web + backend nhóm chạy trên server Khoa; **bản nháp báo cáo đồ án**.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 12 - Demo Day chung & nộp báo cáo đồ án (5 tiết: 0 LT / 5 TH)
- **CLO liên quan:** CLO1, CLO2, CLO3, CLO4 (đánh giá cuối kỳ)
- **Ý chính:**
  1. Demo Day **chung với học phần di động**: web quản trị, màn hình quầy realtime, web đặt món và app di động trên cùng backend triển khai ở server Khoa.
  2. Báo cáo đồ án (Report) chấm bằng checklist theo 4 CLO: phân tích thành phần (CLO1), kiểm thử (CLO2), chất lượng báo cáo (CLO3), kế hoạch và tiến độ (CLO4).
  3. Bảo vệ kỹ thuật: giảng viên chọn ngẫu nhiên đoạn mã, người đã commit giải thích.
  4. Review chéo; nhìn lại học phần.
- **Hoạt động:** mỗi nhóm trình bày (phần web) và trả lời câu hỏi; nộp báo cáo đồ án, báo cáo kiểm thử, link repo, link web đã triển khai, báo cáo vai trò cá nhân.
- **Slide dự kiến:** khoảng 8 slide.

---

## Thông tin đã chốt với giảng viên

Mã học phần 111102; 3 tín chỉ, 60 tiết (15 LT / 45 TH); giảng viên phụ trách ThS. Nguyễn Minh Phúc, cùng tham gia Lê Minh Nhật, Hồ Ngọc Hoàng Long; Học kỳ 6, song song với học phần di động; 12 buổi × 5 tiết, PBL 4 sprint, checkpoint buổi 03/06/09; vibe coding với Google Antigravity và GitHub Copilot Chat; đánh giá 30% / 30% / 40%; CLO1 (PLO2/PI 2.4) trọng số 4, CLO2 (PLO4/PI 4.1), CLO3 (PLO3/PI 3.1), CLO4 (PLO5/PI 5.1) trọng số 2, đánh giá cuối kỳ bằng báo cáo và checklist, đạt khi ≥ 50% trọng số, chỉ tiêu ≥ 75% sinh viên đạt; frontend Next.js (App Router); backend kết hợp: Sprint 1–2 dùng hệ thống API mẫu của giảng viên, Sprint 3–4 nhóm tự xây module quản trị (khuyến khích NestJS dùng chung với đồ án di động, không bắt buộc); phạm vi bắt buộc quản trị + màn hình quầy, web khách ở mức cơ bản; Demo Day gộp chung hai học phần; giáo trình nội bộ riêng cho học phần web, dùng chung SRS và kế hoạch Agile LHU Food; triển khai lên Windows Server của Khoa; thư mục `lap-trinh-ung-dung-web`. Báo cáo đồ án theo quy định định dạng thông dụng (A4, Times New Roman 13, giãn dòng 1,3–1,5, lề trái 3 cm, đánh số chương/hình/bảng, tài liệu tham khảo IEEE); rubric cuối kỳ chấm theo mức giống học phần di động (Report làm minh chứng chính); Next.js không kết nối SQL Server trực tiếp; giao diện Tailwind CSS + shadcn/ui.
