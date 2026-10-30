# Chương 8. Trang quản trị: CRUD, tải ảnh, báo cáo và biểu đồ

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Xây dựng trang quản trị CRUD theo một mẫu thống nhất với form dùng chung cho tạo và sửa.
- Tải ảnh lên API qua Server Action, kiểm tra định dạng và dung lượng ở nhiều lớp.
- Trình bày số liệu báo cáo bằng biểu đồ phù hợp với câu hỏi cần trả lời.
- Xuất dữ liệu thành file CSV mở được bằng Excel qua Route Handler.
- Xây dựng trang quản lý tài khoản nhân viên và kiểm thử các ràng buộc nghiệp vụ quản trị.

## 8.1. Mẫu trang CRUD

### 8.1.1. Một cấu trúc cho mọi trang quản trị

CRUD là bốn thao tác cơ bản trên dữ liệu: tạo (Create), đọc (Read), sửa (Update), xóa (Delete). Mọi trang quản trị (món, danh mục, quầy, tài khoản) dùng cùng một cấu trúc. Người dùng học một lần là dùng được mọi trang, nhóm viết một lần là nhân bản được:

```text
app/admin/products/
├── page.tsx             danh sách (Server Component, bảng của Chương 6)
├── new/page.tsx         tạo mới  → <ProductForm />
├── [id]/edit/page.tsx   sửa      → <ProductForm product={product} />
├── product-form.tsx     form dùng chung (Client Component)
└── actions.ts           saveProduct, uploadProductImage, toggleAvailability
```

### 8.1.2. Một Server Action cho tạo và sửa

```ts
// app/admin/products/actions.ts
'use server';
import { redirect } from 'next/navigation';
import { revalidatePath } from 'next/cache';
import { productSchema } from '@/lib/schemas';
import { requireRole } from '@/lib/dal';
import { apiAuth, ApiError } from '@/lib/api';

export type FormState = { ok: boolean; message?: string; fieldErrors?: Record<string, string[]> };

// id có giá trị: sửa; không có: tạo mới. Gắn id bằng saveProduct.bind(null, product?.id)
export async function saveProduct(id: number | undefined, _prev: FormState, formData: FormData): Promise<FormState> {
  await requireRole('admin');
  const parsed = productSchema.safeParse(Object.fromEntries(formData));   // price, categoryId: z.coerce.number()
  if (!parsed.success) return { ok: false, fieldErrors: parsed.error.flatten().fieldErrors };
  try {
    await apiAuth(id ? `/admin/products/${id}` : '/admin/products', {
      method: id ? 'PUT' : 'POST', body: JSON.stringify(parsed.data),
    });
  } catch (e) {
    if (e instanceof ApiError && e.status === 404) return { ok: false, message: 'Danh mục hoặc món không còn tồn tại' };
    return { ok: false, message: 'Chưa lưu được món, vui lòng thử lại' };
  }
  revalidatePath('/admin/products');
  revalidatePath('/menu');                           // thực đơn của khách cũng đổi
  redirect('/admin/products');
}
```

- Form dùng `useActionState(saveProduct.bind(null, product?.id), { ok: false })`; ô nhập lấy `defaultValue` từ `product` khi sửa; lỗi từng trường lấy từ `state.fieldErrors`.
- `redirect` gọi **sau** khối `try/catch`: `redirect` hoạt động bằng cách ném một lỗi đặc biệt, đặt trong `try` sẽ bị `catch` nuốt mất [1].
- Một thay đổi ở trang quản trị ảnh hưởng tới trang khách: gọi `revalidatePath` cho cả hai.

### 8.1.3. Xóa, ngừng bán và xác nhận

- **Không có nút "Xóa món".** Món đã có trong đơn chỉ được ngừng bán (BR-16), dùng nút bật/tắt của Chương 6. Xóa hẳn sẽ làm hỏng lịch sử đơn hàng và báo cáo.
- Thao tác không hoàn tác được (xóa danh mục, khóa tài khoản) phải qua hộp thoại `AlertDialog` của shadcn/ui ghi rõ hậu quả: "Xóa danh mục Đồ uống? Thao tác này không hoàn tác được." [2].
- Sau khi lưu, hiện thông báo ngắn (toast) "Đã lưu món Cơm gà xối mỡ" và quay về danh sách.

## 8.2. Tải ảnh món

### 8.2.1. Luồng tải ảnh

```text
Trình duyệt ─FormData─▶ Server Action ─multipart/form-data─▶ API (Multer, trường "file")
                        kiểm tra loại, dung lượng              lưu file, sp_Product_UpdateImage
```

Trình duyệt không gửi ảnh thẳng tới API (sẽ cần token ở trình duyệt và mở CORS). Server Action nhận file, kiểm tra, rồi chuyển tiếp tới API kèm token từ cookie.

### 8.2.2. Server Action tải ảnh

```ts
// app/admin/products/actions.ts (tiếp; thêm import { getAccessToken } from '@/lib/session')
const IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp'];
const MAX_BYTES = 2 * 1024 * 1024;

export async function uploadProductImage(productId: number, _prev: FormState, formData: FormData): Promise<FormState> {
  await requireRole('admin');
  const file = formData.get('file');
  if (!(file instanceof File) || file.size === 0) return { ok: false, message: 'Chọn một ảnh' };
  if (!IMAGE_TYPES.includes(file.type)) return { ok: false, message: 'Chỉ nhận ảnh JPG, PNG hoặc WEBP' };
  if (file.size > MAX_BYTES) return { ok: false, message: 'Ảnh tối đa 2 MB' };

  const body = new FormData();
  body.append('file', file);
  const res = await fetch(`${process.env.API_URL}/admin/products/${productId}/image`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${await getAccessToken()}` },   // KHÔNG tự đặt Content-Type
    body,
  });
  if (!res.ok) return { ok: false, message: res.status === 413 ? 'Ảnh vượt quá dung lượng cho phép' : 'Tải ảnh thất bại' };
  revalidatePath('/admin/products');
  return { ok: true, message: 'Đã cập nhật ảnh' };
}
```

**Không tự đặt Content-Type** khi gửi `FormData`: `fetch` tự sinh `multipart/form-data; boundary=…`; đặt tay mà thiếu `boundary` thì server không tách được file. Vì vậy upload không dùng `apiAuth` (hàm đó luôn đặt JSON), giống lưu ý ở Chương 8 giáo trình di động.

### 8.2.3. Cấu hình Next.js

```ts
// next.config.ts
const nextConfig = {
  experimental: { serverActions: { bodySizeLimit: '3mb' } },     // mặc định 1 MB
  images: { remotePatterns: [new URL(`${process.env.API_URL}/uploads/**`)] },  // cho phép next/image
};
export default nextConfig;
```

Dữ liệu gửi tới Server Action mặc định giới hạn 1 MB [3]; ảnh 2 MB cần tăng giới hạn. `images.remotePatterns` cho phép component `next/image` tối ưu ảnh lấy từ địa chỉ API [4].

### 8.2.4. Xem trước và kiểm tra ba lớp

- **Xem trước** ở client: `<input type="file" name="file" accept="image/jpeg,image/png,image/webp">`; khi chọn file thì tạo địa chỉ tạm bằng `URL.createObjectURL(file)` và hiện bằng `<img>`; gọi `URL.revokeObjectURL` khi đổi file để giải phóng bộ nhớ.
- Kiểm tra định dạng ở **ba nơi**: thuộc tính `accept` (tiện cho người dùng, không phải bảo vệ), Server Action (chặn sớm, đỡ tốn băng thông tới API), API (chặn thật bằng `fileFilter` của Multer).
- Không tin phần mở rộng tên file: một file PDF đổi tên thành `.jpg` vẫn là PDF.

## 8.3. Báo cáo và biểu đồ

### 8.3.1. Lấy dữ liệu báo cáo

Trang `/admin/reports?from=2026-10-01&to=2026-10-31`: Server Component đọc khoảng ngày từ URL, gọi ba API báo cáo cùng lúc, truyền dữ liệu cho biểu đồ.

```tsx
// app/admin/reports/page.tsx
export default async function ReportsPage({ searchParams }: { searchParams: Promise<{ from?: string; to?: string }> }) {
  await requireRole('admin');
  const { from = firstDayOfMonth(), to = today() } = await searchParams;
  if (from > to) return <p role="alert">Ngày bắt đầu phải trước hoặc bằng ngày kết thúc.</p>;
  const q = `from=${from}&to=${to}`;
  const [revenue, top, status] = await Promise.all([
    apiAuth<{ day: string; orderCount: number; revenue: number }[]>(`/reports/revenue?${q}`),
    apiAuth<{ id: number; name: string; quantity: number; revenue: number }[]>(`/reports/top-products?${q}&top=5`),
    apiAuth<{ status: string; orderCount: number; percentage: number }[]>(`/reports/order-status?${q}`),
  ]);
  return <ReportView revenue={revenue} top={top} status={status} from={from} to={to} />;
}
```

Bộ chọn ngày là một form GET (hai ô `type="date"` tên `from`, `to`), nên khoảng ngày nằm trên URL và gửi link báo cáo được.

### 8.3.2. Chọn biểu đồ theo câu hỏi

Biểu đồ tốt bắt đầu từ câu hỏi người xem cần trả lời, không phải từ loại biểu đồ đẹp:

| Câu hỏi | Biểu đồ phù hợp | Không nên |
|---|---|---|
| Doanh thu thay đổi thế nào theo ngày? | Cột hoặc đường theo trục thời gian | Biểu đồ tròn |
| Món nào bán chạy nhất? | Cột ngang, sắp xếp giảm dần | Cột dọc không sắp xếp |
| Bao nhiêu phần trăm đơn bị hủy? (US-A06) | Cột chồng 100% hoặc bảng có phần trăm | Biểu đồ tròn nhiều lát |

Một chuỗi số liệu dùng **một màu**; không tô mỗi ngày một màu. Luôn có tiêu đề, đơn vị và bảng số liệu bên dưới cho người không xem được biểu đồ (Chương 10).

### 8.3.3. Biểu đồ với Recharts

Recharts vẽ bằng JavaScript trong trình duyệt, nên component biểu đồ bắt buộc là Client Component [5]:

```tsx
// app/admin/reports/revenue-chart.tsx   (npm install recharts)
'use client';
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const vnd = (n: number) => `${n.toLocaleString('vi-VN')} đ`;

export function RevenueChart({ data }: { data: { day: string; revenue: number }[] }) {
  return (
    <figure>
      <figcaption className="font-bold">Doanh thu theo ngày (không tính đơn đã hủy)</figcaption>
      <ResponsiveContainer width="100%" height={280}>
        <BarChart data={data}>
          <CartesianGrid vertical={false} strokeDasharray="3 3" />
          <XAxis dataKey="day" tickFormatter={(d: string) => d.slice(8, 10) + '/' + d.slice(5, 7)} />
          <YAxis tickFormatter={(n: number) => `${n / 1000}k`} />
          <Tooltip formatter={(n: number) => vnd(n)} labelFormatter={(d: string) => `Ngày ${d}`} />
          <Bar dataKey="revenue" name="Doanh thu" fill="#1e3a8a" radius={[4, 4, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </figure>
  );
}
```

`ResponsiveContainer` cần một khối cha có chiều cao xác định; thiếu thì biểu đồ không hiện.

### 8.3.4. Số liệu phải khớp CSDL

Tiêu chí US-A05: báo cáo doanh thu không tính đơn `cancelled` và **khớp với truy vấn trực tiếp trên CSDL**. Đây là test case bắt buộc: chọn một ngày, so số trên web với `SELECT SUM(...)` chạy trong SSMS. Biểu đồ đẹp mà số sai còn tệ hơn không có biểu đồ.

## 8.4. Xuất CSV

Xuất file dùng **Route Handler** vì cần trả về file, không phải trang [6]:

```ts
// app/admin/reports/export/route.ts   → <a href={`/admin/reports/export?from=${from}&to=${to}`}>
export async function GET(req: Request) {
  await requireRole('admin');
  const { searchParams } = new URL(req.url);
  const q = `from=${searchParams.get('from')}&to=${searchParams.get('to')}`;
  const rows = await apiAuth<{ day: string; orderCount: number; revenue: number }[]>(`/reports/revenue?${q}`);
  const csv = ['Ngày,Số đơn,Doanh thu', ...rows.map((r) => `${r.day},${r.orderCount},${r.revenue}`)].join('\r\n');
  return new Response('﻿' + csv, {                     // BOM: Excel đọc đúng tiếng Việt
    headers: {
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': `attachment; filename="doanh-thu-${searchParams.get('from')}.csv"`,
    },
  });
}
```

- Ký tự **BOM** (`﻿`) ở đầu file báo cho Excel biết file mã hóa UTF-8; thiếu thì tiêu đề tiếng Việt bị lỗi font.
- Thư mục `/admin` đã được `proxy.ts` bảo vệ, nhưng Route Handler vẫn gọi `requireRole` (nguyên tắc ba lớp của Chương 5).
- Giá trị có dấu phẩy (tên món) phải bọc trong dấu nháy kép, dấu nháy kép bên trong nhân đôi.

## 8.5. Tài khoản nhân viên và test case quản trị

### 8.5.1. Trang tài khoản nhân viên

Trang `/admin/users` (US-A04): danh sách lọc theo vai trò và tìm theo tên/email, phân trang qua URL; form tạo tài khoản staff; nút Khóa/Mở khóa có hộp thoại xác nhận; trạng thái khóa hiển thị bằng chữ. Mật khẩu ban đầu do quản lý đặt, được băm bằng bcrypt ở backend; web không bao giờ hiển thị lại mật khẩu.

### 8.5.2. Test case quản trị (CLO2)

Mỗi ràng buộc nghiệp vụ trong danh mục stored procedure (Chương 7) có ít nhất một test case trên giao diện:

| Mã | Story | Bước thực hiện | Kết quả mong đợi |
|---|---|---|---|
| TC-41 | US-A01 | Xóa danh mục còn món | "Danh mục còn món, không xóa được"; danh mục vẫn còn |
| TC-42 | US-A02 | Tạo món giá 0 đ / giá âm | Báo lỗi dưới ô Giá, không gọi API |
| TC-43 | US-A02 | Tải file PDF đổi tên thành `.jpg` | Bị từ chối, ảnh cũ giữ nguyên |
| TC-44 | US-A02 | Tải ảnh 2,5 MB | "Ảnh tối đa 2 MB" |
| TC-45 | US-A05 | So doanh thu một ngày trên web với `SELECT SUM` trên CSDL (bỏ đơn `cancelled`) | Hai số bằng nhau |
| TC-46 | US-A05 | Chọn ngày bắt đầu sau ngày kết thúc | Thông báo lỗi, không gọi API |
| TC-47 | US-A04 | Khóa nhân viên đang đăng nhập, chờ access token hết hạn | Làm mới token bị từ chối, nhân viên về trang đăng nhập và không đăng nhập lại được |
| TC-48 | US-A04 | Quản lý tự khóa tài khoản của mình | "Không thể tự khóa tài khoản của mình" (400) |
| TC-49 | US-A05 | Mở file CSV vừa xuất bằng Excel | Tiêu đề cột tiếng Việt đúng dấu, số liệu khớp trang |

Ảnh chụp biểu đồ và bảng đưa vào báo cáo phải có số hình, chú thích và đoạn giải thích "biểu đồ này cho thấy điều gì".

## Tóm tắt chương

- Mẫu CRUD thống nhất: danh sách, `new`, `[id]/edit`, form dùng chung, `actions.ts`; một Server Action cho tạo và sửa.
- Không xóa món đã bán (BR-16); thao tác không hoàn tác được phải có hộp thoại xác nhận.
- Tải ảnh qua Server Action, không tự đặt `Content-Type`, tăng `bodySizeLimit`; kiểm tra định dạng ở ba lớp.
- Chọn biểu đồ theo câu hỏi; Recharts là Client Component; số liệu phải khớp CSDL.
- Xuất CSV bằng Route Handler có BOM và `requireRole`.

## Câu hỏi ôn tập

1. Vì sao `redirect` phải đặt sau khối `try/catch` trong Server Action?
2. Vì sao trang quản lý món không có nút "Xóa"?
3. Giải thích vì sao không nên tự đặt header `Content-Type` khi gửi `FormData`.
4. Kiểm tra định dạng ảnh ở thuộc tính `accept` có đủ không? Vì sao?
5. Câu hỏi "món nào bán chạy nhất tháng này" nên dùng biểu đồ gì?
6. Vì sao file CSV cần BOM?
7. Viết test case kiểm tra tiêu chí "báo cáo không tính đơn đã hủy".

## Bài tập

1. **Tài khoản nhân viên.** Hoàn thành trang `/admin/users` theo mục 8.5.1 kèm TC-47, TC-48 và 3 test case cho form tạo tài khoản.
2. **Món bán chạy.** Thêm biểu đồ cột ngang 5 món bán chạy, sắp xếp giảm dần, có bảng số liệu bên dưới.
3. **CSV an toàn.** Sửa Route Handler xuất CSV để bọc đúng các giá trị có dấu phẩy hoặc dấu nháy kép.

## Tài liệu tham khảo

[1] Vercel, “redirect,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/functions/redirect

[2] shadcn, “Alert Dialog,” *shadcn/ui Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://ui.shadcn.com/docs/components/alert-dialog

[3] Vercel, “serverActions,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions

[4] Vercel, “Image Component,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/components/image

[5] Recharts, “Getting Started,” *Recharts Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://recharts.org/en-US/guide

[6] Vercel, “Route Handlers,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/route-handlers
