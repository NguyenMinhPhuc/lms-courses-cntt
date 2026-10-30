<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 04 - Client Components, trạng thái &amp; form (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Thực đơn đã có món thật, nhưng khách vẫn chưa làm được gì ngoài nhìn. Hôm nay trang web bắt đầu "phản hồi": bấm thêm món thì giỏ hàng tăng, tải lại trang giỏ vẫn còn, điền sai email thì báo lỗi ngay dưới ô. Và câu hỏi khó hơn: kiểm tra dữ liệu ở trình duyệt rồi thì server có cần kiểm tra lại không?</em></p>
        <p><strong>Mục tiêu:</strong> Phân tích được phần nào của trang cần chạy phía client; xây dựng được giỏ hàng có lưu trạng thái; xây dựng được form kiểm tra dữ liệu ở cả client và server bằng một schema Zod dùng chung; gọi được API ghi dữ liệu và xử lý lỗi 400/409; thiết kế được test case giá trị biên cho form.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Client Component và "đảo tương tác":</strong> state, sự kiện, hook; giữ phần chạy ở trình duyệt nhỏ nhất.</li>
            <li><strong>Ý chính 2 - Trạng thái giỏ hàng:</strong> Zustand, lưu vào <code>localStorage</code>, tránh lỗi hydration.</li>
            <li><strong>Ý chính 3 - Form có kiểm tra dữ liệu:</strong> React Hook Form + Zod, một schema dùng cho cả form và Server Action.</li>
            <li><strong>Ý chính 4 - Ghi dữ liệu và kiểm thử form:</strong> đặt món qua API mẫu, hiển thị lỗi 400/409, bảng giá trị biên.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Web có giỏ hàng (US-C01, C02), form đăng ký (US-G04) và trang đặt món (US-C04) chạy với API mẫu; mỗi form có bảng giá trị biên và test case kèm kết quả.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Client Component và "đảo tương tác"</h3>
            <p>Trang chi tiết món vẫn là Server Component (lấy dữ liệu trên server, như bài 03). Chỉ nút "Thêm vào giỏ" cần biết người dùng bấm, nên chỉ nút đó là Client Component. Phần còn lại của trang không gửi JavaScript xuống trình duyệt.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// components/add-to-cart-button.tsx
'use client';
import { useCart } from '@/lib/cart-store';
import type { Product } from '@/lib/types';

export function AddToCartButton({ product }: { product: Product }) {
  const add = useCart((s) =&gt; s.add);
  const soldOut = !product.isAvailable || product.stock === 0;
  return (
    &lt;button disabled={soldOut} onClick={() =&gt; add(product)}
      className="rounded bg-blue-900 px-4 py-2 text-white disabled:bg-slate-300"&gt;
      {soldOut ? 'Hết món' : 'Thêm vào giỏ'}
    &lt;/button&gt;
  );
}

// app/(shop)/product/[id]/page.tsx (Server Component) chỉ cần:
//   &lt;AddToCartButton product={product} /&gt;</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Props truyền từ Server sang Client Component phải <strong>tuần tự hóa được</strong> (số, chuỗi, mảng, object thường). Không truyền hàm hay đối tượng <code>Date</code>.</li>
                <li>Đặt <code>"use client"</code> ở lá của cây component, không đặt ở layout hay page. Một <code>"use client"</code> ở trên cao kéo cả nhánh con xuống trình duyệt.</li>
                <li>Khi phân tích thành phần (CLO1), ghi rõ component nào chạy ở client và lý do: cần state, sự kiện hay API trình duyệt.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Trạng thái giỏ hàng với Zustand</h3>
            <p>Giỏ hàng được dùng ở nhiều nơi: nút thêm món, biểu tượng giỏ trên header, trang giỏ hàng. Dùng một store chung thay vì truyền props qua nhiều tầng. Middleware <code>persist</code> lưu giỏ vào <code>localStorage</code> nên tải lại trang vẫn còn.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/cart-store.ts   (npm install zustand)
'use client';
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { Product } from './types';

export type CartItem = { productId: number; name: string; price: number; quantity: number };

type CartState = {
  items: CartItem[];
  add: (p: Product) =&gt; void;
  setQuantity: (productId: number, quantity: number) =&gt; void;
  clear: () =&gt; void;
};

export const useCart = create&lt;CartState&gt;()(
  persist(
    (set) =&gt; ({
      items: [],
      add: (p) =&gt; set((s) =&gt; {
        const found = s.items.find((i) =&gt; i.productId === p.id);
        return found
          ? { items: s.items.map((i) =&gt; i.productId === p.id ? { ...i, quantity: i.quantity + 1 } : i) }
          : { items: [...s.items, { productId: p.id, name: p.name, price: p.price, quantity: 1 }] };
      }),
      setQuantity: (productId, quantity) =&gt; set((s) =&gt; ({
        items: quantity &lt;= 0
          ? s.items.filter((i) =&gt; i.productId !== productId)          // về 0 thì xóa (US-C02)
          : s.items.map((i) =&gt; i.productId === productId ? { ...i, quantity } : i),
      })),
      clear: () =&gt; set({ items: [] }),
    }),
    { name: 'lhu-food-cart' },
  ),
);

export const cartTotal = (items: CartItem[]) =&gt; items.reduce((t, i) =&gt; t + i.price * i.quantity, 0);</code></pre>
            <p><strong>Lỗi hydration:</strong> server không có <code>localStorage</code> nên HTML từ server luôn có giỏ rỗng; trình duyệt đọc được giỏ 3 món. Hai bản HTML khác nhau thì React báo lỗi "Hydration failed". Cách xử lý: chỉ hiển thị số liệu giỏ sau khi component đã gắn vào trình duyệt.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// components/cart-badge.tsx
'use client';
import { useEffect, useState } from 'react';
import { useCart } from '@/lib/cart-store';

export function CartBadge() {
  const [mounted, setMounted] = useState(false);
  const count = useCart((s) =&gt; s.items.reduce((n, i) =&gt; n + i.quantity, 0));
  useEffect(() =&gt; setMounted(true), []);
  return &lt;span className="rounded-full bg-amber-400 px-2 text-sm"&gt;{mounted ? count : 0}&lt;/span&gt;;
}</code></pre>
            <p style="margin-bottom: 0;">Giỏ hàng chỉ lưu <code>productId</code>, tên, giá để hiển thị. Giá tính tiền thật luôn do backend lấy từ CSDL lúc đặt (tiêu chí US-C04), nên sửa <code>localStorage</code> cũng không đổi được giá.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Form với React Hook Form + Zod</h3>
            <p>Kiểm tra ở trình duyệt giúp người dùng sửa lỗi nhanh, nhưng ai cũng tắt được JavaScript hoặc gửi request thẳng tới server. Vì vậy server <strong>luôn kiểm tra lại</strong>. Viết schema Zod một lần trong <code>lib/schemas.ts</code> và dùng cho cả hai phía.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/schemas.ts   (npm install zod react-hook-form @hookform/resolvers)
import { z } from 'zod';

export const registerSchema = z.object({
  fullName: z.string().trim().min(2, 'Họ tên tối thiểu 2 ký tự').max(100, 'Họ tên tối đa 100 ký tự'),
  email: z.string().trim().toLowerCase().email('Email không đúng định dạng'),
  password: z.string().min(8, 'Mật khẩu tối thiểu 8 ký tự'),
  confirm: z.string(),
}).refine((d) =&gt; d.password === d.confirm, { path: ['confirm'], message: 'Mật khẩu nhập lại không khớp' });

export type RegisterInput = z.infer&lt;typeof registerSchema&gt;;</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(shop)/register/actions.ts: Server Action, chạy trên server
'use server';
import { registerSchema, type RegisterInput } from '@/lib/schemas';

export type ActionResult = { ok: boolean; message?: string };

export async function registerAction(input: RegisterInput): Promise&lt;ActionResult&gt; {
  const parsed = registerSchema.safeParse(input);               // kiểm tra lại ở server
  if (!parsed.success) return { ok: false, message: parsed.error.issues[0].message };

  const { confirm, ...body } = parsed.data;
  const res = await fetch(`${process.env.API_URL}/auth/register`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body),
  });
  if (res.status === 409) return { ok: false, message: 'Email đã được sử dụng' };
  if (!res.ok) return { ok: false, message: 'Đăng ký chưa thành công, vui lòng thử lại' };
  return { ok: true };
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(shop)/register/register-form.tsx
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
    useForm&lt;RegisterInput&gt;({ resolver: zodResolver(registerSchema) });

  const onSubmit = async (data: RegisterInput) =&gt; {
    const result = await registerAction(data);
    if (result.ok) router.push('/login?registered=1');
    else setServerError(result.message ?? '');
  };

  return (
    &lt;form onSubmit={handleSubmit(onSubmit)} className="space-y-3"&gt;
      &lt;label className="block"&gt;Họ tên
        &lt;input {...register('fullName')} className="w-full rounded border px-3 py-2" /&gt;
      &lt;/label&gt;
      {errors.fullName &amp;&amp; &lt;p className="text-sm text-red-600"&gt;{errors.fullName.message}&lt;/p&gt;}
      {/* email, password, confirm: tương tự */}
      {serverError &amp;&amp; &lt;p role="alert" className="text-red-600"&gt;{serverError}&lt;/p&gt;}
      &lt;button disabled={isSubmitting} className="rounded bg-blue-900 px-4 py-2 text-white"&gt;
        {isSubmitting ? 'Đang gửi…' : 'Đăng ký'}
      &lt;/button&gt;
    &lt;/form&gt;
  );
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Server Action là hàm <code>async</code> trong file <code>'use server'</code>; Client Component gọi nó như hàm bình thường, Next.js tự tạo request POST. Bài 06 học kỹ hơn.</li>
                <li>Lỗi hiện <strong>dưới từng ô</strong>, bằng tiếng Việt, gắn với nhãn của ô (tiêu chí US-G04). Lỗi từ server (409) hiện ở một chỗ chung có <code>role="alert"</code>.</li>
                <li>Nút gửi bị vô hiệu khi đang gửi để tránh gửi hai lần.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Đặt món qua API mẫu và kiểm thử form</h3>
            <p><code>POST /orders</code> cần đăng nhập. Bài 05 mới làm đăng nhập, nên hôm nay lấy tạm một access token ở trang <code>/docs</code> của API mẫu (đăng nhập bằng tài khoản thử, chép <code>accessToken</code>) và đọc qua một hàm duy nhất. Bài 05 chỉ cần sửa hàm này để đọc từ cookie.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/session.ts: TẠM THỜI cho bài 04, bài 05 thay bằng cookie
import 'server-only';
export async function getAccessToken() {
  return process.env.DEV_ACCESS_TOKEN;   // token hết hạn sau 15 phút: lấy lại ở /docs khi gặp 401
}

// app/(shop)/checkout/actions.ts
'use server';
import { z } from 'zod';
import { getAccessToken } from '@/lib/session';

const orderSchema = z.object({
  items: z.array(z.object({ productId: z.number().int().positive(), quantity: z.number().int().min(1).max(50) }))
          .min(1, 'Giỏ hàng đang trống'),
  note: z.string().trim().max(200, 'Ghi chú tối đa 200 ký tự').optional(),
});

export async function placeOrder(input: z.infer&lt;typeof orderSchema&gt;) {
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
}</code></pre>
            <p>Trang <code>/checkout</code> (Client Component) lấy <code>items</code> từ <code>useCart</code>, gửi kèm ghi chú; thành công thì <code>clear()</code> giỏ và chuyển tới <code>/orders/{orderId}</code>. API trả lỗi theo dạng <code>{ statusCode, message, error }</code>; với lỗi 400, <code>message</code> có thể là mảng chi tiết từng trường.</p>
            <p><strong>Phân tích giá trị biên (CLO2).</strong> Mỗi ràng buộc trong schema cho ít nhất hai test case: ngay dưới biên (sai) và đúng biên (đạt).</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mã</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Trường / story</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Dữ liệu vào</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả mong đợi</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-11</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Họ tên · US-G04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"A" (1 ký tự)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Họ tên tối thiểu 2 ký tự" dưới ô Họ tên</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-12</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Họ tên · US-G04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"An" (2 ký tự)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Không báo lỗi ô Họ tên</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-13</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mật khẩu · US-G04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">7 ký tự / 8 ký tự</td><td style="border: 1px solid #ffd6ad; padding: 6px;">7: báo lỗi; 8: hợp lệ</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-14</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhập lại · US-G04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Khác mật khẩu 1 ký tự</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Mật khẩu nhập lại không khớp"</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-15</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Email · US-G04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Email đã đăng ký</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Email đã được sử dụng" (API 409)</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-16</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Giỏ hàng · US-C01</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thêm cùng một món 2 lần</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Một dòng, số lượng 2</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-17</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đặt món · US-C04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Số lượng lớn hơn tồn kho</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Có món đã hết hoặc không đủ số lượng", giỏ còn nguyên</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;">Chạy thêm một lần với JavaScript bị tắt hoặc gửi request trực tiếp tới Server Action: dữ liệu sai vẫn phải bị từ chối. Đó là bằng chứng server có kiểm tra lại.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 04: Client Components, trạng thái &amp; form</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Mục 4.7: tiêu chí US-G04, C01, C02, C04 để viết test case; mục 8: định dạng lỗi của API.</span>
            </a>
            <a href="{{LINK_AGILE_SCRUM}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🗂 Kế hoạch Agile &amp; Product Backlog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Story Sprint 2 và tiêu chí Given-When-Then của giỏ hàng, đặt món.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/getting-started/server-and-client-components" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Server and Client Components</span><br>
                <span style="color: #6c757d; font-size: 13px;">Ranh giới "use client", truyền props, xen kẽ Server và Client Component.</span>
            </a>
            <a href="https://zustand.docs.pmnd.rs/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Zustand</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tạo store, middleware persist, dùng với Next.js.</span>
            </a>
            <a href="https://react-hook-form.com/get-started" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Hook Form - Get Started</span><br>
                <span style="color: #6c757d; font-size: 13px;">register, handleSubmit, formState, tích hợp schema validation.</span>
            </a>
            <a href="https://zod.dev/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Zod</span><br>
                <span style="color: #6c757d; font-size: 13px;">Định nghĩa schema, safeParse, refine, thông báo lỗi tùy chỉnh.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Giỏ hàng, đăng ký, đặt món</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tạo <code>lib/cart-store.ts</code>, nút <code>AddToCartButton</code> trên trang chi tiết món, <code>CartBadge</code> trên header.</li>
                <li>Trang <code>/cart</code>: tăng, giảm, xóa món, tổng tiền định dạng "75.000 đ"; tải lại trang giỏ vẫn còn.</li>
                <li>Trang <code>/register</code> với <code>lib/schemas.ts</code>, form React Hook Form và <code>registerAction</code>.</li>
                <li>Trang <code>/checkout</code> gọi <code>placeOrder</code> với token tạm trong <code>.env.local</code>; thử đặt quá tồn kho để thấy lỗi 409.</li>
                <li>Chạy 7 test case TC-11…TC-17, ghi kết quả.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Form "Góp ý căn tin"</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Trang <code>/feedback</code> gồm: chọn quầy (lấy từ <code>GET /counters</code>), điểm hài lòng 1–5, nội dung 10–500 ký tự, email liên hệ không bắt buộc nhưng nếu nhập phải đúng định dạng. Kiểm tra bằng một schema Zod dùng cho cả form và Server Action; thông báo lỗi tiếng Việt dưới từng ô. Server Action chỉ cần ghi log dữ liệu hợp lệ (API mẫu chưa có endpoint góp ý).</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp link repo và bảng giá trị biên (ít nhất 8 test case: điểm 0/1/5/6, nội dung 9/10/500/501 ký tự) kèm kết quả chạy.</p>
            <a href="{{LINK_NOP_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <p style="margin: 0; color: #495057;">Xây form chính và luồng nhập liệu của web nhóm (giỏ hàng, đặt món hoặc form quản trị theo story đã chọn cho Sprint 2). Cập nhật sơ đồ thành phần: đánh dấu Client Component và lý do (CLO1); thêm bảng giá trị biên và test case vào thư mục <code>docs/test/</code> (CLO2). Mỗi thẻ trên board có liên kết Pull Request.</p>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Form của bạn đã kiểm tra dữ liệu ở trình duyệt. Hãy nêu một cách người dùng có thể vượt qua lớp kiểm tra đó, và chỉ ra dòng mã nào ở server chặn được.</p>
            <a href="{{LINK_DIEN_DAN_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập Client Component, Zustand, hydration, React Hook Form, Zod và giá trị biên.</p>
            <a href="{{LINK_QUIZ_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 04</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Lỗi "useState only works in Client Components":</strong> file dùng hook nhưng thiếu <code>'use client'</code> ở dòng đầu. Thêm vào component lá, không thêm vào page.</p>
        <p><strong>Lỗi "Hydration failed" ở biểu tượng giỏ hàng:</strong> HTML server (giỏ rỗng) khác HTML trình duyệt (giỏ có món). Dùng cờ <code>mounted</code> như mục 2.2.</p>
        <p><strong>Form không báo lỗi gì khi bấm gửi:</strong> quên <code>resolver: zodResolver(schema)</code> hoặc tên trong <code>register('...')</code> không khớp tên trường của schema.</p>
        <p><strong>Đặt món trả 401:</strong> token tạm đã hết hạn (15 phút). Lấy token mới ở <code>/docs</code> rồi khởi động lại <code>npm run dev</code>. Bài 05 sẽ bỏ hẳn bước này.</p>
        <p><strong>Kiến thức mở rộng:</strong> <code>useTransition</code> để giữ giao diện phản hồi khi chờ Server Action; hộp thoại xác nhận của shadcn/ui (<code>AlertDialog</code>) trước khi xóa món khỏi giỏ.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu xóa toàn bộ phần kiểm tra ở trình duyệt, form của bạn có còn từ chối dữ liệu sai không?</p>
    </div>
</details>
