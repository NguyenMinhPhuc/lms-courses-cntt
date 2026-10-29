# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 4: ĐÁNH GIÁ GIỮA KỲ
### Bài 07: Kiểm tra giữa kỳ – Báo cáo tiến độ 50% dự án (Production build check, README, Conventional Commits)

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Kiểm tra giữa kỳ (30% điểm học phần) – Báo cáo đồ án nhóm · **Chuẩn đầu ra:** PI 1.4 (CLO1), PI 2.3 (CLO2), PI 5.1 (CLO4)
> **Dự án xuyên suốt:** Smart Event Hub – nghiệm thu 50% tiến độ: Wireframe 5 màn hình, Routing, UI Layout (Ant Design + SCSS) và kiến trúc Component.

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Giải thích được vì sao một dự án chạy tốt với `npm run dev` vẫn có thể thất bại khi `npm run build`; trình bày được cấu trúc README chuẩn và quy ước Conventional Commits.
> * **[Bloom 3/4 - Kỹ năng]:** Chạy `npm run lint` / `npm run build`, phân tích thông báo lỗi TypeScript/ESLint/Hydration và sửa dứt điểm; dọn dẹp code (console.log, dead code, `any`) trước khi báo cáo.
> * **[Bloom 5/6 - Năng lực]:** Đóng gói và trình bày sản phẩm nhóm trong 10 phút, bảo vệ phần code cá nhân trong 5 phút phản biện; tự đánh giá sản phẩm theo rubric giữa kỳ.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Tối hôm trước buổi báo cáo, nhóm của Minh chạy `npm run dev`, mở trình duyệt và thấy mọi trang Smart Event Hub hiển thị đẹp. Sáng hôm sau, giảng viên yêu cầu chạy `npm run build` ngay tại lớp. Terminal đỏ rực: `Type error: Property 'bannerUrl' does not exist on type 'EventItem'`, kèm hai lỗi ESLint `no-unused-vars` và một cảnh báo `useSearchParams() should be wrapped in a suspense boundary`. Nhóm mất 20 phút đầu buổi chỉ để sửa lỗi thay vì luyện demo.

**Câu hỏi gợi mở:** Nếu dev server không báo gì, tại sao build lại thất bại? Và khi giảng viên hỏi "Phần nào trong repo là do em viết?", bạn sẽ chứng minh bằng cách nào ngoài lời kể? Buổi hôm nay trả lời cả hai câu hỏi đó, đồng thời là buổi **kiểm tra giữa kỳ chiếm 30% điểm học phần**.

> 🧭 **Trước giờ học (Flipped Classroom):** Đọc *Next.js Production Checklist* và *Conventional Commits Specification* (link ở mục 5). Hoàn thành BTVN Buổi 6: chuẩn bị Slide, Wireframe, Source Code. Mỗi nhóm tự chạy thử `npm run lint` và `npm run build` ở nhà, ghi lại các lỗi gặp phải. Làm quiz ôn tập giai đoạn 1 (5–10 câu) trên LMS `https://learn.lhu.edu.vn`.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Quy trình kiểm tra Production Build: vì sao dev chạy được mà build lỗi?

* **Khái niệm:** **Production build** là bước Next.js biên dịch toàn bộ dự án thành bản tối ưu để triển khai. Lệnh `npm run build` (tức `next build`) kích hoạt **TypeScript type checker** và **ESLint** trên mọi file, đồng thời prerender các trang tĩnh. Mọi lỗi type hoặc promise không được xử lý phải được giải quyết triệt để trước khi demo hay deploy.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Dev biên dịch theo yêu cầu:** `next dev` chỉ compile route bạn đang mở. Trang `/admin/manage-events` chưa ai truy cập thì lỗi trong đó vẫn "ngủ yên".
  * **Dev ưu tiên tốc độ:** lỗi type thường chỉ hiện gạch đỏ trong VS Code, không chặn trang. Ngược lại, build dừng hẳn khi gặp lỗi type hoặc lỗi ESLint mức `error`.
  * **Prerender lúc build:** Server Component của trang tĩnh được thực thi ngay khi build. Code chạm vào `window`, `localStorage` ở cấp module sẽ văng lỗi `window is not defined`.
  * **Môi trường khác nhau:** Windows không phân biệt hoa thường trong đường dẫn, còn Linux (máy build của Vercel) thì có. `import Header from './header'` trong khi file tên `Header.tsx` sẽ lỗi khi deploy.

```bash
# Quy trình kiểm tra lỗi tĩnh trước khi báo cáo (chạy theo đúng thứ tự)
npm run lint          # ESLint: unused vars, any, rules của Next.js
npx tsc --noEmit      # (tùy chọn) chỉ kiểm tra type, không sinh file
npm run build         # Type check + lint + build production
npm run start         # Chạy thử bản build tại http://localhost:3000
```

| Lỗi thường gặp khi build | Nguyên nhân | Cách sửa |
|---|---|---|
| `Type error: Property 'x' does not exist on type 'Y'` | Interface lệch với dữ liệu thật, code AI tự thêm field | Cập nhật interface trong `types/`, không ép kiểu bằng `any` |
| `'foo' is defined but never used` | Biến, import thừa sau khi refactor | Xóa bỏ, hoặc dùng `npm run lint -- --fix` |
| `useSearchParams() should be wrapped in a suspense boundary` | Client Component dùng `useSearchParams` trên trang prerender | Bọc component đó trong `<Suspense fallback={...}>` |
| `ReferenceError: window is not defined` | Truy cập Browser API khi render trên server | Chuyển vào `useEffect` hoặc dùng `dynamic(..., { ssr: false })` trong Client Component |
| `Module not found: Can't resolve './header'` | Sai hoa thường tên file | Đặt tên file và import trùng khớp tuyệt đối |

* **💡 Ví dụ thực tế (Real-world Example):**
  > Nhóm Smart Event Hub dùng AI sinh `EventCard` với prop `bannerUrl`, nhưng interface `EventItem` chỉ có `imageUrl`. Ở dev, trang chủ vẫn hiện vì ảnh lỗi không làm vỡ layout. Khi build, TypeScript chặn ngay. Cách sửa đúng: thống nhất một tên field trong `types/event.ts`, không phải thêm `// @ts-ignore`.

#### 2.2. Clean Code trước khi báo cáo

* **Khái niệm:** Clean code giai đoạn giữa kỳ tập trung vào ba việc: **loại bỏ `console.log` và dead code**, **không còn `any`**, và **đặt tên file/component nhất quán**. Giảng viên sẽ mở code của từng thành viên, nên mã nguồn gọn gàng giúp bạn giải thích nhanh và tự tin hơn.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Quy ước đặt tên:** Component và file component dùng PascalCase (`EventCard.tsx`); hook bắt đầu bằng `use` (`useDebounce.ts`); thư mục route dùng chữ thường, gạch nối (`manage-events/`); SCSS Module đặt cùng tên component (`EventCard.module.scss`).
  * **Để ESLint làm "người gác cổng":** nâng các rule quan trọng lên mức `error` để build tự chặn khi còn vi phạm.
  * **Hydration warning cũng là lỗi:** cảnh báo vàng/đỏ trong DevTools Console (ví dụ `Text content does not match server-rendered HTML`) phải được xử lý, không được bỏ qua khi demo.

```js
// eslint.config.mjs (Next.js 15 – flat config do create-next-app sinh ra, bổ sung rules)
import { dirname } from 'path';
import { fileURLToPath } from 'url';
import { FlatCompat } from '@eslint/eslintrc';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const compat = new FlatCompat({ baseDirectory: __dirname });

const eslintConfig = [
  ...compat.extends('next/core-web-vitals', 'next/typescript'),
  {
    rules: {
      'no-console': ['warn', { allow: ['warn', 'error'] }],
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-unused-vars': 'error',
    },
  },
];

export default eslintConfig;
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Trước báo cáo, Lan chạy `npm run lint` và phát hiện 14 câu `console.log('data', data)` còn sót trong trang Đặt vé, cùng một component `OldSeatPicker.tsx` không còn được import ở đâu. Xóa toàn bộ, commit với message `chore(booking): remove debug logs and unused seat picker`. Lịch sử Git vừa sạch, vừa là minh chứng đóng góp.

> 💡 **Mẹo:** Từ Next.js 15.5, lệnh `next lint` được đánh dấu deprecated. Nếu terminal hiện cảnh báo này, các bạn đổi script `"lint"` trong `package.json` thành `"eslint ."` – cấu hình `eslint.config.mjs` ở trên vẫn dùng được.

#### 2.3. Cấu trúc README.md chuẩn cho đồ án

* **Khái niệm:** `README.md` đặt tại **root của Git Repository** là "cửa trước" của dự án. Người chấm mở repo sẽ đọc file này đầu tiên để biết dự án làm gì, ai làm phần nào và chạy thế nào.
* **Chi tiết kỹ thuật / Lý thuyết:** README giữa kỳ bắt buộc có 5 phần:
  * **Tổng quan:** tên dự án, mô tả 3–4 câu, công nghệ sử dụng.
  * **Thành viên & phân công:** bảng gồm Họ tên, MSSV, Vai trò, Tính năng đã đảm nhiệm.
  * **Hướng dẫn cài đặt:** các lệnh chạy được ngay trên máy mới.
  * **Sơ đồ thư mục:** kiến trúc App Router đang dùng.
  * **Thiết kế:** link Figma Wireframe 5 màn hình (hoặc ảnh chụp trong `docs/wireframes/`) và link Preview/Demo.

~~~markdown
# Smart Event Hub

Hệ thống đặt vé & quản lý sự kiện trực tuyến, xây dựng bằng Next.js 15 (App Router),
TypeScript, Ant Design v5 và SCSS Module. Người dùng tìm kiếm sự kiện, xem chi tiết,
chọn ghế và đặt vé; Admin quản lý sự kiện và đơn hàng.

## Thành viên & Phân công
| Họ tên | MSSV | Vai trò | Tính năng đã đảm nhiệm |
|---|---|---|---|
| Nguyễn Văn A | 1234xxxx | Team Lead | Layout chung, Routing, Admin Dashboard |
| Trần Thị B | 1234xxxx | Front-End Dev | Trang chủ, EventCard, Filter |

## Cài đặt & chạy local
```bash
git clone <repo-url>
cd smart-event-hub
npm install
npm run dev   # http://localhost:3000
```

## Cấu trúc thư mục
```text
app/            # Routes (App Router): (auth), events/[id], checkout, admin...
components/     # ui/ (atoms) · shared/ · organisms/
styles/         # _variables.scss, _mixins.scss
types/          # Interface & type dùng chung
```

## Thiết kế & Demo
- Wireframe Figma: <link>
- Preview: <link>
~~~

* **💡 Ví dụ thực tế (Real-world Example):**
  > Một nhóm ghi lệnh `yarn dev` trong README nhưng repo chỉ có `package-lock.json`. Giảng viên clone về, chạy theo hướng dẫn và gặp lỗi ngay bước đầu. Quy tắc: **mỗi lệnh trong README phải được chính nhóm chạy thử trên một thư mục clone mới**.

#### 2.4. Conventional Commits & minh chứng đóng góp Git

* **Khái niệm:** **Conventional Commits** là quy ước viết commit message theo dạng `<type>(<scope>): <mô tả ngắn>`. Lịch sử commit rõ ràng giúp giảng viên nhận ra ai đã làm tính năng nào, thay vì chỉ thấy một chuỗi "update", "fix bug", "abc".
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `feat`: thêm tính năng · `fix`: sửa lỗi · `refactor`: tái cấu trúc, không đổi hành vi · `style`: định dạng, SCSS · `docs`: tài liệu, README · `chore`: cấu hình, dọn dẹp.
  * `scope` là phân hệ: `auth`, `event`, `cart`, `ui`, `admin`…
  * Mô tả viết ở thể mệnh lệnh, ngắn gọn, tiếng Anh hoặc tiếng Việt thống nhất trong nhóm.

```bash
# Mẫu commit message chuẩn
git commit -m "feat(event): implement seat matrix selection logic"
git commit -m "fix(cart): resolve total amount calculation bug"
git commit -m "feat(auth): add login form validation"
git commit -m "fix(ui): repair responsive layout on mobile"

# Lệnh trích xuất minh chứng đóng góp cá nhân
git shortlog -sn --all                        # Số commit theo từng thành viên
git log --author="Tran Thi B" --oneline       # Commit của một người
git log --graph --oneline --all               # Sơ đồ branch & merge
```

* **Minh chứng nên chuẩn bị:** Git Commit Log từng cá nhân, danh sách Pull Request đã tạo/review trên GitHub, trang *Insights → Contributors* của repo, và bảng phân công trong README khớp với lịch sử commit.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Hai nhóm cùng hoàn thành trang Đặt vé. Nhóm thứ nhất có 3 commit "update code" do một người push. Nhóm thứ hai có 27 commit chia đều cho 4 thành viên, mỗi tính năng nằm trên một branch `feature/...` và được merge qua PR. Tiêu chí "Git & phối hợp" sẽ phân biệt rõ hai nhóm này.

#### 2.5. Sản phẩm cần nộp, kịch bản báo cáo & Rubric giữa kỳ

* **Sản phẩm cần nộp:** (1) File Wireframe Figma 5 màn hình (Trang chủ, Chi tiết sự kiện, Đặt vé, Trang cá nhân, Admin Dashboard); (2) Source Code Repository Git có commit đầy đủ của các thành viên; (3) Link Preview/Demo giao diện đã áp dụng Ant Design/SCSS Responsive; (4) `README.md` chuẩn; (5) Slide báo cáo 5–7 slide.
* **Kịch bản 10 phút thuyết trình + 5 phút phản biện:**

| Mốc thời gian | Nội dung trình bày | Người phụ trách gợi ý |
|---|---|---|
| 0'–1' | Giới thiệu nhóm, mục tiêu dự án, phân công | Team Lead |
| 1'–3' | Trình diễn Wireframe 5 màn hình chính | Thành viên phụ trách UI/UX |
| 3'–7' | Demo live: Responsive Mobile/Desktop, Ant Design + SCSS Custom, luồng Routing mượt mà | Mỗi người demo phần mình làm |
| 7'–9' | Kiến trúc Component & cấu trúc thư mục App Router | Thành viên phụ trách kiến trúc |
| 9'–10' | Git Commit Log từng cá nhân, kết quả `npm run build` | Team Lead |
| 10'–15' | **Phản biện cá nhân:** GV hỏi trực tiếp từng thành viên về code mình đảm nhiệm | Từng cá nhân |

* **Rubric giữa kỳ (tổng 5 điểm, quy đổi sang thang 10):**

| Tiêu chí | Điểm tối đa | Yêu cầu để đạt tối đa |
|---|---|---|
| Wireframe UI | 1.5 | Đủ 5 màn hình, cấu trúc chuẩn Header/Content/Sidebar/Footer, khớp giao diện thực tế |
| UI chuyên nghiệp | 2.0 | Ant Design/Bootstrap + SCSS Custom, Responsive Mobile/Desktop, Hot Reload không lỗi, Console sạch |
| Routing & Component Architecture | 1.0 | App Router đúng convention, Nested/Dynamic Route chạy mượt, component tái sử dụng tổ chức rõ ràng |
| Git Commit & phối hợp nhóm | 0.5 | Mỗi thành viên có commit riêng, message theo Conventional Commits, có branch/PR |
| **Tổng** | **5.0** | **Điểm thang 10 = Tổng × 2** |

* **💡 Ví dụ thực tế (Real-world Example):**
  > Nhóm đạt Wireframe 1.5 + UI 1.5 + Routing 1.0 + Git 0.5 = 4.5/5, quy đổi **9.0/10**, chiếm 30% điểm học phần. Phần phản biện 5 phút dùng để xác minh mỗi cá nhân thực sự hiểu và đã viết phần code được ghi trong bảng phân công.

#### 2.6. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

AI rất hữu ích để soạn khung README và chẩn đoán lỗi hydration. Tuy vậy, nội dung báo cáo là **trách nhiệm của nhóm**: AI không biết MSSV, không biết ai làm gì, và có thể "bịa" tính năng chưa hề tồn tại.

```text
Hãy đóng vai một Technical Lead. Viết cho tôi nội dung file README.md bằng Markdown
cho dự án "Smart Event Hub" (Next.js, TypeScript, Ant Design, SCSS).
Yêu cầu chi tiết:
1. Tên dự án & Mô tả ngắn gọn (3-4 câu).
2. Bảng phân công công việc nhóm 4 người (Cột: Họ tên, MSSV, Vai trò, Tính năng đã đảm nhiệm).
3. Hướng dẫn chạy dự án ở local (npm install, npm run dev).
4. Cấu trúc thư mục dự án (App Router architecture).
5. Link đính kèm file thiết kế Wireframe Figma.
```

```text
Tôi gặp lỗi Hydration Error trong Next.js App Router khi sử dụng Component DatePicker / Modal
của Ant Design. Hãy giải thích nguyên nhân và đưa ra giải pháp sửa lỗi triệt để bằng cách
sử dụng `dynamic import` với `{ ssr: false }` hoặc Hook `useEffect` để chỉ render ở Client-side.
```

Lưu ý quan trọng với Next.js 15: `dynamic(..., { ssr: false })` **chỉ được gọi bên trong Client Component**. Nếu AI đặt nó trong `page.tsx` (Server Component), build sẽ báo lỗi.

```tsx
// components/booking/BookingDatePickerNoSSR.tsx
'use client';

import dynamic from 'next/dynamic';
import { Skeleton } from 'antd';

const BookingDatePickerNoSSR = dynamic(() => import('./BookingDatePicker'), {
  ssr: false,
  loading: () => <Skeleton.Input active block />,
});

export default BookingDatePickerNoSSR;
```

**Checklist kiểm duyệt output AI trước khi nộp:**
* README: thay toàn bộ tên, MSSV, link giả bằng thông tin thật; xóa tính năng nhóm chưa làm.
* Mọi lệnh trong README đã được chạy thử; cấu trúc thư mục khớp repo thực tế.
* Lời giải hydration: tìm đúng nguyên nhân gốc (`new Date()`, `Math.random()`, `localStorage` trong lúc render, thẻ `<div>` lồng trong `<p>`…) trước khi tắt SSR. `ssr: false` là giải pháp sau cùng, không phải mặc định.
* Sau khi sửa: `npm run lint` và `npm run build` đều pass, Console không còn cảnh báo.

#### 2.7. Lịch trình 225 phút của buổi kiểm tra

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Tổng kết giai đoạn 1 & quy trình đánh giá | 60' | GV review Wireframe, App Router, Ant Design/SCSS Module, Clean Code TypeScript; phổ biến kịch bản báo cáo và rubric | Nhóm nắm rõ tiêu chí chấm, thứ tự báo cáo |
| Guided – Chuẩn bị & đóng gói báo cáo | 45' | GV hướng dẫn từng nhóm chạy `npm run build`; hoàn thiện `README.md`; tổng hợp link Preview/Demo Buổi 1–6 | README chuẩn tại root repo; build pass 100%, không lỗi Compile/Type |
| Unguided – Kiểm tra lỗi tự động & Hot Reload | 45' | Cross-review 4 trang chính; sửa console warning, hydration mismatch; chuẩn bị Slide 5–7 slide | App chạy mượt, Console không còn lỗi đỏ/vàng; Slide hoàn chỉnh |
| Team Challenge – Báo cáo giữa kỳ | 60' | Mỗi nhóm 10' thuyết trình & demo live + 5' phản biện cá nhân | Điểm giữa kỳ ghi nhận theo rubric |
| Tổng kết | 15' | GV nhận xét chung, công bố điểm, giao BTVN | Danh sách góp ý cho từng nhóm |

* **Guided (45'):** Giảng viên đi từng nhóm, cùng chạy `npm run build` để phát hiện lỗi TypeScript/ESLint ẩn. Nhóm hoàn thiện README gồm mô tả dự án, thành viên & phân công, hướng dẫn cài đặt, sơ đồ Wireframe (link Figma/ảnh chụp).
* **Unguided (45'):** Các nhóm tự review chéo giữa các trang Trang chủ, Chi tiết sự kiện, Đặt vé, Dashboard Admin. Kiểm tra Hot Reload, xử lý dứt điểm lỗi console và hydration còn tồn đọng, hoàn thiện Slide.
* **Team Challenge (60'):** Nội dung demo bắt buộc: Wireframe 5 màn hình chính; giao diện thực tế Responsive Mobile/Desktop với Ant Design + SCSS Custom; luồng điều hướng Routing; Git Commit Log từng cá nhân. Lịch báo cáo cụ thể của từng nhóm do giảng viên công bố trước buổi học.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)
* 🔹 **Build mới là thước đo thật:** `npm run dev` chỉ compile route đang mở; `npm run build` kiểm tra type, lint và prerender toàn bộ dự án.
* 🔹 **Thứ tự kiểm tra:** `npm run lint` → `npm run build` → `npm run start`, và Console DevTools phải sạch lỗi đỏ/vàng.
* 🔹 **Clean code tối thiểu:** không `console.log`, không dead code, không `any`, tên file/component nhất quán.
* 🔹 **README là cửa trước của repo:** tổng quan, phân công, cài đặt, sơ đồ thư mục, link Wireframe/Demo – mọi lệnh phải chạy được.
* 🔹 **Conventional Commits = minh chứng đóng góp:** `type(scope): mô tả`, commit đều đặn trên branch riêng, merge qua PR.
* 🔹 **Rubric giữa kỳ 5 điểm:** Wireframe 1.5 · UI 2.0 · Routing & Component 1.0 · Git 0.5, nhân 2 để quy đổi thang 10.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Dự án chạy bình thường với `npm run dev` nhưng `npm run build` báo `Type error` ở trang `/admin/manage-events`. Nguyên nhân hợp lý nhất là gì?
- A. Máy tính thiếu RAM khi build
- B. Dev server chỉ compile route được truy cập và không chặn trang vì lỗi type
- C. Next.js không hỗ trợ TypeScript ở chế độ production
- D. Trang admin bắt buộc phải là Client Component

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> <code>next dev</code> biên dịch theo yêu cầu và ưu tiên tốc độ, còn <code>next build</code> kiểm tra type trên toàn bộ dự án nên lỗi "ngủ yên" ở trang chưa mở sẽ lộ ra.
</details>

**Câu 2:** Commit message nào tuân thủ Conventional Commits?
- A. `update code trang dat ve`
- B. `Fixed bug!!!`
- C. `fix(cart): resolve total amount calculation bug`
- D. `cart - final version 2`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Định dạng chuẩn là <code>type(scope): mô tả</code>. Phương án C có type <code>fix</code>, scope <code>cart</code> và mô tả rõ thay đổi.
</details>

**Câu 3:** Một nhóm đạt Wireframe 1.0, UI 2.0, Routing & Component 0.75, Git 0.25. Điểm giữa kỳ quy đổi thang 10 là bao nhiêu?
- A. 8.0
- B. 4.0
- C. 7.5
- D. 9.0

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> Tổng 1.0 + 2.0 + 0.75 + 0.25 = 4.0/5, nhân 2 được 8.0/10.
</details>

**Câu 4:** AI đề xuất đặt `dynamic(() => import('./DatePicker'), { ssr: false })` trực tiếp trong `app/checkout/page.tsx` (Server Component). Với Next.js 15, bạn xử lý thế nào?
- A. Giữ nguyên vì `ssr: false` dùng được ở mọi nơi
- B. Thêm `// @ts-ignore` phía trên dòng dynamic
- C. Xóa DatePicker khỏi trang để tránh lỗi
- D. Chuyển lời gọi `dynamic` vào một Client Component có `'use client'` rồi import component đó vào page

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> Next.js 15 không cho phép <code>ssr: false</code> trong Server Component. Cần bọc lời gọi <code>dynamic</code> trong một file Client Component riêng.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-07-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)
* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Sau buổi báo cáo, hãy chia sẻ một lỗi build hoặc lỗi hydration "khó chịu" nhất nhóm bạn gặp phải: dấu hiệu ra sao, nguyên nhân gốc là gì, AI gợi ý gì và gợi ý đó đúng hay sai? Theo bạn, nhóm nên thay đổi quy trình làm việc thế nào (ví dụ chạy build trước mỗi lần merge) để không lặp lại?
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Tiếp thu nhận xét/góp ý của giảng viên trong buổi báo cáo, cập nhật và tối ưu lại UI/Codebase trên branch `main`.
  * Xem trước tài liệu RESTful API / Swagger UI của dự án Smart Event Hub để chuẩn bị cho Buổi 8 (Tích hợp API).
  * **Output:** Codebase sạch, `npm run build` pass, sẵn sàng ghép nối Backend API. Mỗi góp ý được xử lý trong một commit hoặc PR riêng, ví dụ `fix(ui): apply midterm feedback on event detail spacing`.
  * **Hạn nộp:** trước buổi học tiếp theo. Nộp link PR đã merge (tên PR: `[Midterm-Feedback] <Tên nhóm>`) lên LMS.
* **📚 Tài liệu đọc & tham khảo:**
  * Conventional Commits Specification: https://www.conventionalcommits.org/
  * Next.js Production Checklist: https://nextjs.org/docs/app/building-your-application/deploying/production-checklist
  * Next.js – ESLint configuration: https://nextjs.org/docs/app/api-reference/config/eslint
  * Next.js – Hydration error: https://nextjs.org/docs/messages/react-hydration-error
