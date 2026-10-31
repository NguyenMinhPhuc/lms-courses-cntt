# Chương 5. Xác thực, phân quyền và bảo mật web

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Phân biệt xác thực và phân quyền; mô tả luồng đăng nhập bằng JWT trên web.
- Lưu access token và refresh token trong cookie `httpOnly`, `Secure`, `SameSite`.
- Phân tích yêu cầu phân quyền thành ma trận vai trò × chức năng.
- Bảo vệ route bằng `proxy.ts` và kiểm tra lại quyền ở server qua Data Access Layer.
- Làm mới token, đăng xuất, gọi API kèm token từ server.
- Nhận diện các rủi ro bảo mật web phổ biến và viết test case truy cập trái phép.

## 5.1. Xác thực và phân quyền

**Xác thực** (authentication) trả lời câu hỏi "bạn là ai": người dùng chứng minh danh tính bằng email và mật khẩu. **Phân quyền** (authorization) trả lời câu hỏi "bạn được làm gì": tài khoản `staff` được đổi trạng thái đơn, tài khoản `customer` thì không.

Backend LHU Food đã có sẵn cả hai (Chương 6 giáo trình di động): đăng nhập trả về **access token** (JWT, sống 15 phút) và **refresh token** (sống 7 ngày); mỗi API kiểm tra token và vai trò. Phần việc của web là lưu token an toàn, gửi kèm token khi gọi API, và không để người dùng thấy trang họ không được phép vào.

## 5.2. Luồng xác thực trên web và cookie httpOnly

### 5.2.1. Luồng tổng quát

```text
Trình duyệt ──form──▶ Server Action (Next.js) ──POST /auth/login──▶ API
           ◀─Set-Cookie: access_token, refresh_token (httpOnly)───┘
Các request sau: trình duyệt tự gửi cookie ▶ Next.js đọc cookie ▶ gọi API với
                 Authorization: Bearer <access_token>
```

Trình duyệt không bao giờ cầm token trong JavaScript. Next.js là nơi duy nhất đọc token (từ cookie) và gửi nó tới API.

### 5.2.2. Vì sao là cookie httpOnly

Ứng dụng di động lưu token bằng SecureStore. Trên web, nơi tương đương là **cookie có cờ httpOnly**: trình duyệt tự gửi kèm mỗi request tới cùng tên miền, nhưng JavaScript trong trang không đọc được (`document.cookie` không thấy). Nếu trang bị chèn mã độc (XSS), mã đó không lấy cắp được token [1]. Ngược lại, token trong `localStorage` thì mọi đoạn JavaScript trên trang đều đọc được. Vì vậy **không lưu token trong localStorage**.

| Cờ cookie | Tác dụng |
|---|---|
| `httpOnly` | JavaScript không đọc được |
| `Secure` | Chỉ gửi qua HTTPS |
| `SameSite=Lax` | Không gửi kèm request POST xuất phát từ trang khác (giảm CSRF) |
| `Max-Age` | Thời gian sống của cookie |
| `Path=/` | Gửi kèm mọi đường dẫn của web |

### 5.2.3. Quản lý cookie phiên

```ts
// lib/session.ts: thay bản tạm của Chương 4
import 'server-only';
import { cookies } from 'next/headers';

const base = {
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'lax' as const,
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
}
```

Hàm `cookies()` của Next.js là bất đồng bộ từ Next.js 15 [2]. Cookie chỉ **ghi** được trong Server Action, Route Handler hoặc `proxy`; khi đang render Server Component chỉ đọc được. Cookie `access_token` hết hạn sớm hơn JWT một phút để không gửi token sắp hết hạn. Chương 11 tách cờ `secure` thành biến môi trường khi triển khai.

### 5.2.4. Đăng nhập bằng Server Action

```ts
// app/(shop)/login/actions.ts
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
  if (res.status === 401) return { message: 'Email hoặc mật khẩu không đúng' };
  if (res.status === 403) return { message: 'Tài khoản đã bị khóa' };
  if (!res.ok) return { message: 'Đăng nhập chưa thành công, vui lòng thử lại' };

  const data: { accessToken: string; refreshToken: string; role: string } = await res.json();
  await setAuthCookies(data);

  const next = parsed.data.next;
  const safeNext = next?.startsWith('/') && !next.startsWith('//') ? next : null;  // chặn open redirect
  redirect(safeNext ?? (data.role === 'customer' ? '/menu' : '/admin/orders'));
}
```

- Sai email hay sai mật khẩu đều trả **một thông báo chung** (quy tắc BR-03 trong SRS mục 6), để kẻ tấn công không dò được email nào đã đăng ký.
- Trang `/login` dùng `useActionState(loginAction, { message: '' })` (Chương 6) với `<form action={formAction}>`. Form gửi thẳng tới Server Action nên chạy được cả khi JavaScript chưa tải xong.
- Tham số `next` cho phép quay lại đúng trang sau khi đăng nhập; chỉ chấp nhận đường dẫn nội bộ (mục 5.6).

## 5.3. Phân tích phân quyền

### 5.3.1. Ma trận vai trò × chức năng (CLO1)

Từ SRS (US-S01, US-A01 và tiêu chí ở mục 4.7) lập ma trận: hàng là route hoặc chức năng, cột là vai trò, ô là được phép (✔) hay bị chặn (✘) và bị chặn thế nào.

| Route · chức năng | Khách vãng lai | customer | staff | admin |
|---|---|---|---|---|
| `/menu`, `/product/[id]` · xem thực đơn | ✔ | ✔ | ✔ | ✔ |
| `/checkout`, `/orders`, `/profile` · đặt món, đơn của tôi | ✘ → /login | ✔ | ✔ | ✔ |
| `/admin/orders` · màn hình quầy | ✘ → /login | ✘ 403 | ✔ | ✔ |
| `/admin/products`, `/admin/users` · quản trị | ✘ → /login | ✘ 403 | ✘ 403 | ✔ |

Ma trận có hai công dụng. Nó là phần "phân tích phân quyền" trong báo cáo (CLO1), và nó sinh ra bộ test case (CLO2): mỗi ô ✔ cần một test chứng minh được phép, mỗi ô ✘ cần một test chứng minh bị chặn.

### 5.3.2. Ẩn menu không phải là phân quyền

Ẩn mục "Quản trị" trên menu với tài khoản customer chỉ là giao diện. Người dùng vẫn gõ thẳng `/admin/products` được, vẫn gửi request tới Server Action được. Phân quyền thật phải nằm ở server, theo nhiều lớp.

## 5.4. Bảo vệ route theo ba lớp

### 5.4.1. Lớp 1: proxy.ts

`proxy.ts` (đặt ở gốc dự án, cạnh thư mục `app`) chạy **trước** mọi request khớp `matcher`, dùng để chuyển hướng sớm [3]. Từ Next.js 16, file `middleware.ts` đổi tên thành `proxy.ts` và hàm xuất ra tên là `proxy`; Next.js 15 dùng tên cũ, nội dung giống nhau.

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
// … (trích 15/47 dòng; mã đầy đủ ở Phụ lục A, mục A.2)
```

Thứ tự trong `RULES` quan trọng: `/admin/orders` phải đứng trước `/admin` vì `find` lấy quy tắc khớp đầu tiên.

### 5.4.2. Vì sao không dừng ở proxy

`proxy` chỉ **đọc** vai trò trong JWT mà không xác minh chữ ký, vì Next.js không giữ khóa bí mật của backend. Ai đó tự tạo một JWT ghi `role: admin` vẫn qua được lớp này. Thêm nữa, năm 2025 Next.js từng có lỗ hổng CVE-2025-29927 cho phép bỏ qua hoàn toàn middleware bằng một header đặc biệt [4]. Ứng dụng nào chỉ dựa vào middleware để phân quyền đều bị mở toang. Vì vậy `proxy` chỉ phục vụ trải nghiệm (chuyển hướng sớm), không phải hàng rào an ninh.

### 5.4.3. Lớp 2: Data Access Layer

Mỗi trang và mỗi Server Action nhạy cảm tự kiểm tra lại qua một lớp truy cập dữ liệu dùng chung (Data Access Layer), được Next.js khuyến nghị [5]:

```ts
// lib/dal.ts
import 'server-only';
import { cache } from 'react';
import { redirect, forbidden } from 'next/navigation';
import { getAccessToken } from './session';

export type User = { userId: number; fullName: string; email: string; role: 'customer' | 'staff' | 'admin' };

// Backend xác minh chữ ký token; cache() để mỗi request chỉ gọi API một lần
export const getCurrentUser = cache(async (): Promise<User | null> => {
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
//   export default async function Page() { await requireRole('admin'); ... }
```

`getCurrentUser` hỏi backend (`GET /users/me`), nên token giả bị backend từ chối. `cache()` của React ghi nhớ kết quả trong một lần render, nhờ vậy layout, trang và header cùng gọi mà API chỉ bị gọi một lần. Hàm `forbidden()` cần bật `experimental.authInterrupts` trong `next.config.ts`; nếu không bật, dùng `redirect('/forbidden')`.

Không chỉ dựa vào kiểm tra trong `layout.tsx`: layout không chạy lại khi chuyển giữa các trang con, và Server Action không đi qua layout. Gọi `requireRole` trong từng trang và từng Server Action nhạy cảm.

### 5.4.4. Lớp 3: API

Backend trả 403 khi token không đủ quyền, trả 404 khi khách xem đơn của người khác. Đây là lớp bảo vệ dữ liệu cuối cùng và là lớp duy nhất ứng dụng di động cũng đi qua.

| Lớp | Nhiệm vụ | Có xác minh token không |
|---|---|---|
| `proxy.ts` | Chuyển hướng sớm, làm mới token | Không (chỉ đọc) |
| Data Access Layer | Bảo vệ trang, Server Action, Route Handler | Có (qua `/users/me`) |
| API | Bảo vệ dữ liệu | Có |

## 5.5. Gọi API kèm token, làm mới token và đăng xuất

### 5.5.1. Hàm gọi API có xác thực

```ts
// lib/api.ts (thêm)
import { getAccessToken } from './session';

export class ApiError extends Error {
  constructor(public status: number, message: string) { super(message); }
}

export async function apiAuth<T>(path: string, init: RequestInit = {}): Promise<T> {
  const res = await fetch(`${process.env.API_URL}${path}`, {
    ...init,
    cache: 'no-store',                                        // dữ liệu riêng của từng người: không cache
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${await getAccessToken()}`, ...init.headers },
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new ApiError(res.status, Array.isArray(body.message) ? body.message.join(', ') : body.message ?? 'Lỗi API');
  }
  return res.json() as Promise<T>;
}
```

`ApiError` giữ mã HTTP để Server Action phân biệt 404, 409 và hiển thị thông báo phù hợp (Chương 6).

### 5.5.2. Làm mới token

Cookie `access_token` hết hạn sau 14 phút. Lần vào trang được bảo vệ kế tiếp, `proxy` thấy chỉ còn `refresh_token` nên gọi `POST /auth/refresh` và ghi cặp token mới (mục 5.4.1). Refresh thất bại (hết hạn, bị thu hồi, tài khoản bị khóa) thì người dùng về `/login`. Refresh token được **xoay vòng**: mỗi lần làm mới, backend cấp refresh token mới và vô hiệu token cũ.

### 5.5.3. Đăng xuất

```ts
// app/actions/logout.ts
'use server';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import { clearAuthCookies } from '@/lib/session';

export async function logoutAction() {
  const refreshToken = (await cookies()).get('refresh_token')?.value;
  if (refreshToken) {
    await fetch(`${process.env.API_URL}/auth/logout`, {           // thu hồi ở server (US-C13)
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ refreshToken }),
    }).catch(() => {});
  }
  await clearAuthCookies();
  redirect('/login');
}
```

Đăng xuất phải **thu hồi refresh token ở server**, không chỉ xóa cookie; nếu không, ai đã sao chép được refresh token vẫn dùng tiếp được 7 ngày. Nút đăng xuất phía client xóa giỏ hàng (`useCart.getState().clear()`) trước khi gửi form, đúng tiêu chí US-C13. Header là Server Component gọi `getCurrentUser()` để hiện tên người dùng và menu theo vai trò.

## 5.6. Rủi ro bảo mật web

### 5.6.1. OWASP Top 10

OWASP Top 10 là danh sách mười nhóm rủi ro bảo mật web phổ biến nhất, được cập nhật định kỳ [6]. Nhóm đứng đầu là **kiểm soát truy cập hỏng** (Broken Access Control): người dùng làm được việc ngoài quyền của mình. Bảng sau liệt kê các rủi ro sinh viên cần nhận diện được trong LHU Food:

| Rủi ro | Biểu hiện | Cách phòng trong LHU Food |
|---|---|---|
| Kiểm soát truy cập hỏng | Gõ URL quản trị; đổi `/orders/12` thành `/orders/13` | Ba lớp ở mục 5.4; API trả 404 với đơn của người khác |
| XSS (chèn mã) | Ghi chú đơn chứa `<script>` chạy trên màn hình quầy | React tự mã hóa nội dung; không dùng `dangerouslySetInnerHTML`; token trong cookie `httpOnly` |
| CSRF (giả mạo request) | Trang lạ gửi form POST tới web đang đăng nhập | `SameSite=Lax`; Server Action chỉ nhận POST và Next.js so sánh header `Origin` với `Host` |
| Lộ bí mật | Đặt khóa vào `NEXT_PUBLIC_API_KEY`; commit `.env.local` | Biến `NEXT_PUBLIC_*` chỉ cho giá trị công khai; `import 'server-only'` |
| Cấu hình CORS sai | Mở `Access-Control-Allow-Origin: *` cho API có xác thực | Next.js gọi API từ server nên không cần CORS cho REST; chỉ mở cho địa chỉ web cụ thể khi dùng Socket.IO (Chương 9) |
| Open redirect | `/login?next=https://trang-gia.com` | Chỉ nhận `next` bắt đầu bằng `/` và không phải `//` |

### 5.6.2. Server Action là endpoint công khai

Mỗi Server Action là một địa chỉ POST mà ai cũng gửi request tới được, kể cả khi trang chứa nó đã được bảo vệ. Vì vậy mọi Server Action nhạy cảm phải tự kiểm tra quyền (`requireRole`) và kiểm tra dữ liệu (Zod) bên trong nó [7].

## 5.7. Test case phân quyền và bảo mật (CLO2)

| Mã | Tình huống | Kết quả mong đợi |
|---|---|---|
| TC-21 | Chưa đăng nhập, mở `/admin/orders` | Chuyển tới `/login?next=/admin/orders`; đăng nhập staff xong quay lại đúng trang |
| TC-22 | Đăng nhập customer, gõ `/admin/orders` | Trang 403, không thấy dữ liệu đơn |
| TC-23 | Đăng nhập staff, gõ `/admin/users` | Trang 403 |
| TC-24 | Dùng token customer gọi `PATCH /orders/12/status` (Swagger hoặc Postman) | API trả 403 |
| TC-25 | Đăng nhập sai mật khẩu; đăng nhập email không tồn tại | Cùng một thông báo "Email hoặc mật khẩu không đúng" |
| TC-26 | Sau đăng nhập, gõ `document.cookie` trong Console | Không thấy `access_token`; tab Application hiện cờ HttpOnly |
| TC-27 | Mở `/login?next=https://example.com` rồi đăng nhập | Về trang mặc định theo vai trò, không rời khỏi web |
| TC-28 | Đăng xuất, bấm Back của trình duyệt rồi tải lại | Không vào lại được trang được bảo vệ; refresh token cũ bị API từ chối |

TC-24 kiểm tra lớp 3 trực tiếp, bỏ qua giao diện web. Đây là loại test chứng minh phân quyền nằm ở server, không chỉ ở giao diện.

## Tóm tắt chương

- Xác thực xác định danh tính, phân quyền xác định quyền; backend đã có cả hai, web lo lưu và gửi token an toàn.
- Token nằm trong cookie `httpOnly`, `Secure`, `SameSite=Lax`; không bao giờ trong `localStorage`.
- Ma trận vai trò × chức năng là phân tích (CLO1) và là nguồn test case (CLO2).
- Ba lớp: `proxy.ts` chuyển hướng sớm (không xác minh), Data Access Layer bảo vệ trang và Server Action, API bảo vệ dữ liệu.
- Làm mới token trong `proxy`; đăng xuất thu hồi refresh token ở server.
- Nhận diện được kiểm soát truy cập hỏng, XSS, CSRF, lộ bí mật, CORS sai, open redirect.

## Câu hỏi ôn tập

1. Phân biệt xác thực và phân quyền bằng một ví dụ trong LHU Food.
2. Vì sao cookie `httpOnly` an toàn hơn `localStorage` để lưu token?
3. Vì sao đăng nhập sai email và sai mật khẩu phải cùng một thông báo?
4. `proxy.ts` đọc vai trò trong JWT mà không xác minh chữ ký. Điều đó có nguy hiểm không? Ứng dụng còn được bảo vệ ở đâu?
5. Vì sao không chỉ kiểm tra quyền trong `admin/layout.tsx`?
6. Vì sao đăng xuất phải gọi API thu hồi refresh token?
7. Viết test case cho ô "staff vào `/admin/products`" của ma trận.

## Bài tập

1. **Hồ sơ của tôi.** Trang `/profile` đọc `GET /users/me`, sửa họ tên qua `PATCH /users/me` bằng Server Action có kiểm tra Zod.
2. **Ma trận phân quyền.** Lập ma trận cho toàn bộ route của web nhóm, viết test case cho mọi ô ✘.
3. **Thử tấn công.** Tạo một JWT giả có `role: admin` (dùng jwt.io), đặt vào cookie `access_token`, mở `/admin/products`. Giải thích kết quả theo ba lớp.

## Tài liệu tham khảo

[1] MDN Web Docs, “Using HTTP cookies,” *MDN Web Docs*. Accessed: Oct. 30, 2026. [Online]. Available: https://developer.mozilla.org/docs/Web/HTTP/Guides/Cookies

[2] Vercel, “cookies,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/functions/cookies

[3] Vercel, “proxy.js,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/file-conventions/proxy

[4] NIST, “CVE-2025-29927,” *National Vulnerability Database*. Accessed: Oct. 30, 2026. [Online]. Available: https://nvd.nist.gov/vuln/detail/CVE-2025-29927

[5] Vercel, “Authentication,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/guides/authentication

[6] OWASP Foundation, “OWASP Top 10,” *OWASP*. Accessed: Oct. 30, 2026. [Online]. Available: https://owasp.org/Top10/

[7] Vercel, “Data Security,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/guides/data-security
