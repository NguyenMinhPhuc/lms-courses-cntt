# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## ĐẶC TẢ DỰ ÁN XUYÊN SUỐT: SMART EVENT HUB

> **Tên đầy đủ:** Smart Event Hub – Hệ thống Đặt vé & Quản lý Sự kiện trực tuyến
> **Quy mô:** Nhóm 3–4 sinh viên · **Thời gian:** Buổi 1 → Buổi 12 · **Đánh giá:** Giữa kỳ 30% (Buổi 7, 50% tiến độ) · Cuối kỳ 40% (Buổi 12)
> **Công nghệ:** Next.js 15 (App Router) · TypeScript strict · SCSS Module · Ant Design v5 · React Hook Form + Zod · Axios · Vercel

---

## 1. MỤC TIÊU DỰ ÁN

#### Sản phẩm cần đạt

Các bạn xây dựng phần **Front-End** của một nền tảng bán vé sự kiện: người dùng tìm sự kiện, xem chi tiết, chọn hạng vé hoặc chỗ ngồi, đặt vé và lưu sự kiện yêu thích; quản trị viên quản lý sự kiện và đơn đặt vé. Sản phẩm cuối cùng phải được deploy trên Vercel, gọi dữ liệu thật từ Backend, đạt Lighthouse Performance > 85 và SEO > 90.

**Backend không thuộc phạm vi của sinh viên.** Giảng viên cung cấp sẵn một RESTful API kèm tài liệu Swagger UI. Địa chỉ API, tài khoản thử nghiệm và đặc tả chính xác của từng endpoint được GV công bố trên LMS; tài liệu này không ghi URL thật.

#### Mục tiêu học tập gắn với dự án

| Chuẩn đầu ra | Thể hiện trong dự án |
|---|---|
| CLO1 – PI 1.4 | Wireframe 5 màn hình, cây component theo Atomic Design, sơ đồ route |
| CLO2 – PI 2.3 | Giao diện Next.js + TypeScript + SCSS/AntD, state với Hooks, gọi REST API, form + Zod, dùng AI có kiểm soát |
| CLO3 – PI 3.1 | README, báo cáo Word/PDF, thuyết trình demo giữa kỳ và cuối kỳ |
| CLO4 – PI 5.1 | Git branch/PR/review, CI/CD Vercel, SEO Metadata, Lighthouse |

#### Đối tượng sử dụng hệ thống

* **Khách (Guest):** xem trang chủ, danh sách, danh mục, chi tiết sự kiện.
* **Người dùng đã đăng nhập (User):** đặt vé, chọn ghế, xem trang cá nhân và lịch sử vé, quản lý Wishlist.
* **Quản trị viên (Admin):** xem dashboard, quản lý sự kiện, tạo sự kiện mới, quản lý đơn hàng, người dùng.

#### Ngoài phạm vi

Thanh toán trực tuyến thật (cổng thanh toán), viết Backend/cơ sở dữ liệu, gửi email/SMS. Bước "Thanh toán" trong dự án dừng ở việc gửi đơn `POST /api/orders` và hiển thị kết quả.

---

## 2. NĂM MÀN HÌNH CHÍNH

#### Danh sách màn hình và thành phần

| # | Màn hình | Route chính | Thành phần UI chính | Buổi xây dựng |
|---|---|---|---|---|
| 1 | **Trang chủ** | `/` (kèm `/events`) | HeroBanner (Carousel), CategoryFilter (Tabs), FeaturedEventsSection, lưới EventCard, EventFilterBar, Header, Footer | 1, 2, 5, 6, 8 |
| 2 | **Chi tiết sự kiện** | `/events/[id]` | Banner 16:9, tiêu đề, thông tin ban tổ chức/diễn giả, mô tả, bảng hạng vé, Sticky Sidebar đặt vé, Rate | 2, 4, 8, 11 |
| 3 | **Đặt vé** | `/checkout/[id]` | TicketQuantitySelector (VVIP/VIP/Standard), SeatMatrixPicker 5×8, BookingModal, tóm tắt đơn, nút thanh toán | 5, 6, 8 |
| 4 | **Trang cá nhân** | `/user/profile` (kèm `/user/wishlist`) | Thông tin tài khoản, lịch sử vé, danh sách Wishlist | 3, 9 |
| 5 | **Admin Dashboard** | `/admin/dashboard` (kèm `/admin/orders`, `/admin/manage-events`, `/admin/create-event`) | AdminLayout có Sidebar, Table đơn hàng + Tag trạng thái, form tạo sự kiện | 3, 5, 9 |

> 📝 **Về danh sách màn hình:** kế hoạch Buổi 2 liệt kê "Danh sách & Lọc sự kiện" như một màn hình riêng thay cho Admin Dashboard. Đặc tả này theo đề cương (5 màn hình như bảng trên); phần danh sách và lọc được xem là một phần của Trang chủ/`/events`. Nhóm vẽ thêm wireframe cho màn hình Listing là điểm cộng.

#### Luồng người dùng chính (User Flow)

```text
Trang chủ (/)
  ├─ bấm Badge thể loại ──► /category/[slug] ──┐
  ├─ tìm kiếm / lọc ─────► /events?search=…  ──┤
  └─ bấm EventCard ─────────────────────────────┴─► /events/[id]
                                                      └─ bấm "Đặt vé ngay" ─► /checkout/[id]
                                                            (chưa đăng nhập ─► /login ─► quay lại)
                                                            └─ gửi đơn POST /api/orders ─► thông báo thành công ─► /user/profile
```

---

## 3. DANH SÁCH ROUTE

#### Bảng route đầy đủ

| URL | File trong `app/` | Nhóm layout | Server/Client | Buổi | Ghi chú |
|---|---|---|---|---|---|
| `/` | `(main)/page.tsx` | MainLayout | Server (fetch) | 2, 8 | Trang chủ |
| `/events` | `(main)/events/page.tsx` | MainLayout | Server + Client filter | 3, 8 | Danh sách, tìm kiếm, phân trang |
| `/events/categories` | `(main)/events/categories/page.tsx` | MainLayout | Server | 3 | Nested route (Guided Buổi 3) |
| `/events/search` | `(main)/events/search/page.tsx` | MainLayout | Server + Client | 3 | Nested route (Guided Buổi 3) |
| `/events/[id]` | `(main)/events/[id]/page.tsx` | MainLayout | Server | 4, 8, 11 | `generateMetadata` động |
| `/category/[slug]` | `(main)/category/[slug]/page.tsx` | MainLayout | Server | 4 | `slug`: music, technology, sports, workshop |
| `/checkout/[id]` | `(main)/checkout/[id]/page.tsx` | MainLayout | Server + Client | 4, 6, 8 | Khung `/checkout` tạo ở Buổi 3, chuyển thành route động ở Buổi 4 |
| `/about` | `(main)/about/page.tsx` | MainLayout | Server | 3 | Trang giới thiệu |
| `/user/profile` | `(main)/user/profile/page.tsx` | MainLayout | Client | 3, 9 | Cần đăng nhập |
| `/user/wishlist` | `(main)/user/wishlist/page.tsx` | MainLayout | Client | 9 | Đọc `localStorage` |
| `/login` | `(auth)/login/page.tsx` | AuthLayout | Client (form) | 3, 9 | Đề cương ghi `/auth/login` – xem ghi chú |
| `/register` | `(auth)/register/page.tsx` | AuthLayout | Client (form) | 3, 9 | |
| `/admin/dashboard` | `(admin)/admin/dashboard/page.tsx` | AdminLayout | Server | 3 | |
| `/admin/manage-events` | `(admin)/admin/manage-events/page.tsx` | AdminLayout | Server + Client | 3 | Kế hoạch Buổi 3 gọi là `/admin/events-management` |
| `/admin/create-event` | `(admin)/admin/create-event/page.tsx` | AdminLayout | Client (form) | 9 | Form + Zod `.refine()` |
| `/admin/orders` | `(admin)/admin/orders/page.tsx` | AdminLayout | Client (Table) | 5 | AntD Table, Tag, filter, pagination |
| `/admin/users` | `(admin)/admin/users/page.tsx` | AdminLayout | Server | 3 | |
| `/dev-preview/*` | `dev-preview/…/page.tsx` | – | Server | 2 | Trang tĩnh tạm thời; xóa trước khi deploy Production |
| (URL sai) | `not-found.tsx` | – | Server | 3 | Trang 404 tùy chỉnh |

> 🧭 **Vì sao cần nhóm `(main)`?** Layout cha luôn bọc layout con. Nếu đặt Header/Footer trong `app/layout.tsx`, các trang `(auth)` và `(admin)` cũng sẽ có Header/Footer chính. Vì vậy Root Layout chỉ chứa `<html>`, `<body>` và các provider (AntdRegistry, ConfigProvider); Header/Footer nằm trong `(main)/layout.tsx`; AuthLayout và AdminLayout nằm trong nhóm của riêng chúng. Tên group không xuất hiện trên URL.

> 📝 **Về `/login` và `/auth/login`:** đề cương (Buổi 3) nhắc `/auth/login`, còn kế hoạch chi tiết và tài liệu lý thuyết dùng Route Group `(auth)` cho ra `/login`, `/register`. Đặc tả này chọn `/login`, `/register`. Nhóm nào đã làm `/auth/login` thì giữ nguyên nhưng phải dùng thống nhất cho cả `/auth/register`.

---

## 4. CẤU TRÚC THƯ MỤC DỰ ÁN GỢI Ý

#### Cây thư mục

```text
smart-event-hub/
├── app/
│   ├── layout.tsx               # Root: html, body, AntdRegistry, AntdProvider, metadata gốc
│   ├── not-found.tsx            # 404 tùy chỉnh
│   ├── error.tsx                # 'use client' – lỗi runtime, nút Thử lại
│   ├── global-error.tsx         # Lỗi ở mức Root Layout
│   ├── globals.scss
│   ├── (main)/
│   │   ├── layout.tsx           # Header + Footer
│   │   ├── page.tsx             # /
│   │   ├── loading.tsx
│   │   ├── events/
│   │   │   ├── page.tsx
│   │   │   ├── categories/page.tsx
│   │   │   ├── search/page.tsx
│   │   │   └── [id]/
│   │   │       ├── page.tsx
│   │   │       └── loading.tsx
│   │   ├── category/[slug]/page.tsx
│   │   ├── checkout/[id]/page.tsx
│   │   ├── about/page.tsx
│   │   └── user/
│   │       ├── profile/page.tsx
│   │       └── wishlist/page.tsx
│   ├── (auth)/
│   │   ├── layout.tsx           # AuthLayout: logo + form giữa màn hình
│   │   ├── login/page.tsx
│   │   └── register/page.tsx
│   └── (admin)/
│       └── admin/
│           ├── layout.tsx       # AdminLayout: Sidebar + Header admin
│           ├── loading.tsx      # Skeleton khi chuyển trang admin
│           ├── dashboard/page.tsx
│           ├── manage-events/page.tsx
│           ├── create-event/page.tsx
│           ├── orders/page.tsx
│           └── users/page.tsx
├── components/
│   ├── ui/                      # Atom: Button, Input, Modal, Badge
│   ├── common/                  # Header(NavigationBar), Footer, Sidebar, SearchBar
│   ├── features/                # EventCard, EventFilterBar, TicketQuantitySelector, SeatMatrixPicker, BookingModal, LoginForm
│   └── providers/               # AntdProvider ('use client')
├── hooks/                       # useDebounce, useLocalStorage, useWishlist
├── services/                    # apiClient.ts, eventService.ts, categoryService.ts, orderService.ts, authService.ts
├── schemas/                     # loginSchema, registerSchema, createEventSchema (Zod)
├── types/                       # event.ts, category.ts, order.ts, api.ts, auth.ts
├── styles/                      # _variables.scss, _mixins.scss
├── data/                        # mock-events.json (Buổi 4–7)
├── public/                      # ảnh tĩnh, favicon
├── docs/
│   ├── wireframes/              # Ảnh/link Figma 5 màn hình
│   └── Test_Cases_Scenario.md
├── .env.example
├── .cursorrules
├── next.config.ts
├── tsconfig.json                # "strict": true
└── README.md
```

Đề cương gọi thư mục `components/shared/`; kế hoạch Buổi 4 gọi `components/common/`. Hai tên tương đương, nhóm chọn một và dùng thống nhất.

---

## 5. KIỂU DỮ LIỆU TYPESCRIPT CHÍNH

#### Quy ước

Các kiểu dưới đây là **hợp đồng dữ liệu gợi ý** để nhóm làm mock data từ Buổi 4 và thống nhất tên gọi. Từ Buổi 8, các bạn phải **đối chiếu với response thật trên Swagger** và chỉnh tên trường cho khớp (có thể nhờ AI sinh interface từ JSON rồi review lại). Không dùng `any`; trường có thể vắng mặt thì đánh dấu `?`.

```ts
// types/event.ts
export type EventStatus = 'UPCOMING' | 'ONGOING' | 'ENDED';

export type TicketTierType = 'VVIP' | 'VIP' | 'STANDARD';

export interface TicketTier {
  type: TicketTierType;
  name: string;          // Ví dụ: "Vé VVIP"
  price: number;         // VND
  available: number;     // Số vé còn lại
  maxPerOrder: number;   // Giới hạn mỗi lần đặt
}

export interface Organizer {
  id: string;
  name: string;
  avatarUrl?: string;
  bio?: string;
}

export interface EventItem {
  id: string;
  title: string;
  imageUrl: string;
  startDate: string;     // ISO 8601
  endDate: string;       // ISO 8601
  location: string;
  price: number;         // Giá thấp nhất để hiển thị "Từ … đ"
  status: EventStatus;
  categorySlug: string;
}

export interface EventDetail extends EventItem {
  description: string;
  bannerUrl?: string;
  organizer: Organizer;
  ticketTiers: TicketTier[];
}
```

```ts
// types/category.ts
export type CategorySlug = 'music' | 'technology' | 'sports' | 'workshop';

export interface Category {
  id: string;
  name: string;          // "Âm nhạc", "Công nghệ", "Thể thao", "Workshop"
  slug: CategorySlug;
  icon?: string;
}
```

```ts
// types/order.ts
import type { TicketTierType } from './event';

export type OrderStatus = 'PENDING' | 'SUCCESS' | 'CANCELLED';

export type SeatStatus = 'AVAILABLE' | 'SELECTED' | 'SOLD';

export interface OrderItem {
  tier: TicketTierType;
  quantity: number;
  unitPrice: number;
}

export interface Order {
  id: string;
  eventId: string;
  eventTitle: string;
  customerName: string;
  items: OrderItem[];
  seats?: string[];      // Ví dụ: ['A1', 'A2']
  totalAmount: number;
  status: OrderStatus;
  createdAt: string;
}

export interface CreateOrderPayload {
  eventId: string;
  items: Array<Pick<OrderItem, 'tier' | 'quantity'>>;
  seats?: string[];
  attendDate?: string;
  note?: string;
}
```

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

export interface EventQuery {
  page?: number;
  limit?: number;
  search?: string;
  category?: string;
  sort?: 'latest' | 'price_asc' | 'price_desc';
}
```

```ts
// types/auth.ts
export type UserRole = 'USER' | 'ADMIN';

export interface UserProfile {
  id: string;
  fullName: string;
  email: string;
  role: UserRole;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export interface LoginResult {
  accessToken: string;
  user: UserProfile;
}
```

> 📝 Kế hoạch Buổi 8 dùng tên có tiền tố `I` (`IEvent`, `IEventItem`, `IOrganizer`) và `PaginatedResponse<T>`. Đặc tả này dùng `EventItem`, `Organizer`, `PaginatedData<T>` theo tài liệu lý thuyết. Nhóm chọn một quy ước và áp dụng thống nhất.

---

## 6. API ENDPOINT

#### Nguyên tắc

* **Base URL** lấy từ biến môi trường `NEXT_PUBLIC_API_URL` – giá trị do GV cung cấp. Không viết cứng địa chỉ API trong code.
* Đường dẫn dưới đây là các endpoint được nhắc trong tài liệu học phần. **Tên chính xác, tiền tố phiên bản** (ví dụ `/api/v1/events` như kế hoạch Buổi 8 hay `/api/events` như đề cương) **và cấu trúc response theo Swagger của GV.**

| Phương thức | Đường dẫn | Mô tả | Tham số / Body | Response (gợi ý) | Buổi |
|---|---|---|---|---|---|
| GET | `/api/events` | Danh sách sự kiện, tìm kiếm, phân trang | Query: `page`, `limit`, `search` (có thể thêm `category`, `sort`) | `ApiResponse<PaginatedData<EventItem>>` | 8 |
| GET | `/api/events/{id}` | Chi tiết một sự kiện | Path: `id` | `ApiResponse<EventDetail>`; 404 nếu không có | 8, 11 |
| GET | `/api/categories` | Danh mục sự kiện cho Filter Bar/Dropdown | – | `ApiResponse<Category[]>` | 8 |
| POST | `/api/orders` | Tạo đơn đặt vé | Body: `CreateOrderPayload`; header `Authorization: Bearer <token>` nếu API yêu cầu | `ApiResponse<Order>` | 8 |
| POST | *(endpoint đăng nhập theo Swagger)* | Đăng nhập, nhận JWT | Body: `LoginPayload` | `ApiResponse<LoginResult>` | 9 |

> ⚠️ Tài liệu học phần chỉ ghi "gọi API Login" mà không nêu đường dẫn. Hãy tra Swagger để lấy đúng endpoint đăng nhập (và đăng ký, nếu có) trước Buổi 9.

#### Mẫu service gọi API

```ts
// services/eventService.ts – dùng trong Server Component
import type { ApiResponse, EventQuery, PaginatedData } from '@/types/api';
import type { EventDetail, EventItem } from '@/types/event';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getEvents(query: EventQuery = {}): Promise<PaginatedData<EventItem>> {
  const params = new URLSearchParams();
  Object.entries(query).forEach(([key, value]) => {
    if (value !== undefined && value !== '') params.set(key, String(value));
  });

  const res = await fetch(`${API_URL}/api/events?${params.toString()}`, {
    next: { revalidate: 60 },
  });
  if (!res.ok) throw new Error(`Không tải được danh sách sự kiện (HTTP ${res.status})`);

  const json: ApiResponse<PaginatedData<EventItem>> = await res.json();
  return json.data;
}

export async function getEventById(id: string): Promise<EventDetail | null> {
  const res = await fetch(`${API_URL}/api/events/${encodeURIComponent(id)}`, {
    next: { revalidate: 60 },
  });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`Không tải được sự kiện (HTTP ${res.status})`);

  const json: ApiResponse<EventDetail> = await res.json();
  return json.data;
}
```

```tsx
// app/(main)/events/[id]/page.tsx
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getEventById } from '@/services/eventService';

interface PageProps {
  params: Promise<{ id: string }>;
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { id } = await params;
  const event = await getEventById(id);
  if (!event) return { title: 'Không tìm thấy sự kiện | Smart Event Hub' };

  return {
    title: `${event.title} | Smart Event Hub`,
    description: event.description.slice(0, 150),
    openGraph: {
      title: event.title,
      images: [event.bannerUrl ?? event.imageUrl],
    },
  };
}

export default async function EventDetailPage({ params }: PageProps) {
  const { id } = await params;
  const event = await getEventById(id);
  if (!event) notFound();

  return (
    <main>
      <h1>{event.title}</h1>
      <p>{event.location}</p>
    </main>
  );
}
```

```ts
// services/apiClient.ts – dùng trong Client Component (Axios)
import axios from 'axios';

export const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  timeout: 10000,
});

apiClient.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = window.localStorage.getItem('accessToken');
    if (token) config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

```ts
// services/orderService.ts
import { apiClient } from './apiClient';
import type { ApiResponse } from '@/types/api';
import type { CreateOrderPayload, Order } from '@/types/order';

export async function createOrder(payload: CreateOrderPayload): Promise<Order> {
  const res = await apiClient.post<ApiResponse<Order>>('/api/orders', payload);
  return res.data.data;
}
```

---

## 7. LỘ TRÌNH TÍNH NĂNG THEO BUỔI

#### Bảng Buổi → Tính năng → Deliverable

| Buổi | Tính năng xây dựng | Deliverable của nhóm |
|---|---|---|
| 1 | Repo, branch `main`/`dev`/`feature/*`; Design Token SCSS; `types/event.ts`; EventCard, HeaderNavigationBar | Repo + PR đầu tiên được merge; Footer, EventCategoryBadge, SearchBar (BTVN) |
| 2 | Wireframe 5 màn hình; chuyển wireframe sang TSX bằng v0.dev/Claude; EventDetailPageView | `docs/wireframes/`; trang `/dev-preview/*` |
| 3 | App Router, `(main)`, `(auth)`, `(admin)`; nested route; `loading.tsx`, `not-found.tsx` | Sơ đồ routing đầy đủ; 404 tùy chỉnh; `error.tsx`, `global-error.tsx` |
| 4 | `/events/[id]`, `/category/[slug]`; Button đa biến thể; `data/mock-events.json`; luồng Trang chủ → Danh mục → Chi tiết → Đặt vé | User Flow liên tục với mock data; thư mục `components/ui`, `common`, `features` |
| 5 | AntD + `AntdRegistry` + Theme; BookingModal; `/admin/orders`; refactor 5 màn hình sang AntD + SCSS | Giao diện đồng bộ, responsive Tablet/Mobile |
| 6 | TicketQuantitySelector (VVIP/VIP/Standard), EventFilterBar + debounce, SeatMatrixPicker 5×8 (tối đa 6 ghế) | Ứng dụng tích hợp 50%, slide giữa kỳ |
| 7 | `npm run build` sạch, README chuẩn, cross-review | **Báo cáo giữa kỳ**: Wireframe, repo, demo giao diện |
| 8 | `services/`, `getEvents`, `getEventById`, `GET /api/categories`, `POST /api/orders`, Spin/Skeleton | Mock JSON được thay bằng API thật; xử lý Network Error/500 |
| 9 | LoginForm + Zod, lưu token; `/admin/create-event` + `.refine()`; Wishlist + `/user/wishlist` | Form validation chuẩn; Wishlist giữ được sau F5; tài khoản Vercel sẵn sàng |
| 10 | Responsive 375/768/1440px; Drawer/Collapse trên mobile; refactor DRY; Zero Console Warnings | Biên bản nghiệm thu PBL 1; Test Cases Scenario |
| 11 | Metadata tĩnh + `generateMetadata`; `next/image`, `next/font`, `next/dynamic`; deploy Vercel + `NEXT_PUBLIC_API_URL`; Lighthouse | Link Vercel Live; Lighthouse Performance > 85, SEO > 90; báo cáo Word/PDF + slide |
| 12 | Hoàn thiện, demo live, Cross-Testing | **Final Showcase**: thuyết trình 8', Q&A 5' |

---

## 8. DEFINITION OF DONE (ĐIỀU KIỆN HOÀN THÀNH)

#### Một tính năng (một PR) được coi là xong khi

* [ ] Đáp ứng đúng yêu cầu và output của bài tập/tính năng tương ứng.
* [ ] TypeScript strict, không có `any`; props, dữ liệu API có kiểu rõ ràng trong `types/`.
* [ ] `npm run lint` và `npm run build` chạy thành công.
* [ ] Hiển thị đúng ở Mobile 375px, Tablet 768px, Desktop 1440px; không tràn ngang.
* [ ] Có trạng thái loading và thông báo lỗi khi gọi API (từ Buổi 8).
* [ ] Không còn `console.log`, code chết, inline-style rác; dùng biến/mixin chung.
* [ ] Commit theo Conventional Commits; PR vào `dev` có mô tả, mục "Phần có dùng AI", ảnh chụp UI.
* [ ] Được ít nhất 1 thành viên khác review và approve.
* [ ] Tác giả giải thích được toàn bộ code trong PR.

#### Mốc giữa kỳ (Buổi 7) được coi là đạt khi

* [ ] Wireframe đủ 5 màn hình trong `docs/wireframes/` và link Figma.
* [ ] Routing đầy đủ, điều hướng bằng `next/link` không reload trang; có 404.
* [ ] Giao diện dùng AntD + SCSS custom, responsive; Console không còn lỗi Hydration.
* [ ] `main` build thành công; README có mô tả, phân công, hướng dẫn cài đặt, cấu trúc thư mục.
* [ ] Git log cho thấy mọi thành viên đều có commit tính năng.

#### Mốc cuối kỳ (Buổi 12) được coi là đạt khi

* [ ] Toàn bộ dữ liệu lấy từ API thật; đặt vé gửi được `POST /api/orders`.
* [ ] Đăng nhập với Zod validation; Wishlist bằng `localStorage` an toàn với SSR.
* [ ] Deploy Vercel từ `main`, biến môi trường cấu hình đúng; trang `/dev-preview/*` đã gỡ.
* [ ] SEO Metadata động cho `/events/[id]`; Lighthouse Performance > 85, SEO > 90.
* [ ] Có Test Cases Scenario, báo cáo Word/PDF và slide theo mẫu.

---

## 9. MÔI TRƯỜNG & CẤU HÌNH

#### Biến môi trường

| Biến | Ý nghĩa | Nơi khai báo |
|---|---|---|
| `NEXT_PUBLIC_API_URL` | Base URL của Backend API (Swagger) do GV cung cấp | `.env.local` (máy cá nhân); Vercel *Project Settings → Environment Variables* cho Development, Preview, Production |

```bash
# .env.example – commit file này lên repo, KHÔNG chứa giá trị thật
NEXT_PUBLIC_API_URL=

# .env.local – mỗi thành viên tự tạo, đã nằm trong .gitignore
NEXT_PUBLIC_API_URL=<địa chỉ API do giảng viên cung cấp>
```

* Biến có tiền tố `NEXT_PUBLIC_` được nhúng vào mã gửi xuống trình duyệt. Chỉ đặt giá trị công khai (như địa chỉ API); không bao giờ đặt khóa bí mật vào biến này.
* Sau khi thêm hoặc đổi biến môi trường trên Vercel, phải **Redeploy** để giá trị mới có hiệu lực.
* Kiểm tra `.gitignore` có `.env*.local` trước lần commit đầu tiên.

#### Môi trường phát triển

| Thành phần | Yêu cầu |
|---|---|
| Node.js | Bản LTS hiện hành |
| Next.js | 15, App Router |
| TypeScript | `"strict": true` trong `tsconfig.json` |
| Thư viện | `sass`, `antd`, `@ant-design/nextjs-registry`, `axios`, `react-hook-form`, `zod`, `@hookform/resolvers` |
| Lệnh | `npm run dev` (phát triển) · `npm run lint` · `npm run build` (bắt buộc trước khi merge vào `main`) |
| Triển khai | Vercel kết nối GitHub, tự deploy khi push lên `main`; mỗi PR có Preview Deployment |

> 🔒 **Tài khoản thử nghiệm API** (nếu Backend yêu cầu đăng nhập) do GV cấp riêng qua LMS. Không ghi tài khoản/mật khẩu vào README hay commit lên repo công khai.
