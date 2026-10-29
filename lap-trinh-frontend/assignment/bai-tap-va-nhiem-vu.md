# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## BÀI TẬP & NHIỆM VỤ HỌC TẬP (Assignments)

> **Phạm vi:** 12 bài · **Dự án xuyên suốt:** Smart Event Hub · **Đánh giá:** Quá trình 30% · Giữa kỳ 30% (Buổi 7) · Cuối kỳ 40% (Buổi 12)
> **Mỗi buổi gồm:** Guided Practice 45' · Unguided Practice 45' · Team Challenge 60' (xem `discussion/`) · Bài tập về nhà (BTVN) cá nhân

---

## PHẦN A. QUY ĐỊNH NỘP BÀI CHUNG

### A.1. Ba hình thức nộp

#### Chọn hình thức theo loại sản phẩm

| Loại sản phẩm | Hình thức nộp | Nộp gì lên LMS |
|---|---|---|
| Code tính năng, BTVN có code | **Pull Request vào branch `dev`** của repo nhóm | Link PR (dán vào ô Online text của Assignment) |
| Sản phẩm cả nhóm (wireframe, repo, link deploy) | **Link repository / link Figma / link Vercel** | Link, kèm tên nhánh hoặc commit hash nếu GV yêu cầu |
| Tài liệu (slide, báo cáo, test case) | **File** đặt tên `[MãLớp]_[Nhóm/MSSV]_[TênBài]` | File `.pdf`, `.docx`, `.pptx` hoặc `.md` |

**Quy tắc đặt tên file:** không dấu, không khoảng trắng, tên bài viết liền kiểu PascalCase.

```text
24CT111_Nhom02_BaoCaoGiuaKy.pdf        (nộp theo nhóm)
24CT111_Nhom02_TestCasesScenario.md    (nộp theo nhóm)
24CT111_2211xxxx_PhanTuCaNhan.pdf      (nộp cá nhân, dùng MSSV)
```

> 📝 Mã lớp `24CT111` chỉ là ví dụ minh họa; các bạn thay bằng mã lớp học phần của mình.

**Tiêu đề PR** theo Conventional Commits, có ghi số bài: `feat(ui): BTVN Bai01 - Footer, EventCategoryBadge, SearchBar`.

### A.2. Hạn nộp và tiêu chí đạt chung

#### Hạn nộp

* **BTVN:** trước giờ bắt đầu **buổi học tiếp theo**. Thời điểm đóng cụ thể do GV đặt bằng *Group overrides* trên LMS theo lịch của từng lớp.
* **Guided/Unguided:** commit và push lên nhánh `feature/*` của mình **trước khi kết thúc buổi**; GV kiểm tra trực tiếp tại máy hoặc qua commit.
* **Quiz trước giờ học** (5–10 câu): hoàn thành trên LMS trước khi buổi học bắt đầu.

#### Tiêu chí đạt áp dụng cho mọi bài có code

* [ ] `npm run lint` và `npm run build` không lỗi (bắt buộc từ Bài 07 trở đi, khuyến khích từ Bài 01).
* [ ] TypeScript strict, **không có `any`**; Props và dữ liệu có interface/type rõ ràng.
* [ ] Style dùng SCSS Module hoặc thư viện UI đã chọn; dùng biến/mixin chung trong `styles/`.
* [ ] Không vỡ khung ở Mobile 375px.
* [ ] Commit theo Conventional Commits; PR có mô tả, có mục "Phần có dùng AI".
* [ ] Tự giải thích được code của mình khi GV hỏi.

---

## PHẦN B. BẢNG TỔNG HỢP MỐC NỘP TOÀN HỌC PHẦN

| Buổi | Nhiệm vụ cần nộp | Cá nhân / Nhóm | Hình thức nộp | Hạn |
|---|---|---|---|---|
| Mọi buổi | Quiz LMS trước giờ học | Cá nhân | Làm trên LMS | Trước buổi học |
| 1 | Link PR Team Challenge (Design Token) | Nhóm | Link PR | Cuối Buổi 1 |
| 1 | BTVN: Footer, EventCategoryBadge, SearchBar | Cá nhân | PR vào `dev` | Trước Buổi 2 |
| 2 | Wireframe 5 màn hình (`docs/wireframes/`) | Nhóm | Link Figma/repo | Cuối Buổi 2 (bản nháp) |
| 2 | BTVN: hoàn thiện Wireframe + trang `/dev-preview/*` | Cá nhân (theo màn hình phụ trách) | PR vào `dev` + link Figma | Trước Buổi 3 |
| 3 | BTVN: `error.tsx`, `global-error.tsx`, Loading Skeleton | Cá nhân | PR vào `dev` | Trước Buổi 4 |
| 4 | BTVN: tổ chức lại thư mục `components/` | Cá nhân | PR vào `dev` | Trước Buổi 5 |
| 5 | BTVN: responsive toàn bộ component AntD | Cá nhân | PR vào `dev` + ảnh 375px/1440px | Trước Buổi 6 |
| 6 | BTVN: tích hợp 50% + slide giữa kỳ | Nhóm (mỗi người có PR riêng) | PR + link repo | Trước Buổi 7 |
| **7** | **Báo cáo giữa kỳ (30%)** | **Nhóm + cá nhân** | Link repo, Figma, file slide | **Tại Buổi 7** |
| 7 | BTVN: sửa theo góp ý giữa kỳ; đọc Swagger | Cá nhân | PR vào `dev` | Trước Buổi 8 |
| 8 | BTVN: xử lý lỗi API (Network Error, 500) | Cá nhân | PR vào `dev` | Trước Buổi 9 |
| 9 | BTVN: tài khoản Vercel + kết nối repo | Cá nhân | Ảnh chụp Vercel Dashboard | Trước Buổi 10 |
| 10 | BTVN: kịch bản kiểm thử toàn hệ thống | Nhóm | File `[MãLớp]_[Nhóm]_TestCasesScenario` | Trước Buổi 11 |
| 11 | Link Vercel Live + ảnh Lighthouse | Nhóm | Link + ảnh | Cuối Buổi 11 |
| 11 | BTVN: Báo cáo Word/PDF + slide cuối kỳ | Nhóm | File `[MãLớp]_[Nhóm]_BaoCaoCuoiKy`, `..._SlideCuoiKy` | Trước Buổi 12 |
| **12** | **Hackathon & Final Showcase (40%)** | **Nhóm + cá nhân** | Demo live, phản biện | **Tại Buổi 12** |

---

## PHẦN C. BÀI TẬP CHI TIẾT THEO TỪNG BÀI

### Bài 01: SCSS nâng cao, TypeScript căn bản & thiết lập Vibe Coding

#### 🛠️ Guided Practice (45'): Component `EventCard` + SCSS Module responsive

* **Yêu cầu:**
  * Tạo `EventCard.tsx` hiển thị ảnh bìa, tiêu đề, ngày giờ, giá vé, badge trạng thái.
  * Tạo `EventCard.module.scss` có mixin responsive: Desktop 3 cột, Tablet 2 cột, Mobile 1 cột.
  * Định nghĩa interface `EventProps` trong `types/event.ts`, `status` là union `'UPCOMING' | 'ONGOING' | 'ENDED'`.
  * Dùng `next/image`; sửa các lỗi type mismatch do AI gợi ý sai.
* **Output:** Component hiển thị đúng dữ liệu từ props, co giãn không vỡ.
* **Tiêu chí đạt:** không lỗi TypeScript (no implicit any); badge đổi màu theo trạng thái (xanh dương / xanh lá / xám).

#### 🧩 Unguided Practice (45'): `HeaderNavigationBar`

* **Yêu cầu:** Logo "Smart Event Hub", menu (Trang chủ, Sự kiện, Bảng tin, Liên hệ), ô tìm kiếm nhanh, nút Đăng nhập/Đăng ký. Interface `NavItem { label: string; href: string; isExternal?: boolean }` đặt trong `types/`. Sticky header khi cuộn và hover underline bằng SCSS.
* **Output:** Thanh điều hướng cố định trên đỉnh trang, link có hiệu ứng hover mượt.
* **Tiêu chí đạt:** TypeScript strict, không `any`; interface tách khỏi file component.

#### 🏠 BTVN (cá nhân): 3 component tĩnh cho dự án

* **Yêu cầu:**
  1. `Footer.tsx`: thông tin bản quyền, liên kết mạng xã hội, form đăng ký nhận bản tin (Newsletter).
  2. `EventCategoryBadge.tsx`: badge thể loại (Âm nhạc, Công nghệ, Thể thao, Workshop) kèm icon tương ứng.
  3. `SearchBar.tsx`: thanh tìm kiếm sự kiện kèm dropdown chọn địa điểm (Hà Nội, TP.HCM, Đà Nẵng).
* **Output:** Mỗi component có interface Props và SCSS Module riêng.
* **Tiêu chí đạt:** dùng biến/mixin trong `styles/_variables.scss`, `styles/_mixins.scss` của nhóm; không `any`; hiển thị ổn ở 375px.
* **Hạn nộp:** trước Buổi 2.
* **Cách nộp:** PR cá nhân từ `feature/<tên>-static-components` vào `dev`; dán link PR lên LMS.

---

### Bài 02: Tư duy Wireframe/Modeling UI & chuyển Figma thành Next.js Component

#### 🛠️ Guided Practice (45'): Trang chủ từ Wireframe sang TSX

* **Yêu cầu:** Từ bản phác thảo Figma "Trang chủ Danh sách sự kiện" của GV, đưa ảnh/SVG vào v0.dev hoặc Claude để sinh code Next.js. Phân rã thành `HeroBanner`, `FeaturedEventsSection`, `CategoryFilter`; tạo mock data 4 phần tử bằng TypeScript; dùng thẻ semantic. Sau đó refactor: đổi tên biến, tách component dài, bỏ inline-style.
* **Output:** Giao diện giống >85% bản phác thảo.
* **Tiêu chí đạt:** không còn inline-style rác; cấu trúc `header`, `main`, `section`, `article` đúng chỗ.

#### 🧩 Unguided Practice (45'): Màn hình Chi tiết sự kiện

* **Yêu cầu:** Tự phác thảo (giấy hoặc phần mềm) màn hình Event Detail gồm banner lớn, thông tin ban tổ chức, nội dung chi tiết, sơ đồ vé, khung đặt vé cố định. Dùng Vibe Coding chuyển thành `EventDetailPageView.tsx` (cột trái 70%, cột phải 30% sticky).
* **Output:** Màn hình hoàn chỉnh về bố cục.
* **Tiêu chí đạt:** khung đặt vé bám theo khi cuộn (Sticky Sidebar); trên Mobile hai cột xếp dọc.

#### 🏠 BTVN (cá nhân theo màn hình phụ trách): Wireframe hoàn chỉnh & trang dev-preview

* **Yêu cầu:**
  * Hoàn thiện file Wireframe Figma cho màn hình mình phụ trách trong bộ 5 màn hình của nhóm.
  * Chuyển wireframe đó thành trang giao diện tĩnh trong `app/dev-preview/` (ví dụ `/dev-preview/home`, `/dev-preview/detail`, `/dev-preview/checkout`, `/dev-preview/profile`, `/dev-preview/admin`) và tạo các component mẫu tương ứng.
* **Output:** Mọi thành viên truy cập được các đường dẫn `/dev-preview/*` để xem bố cục tĩnh.
* **Tiêu chí đạt:** bố cục khớp wireframe; component đặt đúng thư mục; ảnh wireframe đã có trong `docs/wireframes/`.
* **Hạn nộp:** trước Buổi 3.
* **Cách nộp:** PR vào `dev` + link Figma (dán vào LMS).

---

### Bài 03: Next.js App Router – cấu trúc thư mục, Index & Nested Routing

#### 🛠️ Guided Practice (45'): Khởi tạo dự án và Layout chung

* **Yêu cầu:** Tạo dự án Next.js App Router + TypeScript; thiết lập layout chung chứa Header và Footer cho các trang người dùng; Route Group `(auth)` với `/login`, `/register` dùng AuthLayout riêng (chỉ Logo và form ở giữa); Nested Route `/events`, `/events/categories`, `/events/search`.
* **Output:** Hệ thống route chuyển đổi trơn tru.
* **Tiêu chí đạt:** trang thuộc `(auth)` không hiển thị Header/Footer chính; URL không chứa tên group.

> 🧭 Layout cha luôn bọc layout con, nên nếu đặt Header/Footer ngay trong `app/layout.tsx` thì trang `(auth)` cũng bị kế thừa. Cách làm khuyến nghị: Root Layout chỉ chứa `<html>`, `<body>` và provider; Header/Footer đặt trong `app/(main)/layout.tsx` (xem `documentation/dac-ta-du-an-smart-event-hub.md`, mục 3).

#### 🧩 Unguided Practice (45'): Khu vực quản trị `(admin)`

* **Yêu cầu:** Route Group `(admin)` gồm `/admin/dashboard`, `/admin/manage-events`, `/admin/users`; AdminLayout có Sidebar trái; `loading.tsx` hiển thị Skeleton khi chuyển trang. Bổ sung khung trang `/checkout`, `/user/profile` bằng Vibe Coding.
* **Output:** `/admin/dashboard` hiển thị layout quản trị riêng; có Skeleton khi chuyển route.
* **Tiêu chí đạt:** đúng file convention (`layout.tsx`, `page.tsx`, `loading.tsx`); TypeScript cho props layout.

> 📝 Kế hoạch buổi học dùng tên `/admin/events-management`, đề cương dùng `/admin/manage-events`. Bộ học liệu thống nhất dùng `/admin/manage-events`.

#### 🏠 BTVN (cá nhân): Xử lý lỗi và trạng thái chờ

* **Yêu cầu:**
  * `app/error.tsx` (Client Component) bắt lỗi runtime, có nút "Thử lại (Try Again)" gọi `reset()`.
  * `app/global-error.tsx` bắt lỗi ở mức Root Layout.
  * `loading.tsx` dạng Skeleton cho các route mình đã tạo.
* **Output:** Khi gặp sự cố runtime, màn hình hiện thông báo lỗi lịch sự kèm nút thử lại; khi chuyển trang có Skeleton.
* **Tiêu chí đạt:** `error.tsx` có `'use client'`; `global-error.tsx` tự khai báo `<html>` và `<body>`; Skeleton không gây nhảy layout.
* **Hạn nộp:** trước Buổi 4.
* **Cách nộp:** PR vào `dev`.

---

### Bài 04: Dynamic Routing & kiến trúc Reusable Components

#### 🛠️ Guided Practice (45'): `/events/[id]` và `Button` đa biến thể

* **Yêu cầu:** Tạo `app/events/[id]/page.tsx` đọc `id` bằng `const { id } = await params;` (Next.js 15). Tạo `Button.tsx` mở rộng `ButtonHTMLAttributes<HTMLButtonElement>` với `variant: 'primary' | 'secondary' | 'danger' | 'outline'`, `size: 'sm' | 'md' | 'lg'`, `isLoading`, `leftIcon`.
* **Output:** Đổi URL `/events/ev-101`, `/events/ev-102` hiển thị đúng id; Button đúng với mọi props.
* **Tiêu chí đạt:** khi `isLoading` thì nút bị `disabled` và hiện spinner; interface `PageProps` khai báo `params: Promise<{ id: string }>`.

#### 🧩 Unguided Practice (45'): `/category/[slug]` với searchParams

* **Yêu cầu:** Tạo `app/category/[slug]/page.tsx`; đọc `slug` (`music`, `technology`, `sports`, `workshop`) và `searchParams` (`page`, `sort`), ví dụ `/category/music?page=1&sort=latest`; mock data dạng map theo slug.
* **Output:** Hiển thị cả `slug` và `sort` trên giao diện; danh sách lọc đúng danh mục.
* **Tiêu chí đạt:** `searchParams` cũng là `Promise` và được `await`; slug không tồn tại gọi `notFound()`.

#### 🏠 BTVN (cá nhân): Tổ chức lại thư mục components

* **Yêu cầu:** Sắp xếp toàn bộ component theo:
  * `components/ui/` – atom: Button, Input, Modal, Badge.
  * `components/common/` – Header, Footer, Sidebar (đề cương gọi là `shared/`, hai tên tương đương; nhóm chọn một và dùng thống nhất).
  * `components/features/` – EventCard, SeatPicker, CheckoutForm.
* **Output:** Thư mục dự án gọn, không còn component trùng lặp.
* **Tiêu chí đạt:** mọi import cập nhật đúng, `npm run build` thành công; không có hai component làm cùng một việc.
* **Hạn nộp:** trước Buổi 5.
* **Cách nộp:** PR vào `dev`, mô tả rõ các file đã di chuyển/gộp.

---

### Bài 05: Giao diện chuyên nghiệp với Ant Design, Bootstrap/Tailwind & tùy biến Theme

#### 🛠️ Guided Practice (45'): Cài AntD, cấu hình Theme, `BookingModal`

* **Yêu cầu:** Cài `antd` và `@ant-design/nextjs-registry`; bọc `AntdRegistry` + `ConfigProvider` trong `app/layout.tsx` với `colorPrimary: '#6366F1'`, `borderRadius: 8`. Xây `BookingModal.tsx` dùng `Modal`, `Form`, `Select` (loại vé), `InputNumber` (1–10), `DatePicker`, ghi chú.
* **Output:** Modal mở mượt, màu nút và viền theo Theme.
* **Tiêu chí đạt:** không lỗi SSR/Hydration mismatch trên Console.

#### 🧩 Unguided Practice (45'): Trang `/admin/orders`

* **Yêu cầu:** Dùng `Table` và `Tag` của AntD; cột: Mã đơn, Tên khách hàng, Tên sự kiện, Ngày đặt, Tổng tiền, Trạng thái (SUCCESS xanh lá, PENDING cam, CANCELLED đỏ), Action "Xem chi tiết". Interface `OrderType`, mock 10 đơn, lọc theo trạng thái, phân trang 5 mục/trang.
* **Output:** Bảng dữ liệu căn chỉnh đẹp, lọc và chuyển trang hoạt động.
* **Tiêu chí đạt:** `columns` có kiểu `ColumnsType<OrderType>` (hoặc `TableProps<OrderType>['columns']`); không `any`.

#### 🏠 BTVN (cá nhân): Responsive cho component AntD

* **Yêu cầu:** Rà soát các component AntD mình đã dùng; dùng `Row`/`Col` với `xs`, `sm`, `md`, `lg` để bố cục co giãn; sửa mọi lỗi vỡ khung ở 5 màn hình chính.
* **Output:** Không có thanh cuộn ngang trên di động.
* **Tiêu chí đạt:** kiểm tra ở 375px, 768px, 1440px bằng Chrome DevTools; đính kèm ảnh trước/sau.
* **Hạn nộp:** trước Buổi 6.
* **Cách nộp:** PR vào `dev` kèm ảnh chụp màn hình trong mô tả PR.

---

### Bài 06: Logic & State Management với React Hooks

#### 🛠️ Guided Practice (45'): `TicketQuantitySelector`

* **Yêu cầu:** Client Component quản lý danh sách hạng vé (VVIP, VIP, Standard), mỗi hạng có `price`, `quantity`, `max`; hàm `handleIncrease(id)`, `handleDecrease(id)`; tính `totalAmount`, `totalTickets` bằng `useMemo`.
* **Output:** Tổng tiền và số vé cập nhật ngay khi tăng/giảm.
* **Tiêu chí đạt:** không giảm dưới 0, không vượt `max`; nút "Thanh toán" bị disable khi `totalTickets === 0`.

#### 🧩 Unguided Practice (45'): `EventFilterBar` có Debounce

* **Yêu cầu:** Ô tìm kiếm từ khóa, dropdown khoảng giá, lọc theo ngày (theo danh mục nếu cần); state `searchKeyword`, `priceRange`, `selectedDate`; debounce 200ms bằng custom hook `useDebounce`; trả kết quả lên cha qua `onFilterChange(filters)`.
* **Output:** Lọc mượt, gõ phím không giật.
* **Tiêu chí đạt:** kiểu `Filters` rõ ràng; `useEffect` của debounce có hàm dọn dẹp `clearTimeout`.

#### 🏠 BTVN (nhóm, mỗi thành viên có PR riêng): Tích hợp 50% và chuẩn bị giữa kỳ

* **Yêu cầu:**
  * Ghép toàn bộ State, UI, Dynamic Route, Reusable Component từ Bài 01–06 thành ứng dụng chạy được.
  * Chuẩn bị slide báo cáo và để source code trên GitHub (GV có quyền truy cập).
* **Output:** Dự án chạy ổn định, không có màn hình lỗi đỏ (Runtime Error), sẵn sàng demo.
* **Tiêu chí đạt:** `dev` đã merge vào `main`; mỗi thành viên có commit tính năng; README có bảng phân công.
* **Hạn nộp:** trước Buổi 7.
* **Cách nộp:** link repo + link PR tích hợp trên LMS.

---

### Bài 07: Kiểm tra giữa kỳ – Báo cáo tiến độ 50% dự án

#### 🛠️ Guided Practice (45'): Đóng gói báo cáo

* **Yêu cầu:** Chạy `npm run lint` và `npm run build`, sửa toàn bộ lỗi TypeScript/ESLint ẩn. Viết `README.md` gồm: mô tả dự án, thành viên & phân công (Họ tên, MSSV, Vai trò, Tính năng), hướng dẫn cài đặt, cấu trúc thư mục, link Wireframe Figma. Tổng hợp link preview/demo Bài 01–06.
* **Output:** README ở root repo; build pass 100%.
* **Tiêu chí đạt:** không còn lỗi Compile/Type Error.

#### 🧩 Unguided Practice (45'): Cross-review và Hot Reload

* **Yêu cầu:** Review chéo giữa các trang (Trang chủ, Chi tiết sự kiện, Đặt vé, Dashboard Admin); sửa console warning, hydration mismatch còn tồn đọng; chuẩn bị slide 5–7 trang.
* **Output:** Ứng dụng chạy mượt, Console không còn cảnh báo đỏ/vàng.
* **Tiêu chí đạt:** chạy lại `npm run build` thành công sau khi sửa.

#### 🏠 BTVN (cá nhân): Cập nhật theo góp ý và chuẩn bị tích hợp API

* **Yêu cầu:** Sửa UI/codebase theo nhận xét của GV ở buổi báo cáo; đọc trước tài liệu RESTful API/Swagger UI của Smart Event Hub do GV cung cấp, ghi lại các endpoint mình sẽ phụ trách.
* **Output:** Codebase sạch, sẵn sàng ghép nối Backend.
* **Tiêu chí đạt:** mỗi góp ý có commit/PR xử lý tương ứng.
* **Hạn nộp:** trước Buổi 8.
* **Cách nộp:** PR vào `dev`; liệt kê các góp ý đã xử lý trong mô tả PR.

> 📋 Đặc tả đầy đủ sản phẩm nộp giữa kỳ: xem **Phần D**.

---

### Bài 08: Data Fetching & tích hợp RESTful API

#### 🛠️ Guided Practice (45'): `getEvents()` và Trang chủ dữ liệu thật

* **Yêu cầu:** Thả JSON response mẫu của endpoint danh sách sự kiện trên Swagger vào AI để sinh interface (`EventItem`, `Organizer`…); viết `services/eventService.ts` với `getEvents(params)` (query `page`, `limit`, `search`); fetch trong Server Component `app/page.tsx` và truyền props cho `EventList`.
* **Output:** Trang chủ hiển thị danh sách sự kiện lấy từ Backend.
* **Tiêu chí đạt:** base URL lấy từ `process.env.NEXT_PUBLIC_API_URL`; không `any`; response bọc trong `ApiResponse<T>`.

#### 🧩 Unguided Practice (45'): `getEventById(id)` cho trang chi tiết

* **Yêu cầu:** Viết `getEventById(id: string)` (đề cương gọi `getEventDetail`); tích hợp vào `/events/[id]`; hiển thị banner, tên, giá, ban tổ chức; API trả 404 thì gọi `notFound()`; bọc `try/catch` lỗi kết nối.
* **Output:** Bấm từng Card, trang chi tiết tải đúng dữ liệu theo id.
* **Tiêu chí đạt:** id không tồn tại hiển thị trang 404 của dự án.

#### 🏠 BTVN (cá nhân): Xử lý sự cố API

* **Yêu cầu:** Hiển thị giao diện phù hợp khi API gặp Network Error hoặc Server 500, kết hợp `notification`/`Alert` của AntD hoặc `error.tsx`; giữ Loading Spinner/Skeleton khi đang tải.
* **Output:** Web app có thông báo lỗi lịch sự khi server gián đoạn, không trắng trang.
* **Tiêu chí đạt:** thử bằng cách đổi `NEXT_PUBLIC_API_URL` sai hoặc tắt mạng trong DevTools; mô tả cách thử trong PR.
* **Hạn nộp:** trước Buổi 9.
* **Cách nộp:** PR vào `dev`.

---

### Bài 09: Form Validation (React Hook Form + Zod), Local Storage & Complex UI State

#### 🛠️ Guided Practice (45'): `LoginForm`

* **Yêu cầu:** Cài `react-hook-form`, `zod`, `@hookform/resolvers`; tạo `loginSchema` (email đúng định dạng, password ≥ 6 ký tự); `LoginForm.tsx` dùng `useForm` + `zodResolver`, hiển thị lỗi dưới từng ô; submit gọi API đăng nhập, lưu token vào `localStorage` (khóa `accessToken`), hiện `message.success` và chuyển về Trang chủ.
* **Output:** Form báo lỗi ngay khi nhập sai; đăng nhập thành công lưu token và điều hướng.
* **Tiêu chí đạt:** kiểu dữ liệu form lấy từ `z.infer<typeof loginSchema>`.

#### 🧩 Unguided Practice (45'): Form "Tạo sự kiện mới" `/admin/create-event`

* **Yêu cầu:** `createEventSchema` gồm tên (≥ 5 ký tự), địa điểm, ngày bắt đầu/kết thúc (DatePicker), giá vé (> 0), ảnh bìa (URL), số lượng vé, mô tả; dùng `.refine()` bắt buộc ngày kết thúc sau ngày bắt đầu.
* **Output:** Form bắt được trường hợp ngày không hợp lệ.
* **Tiêu chí đạt:** thông báo lỗi gắn đúng ô `endDate`; nút submit bị khóa khi đang gửi.

#### 🏠 BTVN (cá nhân): Sẵn sàng cho PBL

* **Yêu cầu:** Đăng ký tài khoản Vercel và GitHub (nếu chưa có); đẩy code mới nhất lên GitHub; kiểm tra kết nối repository với Vercel Dashboard.
* **Output:** 100% thành viên có tài khoản Vercel sẵn sàng kết nối CI/CD.
* **Tiêu chí đạt:** import thử repo vào Vercel thấy được danh sách nhánh.
* **Hạn nộp:** trước Buổi 10.
* **Cách nộp:** ảnh chụp Vercel Dashboard đã thấy repo, nộp lên LMS.

---

### Bài 10: PBL 1 – Refactoring, Optimization & Responsive Polish

> Buổi PBL không chia Guided/Unguided. Sau 30 phút định hướng, nhóm làm 3 phần liên tiếp (mỗi phần 60'), GV làm mentor tại từng nhóm.

#### 🛠️ PBL Phần 1 (60'): Responsive Polish

* **Yêu cầu:** Kiểm tra Home, Listing, Event Detail, Booking Modal, Admin Orders ở 375px, 768px, 1440px; sửa tràn ngang; chuyển Menu/Filter Bar sang `Drawer`/`Collapse` trên di động.
* **Tiêu chí đạt:** không có thanh cuộn ngang; nút/link đủ lớn để chạm trên Mobile.

#### 🧩 PBL Phần 2 (60') & Phần 3 (60'): Refactoring và Zero Warning

* **Yêu cầu Phần 2:** tách code lặp thành Reusable Component; xóa biến không dùng, `console.log`, `any`; gom SCSS lặp thành mixin/biến chung.
* **Yêu cầu Phần 3:** chạy dev kiểm tra Hot Reload; sửa warning (`React does not recognize prop…`, `Hydration failed…`); GV review code và nghiệm thu danh sách bug đã sửa.
* **Tiêu chí đạt:** codebase giảm >20% số dòng mà không đổi logic; TypeScript strict pass; Zero Console Warnings; có biên bản nghiệm thu PBL 1.

#### 🏠 BTVN (nhóm): Kịch bản kiểm thử toàn hệ thống

* **Yêu cầu:** Viết file kịch bản chạy thử (`Test_Cases_Scenario`) cho các luồng chính, mỗi ca gồm: Mã ca, Chức năng, Tiền điều kiện, Các bước, Dữ liệu vào, Kết quả mong đợi, Kết quả thực tế, Trạng thái. Chuẩn bị repo GitHub ở nhánh `main` cho buổi PBL 2.
* **Output:** Tài liệu test sẵn sàng để chạy trên bản deploy.
* **Tiêu chí đạt:** tối thiểu bao phủ: xem danh sách/lọc, chi tiết sự kiện, chọn vé/ghế, đặt vé, đăng nhập, Wishlist, trang Admin.
* **Hạn nộp:** trước Buổi 11.
* **Cách nộp:** file `[MãLớp]_[Nhóm]_TestCasesScenario.docx` hoặc `.md` lên LMS (đồng thời lưu trong `docs/` của repo).

---

### Bài 11: PBL 2 – CI/CD, Deploy Vercel, SEO & Performance

#### 🛠️ PBL Phần 1 (60'): SEO & Metadata động

* **Yêu cầu:** Metadata tĩnh ở Root Layout (title, description, keywords, openGraph); `generateMetadata` cho `/events/[id]` lấy dữ liệu bằng `getEventById(id)` (nhớ `await params`), có metadata dự phòng khi không tìm thấy; thay toàn bộ `<img>` bằng `next/image` với `sizes`, `priority` phù hợp.
* **Tiêu chí đạt:** chia sẻ link lên Zalo/Facebook hiện đúng ảnh và tiêu đề sự kiện.

#### 🧩 PBL Phần 2 (60') & Phần 3 (60'): Deploy Vercel và Lighthouse

* **Yêu cầu Phần 2:** đẩy code lên `main`; kết nối repo với Vercel; khai báo `NEXT_PUBLIC_API_URL`; build & deploy, xử lý Build Fail nếu có.
* **Yêu cầu Phần 3:** chạy Lighthouse trên link Vercel; phân tích Performance, Accessibility, Best Practices, SEO; dùng Vibe Coding tìm giải pháp tối ưu.
* **Tiêu chí đạt:** link dạng `*.vercel.app` hoạt động, gọi API và LocalStorage ổn định; Performance > 85, SEO > 90.

#### 🏠 BTVN (nhóm): Báo cáo văn bản & slide cuối kỳ

* **Yêu cầu:** Viết báo cáo Word/PDF theo mẫu (xem dàn ý ở Phần E): kiến trúc dự án, sơ đồ Wireframe, mô tả API tích hợp, phân công công việc, minh chứng Git commit, link Vercel Live. Chuẩn bị slide thuyết trình cho Buổi 12.
* **Output:** File báo cáo hoàn chỉnh và slide sẵn sàng cho buổi bảo vệ.
* **Tiêu chí đạt:** đúng cấu trúc; hình ảnh có chú thích; minh chứng Git thể hiện đóng góp từng thành viên.
* **Hạn nộp:** trước Buổi 12.
* **Cách nộp:** `[MãLớp]_[Nhóm]_BaoCaoCuoiKy.pdf` và `[MãLớp]_[Nhóm]_SlideCuoiKy.pptx` (hoặc `.pdf`) lên LMS.

---

### Bài 12: Thi Hackathon & Final Showcase

#### 🎤 Nhiệm vụ tại buổi (225')

* **Triển lãm Live Products (30'):** mở link Vercel để GV và các nhóm khác trải nghiệm chéo (Cross-Testing).
* **Thuyết trình (8') + Q&A phản biện (5') mỗi nhóm:** thể hiện Wireframe → Vercel App, kỹ thuật Vibe Coding đã dùng, minh chứng Git commit.
* **Tổng kết & trao giải (35'):** GV công bố điểm, trao giải nhóm có UI/UX Vibe Coding xuất sắc nhất.

Bài 12 không có BTVN. Sau buổi, các bạn hoàn thành bài đăng phản tư trên diễn đàn (xem `discussion/`).

> 📋 Đặc tả đầy đủ sản phẩm nộp cuối kỳ: xem **Phần E**.

---

## PHẦN D. ĐẶC TẢ DELIVERABLE GIỮA KỲ (BUỔI 7 – 30%)

#### Sản phẩm phải nộp

| # | Sản phẩm | Yêu cầu | Cách nộp |
|---|---|---|---|
| 1 | Wireframe 5 màn hình | Trang chủ, Chi tiết sự kiện, Đặt vé, Trang cá nhân, Admin Dashboard; chuẩn Header/Footer/Content | Link Figma + ảnh trong `docs/wireframes/` |
| 2 | Source code | Repo Git có commit đầy đủ của các thành viên; `npm run build` thành công; README chuẩn | Link repository (nhánh `main`) |
| 3 | Giao diện demo | Giao diện đã áp dụng Ant Design/SCSS responsive; demo trực tiếp trên máy hoặc link preview nếu nhóm đã deploy thử | Demo tại lớp (link nếu có) |
| 4 | Slide báo cáo | 5–7 slide tóm tắt kết quả đạt được | File `[MãLớp]_[Nhóm]_SlideGiuaKy.pdf` |

#### Hình thức và rubric

Mỗi nhóm có **10 phút** thuyết trình & demo, sau đó **5 phút** GV hỏi phản biện cá nhân (kiểm tra code từng người đảm nhiệm). Nội dung demo bắt buộc: Wireframe 5 màn hình, giao diện responsive Mobile/Desktop, luồng routing, Git commit log từng cá nhân.

| Tiêu chí | Điểm tối đa | Minh chứng |
|---|---|---|
| Wireframe đủ 5 màn hình & cấu trúc chuẩn | 1.5 | Figma/ảnh, khớp với giao diện thật |
| UI chuyên nghiệp (AntD/Bootstrap + Responsive + Hot Reload) | 2.0 | Demo ở nhiều kích thước, Console sạch |
| Routing & Component Architecture | 1.0 | Cây `app/`, thư mục `components/ui`, `common`, `features` |
| Git Commit & phối hợp nhóm | 0.5 | Commit log, PR có review |
| **Tổng** | **5.0** | GV quy đổi sang trọng số 30% |

---

## PHẦN E. ĐẶC TẢ DELIVERABLE CUỐI KỲ (BUỔI 12 – 40%)

#### Sản phẩm phải nộp

| # | Sản phẩm | Yêu cầu |
|---|---|---|
| 1 | Link Vercel Live | Bản deploy từ nhánh `main`, gọi API thật, biến môi trường cấu hình đúng |
| 2 | Repository GitHub | Commit log riêng từng thành viên, PR có review, README cập nhật |
| 3 | Báo cáo Word/PDF | Theo dàn ý bên dưới, file `[MãLớp]_[Nhóm]_BaoCaoCuoiKy.pdf` |
| 4 | Slide thuyết trình | Dùng cho 8 phút trình bày, file `[MãLớp]_[Nhóm]_SlideCuoiKy` |
| 5 | Minh chứng chất lượng | Ảnh Lighthouse (Performance > 85, SEO > 90), file Test Cases Scenario |

#### Dàn ý báo cáo gợi ý

1. Giới thiệu dự án Smart Event Hub, mục tiêu, phạm vi.
2. Phân tích yêu cầu và Wireframe 5 màn hình (ảnh có chú thích).
3. Kiến trúc: công nghệ, cây thư mục `app/`, sơ đồ component, danh sách route.
4. Mô tả API tích hợp: endpoint, kiểu dữ liệu TypeScript, xử lý loading/lỗi.
5. Các tính năng chính và logic xử lý (đặt vé, chọn ghế, form + Zod, Wishlist).
6. Vibe Coding: prompt tiêu biểu, phần AI sinh và phần nhóm đã sửa.
7. Triển khai: Vercel, biến môi trường, SEO, kết quả Lighthouse, kết quả test case.
8. Phân công công việc và minh chứng Git commit từng thành viên.
9. Kết luận, hạn chế, hướng phát triển.

#### Rubric và cách tính điểm

| Tiêu chí | Trọng số | PI |
|---|---|---|
| Mô hình hóa UI & Wireframe | 15% (1.5đ) | PI 1.4 (CLO1) |
| Giao diện & Vibe Coding | 20% (2.0đ) | PI 2.3 (CLO2) |
| Logic, TypeScript & REST API | 20% (2.0đ) | PI 2.3 (CLO2) |
| Deploy Vercel, SEO & Lighthouse | 15% (1.5đ) | PI 5.1 (CLO4) |
| Báo cáo văn bản & minh chứng Git | 15% (1.5đ) | PI 3.1 (CLO3), PI 5.1 |
| Thuyết trình Showcase & phản biện Q&A | 15% (1.5đ) | PI 3.1 (CLO3), PI 5.1 |

```text
Điểm cuối kỳ cá nhân = (Điểm đồ án nhóm × 0.7) + (Điểm phản biện cá nhân × 0.3)
```

**Điểm thưởng Vibe Coding (+0.5 đến +1.0 vào điểm quá trình):** Vibe Coding Master (prompt workflow riêng, hiệu quả), UI Innovation (Dark/Light Mode, micro-interactions), Ultra Performance (Lighthouse Performance 100/100).

> 📌 Bảng mô tả mức Xuất sắc/Khá/Trung bình/Yếu của từng tiêu chí nằm trong thư mục `assessment/`.
