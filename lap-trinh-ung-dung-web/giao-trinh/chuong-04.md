# Chương 4. Client Components, trạng thái và form

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Phân tích phần nào của trang cần chạy phía client và giữ phần đó nhỏ nhất.
- Phân biệt các loại trạng thái và quản lý giỏ hàng bằng Zustand có lưu vào `localStorage`.
- Nhận diện và xử lý lỗi hydration.
- Xây dựng form kiểm tra dữ liệu ở cả client và server bằng một schema Zod dùng chung.
- Gọi API ghi dữ liệu qua Server Action, xử lý lỗi 400/409, thiết kế test case giá trị biên.

## 4.1. Client Component và "đảo tương tác"

### 4.1.1. Khi nào cần Client Component

Một component cần chạy ở trình duyệt khi nó cần một trong ba thứ [1]:

- **Trạng thái** thay đổi theo thao tác người dùng (`useState`, `useReducer`).
- **Sự kiện** (`onClick`, `onChange`, `onSubmit` có xử lý bằng JavaScript).
- **API của trình duyệt** (`localStorage`, `window`, `AudioContext`, camera).

Nếu không cần cả ba, để nó là Server Component.

### 4.1.2. Đảo tương tác

Trang chi tiết món vẫn là Server Component lấy dữ liệu trên server (Chương 3). Chỉ nút "Thêm vào giỏ" cần biết người dùng bấm, nên chỉ nút đó là Client Component. Phần còn lại của trang không gửi JavaScript xuống trình duyệt. Cách tổ chức này gọi là **đảo tương tác** (islands): trang là "biển" HTML tĩnh, xen vài "đảo" nhỏ chạy JavaScript.

```tsx
// components/add-to-cart-button.tsx
'use client';
import { useCart } from '@/lib/cart-store';
import type { Product } from '@/lib/types';

export function AddToCartButton({ product }: { product: Product }) {
  const add = useCart((s) => s.add);
  const soldOut = !product.isAvailable || product.stock === 0;
  return (
    <button disabled={soldOut} onClick={() => add(product)}
      className="rounded bg-blue-900 px-4 py-2 text-white disabled:bg-slate-300">
      {soldOut ? 'Hết món' : 'Thêm vào giỏ'}
    </button>
  );
}

// app/(shop)/product/[id]/page.tsx (Server Component) chỉ cần:
//   <AddToCartButton product={product} />
```

Props truyền từ Server sang Client Component phải tuần tự hóa được. `product` là object thường lấy từ API nên truyền được; một hàm hay đối tượng `Date` thì không.

## 4.2. Trạng thái của ứng dụng web

### 4.2.1. Ba loại trạng thái

| Loại | Ví dụ LHU Food | Nơi giữ |
|---|---|---|
| Trạng thái từ server | Thực đơn, đơn hàng, báo cáo | API; lấy trong Server Component, làm mới bằng revalidate |
| Trạng thái trên URL | Danh mục đang lọc, từ khóa, trang hiện tại | `searchParams` (Chương 3) |
| Trạng thái của trình duyệt | Giỏ hàng chưa đặt, hộp thoại đang mở | Client Component: `useState` hoặc store chung |

Sai lầm hay gặp là chép dữ liệu server vào state của trình duyệt rồi tự đồng bộ. Trên Next.js, dữ liệu server nên ở lại server; trình duyệt chỉ giữ những gì thật sự thuộc về phiên làm việc của người dùng.

### 4.2.2. Giỏ hàng với Zustand

Giỏ hàng được dùng ở nhiều nơi: nút thêm món, biểu tượng giỏ trên header, trang giỏ hàng. Truyền props qua nhiều tầng rất rối, nên dùng một **store chung**. Học phần dùng Zustand (cùng thư viện với giáo trình di động) [2]. Middleware `persist` lưu giỏ vào `localStorage`, tải lại trang vẫn còn.

```ts
// lib/cart-store.ts   (npm install zustand)
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { Product } from './types';

export type CartItem = { productId: number; name: string; price: number; quantity: number };

type CartState = {
  items: CartItem[];
  add: (p: Product) => void;
  setQuantity: (productId: number, quantity: number) => void;
  clear: () => void;
};

export const useCart = create<CartState>()(
  persist(
    (set) => ({
      items: [],
      add: (p) => set((s) => {
        const found = s.items.find((i) => i.productId === p.id);
        return found
          ? { items: s.items.map((i) => i.productId === p.id ? { ...i, quantity: i.quantity + 1 } : i) }
          : { items: [...s.items, { productId: p.id, name: p.name, price: p.price, quantity: 1 }] };
      }),
      setQuantity: (productId, quantity) => set((s) => ({
        items: quantity <= 0
          ? s.items.filter((i) => i.productId !== productId)          // về 0 thì xóa (US-C02)
          : s.items.map((i) => i.productId === productId ? { ...i, quantity } : i),
      })),
      clear: () => set({ items: [] }),
    }),
    { name: 'lhu-food-cart' },
  ),
);

export const cartTotal = (items: CartItem[]) => items.reduce((t, i) => t + i.price * i.quantity, 0);
```

Các hàm cập nhật tạo **mảng mới** thay vì sửa mảng cũ (`push`, gán trực tiếp), vì React và Zustand so sánh tham chiếu để biết có cần vẽ lại hay không. Hành vi "thêm trùng thì cộng dồn" và "giảm về 0 thì xóa" là tiêu chí chấp nhận của US-C01, US-C02 (SRS mục 4.7) và sẽ được kiểm thử tự động ở Chương 10.

### 4.2.3. Giá trong giỏ không phải giá tính tiền

Giỏ hàng chỉ lưu `productId`, tên, giá để **hiển thị**. Giá tính tiền thật luôn do backend lấy từ CSDL lúc đặt (tiêu chí US-C04), nên người dùng sửa `localStorage` cũng không đổi được giá. Nguyên tắc chung: không tin dữ liệu do trình duyệt gửi lên.

## 4.3. Lỗi hydration

### 4.3.1. Hydration là gì

Client Component được render hai lần: một lần trên server để tạo HTML, một lần ở trình duyệt để gắn sự kiện vào HTML đó. Bước thứ hai gọi là **hydration**. React yêu cầu kết quả hai lần phải giống nhau; khác nhau thì báo lỗi "Hydration failed" [3].

### 4.3.2. Giỏ hàng gây lỗi hydration thế nào

Server không có `localStorage` nên HTML từ server luôn có giỏ rỗng (0 món); trình duyệt đọc được giỏ có 3 món. Biểu tượng giỏ hiện "0" trên server và "3" ở trình duyệt: lỗi hydration. Cách xử lý: chỉ hiển thị số liệu giỏ sau khi component đã gắn vào trình duyệt.

```tsx
// components/cart-badge.tsx
'use client';
import { useEffect, useState } from 'react';
import { useCart } from '@/lib/cart-store';

export function CartBadge() {
  const [mounted, setMounted] = useState(false);
  const count = useCart((s) => s.items.reduce((n, i) => n + i.quantity, 0));
  useEffect(() => setMounted(true), []);
  return <span className="rounded-full bg-amber-400 px-2 text-sm">{mounted ? count : 0}</span>;
}
```

Các nguyên nhân hydration khác hay gặp: hiển thị `new Date()` hay `Math.random()` khi render, định dạng ngày giờ theo múi giờ của máy (server và trình duyệt khác múi giờ), lồng thẻ HTML sai (`<p>` trong `<p>`).

## 4.4. Form có kiểm tra dữ liệu

### 4.4.1. Kiểm tra ở hai phía

Kiểm tra ở trình duyệt giúp người dùng sửa lỗi ngay, nhưng ai cũng tắt được JavaScript hoặc gửi request thẳng tới server. Vì vậy **server luôn kiểm tra lại**. Để hai phía không lệch nhau, viết schema bằng Zod một lần trong `lib/schemas.ts` và dùng cho cả form lẫn Server Action [4].

```ts
// lib/schemas.ts   (npm install zod react-hook-form @hookform/resolvers)
import { z } from 'zod';

export const registerSchema = z.object({
  fullName: z.string().trim().min(2, 'Họ tên tối thiểu 2 ký tự').max(100, 'Họ tên tối đa 100 ký tự'),
  email: z.string().trim().toLowerCase().email('Email không đúng định dạng'),
  password: z.string().min(8, 'Mật khẩu tối thiểu 8 ký tự'),
  confirm: z.string(),
}).refine((d) => d.password === d.confirm, { path: ['confirm'], message: 'Mật khẩu nhập lại không khớp' });

export type RegisterInput = z.infer<typeof registerSchema>;
```

`z.infer` sinh kiểu TypeScript từ schema, nên kiểu dữ liệu và quy tắc kiểm tra luôn khớp nhau.

### 4.4.2. Server Action

**Server Action** là hàm `async` trong file có chỉ thị `'use server'`. Client Component gọi nó như một hàm bình thường; Next.js tự tạo request POST tới server [5]. Chương 6 học kỹ hơn; ở đây dùng Server Action để đăng ký tài khoản.

```ts
// app/(shop)/register/actions.ts
'use server';
import { registerSchema, type RegisterInput } from '@/lib/schemas';

export type ActionResult = { ok: boolean; message?: string };

export async function registerAction(input: RegisterInput): Promise<ActionResult> {
  const parsed = registerSchema.safeParse(input);               // kiểm tra lại ở server
  if (!parsed.success) return { ok: false, message: parsed.error.issues[0].message };

  const { confirm, ...body } = parsed.data;
  const res = await fetch(`${process.env.API_URL}/auth/register`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body),
  });
  if (res.status === 409) return { ok: false, message: 'Email đã được sử dụng' };
  if (!res.ok) return { ok: false, message: 'Đăng ký chưa thành công, vui lòng thử lại' };
  return { ok: true };
}
```

### 4.4.3. Form với React Hook Form

React Hook Form quản lý giá trị và lỗi của form mà không vẽ lại cả form ở mỗi phím gõ; `zodResolver` nối nó với schema Zod [6].

```tsx
// app/(shop)/register/register-form.tsx
'use client';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useRouter } from 'next/navigation';
import { useState } from 'react';
import { registerSchema, type RegisterInput } from '@/lib/schemas';
import { registerAction } from './actions';

export function RegisterForm() {
  const router = useRouter();
  const [serverError, setServerError] = useState('');
  const { register, handleSubmit, formState: { errors, isSubmitting } } =
    useForm<RegisterInput>({ resolver: zodResolver(registerSchema) });

  const onSubmit = async (data: RegisterInput) => {
    const result = await registerAction(data);
    if (result.ok) router.push('/login?registered=1');
    else setServerError(result.message ?? '');
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-3">
      <label className="block">Họ tên
        <input {...register('fullName')} className="w-full rounded border px-3 py-2" />
      </label>
      {errors.fullName && <p className="text-sm text-red-600">{errors.fullName.message}</p>}
      {/* email, password, confirm: tương tự */}
      {serverError && <p role="alert" className="text-red-600">{serverError}</p>}
      <button disabled={isSubmitting} className="rounded bg-blue-900 px-4 py-2 text-white">
        {isSubmitting ? 'Đang gửi…' : 'Đăng ký'}
      </button>
    </form>
  );
}
```

Ba yêu cầu giao diện từ tiêu chí US-G04: lỗi hiện **dưới từng ô**, bằng tiếng Việt; lỗi từ server (409) hiện ở vùng chung có `role="alert"` để trình đọc màn hình đọc ngay; nút gửi bị vô hiệu khi đang gửi để tránh gửi hai lần.

## 4.5. Ghi dữ liệu qua API và kiểm thử form

### 4.5.1. Đặt món qua API mẫu

`POST /orders` cần đăng nhập, nhưng Chương 5 mới làm đăng nhập. Trong lúc chờ, lấy tạm access token ở trang `/docs` của API mẫu và đọc qua **một hàm duy nhất**. Chương 5 chỉ cần sửa hàm này.

```ts
// lib/session.ts: TẠM THỜI cho Chương 4, Chương 5 thay bằng cookie
import 'server-only';
export async function getAccessToken() {
  return process.env.DEV_ACCESS_TOKEN;   // token hết hạn sau 15 phút: lấy lại ở /docs khi gặp 401
}
```

```ts
// app/(shop)/checkout/actions.ts
'use server';
import { z } from 'zod';
import { getAccessToken } from '@/lib/session';

const orderSchema = z.object({
  items: z.array(z.object({ productId: z.number().int().positive(), quantity: z.number().int().min(1).max(50) }))
          .min(1, 'Giỏ hàng đang trống'),
  note: z.string().trim().max(200, 'Ghi chú tối đa 200 ký tự').optional(),
});

export async function placeOrder(input: z.infer<typeof orderSchema>) {
  const parsed = orderSchema.safeParse(input);
  if (!parsed.success) return { ok: false as const, message: parsed.error.issues[0].message };

  const res = await fetch(`${process.env.API_URL}/orders`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${await getAccessToken()}` },
    body: JSON.stringify(parsed.data),
  });
  if (res.status === 409) return { ok: false as const, message: 'Có món đã hết hoặc không đủ số lượng' };
  if (res.status === 401) return { ok: false as const, message: 'Bạn cần đăng nhập để đặt món' };
  if (!res.ok) return { ok: false as const, message: 'Đặt món chưa thành công, vui lòng thử lại' };
  const order: { orderId: number } = await res.json();
  return { ok: true as const, orderId: order.orderId };
}
```

API trả lỗi theo dạng `{ statusCode, message, error }`; với lỗi 400, `message` có thể là mảng chi tiết từng trường. Thiếu tồn kho trả 409 và không tạo đơn, không trừ tồn kho của bất kỳ món nào (tiêu chí US-C04, giao dịch trong stored procedure). Trang `/checkout` lấy `items` từ giỏ, gửi kèm ghi chú; thành công thì xóa giỏ và chuyển tới `/orders/{orderId}`.

### 4.5.2. Phân tích giá trị biên (CLO2)

Lỗi phần mềm hay xảy ra **ở biên** của điều kiện: 7 ký tự hay 8 ký tự, số lượng 0 hay 1. Phân tích giá trị biên chọn dữ liệu thử ngay dưới biên (phải bị từ chối) và đúng biên (phải được chấp nhận) cho mỗi ràng buộc.

| Mã | Trường / story | Dữ liệu vào | Kết quả mong đợi |
|---|---|---|---|
| TC-11 | Họ tên · US-G04 | "A" (1 ký tự) | "Họ tên tối thiểu 2 ký tự" dưới ô Họ tên |
| TC-12 | Họ tên · US-G04 | "An" (2 ký tự) | Không báo lỗi ô Họ tên |
| TC-13 | Mật khẩu · US-G04 | 7 ký tự / 8 ký tự | 7: báo lỗi; 8: hợp lệ |
| TC-14 | Nhập lại · US-G04 | Khác mật khẩu 1 ký tự | "Mật khẩu nhập lại không khớp" |
| TC-15 | Email · US-G04 | Email đã đăng ký | "Email đã được sử dụng" (API 409) |
| TC-16 | Giỏ hàng · US-C01 | Thêm cùng một món 2 lần | Một dòng, số lượng 2 |
| TC-17 | Đặt món · US-C04 | Số lượng lớn hơn tồn kho | "Có món đã hết hoặc không đủ số lượng", giỏ còn nguyên |

Chạy thêm một lần với JavaScript bị tắt hoặc gửi request trực tiếp tới Server Action: dữ liệu sai vẫn phải bị từ chối. Đó là bằng chứng server có kiểm tra lại.

## Tóm tắt chương

- Client Component chỉ khi cần state, sự kiện hoặc API trình duyệt; đặt ở lá, giữ nhỏ nhất.
- Dữ liệu server ở lại server, bộ lọc ở URL, giỏ hàng ở store Zustand có `persist`.
- Hydration lỗi khi HTML server khác trình duyệt; với giỏ hàng, chỉ hiện số liệu sau khi đã gắn vào trình duyệt.
- Một schema Zod cho cả form (React Hook Form) và Server Action; server luôn kiểm tra lại.
- Phân tích giá trị biên: mỗi ràng buộc có test ngay dưới biên và đúng biên.

## Câu hỏi ôn tập

1. Nêu ba lý do một component phải là Client Component.
2. Vì sao không đặt `"use client"` ở `page.tsx` để "cho chắc"?
3. Bộ lọc danh mục nên giữ trong `useState` hay trên URL? Vì sao?
4. Vì sao hàm `add` của giỏ hàng tạo mảng mới thay vì `push` vào mảng cũ?
5. Mô tả cơ chế gây lỗi hydration ở biểu tượng giỏ hàng và cách sửa.
6. Form đã kiểm tra ở trình duyệt. Nêu hai cách người dùng vượt qua lớp kiểm tra đó.
7. Ràng buộc "số lượng từ 1 đến 50": chọn bốn giá trị biên để kiểm thử.

## Bài tập

1. **Trang giỏ hàng.** Xây `/cart`: tăng, giảm, xóa món, tổng tiền dạng "75.000 đ", nút Đặt món chuyển tới `/checkout`.
2. **Form góp ý.** Form "Góp ý căn tin" có kiểm tra Zod ở hai phía (xem bài tập hướng dẫn) và bảng giá trị biên 8 test case.
3. **Tìm lỗi hydration.** Hiển thị giờ hiện tại trên header bằng `new Date().toLocaleTimeString()`, quan sát lỗi, rồi sửa.

## Tài liệu tham khảo

[1] Vercel, “Server and Client Components,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/server-and-client-components

[2] Poimandres, “Zustand: Introduction,” *Zustand Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://zustand.docs.pmnd.rs/learn/getting-started/introduction

[3] Meta Open Source, “hydrateRoot,” *React Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react.dev/reference/react-dom/client/hydrateRoot

[4] Zod, “Basic usage,” *Zod Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://zod.dev/basics

[5] Vercel, “Updating Data,” *Next.js Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/mutating-data

[6] React Hook Form, “Get Started,” *React Hook Form Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react-hook-form.com/get-started
