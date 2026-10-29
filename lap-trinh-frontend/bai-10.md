# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 6: DỰ ÁN THỰC TẾ – TỐI ƯU & TRIỂN KHAI
### Bài 10: PBL 1 – Refactoring, Optimization & Responsive Polish

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Học theo dự án (PBL 1) – Giảng viên làm Mentor · **Chuẩn đầu ra:** PI 2.3 (CLO2), PI 5.1 (CLO4)
> **Dự án xuyên suốt:** Smart Event Hub – tối ưu UI/UX toàn bộ dự án, làm sạch codebase và Responsive Polish trên 3 kích thước màn hình

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Nhận diện được các Code Smell phổ biến trong component React (trùng lặp, component quá lớn, lạm dụng `any`, biến thừa) và giải thích được quy chuẩn Responsive 375px – 768px – 1440px.
> * **[Bloom 3/4 - Kỹ năng]:** Áp dụng Vibe Code Refactoring để phân rã component, thay `any` bằng Interface, dùng SCSS Mixin, `Drawer`/Grid của Ant Design để sửa lỗi tràn khung trên di động.
> * **[Bloom 5/6 - Năng lực]:** Đánh giá chất lượng code do AI đề xuất, đưa dự án về trạng thái TypeScript strict pass 100%, Zero Console Warnings và được Giảng viên nghiệm thu tiến độ PBL 1.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Sau 9 buổi, Smart Event Hub của các nhóm đã có đủ routing, giao diện Ant Design, kết nối API và form đặt vé. Thử mở trang chủ trên điện thoại 375px: thanh lọc sự kiện tràn ra ngoài, xuất hiện thanh cuộn ngang, nút "Đặt vé" bé đến mức khó bấm. Mở DevTools thì Console đỏ rực với `Hydration failed`, còn trong code có ba bốn file `EventCard` gần như giống hệt nhau do mỗi thành viên tự sinh bằng AI.

Một sản phẩm "chạy được" chưa phải là sản phẩm có thể đưa cho người dùng thật. **Nếu ngày mai nhóm phải deploy lên Internet, các bạn sẽ sửa lỗi nào trước, và làm sao chứng minh việc refactor không làm hỏng giao diện cũ?** Buổi PBL hôm nay dành trọn cho câu hỏi đó.

> 🧭 **Trước giờ học (Flipped Classroom):** Đọc *Refactoring Guru – Code Smells* và *Google Responsive Web Design Basics* (link ở mục 5). Tự rà soát repo nhóm, liệt kê ít nhất 5 Code Smell và 3 lỗi responsive. Làm quiz nhanh trên LMS. Mang laptop đã chạy được `npm run dev` của dự án.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Code Smell & kỹ thuật Vibe Code Refactoring

* **Khái niệm:** **Code Smell** là dấu hiệu bề mặt cho thấy code khó đọc, khó bảo trì, dù chương trình vẫn chạy. **Refactoring** là cải tổ cấu trúc code mà **không thay đổi hành vi** giao diện và logic.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Các dấu hiệu cần refactor gấp: đoạn JSX/SCSS lặp lại (vi phạm DRY), component dài hơn 300 dòng, khai báo `any` tràn lan, unused imports/variables, `console.log` còn sót.
  * Quy trình Vibe Code Refactoring: dán đoạn code vào Cursor/Copilot, yêu cầu AI phân rã thành sub-component, thay `any` bằng Interface, dùng `React.memo`/`useCallback` khi có lý do re-render rõ ràng.
  * Mục tiêu buổi học: rút gọn codebase **trên 20% số dòng** mà giao diện không đổi.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Nhóm A có `EventList` dùng `any[]`, render thẻ card bằng JSX thô và gọi `alert()` khi đặt vé. Sau refactor, card được tách thành `EventCard` dùng chung cho Home, Category và Wishlist; handler đặt vé được giữ ổn định bằng `useCallback`.

```tsx
// ❌ TRƯỚC: any, console.log, JSX lặp lại ở nhiều trang
export default function EventList({ events }: { events: any[] }) {
  console.log(events);
  return (
    <div>
      {events.map((e) => (
        <div key={e.id} className="card">
          <img src={e.bannerUrl} />
          <h3>{e.title}</h3>
          <p>{e.price.toLocaleString('vi-VN')} đ</p>
          <button onClick={() => alert('Đặt vé ' + e.id)}>Đặt vé</button>
        </div>
      ))}
    </div>
  );
}
```

```tsx
// ✅ SAU: types/event.ts
export interface EventItem {
  id: string;
  title: string;
  startDate: string;
  price: number;
  bannerUrl: string;
  status: 'UPCOMING' | 'ONGOING' | 'ENDED';
}
```

```tsx
// ✅ SAU: components/shared/EventCard.tsx
'use client';

import { memo } from 'react';
import Image from 'next/image';
import { Button, Card } from 'antd';
import type { EventItem } from '@/types/event';

interface EventCardProps {
  event: EventItem;
  onBook: (id: string) => void;
}

const formatPrice = (value: number): string =>
  value === 0 ? 'Miễn phí' : `${value.toLocaleString('vi-VN')} đ`;

function EventCardBase({ event, onBook }: EventCardProps) {
  return (
    <Card
      cover={
        // Ảnh từ domain ngoài cần khai báo images.remotePatterns (xem Bài 11)
        <Image src={event.bannerUrl} alt={event.title} width={400} height={225} />
      }
      actions={[
        <Button key="book" type="primary" onClick={() => onBook(event.id)}>
          Đặt vé
        </Button>,
      ]}
    >
      <Card.Meta title={event.title} description={formatPrice(event.price)} />
    </Card>
  );
}

export const EventCard = memo(EventCardBase);
```

```tsx
// ✅ SAU: components/shared/EventList.tsx
'use client';

import { useCallback } from 'react';
import { useRouter } from 'next/navigation';
import { Col, Row } from 'antd';
import type { EventItem } from '@/types/event';
import { EventCard } from './EventCard';

export default function EventList({ events }: { events: EventItem[] }) {
  const router = useRouter();
  const handleBook = useCallback(
    (id: string) => router.push(`/checkout/${id}`),
    [router],
  );

  return (
    <Row gutter={[16, 16]}>
      {events.map((event) => (
        <Col key={event.id} xs={24} sm={12} lg={8}>
          <EventCard event={event} onBook={handleBook} />
        </Col>
      ))}
    </Row>
  );
}
```

> **Lưu ý:** `memo` chỉ có tác dụng khi props giữ nguyên tham chiếu. Nếu truyền `onBook={(id) => ...}` viết trực tiếp trong JSX, mỗi lần render cha lại tạo hàm mới và `memo` trở nên vô ích.

#### 2.2. Làm sạch TypeScript strict & dọn Console

* **Khái niệm:** Trạng thái "sạch" của buổi PBL 1 gồm: **TypeScript strict mode pass 100%** không warning, không còn `any`, không còn biến thừa và `console.log` dư thừa.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Bật `"strict": true` trong `tsconfig.json`, chạy `tsc --noEmit` để thấy toàn bộ lỗi type mà không cần build.
  * Khi chưa biết kiểu dữ liệu, dùng `unknown` rồi thu hẹp kiểu (type narrowing) thay vì `any`.
  * ESLint báo unused imports/variables; xóa hẳn chứ không comment lại.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Hàm đọc wishlist từ LocalStorage trả về `JSON.parse(raw)` có kiểu `any`. Đổi sang `unknown` buộc nhóm kiểm tra `Array.isArray()` trước khi dùng, tránh crash khi dữ liệu bị sửa tay trong DevTools.

```bash
# Kiểm tra type toàn dự án, không sinh file build
npx tsc --noEmit

# Kiểm tra lint (unused vars, hooks deps...)
npm run lint

# Tìm nhanh any và console.log còn sót
git grep -n -E ": any|as any|console\.log" -- "*.ts" "*.tsx"
```

#### 2.3. Quy chuẩn Responsive Breakpoint & sửa Horizontal Overflow

* **Khái niệm:** Mọi trang phải hiển thị mượt trên 3 kích thước tiêu chuẩn: **Mobile 375px** (iPhone SE/12), **Tablet 768px** (iPad), **Desktop 1440px**.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Danh sách trang phải kiểm tra 100%: Home, Listing, Event Detail, Booking Modal, Admin Orders.
  * Nguyên nhân tràn ngang thường gặp: `width` cố định bằng px, ảnh không có `max-width: 100%`, flex không `wrap`, bảng dữ liệu rộng, dùng `100vw` (tính cả thanh cuộn dọc).
  * Cách xử lý: dùng đơn vị tương đối, `flex-wrap: wrap`, `min-width: 0` cho item flex, bọc bảng trong vùng cuộn riêng (`Table` của AntD có prop `scroll={{ x: true }}`).
  * Mobile UX Adaptation: chuyển cấu trúc ngang phức tạp sang **Vertical Stack**, **Drawer** hoặc **Collapse**; nút bấm đủ lớn cho thao tác cảm ứng.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Trang Admin Orders có bảng 8 cột. Trên 375px, cả trang bị kéo ngang. Thêm `scroll={{ x: true }}` cho `Table`, chỉ vùng bảng cuộn ngang, header và menu vẫn đứng yên.

> ⚠️ **Bẫy thường gặp:** mixin `respond-to` từ Bài 01 viết theo **mobile-first** (`min-width`), nên `respond-to('mobile') { display: none; }` sẽ ẩn phần tử **từ 640px trở lên**, tức là ẩn trên tablet/desktop chứ không phải trên điện thoại. Đừng đổi nghĩa của `respond-to` (mọi file SCSS cũ sẽ hỏng theo). Hãy bổ sung một mixin chiều ngược lại.

```scss
// styles/_mixins.scss – giữ nguyên map & respond-to của Bài 01, bổ sung respond-below
@use 'sass:map';

$breakpoints: ('mobile': 640px, 'tablet': 768px, 'desktop': 1024px);

// Mobile-first: áp dụng TỪ mốc trở lên
@mixin respond-to($breakpoint) {
  $value: map.get($breakpoints, $breakpoint);
  @if $value {
    @media (min-width: $value) { @content; }
  } @else {
    @error "Breakpoint `#{$breakpoint}` không tồn tại.";
  }
}

// Desktop-down: áp dụng DƯỚI mốc (dùng cho ẩn/hiện theo thiết bị)
@mixin respond-below($breakpoint) {
  $value: map.get($breakpoints, $breakpoint);
  @if $value {
    @media (max-width: $value - 0.02px) { @content; }
  } @else {
    @error "Breakpoint `#{$breakpoint}` không tồn tại.";
  }
}
```

```scss
// components/shared/EventFilterBar.module.scss
@use '../../styles/mixins' as *; // đường dẫn tương đối theo vị trí file

// Mốc 'tablet' = 768px, trùng breakpoint md của Grid Ant Design
.desktopOnly {
  display: block;
  @include respond-below('tablet') { display: none; }  // < 768px: ẩn
}

.mobileOnly {
  display: none;
  @include respond-below('tablet') { display: block; } // < 768px: hiện
}
```

#### 2.4. Chuyển Filter Bar sang Drawer trên di động

* **Khái niệm:** Thay vì ép thanh lọc ngang co lại, trên Mobile ta hiển thị một nút **"Bộ lọc"** mở `Drawer`; trên Desktop giữ nguyên Filter Bar nằm ngang.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Tách phần ô lọc thành sub-component `FilterFields` để dùng lại ở cả hai chế độ (đúng tinh thần DRY).
  * Grid AntD `xs={24}` (một cột trên mobile), `md={8}` (ba cột từ 768px).
  * Ẩn/hiện bằng CSS (`.desktopOnly`/`.mobileOnly`) thay vì đọc kích thước màn hình trong JavaScript, nên HTML server và client luôn giống nhau, không gây lỗi hydration.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Các ứng dụng đặt vé phổ biến đều gom bộ lọc vào một nút trên điện thoại. Người dùng chọn xong thì đóng Drawer, danh sách sự kiện cập nhật ngay vì state nằm ở component cha.

```tsx
// components/shared/EventFilterBar.tsx
'use client';

import { useState } from 'react';
import { Button, Col, Drawer, Input, Row, Select } from 'antd';
import styles from './EventFilterBar.module.scss';

export interface EventFilters {
  keyword: string;
  category: string | undefined;
  priceRange: 'all' | 'free' | 'paid';
}

interface EventFilterBarProps {
  value: EventFilters;
  onChange: (next: EventFilters) => void;
}

const CATEGORY_OPTIONS = [
  { label: 'Âm nhạc', value: 'music' },
  { label: 'Công nghệ', value: 'tech' },
  { label: 'Workshop', value: 'workshop' },
];

const PRICE_OPTIONS: { label: string; value: EventFilters['priceRange'] }[] = [
  { label: 'Tất cả mức giá', value: 'all' },
  { label: 'Miễn phí', value: 'free' },
  { label: 'Có phí', value: 'paid' },
];

function FilterFields({ value, onChange }: EventFilterBarProps) {
  return (
    <Row gutter={[16, 16]}>
      <Col xs={24} md={8}>
        <Input
          allowClear
          placeholder="Tìm sự kiện..."
          value={value.keyword}
          onChange={(e) => onChange({ ...value, keyword: e.target.value })}
        />
      </Col>
      <Col xs={24} md={8}>
        <Select
          allowClear
          style={{ width: '100%' }}
          placeholder="Danh mục"
          options={CATEGORY_OPTIONS}
          value={value.category}
          onChange={(category: string | undefined) => onChange({ ...value, category })}
        />
      </Col>
      <Col xs={24} md={8}>
        <Select
          style={{ width: '100%' }}
          options={PRICE_OPTIONS}
          value={value.priceRange}
          onChange={(priceRange: EventFilters['priceRange']) => onChange({ ...value, priceRange })}
        />
      </Col>
    </Row>
  );
}

export default function EventFilterBar(props: EventFilterBarProps) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <div className={styles.desktopOnly}>
        <FilterFields {...props} />
      </div>
      <div className={styles.mobileOnly}>
        <Button block size="large" onClick={() => setOpen(true)}>
          Bộ lọc
        </Button>
        <Drawer title="Bộ lọc sự kiện" placement="bottom" open={open} onClose={() => setOpen(false)}>
          <FilterFields {...props} />
        </Drawer>
      </div>
    </>
  );
}
```

#### 2.5. Hot Reload & dứt điểm Console Warnings

* **Khái niệm:** Mục tiêu cuối buổi là **Zero Console Warnings** và Hot Reload mượt khi chạy `npm run dev`. Hai cảnh báo hay gặp nhất là *React does not recognize the prop...* và *Hydration failed...*.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Unknown prop:** truyền prop tự đặt (ví dụ `isHot`) xuống thẻ DOM qua `{...props}`. Cách sửa: destructure prop đó ra trước khi spread.
  * **Hydration failed:** HTML server render khác HTML client render lần đầu. Nguyên nhân: đọc `localStorage`/`window` ngay khi render, dùng `Date.now()`/`Math.random()`, lồng thẻ sai (`<div>` trong `<p>`). Cách sửa: đọc dữ liệu trình duyệt trong `useEffect`, giữ cấu trúc HTML hợp lệ.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Badge "Yêu thích" trên Header đọc số lượng từ LocalStorage ngay trong thân component. Server không có LocalStorage nên render 0, client render 3, React báo hydration lỗi. Chuyển phần đọc vào `useEffect` là hết.

```tsx
// ✅ Không để prop tự đặt lọt xuống DOM
import type { HTMLAttributes } from 'react';

interface EventTagProps extends HTMLAttributes<HTMLSpanElement> {
  isHot?: boolean;
}

export function EventTag({ isHot = false, className = '', ...rest }: EventTagProps) {
  return <span {...rest} className={`${className} ${isHot ? 'tag-hot' : ''}`.trim()} />;
}
```

```tsx
// ✅ Đọc LocalStorage sau khi mount để tránh Hydration failed
'use client';

import { useEffect, useState } from 'react';
import { Badge } from 'antd';

export default function WishlistBadge() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    try {
      const parsed: unknown = JSON.parse(localStorage.getItem('wishlist') ?? '[]');
      setCount(Array.isArray(parsed) ? parsed.length : 0);
    } catch {
      setCount(0);
    }
  }, []);

  return (
    <Badge count={count} showZero>
      <span>Yêu thích</span>
    </Badge>
  );
}
```

#### 2.6. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

Hãy để AI làm "Tech Lead" rà soát, nhưng người quyết định giữ hay bỏ thay đổi vẫn là nhóm.

```text
Tôi có Component `EventFilterBar.tsx` đang bị tràn khung khi co màn hình xuống kích thước Mobile (375px).
Hãy hướng dẫn tôi refactor Component này sử dụng Ant Design `Drawer` hoặc Responsive Grid (`xs={24}`, `md={8}`)
để hiển thị dạng nút "Bộ lọc" mở ra Drawer trên Mobile, còn trên Desktop thì giữ nguyên Filter Bar nằm ngang.
Viết bằng Next.js TypeScript và Ant Design v5.
```

```text
Hãy đóng vai một Tech Lead chuyên về Clean Code. Hãy rà soát đoạn mã Next.js Component sau và refactor lại giúp tôi:
[Dán đoạn code lặp lại hoặc chưa tối ưu vào đây]

Yêu cầu refactor:
1. Phân rã các khối UI lặp lại thành sub-component nhỏ.
2. Loại bỏ các khai báo `any`, thay bằng Interface có cấu trúc chặt chẽ.
3. Tối ưu hóa re-render bằng cách dùng `React.memo` hoặc `useCallback` nếu cần thiết.
4. Giải thích ngắn gọn các cải tiến đã thực hiện.
```

**Checklist kiểm duyệt code AI trước khi commit:**

* **Hành vi không đổi:** so sánh giao diện trước/sau ở cả 375px, 768px, 1440px.
* **Type:** không còn `any`; `npx tsc --noEmit` không lỗi.
* **Logic:** handler, state, điều kiện hiển thị giữ nguyên; AI không "tiện tay" xóa nhánh xử lý lỗi.
* **Hiệu năng:** `memo`/`useCallback` có lý do cụ thể, không bọc tràn lan.
* **Responsive:** không còn thanh cuộn ngang; nút đủ lớn cho cảm ứng.
* **Console:** reload trang, Console không còn warning.

> **Quy tắc PBL:** mỗi lần refactor là một commit nhỏ, thông điệp rõ ràng (ví dụ `refactor(event-card): tách EventCard dùng chung, bỏ any`) để dễ hoàn tác khi AI làm hỏng logic.

#### 2.7. Thực hành trên lớp

Buổi PBL không theo khung Guided/Unguided thông thường. Giảng viên đóng vai **Technical Director / Senior Mentor**, đi từng nhóm tháo gỡ điểm nghẽn kỹ thuật.

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Định hướng | 30' | GV hướng dẫn Vibe Code Refactoring (Code Smell, Unused Imports, SCSS lặp) và quy chuẩn 375/768/1440px | Nhóm có danh sách lỗi cần xử lý |
| PBL Phần 1 – Responsive Polish | 60' | Kiểm tra 5 trang trên 3 kích thước, sửa tràn khung, chuyển Menu/Filter sang `Drawer`/`Collapse` | Không còn Horizontal Overflow, thao tác cảm ứng mượt |
| PBL Phần 2 – Vibe Code Refactoring & DRY | 60' | Tách Reusable Components, xóa `any`, biến thừa, `console.log`; gom SCSS bằng Mixin & CSS Variables | Codebase giảm >20% số dòng, TS strict pass 100% |
| PBL Phần 3 – Hot Reload & Review trực tiếp | 60' | Chạy Dev, sửa Console Warning; GV review code tại máy từng nhóm | Zero Console Warnings, danh mục bug đã fix |
| Tổng kết | 15' | Nghiệm thu tiến độ tại máy, giao BTVN | Biên bản kiểm tra tiến độ PBL 1 |

* **PBL Phần 1:** Mở DevTools ở chế độ Device Toolbar, lần lượt chọn 375px, 768px, 1440px cho Home, Listing, Event Detail, Booking Modal, Admin Orders. Ghi lỗi vào bảng chung của nhóm rồi chia người sửa.
* **PBL Phần 2:** Mỗi thành viên chọn component dài nhất mình phụ trách, dùng prompt Tech Lead ở mục 2.6 để refactor. Đếm số dòng trước/sau bằng `git diff --stat`.
* **PBL Phần 3:** Cả nhóm chạy `npm run dev`, sửa từng warning trong Console. GV kiểm tra trực tiếp và ghi nhận danh mục bug đã fix vào biên bản.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)

* 🔹 **Refactor không đổi hành vi:** Mục tiêu là code gọn hơn (>20% dòng), dễ bảo trì hơn, nhưng giao diện và logic phải giữ nguyên.
* 🔹 **Code Smell cần xử lý:** JSX/SCSS lặp lại, component >300 dòng, `any`, unused variables, `console.log` dư thừa.
* 🔹 **Responsive 3 mốc:** 375px – 768px – 1440px; tràn ngang được xử lý bằng đơn vị tương đối, `flex-wrap`, vùng cuộn riêng cho bảng, Drawer/Collapse trên mobile.
* 🔹 **Hydration an toàn:** Không đọc `localStorage`/`window` khi render; ẩn/hiện theo thiết bị bằng CSS để HTML server và client giống nhau.
* 🔹 **AI là Tech Lead gợi ý, nhóm là người duyệt:** Mọi thay đổi do AI đề xuất phải qua checklist type – logic – responsive – console trước khi commit.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Dấu hiệu nào sau đây KHÔNG được xem là Code Smell cần refactor gấp?
- A. Component dài hơn 300 dòng
- B. Khai báo `any` ở nhiều props
- C. Component nhận props có Interface rõ ràng
- D. Ba file card gần như giống hệt nhau

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Props có Interface rõ ràng là thực hành tốt. Các phương án còn lại là component quá lớn, lạm dụng <code>any</code> và vi phạm DRY.
</details>

**Câu 2:** Trang Admin Orders có bảng nhiều cột làm cả trang bị cuộn ngang ở 375px. Cách xử lý phù hợp nhất là gì?
- A. Đặt `overflow: hidden` cho thẻ `body`
- B. Cho `Table` cuộn ngang trong vùng riêng bằng `scroll={{ x: true }}`
- C. Giảm font chữ của cả trang xuống 10px
- D. Xóa bớt cột dữ liệu trên mọi thiết bị

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Chỉ vùng bảng cuộn ngang, phần còn lại của trang giữ nguyên. Ẩn overflow ở body sẽ che mất dữ liệu, còn giảm font hay xóa cột làm hỏng trải nghiệm.
</details>

**Câu 3:** Component đọc `localStorage` ngay trong thân hàm render và gây lỗi *Hydration failed*. Nên sửa thế nào?
- A. Chuyển phần đọc `localStorage` vào `useEffect`
- B. Đổi file thành Server Component
- C. Bọc component trong `React.memo`
- D. Xóa directive `'use client'`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> <code>useEffect</code> chỉ chạy trên trình duyệt sau khi mount, nên lần render đầu ở server và client cho cùng kết quả.
</details>

**Câu 4:** Vì sao truyền `onBook={(id) => router.push(...)}` trực tiếp trong JSX làm `React.memo` của `EventCard` mất tác dụng?
- A. Vì `memo` không hỗ trợ props kiểu hàm
- B. Vì `router.push` luôn gây reload toàn trang
- C. Vì Arrow Function không được dùng trong Client Component
- D. Vì mỗi lần cha render lại tạo một hàm mới, tham chiếu props thay đổi

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> <code>memo</code> so sánh nông props. Hàm mới mỗi lần render khiến so sánh luôn khác, nên cần <code>useCallback</code> để giữ tham chiếu ổn định.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-10-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)

* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Hãy chia sẻ một đoạn refactor mà AI đề xuất nhưng nhóm bạn **không** chấp nhận (hoặc phải sửa lại). AI đã sai ở đâu: làm đổi logic, thêm `memo` vô lý, hay phá responsive? Từ đó, theo bạn ranh giới giữa "để AI refactor" và "tự refactor" nằm ở đâu?
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Mỗi nhóm xây dựng file kịch bản chạy thử nghiệm toàn hệ thống `Test_Cases_Scenario.md` (hoặc `.docx`), bao phủ các luồng: Home → Danh mục → Chi tiết sự kiện → Đặt vé, Đăng nhập, Wishlist, Admin Orders.
  * Chuẩn bị sẵn tài khoản Vercel và GitHub Repository **công khai** ở branch `main` cho buổi PBL 2.
  * **Output:** tệp kịch bản kiểm thử sẵn sàng để test live khi deploy; đặt trong thư mục `docs/` của repo.
  * **Hạn nộp:** trước buổi học tiếp theo. Merge qua PR có tên `docs/test-cases-scenario`, nộp link PR lên LMS.
* **📚 Tài liệu đọc & tham khảo:**
  * Refactoring Guru – Code Smells: https://refactoring.guru/refactoring/smells
  * Google Responsive Web Design Basics: https://web.dev/responsive-web-design-basics/
  * Ant Design – Drawer: https://ant.design/components/drawer
  * Ant Design – Grid: https://ant.design/components/grid
  * React – memo: https://react.dev/reference/react/memo
  * Next.js – Hydration Error: https://nextjs.org/docs/messages/react-hydration-error
