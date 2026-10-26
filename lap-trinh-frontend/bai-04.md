# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 2: NEXT.JS CORE – ROUTING & KIẾN TRÚC COMPONENT
### Bài 04: Dynamic Routing & kiến trúc Reusable Components

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Lớp học đảo ngược · **Chuẩn đầu ra:** PI 2.3 (CLO2)
> **Dự án xuyên suốt:** Smart Event Hub – Xây dựng trang Chi tiết sự kiện `/events/[id]`, trang Danh mục động `/category/[slug]` và bộ UI component dùng chung.

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Giải thích được cú pháp Dynamic Segment `[id]`, Catch-all `[...slug]`, Optional Catch-all `[[...slug]]` và sự khác nhau giữa `params`, `searchParams` với các hook `useParams`, `useSearchParams`, `usePathname`.
> * **[Bloom 3/4 - Kỹ năng]:** Xây dựng được trang động đọc tham số URL theo chuẩn Next.js 15 (`params` là `Promise`) và thiết kế component tái sử dụng có `variant`, `size`, `isLoading` mở rộng từ HTML attributes.
> * **[Bloom 5/6 - Năng lực]:** Đánh giá và tái cấu trúc thư mục `components/` theo nguyên tắc DRY, kiểm duyệt được component do AI sinh ra trước khi đưa vào dự án nhóm.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Smart Event Hub hiện có 3 sự kiện mẫu, nhưng Backend sắp trả về vài trăm sự kiện. Nếu mỗi sự kiện cần một thư mục `app/events/ev-101/`, `app/events/ev-102/`… thì dự án sẽ phình ra không kiểm soát được. Cùng lúc đó, nhìn lại code Buổi 3, các bạn sẽ thấy nút "Mua vé", nút "Xem chi tiết", nút "Đăng nhập" mỗi nơi viết một kiểu CSS, sửa màu thương hiệu phải đi tìm ở cả chục file.

**Làm sao để một file `page.tsx` duy nhất phục vụ được mọi sự kiện, và một component `Button` duy nhất phục vụ được mọi nút bấm?** Đó chính là hai câu hỏi bài học này trả lời: Dynamic Routing cho phần URL và Reusable Component cho phần giao diện.

> 🧭 **Trước giờ học (Flipped Classroom):** Xem video/slide về Next.js Dynamic Routes (params) và Component Props & Reusability pattern do giảng viên chia sẻ trên LMS. Đọc trước hai tài liệu ở mục 5. Làm quiz nhanh 5–10 câu trên `https://learn.lhu.edu.vn`. Chuẩn bị dự án Next.js của nhóm từ Buổi 3 (đã có `app/events/page.tsx`).

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Dynamic Segments: `[id]`, `[...slug]` và `[[...slug]]`
* **Khái niệm:** Dynamic Segment là thư mục có tên đặt trong ngoặc vuông. Next.js dùng phần URL tương ứng làm tham số và truyền vào `page.tsx`.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `app/events/[id]/page.tsx` khớp `/events/123`, `/events/ev-101` → `{ id: 'ev-101' }`.
  * `app/docs/[...slug]/page.tsx` (Catch-all) khớp `/docs/a`, `/docs/a/b/c` → `{ slug: ['a', 'b', 'c'] }`, nhưng **không** khớp `/docs`.
  * `app/shop/[[...slug]]/page.tsx` (Optional Catch-all) khớp cả `/shop` → `{ slug: undefined }`.
  * Tên trong ngoặc là tên thuộc tính trong `params`, nên đặt rõ nghĩa (`[eventId]` tốt hơn `[x]`).
* **💡 Ví dụ thực tế (Real-world Example):**
  > Trang Shopee dùng `/product/[shopId]/[productId]`; Smart Event Hub cần `/events/[id]` cho chi tiết, `/category/[slug]` cho danh mục và `/checkout/[id]` cho thanh toán. Ba thư mục động thay cho hàng trăm thư mục tĩnh.

```text
app/
├── events/
│   ├── page.tsx              → /events
│   └── [id]/page.tsx         → /events/ev-101
├── category/[slug]/page.tsx  → /category/music?page=1&sort=latest
├── checkout/[id]/page.tsx    → /checkout/ev-101
└── docs/[...slug]/page.tsx   → /docs/huong-dan/dat-ve
```

#### 2.2. `params` và `searchParams` trong Server Component (Next.js 15)
* **Khái niệm:** Trong App Router, `page.tsx` nhận hai props: `params` (tham số động trên đường dẫn) và `searchParams` (query string `?page=1&sort=desc`).
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Từ Next.js 15, **cả hai đều là `Promise`**. Phải `await` trước khi dùng; viết `params.id` trực tiếp là cách cũ của Next.js 14.
  * Giá trị query có thể là `string`, `string[]` (khi lặp `?tag=a&tag=b`) hoặc `undefined`, nên cần kiểm tra kiểu.
  * Gọi `notFound()` từ `next/navigation` khi không tìm thấy dữ liệu để hiển thị `not-found.tsx` đã làm ở Buổi 3.

```tsx
// app/events/[id]/page.tsx (Server Component)
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getEventById } from '@/lib/events';

interface PageProps {
  params: Promise<{ id: string }>;
}

export default async function EventDetailPage({ params }: PageProps) {
  const { id } = await params;
  const event = getEventById(id);

  if (!event) notFound(); // notFound() trả về never → TS tự thu hẹp kiểu

  return (
    <main>
      <h1>{event.title}</h1>
      <p>Mã sự kiện: {id}</p>
      <Link href={`/category/${event.categorySlug}`}>{event.categoryName}</Link>
      <Link href={`/checkout/${event.id}`}>Mua vé</Link>
    </main>
  );
}
```

```tsx
// app/category/[slug]/page.tsx (Server Component)
interface CategoryPageProps {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}

export default async function CategoryPage({ params, searchParams }: CategoryPageProps) {
  const { slug } = await params;
  const query = await searchParams;
  const sort = typeof query.sort === 'string' ? query.sort : 'latest';
  const page = Number(typeof query.page === 'string' ? query.page : '1') || 1;

  return <h1>Danh mục: {slug} · sắp xếp: {sort} · trang {page}</h1>;
}
```

#### 2.3. Navigation Hooks trong Client Component
* **Khái niệm:** Khi component cần tương tác (đổi bộ lọc, highlight menu đang chọn), ta dùng hook của `next/navigation`. Các hook này chỉ chạy trong file có `'use client'`.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `useParams()` → đọc tham số động (`{ slug: 'music' }`), trả về đồng bộ, không cần `await`.
  * `useSearchParams()` → đọc query (`searchParams.get('sort')`), là đối tượng chỉ đọc.
  * `usePathname()` → đường dẫn hiện tại (`/category/music`), hay dùng cho menu active.
  * `useRouter()` → điều hướng bằng code: `router.push(...)`, `router.replace(...)`.
  * Component dùng `useSearchParams` nên được bọc trong `<Suspense>`; nếu không, `npm run build` có thể báo lỗi ở trang render tĩnh.

```tsx
// app/category/[slug]/SortSelect.tsx
'use client';

import { usePathname, useRouter, useSearchParams } from 'next/navigation';

export default function SortSelect() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const currentSort = searchParams.get('sort') ?? 'latest';

  const handleChange = (value: string) => {
    const next = new URLSearchParams(searchParams.toString());
    next.set('sort', value);
    next.set('page', '1');
    router.push(`${pathname}?${next.toString()}`);
  };

  return (
    <select value={currentSort} onChange={(e) => handleChange(e.target.value)}>
      <option value="latest">Mới nhất</option>
      <option value="price-asc">Giá tăng dần</option>
      <option value="price-desc">Giá giảm dần</option>
    </select>
  );
}
```

```tsx
// Trong CategoryPage (Server Component)
import { Suspense } from 'react';
import SortSelect from './SortSelect';
// ...
<Suspense fallback={<span>Đang tải bộ lọc...</span>}>
  <SortSelect />
</Suspense>
```

> **Ghi nhớ nhanh:** Server Component đọc query bằng prop `searchParams` (phải `await`). Client Component đọc query bằng hook `useSearchParams()`. Đừng trộn lẫn hai cách trong cùng một file.

#### 2.4. Mock Data có kiểu dữ liệu chặt chẽ
* **Khái niệm:** Trước khi có API thật (Buổi 8), chúng ta dùng file JSON giả lập nhưng vẫn khai báo đúng `interface` để khi đổi sang API không phải sửa giao diện.
* **Chi tiết kỹ thuật / Lý thuyết:** Đặt dữ liệu ở `data/mock-events.json`, gom hàm truy vấn vào `lib/events.ts`. Trang chỉ gọi hàm, không tự lọc mảng.

```ts
// types/event.ts
export type EventStatus = 'UPCOMING' | 'ONGOING' | 'ENDED';

export interface EventItem {
  id: string;
  title: string;
  price: number;
  status: EventStatus;
  categorySlug: string;
  categoryName: string;
  startDate: string; // ISO 8601
}
```

```ts
// lib/events.ts
import rawEvents from '@/data/mock-events.json';
import type { EventItem } from '@/types/event';

const events = rawEvents as EventItem[];

export function getEventById(id: string): EventItem | undefined {
  return events.find((event) => event.id === id);
}

export function getEventsByCategory(slug: string): EventItem[] {
  return events.filter((event) => event.categorySlug === slug);
}
```

```json
[
  { "id": "ev-101", "title": "Tech Summit 2025", "price": 500000, "status": "UPCOMING",
    "categorySlug": "technology", "categoryName": "Công nghệ", "startDate": "2025-12-05T08:00:00Z" },
  { "id": "ev-102", "title": "Đêm nhạc Acoustic", "price": 300000, "status": "UPCOMING",
    "categorySlug": "music", "categoryName": "Âm nhạc", "startDate": "2025-12-12T19:30:00Z" }
]
```

#### 2.5. Reusable Component: Composition, Variant Mapping và Polymorphic
* **Khái niệm:** Component tái sử dụng là component nhận cấu hình qua props thay vì sao chép code (nguyên tắc **DRY – Don't Repeat Yourself**). Ba kỹ thuật chính: `children` prop (Composition), bản đồ `variant`/`size` sang class, và prop `as` (Polymorphic).
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Mở rộng `ButtonHTMLAttributes<HTMLButtonElement>` để component nhận sẵn `onClick`, `type`, `disabled`, `aria-*` mà không phải khai báo lại.
  * Dùng union type cho `variant` và `size` để TypeScript chặn giá trị sai ngay khi gõ.
  * Đặt giá trị mặc định khi destructure, gộp `className` từ bên ngoài để người dùng component vẫn tùy biến được.
  * `Button` không dùng hook nên không bắt buộc `'use client'`. Tuy nhiên, khi cần truyền `onClick`, hãy dùng nó bên trong một Client Component, vì Server Component không truyền được hàm.

```tsx
// components/ui/Button.tsx
import type { ButtonHTMLAttributes, ReactNode } from 'react';
import styles from './Button.module.scss';

type ButtonVariant = 'primary' | 'secondary' | 'danger' | 'outline';
type ButtonSize = 'sm' | 'md' | 'lg';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  isLoading?: boolean;
  leftIcon?: ReactNode;
}

export function Button({
  variant = 'primary',
  size = 'md',
  isLoading = false,
  leftIcon,
  disabled,
  className,
  type = 'button',
  children,
  ...rest
}: ButtonProps) {
  const classes = [styles.btn, styles[variant], styles[size], className].filter(Boolean).join(' ');

  return (
    <button type={type} className={classes} disabled={disabled || isLoading} aria-busy={isLoading} {...rest}>
      {isLoading ? <span className={styles.spinner} aria-hidden="true" /> : leftIcon}
      {children}
    </button>
  );
}
```

```scss
// components/ui/Button.module.scss
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid transparent;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s, opacity 0.2s;
  &:disabled { opacity: 0.6; cursor: not-allowed; }
}
.primary   { background: #6366f1; color: #fff; }
.secondary { background: #e0e7ff; color: #3730a3; }
.danger    { background: #ef4444; color: #fff; }
.outline   { background: transparent; color: #6366f1; border-color: #6366f1; }
.sm { padding: 4px 12px;  font-size: 13px; }
.md { padding: 8px 16px;  font-size: 14px; }
.lg { padding: 12px 24px; font-size: 16px; }
.spinner {
  width: 1em; height: 1em;
  border: 2px solid currentColor; border-right-color: transparent;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
```

Composition và Polymorphic giúp một component "khung" dùng được ở nhiều ngữ cảnh:

```tsx
// components/ui/Card.tsx – Polymorphic + children
import type { ComponentPropsWithoutRef, ElementType, ReactNode } from 'react';

type CardProps<C extends ElementType> = {
  as?: C;
  title?: ReactNode;
  footer?: ReactNode;
  children: ReactNode;
} & Omit<ComponentPropsWithoutRef<C>, 'as' | 'title' | 'children'>;

export function Card<C extends ElementType = 'div'>({ as, title, footer, children, ...rest }: CardProps<C>) {
  const Component: ElementType = as ?? 'div';
  return (
    <Component className="card" {...rest}>
      {title && <header className="card__title">{title}</header>}
      <div className="card__body">{children}</div>
      {footer && <footer className="card__footer">{footer}</footer>}
    </Component>
  );
}

// Sử dụng: <Card as="article" title="Tech Summit 2025" footer={<BuyButton />}>...</Card>
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Ant Design, MUI hay shadcn/ui đều thiết kế `Button` theo đúng mô hình này: một component, nhiều `variant`/`size`, nhận thêm mọi thuộc tính HTML gốc. Khi phòng Marketing đổi màu thương hiệu, nhóm chỉ sửa một file SCSS.

#### 2.6. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

Prompt mẫu cho Guided Practice (Button):

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

Prompt mẫu cho Unguided Practice (Category):

```text
Tạo giúp tôi trang Dynamic Route /category/[slug]/page.tsx trong Next.js 15 App Router.
- Sử dụng params để lấy tên danh mục (music, technology, sports).
- Sử dụng searchParams để lấy thông tin phân trang page và sắp xếp sort.
- Render dữ liệu mock tương ứng với danh mục đó.
- Đảm bảo viết chuẩn TypeScript Interface cho PageProps trong Next.js 15
  (params và searchParams đều là Promise). Không dùng any.
```

Prompt mẫu cho Polymorphic Component:

```text
Viết component Card.tsx dạng Polymorphic (prop "as" nhận ElementType, mặc định "div")
bằng TypeScript strict. Props kế thừa thuộc tính của thẻ được chọn qua
ComponentPropsWithoutRef<C>, có slot title, footer và children. Không dùng any.
```

> **Checklist kiểm duyệt code AI trước khi commit:**
> 1. `params`/`searchParams` có được khai báo là `Promise` và `await` chưa? AI hay sinh `params.id` kiểu Next.js 14.
> 2. Union type có dùng dấu `|` đúng chưa, có lọt `any` hay `as any` không?
> 3. Hook `useSearchParams`/`useParams` chỉ nằm trong file `'use client'`, và đã bọc `<Suspense>`?
> 4. Button có `type="button"` mặc định (tránh vô tình submit form), có `disabled` khi `isLoading`?
> 5. Có trường hợp không tìm thấy dữ liệu → gọi `notFound()` chưa?
> 6. Chạy thử với id sai (`/events/abc`) và query lạ (`?page=xyz`) xem trang có vỡ không.

#### 2.7. Thực hành trên lớp

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Guided Practice | 45' | Tạo `/events/[id]/page.tsx` và `components/ui/Button.tsx` nhiều biến thể; GV cùng SV dùng AI thiết kế `EventCard` nhận props `EventItem` | Đổi `/events/ev-101` → `/events/ev-102` hiển thị đúng sự kiện; Button chạy đúng mọi props |
| Unguided Practice | 45' | Tự xây `/category/[slug]/page.tsx`, đọc `page`, `sort` từ URL, mock data dạng key-value theo slug | Hiển thị được `slug` và `sort` trên giao diện, danh sách lọc đúng danh mục |
| Team Challenge | 60' | Thiết kế `data/mock-events.json` cho toàn hệ thống, nối luồng Trang chủ → Danh mục → Chi tiết → Đặt vé | User Flow liên tục, dữ liệu khớp giữa các màn hình |
| Tổng kết | 15' | GV chữa lỗi điển hình, giải đáp, giao BTVN | SV nắm lỗi thường gặp và yêu cầu bài về nhà |

**Guided (45'):** Tạo route động `/events/[id]` lấy `id` từ `params` (nhớ `await`), tra cứu trong mock data, gọi `notFound()` khi không có. Viết `Button.tsx` hỗ trợ `variant` (primary, secondary, danger, outline), `size` (sm, md, lg), `isLoading`, `leftIcon`. Dùng AI sinh `EventCard` nhận prop `event: EventItem` và đặt vào trang chi tiết.

**Unguided (45'):** Tạo `/category/[slug]/page.tsx` cho các danh mục `music`, `technology`, `sports` (có thể thêm `workshop`). Đọc thông số lọc như `/category/music?page=1&sort=latest`: dùng prop `searchParams` ở Server Component, kết hợp một Client Component dùng `useSearchParams` để đổi cách sắp xếp. Mock data tổ chức dạng `Record<string, { title: string; events: EventItem[] }>`.

**Team Challenge (60'):** Nhóm thống nhất một file `data/mock-events.json` duy nhất. Xây luồng điều hướng: bấm Card ở Trang chủ → `/events/[id]`; bấm Badge thể loại → `/category/[slug]`; bấm "Mua vé" → `/checkout/[id]`. Mỗi thành viên phụ trách một route, merge qua Pull Request.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)
* 🔹 **Dynamic Segment:** `[id]` cho một tham số, `[...slug]` bắt nhiều đoạn (bắt buộc có ít nhất một), `[[...slug]]` cho phép rỗng.
* 🔹 **Next.js 15:** `params` và `searchParams` là `Promise` → luôn `const { id } = await params;`.
* 🔹 **Server vs Client:** Server Component dùng props `params`/`searchParams`; Client Component dùng `useParams`, `useSearchParams` (bọc `Suspense`), `usePathname`, `useRouter`.
* 🔹 **Reusable Component:** mở rộng HTML attributes, dùng union type cho `variant`/`size`, đặt mặc định hợp lý, cho phép ghi đè `className`.
* 🔹 **Composition & Polymorphic:** `children` và prop `as` giúp một component khung phục vụ nhiều ngữ cảnh mà không nhân bản code.
* 🔹 **Tổ chức thư mục:** `components/ui` (nguyên tử) · `components/common` (bố cục chung) · `components/features` (theo nghiệp vụ).

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Trong Next.js 15, cách lấy `id` đúng trong `app/events/[id]/page.tsx` (Server Component) là gì?
- A. `const id = params.id;`
- B. `const { id } = useParams();`
- C. `const { id } = await params;`
- D. `const id = router.query.id;`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Từ Next.js 15, <code>params</code> là Promise nên phải <code>await</code>. <code>useParams</code> chỉ dùng trong Client Component, còn <code>router.query</code> thuộc Pages Router cũ.
</details>

**Câu 2:** Thư mục `app/docs/[...slug]/page.tsx` sẽ KHÔNG khớp với URL nào?
- A. `/docs`
- B. `/docs/a`
- C. `/docs/a/b`
- D. `/docs/huong-dan/dat-ve`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> Catch-all <code>[...slug]</code> cần ít nhất một đoạn sau <code>/docs</code>. Muốn khớp cả <code>/docs</code> phải dùng Optional Catch-all <code>[[...slug]]</code>.
</details>

**Câu 3:** Vì sao nên khai báo `interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>`?
- A. Để Button tự động chuyển thành Server Component
- B. Để Button nhận sẵn mọi thuộc tính HTML gốc như `onClick`, `type`, `disabled`, `aria-*`
- C. Để bắt buộc mọi Button phải có `variant`
- D. Để Next.js tự sinh CSS cho Button

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Kế thừa HTML attributes giúp component dùng như thẻ <code>button</code> thật, không phải khai báo lại từng thuộc tính, đồng thời vẫn được TypeScript kiểm tra kiểu.
</details>

**Câu 4:** Một Client Component cần đọc `?sort=latest` trên URL. Lựa chọn nào đúng?
- A. Dùng `useSearchParams()` và bọc component trong `<Suspense>`
- B. Khai báo prop `searchParams` rồi `await` trong Client Component
- C. Đọc `window.location` trong thân component khi render
- D. Dùng `usePathname()` rồi tách chuỗi sau dấu `?`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> <code>useSearchParams</code> là hook chuẩn cho Client Component. <code>usePathname</code> không chứa query string, còn đọc <code>window</code> khi render gây lỗi trên server và hydration mismatch.
</details>

*Bộ 10+ câu đầy đủ: `quiz/quiz-bai-04-aiken.txt`*

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)
* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Bộ lọc danh mục (sắp xếp, trang hiện tại) nên lưu ở URL (`searchParams`) hay ở state cục bộ (`useState`)? Hãy nêu ít nhất một lợi ích và một bất lợi của mỗi cách, kèm tình huống cụ thể trong Smart Event Hub (ví dụ: người dùng gửi link danh mục cho bạn bè qua Zalo).
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Tổ chức lại toàn bộ thư mục component theo chuẩn: `components/ui/` (Button, Input, Modal, Badge) · `components/common/` (Header, Footer, Sidebar – tương đương `shared` trong đề cương) · `components/features/` (EventCard, SeatPicker, CheckoutForm).
  * Bổ sung ít nhất 3 component nguyên tử còn thiếu (Input, Modal, Badge) có props interface rõ ràng, không `any`.
  * **Output:** Thư mục dự án gọn gàng, không còn code trùng lặp; ảnh chụp cây thư mục dán vào mô tả PR.
  * **Hạn nộp:** trước buổi học tiếp theo. Nộp link Pull Request trên LMS. Đặt tên nhánh `feat/b04-<mssv>-components`, tiêu đề PR `[B04] <Họ tên> – Refactor components`, commit theo Conventional Commits (ví dụ `refactor(ui): move Button to components/ui`).
* **📚 Tài liệu đọc & tham khảo:**
  * Next.js Dynamic Routes Guide: https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes
  * TypeScript Component Props Patterns: https://react-typescript-cheatsheet.netlify.app/docs/basic/getting-started/basic_type_example/
  * Next.js – `useSearchParams`: https://nextjs.org/docs/app/api-reference/functions/use-search-params
  * **Câu hỏi tự kiểm tra khi đọc:** (1) Làm thế nào để lấy Query Parameters (`?category=music`) trong một Client Component và trong một Server Component? (2) Tại sao nên mở rộng Props Component từ HTML Native Attributes (ví dụ `ButtonHTMLAttributes<HTMLButtonElement>`)?
