# Bài 03: Điều hướng với Expo Router
Stack, Tab, Modal và từ màn hình đến dữ liệu · Checkpoint Sprint 1

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Giải thích mô hình điều hướng trên mobile: stack, tab, modal
- Xây điều hướng theo file với Expo Router
- Dùng route động, tham số và deep link
- Phác sơ đồ luồng màn hình và ERD sơ bộ
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1, CLO2, CLO3. Cuối buổi là Checkpoint Sprint 1.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Web có thanh địa chỉ và link
- Điện thoại có nút Back, thanh tab, cử chỉ vuốt
- Tổ chức màn hình thế nào để người dùng không bị "lạc"?

---

## Slide 3: Ba kiểu điều hướng
**Nội dung chính**:
- **Stack**: màn hình mới chồng lên, Back gỡ màn hình trên cùng
- **Tab**: thanh cố định ở cuối cho các khu vực chính
- **Modal**: trượt lên cho tác vụ ngắn, đóng xong về chỗ cũ
**Ví dụ**:
- LHU Food: Danh sách → Chi tiết (stack); Trang chủ/Giỏ hàng/Đơn hàng/Tài khoản (tab); Xác nhận đặt hàng (modal)

---

## Slide 4: Expo Router: mỗi file là một màn hình
**Nội dung chính**:
```text
app/
├── _layout.tsx        Stack gốc
├── (tabs)/
│   ├── _layout.tsx    Thanh tab
│   ├── index.tsx      /
│   └── cart.tsx       /cart
├── product/[id].tsx   /product/12
└── confirm.tsx        modal /confirm
```
- `(tabs)` là nhóm route: không xuất hiện trong đường dẫn

---

## Slide 5: Layout: Stack gốc
**Nội dung chính**:
```tsx
<Stack>
  <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
  <Stack.Screen name="product/[id]" options={{ title: 'Chi tiết món' }} />
  <Stack.Screen name="confirm" options={{ presentation: 'modal' }} />
</Stack>
```
**Ghi chú giảng viên**:
- Giải thích vì sao (tabs) cần headerShown: false để không hiện hai thanh tiêu đề.

---

## Slide 6: Layout: Thanh tab
**Nội dung chính**:
```tsx
<Tabs>
  <Tabs.Screen name="index" options={{ title: 'Trang chủ' }} />
  <Tabs.Screen name="cart" options={{ title: 'Giỏ hàng' }} />
  <Tabs.Screen name="orders" options={{ title: 'Đơn hàng' }} />
  <Tabs.Screen name="account" options={{ title: 'Tài khoản' }} />
</Tabs>
```

---

## Slide 7: Route động và tham số
**Nội dung chính**:
- `product/[id].tsx` phục vụ `/product/1`, `/product/2`…
- Đọc tham số trong màn hình chi tiết, mở màn hình từ danh sách:
```tsx
// app/product/[id].tsx
const { id } = useLocalSearchParams<{ id: string }>();

// Màn hình danh sách
<Link href={`/product/${item.id}`}>Xem chi tiết</Link>
```

---

## Slide 8: router.push, back, replace
**Nội dung chính**:
- `router.push()`: thêm màn hình vào stack
- `router.back()`: quay lại
- `router.replace()`: thay màn hình hiện tại
**Ví dụ**:
- Đăng nhập xong dùng replace để Back không quay về màn hình đăng nhập
**Hoạt động**: Hỏi lớp: luồng nào trong đề tài của nhóm cần replace?

---

## Slide 9: Deep link
**Nội dung chính**:
- Khai báo `"scheme": "lhufood"` trong `app.json`
- `lhufood://product/12` mở thẳng chi tiết món 12
- Bài 09: bấm thông báo realtime mở đúng đơn hàng
**Ghi chú giảng viên**:
- Chỉ giới thiệu, chưa yêu cầu sinh viên làm deep link ở buổi này.

---

## Slide 10: Sơ đồ luồng màn hình
**Nội dung chính**:
- Vẽ các màn hình và mũi tên chuyển giữa chúng
- Thống nhất cấu trúc `app/` trước khi viết mã
- Công cụ: draw.io, Figma (FigJam)

---

## Slide 11: Từ màn hình đến dữ liệu: ERD sơ bộ
**Nội dung chính**:
- Trang chủ, Danh mục → Categories, Products
- Giỏ hàng, Xác nhận → Products, Users
- Đơn hàng → Orders, OrderItems
**Ví dụ**:
- Categories 1-n Products; Users 1-n Orders; Orders n-n Products qua OrderItems
**Ghi chú giảng viên**:
- ERD sơ bộ là đầu vào cho bài 05: CSDL SQL Server và stored procedure.

---

## Slide 12: Thực hành có hướng dẫn
**Nội dung chính**:
- Tổ chức lại `app/` theo cây thư mục mẫu
- Stack gốc + 4 tab có biểu tượng
- `product/[id].tsx` với dữ liệu giả, modal `confirm.tsx`
- Kiểm tra nút Back của Android ở từng màn hình
- Vẽ sơ đồ luồng màn hình và ERD sơ bộ LHU Food

---

## Slide 13: Thực hành không hướng dẫn
**Nội dung chính**:
- Luồng Danh mục → Danh sách món theo danh mục → Chi tiết
- Tiêu đề đổi theo danh mục
- Back quay lại đúng từng bước, không lặp màn hình trong stack

---

## Slide 14: Checkpoint Sprint 1
**Nội dung chính**:
- Khung ứng dụng của nhóm đủ điều hướng với dữ liệu giả
- Nộp sơ đồ luồng màn hình và ERD sơ bộ trong `docs/`
- Demo 3 phút trên Android
- Sprint Review: đã làm gì, còn gì · Retrospective: giữ gì, đổi gì
**Ghi chú giảng viên**:
- Ghi nhận xét từng nhóm; nhóm chưa có ERD sơ bộ cần bổ sung trước bài 05.

---

## Slide 15: Tóm tắt
**Nội dung chính**:
- Stack cho đi sâu, Tab cho khu vực chính, Modal cho tác vụ ngắn
- Expo Router: thư mục `app/` là bản đồ điều hướng
- Route động `[id]` + `useLocalSearchParams`
- Màn hình → thực thể → ERD sơ bộ
**Hoạt động**: Làm quiz Bài 03 ở cuối trang bài học

---

## Slide 16: Tài liệu của buổi
**Đọc thêm**:
- Giáo trình nội bộ, Chương 3: Điều hướng với Expo Router
- Bài tập hướng dẫn theo dự án LHU Food (cuối Chương 3)
- SRS LHU Food: mục 5.14.1 (màn hình, route), 7.1 (bảng)
- Kế hoạch Agile & Product Backlog (Definition of Done, tiêu chí nghiệm thu)
**Ghi chú giảng viên**:
- Các file Word/Excel nằm ở mục Tài liệu của bài trên LMS và trang học phần (giao-trinh/, srs/, rubric/).
