# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 3: GIAO DIỆN CHUYÊN NGHIỆP & QUẢN LÝ TRẠNG THÁI
### Bài 05: Giao diện chuyên nghiệp với Ant Design, Bootstrap/Tailwind & tùy biến Theme

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Lớp học đảo ngược · **Chuẩn đầu ra:** PI 2.3 (CLO2)
> **Dự án xuyên suốt:** Smart Event Hub – Tích hợp UI Library (Ant Design v5), tùy biến Theme theo nhận diện thương hiệu, dựng Modal Đặt vé và trang Quản lý đơn hàng `/admin/orders`.

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Trình bày được ưu/nhược điểm của Ant Design v5, Bootstrap 5 và Tailwind CSS; giải thích vì sao cần `@ant-design/nextjs-registry` và cơ chế Design Token của `ConfigProvider`.
> * **[Bloom 3/4 - Kỹ năng]:** Cài đặt và cấu hình Ant Design trong Next.js App Router không lỗi FOUC/Hydration; sử dụng đúng Grid, Table, Modal, Form, Notification với TypeScript.
> * **[Bloom 5/6 - Năng lực]:** Lựa chọn thư viện UI phù hợp cho dự án nhóm và tùy biến giao diện Smart Event Hub có bản sắc riêng, không rập khuôn giao diện mặc định.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Trang Admin của Smart Event Hub cần một bảng đơn hàng có lọc theo trạng thái, phân trang, sắp xếp theo tổng tiền, cùng một form đặt vé có chọn ngày và kiểm tra dữ liệu. Tự viết bằng SCSS thuần, một bạn sinh viên có thể mất cả tuần chỉ để làm cho `DatePicker` chạy mượt trên điện thoại. Trong khi đó, các thư viện UI đã giải quyết sẵn những việc này và được hàng nghìn dự án kiểm chứng.

Nhưng nếu ghép thư viện vào mà không cấu hình, trang web sẽ nhấp nháy mất style khi tải, console báo lỗi Hydration, và giao diện trông "y hệt" mọi trang dùng Ant Design khác. **Làm thế nào để tận dụng sức mạnh của thư viện UI mà sản phẩm vẫn mang nhận diện riêng của nhóm?**

> 🧭 **Trước giờ học (Flipped Classroom):** Xem video/slide về tích hợp Ant Design / Bootstrap vào Next.js và Custom Theme bằng `ConfigProvider`. Lướt qua trang tổng quan component của Ant Design (link ở mục 5). Làm quiz 5–10 câu trên LMS. Chuẩn bị nhánh dự án đã hoàn thành Buổi 4.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Chọn thư viện UI: Ant Design, Bootstrap hay Tailwind?
* **Khái niệm:** Thư viện UI cung cấp component hoặc tiện ích CSS dựng sẵn. Ba lựa chọn phổ biến khác nhau ở **mức độ "có sẵn"** và **mức độ tự do tùy biến**.
* **Chi tiết kỹ thuật / Lý thuyết:**

| Tiêu chí | Ant Design v5 | Bootstrap 5 | Tailwind CSS |
|---|---|---|---|
| Bản chất | Bộ component React hoàn chỉnh (CSS-in-JS) | Bộ class CSS + JS plugin (không gắn React) | Utility-first CSS, không có component |
| Điểm mạnh | Table, Form, DatePicker, Modal cực mạnh; Design Token; hợp trang Admin | Dễ học, Grid quen thuộc, tài liệu nhiều | Tự do thiết kế, bundle CSS nhỏ, hợp với shadcn/ui |
| Điểm yếu | Bundle lớn hơn; giao diện dễ "rập khuôn"; cần registry khi SSR | Component JS cần xử lý thêm trong React (hoặc dùng `react-bootstrap`) | Phải tự dựng component phức tạp; className dài |
| Tùy biến | `ConfigProvider` token + SCSS Module | Biến Sass (`$primary`…) | `@theme` / file cấu hình |

  * Học phần chọn **Ant Design v5 làm trọng tâm** vì Smart Event Hub có nhiều màn hình quản trị (bảng, form, thông báo).
  * Không nên trộn nhiều thư viện CSS toàn cục trong một dự án: reset CSS của Bootstrap hoặc preflight của Tailwind có thể đè style của Ant Design.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Nhiều hệ thống quản trị nội bộ (ERP, CRM) chọn Ant Design vì Table và Form. Các landing page marketing lại hay chọn Tailwind để thiết kế tự do. Nhóm nào làm Smart Event Hub muốn giao diện người dùng thật "khác biệt" có thể dùng Tailwind cho trang công khai, nhưng phải thống nhất ngay từ đầu.

Cài đặt nhanh nếu nhóm chọn phương án khác:

```bash
# Bootstrap 5: import CSS một lần trong app/layout.tsx
npm install bootstrap
# import 'bootstrap/dist/css/bootstrap.min.css';

# Tailwind CSS v4 (hoặc chọn "Tailwind" khi chạy create-next-app)
npm install tailwindcss @tailwindcss/postcss postcss
# postcss.config.mjs: plugins: { '@tailwindcss/postcss': {} }
# app/globals.css: @import "tailwindcss";
```

#### 2.2. Tích hợp Ant Design v5 vào Next.js App Router
* **Khái niệm:** Ant Design v5 sinh CSS bằng JavaScript (CSS-in-JS) lúc chạy. Nếu không thu gom CSS ở phía server, HTML gửi về trình duyệt chưa có style, gây **FOUC** (Flash of Unstyled Content) – trang "trần trụi" vài trăm mili giây rồi mới đẹp.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `@ant-design/nextjs-registry` cung cấp `AntdRegistry` để extract CSS ngay khi render trên server.
  * Next.js 15 dùng React 19, trong khi antd v5 được viết cho React 16–18. Cần cài thêm gói vá `@ant-design/v5-patch-for-react-19` và import một lần ở phía client; nếu không, các hàm tĩnh như `message.success()` hay `Modal.confirm()` có thể không hiển thị.
  * Ghi rõ phiên bản `antd@5` khi cài để cả nhóm dùng cùng bản với tài liệu.

```bash
npm install antd@5 @ant-design/nextjs-registry @ant-design/v5-patch-for-react-19
```

```tsx
// app/providers.tsx
'use client';

import '@ant-design/v5-patch-for-react-19';
import { App, ConfigProvider } from 'antd';
import viVN from 'antd/locale/vi_VN';
import { themeConfig } from '@/theme/themeConfig';

export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ConfigProvider theme={themeConfig} locale={viVN}>
      <App>{children}</App>
    </ConfigProvider>
  );
}
```

```tsx
// app/layout.tsx (Server Component)
import { AntdRegistry } from '@ant-design/nextjs-registry';
import Providers from './providers';
import './globals.scss';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <body>
        <AntdRegistry>
          <Providers>{children}</Providers>
        </AntdRegistry>
      </body>
    </html>
  );
}
```

> **Vì sao tách `providers.tsx`?** Cách viết `ConfigProvider` thẳng trong `layout.tsx` vẫn chạy khi theme chỉ gồm token tĩnh. Nhưng khi thêm `algorithm: theme.darkAlgorithm` (một hàm) hoặc cần hook như `App.useApp()`, phần đó bắt buộc nằm trong Client Component. Tách sớm giúp `layout.tsx` gọn và không phải sửa lại sau này.

#### 2.3. Tùy biến Theme bằng Design Token và SCSS Module
* **Khái niệm:** Design Token là các biến thiết kế (màu chủ đạo, bo góc, font) mà mọi component Ant Design đọc chung. Đổi token một lần, toàn bộ Button, Input, Table, Modal đổi theo.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * `token`: biến toàn cục – `colorPrimary`, `borderRadius`, `fontFamily`, `colorBgContainer`…
  * `components`: token riêng cho từng component, ví dụ chỉ tăng chiều cao Button.
  * Ghi đè chi tiết hơn bằng SCSS Module với `:global(.ant-...)` đặt bên trong một class cục bộ, để chỉ ảnh hưởng đúng component đó. CSS của antd v5 dùng selector `:where()` có độ ưu tiên thấp nên class của chúng ta dễ thắng mà không cần `!important`.

```ts
// theme/themeConfig.ts
import type { ThemeConfig } from 'antd';

export const themeConfig: ThemeConfig = {
  token: {
    colorPrimary: '#6366F1', // Indigo – màu nhận diện Smart Event Hub
    borderRadius: 8,
    fontFamily: "'Be Vietnam Pro', system-ui, sans-serif",
  },
  components: {
    Button: { controlHeight: 40, fontWeight: 600 },
    Table: { headerBg: '#EEF2FF' },
  },
};
```

```scss
// components/features/BookingModal.module.scss
.bookingModal {
  :global(.ant-modal-content) { padding: 24px 28px; }
  :global(.ant-modal-title) { font-size: 20px; color: #4338ca; }
}
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Hai nhóm cùng dùng Ant Design nhưng một nhóm chọn tông Indigo bo góc 8px, nhóm kia chọn tông cam bo góc 16px với font Be Vietnam Pro. Chỉ cần khác token, người xem đã thấy hai sản phẩm có bản sắc riêng.

#### 2.4. Grid System và các component nâng cao
* **Khái niệm:** Grid của Ant Design chia hàng thành **24 cột**. `Row` là hàng, `Col` là cột, các prop `xs` `sm` `md` `lg` `xl` quy định số cột theo từng kích thước màn hình.
* **Chi tiết kỹ thuật / Lý thuyết:** Mốc mặc định: `xs` < 576px, `sm` ≥ 576px, `md` ≥ 768px, `lg` ≥ 992px, `xl` ≥ 1200px. `gutter={[16, 16]}` tạo khoảng cách ngang và dọc. Các component hay dùng: `Table` (dữ liệu Admin), `Modal` (popup đặt vé), `Form` (nhập liệu có validate), `Notification`/`Message` (phản hồi).

```tsx
// Mobile 1 cột · Tablet 2 cột · Laptop 3 cột · Desktop 4 cột
<Row gutter={[16, 16]}>
  {events.map((event) => (
    <Col key={event.id} xs={24} sm={12} md={8} lg={6}>
      <EventCard event={event} />
    </Col>
  ))}
</Row>
```

Modal đặt vé dùng `Modal` + `Form` + `DatePicker` + `Select` (Client Component):

```tsx
// components/features/BookingModal.tsx
'use client';

import { useState } from 'react';
import { App, Button, DatePicker, Form, Input, InputNumber, Modal, Select } from 'antd';
import type { Dayjs } from 'dayjs'; // dayjs được cài kèm antd
import styles from './BookingModal.module.scss';

type TicketType = 'VIP' | 'STANDARD';

interface BookingFormValues {
  ticketType: TicketType;
  quantity: number;
  attendDate: Dayjs;
  note?: string;
}

export default function BookingModal({ eventTitle }: { eventTitle: string }) {
  const [open, setOpen] = useState(false);
  const [form] = Form.useForm<BookingFormValues>();
  const { notification } = App.useApp();

  const handleOk = async () => {
    try {
      const values = await form.validateFields();
      notification.success({
        message: 'Đặt vé thành công',
        description: `${values.quantity} vé ${values.ticketType} – ngày ${values.attendDate.format('DD/MM/YYYY')}`,
      });
      form.resetFields();
      setOpen(false);
    } catch {
      // Lỗi validate đã hiển thị ngay dưới từng trường
    }
  };

  return (
    <>
      <Button type="primary" onClick={() => setOpen(true)}>Đặt vé</Button>
      <Modal
        title={`Đặt vé: ${eventTitle}`}
        open={open}
        onOk={handleOk}
        onCancel={() => setOpen(false)}
        okText="Xác nhận"
        cancelText="Hủy"
        className={styles.bookingModal}
      >
        <Form form={form} layout="vertical" initialValues={{ ticketType: 'STANDARD', quantity: 1 }}>
          <Form.Item name="ticketType" label="Loại vé" rules={[{ required: true }]}>
            <Select options={[{ value: 'VIP', label: 'VIP' }, { value: 'STANDARD', label: 'Standard' }]} />
          </Form.Item>
          <Form.Item name="quantity" label="Số lượng" rules={[{ required: true, type: 'number', min: 1, max: 10 }]}>
            <InputNumber min={1} max={10} style={{ width: '100%' }} />
          </Form.Item>
          <Form.Item name="attendDate" label="Ngày tham dự" rules={[{ required: true, message: 'Chọn ngày tham dự' }]}>
            <DatePicker format="DD/MM/YYYY" style={{ width: '100%' }} />
          </Form.Item>
          <Form.Item name="note" label="Ghi chú">
            <Input.TextArea rows={3} />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
}
```

#### 2.5. Table quản lý đơn hàng: Filter, Sorter, Pagination
* **Khái niệm:** `Table` nhận `columns` (cấu hình cột) và `dataSource` (dữ liệu). Lọc, sắp xếp, phân trang đều khai báo trong cấu hình, không phải tự viết logic.
* **Chi tiết kỹ thuật / Lý thuyết:** Cấu hình cột chứa hàm `render`, `onFilter`, `sorter`. Hàm không thể truyền từ Server Component sang Client Component, nên tách bảng thành **`OrdersTable.tsx` có `'use client'`**, còn `page.tsx` vẫn là Server Component.

```tsx
// app/admin/orders/OrdersTable.tsx
'use client';

import { Button, Table, Tag } from 'antd';
import type { TableProps } from 'antd';

type OrderStatus = 'SUCCESS' | 'PENDING' | 'CANCELLED';

interface OrderType {
  key: string;
  orderCode: string;
  customerName: string;
  eventName: string;
  orderDate: string;
  totalAmount: number;
  status: OrderStatus;
}

const STATUS_META: Record<OrderStatus, { color: string; label: string }> = {
  SUCCESS: { color: 'green', label: 'Đã thanh toán' },
  PENDING: { color: 'orange', label: 'Chờ xử lý' },
  CANCELLED: { color: 'red', label: 'Đã hủy' },
};

const STATUSES: OrderStatus[] = ['SUCCESS', 'PENDING', 'CANCELLED'];

const orders: OrderType[] = Array.from({ length: 10 }, (_, i) => ({
  key: String(i + 1),
  orderCode: `ORD-${String(i + 1).padStart(3, '0')}`,
  customerName: `Khách hàng ${i + 1}`,
  eventName: i % 2 === 0 ? 'Tech Summit 2025' : 'Đêm nhạc Acoustic',
  orderDate: `2025-11-${String(i + 10)}`,
  totalAmount: (i + 1) * 250000,
  status: STATUSES[i % 3],
}));

const columns: TableProps<OrderType>['columns'] = [
  { title: 'Mã đơn', dataIndex: 'orderCode', key: 'orderCode' },
  { title: 'Khách hàng', dataIndex: 'customerName', key: 'customerName' },
  { title: 'Sự kiện', dataIndex: 'eventName', key: 'eventName' },
  { title: 'Ngày đặt', dataIndex: 'orderDate', key: 'orderDate' },
  {
    title: 'Tổng tiền', dataIndex: 'totalAmount', key: 'totalAmount', align: 'right',
    sorter: (a, b) => a.totalAmount - b.totalAmount,
    render: (value: number) => `${value.toLocaleString('vi-VN')} ₫`,
  },
  {
    title: 'Trạng thái', dataIndex: 'status', key: 'status',
    filters: STATUSES.map((s) => ({ text: STATUS_META[s].label, value: s })),
    onFilter: (value, record) => record.status === value,
    render: (status: OrderStatus) => <Tag color={STATUS_META[status].color}>{STATUS_META[status].label}</Tag>,
  },
  {
    title: 'Hành động', key: 'action',
    render: (_, record) => <Button type="link" href={`/admin/orders/${record.orderCode}`}>Xem chi tiết</Button>,
  },
];

export default function OrdersTable() {
  return <Table<OrderType> columns={columns} dataSource={orders} pagination={{ pageSize: 5 }} scroll={{ x: 800 }} />;
}
```

```tsx
// app/admin/orders/page.tsx (Server Component)
import OrdersTable from './OrdersTable';

export default function AdminOrdersPage() {
  return (
    <main>
      <h1>Quản lý đơn hàng</h1>
      <OrdersTable />
    </main>
  );
}
```

> **Mẹo responsive:** `scroll={{ x: 800 }}` cho bảng cuộn ngang bên trong khung thay vì làm cả trang tràn ngang trên điện thoại.

#### 2.6. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

AI thường được huấn luyện trên nhiều code Ant Design v4 cũ, nên rất hay sinh sai API. Hãy nêu rõ phiên bản và môi trường trong prompt.

```text
Hãy hướng dẫn tôi tạo một Component BookingModal.tsx sử dụng Ant Design v5 trong dự án
Next.js 15 App Router (TypeScript strict).

Yêu cầu:
1. Sử dụng các component từ antd: Modal, Form, InputNumber, Select, DatePicker, Button.
2. Tùy biến Theme thông qua ConfigProvider với màu primary là #6366F1 (đặt ở providers.tsx).
3. Form gồm các trường: Loại vé (VIP, Standard), Số lượng (1-10), Ngày tham dự, Ghi chú.
4. Đảm bảo xử lý không bị lỗi Hydration mismatch trong Next.js: dùng 'use client' đúng chỗ,
   dùng prop open (không dùng visible), thông báo bằng App.useApp().
```

```text
Hãy viết mã nguồn /admin/orders gồm page.tsx (Server Component) và OrdersTable.tsx
('use client') sử dụng Table của Ant Design v5 với TypeScript.
- Khai báo Interface OrderType và kiểu TableProps<OrderType>['columns'].
- Render dữ liệu mock 10 đơn hàng.
- Cột "Trạng thái" dùng Tag: SUCCESS (xanh lá), PENDING (cam), CANCELLED (đỏ), có filter.
- Phân trang 5 mục/trang, cột Action có nút "Xem chi tiết". Không dùng any.
```

> **Checklist kiểm duyệt code AI (Ant Design v5):**
> 1. Dùng `open` thay cho `visible` (Modal, Drawer, Dropdown) – `visible` là API v4.
> 2. `Tabs`, `Menu`, `Dropdown` dùng prop `items`, không dùng `TabPane`/`Menu.Item` lồng trong children.
> 3. Không còn `import 'antd/dist/antd.css'` (v5 không cần file CSS này).
> 4. File chứa `columns` có hàm `render`, hoặc dùng hook `Form.useForm`, `App.useApp` phải có `'use client'`.
> 5. `ConfigProvider` đúng cú pháp `theme={{ token: { colorPrimary: '#6366F1', borderRadius: 8 } }}` – không lồng thừa ngoặc.
> 6. Không đọc `window`, `localStorage`, `new Date()` ngẫu nhiên khi render (nguồn gây Hydration mismatch).

#### 2.7. Thực hành trên lớp

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Guided Practice | 45' | Cài `antd`, `@ant-design/nextjs-registry`; cấu hình theme `#6366F1`, `borderRadius: 8`; dựng `BookingModal.tsx` | Modal mở mượt, không lỗi SSR/Hydration; nút và viền theo đúng Theme |
| Unguided Practice | 45' | Dựng `/admin/orders` bằng `Table` + `Tag`, có Filter trạng thái và Pagination | Bảng chuyên nghiệp, lọc và chuyển trang mượt |
| Team Challenge | 60' | Rà soát 5 màn hình chính, thay HTML thô bằng component AntD, tùy biến SCSS | Giao diện đồng bộ, có bản sắc riêng, responsive trên Tablet & Mobile |
| Tổng kết | 15' | GV nhận xét theme của từng nhóm, giải đáp, giao BTVN | Danh sách lỗi UI cần sửa của nhóm |

**Guided (45'):** Cài thư viện, tạo `providers.tsx` và `themeConfig.ts`, bọc `AntdRegistry` trong `app/layout.tsx`. Xây `BookingModal.tsx` với Modal, Form, DatePicker, Select để chọn loại vé, số lượng, ngày tham dự. Kiểm tra bằng cách tắt JavaScript hoặc reload nhanh: trang không được nhấp nháy mất style.

**Unguided (45'):** Trang `/admin/orders` gồm các cột Mã đơn hàng, Tên khách hàng, Tên sự kiện, Ngày đặt, Tổng tiền, Trạng thái (Đã thanh toán, Chờ xử lý, Đã hủy). Thêm Filter theo trạng thái và Pagination có sẵn của Table; khuyến khích thêm Sorter cho cột Tổng tiền.

**Team Challenge (60'):** Thay phần tử HTML thô bằng component tương ứng: `Carousel` cho Banner, `Tabs` cho Danh mục, `Rate` cho Đánh giá, `Skeleton` cho trạng thái chờ. Tùy biến token và SCSS Module để giao diện không mang cảm giác "nguyên bản" của Ant Design.

```tsx
// Ví dụ Tabs đúng cú pháp v5 (items) cho thanh danh mục
<Tabs
  defaultActiveKey="music"
  items={[
    { key: 'music', label: 'Âm nhạc', children: <EventGrid category="music" /> },
    { key: 'technology', label: 'Công nghệ', children: <EventGrid category="technology" /> },
  ]}
/>
```

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)
* 🔹 **Chọn thư viện có chủ đích:** Ant Design mạnh về component quản trị; Bootstrap dễ học; Tailwind tự do thiết kế. Chọn một thư viện chính cho cả nhóm.
* 🔹 **AntdRegistry chống FOUC:** bọc ứng dụng trong `AntdRegistry` ở `app/layout.tsx`; với React 19 thêm gói vá `@ant-design/v5-patch-for-react-19`.
* 🔹 **Design Token:** đổi `colorPrimary`, `borderRadius`, `fontFamily` trong `ConfigProvider` để toàn bộ component đổi theo; ghi đè chi tiết bằng SCSS Module + `:global`.
* 🔹 **Grid 24 cột:** `Row`/`Col` với `xs` `sm` `md` `lg` giúp bố cục co giãn theo thiết bị.
* 🔹 **Ranh giới Client:** component có hàm `render`, hook của antd hay sự kiện phải nằm trong file `'use client'`; trang vẫn giữ là Server Component.
* 🔹 **Vibe Coding với antd:** luôn ghi "Ant Design v5" trong prompt và soát lỗi API cũ (`visible`, `TabPane`, `antd.css`).

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Mục đích chính của `AntdRegistry` (gói `@ant-design/nextjs-registry`) là gì?
- A. Đăng ký bản quyền sử dụng Ant Design
- B. Thu gom CSS-in-JS ở phía server để tránh FOUC khi tải trang
- C. Tự động chuyển mọi component sang Server Component
- D. Thay thế `ConfigProvider` để đổi màu chủ đạo

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Ant Design v5 sinh CSS bằng JavaScript; registry extract CSS ngay khi render server để HTML gửi về đã có style, tránh hiện tượng trang nhấp nháy không style.
</details>

**Câu 2:** Muốn một thẻ sự kiện chiếm cả hàng trên điện thoại nhưng 4 thẻ một hàng trên màn hình lớn, cấu hình `Col` nào đúng?
- A. `<Col xs={24} lg={6}>`
- B. `<Col xs={6} lg={24}>`
- C. `<Col xs={12} lg={4}>`
- D. `<Col span={4}>`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> Grid có 24 cột: <code>xs={24}</code> chiếm trọn hàng trên mobile, <code>lg={6}</code> bằng 24/6 = 4 thẻ một hàng trên màn hình lớn.
</details>

**Câu 3:** Đoạn code AI sinh ra có `<Modal visible={isOpen}>`. Nhận xét nào đúng với Ant Design v5?
- A. Đúng chuẩn, không cần sửa
- B. Phải đổi thành `show={isOpen}`
- C. Phải đổi thành `open={isOpen}` vì `visible` là API cũ của v4
- D. Phải bỏ prop này, Modal tự mở

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Từ v5, Modal, Drawer, Dropdown dùng <code>open</code>. Đây là lỗi AI hay mắc do học từ code v4 cũ.
</details>

**Câu 4:** Cách nào ghi đè style tiêu đề Modal đặt vé mà KHÔNG ảnh hưởng các Modal khác?
- A. Sửa `.ant-modal-title` trong `globals.scss`
- B. Đổi `colorPrimary` trong `ConfigProvider`
- C. Thêm `!important` vào mọi thuộc tính trong `globals.scss`
- D. Gán `className` cục bộ từ SCSS Module cho Modal rồi dùng `:global(.ant-modal-title)` bên trong class đó

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> Class của CSS Module được hash nên chỉ áp dụng cho Modal được gán; <code>:global</code> bên trong chỉ nhắm class antd nằm dưới class đó. Sửa global hoặc đổi token sẽ ảnh hưởng toàn ứng dụng.
</details>

*Bộ 10+ câu đầy đủ: `quiz/quiz-bai-05-aiken.txt`*

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)
* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Nhóm bạn sẽ chọn Ant Design, Bootstrap hay Tailwind cho phần giao diện người dùng công khai của Smart Event Hub, và vì sao? Hãy đưa ra ít nhất 2 tiêu chí (tốc độ phát triển, bản sắc thiết kế, kích thước bundle, kinh nghiệm của thành viên…) và một rủi ro khi lựa chọn của nhóm.
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Kiểm tra và tối ưu tính Responsive cho toàn bộ component Ant Design đã dùng ở 5 màn hình chính, sử dụng Grid `Row`/`Col` với `xs`, `sm`, `md`, `lg`; sửa tất cả lỗi vỡ khung.
  * **Output:** Giao diện không tràn ngang (horizontal overflow) trên màn hình di động; kèm ảnh chụp 3 kích thước (375px, 768px, 1440px) của mỗi màn hình trong mô tả PR.
  * **Hạn nộp:** trước buổi học tiếp theo. Nộp link Pull Request trên LMS. Nhánh `feat/b05-<mssv>-antd-responsive`, tiêu đề PR `[B05] <Họ tên> – Ant Design & Responsive`, commit dạng `feat(ui): ...`, `fix(ui): repair responsive layout on mobile`.
* **📚 Tài liệu đọc & tham khảo:**
  * Ant Design v5 Official Docs: https://ant.design/components/overview/
  * Ant Design with Next.js App Router: https://ant.design/docs/react/use-with-next
  * Ant Design – Customize Theme: https://ant.design/docs/react/customize-theme
  * Ant Design v5 cho React 19: https://ant.design/docs/react/v5-for-19
  * Bootstrap 5 Introduction: https://getbootstrap.com/docs/5.3/getting-started/introduction/
  * Tailwind CSS với Next.js: https://tailwindcss.com/docs/installation/framework-guides/nextjs
  * **Câu hỏi tự kiểm tra khi đọc:** (1) Lỗi Hydration Mismatch xảy ra do đâu khi dùng thư viện UI client-side trong Next.js, và khắc phục thế nào? (2) Làm thế nào để ghi đè CSS của một component Ant Design mà không ảnh hưởng tới các component khác?
