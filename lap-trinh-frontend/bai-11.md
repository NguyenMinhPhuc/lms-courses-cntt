# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 6: DỰ ÁN THỰC TẾ – TỐI ƯU & TRIỂN KHAI
### Bài 11: PBL 2 – CI/CD, Deploy Vercel, SEO & Performance

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Học theo dự án (PBL 2) – Giảng viên làm Mentor · **Chuẩn đầu ra:** PI 5.1 (CLO4)
> **Dự án xuyên suốt:** Smart Event Hub – triển khai lên Vercel, tối ưu SEO Metadata và đạt Lighthouse Performance > 85

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Giải thích được quy trình CI/CD trên Vercel, vai trò của biến môi trường theo từng môi trường (Development, Preview, Production) và các chỉ số Lighthouse.
> * **[Bloom 3/4 - Kỹ năng]:** Cấu hình Metadata tĩnh, `generateMetadata` động cho `/events/[id]` (Next.js 15), thay `<img>` bằng `next/image`, tối ưu font với `next/font` và lazy load bằng `next/dynamic`.
> * **[Bloom 5/6 - Năng lực]:** Deploy thành công Smart Event Hub lên domain Vercel thật, tự chẩn đoán lỗi Build Fail và đánh giá – cải thiện điểm Lighthouse (Performance > 85, SEO > 90).

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Một thành viên gửi link sự kiện "Workshop Next.js 15" của nhóm vào group Zalo lớp. Thay vì ảnh banner và tên sự kiện, bản xem trước chỉ hiện chữ "Create Next App" cùng một ô trống. Tệ hơn, link đó lại là `localhost:3000`, nên không ai ngoài máy bạn mở được. Sản phẩm làm suốt 10 buổi gần như "vô hình" với người dùng thật.

Hôm nay chúng ta đưa Smart Event Hub lên Internet. **Làm sao để mỗi lần `git push` là web tự cập nhật, link chia sẻ hiện đúng ảnh và tiêu đề sự kiện, và trang tải đủ nhanh để Lighthouse chấm điểm xanh?** Ba câu hỏi này tương ứng với ba phần PBL của buổi học.

> 🧭 **Trước giờ học (Flipped Classroom):** Đọc *Next.js Metadata Documentation* và *Google Lighthouse Audit Guide* (link ở mục 5). Đăng nhập Vercel bằng tài khoản GitHub, kiểm tra repo nhóm đã công khai ở branch `main`. Chạy thử `npm run build` trên máy để phát hiện lỗi sớm. Mang theo file `Test_Cases_Scenario` từ Bài 10. Làm quiz nhanh trên LMS.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. CI/CD với Vercel & quản trị biến môi trường

* **Khái niệm:** **CI/CD** (Continuous Integration / Continuous Deployment) là quy trình tự động Build – kiểm tra – Deploy mỗi khi code thay đổi. Vercel kết nối trực tiếp với GitHub: mỗi lượt `git push` lên `main` kích hoạt một bản Production mới.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Các bước: Vercel Dashboard → *Add New Project* → chọn repo → Vercel tự nhận diện Next.js → khai báo Environment Variables → *Deploy*.
  * Biến môi trường được quản lý trong Project Settings theo 3 môi trường: **Development**, **Preview** (các branch/PR khác `main`), **Production**.
  * Biến có tiền tố `NEXT_PUBLIC_` được **gắn cứng vào bundle lúc build** và lộ ra trình duyệt. Không đặt API Key bí mật vào biến này. Đổi giá trị trên Vercel xong phải **Redeploy** mới có hiệu lực.
  * File `.env.local`, `.env.production` chứa giá trị thật không được commit; chỉ commit `.env.example`.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Nhóm B deploy thành công nhưng trang chủ trống trơn. Console báo gọi `undefined/api/events`. Nguyên nhân: quên khai báo `NEXT_PUBLIC_API_URL` trên Vercel. Thêm biến, bấm Redeploy, dữ liệu hiện lại.

```bash
# .env.example (commit file này, KHÔNG commit .env.local)
NEXT_PUBLIC_API_URL=https://your-backend.example.com
NEXT_PUBLIC_SITE_URL=https://smart-event-hub.vercel.app
```

```ts
// lib/config.ts – báo lỗi rõ ràng thay vì gọi "undefined/api/..."
const API_URL = process.env.NEXT_PUBLIC_API_URL;

if (!API_URL) {
  throw new Error('Thiếu biến môi trường NEXT_PUBLIC_API_URL');
}

export const config = {
  apiUrl: API_URL,
  siteUrl: process.env.NEXT_PUBLIC_SITE_URL ?? 'http://localhost:3000',
} as const;
```

```bash
# Quy trình an toàn trước khi push lên main
npm run build                 # build y hệt Vercel: type-check + lint + build
git add .
git commit -m "feat(seo): thêm generateMetadata cho trang chi tiết sự kiện"
git push origin main          # Vercel tự động Build & Deploy
```

> **Lỗi Build Fail hay gặp trên Vercel:** lỗi TypeScript/ESLint mà dev mode bỏ qua; import sai hoa/thường (`EventCard` vs `eventCard`) vì Windows không phân biệt nhưng Linux của Vercel thì có; thiếu biến môi trường; dùng `window`/`localStorage` trong Server Component.

#### 2.2. SEO với Metadata API – Metadata tĩnh cho Root Layout

* **Khái niệm:** **Metadata API** của App Router sinh các thẻ `<title>`, `<meta name="description">`, OpenGraph… từ object `metadata` export trong `layout.tsx` hoặc `page.tsx`, không cần tự viết thẻ `<head>`.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `metadataBase` giúp các URL ảnh tương đối (`/og-default.png`) được chuyển thành URL tuyệt đối khi chia sẻ.
  * `title.template` tạo tiêu đề thống nhất: trang con chỉ cần khai báo `title: 'Đặt vé'`, kết quả là "Đặt vé | Smart Event Hub".
  * Quy ước file: `app/favicon.ico`, `app/opengraph-image.png`, `app/sitemap.ts`, `app/robots.ts` được Next.js tự nhận diện.
  * `next/font` tự host font, tránh nghẽn tải và giảm Layout Shift do đổi font.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Khi dán link trang chủ vào Facebook/Zalo, bản xem trước hiển thị tên "Smart Event Hub", mô tả ngắn và ảnh `og-default.png` thay cho "Create Next App".

```tsx
// app/layout.tsx
import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import { Be_Vietnam_Pro } from 'next/font/google';
import './globals.scss';

const beVietnam = Be_Vietnam_Pro({
  subsets: ['latin', 'vietnamese'],
  weight: ['400', '600', '700'],
  display: 'swap',
});

export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL ?? 'http://localhost:3000'),
  title: {
    default: 'Smart Event Hub – Đặt vé sự kiện trực tuyến',
    template: '%s | Smart Event Hub',
  },
  description: 'Khám phá và đặt vé hội thảo, concert, workshop nhanh chóng trên Smart Event Hub.',
  keywords: ['đặt vé', 'sự kiện', 'workshop', 'concert', 'Smart Event Hub'],
  openGraph: {
    type: 'website',
    locale: 'vi_VN',
    siteName: 'Smart Event Hub',
    images: ['/og-default.png'],
  },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="vi">
      <body className={beVietnam.className}>{children}</body>
    </html>
  );
}
```

```ts
// app/robots.ts
import type { MetadataRoute } from 'next';

export default function robots(): MetadataRoute.Robots {
  const baseUrl = process.env.NEXT_PUBLIC_SITE_URL ?? 'http://localhost:3000';
  return {
    rules: { userAgent: '*', allow: '/', disallow: '/admin/' },
    sitemap: `${baseUrl}/sitemap.xml`,
  };
}
```

```ts
// app/sitemap.ts
import type { MetadataRoute } from 'next';

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = process.env.NEXT_PUBLIC_SITE_URL ?? 'http://localhost:3000';
  return ['', '/events', '/about'].map((path) => ({
    url: `${baseUrl}${path}`,
    lastModified: new Date(),
  }));
}
```

#### 2.3. Metadata động với `generateMetadata` (Next.js 15)

* **Khái niệm:** Với Dynamic Route `/events/[id]`, mỗi sự kiện cần tiêu đề và ảnh OpenGraph riêng. Hàm `generateMetadata` chạy trên server, gọi API rồi trả về object `Metadata`.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Từ Next.js 15, `params` là `Promise`.** Phải viết `const { id } = await params;`. Ví dụ cũ dạng `params.id` sẽ báo lỗi type và cảnh báo khi chạy.
  * Bọc hàm lấy dữ liệu bằng `cache()` của React để `generateMetadata` và component trang dùng chung một kết quả, không gọi API hai lần.
  * Luôn có **fallback metadata** khi không tìm thấy sự kiện; trang thì gọi `notFound()` để hiện 404.
  * Ảnh chính (LCP) của trang dùng `next/image` với `priority` và `sizes` phù hợp.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Link `smart-event-hub.vercel.app/events/12` khi chia sẻ lên Zalo hiển thị đúng banner và tên "Workshop Next.js 15 | Smart Event Hub". Link sự kiện đã bị xóa hiển thị "Không tìm thấy sự kiện" thay vì lỗi trắng trang.

```ts
// lib/events.ts
import { cache } from 'react';

export interface EventItem {
  id: string;
  title: string;
  description: string;
  bannerUrl: string;
  startDate: string;
  price: number;
  status: 'UPCOMING' | 'ONGOING' | 'ENDED';
}

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export const getEventById = cache(async (id: string): Promise<EventItem | null> => {
  try {
    const res = await fetch(`${API_URL}/api/events/${id}`, { next: { revalidate: 60 } });
    if (!res.ok) return null;
    return (await res.json()) as EventItem;
  } catch {
    return null;
  }
});
```

```tsx
// app/events/[id]/page.tsx
import type { Metadata } from 'next';
import Image from 'next/image';
import { notFound } from 'next/navigation';
import { getEventById } from '@/lib/events';

type Props = {
  params: Promise<{ id: string }>;
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;
  const event = await getEventById(id);

  if (!event) {
    return {
      title: 'Không tìm thấy sự kiện',
      description: 'Sự kiện không tồn tại hoặc đã bị gỡ khỏi Smart Event Hub.',
    };
  }

  return {
    title: event.title,
    description: event.description,
    openGraph: {
      title: event.title,
      description: event.description,
      images: [{ url: event.bannerUrl, alt: event.title }],
    },
  };
}

export default async function EventDetailPage({ params }: Props) {
  const { id } = await params;
  const event = await getEventById(id);
  if (!event) notFound();

  return (
    <article>
      <Image
        src={event.bannerUrl}
        alt={event.title}
        width={1200}
        height={630}
        priority
        sizes="(max-width: 768px) 100vw, 1200px"
        style={{ width: '100%', height: 'auto' }}
      />
      <h1>{event.title}</h1>
      <p>{event.description}</p>
    </article>
  );
}
```

#### 2.4. Performance: `next/image`, `next/dynamic` & Lighthouse

* **Khái niệm:** **Google Lighthouse** (trong Chrome DevTools) chấm 4 nhóm chỉ số: **Performance, Accessibility, Best Practices, SEO**. Mục tiêu của buổi: Performance > 85, SEO > 90.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `next/image` tự resize theo thiết bị, lazy load ảnh ngoài màn hình, chuyển sang WebP (thêm AVIF qua `images.formats`). Thuộc tính `width`/`height` giữ chỗ trước nên trang không bị nhảy bố cục (**CLS – Cumulative Layout Shift**).
  * Ảnh từ domain backend phải khai báo trong `images.remotePatterns`, nếu không `next/image` báo lỗi.
  * Component nặng (sơ đồ chọn ghế, biểu đồ Admin) nên lazy load bằng `next/dynamic`. Tùy chọn `ssr: false` chỉ dùng được trong Client Component.
  * Chạy Lighthouse trên **link Vercel Live** trong cửa sổ ẩn danh để extension không làm sai kết quả.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Trang chi tiết sự kiện tải ngay cả component Seat Picker dù người dùng chưa bấm "Chọn ghế". Chuyển sang `dynamic()` kèm `Skeleton`, phần JavaScript tải ban đầu nhỏ lại và điểm Performance tăng rõ.

```ts
// next.config.ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  images: {
    formats: ['image/avif', 'image/webp'],
    remotePatterns: [
      // Thay bằng domain backend thật của lớp
      { protocol: 'https', hostname: 'your-backend.example.com', pathname: '/uploads/**' },
    ],
  },
};

export default nextConfig;
```

```tsx
// components/booking/SeatPickerLazy.tsx
'use client';

import dynamic from 'next/dynamic';
import { Skeleton } from 'antd';

const SeatPicker = dynamic(() => import('./SeatPicker'), {
  ssr: false,
  loading: () => <Skeleton active paragraph={{ rows: 6 }} />,
});

export default function SeatPickerLazy({ eventId }: { eventId: string }) {
  return <SeatPicker eventId={eventId} />;
}
```

| Vấn đề Lighthouse báo | Hướng xử lý trong Smart Event Hub |
|---|---|
| Ảnh quá lớn, sai định dạng | Thay `<img>` bằng `next/image`, đặt `sizes` đúng |
| LCP chậm (banner tải muộn) | Thêm `priority` cho ảnh banner đầu trang |
| Layout Shift (CLS) | Khai báo `width`/`height`, dùng `next/font`, giữ chỗ bằng Skeleton |
| JavaScript ban đầu nặng | Lazy load component nặng bằng `next/dynamic` |
| SEO thiếu description/title | Bổ sung `metadata` và `generateMetadata` |

#### 2.5. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

```text
Hướng dẫn tôi cách viết hàm `generateMetadata` trong Next.js App Router cho trang Dynamic Route `/events/[id]/page.tsx`.
Yêu cầu:
1. Gọi API `getEventById(id)` lấy thông tin sự kiện.
2. Trả về object Metadata gồm: `title`, `description`, `openGraph` (title, description, images chứa URL ảnh sự kiện).
3. Xử lý trường hợp không tìm thấy sự kiện thì trả về fallback metadata tiêu chuẩn.
Lưu ý: dự án dùng Next.js 15, `params` là Promise.
```

```text
Tôi gặp lỗi Build Error trên Vercel khi Deploy dự án Next.js TypeScript:
[Dán đoạn log lỗi Vercel Build Error vào đây]

Hãy phân tích nguyên nhân lỗi và hướng dẫn từng bước cách sửa lỗi trên tệp mã nguồn hoặc cấu hình Vercel Settings.
```

**Checklist kiểm duyệt code AI:**

* **Phiên bản Next.js:** AI hay sinh `params.id` theo kiểu Next.js 14. Bắt buộc sửa thành `const { id } = await params;`.
* **Bảo mật:** Không có secret nào nằm trong biến `NEXT_PUBLIC_`; không commit `.env.local`.
* **Fallback:** `generateMetadata` có xử lý sự kiện không tồn tại; trang gọi `notFound()`.
* **Ảnh:** Mọi `<img>` đã đổi sang `Image`; domain ảnh có trong `remotePatterns`; chỉ ảnh đầu trang dùng `priority`.
* **Kiểm chứng:** `npm run build` pass trên máy trước khi push; chạy lại Lighthouse sau mỗi lần sửa để xác nhận điểm thực sự tăng.

> **Đừng tin "điểm tưởng tượng":** AI có thể nói "sau khi sửa, điểm sẽ đạt 95". Con số duy nhất được ghi vào báo cáo là kết quả Lighthouse nhóm tự chạy trên link Vercel Live.

#### 2.6. Thực hành trên lớp

Buổi PBL 2 do Giảng viên mentor trực tiếp. Kết thúc buổi, mỗi nhóm phải có link Live hoạt động.

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Lý thuyết & Thao tác mẫu | 30' | GV demo CI/CD Vercel, Environment Variables, Metadata API, `next/image`, `next/font`, `next/dynamic` | Nhóm nắm quy trình deploy và checklist SEO |
| PBL Phần 1 – SEO & Metadata động | 60' | Metadata tĩnh cho Root Layout; `generateMetadata` cho `/events/[id]`; thay toàn bộ `<img>` bằng `Image` | Link chia sẻ Zalo/Facebook hiện đúng ảnh và tiêu đề; ảnh tối ưu WebP/AVIF |
| PBL Phần 2 – Deploy Vercel & biến môi trường | 60' | Push `main`, kết nối repo với Vercel, khai báo `NEXT_PUBLIC_API_URL`, xử lý Build Fail | Domain dạng `smart-event-hub.vercel.app` chạy ổn định; API, LocalStorage hoạt động trên Live |
| PBL Phần 3 – Audit Lighthouse | 60' | Chạy Lighthouse trên link Live, phân tích 4 chỉ số, dùng Vibe Coding sửa code | Performance > 85, SEO > 90 |
| Tổng kết | 15' | Tổng hợp link Live Web App của toàn bộ các nhóm, giao BTVN | Danh sách link Vercel của cả lớp |

* **PBL Phần 1:** Bắt đầu từ `app/layout.tsx`, sau đó đến `app/events/[id]/page.tsx`. Kiểm tra thẻ meta bằng View Page Source; sau khi deploy, dán link vào Zalo/Facebook để xem bản xem trước.
* **PBL Phần 2:** Chạy `npm run build` trên máy trước. Nếu Vercel báo lỗi, copy log và dùng prompt "Build Error" ở mục 2.5, nhưng phải hiểu nguyên nhân trước khi sửa.
* **PBL Phần 3:** Chụp ảnh kết quả Lighthouse **trước** và **sau** tối ưu để đưa vào báo cáo cuối kỳ. Chạy thêm kịch bản `Test_Cases_Scenario` trên link Live.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)

* 🔹 **CI/CD Vercel:** Kết nối GitHub một lần, sau đó mỗi `git push` lên `main` tự động Build và Deploy; branch khác tạo bản Preview.
* 🔹 **Biến môi trường:** Khai báo theo Development/Preview/Production; `NEXT_PUBLIC_` lộ ra trình duyệt và chỉ cập nhật sau khi Redeploy.
* 🔹 **Metadata API:** `metadata` tĩnh cho layout, `generateMetadata` cho trang động; Next.js 15 dùng `const { id } = await params;`.
* 🔹 **Performance:** `next/image` (resize, lazy load, WebP/AVIF, chống CLS), `next/font`, `next/dynamic` cho component nặng.
* 🔹 **Lighthouse là thước đo cuối:** Mục tiêu Performance > 85, SEO > 90, đo trên link Vercel Live chứ không phải localhost.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Trong Next.js 15, cách lấy `id` đúng bên trong `generateMetadata({ params })` là gì?
- A. `const id = params.id;`
- B. `const { id } = useParams();`
- C. `const { id } = await params;`
- D. `const id = router.query.id;`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Từ Next.js 15, <code>params</code> là Promise nên phải <code>await</code>. <code>useParams</code> là hook của Client Component, còn <code>router.query</code> thuộc Pages Router cũ.
</details>

**Câu 2:** Nhóm đã sửa giá trị `NEXT_PUBLIC_API_URL` trên Vercel nhưng web vẫn gọi URL cũ. Nguyên nhân hợp lý nhất?
- A. Biến `NEXT_PUBLIC_` được gắn vào bundle lúc build, cần Redeploy
- B. Vercel không hỗ trợ biến môi trường cho Next.js
- C. Phải đổi tên biến thành `API_URL`
- D. Trình duyệt chặn biến môi trường từ Vercel

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> Giá trị biến công khai được thay thế trực tiếp vào code khi build, nên đổi giá trị phải build lại (Redeploy) mới có hiệu lực.
</details>

**Câu 3:** Vì sao dùng `Image` của `next/image` giúp cải thiện điểm Lighthouse Performance?
- A. Vì nó tải toàn bộ ảnh ngay khi mở trang
- B. Vì nó tự resize, lazy load, đổi sang WebP/AVIF và giữ chỗ chống Layout Shift
- C. Vì nó chuyển ảnh thành chuỗi Base64 trong HTML
- D. Vì nó tắt ảnh trên thiết bị di động

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Ảnh nhỏ hơn, đúng kích thước thiết bị và chỉ tải khi cần giúp tăng tốc; <code>width</code>/<code>height</code> giữ chỗ trước nên giảm CLS.
</details>

**Câu 4:** Build trên máy Windows chạy tốt nhưng Vercel báo `Module not found: Can't resolve './eventCard'`, trong khi file thật tên `EventCard.tsx`. Nên sửa thế nào?
- A. Tắt TypeScript trong `tsconfig.json`
- B. Xóa thư mục `.next` trên máy rồi push lại
- C. Chuyển dự án sang Pages Router
- D. Sửa đường dẫn import cho đúng hoa/thường như tên file

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> Môi trường build Linux của Vercel phân biệt chữ hoa/thường, còn Windows thì không. Import phải khớp chính xác tên file.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-11-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)

* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Đăng ảnh Lighthouse trước và sau tối ưu của nhóm bạn. Thay đổi nào giúp tăng điểm nhiều nhất? Có gợi ý nào của AI làm điểm **giảm** hoặc không đổi không? Hãy giải thích vì sao.
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Viết **Báo cáo Văn bản** (Word/PDF) hoàn chỉnh theo mẫu quy định: mô tả kiến trúc dự án, sơ đồ Wireframe, mô tả API tích hợp, phân công công việc, ảnh chụp minh chứng Git commit và Link Vercel Live.
  * Chuẩn bị **Slide thuyết trình** chuyên nghiệp cho Bài 12 – Thi Hackathon & Final Showcase.
  * **Output:** file `BaoCao_SmartEventHub_<TenNhom>.pdf` (hoặc `.docx`) và slide sẵn sàng cho buổi bảo vệ cuối kỳ.
  * **Hạn nộp:** trước buổi học tiếp theo. Nộp file trên LMS, đồng thời đưa báo cáo vào thư mục `docs/` qua PR `docs/final-report`.
* **📚 Tài liệu đọc & tham khảo:**
  * Next.js Metadata Documentation: https://nextjs.org/docs/app/building-your-application/optimizing/metadata
  * Next.js – generateMetadata: https://nextjs.org/docs/app/api-reference/functions/generate-metadata
  * Next.js – Image Component: https://nextjs.org/docs/app/api-reference/components/image
  * Vercel – Environment Variables: https://vercel.com/docs/projects/environment-variables
  * Google Lighthouse Audit Guide: https://developer.chrome.com/docs/lighthouse/overview/
