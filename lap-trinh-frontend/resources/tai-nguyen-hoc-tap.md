# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## TÀI NGUYÊN HỌC TẬP (Learning Resources)

> **Dùng khi nào:** trước giờ học (đọc tài liệu, xem video theo từ khóa), trong giờ (tra docs, lấy prompt mẫu), sau giờ (làm BTVN, ôn self-check)
> **Dự án xuyên suốt:** Smart Event Hub – Next.js 15 App Router · TypeScript strict · SCSS Module · Ant Design v5

---

Trang này có năm phần: tài liệu đọc bắt buộc theo từng buổi, tài liệu chính thức của các công nghệ, bộ công cụ cần cài, thư viện prompt Vibe Coding gom từ 11 buổi học và danh sách chủ đề video gợi ý. Các bạn nên đánh dấu (bookmark) trang này ngay từ tuần đầu.

> ⚠️ **Về đường dẫn:** Các link đọc bắt buộc giữ nguyên như trong tài liệu lý thuyết của học phần. Một số trang docs Next.js đã được tổ chức lại theo phiên bản mới nên có thể tự chuyển hướng; nếu gặp trang không tìm thấy, hãy dùng ô tìm kiếm tại `https://nextjs.org/docs` với đúng tên chủ đề.

---

## 1. TÀI LIỆU ĐỌC BẮT BUỘC THEO TỪNG BUỔI (Readings)

#### Cách đọc hiệu quả

Đọc trước giờ học, mỗi buổi khoảng 45–60 phút. Đừng cố đọc hết từng chữ. Hãy đọc với câu hỏi self-check trong đầu, chạy thử ít nhất một ví dụ code trong docs, rồi ghi lại 2–3 điều còn thắc mắc để hỏi trên lớp.

| Buổi | Tài liệu | Đường dẫn | Đọc để trả lời được |
|---|---|---|---|
| 01 | Sass Official Documentation | https://sass-lang.com/documentation/ | Mixin, biến, nesting, `map-get` dùng thế nào? |
| 01 | TypeScript Handbook for React | https://www.typescriptlang.org/docs/handbook/react.html | Khác biệt `interface` và `type`; khi nào dùng loại nào? |
| 01 | Next.js CSS Modules | https://nextjs.org/docs/app/building-your-application/styling/css-modules | Vì sao CSS Modules tránh được xung đột CSS toàn cục? |
| 02 | Atomic Design Methodology (Brad Frost) | https://atomicdesign.bradfrost.com/ | Atomic Design giúp tái sử dụng code ra sao? |
| 02 | v0.dev Generative UI Documentation | https://v0.dev/docs | Cần chú ý gì khi refactor TSX do AI sinh từ wireframe? |
| 03 | Next.js App Router Routing Docs | https://nextjs.org/docs/app/building-your-application/routing | Route Groups `(group)` có lợi gì cho layout? |
| 03 | React Server Components | https://react.dev/reference/rsc/server-components | Khi nào bắt buộc thêm `'use client'`? |
| 04 | Next.js Dynamic Routes Guide | https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes | Lấy `params`, `searchParams` ở Server và Client Component thế nào? |
| 04 | React TypeScript Cheatsheet – Props | https://react-typescript-cheatsheet.netlify.app/docs/basic/getting-started/basic_type_example/ | Vì sao nên mở rộng Props từ HTML attributes? |
| 05 | Ant Design v5 Official Docs | https://ant.design/components/overview/ | Override CSS một component AntD mà không ảnh hưởng chỗ khác? |
| 05 | Ant Design with Next.js App Router | https://ant.design/docs/react/use-with-next | Hydration mismatch do đâu, khắc phục bằng registry ra sao? |
| 06 | React Docs on Hooks | https://react.dev/reference/react/hooks | `useMemo` và `useCallback` khác nhau ở mục đích nào? |
| 06 | You Might Not Need an Effect | https://react.dev/learn/you-might-not-need-an-effect | Vì sao không dùng `useEffect` để tính dữ liệu suy ra từ state/props? |
| 07 | Conventional Commits Specification | https://www.conventionalcommits.org/ | Commit message thế nào thì minh chứng được đóng góp cá nhân? |
| 07 | Next.js Production Checklist | https://nextjs.org/docs/app/building-your-application/deploying/production-checklist | Vì sao chạy được ở `dev` vẫn có thể fail ở `build`? |
| 08 | Next.js Data Fetching, Caching, and Revalidating | https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating | `revalidate` trong `fetch` hoạt động thế nào? |
| 08 | Axios Documentation | https://axios-http.com/docs/intro | Fetch ở Server Component khác gì gọi Axios ở Client? |
| 09 | React Hook Form Documentation | https://react-hook-form.com/ | Vì sao RHF + Zod tốt cho cả hiệu năng lẫn type safety? |
| 09 | Zod Documentation | https://zod.dev/ | `z.infer`, `.refine()` dùng ra sao? |
| 10 | Refactoring Guru – Code Smells | https://refactoring.guru/refactoring/smells | Dấu hiệu nào cho thấy component cần refactor gấp? |
| 10 | Google Responsive Web Design Basics | https://web.dev/responsive-web-design-basics/ | Xử lý tràn ngang (horizontal overflow) trên di động thế nào? |
| 11 | Next.js Metadata Documentation | https://nextjs.org/docs/app/building-your-application/optimizing/metadata | Cấu hình `metadata` tĩnh và `generateMetadata` động thế nào? |
| 11 | Google Lighthouse Audit Guide | https://developer.chrome.com/docs/lighthouse/overview/ | Vì sao `next/image` cải thiện Performance; xử lý CLS ra sao? |
| 12 | Ôn lại toàn bộ readings + Rubric Hackathon | (thư mục `assessment/`) | Sản phẩm nhóm đã đáp ứng từng tiêu chí rubric chưa? |

> 📝 **Lưu ý Next.js 15:** Trong các ví dụ cũ trên mạng, `params` là object thường (`params.id`). Từ Next.js 15, `params` và `searchParams` là `Promise`, nên viết `const { id } = await params;`.

---

## 2. TÀI LIỆU CHÍNH THỨC (Official Documentation)

#### Framework và ngôn ngữ

| Công nghệ | Trang chính thức | Dùng nhiều ở buổi |
|---|---|---|
| Next.js | https://nextjs.org/docs | 03 → 11 |
| React | https://react.dev/ | 03, 04, 06, 09 |
| TypeScript | https://www.typescriptlang.org/docs/ | 01 → 12 |
| Sass (SCSS) | https://sass-lang.com/documentation/ | 01, 02, 05, 10 |

#### Thư viện giao diện

| Thư viện | Trang chính thức | Ghi chú |
|---|---|---|
| Ant Design v5 | https://ant.design/components/overview/ | Thư viện UI chính của dự án; tích hợp Next.js qua `@ant-design/nextjs-registry` |
| Ant Design – dùng với Next.js | https://ant.design/docs/react/use-with-next | Cấu hình `AntdRegistry`, tránh FOUC |
| Bootstrap 5 | https://getbootstrap.com/docs/5.3/getting-started/introduction/ | Phương án thay thế, mạnh về utilities và grid |
| Tailwind CSS | https://tailwindcss.com/docs | Phương án thay thế; một số prompt mẫu cho phép chọn Tailwind hoặc SCSS |

#### Dữ liệu, form và lưu trữ

| Thư viện / API | Trang chính thức | Ghi chú |
|---|---|---|
| React Hook Form | https://react-hook-form.com/ | Quản lý form, ít re-render |
| Zod | https://zod.dev/ | Schema validation, sinh type bằng `z.infer` |
| Axios | https://axios-http.com/docs/intro | Gọi REST API phía Client |
| Web Storage API (MDN) | https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API | `localStorage`, `sessionStorage` |

#### Triển khai, chất lượng và quy chuẩn

| Chủ đề | Trang chính thức | Ghi chú |
|---|---|---|
| Vercel | https://vercel.com/docs | CI/CD, Environment Variables, Preview/Production |
| Lighthouse | https://developer.chrome.com/docs/lighthouse/overview/ | Audit Performance, Accessibility, Best Practices, SEO |
| web.dev | https://web.dev/ | Responsive, Core Web Vitals (LCP, CLS, INP) |
| Conventional Commits | https://www.conventionalcommits.org/ | Chuẩn commit message của nhóm |
| Refactoring Guru | https://refactoring.guru/refactoring/smells | Danh mục code smell và kỹ thuật refactor |
| Atomic Design | https://atomicdesign.bradfrost.com/ | Phân rã giao diện thành atom → page |

---

## 3. CÔNG CỤ (Tools)

#### Danh sách công cụ cần chuẩn bị

| Công cụ | Dùng để | Trang tải / truy cập | Cần từ |
|---|---|---|---|
| VS Code | Trình soạn thảo chính | https://code.visualstudio.com/ | Buổi 1 |
| Node.js (bản LTS) | Chạy Next.js, npm | https://nodejs.org/ | Buổi 1 |
| Git | Quản lý phiên bản | https://git-scm.com/ | Buổi 1 |
| GitHub | Repo nhóm, Pull Request, code review | https://github.com/ | Buổi 1 |
| Cursor | Trình soạn thảo tích hợp AI, đọc toàn bộ codebase | https://cursor.com/ | Buổi 1 |
| GitHub Copilot | AI gợi ý code trong VS Code (gói miễn phí cho sinh viên qua GitHub Education) | https://github.com/features/copilot | Buổi 1 |
| v0.dev | Sinh giao diện React từ mô tả/ảnh wireframe | https://v0.dev/ | Buổi 2 |
| Claude | Trợ lý AI, đọc ảnh wireframe, review code | https://claude.ai/ | Buổi 1 |
| ChatGPT | Trợ lý AI, giải thích lỗi, sinh type từ JSON | https://chatgpt.com/ | Buổi 1 |
| Figma | Vẽ wireframe 5 màn hình | https://www.figma.com/ | Buổi 2 |
| Swagger UI | Đọc tài liệu API Backend do GV cung cấp, thử request | https://swagger.io/tools/swagger-ui/ | Buổi 7–8 |
| Chrome DevTools | Responsive mode, Console, Network, Lighthouse | https://developer.chrome.com/docs/devtools/ | Buổi 1 |
| Vercel | Deploy, CI/CD | https://vercel.com/ | Buổi 9 |

#### Kiểm tra môi trường sau khi cài

```bash
node -v          # nên là bản LTS hiện hành
npm -v
git --version
git config --global user.name "Ho Ten"
git config --global user.email "email@example.com"

# Khởi tạo dự án (Buổi 3)
npx create-next-app@latest smart-event-hub --typescript --eslint --app
cd smart-event-hub
npm install sass antd @ant-design/nextjs-registry
npm run dev
```

> 💡 Email trong `git config` nên trùng email tài khoản GitHub, để commit được tính đúng người trong Git log khi GV chấm minh chứng đóng góp cá nhân.

#### File quy tắc cho AI (`.cursorrules`)

Buổi 1 yêu cầu thiết lập rule cho Cursor/Copilot. Một file mẫu để nhóm bắt đầu, đặt ở root repo:

```text
Dự án: Smart Event Hub – Next.js 15 App Router, TypeScript strict, SCSS Module, Ant Design v5.
- Luôn viết TypeScript, không dùng any. Union type dùng dấu |.
- Mặc định Server Component; chỉ thêm 'use client' khi dùng hook, sự kiện hoặc Browser API.
- params và searchParams trong page là Promise: const { id } = await params;
- Style: SCSS Module (*.module.scss), dùng biến trong styles/_variables.scss và mixin respond-to trong styles/_mixins.scss.
- Ảnh dùng next/image, link dùng next/link.
- Component đặt trong components/ui, components/common hoặc components/features.
- Gọi API qua services/, base URL lấy từ process.env.NEXT_PUBLIC_API_URL.
- Không để lại console.log. Đặt tên rõ nghĩa, tiếng Anh.
```

---

## 4. THƯ VIỆN PROMPT VIBE CODING MẪU

### 4.1. Nguyên tắc chung

#### Cấu trúc prompt 3 thành phần

Mọi prompt trong học phần đi theo khung **Bối cảnh (Context) → Yêu cầu (Requirement) → Ràng buộc (Constraints)**. AI lo phần khung code (boilerplate); các bạn chịu trách nhiệm kiểm duyệt type, logic và refactor. Nói cách khác, các bạn là Architect: yêu cầu AI tạo khung và TypeScript interface trước, sau đó mới tới phần chi tiết.

```text
[Context]     Dự án Smart Event Hub, Next.js 15 App Router, TypeScript strict, SCSS Module, Ant Design v5.
[Requirement] Tạo component ... gồm ... ; interface ... có các trường ...
[Constraints] Không dùng any; dùng next/image; mixin respond-to; giải thích ngắn các phần quan trọng.
```

#### Checklist kiểm duyệt code AI (dùng cho mọi prompt)

* [ ] Có `any` hoặc ép kiểu `as` vô lý không?
* [ ] Union type có bị viết thành `string` chung chung không?
* [ ] `'use client'` có thừa hoặc thiếu không?
* [ ] `params`/`searchParams` đã `await` chưa (Next.js 15)?
* [ ] Import đúng gói, đúng phiên bản (Ant Design v5, không phải v4)?
* [ ] Responsive ở 375px / 768px / 1440px?
* [ ] Có inline-style, magic number, `console.log` thừa không?
* [ ] Mình giải thích được từng dòng chưa? Nếu chưa, hỏi lại AI "giải thích đoạn này" trước khi commit.

> ⚠️ Trong file trích xuất từ tài liệu gốc, dấu `|` của union type từng bị hiển thị thành `/`. Các prompt dưới đây đã được sửa lại đúng cú pháp TypeScript.

### 4.2. Prompt theo từng buổi

#### Buổi 01 – EventCard, HeaderNavigationBar

```text
Hãy đóng vai một Chuyên gia Front-End Developer kinh nghiệm với Next.js và TypeScript.
Hãy viết cho tôi một Component React tên là EventCard.tsx kèm theo file SCSS Module EventCard.module.scss.

Yêu cầu chi tiết:
1. TypeScript Interface EventProps:
   - id: string
   - title: string
   - imageUrl: string
   - startDate: string
   - location: string
   - price: number
   - status: 'UPCOMING' | 'ONGOING' | 'ENDED'
2. SCSS Module:
   - Sử dụng CSS Grid/Flexbox.
   - Tạo mixin responsive: Mobile (< 640px), Tablet (640px - 1024px), Desktop (> 1024px).
   - Màu badge status: UPCOMING (Xanh dương), ONGOING (Xanh lá), ENDED (Xám).
3. Ràng buộc:
   - Sử dụng Next.js Image component (next/image).
   - Code rõ ràng, ngắn gọn, có comment giải thích các phần quan trọng.
```

```text
Tạo giúp tôi Component HeaderNavigationBar.tsx bằng Next.js App Router và TypeScript.
- Yêu cầu UI: Gồm Logo bên trái, Search Input ở giữa, Menu điều hướng và nút Auth bên phải.
- Yêu cầu TypeScript: Định nghĩa interface NavItem { label: string; href: string; isExternal?: boolean }.
- Yêu cầu SCSS Module: Viết hiệu ứng Sticky Navigation khi scroll và hiệu ứng Hover underline mượt mà cho Menu Link.
- Viết theo chuẩn Clean Code, không xài any.
```

```text
Hãy tạo cho tôi 1 Component Next.js App Router bằng TypeScript sử dụng Ant Design v5 Card để hiển thị thông tin sự kiện gồm: tên, ngày, giá vé, nút đặt vé. Đảm bảo có Interface rõ ràng.
```

#### Buổi 02 – Wireframe sang TSX

```text
[Gửi kèm ảnh phác thảo Wireframe màn hình Trang chủ]
Bạn là một Senior UI/UX Developer. Hãy chuyển đổi hình ảnh Wireframe này thành React Component (Next.js App Router, TypeScript).

Yêu cầu chi tiết:
1. Hãy phân rã giao diện thành 3 Component nhỏ: HeroBanner, FeaturedEventsSection, CategoryFilter.
2. Sử dụng TailwindCSS hoặc SCSS Module để tái hiện lại chính xác bố cục lưới (Grid) như ảnh.
3. Tạo dữ liệu giả (Mock Data) bằng TypeScript với 4 phần tử mẫu.
4. Đảm bảo cấu trúc HTML chuẩn Semantic (<header>, <main>, <section>, <article>).
```

```text
Tôi có ý tưởng thiết kế Màn hình Chi tiết Sự kiện như sau:
- Cột bên trái (70%): Banner sự kiện (16:9), Tiêu đề lớn, Thông tin chi tiết diễn giả (Avatar, Tên, Bio), Bài viết mô tả nội dung.
- Cột bên phải (30%): Thẻ Sticky chứa Giá vé từ X đồng, Hạn đặt vé, Nút "Đặt vé ngay" màu cam nổi bật.

Hãy sinh mã nguồn Next.js TypeScript và SCSS/Tailwind cho màn hình này.
```

#### Buổi 03 – Cấu trúc App Router

```text
Hãy hướng dẫn tạo cấu trúc thư mục Next.js App Router cho dự án "Smart Event Hub" với các yêu cầu:
1. Root Layout chứa Header và Footer chung.
2. Route Group (auth) có AuthLayout riêng (chỉ chứa Logo và Form ở trung tâm màn hình) cho các trang /login và /register.
3. Nested Route /events và /events/categories.
Hãy cho tôi sơ đồ cây thư mục chi tiết và nội dung mã nguồn của các file layout.tsx tương ứng.
```

```text
Tạo giúp tôi cấu trúc Route Group (admin) trong Next.js App Router.
- AdminLayout: Gồm Sidebar bên trái (Dashboard, Quản lý sự kiện, Quản lý người dùng) và Header Admin ở trên.
- Tạo file loading.tsx sử dụng hiệu ứng Skeleton UI đơn giản bằng SCSS/Tailwind.
- Viết bằng TypeScript.
```

#### Buổi 04 – Reusable Button, Dynamic Category

```text
Hãy thiết kế cho tôi một Reusable Component tên là Button.tsx trong Next.js TypeScript.

Yêu cầu:
1. Props Interface ButtonProps mở rộng từ React.ButtonHTMLAttributes<HTMLButtonElement>:
   - variant: 'primary' | 'secondary' | 'danger' | 'outline'
   - size: 'sm' | 'md' | 'lg'
   - isLoading?: boolean
   - leftIcon?: React.ReactNode
2. Xử lý SCSS Module / TailwindCSS tương ứng với các biến thể.
3. Khi isLoading = true, vô hiệu hóa button (disabled) và hiển thị Spinner.
```

```text
Tạo giúp tôi trang Dynamic Route /category/[slug]/page.tsx trong Next.js App Router.
- Sử dụng params để lấy tên danh mục (music, technology, sports).
- Sử dụng searchParams để lấy thông tin phân trang page và sắp xếp sort.
- Render dữ liệu mock tương ứng với danh mục đó.
- Đảm bảo viết chuẩn TypeScript Interface cho PageProps trong Next.js.
```

> 🔎 **Kiểm duyệt:** với Next.js 15, `PageProps` phải khai báo `params: Promise<{ slug: string }>` và `searchParams: Promise<...>`. Nếu AI trả về `params.slug` trực tiếp, hãy sửa lại.

#### Buổi 05 – Ant Design

```text
Hãy hướng dẫn tôi tạo một Component BookingModal.tsx sử dụng Ant Design v5 trong dự án Next.js App Router (TypeScript).

Yêu cầu:
1. Sử dụng các component từ antd: Modal, Form, InputNumber, Select, DatePicker, Button.
2. Tùy biến Theme thông qua ConfigProvider với màu primary là #6366F1.
3. Form gồm các trường: Loại vé (VIP, Standard), Số lượng (1-10), Ngày tham dự, Ghi chú.
4. Đảm bảo xử lý không bị lỗi Hydration mismatch trong Next.js.
```

```text
Hãy viết mã nguồn trang /admin/orders/page.tsx sử dụng Table component của Ant Design v5 với TypeScript.
- Khai báo Interface OrderType.
- Render dữ liệu mock 10 đơn hàng.
- Cột "Trạng thái" dùng component Tag hiển thị màu sắc: SUCCESS (Xanh lá), PENDING (Cam), CANCELLED (Đỏ).
- Cấu hình phân trang 5 mục/trang và cột Action có nút "Xem chi tiết".
```

#### Buổi 06 – Hooks & State

```text
Hãy tạo một Client Component TicketQuantitySelector.tsx trong Next.js App Router bằng React Hooks và TypeScript.

Yêu cầu:
1. State chứa danh sách loại vé: [{ id: '1', name: 'Vé VIP', price: 1000000, quantity: 0, max: 5 }].
2. Viết các hàm handleIncrease(id) và handleDecrease(id).
3. Sử dụng useMemo để tính toán totalAmount và totalTickets.
4. Giao diện hiển thị rõ ràng, kèm nút "Thanh toán" bị disable nếu totalTickets === 0.
```

```text
Tạo giúp tôi Component EventFilterBar.tsx tích hợp Debounce cho ô Input tìm kiếm trong React/Next.js.
- Quản lý các State: searchKeyword, priceRange, selectedDate.
- Sử dụng Custom Hook useDebounce hoặc lodash.debounce cho ô nhập từ khóa.
- Trả kết quả lọc về cho Component cha thông qua callback onFilterChange(filters).
```

#### Buổi 07 – README, sửa lỗi Hydration

```text
Hãy đóng vai một Technical Lead. Viết cho tôi nội dung file README.md bằng Markdown cho dự án "Smart Event Hub" (Next.js, TypeScript, Ant Design, SCSS).

Yêu cầu chi tiết:
1. Tên dự án & Mô tả ngắn gọn (3-4 câu).
2. Bảng phân công công việc nhóm 4 người (Cột: Họ tên, MSSV, Vai trò, Tính năng đã đảm nhiệm).
3. Hướng dẫn chạy dự án ở local (npm install, npm run dev).
4. Cấu trúc thư mục dự án (App Router architecture).
5. Link đính kèm file thiết kế Wireframe Figma.
```

```text
Tôi gặp lỗi Hydration Error trong Next.js App Router khi sử dụng Component DatePicker / Modal của Ant Design.
Hãy giải thích nguyên nhân và đưa ra giải pháp sửa lỗi triệt để bằng cách sử dụng dynamic import với { ssr: false } hoặc Hook useEffect để chỉ render ở Client-side.
```

> 🔎 **Kiểm duyệt:** Next.js 15 không cho dùng `next/dynamic` với `{ ssr: false }` bên trong Server Component; lời gọi đó phải nằm trong file có `'use client'`. Trước khi dùng cách này, hãy kiểm tra đã bọc `AntdRegistry` trong `app/layout.tsx` chưa.

#### Buổi 08 – Swagger sang TypeScript & Service

```text
Bạn là một Fullstack Developer. Dưới đây là JSON Response từ Swagger API danh sách sự kiện:
[Dán đoạn JSON Swagger API Response vào đây]

Yêu cầu:
1. Sinh các TypeScript Interfaces tương ứng (IEventResponse, IEventItem, IOrganizer).
2. Viết 1 file services/eventService.ts sử dụng axios để thực hiện hàm getEvents(params) với các query: page, limit, search.
3. Viết code ví dụ Fetch dữ liệu trong Server Component Next.js (app/page.tsx) và truyền props vào Component EventList.
```

```text
Viết giúp tôi hàm getEventById(id: string) trong services/eventService.ts và tích hợp vào trang Next.js Server Component /app/events/[id]/page.tsx.
- Nếu không tìm thấy sự kiện (API trả về lỗi 404), gọi hàm notFound() từ next/navigation để chuyển hướng đến trang 404.
- Bổ sung Try/Catch block để bắt lỗi kết nối API.
```

> 🔎 **Kiểm duyệt:** đặc tả dự án dùng tên không tiền tố `I` (`EventItem`, `Organizer`) và bọc response trong `ApiResponse<T>`. Có thể thêm vào prompt: "Đặt tên theo `types/` hiện có của dự án". Luôn đối chiếu interface AI sinh với response thật trên Swagger UI.

#### Buổi 09 – Form & Zod

```text
Hãy tạo cho tôi Component LoginForm.tsx bằng Next.js ("use client") kết hợp React Hook Form, Zod và Ant Design Input.

Yêu cầu chi tiết:
1. Định nghĩa Zod Schema loginSchema:
   - email: Chuỗi, bắt buộc, đúng định dạng Email.
   - password: Chuỗi, bắt buộc, tối thiểu 6 ký tự.
2. Tích hợp useForm với zodResolver(loginSchema).
3. Khi submit hợp lệ, gọi hàm onLogin(values) giả lập, lưu token vào localStorage.setItem('accessToken', 'mock-token-123') và hiển thị Antd message.success("Đăng nhập thành công").
4. Hiển thị error message màu đỏ dưới ô input nếu dữ liệu không hợp lệ.
```

```text
Hãy viết một Zod Schema tên là createEventSchema cho Form Tạo sự kiện có ràng buộc nâng cao:
- title: string, min 5 chars.
- startDate: date string.
- endDate: date string.
- Sử dụng hàm .refine() của Zod để kiểm tra endDate phải có thời gian lớn hơn startDate. Cho tôi mã nguồn Zod Schema và cách dùng với React Hook Form.
```

#### Buổi 10 – Responsive & Refactor

```text
Tôi có Component EventFilterBar.tsx đang bị tràn khung khi co màn hình xuống kích thước Mobile (375px).
Hãy hướng dẫn tôi refactor Component này sử dụng Ant Design Drawer hoặc Responsive Grid (xs={24}, md={8}) để hiển thị dạng nút "Bộ lọc" mở ra Drawer trên Mobile, còn trên Desktop thì giữ nguyên Filter Bar nằm ngang.
Viết bằng Next.js TypeScript và Ant Design v5.
```

```text
Hãy đóng vai một Tech Lead chuyên về Clean Code. Hãy rà soát đoạn mã Next.js Component sau và refactor lại giúp tôi:
[Dán đoạn code lặp lại hoặc chưa tối ưu vào đây]

Yêu cầu refactor:
1. Phân rã các khối UI lặp lại thành sub-component nhỏ.
2. Loại bỏ các khai báo any, thay bằng Interface có cấu trúc chặt chẽ.
3. Tối ưu hóa re-render bằng cách dùng React.memo hoặc useCallback nếu cần thiết.
4. Giải thích ngắn gọn các cải tiến đã thực hiện.
```

#### Buổi 11 – SEO & Deploy

```text
Hướng dẫn tôi cách viết hàm generateMetadata trong Next.js App Router cho trang Dynamic Route /events/[id]/page.tsx.
Yêu cầu:
1. Gọi API getEventById(id) lấy thông tin sự kiện.
2. Trả về object Metadata gồm: title, description, openGraph (title, description, images chứa URL ảnh sự kiện).
3. Xử lý trường hợp không tìm thấy sự kiện thì trả về fallback metadata tiêu chuẩn.
```

```text
Tôi gặp lỗi Build Error trên Vercel khi Deploy dự án Next.js TypeScript:
[Dán đoạn log lỗi Vercel Build Error vào đây]

Hãy phân tích nguyên nhân lỗi và hướng dẫn từng bước cách sửa lỗi trên tệp mã nguồn hoặc cấu hình Vercel Settings.
```

> 🔒 **An toàn khi dán log/code cho AI:** xóa token, mật khẩu, khóa API thật trước khi dán. Không dán file `.env` vào bất kỳ công cụ AI nào.

---

## 5. GỢI Ý VIDEO TỰ HỌC (theo chủ đề và từ khóa tìm kiếm)

#### Cách tìm và chọn video

Học phần không chỉ định kênh cụ thể. Các bạn tìm trên YouTube hoặc nền tảng học trực tuyến theo từ khóa bên dưới. Ưu tiên video đăng trong khoảng 12 tháng gần đây, ghi rõ phiên bản (Next.js 15, Ant Design v5, React 19), và có repo mã nguồn đi kèm. Nếu giảng viên đã đăng video/slide riêng trên LMS thì xem video đó trước.

| Buổi | Chủ đề cần xem trước giờ học | Từ khóa tìm kiếm gợi ý |
|---|---|---|
| 01 | SCSS Flexbox/Grid Mixin; TypeScript Interface vs Type; cài VS Code, Node.js, Cursor/Copilot | `SCSS mixin responsive breakpoints`, `TypeScript interface vs type`, `Cursor AI setup tutorial` |
| 02 | Nguyên tắc UX Wireframing; cấu trúc UI Layout (Header, Content, Sidebar, Footer) | `UX wireframing principles`, `Figma wireframe tutorial`, `v0.dev image to React` |
| 03 | Next.js App Router: `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx` | `Next.js 15 App Router tutorial`, `Next.js route groups layout`, `server vs client components` |
| 04 | Dynamic Routes params; Component Props & Reusability | `Next.js 15 dynamic routes params promise`, `reusable React components TypeScript` |
| 05 | Tích hợp Ant Design/Bootstrap vào Next.js; Custom Theme `ConfigProvider` | `Ant Design v5 Next.js App Router`, `antd ConfigProvider theme token` |
| 06 | State lifecycle, `useState`, `useEffect`, `useCallback`, `'use client'` | `React hooks useMemo useCallback`, `useEffect infinite loop fix`, `React debounce hook` |
| 07 | Production build, README chuẩn, Conventional Commits | `Next.js npm run build errors`, `conventional commits tutorial`, `GitHub pull request code review` |
| 08 | RESTful API, Fetch API, Axios, Async/Await trong TypeScript | `Next.js server component data fetching`, `axios TypeScript service`, `Swagger UI tutorial` |
| 09 | Web Storage API, Form State, Validation Schema (Zod/Yup) | `React Hook Form Zod tutorial`, `zod refine date validation`, `localStorage Next.js hydration` |
| 10 | Refactoring, code smells, responsive polish | `React refactoring code smells`, `fix horizontal overflow mobile CSS`, `antd Drawer responsive` |
| 11 | Deploy Vercel, biến môi trường, Metadata API, Lighthouse | `deploy Next.js to Vercel`, `Next.js generateMetadata open graph`, `Lighthouse performance next/image` |
| 12 | Kỹ năng thuyết trình demo sản phẩm kỹ thuật | `technical product demo presentation tips`, `hackathon pitch demo` |

> 📌 **Ghi chú:** Danh sách trên chỉ là chủ đề và từ khóa, không phải link cụ thể. Khi chia sẻ video hay lên diễn đàn, hãy ghi kèm phiên bản công nghệ trong video để các bạn khác biết có còn dùng được không.
