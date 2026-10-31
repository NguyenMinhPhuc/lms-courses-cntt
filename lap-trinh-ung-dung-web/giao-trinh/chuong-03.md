# Chương 3. Server Components và lấy dữ liệu từ API

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Phân biệt Server Component và Client Component, xác định ranh giới `"use client"` trên một trang.
- Lấy dữ liệu từ API trong Server Component với biến môi trường và kiểu TypeScript.
- Chọn cách cache và thời gian `revalidate` phù hợp với mức thay đổi của dữ liệu.
- Xử lý trạng thái tải, lỗi và rỗng bằng `loading.tsx`, `Suspense`, `error.tsx`.
- Viết test case từ tiêu chí chấp nhận, viết báo cáo sprint và lập kế hoạch sprint tiếp theo.

## 3.1. Server Component và Client Component

### 3.1.1. So sánh

| | Server Component (mặc định) | Client Component (`"use client"`) |
|---|---|---|
| Chạy ở đâu | Server (lúc build hoặc mỗi request) | Server lần đầu (tạo HTML) rồi trình duyệt |
| Dùng được | `async/await`, biến môi trường bí mật, gọi API trực tiếp | `useState`, `useEffect`, sự kiện, API trình duyệt |
| Gửi xuống trình duyệt | Chỉ kết quả render, không gửi mã | Mã JavaScript của component |
| Ví dụ LHU Food | Trang thực đơn, chi tiết món | Nút "Thêm vào giỏ", bộ lọc có hiệu ứng |

Server Component giảm lượng JavaScript trình duyệt phải tải, giữ bí mật (khóa API, địa chỉ nội bộ) ở server và lấy dữ liệu gần nguồn hơn [1].

### 3.1.2. Ranh giới "use client"

Chỉ thị `"use client"` ở đầu file đánh dấu **ranh giới**: file đó và mọi component nó import đều trở thành Client Component. Vì vậy:

- Đặt `"use client"` ở **lá** của cây component (component nhỏ cần tương tác), không đặt ở page hay layout.
- Server Component có thể render Client Component và truyền props cho nó. Props phải tuần tự hóa được: số, chuỗi, mảng, object thường; không truyền hàm.
- Client Component có thể nhận Server Component qua `children`, nhờ vậy một khung tương tác vẫn bọc được nội dung render trên server.

Trên cây component của Chương 2, đánh dấu từng nút là S (server) hoặc C (client) và ghi lý do. Đó là phần "thiết kế component" trong báo cáo (CLO1).

## 3.2. Lấy dữ liệu từ API

### 3.2.1. Biến môi trường

Địa chỉ API đặt trong file `.env.local` ở gốc dự án, không commit lên Git [2]:

```text
# .env.local
API_URL=http://<địa-chỉ-API-mẫu>:3000
```

Biến **không có** tiền tố `NEXT_PUBLIC_` chỉ đọc được ở server; biến có tiền tố `NEXT_PUBLIC_` được chép vào JavaScript gửi xuống trình duyệt, ai cũng xem được. Sau khi sửa `.env.local` phải khởi động lại `npm run dev`.

### 3.2.2. Kiểu dữ liệu và hàm gọi API tập trung

Kiểu dữ liệu viết theo định dạng trả về của API mẫu (xem Swagger tại `/docs` và SRS mục 8):

```ts
// lib/types.ts
export type Category = { id: number; name: string; productCount: number };
export type Product = {
  id: number; categoryId: number; categoryName: string; name: string;
  description: string | null; price: number; imageUrl: string | null;
  isAvailable: boolean; stock: number;
};
```

Mọi lời gọi API đi qua một hàm duy nhất. Khi đổi backend (Sprint 3) hay thêm xác thực (Chương 5), chỉ sửa một chỗ:

```ts
// lib/api.ts: chỉ dùng ở server
import 'server-only';

export async function apiGet<T>(path: string, revalidate = 30): Promise<T> {
  const res = await fetch(`${process.env.API_URL}${path}`, { next: { revalidate } });
  if (!res.ok) throw new Error(`API ${path} trả về ${res.status}`);
  return res.json() as Promise<T>;
}
```

Gói `server-only` (cài bằng `npm install server-only`) làm lỗi build nếu một Client Component vô tình import file này, nhờ vậy địa chỉ API nội bộ không bao giờ bị gửi xuống trình duyệt.

### 3.2.3. Trang thực đơn

```tsx
// app/(shop)/menu/page.tsx
import Link from 'next/link';
import { apiGet } from '@/lib/api';
import type { Category, Product } from '@/lib/types';

type Props = { searchParams: Promise<{ category?: string; q?: string }> };

export default async function MenuPage({ searchParams }: Props) {
  const { category, q } = await searchParams;
  const query = new URLSearchParams({ pageSize: '50' });
  if (category) query.set('categoryId', category);
  if (q) query.set('keyword', q);

  const [categories, products] = await Promise.all([
    apiGet<Category[]>('/categories', 300),          // danh mục ít đổi: 5 phút
// … (trích 15/43 dòng; mã đầy đủ ở Phụ lục A, mục A.1)
```

Những điểm cần chú ý:

- `searchParams` cũng là `Promise` từ Next.js 15 [3].
- `Promise.all` gọi hai API **song song**, không chờ lần lượt.
- Form tìm kiếm dùng phương thức GET bình thường nên không cần JavaScript phía client; kết quả nằm trong URL (`/menu?q=com`), chia sẻ và tải lại được.
- Luôn có trạng thái **rỗng** ("Không tìm thấy món phù hợp"), không để trang trắng.
- `imageUrl` của API là đường dẫn tương đối (`/uploads/...`) và có thể rỗng; ghép với `API_URL` và có ảnh thay thế.

## 3.3. Cache và làm mới dữ liệu

### 3.3.1. Mặc định từ Next.js 15

Từ Next.js 15, `fetch` trong Server Component **không tự cache**: mỗi request tới trang là một lần gọi API [4]. Muốn dùng lại kết quả, khai báo `{ next: { revalidate: N } }`: kết quả được dùng lại trong N giây, sau đó lần gọi kế tiếp lấy dữ liệu mới.

### 3.3.2. Chọn thời gian theo mức thay đổi của dữ liệu

| Dữ liệu | Mức thay đổi | Lựa chọn | Hệ quả |
|---|---|---|---|
| Danh mục | Vài lần mỗi học kỳ | `revalidate: 300` | Danh mục mới hiện sau tối đa 5 phút |
| Món, tồn kho | Nhiều lần mỗi giờ | `revalidate: 30` | Món vừa hết hàng, khách thấy sau tối đa 30 giây |
| Đơn của tôi, màn hình quầy | Liên tục, riêng từng người | `cache: 'no-store'` | Luôn gọi API (Chương 5, 6) |

Lựa chọn cache là một quyết định thiết kế có đánh đổi giữa tốc độ và độ mới của dữ liệu, cần được giải thích trong báo cáo. Dữ liệu riêng của từng người **không bao giờ** được cache chung. Chương 6 giới thiệu `revalidatePath` để làm mới ngay sau khi ghi dữ liệu.

## 3.4. Trạng thái tải và lỗi

### 3.4.1. File loading.tsx và streaming

```tsx
// app/(shop)/menu/loading.tsx: hiện ngay trong lúc trang chờ API
export default function Loading() {
  return <p className="p-6 text-slate-500">Đang tải thực đơn…</p>;
}
```

`loading.tsx` dùng cơ chế **streaming**: layout và khung trang hiện ngay, phần dữ liệu đến sau [5]. Có thể bọc riêng từng khối chậm bằng `<Suspense fallback={...}>` để phần nhanh không phải chờ phần chậm, ví dụ danh mục hiện trước, lưới món hiện sau. Khung chờ nên có kích thước gần đúng nội dung thật để trang không bị nhảy (Chương 10).

### 3.4.2. File error.tsx

```tsx
// app/(shop)/menu/error.tsx: bắt buộc là Client Component
'use client';
export default function MenuError({ reset }: { error: Error; reset: () => void }) {
  return (
    <div className="p-6">
      <p>Không tải được thực đơn. Vui lòng thử lại.</p>
      <button onClick={reset} className="mt-2 rounded bg-blue-900 px-4 py-2 text-white">Thử lại</button>
    </div>
  );
}
```

`error.tsx` bắt lỗi của trang và các component con, hiển thị giao diện thay thế [6]. Không hiển thị thông báo kỹ thuật (`API /products trả về 500`) cho người dùng; ghi log ở server để nhóm gỡ lỗi.

## 3.5. Kiểm thử và báo cáo sprint

### 3.5.1. Test case từ tiêu chí chấp nhận (CLO2)

SRS mục 4.7 ghi tiêu chí chấp nhận của các story Must. Mỗi tiêu chí thành ít nhất một **test case** có các cột: mã, story, điều kiện trước, bước thực hiện, dữ liệu vào, kết quả mong đợi (đo được), kết quả thực tế.

| Mã | Story | Bước thực hiện | Kết quả mong đợi | Kết quả |
|---|---|---|---|---|
| TC-01 | US-G01 | Mở `/menu` | Thấy danh mục và món đang bán, giá dạng "35.000 đ" | Đạt |
| TC-02 | US-G01 | Chọn danh mục "Đồ uống" | Chỉ còn món thuộc "Đồ uống" | Đạt |
| TC-03 | US-G02 | Tìm "com ga" | Có "Cơm gà xối mỡ" (tìm không phân biệt dấu) | … |
| TC-04 | US-G03 | Mở `/product/999999` | Trang 404 thân thiện | … |
| TC-05 | US-G01 | Đổi `API_URL` sai, mở `/menu` | Thông báo lỗi và nút Thử lại, không lộ lỗi kỹ thuật | … |

"Kết quả mong đợi" phải kiểm tra được: "hiển thị đúng" là không đo được; "chỉ còn món thuộc Đồ uống" là đo được. Test case TC-05 kiểm tra một trường hợp lỗi: bộ test chỉ có trường hợp thuận lợi là chưa đủ.

### 3.5.2. Báo cáo sprint (CLO3)

Báo cáo sprint dài 1–2 trang, trình bày theo quy định định dạng ở trang Đánh giá học phần (A4, Times New Roman 13, hình và bảng có số, chú thích):

1. **Sprint Goal và kết quả:** đạt hay chưa đạt, link demo.
2. **Story đã hoàn thành:** bảng mã story, người phụ trách, Pull Request.
3. **Phân tích thành phần của sprint:** sơ đồ chức năng, sitemap, bảng ánh xạ route, có số hình và chú thích.
4. **Kiểm thử:** số test case, số đạt, lỗi tìm thấy và đã sửa.
5. **Kế hoạch so với thực tế:** story point cam kết và hoàn thành, nguyên nhân chênh lệch.
6. **Kế hoạch sprint sau và bài học rút ra** (Retrospective).

Bốn báo cáo sprint là nguyên liệu cho báo cáo đồ án cuối kỳ (Chương 11).

### 3.5.3. Sprint Review và kế hoạch Sprint 2 (CLO4)

Cuối sprint, nhóm demo sản phẩm cho giảng viên (**Sprint Review**), nhận góp ý và cập nhật backlog. Kế hoạch Sprint 2 chọn story theo **năng lực thực tế** đo được ở Sprint 1: nếu Sprint 1 cam kết 20 story point nhưng chỉ hoàn thành 13, Sprint 2 không nên cam kết 25. Board phải được cập nhật trước khi rời lớp.

## Tóm tắt chương

- Trang là Server Component, chỉ phần nhỏ cần tương tác mới là Client Component; `"use client"` đặt ở lá.
- Lấy dữ liệu trong Server Component qua hàm `apiGet` tập trung, biến `API_URL` chỉ ở server, gói `server-only` chặn import nhầm.
- Từ Next.js 15, `fetch` không tự cache; chọn `revalidate` theo mức thay đổi của dữ liệu; dữ liệu riêng dùng `no-store`.
- Luôn có trạng thái tải (`loading.tsx`, `Suspense`), lỗi (`error.tsx`) và rỗng.
- Test case viết từ tiêu chí chấp nhận, kết quả mong đợi đo được; báo cáo sprint 6 mục; kế hoạch sprint sau dựa trên năng lực thực tế.

## Câu hỏi ôn tập

1. Một component dùng `useState` nhưng được import vào Server Component. Cần làm gì để chạy đúng?
2. Vì sao biến `API_URL` không nên có tiền tố `NEXT_PUBLIC_`?
3. Gói `server-only` bảo vệ điều gì?
4. Giải thích ý nghĩa của `{ next: { revalidate: 30 } }`. Khách thấy món vừa hết hàng sau tối đa bao lâu?
5. Vì sao trang "Đơn của tôi" không được cache chung?
6. Vì sao `error.tsx` phải là Client Component?
7. Viết lại kết quả mong đợi "Trang hiển thị đúng" thành một kết quả đo được cho TC-02.

## Bài tập

1. **Chi tiết món.** Chuyển `/product/[id]` sang lấy dữ liệu từ `GET /products/:id`, hiện "Hết món" khi `isAvailable` sai hoặc `stock` bằng 0.
2. **Suspense.** Tách danh mục và lưới món thành hai khối có `Suspense` riêng; đo bằng tab Network khi giả lập mạng chậm.
3. **Test case.** Viết thêm 3 test case cho US-G02 (từ khóa rỗng, từ khóa có dấu, từ khóa không có kết quả).

## Tài liệu tham khảo

[1] Vercel, “Server and Client Components,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/server-and-client-components

[2] Vercel, “Environment Variables,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/guides/environment-variables

[3] Vercel, “page.js,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/page

[4] Vercel, “Fetching Data,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/fetching-data

[5] Vercel, “loading.js,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/loading

[6] Vercel, “Error Handling,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/error-handling
