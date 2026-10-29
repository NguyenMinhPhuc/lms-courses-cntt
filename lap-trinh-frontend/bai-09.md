# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 5: DỮ LIỆU, FORM & LƯU TRỮ PHÍA CLIENT
### Bài 09: Form Validation (React Hook Form + Zod), Local Storage & Complex UI State

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Lớp học đảo ngược · **Chuẩn đầu ra:** PI 2.3 (CLO2)
> **Dự án xuyên suốt:** Smart Event Hub – Form Đăng nhập/Đăng ký, lưu Auth Token vào LocalStorage/Cookies, Form "Tạo sự kiện mới" cho Admin và tính năng Wishlist đồng bộ toàn ứng dụng.

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Giải thích cơ chế Uncontrolled Form của React Hook Form, vai trò của Zod Schema và `z.infer`; so sánh localStorage, sessionStorage và Cookies.
> * **[Bloom 3/4 - Kỹ năng]:** Xây dựng form có validation (email, độ dài mật khẩu, xác nhận mật khẩu, ràng buộc ngày) bằng `useForm` + `zodResolver` kết hợp Ant Design; viết hook `useLocalStorage` an toàn với hydration.
> * **[Bloom 5/6 - Năng lực]:** Thiết kế trạng thái Wishlist dùng chung giữa nhiều component, duy trì sau khi F5; đánh giá rủi ro bảo mật khi chọn nơi lưu token.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Một người dùng điền form đăng ký Smart Event Hub, gõ email thiếu dấu `@`, mật khẩu 3 ký tự, bấm "Đăng ký" và nhận về… một trang trắng vì Backend trả lỗi 400. Một Admin khác tạo sự kiện có ngày kết thúc **trước** ngày bắt đầu, hệ thống vẫn lưu và đăng lên trang chủ. Cả hai lỗi đều có thể chặn ngay trên trình duyệt, trước khi request kịp rời khỏi máy người dùng.

**Câu hỏi gợi mở:** Làm sao kiểm tra dữ liệu ngay khi gõ mà form không bị giật vì re-render liên tục? Bạn thả tim một sự kiện, bấm F5 – trái tim còn đỏ không? Và nếu bạn đọc `localStorage` ngay khi render, vì sao Next.js lại báo `window is not defined` hoặc Hydration Error?

> 🧭 **Trước giờ học (Flipped Classroom):** Xem video Web Storage API (LocalStorage), Form State Handling, Validation Schema (Zod/Yup). Đọc trang chủ *React Hook Form* và *Zod* (mục 5). Cài sẵn thư viện: `npm install react-hook-form zod @hookform/resolvers dayjs @ant-design/icons`. Làm quiz 5–10 câu trên LMS.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. React Hook Form + Zod: validation nhanh và type-safe

* **Khái niệm:** **React Hook Form (RHF)** quản lý form theo cơ chế **Uncontrolled Component**: giá trị nằm trong ref của input thay vì state, nên gõ phím không làm cả form re-render. **Zod** định nghĩa **Schema** kiểm tra dữ liệu; nối với RHF qua `zodResolver` từ `@hookform/resolvers/zod`. Điểm mạnh: `z.infer<typeof schema>` tự sinh TypeScript type từ chính schema, nên rule và type không bao giờ lệch nhau.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Rule thông dụng: bắt buộc nhập (`.min(1, ...)`), định dạng email (`.email()`), độ dài (`.min(6)`), so khớp mật khẩu (`.refine()` cấp object với `path`).
  * `useForm<T>({ resolver: zodResolver(schema), defaultValues, mode })`: `mode: 'onChange'` kiểm tra ngay khi gõ; `'onTouched'` chờ người dùng rời ô lần đầu.
  * Lấy lỗi qua `formState.errors.<field>?.message`; trạng thái gửi qua `formState.isSubmitting`.

```ts
// schemas/authSchema.ts
import { z } from 'zod';

export const loginSchema = z.object({
  email: z.string().min(1, 'Email là bắt buộc').email('Email không đúng định dạng'),
  password: z.string().min(6, 'Mật khẩu tối thiểu 6 ký tự'),
});
export type LoginInput = z.infer<typeof loginSchema>;

export const registerSchema = z
  .object({
    fullName: z.string().trim().min(2, 'Họ tên tối thiểu 2 ký tự'),
    email: z.string().min(1, 'Email là bắt buộc').email('Email không đúng định dạng'),
    password: z.string().min(6, 'Mật khẩu tối thiểu 6 ký tự'),
    confirmPassword: z.string().min(1, 'Vui lòng nhập lại mật khẩu'),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: 'Mật khẩu nhập lại không khớp',
    path: ['confirmPassword'], // Lỗi hiển thị dưới ô Nhập lại mật khẩu
  });
export type RegisterInput = z.infer<typeof registerSchema>;
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Form Thanh toán có 12 trường. Với `useState` cho từng ô, mỗi ký tự gõ vào ô "Địa chỉ" làm cả 12 ô render lại. Với RHF, chỉ phần hiển thị lỗi của ô đó cập nhật, form vẫn mượt trên điện thoại cấu hình thấp.

#### 2.2. Component LoginForm: RHF + Zod + Ant Design

* **Khái niệm:** Ant Design `Input` là component có giao diện riêng, nên chúng ta nối nó với RHF bằng **`Controller`**. Antd `Form` được đặt `component={false}` để chỉ mượn layout và kiểu hiển thị lỗi, còn việc submit do `handleSubmit` của RHF đảm nhận.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `Form.Item` nhận `validateStatus="error"` và `help={errors.email?.message}` để hiện chữ đỏ ngay dưới input.
  * Dùng `App.useApp()` lấy `message` – yêu cầu `app/layout.tsx` đã bọc `<App>` của antd (như Bài 08). Thông báo vẫn hiển thị khi `router.push('/')` chuyển trang.
  * Token lưu vào `localStorage` **chỉ trong hàm xử lý sự kiện**, không phải lúc render.

```tsx
// components/auth/LoginForm.tsx
'use client';

import { useRouter } from 'next/navigation';
import { Controller, useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { App, Button, Form, Input } from 'antd';
import { loginSchema, type LoginInput } from '@/schemas/authSchema';

// Giả lập API POST /auth/login – thay bằng authService thật khi Backend sẵn sàng
async function onLogin(values: LoginInput): Promise<{ accessToken: string }> {
  await new Promise((resolve) => setTimeout(resolve, 800));
  if (!values.email.endsWith('@lhu.edu.vn')) throw new Error('Sai email hoặc mật khẩu');
  return { accessToken: 'mock-token-123' };
}

export default function LoginForm() {
  const router = useRouter();
  const { message } = App.useApp();
  const {
    control,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginInput>({
    resolver: zodResolver(loginSchema),
    defaultValues: { email: '', password: '' },
    mode: 'onChange',
  });

  const onSubmit = async (values: LoginInput) => {
    try {
      const { accessToken } = await onLogin(values);
      localStorage.setItem('accessToken', accessToken);
      message.success('Đăng nhập thành công');
      router.push('/');
    } catch (error) {
      message.error(error instanceof Error ? error.message : 'Đăng nhập thất bại');
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} noValidate>
      <Form layout="vertical" component={false}>
        <Form.Item label="Email" validateStatus={errors.email ? 'error' : undefined} help={errors.email?.message}>
          <Controller
            name="email"
            control={control}
            render={({ field }) => <Input {...field} type="email" placeholder="ban@lhu.edu.vn" />}
          />
        </Form.Item>
        <Form.Item label="Mật khẩu" validateStatus={errors.password ? 'error' : undefined} help={errors.password?.message}>
          <Controller
            name="password"
            control={control}
            render={({ field }) => <Input.Password {...field} placeholder="Tối thiểu 6 ký tự" />}
          />
        </Form.Item>
        <Button type="primary" htmlType="submit" loading={isSubmitting} block>
          Đăng nhập
        </Button>
      </Form>
    </form>
  );
}
```

> ⚠️ **Bảo mật:** `localStorage` đọc được bởi mọi đoạn JavaScript trên trang, nên nếu site dính lỗi XSS thì token bị đánh cắp. Bài tập hôm nay dùng `localStorage` để luyện kỹ thuật; với sản phẩm thật, Auth Token nên nằm trong **httpOnly Cookie** do Backend thiết lập.

#### 2.3. Schema phức tạp: Form "Tạo sự kiện mới" với `.refine()`

* **Khái niệm:** Form Admin `/admin/create-event` có nhiều kiểu dữ liệu: chuỗi, số, URL, ngày giờ. Ràng buộc liên quan **hai trường cùng lúc** (ngày kết thúc phải sau ngày bắt đầu) được viết bằng `.refine()` trên cả object.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Lưu ngày dưới dạng **chuỗi ISO** trong form; `Controller` chuyển đổi qua lại với `Dayjs` mà `DatePicker` của antd yêu cầu.
  * `InputNumber` trả về `number | null`; schema `z.number({ message })` bắt cả trường hợp ô bị xóa trống.
  * `path: ['endDate']` gắn lỗi vào đúng ô Ngày kết thúc.

```ts
// schemas/eventSchema.ts
import { z } from 'zod';

export const createEventSchema = z
  .object({
    title: z.string().trim().min(5, 'Tên sự kiện tối thiểu 5 ký tự'),
    location: z.string().trim().min(1, 'Vui lòng nhập địa điểm'),
    startDate: z.string().min(1, 'Vui lòng chọn ngày bắt đầu'),
    endDate: z.string().min(1, 'Vui lòng chọn ngày kết thúc'),
    price: z.number({ message: 'Vui lòng nhập giá vé hợp lệ' }).positive('Giá vé phải lớn hơn 0'),
    coverImage: z.string().url('Ảnh bìa phải là một URL hợp lệ'),
    description: z.string().trim().min(20, 'Mô tả tối thiểu 20 ký tự'),
  })
  .refine((data) => new Date(data.endDate).getTime() > new Date(data.startDate).getTime(), {
    message: 'Ngày kết thúc phải sau ngày bắt đầu',
    path: ['endDate'],
  });

export type CreateEventInput = z.infer<typeof createEventSchema>;
```

```tsx
// Trích đoạn trong components/admin/CreateEventForm.tsx ('use client')
// import dayjs from 'dayjs'; import { DatePicker, InputNumber } from 'antd';
<Form.Item label="Ngày kết thúc" validateStatus={errors.endDate ? 'error' : undefined} help={errors.endDate?.message}>
  <Controller
    name="endDate"
    control={control}
    render={({ field }) => (
      <DatePicker
        showTime
        style={{ width: '100%' }}
        value={field.value ? dayjs(field.value) : null}
        onChange={(date) => field.onChange(date ? date.toISOString() : '')}
        onBlur={field.onBlur}
      />
    )}
  />
</Form.Item>

<Form.Item label="Giá vé (VNĐ)" validateStatus={errors.price ? 'error' : undefined} help={errors.price?.message}>
  <Controller
    name="price"
    control={control}
    render={({ field }) => (
      <InputNumber min={0} step={10000} style={{ width: '100%' }} value={field.value} onChange={field.onChange} onBlur={field.onBlur} />
    )}
  />
</Form.Item>
```

`useForm<CreateEventInput>` cần `defaultValues` đầy đủ: `{ title: '', location: '', startDate: '', endDate: '', price: 0, coverImage: '', description: '' }`.

* **💡 Ví dụ thực tế (Real-world Example):**
  > Admin nhập workshop "React Summit" bắt đầu 20/12 9:00, kết thúc 20/12 8:00 do chọn nhầm giờ. Ngay khi rời ô, dòng đỏ "Ngày kết thúc phải sau ngày bắt đầu" xuất hiện dưới ô Ngày kết thúc, nút Lưu không gửi request. Backend không phải nhận dữ liệu rác.

#### 2.4. Web Storage API & Hydration Safety

* **Khái niệm:** Trình duyệt cung cấp ba nơi lưu dữ liệu phía client. Chọn sai nơi lưu có thể gây lỗi bảo mật hoặc mất dữ liệu.

| Tiêu chí | localStorage | sessionStorage | Cookies |
|---|---|---|---|
| Thời gian tồn tại | Đến khi bị xóa | Đến khi đóng tab | Theo `Expires`/`Max-Age` |
| Gửi kèm request | Không | Không | Có, tự động |
| JavaScript đọc được | Có | Có | Có, trừ httpOnly |
| Dùng cho | Wishlist, theme, tùy chọn UI | Bước tạm của form nhiều trang | Auth Token (httpOnly), phiên đăng nhập |

* **Chi tiết kỹ thuật / Lý thuyết:**
  * Client Component vẫn được **render trước trên server**, nơi không có `window`. Đọc `localStorage` khi render sẽ gây `window is not defined`, hoặc HTML server và client khác nhau → **Hydration Mismatch**.
  * Cách an toàn: render lần đầu bằng giá trị mặc định (giống server), **đọc storage trong `useEffect`** sau khi mount, rồi cập nhật state.
  * Đọc Cookie trên server trong Next.js 15: `const token = (await cookies()).get('accessToken')?.value;` (hàm `cookies()` từ `next/headers` trả về Promise).

```ts
// hooks/useLocalStorage.ts – an toàn với SSR/hydration
'use client';

import { useEffect, useState } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(initialValue);
  const [isHydrated, setIsHydrated] = useState(false);

  // 1) Chỉ đọc localStorage sau khi đã mount trên trình duyệt
  useEffect(() => {
    try {
      const item = window.localStorage.getItem(key);
      if (item !== null) setStoredValue(JSON.parse(item) as T);
    } catch {
      // JSON hỏng hoặc trình duyệt chặn storage → giữ initialValue
    }
    setIsHydrated(true);
  }, [key]);

  // 2) Ghi lại mỗi khi giá trị thay đổi, bỏ qua lần render trước khi hydrate
  useEffect(() => {
    if (!isHydrated) return;
    try {
      window.localStorage.setItem(key, JSON.stringify(storedValue));
    } catch {
      // Hết dung lượng hoặc chế độ ẩn danh chặn ghi
    }
  }, [key, storedValue, isHydrated]);

  return [storedValue, setStoredValue, isHydrated] as const;
}
```

> 💡 **Vì sao cần `isHydrated`?** Nếu thiếu cờ này, effect ghi sẽ chạy ngay lần đầu và lưu đè `initialValue` (mảng rỗng) lên dữ liệu thật trước khi kịp đọc. Hook giả định `key` cố định trong suốt vòng đời component. Muốn đồng bộ giữa nhiều tab, có thể lắng nghe thêm sự kiện `storage` của `window`.

* **💡 Ví dụ thực tế (Real-world Example):**
  > Phiên bản đầu của nhóm dùng `useState(JSON.parse(localStorage.getItem('wishlist') ?? '[]'))`. `npm run dev` báo Hydration Error, còn `npm run build` thất bại với `localStorage is not defined`. Chuyển sang `useLocalStorage` giải quyết cả hai.

#### 2.5. Complex UI State: Wishlist đồng bộ giữa nhiều component

* **Khái niệm:** Trái tim Wishlist xuất hiện ở Card trang chủ, trang chi tiết và trang `/user/wishlist`. Nếu mỗi nơi tự gọi `useLocalStorage`, chúng giữ các bản state riêng: thả tim ở Card nhưng bộ đếm trên Header không đổi. Giải pháp là **nâng state lên một Context Provider** dùng chung.
* **Chi tiết kỹ thuật / Lý thuyết:** Provider giữ state bằng `useLocalStorage`; component con đọc qua hook `useWishlist()`. Chỉ hiển thị trạng thái "đã thích" khi `isHydrated` để HTML server và client trùng nhau.

```tsx
// contexts/WishlistContext.tsx
'use client';

import { createContext, useCallback, useContext, useMemo, type ReactNode } from 'react';
import { useLocalStorage } from '@/hooks/useLocalStorage';

interface WishlistContextValue {
  ids: string[];
  isHydrated: boolean;
  isWishlisted: (id: string) => boolean;
  toggle: (id: string) => void;
}

const WishlistContext = createContext<WishlistContextValue | null>(null);

export function WishlistProvider({ children }: { children: ReactNode }) {
  const [ids, setIds, isHydrated] = useLocalStorage<string[]>('seh-wishlist', []);

  const toggle = useCallback(
    (id: string) => setIds((prev) => (prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id])),
    [setIds],
  );

  const value = useMemo<WishlistContextValue>(
    () => ({ ids, isHydrated, isWishlisted: (id) => ids.includes(id), toggle }),
    [ids, isHydrated, toggle],
  );

  return <WishlistContext.Provider value={value}>{children}</WishlistContext.Provider>;
}

export function useWishlist(): WishlistContextValue {
  const ctx = useContext(WishlistContext);
  if (!ctx) throw new Error('useWishlist phải được dùng bên trong <WishlistProvider>');
  return ctx;
}
```

```tsx
// components/events/WishlistButton.tsx
'use client';

import { HeartFilled, HeartOutlined } from '@ant-design/icons';
import { Button } from 'antd';
import { useWishlist } from '@/contexts/WishlistContext';

export default function WishlistButton({ eventId }: { eventId: string }) {
  const { isHydrated, isWishlisted, toggle } = useWishlist();
  const active = isHydrated && isWishlisted(eventId);

  return (
    <Button
      type="text"
      shape="circle"
      aria-pressed={active}
      aria-label={active ? 'Bỏ khỏi danh sách yêu thích' : 'Thêm vào danh sách yêu thích'}
      icon={active ? <HeartFilled style={{ color: '#ef4444' }} /> : <HeartOutlined />}
      onClick={() => toggle(eventId)}
    />
  );
}
```

Đặt `<WishlistProvider>` bao quanh `{children}` trong `app/layout.tsx` (Server Component vẫn render được Client Provider). Trang `/user/wishlist` dùng `ids` từ `useWishlist()` để lọc/gọi API lấy thông tin các sự kiện đã lưu.

* **💡 Ví dụ thực tế (Real-world Example):**
  > Người dùng thả tim 3 concert trên trang chủ, Header lập tức hiện "Yêu thích (3)". Họ tắt máy, sáng hôm sau mở lại, danh sách vẫn còn nguyên. Đây chính là output mong muốn của Team Challenge hôm nay.

#### 2.6. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

AI sinh Zod Schema và form rất nhanh, nhưng hay trộn cú pháp cũ – mới hoặc quên các chi tiết Next.js. Hãy dùng prompt có ràng buộc rõ ràng.

```text
Hãy tạo cho tôi Component `LoginForm.tsx` bằng Next.js ("use client") kết hợp React Hook Form,
Zod và Ant Design Input.
Yêu cầu chi tiết:
1. Định nghĩa Zod Schema `loginSchema`:
   - email: Chuỗi, bắt buộc, đúng định dạng Email.
   - password: Chuỗi, bắt buộc, tối thiểu 6 ký tự.
2. Tích hợp `useForm` với `zodResolver(loginSchema)`.
3. Khi submit hợp lệ, gọi hàm `onLogin(values)` giả lập, lưu token vào
   `localStorage.setItem('accessToken', 'mock-token-123')` và hiển thị Antd `message.success("Đăng nhập thành công")`.
4. Hiển thị error message màu đỏ dưới ô input nếu dữ liệu không hợp lệ.
Ràng buộc: TypeScript strict, type lấy từ z.infer, dùng Controller cho Input của antd.
```

```text
Hãy viết một Zod Schema tên là `createEventSchema` cho Form Tạo sự kiện có ràng buộc nâng cao:
- `title`: string, min 5 chars.
- `startDate`: date string.
- `endDate`: date string.
- Sử dụng hàm `.refine()` của Zod để kiểm tra `endDate` phải có thời gian lớn hơn `startDate`.
Cho tôi mã nguồn Zod Schema và cách dùng với React Hook Form.
```

**Checklist kiểm duyệt code AI:**
* Import đúng: `zodResolver` từ `@hookform/resolvers/zod`; type lấy bằng `z.infer`, không khai báo interface trùng lặp.
* `defaultValues` có đủ mọi trường (tránh cảnh báo uncontrolled → controlled).
* Component antd (`Input`, `DatePicker`, `InputNumber`) được nối qua `Controller`; `DatePicker` nhận `Dayjs`, không nhận chuỗi.
* `.refine()` có `path` để lỗi hiện đúng ô.
* Không đọc `localStorage`/`window` trong lúc render; có `'use client'`; không `console.log` token.

#### 2.7. Thực hành trên lớp

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Guided Practice | 45' | Cài `react-hook-form`, `zod`, `@hookform/resolvers`; tạo `loginSchema`; xây `LoginForm.tsx` lưu JWT vào localStorage | Lỗi hiện ngay khi gõ; đăng nhập thành công lưu token và về Trang chủ |
| Unguided Practice | 45' | Form "Tạo sự kiện mới" `/admin/create-event` với `createEventSchema` | Bắt được mọi trường hợp ngày tháng, giá vé, URL không hợp lệ |
| Team Challenge | 60' | Tính năng Wishlist toàn app + trang `/user/wishlist` | F5 vẫn giữ đúng trạng thái; các component đồng bộ tức thì |
| Tổng kết | 15' | GV chữa lỗi hydration/validation phổ biến, giao BTVN | Danh sách lỗi cần sửa của từng nhóm |

* **Guided (45'):** Theo giảng viên tạo `schemas/authSchema.ts` và `LoginForm.tsx`. Form hiển thị lỗi validation ngay dưới từng input, submit gọi API Login (giả lập), lưu JWT vào `localStorage` và chuyển hướng về Trang chủ.
* **Unguided (45'):** Tự xây form Admin gồm Tên sự kiện, Địa điểm, Ngày bắt đầu/kết thúc (DatePicker), Giá vé (> 0), Ảnh bìa (URL), Mô tả; ràng buộc Ngày kết thúc sau Ngày bắt đầu.
* **Team Challenge (60'):** Bấm icon trái tim trên bất kỳ Card nào để thêm/xóa khỏi Wishlist; lưu danh sách ID vào `localStorage`; tạo trang `/user/wishlist` render các sự kiện đã lưu; đảm bảo đồng bộ state giữa các component trên cùng trang.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)
* 🔹 **RHF giảm re-render:** form uncontrolled, chỉ cập nhật phần cần thiết; `Controller` dùng cho component UI như antd.
* 🔹 **Zod là nguồn sự thật duy nhất:** rule validation và TypeScript type (`z.infer`) sinh từ cùng một schema.
* 🔹 **Ràng buộc nhiều trường dùng `.refine()` + `path`:** xác nhận mật khẩu, ngày kết thúc sau ngày bắt đầu.
* 🔹 **Chọn đúng nơi lưu:** localStorage cho dữ liệu UI không nhạy cảm; Auth Token thật nên ở httpOnly Cookie.
* 🔹 **Hydration safety:** chỉ đọc `localStorage` trong `useEffect`, render lần đầu bằng giá trị mặc định.
* 🔹 **State dùng chung → Context Provider:** Wishlist đồng bộ mọi component và tồn tại sau F5.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Vì sao React Hook Form giúp form nhiều trường mượt hơn so với dùng `useState` cho từng ô?
- A. RHF tự động gửi dữ liệu lên server sau mỗi ký tự
- B. RHF quản lý giá trị theo cơ chế uncontrolled (ref), hạn chế re-render toàn form
- C. RHF chỉ hoạt động trong Server Component
- D. RHF thay thế hoàn toàn nhu cầu validation

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Giá trị input nằm trong ref, không phải state của component, nên gõ phím không kích hoạt render lại cả form.
</details>

**Câu 2:** Để lỗi "Mật khẩu nhập lại không khớp" hiển thị dưới ô `confirmPassword`, cần làm gì với `.refine()`?
- A. Đặt `.refine()` bên trong `z.string()` của `password`
- B. Gọi `.refine()` hai lần
- C. Khai báo `path: ['confirmPassword']` trong tham số thứ hai
- D. Thêm `mode: 'onSubmit'` vào `useForm`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> <code>.refine()</code> cấp object mặc định gắn lỗi vào gốc form; <code>path</code> chỉ định trường nhận lỗi để RHF hiển thị qua <code>errors.confirmPassword</code>.
</details>

**Câu 3:** Đoạn `const [list] = useState(JSON.parse(localStorage.getItem('wishlist') ?? '[]'))` trong Client Component gây ra vấn đề gì?
- A. Lỗi `localStorage is not defined` khi render trên server hoặc Hydration Mismatch
- B. Không có vấn đề vì đã có `'use client'`
- C. Chỉ chậm hơn một chút
- D. localStorage tự xóa sau mỗi lần render

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> Client Component vẫn được prerender trên server, nơi không có <code>localStorage</code>. Cần đọc trong <code>useEffect</code> như hook <code>useLocalStorage</code>.
</details>

**Câu 4:** Nơi lưu Auth Token nào an toàn nhất trước tấn công XSS?
- A. localStorage
- B. sessionStorage
- C. Biến toàn cục `window.token`
- D. httpOnly Cookie do server thiết lập

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> JavaScript trên trang không đọc được httpOnly Cookie, nên mã độc XSS không lấy được token; trình duyệt vẫn tự gửi cookie kèm request.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-09-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)
* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Đã có validation phía client bằng Zod, Backend còn cần validate lại không? Hãy nêu ít nhất hai tình huống người dùng có thể vượt qua validation trên trình duyệt, và đề xuất cách chia sẻ cùng một schema giữa Front-End và Back-End.
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Tất cả thành viên đăng ký tài khoản **GitHub** và **Vercel**.
  * Đẩy code mới nhất (Login, Create Event, Wishlist) lên GitHub; kiểm tra kết nối Repository với Vercel Dashboard để sẵn sàng cho các buổi PBL Deploy.
  * **Output:** 100% thành viên có tài khoản Vercel sẵn sàng kết nối CI/CD; ảnh chụp màn hình Vercel Dashboard đã thấy repo của nhóm.
  * **Hạn nộp:** trước buổi học tiếp theo. Commit cuối theo mẫu `feat(wishlist): persist favorite events in localStorage`; nộp link repo + ảnh chụp lên LMS với tên file `B09_<TenNhom>_Vercel.png`.
* **📚 Tài liệu đọc & tham khảo:**
  * React Hook Form Documentation: https://react-hook-form.com/
  * Zod Documentation: https://zod.dev/
  * Hook Form Resolvers: https://github.com/react-hook-form/resolvers
  * MDN – Window.localStorage: https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
  * Next.js `cookies()`: https://nextjs.org/docs/app/api-reference/functions/cookies
