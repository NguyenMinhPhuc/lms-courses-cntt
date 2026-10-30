# Bài 03: Server Components & lấy dữ liệu từ API
Sprint 1 · Checkpoint Sprint 1

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Phân biệt Server và Client Component
- Lấy dữ liệu từ API mẫu với cache phù hợp
- Trạng thái tải và lỗi
- Test case, báo cáo sprint, kế hoạch Sprint 2
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1–CLO4. Cuối buổi là Checkpoint Sprint 1.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Thực đơn đang hiện món giả
- Hôm nay: món thật từ API, lấy ngay trên server
- Chứng minh trang đúng yêu cầu bằng test case, không bằng "em chạy thử thấy được"

---

## Slide 3: Server và Client Component
**Nội dung chính**:
- **Server**: async/await, biến bí mật, gọi API; không gửi mã xuống
- **Client**: state, sự kiện, API trình duyệt; gửi mã xuống
- Trang = Server Component; tách phần tương tác nhỏ
**Hoạt động**: Chỉ ra ranh giới "use client" trên trang chi tiết món

---

## Slide 4: Biến môi trường
**Nội dung chính**:
```text
# .env.local
API_URL=http://<địa-chỉ-API-mẫu>:3000
```
- Không có NEXT_PUBLIC_: chỉ server đọc được
- Không commit .env.local; khởi động lại dev sau khi sửa

---

## Slide 5: Hàm gọi API tập trung
**Nội dung chính**:
```ts
import 'server-only';
export async function apiGet<T>(path: string, revalidate = 30) {
  const res = await fetch(`${process.env.API_URL}${path}`,
                          { next: { revalidate } });
  if (!res.ok) throw new Error(`API ${path} trả về ${res.status}`);
  return res.json() as Promise<T>;
}
```

---

## Slide 6: Trang thực đơn
**Nội dung chính**:
```tsx
const { category, q } = await searchParams;
const [categories, products] = await Promise.all([
  apiGet<Category[]>('/categories', 300),
  apiGet<Product[]>(`/products?${query}`, 30),
]);
```
- Lọc danh mục, tìm kiếm qua URL
- Form GET: không cần JavaScript phía client

---

## Slide 7: Cache và làm mới
**Nội dung chính**:
- Từ Next.js 15, fetch không tự cache
- revalidate: dùng lại kết quả N giây rồi làm mới
- Danh mục 5 phút, món 30 giây: theo mức thay đổi dữ liệu
- Món vừa hết hàng: khách thấy sau tối đa 30 giây

---

## Slide 8: Trạng thái tải và lỗi
**Nội dung chính**:
- loading.tsx: streaming, khung trang hiện ngay
- Suspense: khối chậm không chặn khối nhanh
- error.tsx (Client Component): thông báo thân thiện + Thử lại
- Không hiển thị lỗi kỹ thuật cho người dùng

---

## Slide 9: Test case từ tiêu chí nghiệm thu (CLO2)
**Nội dung chính**:
- TC-01 US-G01: mở /menu → thấy danh mục, giá "35.000 đ"
- TC-02 US-G01: chọn "Đồ uống" → chỉ còn đồ uống
- TC-03 US-G02: tìm "com ga" → có "Cơm gà xối mỡ"
- TC-04 US-G03: /product/999999 → trang 404
- TC-05: API sai → thông báo lỗi + Thử lại

---

## Slide 10: Báo cáo sprint (CLO3)
**Nội dung chính**:
- Sprint Goal và kết quả, link demo
- Story hoàn thành: người phụ trách, PR
- Phân tích thành phần: sơ đồ có số hình, chú thích
- Kiểm thử: số test case, đạt, lỗi đã sửa
- Kế hoạch so với thực tế; kế hoạch sprint sau

---

## Slide 11: Sprint Review và kế hoạch Sprint 2 (CLO4)
**Nội dung chính**:
- Demo cho giảng viên, nhận góp ý
- Cập nhật backlog
- Chọn story theo velocity thực tế của Sprint 1
- Board cập nhật trước khi rời lớp

---

## Slide 12: Checkpoint Sprint 1
**Nội dung chính**:
- Demo khung web với dữ liệu thật từ API mẫu
- Sơ đồ chức năng, sitemap, bảng ánh xạ route (CLO1)
- Test case + kết quả (CLO2)
- Báo cáo sprint 1 đúng định dạng (CLO3)
- Kế hoạch Sprint 2 trên board (CLO4)

---

## Slide 13: Tổng kết
**Nội dung chính**:
- Server Component lấy dữ liệu, Client Component lo tương tác
- Cache theo mức thay đổi của dữ liệu
- Luôn có trạng thái tải, lỗi, rỗng
- Buổi sau: Client Components, giỏ hàng, form

---

## Slide 14: Tài liệu của buổi
**Đọc thêm**:
- SRS LHU Food: mục 4.7 (tiêu chí US-G01, G02, G03), 8 (định dạng API)
- Kế hoạch Agile: Definition of Done, Sprint Review
- Next.js: Fetching Data, Error Handling, Environment Variables
- Trang Đánh giá học phần: quy định định dạng báo cáo
**Ghi chú giảng viên**:
- Chấm checkpoint theo đủ 4 sản phẩm; ghi nhận xét vào báo cáo sprint của nhóm.
