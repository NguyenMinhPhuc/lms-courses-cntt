# Bài 02: Routing, layout & giao diện với Tailwind CSS
Sprint 1 · Nền tảng & Giao diện

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Phân tích chức năng thành sitemap và route
- Route lồng nhau, route group, route động
- Layout quản trị và layout khách
- Giao diện responsive với Tailwind CSS và shadcn/ui
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Quản lý cần sidebar, sinh viên cần thực đơn gọn trên điện thoại
- Hai khu vực, hai bố cục, một ứng dụng
- Vẽ giao diện trước hay phân tích trang trước?

---

## Slide 3: Từ chức năng đến route
**Nội dung chính**:
- Xem thực đơn (US-G01) → /menu → mọi người → GET /products
- Chi tiết món (US-G03) → /product/[id] → GET /products/:id
- Quản lý món (US-A02) → /admin/products → admin
- Màn hình quầy (US-S02) → /admin/orders → staff, admin
**Hoạt động**: Nhóm điền bảng ánh xạ cho 3 chức năng của đề tài

---

## Slide 4: Cây thư mục
**Nội dung chính**:
```text
app/
  (shop)/layout.tsx           header khách
  (shop)/menu/page.tsx        /menu
  (shop)/product/[id]/page.tsx
  admin/layout.tsx            sidebar
  admin/products/page.tsx     /admin/products
  not-found.tsx
```

---

## Slide 5: Route group
**Nội dung chính**:
- Thư mục trong ngoặc: (shop), (admin)
- Không xuất hiện trong URL
- Mỗi nhóm có layout riêng
- Cẩn thận: hai nhóm không được trùng đường dẫn

---

## Slide 6: Route động
**Nội dung chính**:
```tsx
export default async function ProductPage(
  { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const product = mockProducts.find((p) => p.id === Number(id));
  if (!product) notFound();
  return <h1>{product.name}</h1>;
}
```
- Từ Next.js 15, params là Promise

---

## Slide 7: File đặc biệt
**Nội dung chính**:
- loading.tsx: giao diện chờ
- error.tsx: giao diện lỗi (Client Component)
- not-found.tsx: trang 404
- Link: điều hướng không tải lại toàn trang

---

## Slide 8: Layout quản trị
**Nội dung chính**:
- Sidebar ẩn trên điện thoại, hiện từ md
- Layout không vẽ lại khi chuyển trang con
- metadata: tiêu đề từng trang
- Cây component: layout → trang → ProductCard, OrderTable

---

## Slide 9: Tailwind CSS
**Nội dung chính**:
- Utility class trong JSX: p-4, text-xl, bg-blue-950
- Mobile-first: sm:, md:, lg: áp dụng từ kích thước đó trở lên
- grid-cols-1 md:grid-cols-3
- Viết đủ tên class, không ghép chuỗi động

---

## Slide 10: shadcn/ui
**Nội dung chính**:
```bash
npx shadcn@latest init
npx shadcn@latest add button card table dialog
```
- Mã component chép vào components/ui
- Sửa theo nhận diện LHU được

---

## Slide 11: Từ Figma đến mã
**Nội dung chính**:
- Đưa AI: ảnh thiết kế, bảng route, AGENTS.md
- Yêu cầu dùng shadcn/ui và class Tailwind
- Kiểm tra: màu, khoảng cách, responsive 3 kích thước
- Loại bỏ thư viện UI lạ do AI tự thêm

---

## Slide 12: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: khung (shop) và admin, lưới món, route động, bảng ánh xạ
- **Không hướng dẫn**: /counters và /counters/[id] responsive
- **Nhóm**: sơ đồ chức năng, sitemap, bảng ánh xạ, khung route

---

## Slide 13: Tổng kết
**Nội dung chính**:
- Phân tích route trước khi code
- Route group, route động, layout dùng chung
- Tailwind mobile-first, shadcn/ui
- Buổi sau: lấy dữ liệu thật từ API, Checkpoint Sprint 1

---

## Slide 14: Tài liệu của buổi
**Đọc thêm**:
- SRS LHU Food: mục 5.1 (module), 5.14.2 (trang web), 8 (danh mục API)
- Next.js: Layouts and Pages, Route Groups
- Tailwind CSS: Responsive design; shadcn/ui cho Next.js
**Ghi chú giảng viên**:
- Nhắc nhóm lưu file nguồn sơ đồ trong docs/ để dùng cho báo cáo.
