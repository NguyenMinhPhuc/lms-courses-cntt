<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 05 - Xác thực, phân quyền &amp; bảo mật web (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Một sinh viên gõ thẳng <code>/admin/products</code> vào thanh địa chỉ. Menu quản trị đã bị ẩn, nhưng trang vẫn mở ra và nút "Xóa món" vẫn bấm được. Ẩn menu không phải là phân quyền. Hôm nay ta làm đăng nhập thật, giữ token ở nơi JavaScript không đọc được, và kiểm tra quyền ở mọi lớp.</em></p>
        <p><strong>Mục tiêu:</strong> Phân tích được yêu cầu phân quyền theo vai trò thành ma trận; triển khai được đăng nhập bằng JWT của backend với cookie <code>httpOnly</code>; bảo vệ được route bằng <code>proxy</code> và kiểm tra lại quyền ở server; nhận diện được các lỗ hổng web phổ biến; kiểm thử được các tình huống truy cập trái phép.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Luồng xác thực web:</strong> đăng nhập qua Server Action, access/refresh token trong cookie <code>httpOnly</code>, <code>Secure</code>, <code>SameSite</code>.</li>
            <li><strong>Ý chính 2 - Phân quyền theo vai trò:</strong> ma trận vai trò × chức năng, <code>proxy.ts</code> chặn route, kiểm tra lại ở server.</li>
            <li><strong>Ý chính 3 - Làm mới token và đăng xuất:</strong> gọi API kèm token từ server, refresh khi access token hết hạn.</li>
            <li><strong>Ý chính 4 - Bảo mật web và test case:</strong> XSS, CSRF, CORS, lộ biến <code>NEXT_PUBLIC_*</code>, open redirect, OWASP Top 10.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Web đăng nhập được bằng tài khoản của API mẫu (US-G05, US-S01), khu quản trị chỉ mở cho đúng vai trò, đăng xuất thu hồi token (US-C13); nhóm có ma trận phân quyền và bộ test case truy cập trái phép kèm kết quả.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Luồng xác thực và cookie httpOnly</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>Trình duyệt ──form──▶ Server Action (Next.js) ──POST /auth/login──▶ API
           ◀─Set-Cookie: access_token, refresh_token (httpOnly)───┘
Các request sau: trình duyệt tự gửi cookie ▶ Next.js đọc cookie ▶ gọi API với
                 Authorization: Bearer &lt;access_token&gt;</code></pre>
            <p>Ứng dụng di động lưu token bằng SecureStore. Trên web, nơi tương đương là <strong>cookie <code>httpOnly</code></strong>: trình duyệt tự gửi kèm mỗi request nhưng JavaScript trong trang không đọc được, nên một đoạn mã XSS không lấy cắp được token. <strong>Không lưu token trong <code>localStorage</code>.</strong></p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/session.ts: thay bản tạm của bài 04
import 'server-only';
import { cookies } from 'next/headers';

const base = {
  httpOnly: true,                                   // JavaScript không đọc được
  secure: process.env.NODE_ENV === 'production',    // chỉ gửi qua HTTPS khi chạy thật
  sameSite: 'lax' as const,                         // không gửi kèm request POST từ trang khác
  path: '/',
};

export type Tokens = { accessToken: string; refreshToken: string };

export async function setAuthCookies(t: Tokens) {
  const c = await cookies();
  c.set('access_token', t.accessToken, { ...base, maxAge: 14 * 60 });          // JWT sống 15 phút
  c.set('refresh_token', t.refreshToken, { ...base, maxAge: 7 * 24 * 3600 });  // 7 ngày
}

export async function getAccessToken() {
  return (await cookies()).get('access_token')?.value;
}

export async function clearAuthCookies() {
  const c = await cookies();
  c.delete('access_token');
  c.delete('refresh_token');
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(shop)/login/actions.ts
'use server';
import { redirect } from 'next/navigation';
import { z } from 'zod';
import { setAuthCookies } from '@/lib/session';

const loginSchema = z.object({
  email: z.string().trim().email('Email không đúng định dạng'),
  password: z.string().min(1, 'Nhập mật khẩu'),
  next: z.string().optional(),
});

export async function loginAction(_prev: { message: string }, formData: FormData) {
  const parsed = loginSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { message: parsed.error.issues[0].message };

  const res = await fetch(`${process.env.API_URL}/auth/login`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: parsed.data.email, password: parsed.data.password }),
  });
  if (res.status === 401) return { message: 'Email hoặc mật khẩu không đúng' };   // thông báo chung (BR-03)
  if (res.status === 403) return { message: 'Tài khoản đã bị khóa' };
  if (!res.ok) return { message: 'Đăng nhập chưa thành công, vui lòng thử lại' };

  const data: { accessToken: string; refreshToken: string; role: string } = await res.json();
  await setAuthCookies(data);

  const next = parsed.data.next;
  const safeNext = next?.startsWith('/') &amp;&amp; !next.startsWith('//') ? next : null;  // chặn open redirect
  redirect(safeNext ?? (data.role === 'customer' ? '/menu' : '/admin/orders'));
}</code></pre>
            <p style="margin-bottom: 0;">Trang <code>/login</code> dùng <code>useActionState(loginAction, { message: '' })</code> và <code>&lt;form action={formAction}&gt;</code> có ô ẩn <code>next</code>. Vì form gửi thẳng tới Server Action, nó vẫn chạy được khi JavaScript chưa tải xong. Cookie chỉ được ghi trong Server Action, Route Handler hoặc <code>proxy</code>, không ghi được khi đang render Server Component.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Ma trận phân quyền và bảo vệ route</h3>
            <p><strong>Phân tích trước (CLO1).</strong> Từ SRS (US-S01, US-A01) lập ma trận vai trò × chức năng. Mỗi ô "✔" phải có test case chứng minh được phép, mỗi ô "✘" phải có test case chứng minh bị chặn.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px; text-align: left;">Route · chức năng</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Khách vãng lai</th><th style="border: 1px solid #ffd6ad; padding: 6px;">customer</th><th style="border: 1px solid #ffd6ad; padding: 6px;">staff</th><th style="border: 1px solid #ffd6ad; padding: 6px;">admin</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/menu</code>, <code>/product/[id]</code> · xem thực đơn</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/checkout</code>, <code>/orders</code>, <code>/profile</code> · đặt món, đơn của tôi</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✘ → /login</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/orders</code> · màn hình quầy</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✘ → /login</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✘ 403</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/products</code>, <code>/admin/users</code> · quản trị</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✘ → /login</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✘ 403</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✘ 403</td><td style="border: 1px solid #ffd6ad; padding: 6px; text-align: center;">✔</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Lớp 1 – <code>proxy.ts</code> (kiểm tra nhanh, chuyển hướng sớm).</strong> Từ Next.js 16, file <code>middleware.ts</code> đổi tên thành <code>proxy.ts</code> và hàm xuất ra tên là <code>proxy</code>; Next.js 15 dùng tên cũ, nội dung giống nhau. Kiểm tra bằng <code>npx next --version</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// proxy.ts (gốc dự án, cạnh thư mục app)   npm install jose
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
  const rule = RULES.find((r) =&gt; req.nextUrl.pathname.startsWith(r.prefix));
  if (!rule) return NextResponse.next();

  let access = req.cookies.get('access_token')?.value;
  const refresh = req.cookies.get('refresh_token')?.value;
  let res = NextResponse.next();

  if (!access &amp;&amp; refresh) {                                   // access hết hạn: làm mới (mục 2.3)
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

export const config = { matcher: ['/admin/:path*', '/checkout', '/orders/:path*', '/profile'] };</code></pre>
            <p><strong>Lớp 2 – kiểm tra lại ở server.</strong> <code>proxy</code> chỉ đọc vai trò trong token mà không xác minh chữ ký (Next.js không giữ khóa bí mật của backend), nên nó chỉ để chuyển hướng sớm. Năm 2025, Next.js từng có lỗ hổng cho phép bỏ qua hoàn toàn middleware bằng một header đặc biệt (CVE-2025-29927). Ứng dụng nào chỉ dựa vào middleware đều bị mở toang. Vì vậy mỗi trang và mỗi Server Action nhạy cảm tự kiểm tra lại qua một lớp truy cập dữ liệu (Data Access Layer):</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/dal.ts
import 'server-only';
import { cache } from 'react';
import { redirect, forbidden } from 'next/navigation';
import { getAccessToken } from './session';

export type User = { userId: number; fullName: string; email: string; role: 'customer' | 'staff' | 'admin' };

// Backend xác minh chữ ký token; cache() để mỗi request chỉ gọi API một lần
export const getCurrentUser = cache(async (): Promise&lt;User | null&gt; =&gt; {
  const token = await getAccessToken();
  if (!token) return null;
  const res = await fetch(`${process.env.API_URL}/users/me`, {
    headers: { Authorization: `Bearer ${token}` }, cache: 'no-store',
  });
  return res.ok ? res.json() : null;
});

export async function requireRole(...roles: User['role'][]) {
  const user = await getCurrentUser();
  if (!user) redirect('/login');
  if (!roles.includes(user.role)) forbidden();     // hoặc redirect('/forbidden') nếu chưa bật forbidden()
  return user;
}

// app/admin/products/page.tsx
//   export default async function Page() { await requireRole('admin'); ... }</code></pre>
            <p style="margin-bottom: 0;"><strong>Lớp 3 – API.</strong> Backend trả 403 khi token không đủ quyền, và trả 404 khi khách xem đơn của người khác. Ba lớp có ba nhiệm vụ khác nhau: <code>proxy</code> cho trải nghiệm (chuyển hướng sớm), DAL bảo vệ trang và Server Action, API bảo vệ dữ liệu. Ẩn menu theo vai trò chỉ là giao diện, không được tính là phân quyền.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Gọi API kèm token, làm mới token và đăng xuất</h3>
            <p>Bổ sung vào <code>lib/api.ts</code> một hàm gọi API có xác thực. Hàm chỉ chạy ở server nên token không bao giờ xuống trình duyệt.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/api.ts (thêm)
import { getAccessToken } from './session';

export class ApiError extends Error {
  constructor(public status: number, message: string) { super(message); }
}

export async function apiAuth&lt;T&gt;(path: string, init: RequestInit = {}): Promise&lt;T&gt; {
  const res = await fetch(`${process.env.API_URL}${path}`, {
    ...init,
    cache: 'no-store',                                        // dữ liệu riêng của từng người: không cache
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${await getAccessToken()}`, ...init.headers },
  });
  if (!res.ok) {
    const body = await res.json().catch(() =&gt; ({}));
    throw new ApiError(res.status, Array.isArray(body.message) ? body.message.join(', ') : body.message ?? 'Lỗi API');
  }
  return res.json() as Promise&lt;T&gt;;
}</code></pre>
            <ul>
                <li><strong>Làm mới token:</strong> cookie <code>access_token</code> hết hạn sau 14 phút (sớm hơn JWT 1 phút). Lần vào trang được bảo vệ kế tiếp, <code>proxy</code> thấy chỉ còn <code>refresh_token</code> nên gọi <code>POST /auth/refresh</code> và ghi cặp token mới. Refresh thất bại (hết hạn, bị thu hồi, tài khoản bị khóa) thì chuyển về <code>/login</code>.</li>
                <li><strong>Không cache dữ liệu riêng:</strong> đơn của tôi, hồ sơ, màn hình quầy luôn dùng <code>cache: 'no-store'</code>. Nếu cache, người sau có thể thấy dữ liệu của người trước.</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/actions/logout.ts
'use server';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import { clearAuthCookies } from '@/lib/session';

export async function logoutAction() {
  const refreshToken = (await cookies()).get('refresh_token')?.value;
  if (refreshToken) {
    await fetch(`${process.env.API_URL}/auth/logout`, {           // thu hồi ở server (US-C13)
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ refreshToken }),
    }).catch(() =&gt; {});
  }
  await clearAuthCookies();
  redirect('/login');
}
// Header: &lt;form action={logoutAction}&gt;&lt;button&gt;Đăng xuất&lt;/button&gt;&lt;/form&gt;
// Nút đăng xuất phía client gọi useCart.getState().clear() trước khi gửi form (xóa giỏ hàng).</code></pre>
            <p style="margin-bottom: 0;">Header là Server Component gọi <code>getCurrentUser()</code> để hiện "Xin chào, Nguyễn Văn A" và menu theo vai trò; khách vãng lai thấy nút "Đăng nhập".</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Bảo mật web và test case truy cập trái phép</h3>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px; text-align: left;">Rủi ro</th><th style="border: 1px solid #ffd6ad; padding: 6px; text-align: left;">Biểu hiện</th><th style="border: 1px solid #ffd6ad; padding: 6px; text-align: left;">Cách phòng trong LHU Food</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><strong>Kiểm soát truy cập hỏng</strong> (OWASP A01)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Gõ URL quản trị; đổi <code>/orders/12</code> thành <code>/orders/13</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Ba lớp ở mục 2.2; API trả 404 với đơn của người khác</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><strong>XSS</strong></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Ghi chú đơn chứa <code>&lt;script&gt;</code> chạy trên màn hình quầy</td><td style="border: 1px solid #ffd6ad; padding: 6px;">React tự mã hóa nội dung; không dùng <code>dangerouslySetInnerHTML</code>; token trong cookie <code>httpOnly</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><strong>CSRF</strong></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Trang lạ gửi form POST tới web đang đăng nhập</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>SameSite=Lax</code>; Server Action chỉ nhận POST và Next.js so sánh header <code>Origin</code> với <code>Host</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><strong>Lộ bí mật</strong></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đặt khóa vào <code>NEXT_PUBLIC_API_KEY</code>; commit <code>.env.local</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Biến <code>NEXT_PUBLIC_*</code> bị chép vào mã gửi xuống trình duyệt, chỉ dùng cho giá trị công khai; <code>import 'server-only'</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><strong>CORS</strong></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Gọi API từ trình duyệt bị chặn</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Next.js gọi API từ server nên không cần mở CORS; không bật <code>*</code> cho API có xác thực</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><strong>Open redirect</strong></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/login?next=https://trang-gia.com</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chỉ nhận <code>next</code> bắt đầu bằng <code>/</code> và không phải <code>//</code></td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Test case phân quyền và bảo mật (CLO2):</strong></p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mã</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Tình huống</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả mong đợi</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-21</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chưa đăng nhập, mở <code>/admin/orders</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chuyển tới <code>/login?next=/admin/orders</code>; đăng nhập staff xong quay lại đúng trang</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-22</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đăng nhập customer, gõ <code>/admin/orders</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Trang 403, không thấy dữ liệu đơn</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-23</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đăng nhập staff, gõ <code>/admin/users</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Trang 403</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-24</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Dùng token customer gọi <code>PATCH /orders/12/status</code> (Swagger hoặc Postman)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">API trả 403</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-25</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đăng nhập sai mật khẩu; đăng nhập email không tồn tại</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Cùng một thông báo "Email hoặc mật khẩu không đúng"</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-26</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Sau đăng nhập, gõ <code>document.cookie</code> trong Console</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Không thấy <code>access_token</code>; tab Application hiện cờ HttpOnly</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-27</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mở <code>/login?next=https://example.com</code> rồi đăng nhập</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Về trang mặc định theo vai trò, không rời khỏi web</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-28</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đăng xuất, bấm Back của trình duyệt rồi tải lại</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Không vào lại được trang được bảo vệ; refresh token cũ bị API từ chối</td></tr>
                </tbody>
            </table>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 05: Xác thực, phân quyền &amp; bảo mật web</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tiêu chí US-G05, C13, S01, A01; quy tắc nghiệp vụ BR-03 (thông báo đăng nhập chung); mục 8: các endpoint /auth.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/guides/authentication" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Authentication</span><br>
                <span style="color: #6c757d; font-size: 13px;">Quản lý phiên bằng cookie, Data Access Layer, kiểm tra quyền lạc quan và kiểm tra an toàn.</span>
            </a>
            <a href="https://nextjs.org/docs/app/api-reference/file-conventions/proxy" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - proxy.js (trước đây là middleware.js)</span><br>
                <span style="color: #6c757d; font-size: 13px;">matcher, đọc và ghi cookie, chuyển hướng, rewrite.</span>
            </a>
            <a href="https://owasp.org/Top10/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 OWASP Top 10</span><br>
                <span style="color: #6c757d; font-size: 13px;">Mười nhóm rủi ro bảo mật web phổ biến nhất.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Đăng nhập và chặn khu quản trị</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Thay <code>lib/session.ts</code> tạm của bài 04 bằng bản dùng cookie; xóa <code>DEV_ACCESS_TOKEN</code> khỏi <code>.env.local</code>.</li>
                <li>Trang <code>/login</code> với <code>loginAction</code> và <code>useActionState</code>; thử bằng tài khoản customer và staff của API mẫu.</li>
                <li>Tạo <code>proxy.ts</code> (hoặc <code>middleware.ts</code> nếu dùng Next.js 15), trang <code>/forbidden</code>, <code>lib/dal.ts</code>; gọi <code>requireRole</code> trong layout và trang quản trị.</li>
                <li>Header hiện tên người dùng, menu theo vai trò, nút Đăng xuất; kiểm tra trang đặt món của bài 04 giờ dùng token từ cookie.</li>
                <li>Chạy TC-21…TC-28, ghi kết quả.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Trang "Hồ sơ của tôi"</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Trang <code>/profile</code> hiển thị họ tên, email, vai trò từ <code>GET /users/me</code>; cho sửa họ tên qua <code>PATCH /users/me</code> bằng Server Action có kiểm tra Zod (2–100 ký tự). Trang chỉ mở khi đã đăng nhập.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp link repo và kết quả 4 tình huống truy cập trái phép: chưa đăng nhập mở <code>/profile</code>; cookie <code>access_token</code> bị xóa tay nhưng còn refresh token; refresh token bị sửa một ký tự; gọi Server Action sửa họ tên khi đã đăng xuất.</p>
            <a href="{{LINK_NOP_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <p style="margin: 0; color: #495057;">Lập <strong>ma trận phân quyền</strong> cho toàn bộ route của web nhóm (CLO1), áp dụng xác thực và phân quyền ba lớp, viết test case cho mọi ô "✘" của ma trận (CLO2). Ma trận và kết quả test là một phần của Checkpoint Sprint 2.</p>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Nếu nhóm bạn chỉ bảo vệ trang quản trị bằng <code>proxy.ts</code>, điều gì xảy ra khi có một lỗ hổng như CVE-2025-29927? Lớp nào trong ứng dụng của bạn vẫn còn chặn được?</p>
            <a href="{{LINK_DIEN_DAN_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập cookie httpOnly, proxy, Data Access Layer, làm mới token và các rủi ro bảo mật web.</p>
            <a href="{{LINK_QUIZ_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 05</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong><code>proxy.ts</code> không chạy:</strong> file phải nằm ở gốc dự án (hoặc trong <code>src/</code> nếu dùng thư mục src), cùng cấp với <code>app</code>. Next.js 15 thì đặt tên <code>middleware.ts</code> và xuất hàm <code>middleware</code>. Kiểm tra lại <code>matcher</code>.</p>
        <p><strong>Lỗi "Cookies can only be modified in a Server Action or Route Handler":</strong> bạn gọi <code>cookies().set</code> trong Server Component. Chuyển việc ghi cookie vào Server Action hoặc <code>proxy</code>.</p>
        <p><strong>Đăng nhập xong vẫn bị đẩy về /login:</strong> trên môi trường chạy bằng HTTP (không HTTPS), cookie có <code>secure: true</code> sẽ không được lưu. Kiểm tra <code>NODE_ENV</code>; khi triển khai lên server Khoa phải dùng HTTPS.</p>
        <p><strong><code>forbidden()</code> báo lỗi:</strong> hàm này cần bật <code>experimental.authInterrupts</code> trong <code>next.config.ts</code>. Nếu không muốn bật, dùng <code>redirect('/forbidden')</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> Auth.js (NextAuth) khi cần đăng nhập bằng Google hoặc Microsoft của trường; Content Security Policy (CSP) để giảm rủi ro XSS.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Mỗi ô "✘" trong ma trận phân quyền của nhóm bạn đã có một test case chứng minh bị chặn ở API chưa, hay chỉ bị chặn ở giao diện?</p>
    </div>
</details>
