# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 1: NỀN TẢNG & MÔ HÌNH HÓA GIAO DIỆN
### Bài 01: SCSS nâng cao, TypeScript căn bản & thiết lập Vibe Coding

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Lớp học đảo ngược · **Chuẩn đầu ra:** PI 1.4 (CLO1), PI 2.3 (CLO2)
> **Dự án xuyên suốt:** Smart Event Hub – Khởi tạo dự án, dựng Design Token SCSS, Layout Banner và Card sự kiện.

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Giải thích được Variables, Nesting, Mixins, Breakpoints trong SCSS; quy tắc BEM kết hợp CSS Modules; khác biệt giữa `interface` và `type` trong TypeScript.
> * **[Bloom 3/4 - Kỹ năng]:** Áp dụng Mixin `respond-to` và TypeScript Interface để xây dựng component `EventCard` responsive, không có lỗi `implicit any`.
> * **[Bloom 5/6 - Năng lực]:** Viết Prompt theo cấu trúc Context → Requirement → Constraint, đánh giá và sửa code do AI sinh ra; phối hợp nhóm qua Git (branch, Pull Request, review chéo).

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Hãy hình dung nhóm các bạn có bốn thành viên, mỗi người tự đặt màu chủ đạo cho phần mình làm. Người dùng `#3b82f6`, người dùng `blue`, người khác lại viết `.title` trùng tên với file CSS của bạn cùng nhóm. Đến ngày ghép code, giao diện "Smart Event Hub" trông như bốn website khác nhau, còn card sự kiện thì vỡ khung trên điện thoại. Nguyên nhân không nằm ở kỹ năng gõ code, mà ở chỗ nhóm chưa có một **hệ thống biến dùng chung**, chưa có **kiểu dữ liệu thống nhất** cho đối tượng sự kiện và chưa có **quy tắc làm việc với AI**.

Vậy làm thế nào để AI sinh code nhanh mà vẫn đúng kiểu, đúng màu, đúng breakpoint của cả nhóm? Buổi học này trả lời câu hỏi đó bằng ba công cụ: SCSS có tổ chức, TypeScript chặt chẽ và một quy trình Vibe Coding có kiểm soát.

> 🧭 **Trước giờ học (Flipped Classroom):**
> * Xem video SCSS Flexbox/Grid Mixin và video TypeScript Interface vs Type do giảng viên đăng trên LMS.
> * Cài đặt VS Code, Node.js (bản LTS), Git và Cursor AI hoặc extension GitHub Copilot.
> * Đọc tài liệu Sass, TypeScript for React, Next.js CSS Modules (mục 5) và làm Quiz nhanh 5–10 câu trên LMS.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. SCSS nâng cao: Variables, Nesting, Mixins & Breakpoints

* **Khái niệm:** SCSS là cú pháp mở rộng của CSS, cho phép khai báo biến, lồng selector và đóng gói đoạn CSS lặp lại bằng `@mixin`. Mã SCSS được biên dịch thành CSS thuần trước khi chạy trên trình duyệt.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Variable System:** gom màu sắc, spacing, font size, shadow vào một file `_variables.scss` (Design Token). Đổi một biến, toàn bộ dự án thay đổi theo.
  * **Nesting:** viết selector con bên trong selector cha, nhưng không nên lồng quá 3 cấp để tránh CSS khó ghi đè.
  * **Mixin & Breakpoints:** `@mixin respond-to($breakpoint)` dùng map để quản lý responsive tập trung tại các mốc 640px, 768px, 1024px. Mixin viết theo hướng **mobile-first** (`min-width`): style gốc dành cho điện thoại, các mốc lớn hơn bổ sung dần.
  * Dart Sass hiện khuyến nghị `@use` thay cho `@import` và `map.get` (module `sass:map`) thay cho hàm cũ `map-get`; hai cách cho kết quả như nhau.

```scss
// styles/_variables.scss – Design Token dùng chung cho cả nhóm
$color-primary: #6366f1;
$color-upcoming: #3b82f6;
$color-ongoing: #22c55e;
$color-ended: #9ca3af;
$color-text: #1f2937;

$space-sm: 8px;
$space-md: 16px;
$space-lg: 24px;

$font-size-base: 16px;
$font-size-lg: 20px;
$radius-md: 12px;
$shadow-card: 0 4px 16px rgba(0, 0, 0, 0.08);
```

```scss
// styles/_mixins.scss
@use 'sass:map';

$breakpoints: ('mobile': 640px, 'tablet': 768px, 'desktop': 1024px);

@mixin respond-to($breakpoint) {
  $value: map.get($breakpoints, $breakpoint);
  @if $value {
    @media (min-width: $value) { @content; }
  } @else {
    @warn "Breakpoint `#{$breakpoint}` không tồn tại.";
  }
}

@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

@mixin text-truncate($lines: 1) {
  display: -webkit-box;
  -webkit-line-clamp: $lines;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Khách hàng yêu cầu đổi màu thương hiệu Smart Event Hub từ tím sang cam ngay trước buổi demo. Nhờ `$color-primary` nằm trong `_variables.scss`, nhóm chỉ sửa đúng một dòng thay vì dò tìm hàng chục mã màu rải rác trong 20 file.

#### 2.2. BEM Naming Convention & CSS Modules trong Next.js

* **Khái niệm:** BEM (`Block__Element--Modifier`) là quy tắc đặt tên class giúp đọc tên là hiểu cấu trúc. CSS Modules (`filename.module.scss`) tự động mã hóa (hash) tên class, ví dụ `.card` thành `EventCard_card__x7Ab2`, nên style chỉ có hiệu lực trong component import nó.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Block: `card`; Element: `card__title`, `card__image`; Modifier: `badge--upcoming`, `badge--ended`.
  * Trong TSX, truy cập class có ký tự đặc biệt bằng ngoặc vuông: `styles['card__title']`.
  * CSS Modules giải quyết **Global CSS pollution**: hai component cùng có class `.title` không còn ghi đè lẫn nhau, vì sau khi build chúng mang hai tên hash khác nhau.
  * Next.js hỗ trợ SCSS sẵn, chỉ cần cài thêm gói `sass`: `npm install -D sass`.

> **Lưu ý:** CSS Modules không thay thế BEM. Hash tránh xung đột giữa các file, còn BEM giúp đồng đội đọc hiểu quan hệ giữa các class trong cùng một file.

#### 2.3. TypeScript căn bản cho React

* **Khái niệm:** TypeScript bổ sung hệ thống kiểu tĩnh cho JavaScript. Lỗi sai kiểu được phát hiện ngay trong editor và lúc build, thay vì đợi người dùng gặp lỗi trên trình duyệt.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Primitives & Array/Object typing:** `string`, `number`, `boolean`, `string[]`, `{ id: string; price: number }`.
  * **Interface vs Type:** `interface` mở rộng được qua `extends`, hợp với React Props và Data Model. `type` hợp với **Union Types** như `'UPCOMING' | 'ONGOING' | 'ENDED'`.
  * **Enum:** cũng biểu diễn được trạng thái, nhưng sinh thêm mã JavaScript lúc chạy. Trong dự án Next.js, union type gọn hơn và tương thích JSON từ API tốt hơn.
  * **Strict mode & Generics:** bật `"strict": true` trong `tsconfig.json` (mặc định khi tạo dự án Next.js), tuyệt đối tránh `any`. Dùng Generics `<T>` cho hàm/component tái sử dụng.

```ts
// types/event.ts
export type EventStatus = 'UPCOMING' | 'ONGOING' | 'ENDED';

export interface EventItem {
  id: string;
  title: string;
  imageUrl: string;
  startDate: string; // ISO 8601, ví dụ '2026-12-20T19:00:00+07:00'
  location: string;
  price: number;
  status: EventStatus;
}

export interface EventProps {
  event: EventItem;
}

// Cách viết bằng enum (tham khảo) – sinh thêm object JS khi chạy
export enum EventStatusEnum {
  UPCOMING = 'UPCOMING',
  ONGOING = 'ONGOING',
  ENDED = 'ENDED',
}

// Generics: một hàm dùng được cho mọi kiểu phần tử
export function getFirst<T>(items: T[]): T | undefined {
  return items[0];
}
```

#### 2.4. Ghép lại: Component EventCard responsive

Hãy quan sát cách ba mảnh kiến thức trên kết hợp trong một component thật của dự án. Card hiển thị ảnh bìa, tiêu đề, ngày giờ, giá vé và badge trạng thái; lưới card hiển thị 1 cột trên mobile, 2 cột từ 640px và 3 cột từ 1024px.

```tsx
// components/EventCard/EventCard.tsx
import Image from 'next/image';
import type { ReactNode } from 'react';
import type { EventProps, EventStatus } from '@/types/event';
import styles from './EventCard.module.scss';

const STATUS_LABEL: Record<EventStatus, string> = {
  UPCOMING: 'Sắp diễn ra',
  ONGOING: 'Đang diễn ra',
  ENDED: 'Đã kết thúc',
};

const formatPrice = (price: number): string =>
  price === 0
    ? 'Miễn phí'
    : new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);

export default function EventCard({ event }: EventProps) {
  const { title, imageUrl, startDate, location, price, status } = event;

  return (
    <article className={styles.card}>
      <div className={styles['card__image']}>
        {/* fill + sizes: next/image tự chọn kích thước ảnh phù hợp từng màn hình */}
        <Image src={imageUrl} alt={title} fill sizes="(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw" />
        <span className={`${styles.badge} ${styles[`badge--${status.toLowerCase()}`]}`}>
          {STATUS_LABEL[status]}
        </span>
      </div>
      <div className={styles['card__body']}>
        <h3 className={styles['card__title']}>{title}</h3>
        <p>{new Date(startDate).toLocaleString('vi-VN')} · {location}</p>
        <p className={styles['card__price']}>{formatPrice(price)}</p>
      </div>
    </article>
  );
}

export function EventCardGrid({ children }: { children: ReactNode }) {
  return <div className={styles.grid}>{children}</div>;
}
```

```scss
// components/EventCard/EventCard.module.scss
@use '../../styles/variables' as *;
@use '../../styles/mixins' as *;

.grid {
  display: grid;
  grid-template-columns: 1fr;            // Mobile (< 640px): 1 cột
  gap: $space-lg;
  @include respond-to('mobile') { grid-template-columns: repeat(2, 1fr); }  // Tablet: 2 cột
  @include respond-to('desktop') { grid-template-columns: repeat(3, 1fr); } // Desktop: 3 cột
}

.card {
  border-radius: $radius-md;
  box-shadow: $shadow-card;
  overflow: hidden;
  background: #fff;
  transition: transform 0.2s ease;
  &:hover { transform: translateY(-4px); }

  &__image { position: relative; aspect-ratio: 16 / 9; img { object-fit: cover; } }
  &__body { padding: $space-md; color: $color-text; }
  &__title { font-size: $font-size-lg; @include text-truncate(2); }
  &__price { font-weight: 700; color: $color-primary; }
}

.badge {
  position: absolute; top: $space-sm; left: $space-sm;
  padding: 4px $space-sm; border-radius: 999px; color: #fff; font-size: 12px;
  &--upcoming { background: $color-upcoming; }
  &--ongoing { background: $color-ongoing; }
  &--ended { background: $color-ended; }
}
```

> **Cấu hình ảnh từ xa:** nếu `imageUrl` trỏ tới domain ngoài (CDN của Backend), cần khai báo domain đó trong `images.remotePatterns` của `next.config.ts`, nếu không `next/image` sẽ báo lỗi.

#### 2.5. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

* **Khái niệm:** Vibe Coding là cách làm việc trong đó **AI sinh khung code (boilerplate)**, còn **sinh viên chịu trách nhiệm kiểm duyệt** Type Safety, logic và refactor. Các bạn đóng vai Architect, AI là trợ lý gõ phím.
* **Thiết lập Rule cho AI:** tạo file `.cursorrules` ở thư mục gốc (Cursor đọc tự động; với Copilot dùng `.github/copilot-instructions.md`) để AI luôn tuân theo quy ước của nhóm:

```text
# .cursorrules – Smart Event Hub
- Stack: Next.js 15 App Router, TypeScript strict, SCSS Modules.
- Không dùng kiểu any. Interface/Type đặt trong thư mục types/.
- Style: dùng biến trong styles/_variables.scss và mixin trong styles/_mixins.scss, không hard-code màu.
- Đặt tên class theo BEM. Không viết inline style.
- Ảnh dùng next/image, link nội bộ dùng next/link.
- Comment tiếng Việt ngắn gọn ở các đoạn logic quan trọng.
```

* **Prompt 3 bước – Context → Requirement → Constraint.** Prompt hướng dẫn trong phần Guided:

```text
[Context] Hãy đóng vai một Chuyên gia Front-End Developer kinh nghiệm với Next.js và TypeScript.
Hãy viết cho tôi một Component React tên là EventCard.tsx kèm theo file SCSS Module EventCard.module.scss.

[Requirement]
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

[Constraint]
- Sử dụng Next.js Image component (next/image).
- Code rõ ràng, ngắn gọn, có comment giải thích các phần quan trọng.
```

* **Checklist kiểm duyệt code AI trước khi commit:**
  * Có kiểu `any` hoặc thiếu kiểu cho props không? Chạy `npx tsc --noEmit` để chắc chắn.
  * Union type có đủ 3 trạng thái, `Record<EventStatus, string>` có thiếu key nào không?
  * AI có hard-code màu/kích thước thay vì dùng biến SCSS không?
  * Dùng `next/image` đúng cách (`alt`, `fill` + `sizes` hoặc `width`/`height`)?
  * Thu nhỏ trình duyệt qua 375px, 768px, 1440px: lưới có đổi 1–2–3 cột, có tràn ngang không?

#### 2.6. Thực hành trên lớp

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Guided Practice | 45 phút | Dùng prompt mẫu sinh `EventCard.tsx`, `EventCard.module.scss`, `types/event.ts`; sửa lỗi type mismatch do AI gợi ý sai | Card hiển thị đúng dữ liệu từ Props, không lỗi TS, co giãn không vỡ |
| Unguided Practice | 45 phút | Tự xây `HeaderNavigationBar.tsx` với TypeScript strict và SCSS Module | Header sticky, link hover mượt, Interface tách ra `types/` |
| Team Challenge | 60 phút | Khởi tạo Git repo nhóm, Design Token System, Mixin dùng chung, PR & review chéo | 1 repo chuẩn cấu trúc, biến SCSS được import thành công, PR merge thành công |
| Tổng kết | 15 phút | Giải đáp, nhận xét PR tiêu biểu, giao BTVN | Danh sách lỗi thường gặp, BTVN đã rõ |

**Guided (45'):** giảng viên làm mẫu từng bước theo prompt ở mục 2.5. Sau khi AI trả kết quả, cả lớp đối chiếu với code mục 2.4, chỉ ra chỗ AI dùng `string` thay vì union type hoặc quên `sizes` cho ảnh.

**Unguided (45'):** tự thiết kế `HeaderNavigationBar.tsx` gồm Logo "Smart Event Hub", menu (Trang chủ, Sự kiện, Bảng tin, Liên hệ), khung tìm kiếm nhanh, nút Đăng nhập/Đăng ký. Tạo Interface `NavMenuItem` cho danh sách menu, hiệu ứng **sticky header** (`position: sticky; top: 0`) và hover animation bằng SCSS. Prompt gợi ý:

```text
Tạo giúp tôi Component HeaderNavigationBar.tsx bằng Next.js App Router và TypeScript.
- Yêu cầu UI: Gồm Logo bên trái, Search Input ở giữa, Menu điều hướng và nút Auth bên phải.
- Yêu cầu TypeScript: Định nghĩa interface NavItem { label: string; href: string; isExternal?: boolean }.
- Yêu cầu SCSS Module: Viết hiệu ứng Sticky Navigation khi scroll và hiệu ứng Hover underline mượt mà cho Menu Link.
- Viết theo chuẩn Clean Code, không xài any.
```

**Team Challenge (60'):** nhóm 3–4 sinh viên khởi tạo repo chung, thiết lập Branch Strategy `main` – `dev` – `feature/<ten>`. Phân công dựng `styles/_variables.scss` (Color Palette, Typography, Spacing, Shadows) và `styles/_mixins.scss` (Responsive Breakpoints, Flex Alignment, Text Truncate) bằng prompt AI. Mỗi thành viên push lên nhánh riêng, tạo Pull Request và review chéo để không xảy ra conflict.

```bash
git checkout -b dev && git push -u origin dev
git checkout -b feature/an-design-tokens
git add styles/ && git commit -m "feat(styles): add design tokens and shared mixins"
git push -u origin feature/an-design-tokens   # sau đó mở PR vào nhánh dev
```

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)

* 🔹 **Design Token trước, component sau:** màu, spacing, typography, shadow nằm trong `_variables.scss`; responsive nằm trong `@mixin respond-to`.
* 🔹 **CSS Modules + BEM:** hash tên class chống xung đột toàn cục, BEM giúp đọc hiểu cấu trúc.
* 🔹 **`interface` cho Props/Data Model, `type` cho Union:** `type EventStatus = 'UPCOMING' | 'ONGOING' | 'ENDED'`.
* 🔹 **Strict mode, không `any`:** lỗi kiểu phải được bắt lúc viết code, không phải lúc demo.
* 🔹 **Prompt 3 bước + `.cursorrules`:** AI sinh khung, người học kiểm duyệt và chịu trách nhiệm về code cuối cùng.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Trường hợp nào nên dùng `type` thay vì `interface` trong TypeScript?
- A. Khai báo Props cho component cần mở rộng bằng `extends`
- B. Khai báo tập giá trị trạng thái `'UPCOMING' | 'ONGOING' | 'ENDED'`
- C. Khai báo class có constructor
- D. Khai báo biến môi trường trong `.env`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Union type chỉ khai báo được bằng <code>type</code>. <code>interface</code> phù hợp cho Props và Data Model nhờ khả năng mở rộng qua <code>extends</code>.
</details>

**Câu 2:** Vì sao CSS Modules giải quyết được vấn đề Global CSS pollution?
- A. Vì nó tự động xóa các class không sử dụng
- B. Vì nó bắt buộc dùng inline style
- C. Vì nó mã hóa (hash) tên class theo từng file, tạo scope cục bộ
- D. Vì nó chuyển toàn bộ CSS sang JavaScript lúc chạy

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Class <code>.title</code> trong <code>EventCard.module.scss</code> được đổi thành tên dạng <code>EventCard_title__hash</code>, nên không đụng với <code>.title</code> của file khác.
</details>

**Câu 3:** Với mixin `respond-to` viết theo `min-width` và map `('mobile': 640px, 'tablet': 768px, 'desktop': 1024px)`, đoạn `@include respond-to('desktop') { grid-template-columns: repeat(3, 1fr); }` có hiệu lực khi nào?
- A. Màn hình rộng từ 1024px trở lên
- B. Màn hình rộng dưới 1024px
- C. Chỉ khi màn hình đúng bằng 1024px
- D. Màn hình từ 640px đến 768px

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> Mixin sinh <code>@media (min-width: 1024px)</code>, tức áp dụng từ 1024px trở lên. Đây là cách viết mobile-first.
</details>

**Câu 4:** Trong prompt 3 bước, câu "Sử dụng next/image, không dùng type any" thuộc thành phần nào?
- A. Context
- B. Requirement
- C. Output format
- D. Constraint

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> Constraint là các ràng buộc kỹ thuật mà code sinh ra bắt buộc tuân theo, giúp AI không "sáng tạo" ngoài quy ước của nhóm.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-01-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)

* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Khi dùng AI sinh `EventCard`, bạn đã gặp lỗi gì (sai kiểu, hard-code màu, quên responsive, dùng `<img>` thay vì `next/image`…)? Hãy dán đoạn code lỗi, giải thích vì sao nó sai và câu prompt bạn đã sửa để AI trả kết quả tốt hơn. Bình luận cho ít nhất 2 bài của bạn khác.
* **Yêu cầu nộp bài (Bài tập về nhà):** Phát triển độc lập 3 component tĩnh cho Smart Event Hub:
  1. `Footer.tsx`: thông tin bản quyền, liên kết mạng xã hội, form Đăng ký nhận bản tin (Newsletter).
  2. `EventCategoryBadge.tsx`: badge thể loại sự kiện (Âm nhạc, Công nghệ, Thể thao, Workshop) kèm icon tương ứng.
  3. `SearchBar.tsx`: thanh tìm kiếm sự kiện nâng cao kèm dropdown chọn địa điểm (Hà Nội, TP.HCM, Đà Nẵng).
  * **Output:** mỗi component có Type Safety (Interface trong `types/`) và SCSS Module riêng; không có `any`.
  * **Hạn nộp:** trước buổi học tiếp theo, dưới dạng Pull Request cá nhân vào nhánh `dev` của nhóm; nộp link PR lên LMS.
  * **Quy tắc đặt tên:** nhánh `feature/<ho-ten-khong-dau>-bai01`, tiêu đề PR `feat(ui): add Footer, EventCategoryBadge, SearchBar`.
* **📚 Tài liệu đọc & tham khảo:**
  * Sass Official Documentation: https://sass-lang.com/documentation/
  * TypeScript Handbook for React: https://www.typescriptlang.org/docs/handbook/react.html
  * Next.js CSS Modules: https://nextjs.org/docs/app/building-your-application/styling/css-modules
  * BEM Methodology: https://getbem.com/
  * **Câu hỏi tự kiểm tra khi đọc:** Khác biệt cốt lõi giữa `interface` và `type` là gì, khi nào dùng loại nào? Tại sao CSS Modules giải quyết được xung đột CSS toàn cục?
