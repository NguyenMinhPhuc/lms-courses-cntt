# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## THẢO LUẬN DIỄN ĐÀN & HOẠT ĐỘNG NHÓM (LMS Discussion & Team Activities)

> **Phạm vi:** 12 bài (60 tiết) · **Dự án xuyên suốt:** Smart Event Hub – Hệ thống Đặt vé & Quản lý Sự kiện trực tuyến · **Quy mô nhóm:** 3–4 sinh viên
> **Chuẩn đầu ra liên quan:** PI 1.4 (CLO1), PI 2.3 (CLO2), PI 3.1 (CLO3), PI 5.1 (CLO4)

---

Tài liệu này gom toàn bộ chủ đề diễn đàn và hoạt động nhóm (Team Challenge 60 phút) của học phần vào một chỗ. Phần A là luật chơi chung: cách thảo luận, cách lập nhóm, phân vai và quy trình Git. Phần B đi theo từng bài, mỗi bài gồm một chủ đề diễn đàn và một hoạt động nhóm bám đúng kế hoạch buổi học.

> 💡 **Mẹo:** Đọc phần A một lần ở tuần đầu. Từ Bài 02 trở đi, các bạn chỉ cần mở đúng mục của bài đang học.

---

## PHẦN A. QUY TẮC CHUNG

### A.1. Quy tắc thảo luận trên diễn đàn LMS

#### Cách tham gia

Mỗi bài có **một chủ đề thảo luận** mở trên diễn đàn LMS (`https://learn.lhu.edu.vn`), đặt trong chế độ nhóm lớp riêng biệt (Separate groups), nên các bạn chỉ thấy bài đăng của lớp mình. Diễn đàn mở sau buổi học và đóng **trước buổi học tiếp theo**.

* **Bài đăng chính:** trả lời câu hỏi mở của bài, khoảng 150–300 từ.
* **Phản hồi:** bình luận có nội dung cho **ít nhất 2 bài** của bạn khác (đặt câu hỏi ngược, chỉ ra điểm chưa ổn, bổ sung ví dụ).
* **Minh chứng:** khi nói về code, dán đoạn code ngắn trong khung code, ảnh chụp màn hình hoặc link commit/PR trên GitHub.

#### Tiêu chí chung của một bài đăng tốt

| Tiêu chí | Bài đăng tốt | Bài đăng chưa đạt |
|---|---|---|
| Bám dự án | Lấy ví dụ từ Smart Event Hub của nhóm mình | Trả lời chung chung, chép định nghĩa |
| Có minh chứng | Code trước/sau, ảnh UI, log lỗi, link PR | Chỉ nêu ý kiến, không có bằng chứng |
| Lập luận | Nêu lý do, so sánh ít nhất 2 phương án | "Mình thấy cách này hay" |
| Trung thực với AI | Ghi rõ đoạn nào AI sinh, đoạn nào mình sửa và vì sao | Dán nguyên câu trả lời của AI |
| Phản hồi | Phản biện lịch sự, có gợi ý cụ thể | "Hay quá", "Đồng ý" |

> ⚠️ **Lưu ý:** Không dán nguyên văn câu trả lời của ChatGPT/Claude làm bài đăng. Diễn đàn dùng để các bạn tự lập luận; AI chỉ là nguồn tham khảo cần được kiểm chứng.

---

### A.2. Tổ chức nhóm 3–4 sinh viên

#### Lập nhóm và giữ nhóm

* Nhóm lập ngay **Buổi 1**, giữ nguyên đến **Buổi 12**. Danh sách nhóm được GV nhập vào LMS thành Grouping theo lớp.
* Đặt tên nhóm theo mẫu `Nhom01`, `Nhom02`… để khớp quy tắc đặt tên file `[MãLớp]_[Nhóm/MSSV]_[TênBài]`.
* Mỗi nhóm có **một Repository GitHub chung** (do Team Lead tạo, mời các thành viên và GV làm collaborator) và **một kênh liên lạc** riêng (Zalo/Discord/Teams).
* Họp nhanh 10 phút đầu mỗi Team Challenge: mỗi người nói "hôm qua làm gì – hôm nay làm gì – đang vướng gì".

Tại sao phải giữ nhóm suốt học phần? Dự án Smart Event Hub được xây dần qua 11 buổi, và Git log của nhóm là minh chứng chấm điểm giữa kỳ, cuối kỳ cũng như điểm phản biện cá nhân, nên đổi nhóm giữa chừng sẽ làm đứt lịch sử đóng góp của chính các bạn.

---

### A.3. Vai trò trong nhóm

#### Bốn vai trò gợi ý

| Vai trò | Trách nhiệm chính | Ví dụ việc cụ thể trong Smart Event Hub |
|---|---|---|
| **Team Lead** | Chia việc, quản lý board công việc, merge `dev` → `main`, giữ tiến độ | Tạo repo, bảo vệ branch `main`, viết README, điều phối báo cáo giữa kỳ/cuối kỳ |
| **UI Developer** | Wireframe, Design Token SCSS, layout, AntD Theme, responsive | `styles/_variables.scss`, Header/Footer, EventCard, tùy biến `ConfigProvider` |
| **Logic/API Developer** | TypeScript types, state, hooks, services gọi API, form | `types/`, `services/eventService.ts`, TicketQuantitySelector, LoginForm + Zod |
| **QA/DevOps** | Review PR, kiểm thử responsive, `npm run lint`/`build`, deploy Vercel, Lighthouse | Checklist review, Test Case Scenario, cấu hình `NEXT_PUBLIC_API_URL` trên Vercel |

#### Nguyên tắc phân vai

* **Nhóm 3 người:** gộp Team Lead với QA/DevOps.
* **Vai trò không có nghĩa là "chỉ làm phần đó".** Mọi thành viên đều phải có commit code tính năng thật, vì GV sẽ hỏi phản biện cá nhân trên chính đoạn code mình đảm nhiệm.
* **Luân phiên:** khuyến khích đổi vai sau Buổi 7 để ai cũng chạm vào UI, logic và deploy.
* Ghi bảng phân vai vào `README.md` (mục "Thành viên & Phân công") và cập nhật khi đổi vai.

---

### A.4. Git Branch Strategy (main / dev / feature/*)

#### Ba loại nhánh

| Nhánh | Mục đích | Ai được push/merge |
|---|---|---|
| `main` | Bản ổn định, luôn build được; Vercel tự deploy Production từ nhánh này | Chỉ Team Lead merge từ `dev` qua PR |
| `dev` | Nhánh tích hợp hằng ngày; đích của mọi PR tính năng và BTVN | Merge qua PR đã được review |
| `feature/<tên>-<tính-năng>` | Mỗi tính năng/bài tập một nhánh, tách từ `dev` | Chủ nhánh push tự do |

Quy ước tên nhánh: chữ thường, gạch nối, không dấu. Ví dụ `feature/an-event-card`, `feature/binh-seat-picker`, `feature/chi-login-form`. Nhánh sửa lỗi gấp trên bản đã deploy có thể đặt `fix/<mô-tả>`.

#### Các lệnh thường dùng

```bash
# Bắt đầu một tính năng mới
git checkout dev
git pull origin dev
git checkout -b feature/an-event-card

# Commit theo Conventional Commits
git add .
git commit -m "feat(event): add EventCard component with responsive SCSS"

# Cập nhật nhánh trước khi mở PR (tránh conflict)
git fetch origin
git rebase origin/dev        # hoặc: git merge origin/dev
git push -u origin feature/an-event-card
```

> 🔒 **Thiết lập một lần (Team Lead):** vào *Settings → Branches* trên GitHub, thêm rule cho `main` (và nên cả `dev`): bắt buộc Pull Request, tối thiểu 1 approval, không cho force-push.

---

### A.5. Quy trình Pull Request & Code Review

#### Sáu bước của một PR

1. **Tự kiểm tra trước khi mở PR:** chạy `npm run lint` và `npm run build` không lỗi; xóa `console.log`; không còn `any`.
2. **Mở PR vào `dev`** với tiêu đề theo Conventional Commits, ví dụ `feat(checkout): add TicketQuantitySelector`.
3. **Điền mô tả theo mẫu** (bên dưới), kèm ảnh chụp UI ở Mobile 375px và Desktop 1440px nếu có thay đổi giao diện.
4. **Gán reviewer:** ít nhất 1 thành viên khác (ưu tiên QA/DevOps).
5. **Review và sửa:** reviewer để comment theo checklist; tác giả sửa bằng commit mới, trả lời từng comment.
6. **Merge:** khi có approval và không conflict; xóa nhánh feature sau khi merge.

```markdown
## Mô tả
- Tính năng/bài tập: (ví dụ: BTVN Bài 01 – Footer, EventCategoryBadge, SearchBar)
- Liên quan: (link issue/task nếu có)

## Thay đổi chính
- ...

## Phần có dùng AI (Vibe Coding)
- Công cụ: Cursor / Copilot / v0.dev / Claude / ChatGPT
- Prompt chính: (dán tóm tắt)
- Những gì mình đã sửa lại so với code AI sinh: ...

## Cách kiểm tra
- [ ] npm run lint không lỗi
- [ ] npm run build thành công
- [ ] Đã xem ở 375px / 768px / 1440px

## Ảnh chụp màn hình
(Mobile & Desktop)
```

#### Checklist cho người review

* **TypeScript:** không có `any`; Props có interface rõ ràng; union type dùng `|` đúng chỗ.
* **Cấu trúc:** component đặt đúng thư mục (`components/ui`, `components/common`, `components/features`); không trùng lặp code đã có.
* **Next.js:** chỉ thêm `'use client'` khi thật sự cần hook/sự kiện; dùng `next/link`, `next/image`.
* **Style:** dùng biến và mixin chung trong `styles/`; không inline-style rác, không magic number.
* **Responsive:** không tràn ngang ở 375px.
* **Commit:** thông điệp đúng chuẩn, mỗi commit một ý.

> 💬 **Văn hóa review:** góp ý vào code, không nhắm vào người. Viết "Chỗ này nên tách thành `PriceTag` để tái sử dụng ở trang Checkout" thay vì "Code này dở".

---

## PHẦN B. THẢO LUẬN & HOẠT ĐỘNG NHÓM THEO TỪNG BÀI

### Bài 01: SCSS nâng cao, TypeScript căn bản & thiết lập Vibe Coding

#### 💬 Chủ đề diễn đàn: "Interface hay Type – và lần đầu AI viết sai TypeScript"

**Câu hỏi mở:** Khi khai báo kiểu cho `EventItem`, `EventStatus` và `EventCardProps`, các bạn chọn `interface` hay `type` cho từng cái, vì sao? Hãy kể lại một lần AI (Cursor/Copilot/ChatGPT) gợi ý code TypeScript hoặc SCSS chưa đúng trong buổi học và cách các bạn phát hiện ra.

**Gợi ý trả lời:**
* `interface` hợp với data model và Props vì mở rộng được bằng `extends`; `type` hợp với union như `type EventStatus = 'UPCOMING' | 'ONGOING' | 'ENDED'`.
* Lỗi AI hay gặp: khai báo `status: string` thay vì union, dùng `any` cho props, quên `alt`/`width`/`height` của `next/image`, mixin breakpoint không khớp mốc 640/768/1024px.
* Nêu cách phát hiện: lỗi gạch đỏ của VS Code, `tsc` báo lỗi, hoặc giao diện vỡ khi co màn hình.

**Tiêu chí bài đăng tốt:** có đoạn code trước khi sửa và sau khi sửa; giải thích được lỗi bằng lời của mình; nêu prompt đã dùng và cách cải thiện prompt (thêm phần Constraints).

#### 👥 Hoạt động nhóm (Team Challenge 60'): Khởi tạo Repo & Design Token System

**Mục tiêu:** Nhóm có một repository chung chạy được, thống nhất bộ biến SCSS dùng cho toàn dự án và trải qua quy trình PR đầu tiên.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Tạo repo, tạo nhánh `main`, `dev`; mời thành viên và GV; thêm rule bảo vệ `main` |
| UI Developer | Viết `styles/_variables.scss`: Color Palette, Typography, Spacing, Shadows |
| Logic/API | Viết `styles/_mixins.scss`: `respond-to`, flex alignment, text truncate; khai báo `types/event.ts` |
| QA/DevOps | Review chéo 2 PR, kiểm tra các thành viên import được biến SCSS, xử lý conflict nếu có |

**Output:**
* 1 repository Git với cấu trúc thư mục chuẩn và hai nhánh `main`, `dev`.
* File biến SCSS tập trung được các thành viên import và dùng thành công.
* Minh chứng ít nhất 1 PR được merge trên GitHub (link PR nộp lên LMS).

---

### Bài 02: Tư duy Wireframe/Modeling UI & chuyển Figma thành Next.js Component

#### 💬 Chủ đề diễn đàn: "Từ ảnh Wireframe đến code: AI làm được bao nhiêu phần trăm?"

**Câu hỏi mở:** Sau khi đưa ảnh Wireframe vào v0.dev/Claude để sinh TSX, các bạn phải sửa những gì nhiều nhất? Theo Atomic Design, trong Smart Event Hub thì `SearchBar`, `EventCard`, `Header` thuộc cấp nào (atom, molecule, organism), và có trường hợp nào khó xếp loại không?

**Gợi ý trả lời:**
* Phần thường phải sửa: inline-style, magic number (`padding: 13px`), thẻ `div` lồng nhau thay cho `header`/`main`/`section`, component quá dài chưa tách.
* `SearchBar` = Input + Button → molecule; `Header` = Logo + Nav + SearchBar → organism. `EventCard` có thể là molecule hoặc organism tùy độ phức tạp – hãy nêu lập luận của nhóm.
* Có thể ước lượng mức giống bản phác thảo (mục tiêu >85%) và chỉ ra chỗ lệch.

**Tiêu chí bài đăng tốt:** có ảnh wireframe đặt cạnh ảnh giao diện thật; liệt kê ít nhất 3 chỉnh sửa cụ thể sau khi AI sinh code; phân loại Atomic có lý do.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Wireframe 5 màn hình chính

**Mục tiêu:** Thống nhất bộ Wireframe 5 màn hình làm cơ sở cho toàn bộ dự án và cho tiêu chí PI 1.4 ở giữa kỳ, cuối kỳ.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Chủ trì họp, chốt danh sách màn hình và luồng điều hướng giữa chúng |
| UI Developer | Vẽ Trang chủ (kèm danh sách & lọc sự kiện) và Chi tiết sự kiện trên Figma |
| Logic/API | Vẽ Đặt vé (Checkout & Booking) và Trang cá nhân (lịch sử vé) |
| QA/DevOps | Vẽ Admin Dashboard; xuất ảnh, đặt tên file thống nhất và commit vào `docs/wireframes/` |

> 📝 **Ghi chú:** Kế hoạch buổi học tách "Danh sách & Lọc sự kiện" thành một màn hình riêng, còn đề cương xếp Admin Dashboard vào 5 màn hình chính. Bộ học liệu này theo đề cương (Trang chủ, Chi tiết sự kiện, Đặt vé, Trang cá nhân, Admin Dashboard); phần danh sách & lọc nằm trong Trang chủ. Nhóm nào vẽ thêm màn hình Listing riêng thì càng tốt.

**Output:**
* Bộ Wireframe 5 màn hình đủ thành phần UI (Header, Content, Sidebar, Footer).
* File Figma (link) hoặc ảnh chụp rõ nét trong `docs/wireframes/` trên repo.

---

### Bài 03: Next.js App Router – cấu trúc thư mục, Index & Nested Routing

#### 💬 Chủ đề diễn đàn: "Server Component mặc định – vậy cái gì phải là Client?"

**Câu hỏi mở:** Trong App Router, mọi component trong `app/` mặc định là Server Component. Hãy liệt kê các component của Smart Event Hub mà nhóm bạn **bắt buộc** phải đánh dấu `'use client'` và giải thích lý do. Route Group `(auth)` và `(admin)` giúp ích gì cho bố cục dự án?

**Gợi ý trả lời:**
* Cần `'use client'` khi dùng `useState`/`useEffect`, sự kiện `onClick`/`onChange`, hoặc Browser API: ô tìm kiếm, Sidebar admin có trạng thái thu gọn, nút đăng nhập mở menu.
* Không cần: trang danh sách chỉ hiển thị dữ liệu, Footer tĩnh.
* Route Group cho phép `(auth)` dùng AuthLayout không có Header/Footer, `(admin)` dùng AdminLayout có Sidebar, mà URL vẫn là `/login`, `/admin/dashboard`.

**Tiêu chí bài đăng tốt:** có sơ đồ cây thư mục `app/` thật của nhóm; chỉ ra ít nhất một chỗ đã thêm `'use client'` thừa và gỡ bỏ được.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Tích hợp hệ thống Navigation Route

**Mục tiêu:** Ghép route của từng cá nhân thành một sơ đồ routing thống nhất, điều hướng không reload trang, có trang 404 riêng.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Gom các nhánh route vào `dev`, giải quyết conflict ở `app/layout.tsx`, sau đó merge `dev` → `main` |
| UI Developer | Thiết kế `not-found.tsx` thân thiện, có nút "Quay lại trang chủ" |
| Logic/API | Cập nhật `HeaderNavigationBar` dùng `next/link` tới mọi route; khai báo mảng `NavItem[]` có kiểu |
| QA/DevOps | Bấm thử toàn bộ link, gõ URL sai (ví dụ `/abc-xyz`) để kiểm tra trang 404, ghi lỗi vào issue |

**Output:**
* Mã nguồn chung chứa toàn bộ sơ đồ routing của web app.
* Nhập đường dẫn sai hiển thị đúng trang 404 tùy chỉnh.

---

### Bài 04: Dynamic Routing & kiến trúc Reusable Components

#### 💬 Chủ đề diễn đàn: "Reusable đến mức nào thì vừa?"

**Câu hỏi mở:** Component `Button` của nhóm bạn có bao nhiêu props? Khi nào một component "tái sử dụng" trở thành quá phức tạp (over-engineering)? Ngoài ra, hãy giải thích vì sao trong Next.js 15 phải viết `const { id } = await params;` thay vì `params.id`.

**Gợi ý trả lời:**
* Dấu hiệu quá tay: props boolean chồng chéo (`isPrimary`, `isOutline` cùng lúc), quá nhiều nhánh `if` trong JSX. Gom lại bằng `variant` và `size` dạng union.
* Mở rộng `ButtonHTMLAttributes<HTMLButtonElement>` để nhận sẵn `onClick`, `type`, `disabled` mà không khai báo lại.
* Next.js 15 truyền `params` và `searchParams` dưới dạng `Promise`, nên Server Component phải `await` trước khi dùng.

**Tiêu chí bài đăng tốt:** dán interface Props thật của nhóm; chỉ ra một chỗ code bị lặp đã được thay bằng component dùng chung.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Mock Data & luồng điều hướng hoàn chỉnh

**Mục tiêu:** Có bộ dữ liệu giả lập chung và luồng người dùng liền mạch Trang chủ → Danh mục → Chi tiết sự kiện → Đặt vé.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Thống nhất schema dữ liệu (dựa trên `types/event.ts`), chia việc theo từng bước của luồng |
| UI Developer | Card ở Trang chủ chuyển tới `/events/[id]`; Badge thể loại chuyển tới `/category/[slug]` |
| Logic/API | Viết `data/mock-events.json` và hàm đọc dữ liệu theo `id`, theo `slug` có kiểu rõ ràng |
| QA/DevOps | Nút "Mua vé" chuyển tới `/checkout/[id]`; kiểm tra dữ liệu khớp giữa các màn hình |

**Output:** User Flow liên tục, dữ liệu khớp giữa các màn hình; file `data/mock-events.json` trên `dev`.

---

### Bài 05: Giao diện chuyên nghiệp với Ant Design, Bootstrap/Tailwind & tùy biến Theme

#### 💬 Chủ đề diễn đàn: "Làm sao để Smart Event Hub không trông giống mọi trang Ant Design khác?"

**Câu hỏi mở:** Nhóm bạn chọn Ant Design, Bootstrap hay Tailwind cho dự án, và đánh đổi là gì? Các bạn đã tùy biến những gì (Design Token trong `ConfigProvider`, override bằng SCSS Module…) để giao diện có bản sắc riêng?

**Gợi ý trả lời:**
* AntD mạnh ở component dữ liệu (Table, Form, Modal, DatePicker); Bootstrap/Tailwind gọn và linh hoạt về layout nhưng phải tự dựng nhiều thành phần.
* Tùy biến tập trung qua `theme={{ token: { colorPrimary: '#6366F1', borderRadius: 8 } }}`, sau đó override cục bộ bằng SCSS Module để không ảnh hưởng component khác.
* Nhắc tới `@ant-design/nextjs-registry` để tránh FOUC/Hydration mismatch.

**Tiêu chí bài đăng tốt:** có ảnh "trước – sau khi tùy biến"; nêu ít nhất 2 token đã đổi và 1 chỗ override SCSS.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Refactor 5 màn hình sang Ant Design + SCSS Custom

**Mục tiêu:** Thay HTML thô bằng component AntD phù hợp và tùy biến để giao diện đồng bộ, có bản sắc.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Lập danh sách phần tử cần thay ở 5 màn hình, chia mỗi người 1–2 màn hình |
| UI Developer | Trang chủ: `Carousel` cho Banner, `Tabs` cho danh mục |
| Logic/API | Chi tiết sự kiện & Đặt vé: `Rate` cho đánh giá, `Skeleton` cho trạng thái chờ |
| QA/DevOps | Admin Dashboard & Trang cá nhân; kiểm tra Tablet & Mobile, ghi lỗi vỡ khung |

**Output:** Giao diện toàn web app đồng bộ, không mang cảm giác "nguyên bản" của Ant Design; PR merge vào `dev`.

---

### Bài 06: Logic & State Management với React Hooks

#### 💬 Chủ đề diễn đàn: "useEffect nào trong code của bạn là thừa?"

**Câu hỏi mở:** Sau khi đọc bài "You Might Not Need an Effect", hãy tìm trong code của nhóm một `useEffect` có thể bỏ đi (ví dụ dùng để tính tổng tiền). Các bạn đã từng gặp vòng lặp re-render vô hạn chưa, AI giúp tìm ra nguyên nhân như thế nào?

**Gợi ý trả lời:**
* Tổng tiền, số vé là dữ liệu suy ra từ state → tính trực tiếp hoặc dùng `useMemo`, không cần `useEffect` + `setState`.
* Re-render vô hạn thường do `setState` trong `useEffect` không có hoặc sai dependency array, hoặc dependency là object/hàm tạo mới mỗi lần render.
* Phân biệt `useMemo` (ghi nhớ giá trị) và `useCallback` (ghi nhớ tham chiếu hàm).

**Tiêu chí bài đăng tốt:** có đoạn code trước/sau; nêu prompt debug đã gửi cho AI và đánh giá câu trả lời đúng hay sai ở điểm nào.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Sơ đồ chọn ghế ngồi trực quan (SeatMatrixPicker)

**Mục tiêu:** Xây dựng tính năng tương tác phức tạp với state chia sẻ giữa sơ đồ ghế và khung tổng tiền.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Thiết kế state (lift state lên component cha), định nghĩa kiểu `SeatStatus` |
| UI Developer | Dựng lưới 5 hàng × 8 cột, màu cho 3 trạng thái: trống, đang chọn, đã bán |
| Logic/API | Xử lý click chọn/hủy, cập nhật mảng ghế đã chọn (`['A1', 'A2']`), tính thành tiền, giới hạn tối đa 6 ghế |
| QA/DevOps | Kiểm thử ca biên: bấm ghế đã bán, chọn ghế thứ 7, bỏ chọn rồi chọn lại |

**Output:** Sơ đồ ghế đổi màu tức thì khi click; chặn chọn quá 6 ghế/lần; hiển thị đúng thành tiền.

---

### Bài 07: Kiểm tra giữa kỳ – Báo cáo tiến độ 50% dự án

#### 💬 Chủ đề diễn đàn: "Retrospective giữa kỳ: chạy được ở dev, vỡ ở build"

**Câu hỏi mở:** Lần chạy `npm run build` đầu tiên của nhóm bạn báo những lỗi gì mà `npm run dev` không hề hiện ra? Nhìn vào Git log, các bạn thấy việc phân công và đóng góp trong nhóm đã đều chưa, nửa sau học phần sẽ thay đổi gì?

**Gợi ý trả lời:**
* `build` bật type-check và ESLint toàn bộ dự án: lỗi kiểu ở file chưa mở, biến không dùng, promise chưa xử lý, import sai hoa/thường.
* Minh chứng đóng góp: commit theo Conventional Commits, PR có review, bảng phân công trong README.
* Đề xuất cải tiến cụ thể: chia nhỏ task, review PR trong 24 giờ, chạy build trước khi merge.

**Tiêu chí bài đăng tốt:** có ảnh log lỗi build và cách đã sửa; có ít nhất 1 cam kết cải tiến đo được cho nhóm.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Thực hành báo cáo giữa kỳ

**Mục tiêu:** Trình bày 50% tiến độ dự án trong 10 phút và trả lời phản biện cá nhân trong 5 phút.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Mở đầu, giới thiệu dự án và bảng phân công; điều phối thời gian |
| UI Developer | Trình diễn Wireframe 5 màn hình và giao diện responsive (AntD + SCSS Custom) |
| Logic/API | Demo luồng routing mượt mà, các tính năng state đã làm (chọn vé, lọc, chọn ghế) |
| QA/DevOps | Chiếu Git commit log từng cá nhân, kết quả `npm run build` thành công |

**Output:** Điểm giữa kỳ ghi nhận theo rubric (Wireframe 1.5đ, UI 2.0đ, Routing 1.0đ, Git 0.5đ). Mỗi thành viên sẵn sàng giải thích code của mình.

---

### Bài 08: Data Fetching & tích hợp RESTful API

#### 💬 Chủ đề diễn đàn: "Fetch trên Server hay gọi Axios trên Client?"

**Câu hỏi mở:** Với từng màn hình của Smart Event Hub (Trang chủ, Chi tiết sự kiện, Bộ lọc danh mục, Đặt vé), nhóm bạn lấy dữ liệu ở Server Component hay Client Component, vì sao? Khi thả Swagger JSON vào AI để sinh interface, các bạn có phát hiện chỗ nào lệch với response thật không?

**Gợi ý trả lời:**
* Dữ liệu đọc, cần SEO (danh sách, chi tiết sự kiện) → `fetch` trong Server Component với `next: { revalidate }`.
* Dữ liệu phụ thuộc thao tác người dùng (tìm kiếm gõ phím, gửi đơn `POST /api/orders`) → Client Component với Axios.
* AI có thể đoán sai kiểu (`price` là `string` hay `number`), bỏ sót trường `null`, đặt tên khác với API. Cách kiểm: so với response thật trên Swagger UI.

**Tiêu chí bài đăng tốt:** có bảng "màn hình – nơi fetch – lý do"; dán interface AI sinh và phần đã sửa.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Thay Mock JSON bằng API thật

**Mục tiêu:** Mỗi thành viên phụ trách một mảng API; toàn bộ dữ liệu mock được thay bằng dữ liệu từ Backend.

| Vai trò | Việc cần làm |
|---|---|
| Thành viên 1 (UI) | Fetch `GET /api/categories`, render vào Filter Bar/Dropdown |
| Thành viên 2 (Logic/API) | Fetch tìm kiếm & phân trang `GET /api/events?search=...&page=...` |
| Thành viên 3 (QA/DevOps) | Tích hợp `POST /api/orders`, hiển thị Notification thành công/thất bại của AntD |
| Team Lead | Viết `services/` dùng chung (base URL từ `NEXT_PUBLIC_API_URL`), thêm `Spin`/`Skeleton` khi tải |

**Output:** Toàn bộ dữ liệu mock cũ được thay bằng dữ liệu API thật; có trạng thái Loading khi chờ API.

---

### Bài 09: Form Validation (React Hook Form + Zod), Local Storage & Complex UI State

#### 💬 Chủ đề diễn đàn: "Lưu token ở đâu cho đúng?"

**Câu hỏi mở:** Nhóm bạn lưu Auth Token ở `localStorage` hay Cookie (đặc biệt là `httpOnly`)? Hãy phân tích đánh đổi về bảo mật và độ tiện. Vì sao đọc `localStorage` trong Next.js dễ gặp lỗi `window is not defined` hoặc Hydration mismatch, và nhóm đã xử lý ra sao?

**Gợi ý trả lời:**
* `localStorage` tiện, hợp với dữ liệu UI không nhạy cảm (Wishlist, theme) nhưng JavaScript nào cũng đọc được. Cookie `httpOnly` do server đặt, trình duyệt tự gửi kèm request, script không đọc được.
* Server không có `window`; phải đọc `localStorage` trong `useEffect` hoặc qua custom hook như `useLocalStorage`.
* Có thể nói thêm về `z.infer<typeof schema>` giúp form và type luôn khớp.

**Tiêu chí bài đăng tốt:** nêu lựa chọn và lý do gắn với Smart Event Hub; có đoạn code đọc storage an toàn.

#### 👥 Hoạt động nhóm (Team Challenge 60'): Tính năng Wishlist bằng LocalStorage

**Mục tiêu:** Người dùng thả tim sự kiện ở bất kỳ Card nào, danh sách được giữ lại sau khi tải lại trang.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Thiết kế cách chia sẻ state (custom hook hoặc Context) để mọi Card đồng bộ |
| UI Developer | Icon trái tim trên `EventCard`, trạng thái bật/tắt rõ ràng |
| Logic/API | Hook đọc/ghi mảng ID vào `localStorage` an toàn với SSR |
| QA/DevOps | Trang `/user/wishlist`; kiểm thử F5, nhiều Card cùng một sự kiện trên một trang |

**Output:** Refresh/F5 vẫn giữ đúng trạng thái Wishlist; trang `/user/wishlist` hiển thị đúng danh sách.

---

### Bài 10: PBL 1 – Refactoring, Optimization & Responsive Polish

#### 💬 Chủ đề diễn đàn: "Code smell nào AI hay để lại nhất?"

**Câu hỏi mở:** Khi rà lại toàn bộ codebase, loại code smell nào xuất hiện nhiều nhất trong phần code do AI sinh (component quá 300 dòng, lặp code, `any`, biến không dùng…)? Hãy chia sẻ một lần refactor mà nhóm đo được kết quả (số dòng giảm, số warning còn lại).

**Gợi ý trả lời:**
* Đối chiếu với danh mục của Refactoring Guru: Long Method, Duplicate Code, Large Class.
* Đo bằng số dòng trước/sau, số cảnh báo ESLint/TypeScript, hoặc ảnh màn hình 375px trước/sau khi sửa tràn ngang.
* Nêu rõ prompt refactor đã dùng và chỗ AI đề xuất sai (đổi logic, xóa nhầm xử lý).

**Tiêu chí bài đăng tốt:** có số liệu trước/sau; chỉ ra ít nhất một đề xuất của AI mà nhóm **không** chấp nhận và lý do.

#### 👥 Hoạt động nhóm (PBL 180'): Responsive Polish – Refactoring – Zero Warning

**Mục tiêu:** Đưa codebase về trạng thái sạch: responsive ở 375/768/1440px, rút gọn code lặp, không còn warning trên Console.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Lập danh sách bug, theo dõi tiến độ 3 phần; chuẩn bị nghiệm thu với GV |
| UI Developer | Phần 1: sửa tràn ngang; chuyển Menu/Filter sang `Drawer`/`Collapse` trên di động |
| Logic/API | Phần 2: tách component lặp, xóa `any`, biến không dùng, `console.log`; gom SCSS lặp thành mixin |
| QA/DevOps | Phần 3: chạy dev kiểm tra Hot Reload, sửa warning (Hydration failed, React does not recognize prop…) |

**Output:** Codebase rút gọn >20% số dòng mà không đổi logic; TypeScript strict pass; Zero Console Warnings; biên bản nghiệm thu PBL 1.

---

### Bài 11: PBL 2 – CI/CD, Deploy Vercel, SEO & Performance

#### 💬 Chủ đề diễn đàn: "Lighthouse chưa tới 85 – thủ phạm là ai?"

**Câu hỏi mở:** Lần audit Lighthouse đầu tiên trên link Vercel của nhóm bạn được bao nhiêu điểm Performance và SEO? Ba nguyên nhân lớn nhất là gì và nhóm đã cải thiện thế nào? Ngoài ra, biến có tiền tố `NEXT_PUBLIC_` sẽ lộ ra phía trình duyệt – vậy nên đặt gì vào đó và không nên đặt gì?

**Gợi ý trả lời:**
* Nguyên nhân thường gặp: ảnh lớn dùng `<img>` thô, font gây layout shift (CLS), component nặng tải ngay từ đầu.
* Giải pháp: `next/image` với `sizes`/`priority`, `next/font`, `next/dynamic`, Metadata API và `generateMetadata`.
* `NEXT_PUBLIC_API_URL` là địa chỉ công khai nên đặt được; khóa bí mật thì không bao giờ gắn tiền tố này.

**Tiêu chí bài đăng tốt:** có ảnh Lighthouse trước/sau; nêu từng thay đổi gắn với chỉ số nào tăng.

#### 👥 Hoạt động nhóm (PBL 180'): SEO động – Deploy Vercel – Lighthouse > 85

**Mục tiêu:** Đưa Smart Event Hub lên Internet với SEO đúng chuẩn và hiệu năng đạt yêu cầu.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Merge `dev` → `main`, chốt bản deploy, tổng hợp link Live nộp LMS |
| UI Developer | Thay toàn bộ `<img>` bằng `next/image`, tối ưu font bằng `next/font` |
| Logic/API | Metadata tĩnh ở Root Layout; `generateMetadata` cho `/events/[id]` (OpenGraph theo sự kiện) |
| QA/DevOps | Kết nối repo với Vercel, khai báo `NEXT_PUBLIC_API_URL`, xử lý Build Fail, chạy Lighthouse |

**Output:** Link `*.vercel.app` hoạt động; chia sẻ link lên Zalo/Facebook hiện đúng ảnh và tiêu đề; Lighthouse Performance > 85, SEO > 90.

---

### Bài 12: Thi Hackathon & Final Showcase

#### 💬 Chủ đề diễn đàn: "Nhìn lại 12 buổi: Vibe Coding đã thay đổi cách bạn làm Front-End ra sao?"

**Câu hỏi mở:** Sau học phần, các bạn vạch ranh giới giữa "dùng AI để tăng tốc" và "để AI làm thay" ở đâu? Hãy chọn một sản phẩm của nhóm khác mà bạn đã trải nghiệm trong phần Cross-Testing và góp ý 2 điểm mạnh, 1 điểm cần cải thiện.

**Gợi ý trả lời:**
* Ranh giới thực tế: mình phải giải thích được từng dòng code mình commit; AI sinh khung, mình chịu trách nhiệm type, logic, responsive.
* Góp ý Cross-Testing nên cụ thể: màn hình nào, thiết bị nào, bước tái hiện lỗi.
* Có thể kể prompt workflow hiệu quả nhất của nhóm.

**Tiêu chí bài đăng tốt:** phản tư trung thực, có ví dụ cụ thể; góp ý cho nhóm khác lịch sự, đủ thông tin để họ tái hiện.

#### 👥 Hoạt động nhóm: Chuẩn bị và trình bày Final Showcase

**Mục tiêu:** Trình bày sản phẩm hoàn chỉnh trong 8 phút, demo live, trả lời phản biện 5 phút; tham gia trải nghiệm chéo các nhóm khác.

| Vai trò | Việc cần làm |
|---|---|
| Team Lead | Dẫn dắt kịch bản thuyết trình: Wireframe → Vercel App; giữ đúng 8 phút |
| UI Developer | Demo giao diện responsive, tùy biến Theme, các điểm UI/UX nổi bật |
| Logic/API | Demo luồng chính: xem sự kiện → chọn vé/ghế → đặt vé (API thật) → Wishlist/đăng nhập |
| QA/DevOps | Chuẩn bị link Vercel, ảnh Lighthouse, Git log từng cá nhân; phương án dự phòng (video demo) |

**Output:** Slide thuyết trình, link Vercel Live, báo cáo Word/PDF đã nộp; điểm cuối kỳ cá nhân = Điểm nhóm × 0.7 + Điểm phản biện cá nhân × 0.3.

---

> 📚 **Liên kết trong bộ học liệu:** yêu cầu nộp chi tiết xem `assignment/bai-tap-va-nhiem-vu.md`; tài liệu và prompt mẫu xem `resources/tai-nguyen-hoc-tap.md`; đặc tả dự án xem `documentation/dac-ta-du-an-smart-event-hub.md`.
