<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 06 - Server Actions, bảng dữ liệu &amp; màn hình quầy (5 tiết: 1 LT / 4 TH) · Checkpoint Sprint 2</strong></p>
        <p><em>11 giờ 30, quầy căn tin có 20 đơn chờ. Hai nhân viên cùng bấm "Bắt đầu làm" một đơn. Một khách vừa hủy đơn mà bếp đã nấu xong. Màn hình quầy không chỉ là một bảng dữ liệu đẹp: nó phải đúng trình tự nghiệp vụ, phản hồi tức thì và báo lỗi rõ ràng khi hai người tranh nhau một đơn.</em></p>
        <p><strong>Mục tiêu:</strong> Thực hiện được thao tác ghi dữ liệu bằng Server Actions với <code>useActionState</code>, <code>revalidatePath</code> và <code>useOptimistic</code>; xây dựng được bảng dữ liệu có lọc, sắp xếp, phân trang theo URL; xây dựng được màn hình quầy chuyển trạng thái đúng trình tự; kiểm thử được luồng "khách đặt → nhân viên xử lý"; báo cáo được kết quả Sprint 2.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Server Actions:</strong> <code>useActionState</code>, <code>revalidatePath</code>, xử lý lỗi, cập nhật lạc quan với <code>useOptimistic</code>.</li>
            <li><strong>Ý chính 2 - Bảng dữ liệu:</strong> TanStack Table, lọc và phân trang qua tham số URL.</li>
            <li><strong>Ý chính 3 - Màn hình quầy:</strong> đơn theo trạng thái, chuyển trạng thái đúng trình tự, hủy kèm lý do, xử lý 409.</li>
            <li><strong>Ý chính 4 - Kiểm thử luồng và báo cáo Sprint 2:</strong> test case theo tiêu chí nghiệm thu, velocity, Checkpoint Sprint 2.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Màn hình quầy (US-S02, S03, S06, S07) và bảng món cho nhân viên (US-S04) chạy với API mẫu; nhóm demo được luồng đặt món trên web → nhân viên xử lý và hoàn thành Checkpoint Sprint 2.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2, CLO3, CLO4.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Server Actions</h3>
            <p>Server Action là hàm <code>async</code> có chỉ thị <code>'use server'</code>, chạy trên server nhưng được gọi từ form hoặc Client Component. Không cần tự viết Route Handler cho từng thao tác ghi. Mỗi Server Action là một endpoint công khai, nên <strong>luôn kiểm tra quyền và dữ liệu bên trong nó</strong>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/orders/actions.ts
'use server';
import { revalidatePath } from 'next/cache';
import { z } from 'zod';
import { requireRole } from '@/lib/dal';
import { apiAuth, ApiError } from '@/lib/api';

export type NextStatus = 'preparing' | 'ready' | 'completed';
export type ActionResult = { ok: boolean; message?: string };

export async function advanceStatus(orderId: number, status: NextStatus): Promise&lt;ActionResult&gt; {
  await requireRole('staff', 'admin');                       // kiểm tra quyền ở chính Server Action
  try {
    await apiAuth(`/orders/${orderId}/status`, { method: 'PATCH', body: JSON.stringify({ status }) });
    return { ok: true };
  } catch (e) {
    if (e instanceof ApiError &amp;&amp; e.status === 409)
      return { ok: false, message: `Đơn #${orderId} đã được cập nhật bởi người khác` };
    return { ok: false, message: 'Không cập nhật được trạng thái, vui lòng thử lại' };
  } finally {
    revalidatePath('/admin/orders');                         // vẽ lại trang với dữ liệu mới
  }
}

const cancelSchema = z.object({
  orderId: z.coerce.number().int().positive(),
  reason: z.string().trim().min(3, 'Nhập lý do hủy (tối thiểu 3 ký tự)').max(200, 'Lý do tối đa 200 ký tự'),
});

// Dùng với useActionState: nhận state trước và FormData
export async function staffCancel(_prev: ActionResult, formData: FormData): Promise&lt;ActionResult&gt; {
  await requireRole('staff', 'admin');
  const parsed = cancelSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { ok: false, message: parsed.error.issues[0].message };
  try {
    await apiAuth(`/orders/${parsed.data.orderId}/staff-cancel`, {
      method: 'POST', body: JSON.stringify({ reason: parsed.data.reason }),
    });
  } catch (e) {
    if (e instanceof ApiError &amp;&amp; e.status === 409) return { ok: false, message: 'Đơn đã sẵn sàng hoặc đã hoàn tất, không hủy được' };
    return { ok: false, message: 'Không hủy được đơn, vui lòng thử lại' };
  }
  revalidatePath('/admin/orders');
  return { ok: true, message: 'Đã hủy đơn và báo cho khách' };
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li><code>useActionState(action, initialState)</code> (từ <code>react</code>) trả về <code>[state, formAction, isPending]</code>: hiện thông báo lỗi và vô hiệu nút khi đang gửi.</li>
                <li><code>revalidatePath</code> xóa cache của trang để lần render sau lấy dữ liệu mới. Không cần tự gọi lại API ở client.</li>
                <li><code>useOptimistic</code> hiện ngay kết quả mong đợi trong lúc chờ server; nếu Server Action thất bại, giao diện tự trở về dữ liệu thật sau khi trang được làm mới.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Bảng dữ liệu với TanStack Table</h3>
            <p>Trang <code>/admin/products</code> cho nhân viên xem cả món ngừng bán (<code>includeUnavailable=true</code>) và bật/tắt "còn bán" (US-S04). Lọc và phân trang đặt trong URL (<code>?q=com&amp;page=2</code>) để Server Component gọi API đúng trang, tải lại hoặc gửi link vẫn giữ nguyên bộ lọc. TanStack Table lo phần hiển thị và sắp xếp cột trên trang hiện tại.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/products/page.tsx (Server Component)
const PAGE_SIZE = 20;
type Props = { searchParams: Promise&lt;{ q?: string; page?: string }&gt; };

export default async function ProductsPage({ searchParams }: Props) {
  await requireRole('staff', 'admin');
  const { q = '', page = '1' } = await searchParams;
  const query = new URLSearchParams({ includeUnavailable: 'true', page, pageSize: String(PAGE_SIZE) });
  if (q) query.set('keyword', q);
  const products = await apiAuth&lt;Product[]&gt;(`/products?${query}`);
  return &lt;ProductTable data={products} page={Number(page)} q={q} hasNext={products.length === PAGE_SIZE} /&gt;;
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/products/product-table.tsx   (npm install @tanstack/react-table)
'use client';
import { useState } from 'react';
import Link from 'next/link';
import { flexRender, getCoreRowModel, getSortedRowModel, useReactTable,
         type ColumnDef, type SortingState } from '@tanstack/react-table';
import type { Product } from '@/lib/types';
import { toggleAvailability } from './actions';

const columns: ColumnDef&lt;Product&gt;[] = [
  { accessorKey: 'name', header: 'Tên món' },
  { accessorKey: 'categoryName', header: 'Danh mục' },
  { accessorKey: 'price', header: 'Giá', cell: (c) =&gt; `${c.getValue&lt;number&gt;().toLocaleString('vi-VN')} đ` },
  { accessorKey: 'stock', header: 'Tồn' },
  { id: 'available', header: 'Còn bán', cell: ({ row }) =&gt; (
      &lt;form action={toggleAvailability.bind(null, row.original.id, !row.original.isAvailable)}&gt;
        &lt;button className="underline"&gt;{row.original.isAvailable ? 'Đang bán' : 'Ngừng bán'}&lt;/button&gt;
      &lt;/form&gt;) },
];

export function ProductTable({ data, page, q, hasNext }:
  { data: Product[]; page: number; q: string; hasNext: boolean }) {
  const [sorting, setSorting] = useState&lt;SortingState&gt;([]);
  const table = useReactTable({ data, columns, state: { sorting }, onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(), getSortedRowModel: getSortedRowModel() });
  const href = (p: number) =&gt; `?${new URLSearchParams({ q, page: String(p) })}`;
  return (
    &lt;&gt;
      &lt;table className="w-full text-sm"&gt;
        &lt;thead&gt;{table.getHeaderGroups().map((g) =&gt; (
          &lt;tr key={g.id}&gt;{g.headers.map((h) =&gt; (
            &lt;th key={h.id} onClick={h.column.getToggleSortingHandler()} className="cursor-pointer text-left"&gt;
              {flexRender(h.column.columnDef.header, h.getContext())}
              {{ asc: ' ▲', desc: ' ▼' }[h.column.getIsSorted() as string] ?? ''}
            &lt;/th&gt;))}&lt;/tr&gt;))}
        &lt;/thead&gt;
        &lt;tbody&gt;{table.getRowModel().rows.map((r) =&gt; (
          &lt;tr key={r.id}&gt;{r.getVisibleCells().map((c) =&gt; (
            &lt;td key={c.id}&gt;{flexRender(c.column.columnDef.cell, c.getContext())}&lt;/td&gt;))}&lt;/tr&gt;))}
        &lt;/tbody&gt;
      &lt;/table&gt;
      &lt;nav className="mt-3 flex gap-3"&gt;
        {page &gt; 1 &amp;&amp; &lt;Link href={href(page - 1)}&gt;← Trang trước&lt;/Link&gt;}
        {hasNext &amp;&amp; &lt;Link href={href(page + 1)}&gt;Trang sau →&lt;/Link&gt;}
      &lt;/nav&gt;
    &lt;/&gt;
  );
}</code></pre>
            <p style="margin-bottom: 0;">API mẫu trả về mảng, không có tổng số dòng: còn trang sau khi số phần tử bằng <code>pageSize</code>. <code>toggleAvailability</code> là Server Action gọi <code>PATCH /products/:id/availability</code>, kiểm tra quyền staff và <code>revalidatePath('/admin/products')</code>. Với shadcn/ui, có thể dùng mẫu "Data Table" (<code>npx shadcn@latest add table</code>) dựng sẵn trên TanStack Table.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Màn hình quầy</h3>
            <p><strong>Phân tích nghiệp vụ (CLO1).</strong> Trạng thái đơn chỉ đi một chiều theo quy tắc BR-15:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>pending ──"Bắt đầu làm"──▶ preparing ──"Đã xong"──▶ ready ──"Đã giao"──▶ completed
   │ khách hủy (US-C08)         │
   └── nhân viên hủy kèm lý do (US-S07) ──▶ cancelled</code></pre>
            <p>Trang <code>/admin/orders</code> là Server Component gọi <code>GET /orders/staff</code> (mặc định trả đơn <code>pending</code>, <code>preparing</code>, <code>ready</code> trong ngày), chia thành ba cột. Lọc trạng thái (US-S06) qua tham số <code>?status=</code>. Mỗi đơn là một Client Component nhỏ:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/orders/order-card.tsx
'use client';
import { useOptimistic, useState, useTransition } from 'react';
import { advanceStatus, type NextStatus } from './actions';

type StaffOrder = { orderId: number; status: string; note: string | null; createdAt: string;
                    customerName: string; total: number; summary: string };

const NEXT: Record&lt;string, { to: NextStatus; label: string } | undefined&gt; = {
  pending: { to: 'preparing', label: 'Bắt đầu làm' },
  preparing: { to: 'ready', label: 'Đã xong' },
  ready: { to: 'completed', label: 'Đã giao' },
};
const LABEL: Record&lt;string, string&gt; = {
  pending: 'Chờ xác nhận', preparing: 'Đang chuẩn bị', ready: 'Sẵn sàng', completed: 'Hoàn tất', cancelled: 'Đã hủy',
};

export function OrderCard({ order }: { order: StaffOrder }) {
  const [status, setOptimisticStatus] = useOptimistic(order.status);
  const [isPending, startTransition] = useTransition();
  const [error, setError] = useState('');
  const next = NEXT[status];

  const onAdvance = () =&gt; next &amp;&amp; startTransition(async () =&gt; {
    setError('');
    setOptimisticStatus(next.to);                       // hiện ngay, chưa chờ server
    const result = await advanceStatus(order.orderId, next.to);
    if (!result.ok) setError(result.message ?? '');
  });

  return (
    &lt;article className="rounded-xl border bg-white p-3"&gt;
      &lt;p className="font-bold"&gt;#{order.orderId} · {order.customerName}&lt;/p&gt;
      &lt;p&gt;{order.summary}&lt;/p&gt;
      {order.note &amp;&amp; &lt;p className="text-amber-700"&gt;Ghi chú: {order.note}&lt;/p&gt;}
      &lt;p className="text-sm"&gt;Trạng thái: &lt;strong&gt;{LABEL[status]}&lt;/strong&gt;&lt;/p&gt;
      {next &amp;&amp; &lt;button onClick={onAdvance} disabled={isPending}
        className="mt-2 rounded bg-blue-900 px-3 py-1 text-white"&gt;{next.label}&lt;/button&gt;}
      {error &amp;&amp; &lt;p role="alert" className="text-sm text-red-600"&gt;{error}&lt;/p&gt;}
    &lt;/article&gt;
  );
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Trạng thái hiện bằng <strong>chữ</strong>, không chỉ bằng màu (người mù màu vẫn đọc được).</li>
                <li>Nút "Hủy đơn" chỉ hiện với đơn <code>pending</code>/<code>preparing</code>, mở hộp thoại nhập lý do dùng <code>useActionState(staffCancel, { ok: false })</code>.</li>
                <li><strong>Xung đột 409:</strong> khi hai nhân viên cùng bấm, API chỉ nhận người đầu; người sau thấy thông báo và danh sách được làm mới nhờ <code>revalidatePath</code>.</li>
                <li>Tạm thời làm mới danh sách mỗi 15 giây bằng một Client Component gọi <code>router.refresh()</code> trong <code>setInterval</code>. Bài 09 thay bằng Socket.IO để đơn mới hiện ngay lập tức.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Kiểm thử luồng nghiệp vụ và báo cáo Sprint 2</h3>
            <p><strong>Test case luồng "khách đặt → nhân viên xử lý" (CLO2).</strong> Mở hai trình duyệt (hoặc một cửa sổ ẩn danh): một bên đăng nhập customer, một bên đăng nhập staff.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mã</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Story</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Bước thực hiện</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả mong đợi</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-31</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-C04, S02</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Khách đặt 2 món, ghi chú "Ít cay"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Trong 15 giây, đơn xuất hiện ở cột "Chờ xác nhận" kèm ghi chú</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-32</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-S03, C07</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhân viên bấm "Bắt đầu làm"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đơn sang cột "Đang chuẩn bị"; khách tải lại chi tiết đơn thấy "Đang chuẩn bị"</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-33</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-C08</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Khách hủy đơn đang <code>preparing</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Không có nút Hủy; gọi thẳng API thì nhận 409</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-34</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-S03</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Hai nhân viên cùng bấm "Bắt đầu làm" một đơn</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Người sau thấy "đã được cập nhật bởi người khác", danh sách làm mới</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-35</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-S07</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhân viên hủy đơn <code>pending</code>, lý do "Hết nguyên liệu"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đơn biến mất khỏi màn hình quầy; khách thấy "Đã hủy" kèm lý do; tồn kho được hoàn lại</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-36</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-S07</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Lý do hủy "ok" (2 ký tự)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Nhập lý do hủy (tối thiểu 3 ký tự)", đơn không đổi</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-37</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-S04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhân viên chuyển một món sang "Ngừng bán"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Sau tối đa 30 giây (cache thực đơn), khách thấy "Hết món", nút Thêm bị vô hiệu</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Velocity và kế hoạch Sprint 3 (CLO4).</strong> Velocity là số story point thực sự hoàn thành (đạt Definition of Done) trong một sprint. Ghi bảng:</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 600px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Sprint</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Cam kết (SP)</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Hoàn thành (SP)</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Nguyên nhân chênh lệch</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">1</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">2</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;">Sprint 3 chuyển sang backend của nhóm, nên kế hoạch phải tính thêm việc xây module quản trị và stored procedure. Cam kết Sprint 3 không vượt quá trung bình velocity của hai sprint đầu. Báo cáo Sprint 2 (CLO3) theo cùng cấu trúc 6 mục của báo cáo Sprint 1 (bài 03), thêm mục ma trận phân quyền và kết quả test case bảo mật.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 06: Server Actions, bảng dữ liệu &amp; màn hình quầy</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tiêu chí US-S02, S03, S04, S06, S07, C08; quy tắc BR-15 (trình tự trạng thái); mục 8: các endpoint /orders/staff.</span>
            </a>
            <a href="{{LINK_AGILE_SCRUM}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🗂 Kế hoạch Agile &amp; Product Backlog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Velocity, release burndown, story của Sprint 3; Definition of Done.</span>
            </a>
            <a href="{{LINK_RUBRIC}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📊 Rubric chấm điểm</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tiêu chí CLO4 cá nhân: chuẩn bị bản nháp báo cáo vai trò cá nhân.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/getting-started/mutating-data" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Updating Data</span><br>
                <span style="color: #6c757d; font-size: 13px;">Server Functions, form, trạng thái chờ, revalidate sau khi ghi.</span>
            </a>
            <a href="https://react.dev/reference/react/useOptimistic" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React - useOptimistic, useActionState</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cập nhật lạc quan và quản lý trạng thái của action.</span>
            </a>
            <a href="https://tanstack.com/table/latest/docs/overview" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 TanStack Table</span><br>
                <span style="color: #6c757d; font-size: 13px;">Định nghĩa cột, sắp xếp, phân trang thủ công (manual pagination).</span>
            </a>
        </div>
    </div>
</details>

<details style="border: 1px solid #28a745; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #eafaf1; color: #28a745; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>💡 3. Hoạt động &amp; Thực hành trên lớp</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Màn hình quầy và bảng món</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tạo <code>app/admin/orders/actions.ts</code> với <code>advanceStatus</code> và <code>staffCancel</code>.</li>
                <li>Trang <code>/admin/orders</code>: ba cột theo trạng thái, <code>OrderCard</code> dùng <code>useOptimistic</code>, hộp thoại hủy đơn dùng <code>useActionState</code>, lọc <code>?status=</code>, làm mới mỗi 15 giây.</li>
                <li>Trang <code>/admin/products</code>: bảng TanStack Table có sắp xếp cột, tìm kiếm và phân trang qua URL, nút bật/tắt còn bán.</li>
                <li>Chạy TC-31…TC-37 với hai trình duyệt, ghi kết quả.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Trang "Đơn của tôi"</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Trang <code>/orders</code> liệt kê đơn của khách (<code>GET /orders</code>), mới nhất trước, có mã đơn, thời gian, tổng tiền, trạng thái bằng chữ (US-C06). Trang <code>/orders/[id]</code> hiện từng món, đơn giá lúc đặt, ghi chú, trạng thái (US-C07); nút "Hủy đơn" chỉ hiện khi <code>pending</code>, có hộp thoại xác nhận, gọi <code>POST /orders/:id/cancel</code> qua Server Action (US-C08).</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp link repo và ít nhất 5 test case kèm kết quả, trong đó có: mở đơn của tài khoản khác (mong đợi 404), hủy đơn đã <code>preparing</code> (mong đợi 409).</p>
            <a href="{{LINK_NOP_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🏁 Checkpoint Sprint 2 (1 tiết)</strong></p>
            <ul style="margin: 0 0 8px 0; color: #495057;">
                <li>Demo luồng: khách đặt món trên web → nhân viên nhận và xử lý trên màn hình quầy → khách thấy trạng thái mới.</li>
                <li><strong>Phân tích (CLO1):</strong> ma trận phân quyền, sơ đồ trạng thái đơn, sơ đồ thành phần có đánh dấu Server/Client Component.</li>
                <li><strong>Kiểm thử (CLO2):</strong> test case form (giá trị biên), phân quyền và luồng nghiệp vụ, kèm kết quả chạy.</li>
                <li><strong>Báo cáo sprint 2 (CLO3)</strong> đúng cấu trúc và quy định định dạng.</li>
                <li><strong>Kế hoạch Sprint 3 (CLO4):</strong> bảng velocity hai sprint, story Sprint 3 trên board (kể cả việc backend của nhóm); <strong>bản nháp báo cáo vai trò cá nhân</strong> của từng thành viên.</li>
            </ul>
            <a href="{{LINK_NOP_CHECKPOINT_2}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp Checkpoint 2</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Cập nhật lạc quan làm giao diện nhanh hơn, nhưng nếu server từ chối thì nhân viên đã thấy trạng thái sai trong chốc lát. Với màn hình quầy, thao tác nào nên dùng cập nhật lạc quan và thao tác nào không nên? Vì sao?</p>
            <a href="{{LINK_DIEN_DAN_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập Server Actions, revalidatePath, useOptimistic, bảng dữ liệu, trạng thái đơn, velocity.</p>
            <a href="{{LINK_QUIZ_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 06</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Bấm nút xong dữ liệu không đổi:</strong> quên <code>revalidatePath</code> hoặc đường dẫn truyền vào khác đường dẫn trang (ví dụ <code>/admin/order</code> thay vì <code>/admin/orders</code>).</p>
        <p><strong>Lỗi "An optimistic state update occurred outside a transition":</strong> gọi hàm cập nhật của <code>useOptimistic</code> ngoài <code>startTransition</code> hoặc ngoài form action.</p>
        <p><strong>Bảng báo lỗi hydration khi sắp xếp:</strong> định dạng ngày giờ bằng <code>toLocaleString()</code> cho kết quả khác nhau giữa server và trình duyệt. Truyền rõ <code>'vi-VN'</code> và múi giờ, hoặc định dạng sẵn ở Server Component.</p>
        <p><strong>Đơn mới không hiện:</strong> <code>GET /orders/staff</code> chỉ trả đơn trong ngày; kiểm tra giờ của máy chủ API và tham số <code>date</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> <code>revalidateTag</code> để làm mới theo nhóm dữ liệu thay vì theo đường dẫn; âm báo khi có đơn mới bằng Web Audio API (cần người dùng tương tác trước).</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Báo cáo Sprint 2 của nhóm bạn có giải thích được vì sao velocity thay đổi so với Sprint 1, và kế hoạch Sprint 3 có dựa vào con số đó không?</p>
    </div>
</details>
