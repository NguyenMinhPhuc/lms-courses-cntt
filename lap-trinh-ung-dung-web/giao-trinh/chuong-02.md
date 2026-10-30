# Chương 2. Routing, layout và giao diện với Tailwind CSS

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Phân tích chức năng của ứng dụng thành sơ đồ chức năng, sitemap và bảng ánh xạ route – chức năng – vai trò – API.
- Tổ chức route bằng thư mục, route group và route động của App Router.
- Dùng các file đặc biệt `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`.
- Xây dựng layout riêng cho khu vực khách và khu vực quản trị.
- Xây dựng giao diện responsive bằng Tailwind CSS và component shadcn/ui.

## 2.1. Phân tích trước khi code

### 2.1.1. Sơ đồ chức năng

Sơ đồ chức năng (functional decomposition) chia hệ thống thành các khu vực lớn, mỗi khu vực thành các chức năng nhỏ hơn, tới mức một chức năng ứng với một hoặc vài user story. Với phần web LHU Food, cấp đầu tiên lấy từ các module trong SRS mục 5.1:

```text
Web LHU Food
├── Khu vực khách        (M02 Thực đơn, M03 Giỏ hàng, M04 Đơn hàng, M01 Tài khoản)
│   ├── Xem thực đơn, tìm món, xem chi tiết món
│   ├── Giỏ hàng, đặt món
│   └── Đơn của tôi, hồ sơ
├── Màn hình quầy        (M09 Vận hành của nhân viên)
│   ├── Danh sách đơn theo trạng thái
│   ├── Chuyển trạng thái, hủy đơn có lý do
│   └── Bật/tắt món còn bán, cập nhật tồn kho
└── Quản trị             (M10 Báo cáo, M11 Quản trị)
    ├── Danh mục, món, quầy
    ├── Tài khoản nhân viên
    └── Báo cáo doanh thu, món bán chạy
```

### 2.1.2. Sitemap và bảng ánh xạ route

**Sitemap** là sơ đồ các trang và quan hệ cha – con giữa chúng; nó cho thấy người dùng đi từ đâu tới đâu. Từ sitemap, lập **bảng ánh xạ** cho mỗi trang: đường dẫn, chức năng (user story), vai trò được vào và API cung cấp dữ liệu. SRS mục 5.14.2 liệt kê các màn hình web, mục 8 liệt kê API.

| Chức năng (SRS) | Route | Vai trò | API |
|---|---|---|---|
| Xem thực đơn (US-G01, G02) | `/menu` | Mọi người | `GET /categories`, `GET /products` |
| Chi tiết món (US-G03) | `/product/[id]` | Mọi người | `GET /products/:id` |
| Giỏ hàng (US-C01, C02) | `/cart` | Mọi người (đặt món cần đăng nhập) | Không gọi API |
| Đặt món (US-C04) | `/checkout` | customer | `POST /orders` |
| Màn hình quầy (US-S02, S03) | `/admin/orders` | staff, admin | `GET /orders/staff`, `PATCH /orders/:id/status` |
| Quản lý món (US-A02) | `/admin/products` | admin | `/admin/products` |

Bảng ánh xạ là minh chứng chính của CLO1 trong báo cáo (Chương 3 của báo cáo đồ án) và là đầu vào cho ma trận phân quyền ở Chương 5. Lập bảng trước khi tạo thư mục giúp nhóm phát hiện sớm trang thừa, trang thiếu và API chưa có.

## 2.2. Routing của App Router

### 2.2.1. Cây thư mục của LHU Food

Từ bảng ánh xạ, cây thư mục `app/` gần như được suy ra trực tiếp [1]:

```text
app/
├── layout.tsx                 layout gốc
├── not-found.tsx              trang 404
├── (shop)/                    route group: không xuất hiện trong URL
│   ├── layout.tsx             header cho khách
│   ├── menu/page.tsx          /menu
│   ├── product/[id]/page.tsx  /product/12   (route động)
│   └── cart/page.tsx          /cart
└── admin/
    ├── layout.tsx             sidebar quản trị
    ├── page.tsx               /admin        (tổng quan)
    ├── orders/page.tsx        /admin/orders
    └── products/page.tsx      /admin/products
```

### 2.2.2. Route group

Thư mục có tên trong ngoặc tròn, như `(shop)`, là **route group**: nó gom các trang dùng chung một layout nhưng **không** xuất hiện trong đường dẫn. `app/(shop)/menu/page.tsx` hiển thị ở `/menu`, không phải `/shop/menu` [2]. Route group cho phép khu vực khách có header riêng, khu vực quản trị có sidebar riêng, dù cả hai ở cùng cấp đường dẫn. Lưu ý: hai route group không được chứa hai trang ra cùng một đường dẫn, Next.js sẽ báo lỗi.

### 2.2.3. Route động

Thư mục tên trong ngoặc vuông, như `[id]`, là **route động**: một file phục vụ mọi đường dẫn `/product/1`, `/product/12`… Giá trị được truyền vào trang qua `params`. Từ Next.js 15, `params` là `Promise` nên phải `await` [3]:

```tsx
// app/(shop)/product/[id]/page.tsx
import { notFound } from 'next/navigation';
import { mockProducts } from '@/lib/mock';

export default async function ProductPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const product = mockProducts.find((p) => p.id === Number(id));
  if (!product) notFound();               // hiển thị not-found.tsx
  return <h1 className="text-2xl font-bold">{product.name}</h1>;
}
```

Tham số trên URL luôn là **chuỗi**: so sánh với mã món kiểu số phải chuyển kiểu (`Number(id)`). Mã không tồn tại thì gọi `notFound()` để hiển thị trang 404, không để trang vỡ.

### 2.2.4. Các file đặc biệt

| File | Vai trò | Ghi chú |
|---|---|---|
| `layout.tsx` | Bọc các trang con, giữ nguyên khi chuyển trang con | Layout gốc bắt buộc có `<html>`, `<body>` |
| `page.tsx` | Nội dung trang tại đường dẫn | Không có `page.tsx` thì thư mục không thành đường dẫn |
| `loading.tsx` | Giao diện chờ khi trang đang lấy dữ liệu | Dùng ở Chương 3 |
| `error.tsx` | Giao diện khi trang gặp lỗi | Bắt buộc là Client Component |
| `not-found.tsx` | Trang 404 | Hiện khi gọi `notFound()` hoặc đường dẫn không tồn tại |

### 2.2.5. Điều hướng

Dùng component `Link` của Next.js thay cho thẻ `<a>`: `Link` tải trước trang đích khi liên kết xuất hiện trên màn hình và chuyển trang mà không tải lại toàn bộ [4]. Trong Client Component, chuyển trang bằng mã qua `useRouter()` (`router.push('/cart')`).

## 2.3. Layout dùng chung và cây component

### 2.3.1. Layout quản trị

```tsx
// app/admin/layout.tsx
import Link from 'next/link';

const MENU = [
  { href: '/admin', label: 'Tổng quan' },
  { href: '/admin/orders', label: 'Màn hình quầy' },
  { href: '/admin/products', label: 'Món ăn' },
];

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen">
      <aside className="hidden w-60 bg-blue-950 p-4 text-white md:block">
        <p className="mb-6 font-bold">LHU Food · Quản trị</p>
        <nav className="space-y-1">
          {MENU.map((m) => (
            <Link key={m.href} href={m.href} className="block rounded px-3 py-2 hover:bg-blue-800">
              {m.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="flex-1 bg-slate-50 p-6">{children}</main>
    </div>
  );
}
```

- Sidebar ẩn trên điện thoại (`hidden`), hiện từ màn hình vừa (`md:block`). Trên điện thoại cần một nút mở menu (bài tập cuối chương).
- Layout **không vẽ lại** khi chuyển giữa các trang con: trạng thái của sidebar giữ nguyên, trang chuyển nhanh.
- Đặt tiêu đề từng trang bằng `export const metadata = { title: 'Món ăn | LHU Food' }` trong `page.tsx`.

### 2.3.2. Cây component

Mỗi trang được chia thành component theo trách nhiệm. Cây component cho trang thực đơn:

```text
RootLayout
└── ShopLayout (header, giỏ hàng)
    └── MenuPage
        ├── SearchBox
        ├── CategoryTabs
        └── ProductGrid
            └── ProductCard × n
                └── AddToCartButton
```

Cây component là một phần của phân tích thành phần (CLO1). Chương 3 và 4 đánh dấu trên cây này component nào chạy ở server, component nào ở client. Vẽ lại cây cho các trang chính của nhóm và lưu trong `docs/`.

## 2.4. Tailwind CSS

### 2.4.1. Utility class

Tailwind CSS viết giao diện bằng các **utility class** ngay trong JSX thay vì viết file CSS riêng [5]. Mỗi class làm một việc nhỏ:

| Class | Ý nghĩa |
|---|---|
| `p-4`, `px-3`, `mt-2` | padding 1rem, padding ngang 0,75rem, margin trên 0,5rem |
| `text-xl font-bold text-blue-900` | cỡ chữ, độ đậm, màu chữ |
| `bg-white rounded-xl border` | nền, bo góc, viền |
| `flex gap-2`, `grid grid-cols-3` | bố cục flex, lưới |

### 2.4.2. Mobile-first và responsive

Tailwind thiết kế theo hướng **mobile-first**: class không có tiền tố áp dụng cho mọi kích thước; tiền tố `sm:`, `md:`, `lg:` áp dụng **từ kích thước đó trở lên** [6]. Ví dụ lưới món:

```tsx
<ul className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
  {products.map((p) => <ProductCard key={p.id} product={p} />)}
</ul>
```

Điện thoại thấy 1 cột, máy tính bảng 2 cột, máy tính 3 cột. Luôn kiểm tra giao diện ở ba kích thước bằng chế độ thiết bị của DevTools.

### 2.4.3. Lưu ý khi viết class

Tailwind quét mã nguồn để tìm các class được dùng. Vì vậy **viết đủ tên class**, không ghép chuỗi động:

```tsx
// Sai: Tailwind không thấy class "bg-green-100" trong mã
<span className={`bg-${color}-100`}>...</span>

// Đúng: liệt kê đủ tên class
const STATUS_CLASS = { ready: 'bg-green-100 text-green-800', pending: 'bg-amber-100 text-amber-800' };
<span className={STATUS_CLASS[status]}>...</span>
```

## 2.5. shadcn/ui

### 2.5.1. Khác thư viện UI thông thường

shadcn/ui không phải thư viện cài vào `node_modules` rồi dùng. Công cụ của nó **chép mã nguồn component** vào thư mục `components/ui/` của dự án [7]. Nhóm sở hữu và sửa được mã đó theo nhận diện LHU. Các component dựa trên Radix UI nên đã xử lý sẵn bàn phím và trình đọc màn hình.

```bash
npx shadcn@latest init                          # cấu hình cho dự án
npx shadcn@latest add button card table dialog  # chép các component cần dùng
```

Trong LHU Food: `Card` cho thẻ món, `Table` cho danh sách quản trị, `Dialog` và `AlertDialog` cho xác nhận, `Button` cho mọi nút.

### 2.5.2. Từ Figma đến mã bằng vibe coding

Thiết kế giao diện đã làm ở học phần Thiết kế UI/UX là đầu vào. Quy trình chuyển thiết kế thành mã:

1. Chụp màn hình thiết kế Figma của trang.
2. Đưa cho AI: ảnh thiết kế, dòng tương ứng trong bảng ánh xạ route, file `AGENTS.md`.
3. Yêu cầu dùng component shadcn/ui đã có và class Tailwind, không viết CSS riêng, không thêm thư viện UI khác.
4. Kiểm tra: màu, khoảng cách khớp thiết kế; responsive ở ba kích thước; không có thư viện lạ trong `package.json`.

## Tóm tắt chương

- Phân tích trước khi code: sơ đồ chức năng → sitemap → bảng ánh xạ route – chức năng – vai trò – API.
- App Router: thư mục là đường dẫn, `(nhóm)` không vào URL, `[id]` là route động; `params` là `Promise` từ Next.js 15.
- Các file đặc biệt: `layout`, `page`, `loading`, `error` (Client Component), `not-found`.
- Layout giữ nguyên khi chuyển trang con; mỗi khu vực có layout riêng; cây component là một phần phân tích thành phần.
- Tailwind CSS: utility class, mobile-first, viết đủ tên class; shadcn/ui chép mã component vào dự án.

## Câu hỏi ôn tập

1. Bảng ánh xạ route – chức năng – vai trò – API dùng cho những việc gì trong dự án?
2. Vì sao `app/(shop)/menu/page.tsx` hiển thị ở `/menu` mà không phải `/shop/menu`?
3. Tham số `id` của route động có kiểu gì? Viết đoạn mã đọc tham số đúng với Next.js 15.
4. Khi nào nên gọi `notFound()`?
5. Class `md:grid-cols-3` có tác dụng ở kích thước màn hình nào?
6. Vì sao không nên ghép tên class Tailwind bằng chuỗi động như `text-${color}-600`?
7. shadcn/ui khác một thư viện UI cài qua npm ở điểm nào?

## Bài tập

1. **Bảng ánh xạ.** Lập bảng ánh xạ đầy đủ cho khu vực khách và màn hình quầy theo SRS mục 5.14.2 và mục 8.
2. **Menu quản trị trên điện thoại.** Thêm nút mở sidebar trên điện thoại cho layout quản trị (dùng `Sheet` của shadcn/ui).
3. **Trang quầy.** Tạo `/counters` và `/counters/[id]` với dữ liệu giả, `id` sai hiển thị trang 404.

## Tài liệu tham khảo

[1] Vercel, “Layouts and Pages,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/layouts-and-pages

[2] Vercel, “Route Groups,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/route-groups

[3] Vercel, “Dynamic Route Segments,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes

[4] Vercel, “Linking and Navigating,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/linking-and-navigating

[5] Tailwind Labs, “Styling with utility classes,” *Tailwind CSS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://tailwindcss.com/docs/styling-with-utility-classes

[6] Tailwind Labs, “Responsive design,” *Tailwind CSS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://tailwindcss.com/docs/responsive-design

[7] shadcn, “Installation: Next.js,” *shadcn/ui Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://ui.shadcn.com/docs/installation/next
