# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 5: DỮ LIỆU, FORM & LƯU TRỮ PHÍA CLIENT
### Bài 08: Data Fetching & tích hợp RESTful API

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Lớp học đảo ngược · **Chuẩn đầu ra:** PI 2.3 (CLO2)
> **Dự án xuyên suốt:** Smart Event Hub – kết nối RESTful API / Swagger UI Backend có sẵn, thay toàn bộ Mock JSON bằng dữ liệu động (danh sách và chi tiết sự kiện, danh mục, tìm kiếm – phân trang, đặt vé).

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Phân biệt Data Fetching trong Server Component và Client Component; giải thích cơ chế caching và `revalidate` của `fetch` trong Next.js.
> * **[Bloom 3/4 - Kỹ năng]:** Xây dựng Generic Interface `ApiResponse<T>`, `PaginatedData<T>`, tầng service `eventService.ts` bằng Axios; render dữ liệu dạng mảng (danh sách) và dạng đơn (chi tiết theo `id`) với Loading, Error, 404.
> * **[Bloom 5/6 - Năng lực]:** Dùng AI chuyển Swagger JSON thành DTO/Interface/Service, đánh giá và sửa output AI để đạt type-safety tuyệt đối, không dùng `any`.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Đến hết giữa kỳ, trang chủ Smart Event Hub vẫn đọc dữ liệu từ file `mockEvents.json`. Ban tổ chức thêm một concert mới trên hệ thống quản trị, nhưng người dùng không thấy gì cho đến khi lập trình viên sửa file JSON và deploy lại. Thực tế không ứng dụng đặt vé nào vận hành như vậy: dữ liệu phải chảy từ Backend qua RESTful API lên giao diện theo thời gian thực.

**Câu hỏi gợi mở:** Nên gọi API ngay trên server khi render trang, hay để trình duyệt tự gọi sau khi tải xong? Khi API trả về một object JSON có 30 trường lồng nhau, làm sao để TypeScript "hiểu" đúng từng trường mà không phải gõ tay từng dòng interface? Và nếu Backend sập lúc 8 giờ tối, người dùng sẽ thấy gì?

> 🧭 **Trước giờ học (Flipped Classroom):** Xem video RESTful API concepts, Fetch API, Axios, Async/Await trong TypeScript. Đọc tài liệu *Next.js Data Fetching, Caching, and Revalidating* và *Axios Documentation* (mục 5). Mở Swagger UI của Backend Smart Event Hub do giảng viên cung cấp, thử gọi `GET /events` và lưu lại một JSON response mẫu. Làm quiz 5–10 câu trên LMS.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Data Fetching trong Next.js: Server Component vs Client Component

* **Khái niệm:** Next.js App Router cho phép lấy dữ liệu ở hai nơi. **Server-side fetching** dùng `async/await` trực tiếp trong Server Component, HTML trả về đã có sẵn dữ liệu. **Client-side fetching** dùng Axios hoặc SWR/TanStack Query trong Client Component, phù hợp với dữ liệu cần tương tác liên tục hoặc cập nhật thời gian thực.
* **Chi tiết kỹ thuật / Lý thuyết:**

| Tiêu chí | Server Component | Client Component |
|---|---|---|
| Nơi chạy | Server (Node.js), lúc render trang | Trình duyệt, sau khi trang hydrate |
| Cú pháp | `export default async function Page()` + `await` | `useEffect` + `useState`, hoặc SWR/TanStack Query |
| SEO | HTML đã có dữ liệu, tốt cho SEO | Dữ liệu xuất hiện sau, bot có thể không thấy |
| Bảo mật | Giữ được secret/API key phía server | Mọi request lộ trong tab Network |
| Dùng cho | Danh sách sự kiện, trang chi tiết | Tìm kiếm khi gõ, POST đặt vé, dữ liệu realtime |

  * Next.js mở rộng `fetch` native với tùy chọn **caching** (`cache: 'force-cache'`) và **revalidation** (`next: { revalidate: giây }`). Từ **Next.js 15, `fetch` không còn được cache mặc định**, vì vậy muốn cache phải khai báo rõ ràng.
  * `revalidate: 3600` nghĩa là kết quả được dùng lại tối đa 1 giờ; request đầu tiên sau mốc đó vẫn nhận bản cũ, đồng thời Next.js lấy bản mới ở nền cho lượt sau.

```ts
// services/eventServer.ts – Fetch trên Server Component có caching/revalidate
import type { ApiResponse, PaginatedData } from '@/types/api';
import type { IEventItem } from '@/types/event';

export async function getFeaturedEvents(): Promise<PaginatedData<IEventItem>> {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/events?page=1&limit=8`, {
    next: { revalidate: 3600 }, // Làm mới tối đa mỗi 1 giờ
  });
  if (!res.ok) throw new Error(`Không tải được danh sách sự kiện (HTTP ${res.status})`);
  const json = (await res.json()) as ApiResponse<PaginatedData<IEventItem>>;
  return json.data;
}
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Danh sách "Sự kiện nổi bật" ít thay đổi trong ngày, nên fetch trên server với `revalidate: 3600` giúp trang chủ tải nhanh và chia sẻ link lên Zalo vẫn hiện đúng nội dung. Ngược lại, ô tìm kiếm gợi ý theo từng ký tự gõ phải chạy ở Client Component vì phụ thuộc thao tác người dùng.

#### 2.2. Type-safe API: Generic Response, DTO và ViewModel

* **Khái niệm:** Backend RESTful thường bọc dữ liệu trong một "vỏ" chung gồm mã trạng thái, thông điệp và `data`. Khai báo vỏ này bằng **Generic Interface** giúp tái sử dụng cho mọi endpoint. **DTO (Data Transfer Object)** mô tả đúng hình dạng JSON Backend trả về; **ViewModel** là dữ liệu đã được định dạng sẵn để UI hiển thị.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `ApiResponse<T>` cho mọi response; `PaginatedData<T>` cho danh sách có phân trang.
  * DTO bám sát Swagger: ngày tháng là `string` (ISO 8601), trường có thể rỗng khai báo `| null`.
  * Hàm **mapper** chuyển DTO → ViewModel, gom logic định dạng tiền, ngày về một chỗ. Khi Backend đổi tên field, chỉ sửa mapper.

```ts
// types/api.ts
export interface ApiResponse<T> {
  statusCode: number;
  message: string;
  data: T;
}

export interface PaginatedData<T> {
  items: T[];
  total: number;
  page: number;
  limit: number;
}
```

```ts
// types/event.ts – DTO theo Swagger
export type EventStatus = 'UPCOMING' | 'ONGOING' | 'ENDED';

export interface IOrganizer {
  id: string;
  name: string;
  email: string;
  avatarUrl: string | null;
}

export interface ICategory {
  id: string;
  name: string;
  slug: string;
}

export interface IEventItem {
  id: string;
  title: string;
  bannerUrl: string;
  location: string;
  startDate: string; // ISO 8601
  price: number;
  status: EventStatus;
  category: ICategory;
  organizer: IOrganizer;
}

// ViewModel cho EventCard
export interface EventCardVM {
  id: string;
  title: string;
  bannerUrl: string;
  dateLabel: string;
  priceLabel: string;
  status: EventStatus;
}
```

```ts
// lib/mappers/event.ts
import type { EventCardVM, IEventItem } from '@/types/event';

const dateFmt = new Intl.DateTimeFormat('vi-VN', { dateStyle: 'medium', timeZone: 'Asia/Ho_Chi_Minh' });
const priceFmt = new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' });

export function toEventCardVM(dto: IEventItem): EventCardVM {
  return {
    id: dto.id,
    title: dto.title,
    bannerUrl: dto.bannerUrl,
    dateLabel: dateFmt.format(new Date(dto.startDate)),
    priceLabel: dto.price === 0 ? 'Miễn phí' : priceFmt.format(dto.price),
    status: dto.status,
  };
}
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Backend đổi `bannerUrl` thành `coverImage` ở phiên bản API mới. Nhờ DTO và mapper, nhóm chỉ sửa 2 dòng trong `types/event.ts` và `toEventCardVM`, TypeScript tự chỉ ra mọi chỗ còn dùng tên cũ. Không ai phải lục từng component.

#### 2.3. Tầng Service với Axios: danh sách (Array Data)

* **Khái niệm:** **Service layer** là các hàm gọi API tập trung trong thư mục `services/`. Component không gọi `axios` trực tiếp mà gọi `getEvents()`, `getEventById()`… Nhờ đó URL, header, xử lý lỗi nằm ở một nơi, dễ kiểm thử và dễ thay đổi.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Tạo một Axios instance với `baseURL` đọc từ biến môi trường `NEXT_PUBLIC_API_URL` (khai báo trong `.env.local`), không hard-code URL.
  * Truyền kiểu generic cho `http.get<...>()` để `res.data` có type chính xác.
  * Trong Next.js 15, `searchParams` của page là **Promise**, cần `await` trước khi dùng.

```ts
// lib/http.ts
import axios from 'axios';

export const http = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL, // ví dụ: https://<backend-cua-lop>/api/v1
  timeout: 10_000,
  headers: { 'Content-Type': 'application/json' },
});
```

```ts
// services/eventService.ts
import axios from 'axios';
import { http } from '@/lib/http';
import type { ApiResponse, PaginatedData } from '@/types/api';
import type { ICategory, IEventItem } from '@/types/event';

export interface GetEventsParams {
  page?: number;
  limit?: number;
  search?: string;
  categoryId?: string;
}

export async function getEvents(params: GetEventsParams = {}): Promise<PaginatedData<IEventItem>> {
  const res = await http.get<ApiResponse<PaginatedData<IEventItem>>>('/events', { params });
  return res.data.data;
}

export async function getEventById(id: string): Promise<IEventItem | null> {
  try {
    const res = await http.get<ApiResponse<IEventItem>>(`/events/${encodeURIComponent(id)}`);
    return res.data.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response?.status === 404) return null;
    throw error; // Network Error / 500 → để error.tsx xử lý
  }
}

export async function getCategories(): Promise<ICategory[]> {
  const res = await http.get<ApiResponse<ICategory[]>>('/categories');
  return res.data.data;
}

export interface CreateOrderPayload {
  eventId: string;
  ticketType: 'VVIP' | 'VIP' | 'STANDARD';
  quantity: number;
}

export interface IOrder {
  id: string;
  totalAmount: number;
}

export async function createOrder(payload: CreateOrderPayload): Promise<IOrder> {
  const res = await http.post<ApiResponse<IOrder>>('/orders', payload);
  return res.data.data;
}
```

```tsx
// app/page.tsx – Server Component: fetch danh sách rồi truyền props
import EventList from '@/components/events/EventList';
import { toEventCardVM } from '@/lib/mappers/event';
import { getEvents } from '@/services/eventService';

interface HomePageProps {
  searchParams: Promise<{ page?: string; search?: string }>;
}

export default async function HomePage({ searchParams }: HomePageProps) {
  const { page = '1', search = '' } = await searchParams;
  const data = await getEvents({ page: Number(page) || 1, limit: 12, search });

  return (
    <EventList
      events={data.items.map(toEventCardVM)}
      total={data.total}
      page={data.page}
      pageSize={data.limit}
    />
  );
}
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > URL `/?search=rock&page=2` được đọc ngay trên server, nên người dùng copy link gửi bạn bè sẽ thấy đúng trang 2 kết quả "rock". Đây cũng là cách Member 2 trong Team Challenge làm tính năng Tìm kiếm & Phân trang.

#### 2.4. Dữ liệu đơn (Single Data): trang chi tiết, 404, Loading và Error

* **Khái niệm:** Trang `/events/[id]` lấy **một** sự kiện theo `id` trên URL. Ba trạng thái phải xử lý đủ: **đang tải** (`loading.tsx`), **không tồn tại** (`notFound()` → `not-found.tsx`), **lỗi máy chủ** (`error.tsx`).
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `params` là Promise trong Next.js 15: `const { id } = await params;`.
  * `notFound()` từ `next/navigation` hoạt động bằng cách ném một lỗi đặc biệt. **Không gọi `notFound()` bên trong `try` có `catch` bắt mọi lỗi**, nếu không trang 404 sẽ bị "nuốt". Vì vậy `getEventById` tự xử lý 404 và trả `null`.
  * `error.tsx` bắt buộc là Client Component, nhận props `error` và `reset`.

```tsx
// app/events/[id]/page.tsx
import Image from 'next/image';
import { notFound } from 'next/navigation';
import { getEventById } from '@/services/eventService';

interface PageProps {
  params: Promise<{ id: string }>;
}

export default async function EventDetailPage({ params }: PageProps) {
  const { id } = await params;
  const event = await getEventById(id);
  if (!event) notFound(); // TypeScript hiểu từ đây event không còn null

  return (
    <article>
      <Image src={event.bannerUrl} alt={event.title} width={1200} height={480} priority />
      <h1>{event.title}</h1>
      <p>Giá vé: {event.price.toLocaleString('vi-VN')} đ</p>
      <p>Ban tổ chức: {event.organizer.name} ({event.organizer.email})</p>
    </article>
  );
}
```

```tsx
// app/events/[id]/error.tsx
'use client';

import { useEffect } from 'react';
import { Button, Result } from 'antd';

export default function EventDetailError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  useEffect(() => {
    console.error(error); // Gửi lên công cụ log nếu có
  }, [error]);

  return (
    <Result
      status="500"
      title="Không tải được sự kiện"
      subTitle="Máy chủ đang gián đoạn, vui lòng thử lại sau."
      extra={<Button type="primary" onClick={reset}>Thử lại</Button>}
    />
  );
}
```

```tsx
// app/events/[id]/loading.tsx
import { Skeleton } from 'antd';

export default function Loading() {
  return <Skeleton active paragraph={{ rows: 6 }} />;
}
```

> ⚠️ **Lưu ý:** `next/image` với ảnh từ domain Backend cần khai báo `images.remotePatterns` trong `next.config.ts`, nếu không trang sẽ báo lỗi "hostname is not configured".

* **💡 Ví dụ thực tế (Real-world Example):**
  > Người dùng mở link cũ `/events/abc-2023` của một sự kiện đã bị xóa. Thay vì trang trắng hay lỗi 500, họ thấy trang 404 thân thiện kèm nút "Xem sự kiện khác". Đó là khác biệt giữa sản phẩm demo và sản phẩm thật.

#### 2.5. Client-side Fetching: danh mục, đặt vé và trạng thái Loading

* **Khái niệm:** Khi dữ liệu phụ thuộc thao tác người dùng (chọn danh mục, bấm Đặt vé), chúng ta gọi API trong Client Component. Mỗi lần gọi phải thể hiện rõ trạng thái bằng **Spin/Skeleton** của Ant Design và thông báo kết quả bằng **Notification**.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Dùng biến cờ `ignore` trong `useEffect` để bỏ qua kết quả trả về sau khi component đã unmount.
  * Dùng `App.useApp()` để lấy `notification` theo đúng theme. Yêu cầu: `app/layout.tsx` bọc nội dung trong `<App>` của antd (bên trong `ConfigProvider`).
  * Với dữ liệu fetch lặp lại nhiều nơi, có thể dùng SWR/TanStack Query để có sẵn cache, retry, `isLoading`.

```tsx
// components/events/CategoryFilter.tsx – dùng bên trong một Client Component cha (FilterBar)
'use client';

import { useEffect, useState } from 'react';
import { Alert, Select } from 'antd';
import { getCategories } from '@/services/eventService';
import type { ICategory } from '@/types/event';

interface CategoryFilterProps {
  onChange: (categoryId: string | undefined) => void;
}

export default function CategoryFilter({ onChange }: CategoryFilterProps) {
  const [categories, setCategories] = useState<ICategory[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let ignore = false;
    getCategories()
      .then((data) => { if (!ignore) setCategories(data); })
      .catch(() => { if (!ignore) setError('Không tải được danh mục sự kiện'); })
      .finally(() => { if (!ignore) setLoading(false); });
    return () => { ignore = true; };
  }, []);

  if (error) return <Alert type="error" message={error} showIcon />;

  return (
    <Select
      allowClear
      loading={loading}
      placeholder="Chọn danh mục"
      style={{ minWidth: 200 }}
      options={categories.map((c) => ({ value: c.id, label: c.name }))}
      onChange={(value: string | undefined) => onChange(value)}
    />
  );
}
```

```tsx
// components/booking/BookTicketButton.tsx – POST /orders
'use client';

import { useState } from 'react';
import axios from 'axios';
import { App, Button } from 'antd';
import { createOrder, type CreateOrderPayload } from '@/services/eventService';

export default function BookTicketButton({ payload }: { payload: CreateOrderPayload }) {
  const { notification } = App.useApp();
  const [submitting, setSubmitting] = useState(false);

  const handleBook = async () => {
    setSubmitting(true);
    try {
      const order = await createOrder(payload);
      notification.success({ message: 'Đặt vé thành công', description: `Mã đơn hàng: ${order.id}` });
    } catch (error) {
      const description =
        axios.isAxiosError(error) && error.response?.status === 409
          ? 'Hạng vé này vừa hết chỗ, vui lòng chọn hạng khác.'
          : 'Không thể kết nối máy chủ, vui lòng thử lại.';
      notification.error({ message: 'Đặt vé thất bại', description });
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Button type="primary" size="large" loading={submitting} onClick={handleBook}>
      Đặt vé ngay
    </Button>
  );
}
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Khi mạng 4G chập chờn, nút "Đặt vé ngay" chuyển sang trạng thái loading và bị vô hiệu hóa. Người dùng không thể bấm liên tục 5 lần tạo ra 5 đơn hàng trùng – một lỗi rất hay gặp ở các trang bán vé làm vội.

#### 2.6. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

Quy trình Vibe Coding của buổi này: **thả API Specification / JSON Swagger vào AI** để sinh DTO, Interface và hàm service. AI làm phần gõ phím lặp lại; các bạn chịu trách nhiệm đối chiếu với dữ liệu thật.

```text
Bạn là một Fullstack Developer. Dưới đây là JSON Response từ Swagger API danh sách sự kiện:
[Dán đoạn JSON Swagger API Response vào đây]

Yêu cầu:
1. Sinh các TypeScript Interfaces tương ứng (`IEventResponse`, `IEventItem`, `IOrganizer`).
2. Viết 1 file `services/eventService.ts` sử dụng `axios` để thực hiện hàm `getEvents(params)`
   với các query: `page`, `limit`, `search`.
3. Viết code ví dụ Fetch dữ liệu trong Server Component Next.js (`app/page.tsx`)
   và truyền props vào Component `EventList`.
Ràng buộc: Next.js 15 (searchParams là Promise), TypeScript strict, không dùng `any`.
```

```text
Viết giúp tôi hàm `getEventById(id: string)` trong `services/eventService.ts` và tích hợp vào
trang Next.js Server Component `/app/events/[id]/page.tsx`.
- Nếu không tìm thấy sự kiện (API trả về lỗi 404), gọi hàm `notFound()` từ `next/navigation`
  để chuyển hướng đến trang 404.
- Bổ sung Try/Catch block để bắt lỗi kết nối API.
```

**Checklist kiểm duyệt code AI:**
* Tên field trong interface khớp **từng ký tự** với JSON thật (`startDate` hay `start_date`?).
* Trường có thể `null` trong Swagger được khai báo `| null`; ngày tháng là `string`, không phải `Date`.
* Không có `any`, không có `as unknown as ...` để "lách" type checker.
* `notFound()` nằm ngoài khối `try/catch` bắt mọi lỗi; `params`/`searchParams` được `await`.
* URL lấy từ biến môi trường; component dùng `useEffect`/`useState` có `'use client'`.
* Mọi lời gọi API đều có trạng thái Loading và nhánh xử lý lỗi.

#### 2.7. Thực hành trên lớp

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Guided Practice | 45' | Sinh `IEvent` từ JSON `/api/v1/events`; viết `services/eventService.ts` với `getEvents()`; render danh sách ở `app/page.tsx` | Trang chủ hiển thị sự kiện từ API thật, không dùng `any` |
| Unguided Practice | 45' | Viết `getEventById(id)`; kết nối trang `/events/[id]`; hiển thị Banner, Tên, Giá vé, Ban tổ chức | Bấm từng Card mở đúng chi tiết theo `id` |
| Team Challenge | 60' | Chia việc gọi API: danh mục, tìm kiếm & phân trang, POST đặt vé; dùng Spin/Skeleton khi tải | Toàn bộ Mock JSON được thay bằng dữ liệu API thật |
| Tổng kết | 15' | GV chữa lỗi phổ biến, giải đáp, giao BTVN | Danh sách lỗi cần sửa của từng nhóm |

* **Guided (45'):** Thả JSON response mẫu của `/api/v1/events` vào AI để sinh interface, sau đó tự đối chiếu và chỉnh sửa. Viết `services/eventService.ts` với hàm `getEvents()` gọi API bằng Axios/Fetch. Kết nối vào `app/page.tsx` để render danh sách Card sự kiện.
* **Unguided (45'):** Tự viết hàm lấy chi tiết sự kiện (`getEventById`, có thể đặt tên `getEventDetail`) và tích hợp vào Dynamic Route `/events/[id]`. Hiển thị dữ liệu đơn lên giao diện; xử lý trường hợp 404 bằng `notFound()`.
* **Team Challenge (60'):** **Member 1** fetch `/api/categories` render vào Filter Bar. **Member 2** làm Tìm kiếm & Phân trang qua `/api/events?search=...&page=...`. **Member 3** tích hợp `POST /api/orders`, truyền payload từ Client lên Server và hiện Notification thành công. Mọi thao tác chờ API đều có Spin/Skeleton của Ant Design.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)
* 🔹 **Chọn đúng nơi fetch:** dữ liệu cần SEO, ít thay đổi → Server Component; dữ liệu phụ thuộc tương tác → Client Component.
* 🔹 **Next.js 15 không cache `fetch` mặc định:** muốn cache dùng `cache: 'force-cache'` hoặc `next: { revalidate: giây }`.
* 🔹 **Generic + DTO + mapper:** `ApiResponse<T>`, `PaginatedData<T>` cho vỏ response; DTO bám Swagger; mapper tạo ViewModel cho UI.
* 🔹 **Service layer:** component gọi `getEvents()`, không gọi `axios` trực tiếp; URL nằm trong `NEXT_PUBLIC_API_URL`.
* 🔹 **Đủ 3 trạng thái:** Loading (`loading.tsx`, Spin/Skeleton), 404 (`notFound()`), lỗi máy chủ (`error.tsx`, Notification).
* 🔹 **AI sinh – người duyệt:** luôn đối chiếu interface do AI sinh với JSON thật trước khi dùng.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Trong Next.js 15, đoạn `fetch(url, { next: { revalidate: 3600 } })` trong Server Component có ý nghĩa gì?
- A. Gọi lại API mỗi 3600 mili-giây trên trình duyệt
- B. Không bao giờ cache kết quả
- C. Dùng lại kết quả đã cache tối đa 1 giờ rồi mới lấy bản mới
- D. Chỉ cho phép gọi API 3600 lần mỗi ngày

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> <code>revalidate</code> tính bằng giây. Sau 3600 giây, Next.js làm mới dữ liệu ở lần request kế tiếp; trong khoảng đó dùng bản cache.
</details>

**Câu 2:** Vì sao nên khai báo `ApiResponse<T>` thay vì viết riêng interface vỏ response cho từng endpoint?
- A. Vì TypeScript bắt buộc mọi interface phải có generic
- B. Để tái sử dụng một cấu trúc vỏ chung, chỉ thay kiểu của `data`
- C. Để Axios tự động sinh dữ liệu mẫu
- D. Để không cần kiểm tra lỗi HTTP

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Mọi response có chung <code>statusCode</code>, <code>message</code>, <code>data</code>. Generic <code>T</code> cho phép dùng <code>ApiResponse&lt;IEventItem[]&gt;</code>, <code>ApiResponse&lt;ICategory[]&gt;</code>… mà không lặp code.
</details>

**Câu 3:** Đoạn code `try { const e = await getEvent(id); if (!e) notFound(); } catch { return <p>Lỗi</p>; }` gặp vấn đề gì?
- A. `notFound()` ném lỗi đặc biệt nên bị `catch` nuốt, trang 404 không hiển thị
- B. `notFound()` chỉ dùng được trong Client Component
- C. Không thể dùng `await` trong Server Component
- D. Không có vấn đề gì

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> <code>notFound()</code> hoạt động bằng cách throw. Khối <code>catch</code> bắt mọi lỗi sẽ chặn cơ chế này. Hãy xử lý 404 trong service (trả <code>null</code>) và gọi <code>notFound()</code> ngoài <code>try/catch</code>.
</details>

**Câu 4:** Tính năng gợi ý kết quả ngay khi người dùng gõ vào ô tìm kiếm nên fetch dữ liệu ở đâu?
- A. Trong `layout.tsx` gốc
- B. Trong Server Component với `revalidate: 3600`
- C. Trong file `next.config.ts`
- D. Trong Client Component (kết hợp debounce), dùng Axios hoặc SWR

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> Dữ liệu phụ thuộc từng thao tác gõ phím nên phải gọi từ trình duyệt; kết hợp debounce (Buổi 6) để tránh gọi API ở mỗi ký tự.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-08-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)
* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Trang Chi tiết sự kiện có phần "Số vé còn lại" thay đổi liên tục, trong khi mô tả sự kiện gần như cố định. Bạn sẽ chia phần nào fetch trên server, phần nào fetch trên client, và chọn `revalidate` bao nhiêu cho từng phần? Hãy lập luận dựa trên SEO, hiệu năng và trải nghiệm người dùng.
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Xử lý ngoại lệ khi API gặp sự cố (Network Error, Server 500) bằng cách kết hợp Ant Design Notification / Alert hoặc `error.tsx` cho các route đã tích hợp API.
  * **Output:** Web app hoạt động an toàn, có thông báo lỗi văn minh khi Server API gián đoạn. Ảnh chụp màn hình 3 trạng thái (Loading – Lỗi – Thành công) đính kèm trong mô tả PR.
  * **Hạn nộp:** trước buổi học tiếp theo. Branch `feature/api-error-handling-<mssv>`, PR đặt tên `feat(api): handle network and server errors – <Họ tên>`; nộp link PR lên LMS.
* **📚 Tài liệu đọc & tham khảo:**
  * Next.js Data Fetching, Caching, and Revalidating: https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating
  * Axios Documentation: https://axios-http.com/docs/intro
  * Next.js Error Handling: https://nextjs.org/docs/app/building-your-application/routing/error-handling
  * Next.js `notFound()`: https://nextjs.org/docs/app/api-reference/functions/not-found
