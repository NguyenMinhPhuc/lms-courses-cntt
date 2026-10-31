# Chương 6. Server Actions, bảng dữ liệu và màn hình quầy

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Thực hiện thao tác ghi dữ liệu bằng Server Actions với `useActionState`, `revalidatePath` và `useOptimistic`.
- Xây dựng bảng dữ liệu có sắp xếp, lọc và phân trang theo tham số URL bằng TanStack Table.
- Phân tích nghiệp vụ trạng thái đơn và xây dựng màn hình quầy đúng trình tự, xử lý xung đột 409.
- Kiểm thử luồng nghiệp vụ "khách đặt → nhân viên xử lý" theo tiêu chí chấp nhận.
- Tính velocity và lập kế hoạch sprint dựa trên số liệu thực tế.

## 6.1. Server Actions

### 6.1.1. Khái niệm

**Server Action** (Next.js gọi chung là Server Function) là hàm `async` có chỉ thị `'use server'`, chạy trên server nhưng được gọi từ form hoặc Client Component [1]. Next.js tự tạo một endpoint POST cho mỗi Server Action. Nhờ vậy nhóm không phải tự viết Route Handler cho từng thao tác ghi.

Hệ quả quan trọng: **mỗi Server Action là một endpoint công khai**. Ai cũng gửi request tới được, kể cả khi trang chứa nút bấm đã được bảo vệ. Vì vậy luôn kiểm tra quyền và dữ liệu **bên trong** Server Action (Chương 5).

### 6.1.2. Server Action của màn hình quầy

```ts
// app/admin/orders/actions.ts
'use server';
import { revalidatePath } from 'next/cache';
import { z } from 'zod';
import { requireRole } from '@/lib/dal';
import { apiAuth, ApiError } from '@/lib/api';

export type NextStatus = 'preparing' | 'ready' | 'completed';
export type ActionResult = { ok: boolean; message?: string };

export async function advanceStatus(orderId: number, status: NextStatus): Promise<ActionResult> {
  await requireRole('staff', 'admin');                       // kiểm tra quyền ở chính Server Action
  try {
    await apiAuth(`/orders/${orderId}/status`, { method: 'PATCH', body: JSON.stringify({ status }) });
    return { ok: true };
// … (trích 15/45 dòng; mã đầy đủ ở Phụ lục A, mục A.3)
```

Dữ liệu từ `FormData` luôn là chuỗi; `z.coerce.number()` chuyển `"12"` thành `12` trước khi kiểm tra.

### 6.1.3. Hook useActionState

`useActionState(action, initialState)` (từ thư viện `react`) nối form với Server Action và trả về `[state, formAction, isPending]` [2]:

```tsx
'use client';
import { useActionState } from 'react';
import { staffCancel } from './actions';

export function CancelForm({ orderId }: { orderId: number }) {
  const [state, formAction, isPending] = useActionState(staffCancel, { ok: false });
  return (
    <form action={formAction} className="space-y-2">
      <input type="hidden" name="orderId" value={orderId} />
      <label className="block">Lý do hủy
        <input name="reason" className="w-full rounded border px-2 py-1" />
      </label>
      {state.message && <p role="alert" className={state.ok ? 'text-green-700' : 'text-red-600'}>{state.message}</p>}
      <button disabled={isPending} className="rounded bg-red-700 px-3 py-1 text-white">Hủy đơn</button>
    </form>
  );
}
```

`state` là giá trị Server Action trả về lần gần nhất; `isPending` dùng để vô hiệu nút khi đang gửi.

### 6.1.4. Hàm revalidatePath

Sau khi ghi dữ liệu, trang đang hiển thị dữ liệu cũ. `revalidatePath('/admin/orders')` xóa cache của trang đó; lần render kế tiếp (ngay sau Server Action) lấy dữ liệu mới từ API [3]. Không cần tự gọi lại API ở client hay tự cập nhật state.

### 6.1.5. Hook useOptimistic

Chờ server phản hồi rồi mới đổi giao diện tạo cảm giác chậm. **Cập nhật lạc quan** (optimistic update) hiện ngay kết quả mong đợi trong lúc chờ; nếu server từ chối, giao diện tự trở về dữ liệu thật khi trang được làm mới. React cung cấp hook `useOptimistic` cho việc này [4]. Ví dụ dùng ở mục 6.3.3.

Không phải thao tác nào cũng nên lạc quan. Đổi trạng thái đơn thì hợp (hiếm khi thất bại, thất bại thì tự sửa lại ngay). Hủy đơn hay thanh toán thì không: người dùng không nên thấy "đã hủy" khi thực tế chưa hủy.

## 6.2. Bảng dữ liệu với TanStack Table

### 6.2.1. Trạng thái bảng nằm ở đâu

Trang `/admin/products` cho nhân viên xem cả món ngừng bán và bật/tắt "còn bán" (US-S04). Một bảng quản trị có bốn trạng thái: lọc, sắp xếp, trang hiện tại, dữ liệu. Cách tổ chức của học phần:

- **Lọc và phân trang** đặt trong URL (`?q=com&page=2`): Server Component đọc `searchParams`, gọi API đúng trang; tải lại hoặc gửi link vẫn giữ nguyên.
- **Sắp xếp cột** trên trang hiện tại đặt trong state của Client Component.
- **Dữ liệu** lấy từ API ở server.

### 6.2.2. Server Component lấy dữ liệu

```tsx
// app/admin/products/page.tsx
const PAGE_SIZE = 20;
type Props = { searchParams: Promise<{ q?: string; page?: string }> };

export default async function ProductsPage({ searchParams }: Props) {
  await requireRole('staff', 'admin');
  const { q = '', page = '1' } = await searchParams;
  const query = new URLSearchParams({ includeUnavailable: 'true', page, pageSize: String(PAGE_SIZE) });
  if (q) query.set('keyword', q);
  const products = await apiAuth<Product[]>(`/products?${query}`);
  return <ProductTable data={products} page={Number(page)} q={q} hasNext={products.length === PAGE_SIZE} />;
}
```

API mẫu trả về mảng, không có tổng số dòng: còn trang sau khi số phần tử bằng `pageSize`.

### 6.2.3. Client Component hiển thị bảng

TanStack Table là thư viện "headless": nó quản lý logic bảng (cột, sắp xếp, phân trang) còn giao diện do nhóm tự viết [5].

```tsx
// app/admin/products/product-table.tsx   (npm install @tanstack/react-table)
'use client';
import { useState } from 'react';
import Link from 'next/link';
import { flexRender, getCoreRowModel, getSortedRowModel, useReactTable,
         type ColumnDef, type SortingState } from '@tanstack/react-table';
import type { Product } from '@/lib/types';
import { toggleAvailability } from './actions';

const columns: ColumnDef<Product>[] = [
  { accessorKey: 'name', header: 'Tên món' },
  { accessorKey: 'categoryName', header: 'Danh mục' },
  { accessorKey: 'price', header: 'Giá', cell: (c) => `${c.getValue<number>().toLocaleString('vi-VN')} đ` },
  { accessorKey: 'stock', header: 'Tồn' },
  { id: 'available', header: 'Còn bán', cell: ({ row }) => (
// … (trích 15/48 dòng; mã đầy đủ ở Phụ lục A, mục A.4)
```

`toggleAvailability.bind(null, id, value)` gắn sẵn tham số cho Server Action để dùng làm `action` của form. `toggleAvailability` gọi `PATCH /products/:id/availability`, kiểm tra quyền staff và gọi `revalidatePath('/admin/products')`. shadcn/ui có mẫu "Data Table" dựng sẵn trên TanStack Table, nhóm có thể dùng.

## 6.3. Màn hình quầy

### 6.3.1. Phân tích nghiệp vụ trạng thái đơn (CLO1)

SRS mục 6.1 mô tả sơ đồ trạng thái đơn hàng; quy tắc BR-15 yêu cầu trạng thái chỉ đi một chiều:

```text
pending ──"Bắt đầu làm"──▶ preparing ──"Đã xong"──▶ ready ──"Đã giao"──▶ completed
   │ khách hủy (US-C08)         │
   └── nhân viên hủy kèm lý do (US-S07) ──▶ cancelled
```

Từ sơ đồ suy ra ba điều cho giao diện: mỗi trạng thái chỉ có **một** nút đi tiếp; nút hủy chỉ hiện với `pending` và `preparing`; chuyển sai trình tự thì API trả 409, giao diện phải hiển thị được lỗi đó. Sơ đồ trạng thái có số hình và chú thích là một phần của báo cáo Sprint 2.

### 6.3.2. Bố cục

Trang `/admin/orders` là Server Component gọi `GET /orders/staff` (mặc định trả đơn `pending`, `preparing`, `ready` trong ngày), chia thành ba cột theo trạng thái. Lọc trạng thái (US-S06) qua tham số `?status=`. Mỗi đơn là một Client Component nhỏ.

### 6.3.3. Thẻ đơn với cập nhật lạc quan

```tsx
// app/admin/orders/order-card.tsx
'use client';
import { useOptimistic, useState, useTransition } from 'react';
import { advanceStatus, type NextStatus } from './actions';

type StaffOrder = { orderId: number; status: string; note: string | null; createdAt: string;
                    customerName: string; total: number; summary: string };

const NEXT: Record<string, { to: NextStatus; label: string } | undefined> = {
  pending: { to: 'preparing', label: 'Bắt đầu làm' },
  preparing: { to: 'ready', label: 'Đã xong' },
  ready: { to: 'completed', label: 'Đã giao' },
};
const LABEL: Record<string, string> = {
  pending: 'Chờ xác nhận', preparing: 'Đang chuẩn bị', ready: 'Sẵn sàng', completed: 'Hoàn tất', cancelled: 'Đã hủy',
// … (trích 15/42 dòng; mã đầy đủ ở Phụ lục A, mục A.5)
```

- Hàm cập nhật của `useOptimistic` phải được gọi trong `startTransition` hoặc trong form action.
- Trạng thái hiện bằng **chữ**, không chỉ bằng màu (người mù màu vẫn đọc được, Chương 10).
- Ghi chú của khách hiển thị dạng văn bản; React tự mã hóa nên `<script>` trong ghi chú không chạy (Chương 5).

### 6.3.4. Xung đột khi hai nhân viên cùng thao tác

Giờ cao điểm, hai nhân viên có thể cùng bấm "Bắt đầu làm" một đơn. Stored procedure chỉ cho phép chuyển từ đúng trạng thái hiện tại, nên chỉ người đầu thành công; người sau nhận 409. Server Action trả thông báo "đã được cập nhật bởi người khác", và nhờ `revalidatePath` trong khối `finally`, danh sách được làm mới ngay. Đây là ví dụ quy tắc nghiệp vụ đặt ở CSDL bảo vệ được tình huống đồng thời mà giao diện không tự xử lý được.

Tạm thời, danh sách tự làm mới mỗi 15 giây bằng một Client Component gọi `router.refresh()` trong `setInterval`. Chương 9 thay bằng Socket.IO để đơn mới hiện ngay lập tức.

## 6.4. Kiểm thử luồng nghiệp vụ và báo cáo Sprint 2

### 6.4.1. Test case luồng "khách đặt → nhân viên xử lý" (CLO2)

Test luồng nghiệp vụ đi qua nhiều trang, nhiều vai trò. Mở hai trình duyệt (hoặc một cửa sổ ẩn danh): một bên đăng nhập customer, một bên đăng nhập staff.

| Mã | Story | Bước thực hiện | Kết quả mong đợi |
|---|---|---|---|
| TC-31 | US-C04, S02 | Khách đặt 2 món, ghi chú "Ít cay" | Trong 15 giây, đơn xuất hiện ở cột "Chờ xác nhận" kèm ghi chú |
| TC-32 | US-S03, C07 | Nhân viên bấm "Bắt đầu làm" | Đơn sang cột "Đang chuẩn bị"; khách tải lại chi tiết đơn thấy "Đang chuẩn bị" |
| TC-33 | US-C08 | Khách hủy đơn đang `preparing` | Không có nút Hủy; gọi thẳng API thì nhận 409 |
| TC-34 | US-S03 | Hai nhân viên cùng bấm "Bắt đầu làm" một đơn | Người sau thấy "đã được cập nhật bởi người khác", danh sách làm mới |
| TC-35 | US-S07 | Nhân viên hủy đơn `pending`, lý do "Hết nguyên liệu" | Đơn biến mất khỏi màn hình quầy; khách thấy "Đã hủy" kèm lý do; tồn kho được hoàn lại |
| TC-36 | US-S07 | Lý do hủy "ok" (2 ký tự) | "Nhập lý do hủy (tối thiểu 3 ký tự)", đơn không đổi |
| TC-37 | US-S04 | Nhân viên chuyển một món sang "Ngừng bán" | Sau tối đa 30 giây (cache thực đơn), khách thấy "Hết món", nút Thêm bị vô hiệu |

TC-35 kiểm tra cả dữ liệu phía sau giao diện (tồn kho được hoàn lại): mở Swagger hoặc SSMS để xác nhận. TC-37 cho thấy một quyết định cache ở Chương 3 trở thành một kết quả mong đợi có thể đo được.

### 6.4.2. Velocity (CLO4)

**Velocity** là tổng story point thực sự hoàn thành (đạt Definition of Done) trong một sprint [6]. Story làm dở không được tính. Sau hai sprint, nhóm có số liệu thật để lập kế hoạch:

| Sprint | Cam kết (SP) | Hoàn thành (SP) | Nguyên nhân chênh lệch |
|---|---|---|---|
| 1 | 21 | 13 | Chưa quen App Router; ước lượng thấp việc viết test case |
| 2 | 18 | 16 | Đăng nhập mất thêm một ngày vì lỗi cookie |

Sprint 3 chuyển sang backend của nhóm (Chương 7), nên kế hoạch phải tính thêm việc xây module quản trị và stored procedure. Cam kết Sprint 3 không vượt quá trung bình velocity của hai sprint đầu (ví dụ trên: khoảng 14–15 SP).

### 6.4.3. Báo cáo Sprint 2 (CLO3)

Báo cáo Sprint 2 theo cùng cấu trúc 6 mục của báo cáo Sprint 1 (Chương 3), bổ sung: ma trận phân quyền (Chương 5), sơ đồ trạng thái đơn, sơ đồ thành phần có đánh dấu Server/Client, kết quả test case form, phân quyền và luồng nghiệp vụ, bảng velocity.

## Tóm tắt chương

- Server Action là endpoint công khai: luôn kiểm tra quyền và dữ liệu bên trong; `useActionState` nối form với Server Action.
- `revalidatePath` làm mới trang sau khi ghi; `useOptimistic` hiện ngay kết quả mong đợi, chỉ dùng cho thao tác hiếm khi thất bại.
- Bảng quản trị: lọc và phân trang trong URL, sắp xếp trong state, dữ liệu từ API; TanStack Table quản lý logic bảng.
- Màn hình quầy bám sơ đồ trạng thái (BR-15); xung đột đồng thời được stored procedure chặn và giao diện hiển thị rõ.
- Test luồng nghiệp vụ cần nhiều vai trò, nhiều phiên; velocity là cơ sở lập kế hoạch sprint.

## Câu hỏi ôn tập

1. Vì sao trang `/admin/orders` đã được bảo vệ mà Server Action `advanceStatus` vẫn phải gọi `requireRole`?
2. `useActionState` trả về những gì? Mỗi giá trị dùng để làm gì?
3. Nếu quên `revalidatePath` trong `advanceStatus`, nhân viên thấy gì sau khi bấm nút?
4. Thao tác nào trên màn hình quầy nên dùng cập nhật lạc quan, thao tác nào không? Vì sao?
5. Vì sao lọc và phân trang nên nằm trong URL?
6. Hai nhân viên cùng bấm một đơn. Lớp nào trong hệ thống quyết định ai thành công?
7. Sprint 1 cam kết 21 SP, hoàn thành 13 SP; Sprint 2 cam kết 18 SP, hoàn thành 16 SP. Đề xuất mức cam kết Sprint 3 và giải thích.

## Bài tập

1. **Đơn của tôi.** Trang `/orders` và `/orders/[id]` cho khách: lịch sử, chi tiết, hủy đơn `pending` có xác nhận.
2. **Lọc trạng thái.** Thêm bộ lọc `?status=` cho màn hình quầy, trạng thái lọc hiện rõ trên giao diện.
3. **Sơ đồ trạng thái.** Vẽ sơ đồ trạng thái cho thực thể chính của đề tài nhóm và liệt kê các chuyển trạng thái bị cấm.

## Tài liệu tham khảo

[1] Vercel, “Updating Data,” *Next.js Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/mutating-data

[2] Meta Open Source, “useActionState,” *React Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react.dev/reference/react/useActionState

[3] Vercel, “revalidatePath,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/functions/revalidatePath

[4] Meta Open Source, “useOptimistic,” *React Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react.dev/reference/react/useOptimistic

[5] TanStack, “Introduction,” *TanStack Table Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://tanstack.com/table/latest/docs/overview

[6] K. Schwaber and J. Sutherland, “The Scrum Guide,” Nov. 2020. Accessed: Oct. 30, 2026. [Online]. Available: https://scrumguides.org/scrum-guide.html
