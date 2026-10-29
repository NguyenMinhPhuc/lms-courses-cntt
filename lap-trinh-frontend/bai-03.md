# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 2: NEXT.JS CORE – ROUTING & KIẾN TRÚC COMPONENT
### Bài 03: Next.js App Router: cấu trúc thư mục, Index & Nested Routing

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Lớp học đảo ngược · **Chuẩn đầu ra:** PI 2.3 (CLO2)
> **Dự án xuyên suốt:** Smart Event Hub – Thiết lập kiến trúc thư mục App Router, Layout chung, Route Groups (auth), (admin) và trang 404.

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Giải thích được vai trò các file đặc biệt `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`; phân biệt Server Component và Client Component, SSR và CSR.
> * **[Bloom 3/4 - Kỹ năng]:** Xây dựng Index Route, Nested Route, Route Groups và điều hướng bằng `next/link` cho dự án Smart Event Hub.
> * **[Bloom 5/6 - Năng lực]:** Thiết kế và đánh giá cấu trúc thư mục App Router cho nhiều Layout (site chính, auth, admin), có xử lý Loading, Error, 404 và bảo vệ Private Routes.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Sau hai buổi, nhóm các bạn đã có bộ component và 5 trang dàn tĩnh trong `/dev-preview`. Bây giờ khách hàng muốn trang Đăng nhập chỉ có logo và form ở giữa màn hình, không có menu; khu Quản trị phải có Sidebar riêng; còn người dùng gõ sai đường dẫn thì không được thấy trang trắng. Nếu mỗi trang tự import Header, Footer, Sidebar, các bạn sẽ phải sửa hàng chục file mỗi khi đổi menu.

Vậy Next.js tổ chức thư mục thế nào để **một thay đổi ở Layout áp dụng cho đúng nhóm trang**, mà URL vẫn gọn gàng như `/login`, `/admin/dashboard`? Buổi học này giải quyết bài toán đó bằng App Router.

> 🧭 **Trước giờ học (Flipped Classroom):**
> * Xem video Next.js App Router architecture (`page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`).
> * Đọc Next.js Routing Docs và React Server Components Guide ở mục 5.
> * Cài Node.js LTS, thử chạy `npx create-next-app@latest` tại nhà; làm Quiz nhanh 5–10 câu trên LMS.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Kiến trúc App Router & các file đặc biệt

* **Khái niệm:** App Router dùng **directory-based routing**: mỗi thư mục trong `app/` là một đoạn URL (segment), và thư mục chỉ trở thành route truy cập được khi có file `page.tsx`.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `page.tsx`: giao diện duy nhất của một route. `app/page.tsx` là **Index Route** `/`.
  * `layout.tsx`: giao diện bọc chung, **không bị re-render** khi chuyển giữa các trang con, giữ nguyên state (ví dụ ô tìm kiếm trên Header). `app/layout.tsx` (Root Layout) bắt buộc có thẻ `<html>` và `<body>`.
  * `loading.tsx`: UI chờ (Skeleton) hiển thị tức thì trong lúc trang đang tải, dựa trên React Suspense.
  * `error.tsx`: Error Boundary bắt lỗi runtime của route, **bắt buộc là Client Component**.
  * `not-found.tsx`: trang 404. `global-error.tsx`: bắt lỗi xảy ra ngay trong Root Layout.

```tsx
// app/layout.tsx – Root Layout: chỉ chứa html/body và style toàn cục
import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import './globals.scss';

export const metadata: Metadata = {
  title: 'Smart Event Hub',
  description: 'Hệ thống đặt vé & quản lý sự kiện trực tuyến',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="vi">
      <body>{children}</body>
    </html>
  );
}
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Người dùng đang gõ từ khóa trong ô tìm kiếm trên Header rồi bấm sang trang Sự kiện. Vì Header nằm trong `layout.tsx`, nó không bị render lại, nên từ khóa vẫn còn nguyên; nếu Header đặt trong từng `page.tsx`, ô tìm kiếm sẽ bị xóa trắng mỗi lần chuyển trang.

#### 2.2. Server Components (RSC) và Client Components

* **Khái niệm:** Mặc định **mọi component trong `app/` là Server Component**: render hoàn toàn trên server, không gửi JavaScript của nó về trình duyệt. Client Component được đánh dấu bằng chỉ thị `'use client'` ở dòng đầu file.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Server Component giảm kích thước bundle, gọi dữ liệu trực tiếp trên server (sẽ học ở Bài 08) và giữ bí mật API key.
  * **Bắt buộc `'use client'`** khi component cần: sự kiện người dùng (`onClick`, `onChange`), React Hooks (`useState`, `useEffect`, `usePathname`) hoặc Browser APIs (`window`, `localStorage`).
  * Chiến lược tốt: giữ trang là Server Component, chỉ tách **phần nhỏ cần tương tác** thành Client Component.
  * Liên hệ cơ chế render: Server Component tương ứng tư duy **SSR** (HTML tạo sẵn trên server), còn phần tương tác chạy theo **CSR** (JavaScript thực thi trên trình duyệt).

| Tiêu chí | Server Component | Client Component (`'use client'`) |
|---|---|---|
| Nơi render | Server | Server (HTML ban đầu) + trình duyệt (hydrate) |
| Dùng Hooks, onClick | Không | Có |
| Gọi dữ liệu trực tiếp, dùng secret | Có | Không nên |
| JavaScript gửi về client | Không | Có |

```tsx
// app/(main)/events/page.tsx – Server Component
import ClientFilter from './ClientFilter';

export default async function EventsPage() {
  // Có thể fetch dữ liệu trực tiếp trên server tại đây (Bài 08)
  return (
    <section>
      <h1>Tất cả sự kiện</h1>
      <ClientFilter />
    </section>
  );
}
```

```tsx
// app/(main)/events/ClientFilter.tsx – Client Component
'use client';

import { useState } from 'react';

const CATEGORIES = ['Tất cả', 'Âm nhạc', 'Công nghệ', 'Workshop'] as const;
type Category = (typeof CATEGORIES)[number];

export default function ClientFilter() {
  const [active, setActive] = useState<Category>('Tất cả');

  return (
    <div role="group" aria-label="Lọc theo thể loại">
      {CATEGORIES.map((category) => (
        <button key={category} type="button" aria-pressed={active === category} onClick={() => setActive(category)}>
          {category}
        </button>
      ))}
    </div>
  );
}
```

#### 2.3. Routing System: Index, Nested, Route Groups & Private Routes

* **Khái niệm:** Hệ thống route được suy ra từ cây thư mục. Thư mục lồng nhau tạo **Nested Route** (`/events/categories`); thư mục có ngoặc tròn `(group)` tạo **Route Group**, gom trang dùng chung Layout mà **không xuất hiện trên URL**.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Index Route:** `app/(main)/page.tsx` → `/`; `app/(main)/events/page.tsx` → `/events`.
  * **Nested Route & Nested Layout:** `events/categories/page.tsx` → `/events/categories`; nếu có `events/layout.tsx`, nó bọc mọi trang con của `/events`.
  * **Route Groups:** `(auth)/login/page.tsx` vẫn là `/login`. Mỗi group có `layout.tsx` riêng; file phải tên là `layout.tsx`, còn tên hàm có thể là `AuthLayout`.
  * **Lưu ý quan trọng:** Layout lồng nhau **cộng dồn** chứ không thay thế. Nếu đặt Header/Footer trong Root Layout, trang `(auth)` vẫn hiện Header. Vì vậy, Header/Footer được đặt trong group `(main)`, còn Root Layout chỉ chứa `html`/`body`.

```text
app/
├── layout.tsx                  Root Layout (html, body) – không Header/Footer
├── not-found.tsx               404 tùy chỉnh
├── global-error.tsx            Bắt lỗi ở mức Root Layout
├── (main)/
│   ├── layout.tsx              Header + Footer chung
│   ├── page.tsx                /
│   ├── error.tsx               Error Boundary cho site chính
│   └── events/
│       ├── page.tsx            /events
│       ├── categories/page.tsx /events/categories
│       └── search/page.tsx     /events/search
├── (auth)/
│   ├── layout.tsx              AuthLayout: Logo + Form giữa màn hình
│   ├── login/page.tsx          /login
│   └── register/page.tsx       /register
└── (admin)/
    ├── layout.tsx              AdminLayout: Sidebar trái + Header Admin
    └── admin/
        ├── loading.tsx         Skeleton khi chuyển trang Admin
        ├── dashboard/page.tsx          /admin/dashboard
        ├── events-management/page.tsx  /admin/events-management
        └── users/page.tsx              /admin/users
```

```tsx
// app/(auth)/layout.tsx
import type { ReactNode } from 'react';
import Link from 'next/link';
import styles from './auth.module.scss';

export default function AuthLayout({ children }: { children: ReactNode }) {
  return (
    <main className={styles.authWrapper}>
      <Link href="/" className={styles.logo}>Smart Event Hub</Link>
      <div className={styles.formCard}>{children}</div>
    </main>
  );
}
```

* **Private Routes:** các trang `/admin/*`, `/user/*` chỉ dành cho người đã đăng nhập. Trong Next.js 15, cách gọn nhất là dùng `middleware.ts` ở thư mục gốc để chuyển hướng trước khi trang được render:

```ts
// middleware.ts
import { NextResponse, type NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('access_token')?.value;
  if (!token) {
    const loginUrl = new URL('/login', request.url);
    loginUrl.searchParams.set('redirect', request.nextUrl.pathname);
    return NextResponse.redirect(loginUrl);
  }
  return NextResponse.next();
}

export const config = { matcher: ['/admin/:path*', '/user/:path*'] };
```

> Ở buổi này `access_token` chỉ là cookie giả lập để thử luồng chuyển hướng. Việc lưu token thật sau khi gọi API Login sẽ được làm ở Bài 09.

#### 2.4. Điều hướng, Loading, Error & 404

* **Khái niệm:** `Link` từ `next/link` chuyển trang phía client, **không reload toàn trang** và tự prefetch route khi link xuất hiện trong khung nhìn. Thẻ `<a href>` thường sẽ tải lại toàn bộ ứng dụng.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Đánh dấu menu đang active cần `usePathname()`, nên Sidebar Admin hoặc NavLink phải là Client Component.
  * `loading.tsx` đặt cùng cấp với `page.tsx` sẽ bọc trang đó và các trang con.
  * `error.tsx` nhận `error` và hàm `reset()` để thử render lại; `global-error.tsx` phải tự khai báo `<html>` và `<body>` vì nó thay thế cả Root Layout.

```tsx
// app/(admin)/admin/loading.tsx – Skeleton đơn giản
import styles from './admin.module.scss';

export default function AdminLoading() {
  return (
    <div className={styles.skeletonList} aria-busy="true" aria-label="Đang tải">
      {Array.from({ length: 4 }, (_, i) => (
        <div key={i} className={styles.skeletonRow} />
      ))}
    </div>
  );
}
```

```tsx
// app/not-found.tsx
import Link from 'next/link';

export default function NotFound() {
  return (
    <main style={{ textAlign: 'center', padding: '80px 16px' }}>
      <h1>404 – Không tìm thấy trang</h1>
      <p>Sự kiện bạn tìm có thể đã kết thúc hoặc đường dẫn không đúng.</p>
      <Link href="/">Quay lại trang chủ</Link>
    </main>
  );
}
```

```tsx
// app/(main)/error.tsx – bắt buộc là Client Component
'use client';

import { useEffect } from 'react';

export default function ErrorBoundary({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  useEffect(() => {
    console.error(error); // thay bằng dịch vụ ghi log khi triển khai thật
  }, [error]);

  return (
    <section role="alert">
      <h2>Đã có lỗi xảy ra</h2>
      <p>Xin lỗi vì sự bất tiện. Vui lòng thử lại.</p>
      <button type="button" onClick={() => reset()}>Thử lại (Try Again)</button>
    </section>
  );
}
```

> Ví dụ `not-found.tsx` dùng inline style cho ngắn gọn; trong dự án, hãy chuyển sang SCSS Module như đã thống nhất ở Bài 02.

#### 2.5. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

AI rất nhanh trong việc sinh cây thư mục theo Clean Architecture, nhưng hay mắc lỗi với các phiên bản Next.js cũ (thư mục `pages/`, `getServerSideProps`, `next/router`). Prompt Guided:

```text
Hãy hướng dẫn tạo cấu trúc thư mục Next.js App Router cho dự án "Smart Event Hub" với các yêu cầu:
1. Root Layout chứa Header và Footer chung.
2. Route Group (auth) có AuthLayout riêng (chỉ chứa Logo và Form ở trung tâm màn hình) cho các trang /login và /register.
3. Nested Route /events và /events/categories.
Hãy cho tôi sơ đồ cây thư mục chi tiết và nội dung mã nguồn của các file layout.tsx tương ứng.
Ràng buộc: Next.js 15 App Router, TypeScript strict, không dùng thư mục pages/.
```

> **Bài tập phản biện:** yêu cầu số 1 trong prompt trên sẽ khiến trang `/login` vẫn hiện Header. Hãy xem AI có phát hiện ra không; nếu không, sửa lại theo cấu trúc group `(main)` ở mục 2.3.

* **Checklist kiểm duyệt code AI:**
  * Có dùng nhầm API cũ: `pages/`, `next/router`, `getServerSideProps`, `next/head`?
  * Tên file đặc biệt đúng chưa (`layout.tsx`, không phải `AuthLayout.tsx`)? Root Layout có `<html>`, `<body>`?
  * `'use client'` chỉ đặt ở file thật sự cần hook/sự kiện, không gắn bừa lên mọi trang?
  * `error.tsx` có `'use client'`; `global-error.tsx` có `<html>`/`<body>`?
  * Menu dùng `Link` từ `next/link` thay vì `<a href>`; gõ thử `/abc-xyz` ra đúng trang 404?

#### 2.6. Thực hành trên lớp

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Guided Practice | 45 phút | Khởi tạo dự án Next.js, Layout chung có Header/Footer, Route Group (auth) và Nested Route /events | Chuyển route trơn tru; trang (auth) dùng AuthLayout riêng |
| Unguided Practice | 45 phút | Xây khu Quản trị với Route Group (admin), AdminLayout có Sidebar, `loading.tsx` Skeleton | /admin/dashboard có layout riêng, Skeleton khi chuyển trang |
| Team Challenge | 60 phút | Tích hợp route của cả nhóm vào `main`, Navigation dùng `next/link`, trang 404 tùy chỉnh | Sơ đồ Routing hoàn chỉnh; /abc-xyz hiện đúng 404 |
| Tổng kết | 15 phút | Rà lỗi cấu trúc thư mục phổ biến, giao BTVN | Mỗi nhóm có danh sách route đã chốt |

**Guided (45'):** chạy lệnh khởi tạo, chọn TypeScript, ESLint, App Router, thư mục `src/` tùy nhóm, alias `@/*`. Tạo group `(main)` chứa Header/Footer, group `(auth)` với `/login`, `/register`, và Nested Route `/events/categories`, `/events/search`.

```bash
npx create-next-app@latest smart-event-hub --typescript --eslint --app
cd smart-event-hub && npm install -D sass && npm run dev
```

> `create-next-app` sinh sẵn `app/page.tsx`. Hãy chuyển file này vào `app/(main)/page.tsx`; nếu để cả hai, Next.js báo lỗi vì hai trang cùng trỏ tới `/`.

**Unguided (45'):** xây khu Quản trị với Route Group `(admin)` tại `/admin/dashboard`, `/admin/events-management`, `/admin/users`. `AdminLayout` có Sidebar trái để chuyển trang, thêm `loading.tsx` hiển thị Skeleton. Nhóm nào xong sớm bổ sung `/checkout` và `/user/profile`. Prompt gợi ý:

```text
Tạo giúp tôi cấu trúc Route Group (admin) trong Next.js App Router.
- AdminLayout: Gồm Sidebar bên trái (Dashboard, Quản lý sự kiện, Quản lý người dùng) và Header Admin ở trên.
- Tạo file loading.tsx sử dụng hiệu ứng Skeleton UI đơn giản bằng SCSS/Tailwind.
- Viết bằng TypeScript.
```

**Team Challenge (60'):** tích hợp toàn bộ route của từng cá nhân vào nhánh `main` qua Pull Request. Đảm bảo `HeaderNavigationBar` (Bài 01) dùng `Link` của `next/link` để điều hướng tới mọi route mà không reload trang. Xây `not-found.tsx` thân thiện có nút "Quay lại trang chủ"; kiểm tra bằng cách gõ `/abc-xyz`.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)

* 🔹 **Thư mục = URL, `page.tsx` = route:** thư mục không có `page.tsx` không truy cập được.
* 🔹 **Layout cộng dồn và không re-render:** Root Layout chỉ giữ `html`/`body`; Header/Footer đặt trong group `(main)`.
* 🔹 **Route Groups `(name)`:** tách Layout cho site chính, auth, admin mà không đổi URL.
* 🔹 **Server Component mặc định:** chỉ thêm `'use client'` khi cần hooks, sự kiện hoặc Browser API.
* 🔹 **Đủ trạng thái giao diện:** `loading.tsx`, `error.tsx` (Client), `not-found.tsx`, `global-error.tsx`; Private Routes chặn bằng `middleware.ts`.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** File `app/(auth)/login/page.tsx` tương ứng với URL nào?
- A. `/auth/login`
- B. `/(auth)/login`
- C. `/login`
- D. `/auth`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Thư mục trong ngoặc tròn là Route Group, chỉ dùng để tổ chức và gán Layout, không xuất hiện trên URL.
</details>

**Câu 2:** Component nào sau đây **bắt buộc** có `'use client'`?
- A. Trang hiển thị danh sách sự kiện tĩnh
- B. Nút "Yêu thích" dùng `useState` và `onClick`
- C. Root Layout chứa thẻ `<html>`
- D. Trang `not-found.tsx` chỉ có chữ và `Link`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Hooks và sự kiện người dùng chỉ chạy trong Client Component. Các trường hợp còn lại giữ là Server Component để giảm JavaScript gửi về trình duyệt.
</details>

**Câu 3:** Nhóm đặt Header/Footer trong `app/layout.tsx` rồi tạo `app/(auth)/layout.tsx`. Kết quả khi mở `/login` là gì?
- A. Trang `/login` vẫn hiện Header/Footer vì Layout lồng nhau cộng dồn
- B. AuthLayout thay thế hoàn toàn Root Layout
- C. Next.js báo lỗi vì có hai file `layout.tsx`
- D. Trang `/login` trả về 404

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> Layout con được render bên trong Layout cha. Muốn trang auth không có Header, hãy chuyển Header/Footer vào một group riêng như <code>(main)</code>.
</details>

**Câu 4:** Điều nào đúng về file `error.tsx` trong App Router?
- A. Là Server Component và chỉ bắt lỗi 404
- B. Phải khai báo `<html>` và `<body>`
- C. Chỉ hoạt động khi đặt trong thư mục `pages/`
- D. Phải là Client Component, nhận `error` và hàm `reset()`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> <code>error.tsx</code> là Error Boundary nên cần <code>'use client'</code>. Thẻ <code>&lt;html&gt;</code>, <code>&lt;body&gt;</code> chỉ bắt buộc ở <code>global-error.tsx</code>.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-03-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)

* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Hãy chia sẻ cây thư mục `app/` của nhóm bạn. Nhóm đã dùng những Route Group nào, vì sao? Có trang nào các bạn phân vân giữa Server Component và Client Component không? Đề xuất cách tách phần tương tác ra khỏi trang để giữ phần còn lại là Server Component.
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Tạo `error.tsx` (Client Component) xử lý lỗi ngoại lệ cho các nhóm route và `global-error.tsx` bắt lỗi ở mức Root Layout.
  * Bổ sung `loading.tsx` dạng Skeleton UI cho từng nhóm route đã tạo (`(main)`, `(auth)`, `(admin)`), hoàn thiện trang 404.
  * **Output:** khi ứng dụng gặp sự cố runtime (thử `throw new Error('test')` trong một trang), màn hình hiển thị thông báo lỗi văn minh kèm nút "Thử lại (Try Again)".
  * **Hạn nộp:** trước buổi học tiếp theo; Pull Request cá nhân vào nhánh `dev`, kèm ảnh chụp màn hình trang lỗi và trang 404; nộp link PR lên LMS.
  * **Quy tắc đặt tên:** nhánh `feature/<ho-ten-khong-dau>-error-handling`, commit theo dạng `feat(routing): add error and loading boundaries`.
* **📚 Tài liệu đọc & tham khảo:**
  * Next.js App Router Routing Docs: https://nextjs.org/docs/app/building-your-application/routing
  * React Server Components Conceptual Guide: https://react.dev/reference/rsc/server-components
  * React – `'use client'` directive: https://react.dev/reference/rsc/use-client
  * Next.js File Conventions: https://nextjs.org/docs/app/api-reference/file-conventions
  * **Câu hỏi tự kiểm tra khi đọc:** Khi nào bắt buộc phải thêm `'use client'` vào đầu tệp component? Lợi ích của Route Groups `(group_name)` trong việc tổ chức Layout dự án là gì?
