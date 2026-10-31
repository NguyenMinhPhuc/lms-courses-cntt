# Phụ lục A. Mã nguồn đầy đủ

Các đoạn mã dài hơn 40 dòng được đặt ở phụ lục này để chương chính dễ đọc; trong chương chỉ giữ phần đầu của mỗi đoạn. Mã nguồn đầy đủ của dự án mẫu cũng có trong repo của học phần.

## A.1. 3.2.3. Trang thực đơn (Chương 3)

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
    apiGet<Product[]>(`/products?${query}`, 30),     // tồn kho đổi thường xuyên: 30 giây
  ]);

  return (
    <main className="mx-auto max-w-5xl p-6">
      <form action="/menu" className="mb-4">
        <input name="q" defaultValue={q} placeholder="Tìm món…" className="w-full rounded border px-3 py-2" />
      </form>
      <nav className="mb-4 flex gap-2 overflow-x-auto">
        {categories.map((c) => (
          <Link key={c.id} href={`/menu?category=${c.id}`} className="rounded-full border px-3 py-1">{c.name}</Link>
        ))}
      </nav>
      {products.length === 0 ? (
        <p className="text-slate-500">Không tìm thấy món phù hợp.</p>
      ) : (
        <ul className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {products.map((p) => (
            <li key={p.id} className="rounded-xl border bg-white p-4">
              <Link href={`/product/${p.id}`} className="font-bold">{p.name}</Link>
              <p>{p.price.toLocaleString('vi-VN')} đ</p>
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}
```

## A.2. 5.4.1. Lớp 1: proxy.ts (Chương 5)

```ts
// proxy.ts   (npm install jose)
import { NextResponse, type NextRequest } from 'next/server';
import { decodeJwt } from 'jose';

const RULES: { prefix: string; roles: string[] }[] = [
  { prefix: '/admin/orders', roles: ['staff', 'admin'] },
  { prefix: '/admin', roles: ['admin'] },
  { prefix: '/checkout', roles: ['customer', 'staff', 'admin'] },
  { prefix: '/orders', roles: ['customer', 'staff', 'admin'] },
  { prefix: '/profile', roles: ['customer', 'staff', 'admin'] },
];

export async function proxy(req: NextRequest) {
  const rule = RULES.find((r) => req.nextUrl.pathname.startsWith(r.prefix));
  if (!rule) return NextResponse.next();

  let access = req.cookies.get('access_token')?.value;
  const refresh = req.cookies.get('refresh_token')?.value;
  let res = NextResponse.next();

  if (!access && refresh) {                                   // access hết hạn: làm mới (mục 5.5)
    const r = await fetch(`${process.env.API_URL}/auth/refresh`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refreshToken: refresh }),
    });
    if (r.ok) {
      const t = await r.json();
      access = t.accessToken;
      req.cookies.set('access_token', t.accessToken);          // trang đang mở đọc được token mới
      res = NextResponse.next({ request: req });
      const opts = { httpOnly: true, secure: process.env.NODE_ENV === 'production', sameSite: 'lax' as const, path: '/' };
      res.cookies.set('access_token', t.accessToken, { ...opts, maxAge: 14 * 60 });
      res.cookies.set('refresh_token', t.refreshToken, { ...opts, maxAge: 7 * 24 * 3600 });
    }
  }

  if (!access) {
    const login = new URL('/login', req.url);
    login.searchParams.set('next', req.nextUrl.pathname);
    return NextResponse.redirect(login);
  }
  const { role } = decodeJwt(access) as { role: string };      // chỉ đọc, KHÔNG xác minh chữ ký
  if (!rule.roles.includes(role)) return NextResponse.rewrite(new URL('/forbidden', req.url));
  return res;
}

export const config = { matcher: ['/admin/:path*', '/checkout', '/orders/:path*', '/profile'] };
```

## A.3. 6.1.2. Server Action của màn hình quầy (Chương 6)

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
  } catch (e) {
    if (e instanceof ApiError && e.status === 409)
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
export async function staffCancel(_prev: ActionResult, formData: FormData): Promise<ActionResult> {
  await requireRole('staff', 'admin');
  const parsed = cancelSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { ok: false, message: parsed.error.issues[0].message };
  try {
    await apiAuth(`/orders/${parsed.data.orderId}/staff-cancel`, {
      method: 'POST', body: JSON.stringify({ reason: parsed.data.reason }),
    });
  } catch (e) {
    if (e instanceof ApiError && e.status === 409) return { ok: false, message: 'Đơn đã sẵn sàng hoặc đã hoàn tất, không hủy được' };
    return { ok: false, message: 'Không hủy được đơn, vui lòng thử lại' };
  }
  revalidatePath('/admin/orders');
  return { ok: true, message: 'Đã hủy đơn và báo cho khách' };
}
```

## A.4. 6.2.3. Client Component hiển thị bảng (Chương 6)

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
      <form action={toggleAvailability.bind(null, row.original.id, !row.original.isAvailable)}>
        <button className="underline">{row.original.isAvailable ? 'Đang bán' : 'Ngừng bán'}</button>
      </form>) },
];

export function ProductTable({ data, page, q, hasNext }:
  { data: Product[]; page: number; q: string; hasNext: boolean }) {
  const [sorting, setSorting] = useState<SortingState>([]);
  const table = useReactTable({ data, columns, state: { sorting }, onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(), getSortedRowModel: getSortedRowModel() });
  const href = (p: number) => `?${new URLSearchParams({ q, page: String(p) })}`;
  return (
    <>
      <table className="w-full text-sm">
        <thead>{table.getHeaderGroups().map((g) => (
          <tr key={g.id}>{g.headers.map((h) => (
            <th key={h.id} onClick={h.column.getToggleSortingHandler()} className="cursor-pointer text-left">
              {flexRender(h.column.columnDef.header, h.getContext())}
              {{ asc: ' ▲', desc: ' ▼' }[h.column.getIsSorted() as string] ?? ''}
            </th>))}</tr>))}
        </thead>
        <tbody>{table.getRowModel().rows.map((r) => (
          <tr key={r.id}>{r.getVisibleCells().map((c) => (
            <td key={c.id}>{flexRender(c.column.columnDef.cell, c.getContext())}</td>))}</tr>))}
        </tbody>
      </table>
      <nav className="mt-3 flex gap-3">
        {page > 1 && <Link href={href(page - 1)}>← Trang trước</Link>}
        {hasNext && <Link href={href(page + 1)}>Trang sau →</Link>}
      </nav>
    </>
  );
}
```

## A.5. 6.3.3. Thẻ đơn với cập nhật lạc quan (Chương 6)

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
};

export function OrderCard({ order }: { order: StaffOrder }) {
  const [status, setOptimisticStatus] = useOptimistic(order.status);
  const [isPending, startTransition] = useTransition();
  const [error, setError] = useState('');
  const next = NEXT[status];

  const onAdvance = () => next && startTransition(async () => {
    setError('');
    setOptimisticStatus(next.to);                       // hiện ngay, chưa chờ server
    const result = await advanceStatus(order.orderId, next.to);
    if (!result.ok) setError(result.message ?? '');
  });

  return (
    <article className="rounded-xl border bg-white p-3">
      <p className="font-bold">#{order.orderId} · {order.customerName}</p>
      <p>{order.summary}</p>
      {order.note && <p className="text-amber-700">Ghi chú: {order.note}</p>}
      <p className="text-sm">Trạng thái: <strong>{LABEL[status]}</strong></p>
      {next && <button onClick={onAdvance} disabled={isPending}
        className="mt-2 rounded bg-blue-900 px-3 py-1 text-white">{next.label}</button>}
      {error && <p role="alert" className="text-sm text-red-600">{error}</p>}
    </article>
  );
}
```

## A.6. 9.3.1. Socket là chuông báo (Chương 9)

```tsx
// app/admin/orders/orders-realtime.tsx
'use client';
import { useEffect, useRef, useState } from 'react';
import { useRouter } from 'next/navigation';
import { io } from 'socket.io-client';

type Conn = 'connecting' | 'online' | 'offline';
const LABEL: Record<Conn, string> = { connecting: 'Đang kết nối…', online: 'Đang nhận đơn trực tiếp', offline: 'Mất kết nối, đang thử lại…' };

export function OrdersRealtime() {
  const router = useRouter();
  const [conn, setConn] = useState<Conn>('connecting');
  const [lastOrder, setLastOrder] = useState<number | null>(null);
  const soundOn = useRef(false);

  useEffect(() => {
    const socket = io(process.env.NEXT_PUBLIC_SOCKET_URL!, {
      transports: ['websocket'],
      // auth dạng hàm: được gọi lại ở MỖI lần (kết nối lại), nên luôn có token mới
      auth: (cb) => {
        fetch('/api/socket-token', { cache: 'no-store' })
          .then((r) => (r.ok ? r.json() : { token: '' }))
          .then((d) => cb({ token: d.token }));
      },
    });

    socket.on('connect', () => { setConn('online'); router.refresh(); });   // bù các đơn lỡ khi mất kết nối
    socket.on('disconnect', () => setConn('offline'));
    socket.on('connect_error', () => {
      setConn('offline');
      setTimeout(() => socket.connect(), 3000);              // token bị từ chối: tự thử lại
    });
    socket.on('order:new', (e: { orderId: number }) => {
      setLastOrder(e.orderId);
      if (soundOn.current) beep();
      router.refresh();
    });
    socket.on('order:updated', () => router.refresh());     // nhân viên khác vừa đổi trạng thái

    return () => { socket.disconnect(); };
  }, [router]);

  return (
    <div className="flex items-center gap-3">
      <p aria-live="polite" className="text-sm">{LABEL[conn]}{lastOrder && ` · Đơn mới nhất #${lastOrder}`}</p>
      <button onClick={() => { soundOn.current = true; beep(); }} className="rounded border px-2 py-1 text-sm">
        Bật âm báo
      </button>
    </div>
  );
}

function beep() {
  const ctx = new AudioContext();
  const osc = ctx.createOscillator();
  osc.frequency.value = 880;
  osc.connect(ctx.destination);
  osc.start();
  osc.stop(ctx.currentTime + 0.2);
}
```
