# Bài 04: Quản lý trạng thái, danh sách & form
Giỏ hàng dùng chung, thực đơn cuộn mượt, form kiểm tra dữ liệu

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Phân biệt trạng thái cục bộ, toàn cục và dữ liệu từ server
- Quản lý giỏ hàng toàn cục bằng Zustand
- Hiển thị danh sách lớn bằng FlatList
- Xây form có kiểm tra dữ liệu với React Hook Form + Zod
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Thêm món ở màn hình Chi tiết → tab Giỏ hàng biết ngay bằng cách nào?
- Thực đơn có 500 món → làm sao cuộn vẫn mượt?
- Người dùng gõ sai số điện thoại → báo lỗi ở đâu, lúc nào?

---

## Slide 3: Ba loại trạng thái
**Nội dung chính**:
- **Cục bộ**: một màn hình dùng → `useState`, `useReducer`
- **Toàn cục**: nhiều màn hình dùng → Zustand
- **Từ server**: bản gốc trong SQL Server → TanStack Query (bài 05)
**Ví dụ**:
- Số lượng đang chọn (cục bộ) · Giỏ hàng (toàn cục) · Thực đơn (server)
**Hoạt động**: Lớp phân loại nhanh 6 dữ liệu của LHU Food

---

## Slide 4: Giỏ hàng với Zustand
**Nội dung chính**:
```ts
export const useCart = create<CartState>((set, get) => ({
  items: [],
  add: (p) => set((s) => ({ items: [...s.items, { ...p, quantity: 1 }] })),
  remove: (id) => set((s) => ({ items: s.items.filter((i) => i.id !== id) })),
  total: () => get().items.reduce((sum, i) => sum + i.price * i.quantity, 0),
}));
```
- Bản đầy đủ (cộng dồn số lượng) ở mục 2.1 của bài học
**Ghi chú giảng viên**:
- Nhấn mạnh luôn trả về mảng mới, không dùng push.

---

## Slide 5: Đọc store ở màn hình
**Nội dung chính**:
```tsx
const items = useCart((state) => state.items);
const add = useCart((state) => state.add);
```
- Chỉ chọn phần state cần dùng
- Màn hình chỉ vẽ lại khi phần đó thay đổi
- Badge số món trên tab: `tabBarBadge`

---

## Slide 6: ScrollView và FlatList
**Nội dung chính**:
- `ScrollView` vẽ **tất cả** phần tử ngay lập tức
- `FlatList` chỉ vẽ phần tử đang hiển thị → mượt, ít bộ nhớ
- Không lồng FlatList trong ScrollView; phần đầu trang đưa vào `ListHeaderComponent`
**Ghi chú giảng viên**:
- Demo: 500 món bằng ScrollView và FlatList trên máy Android tầm trung.

---

## Slide 7: FlatList cho thực đơn
**Nội dung chính**:
```tsx
<FlatList
  data={products}
  keyExtractor={(item) => String(item.id)}
  renderItem={({ item }) => <ProductCard {...item} />}
  numColumns={2}
  ListEmptyComponent={<Text>Chưa có món nào.</Text>}
  refreshing={refreshing}
  onRefresh={reload}
/>
```

---

## Slide 8: Form với React Hook Form + Zod
**Nội dung chính**:
- **Zod**: mô tả quy tắc dữ liệu một lần (schema)
- **React Hook Form**: quản lý giá trị, lỗi, gửi form
- `npx expo install react-hook-form zod @hookform/resolvers`
```ts
const schema = z.object({
  phone: z.string().regex(/^0\d{9}$/, 'Số điện thoại gồm 10 chữ số, bắt đầu bằng 0'),
  note: z.string().max(200, 'Ghi chú tối đa 200 ký tự').optional(),
});
```

---

## Slide 9: Controller cho TextInput
**Nội dung chính**:
```tsx
<Controller control={control} name="phone"
  render={({ field: { onChange, onBlur, value } }) => (
    <TextInput value={value} onChangeText={onChange}
      onBlur={onBlur} keyboardType="phone-pad" />
  )}
/>
{errors.phone && <Text>{errors.phone.message}</Text>}
```
- Gửi form: `handleSubmit(onSubmit)` chỉ chạy khi dữ liệu hợp lệ

---

## Slide 10: Mẹo form trên mobile
**Nội dung chính**:
- Chọn đúng `keyboardType`: email, số điện thoại, số
- `KeyboardAvoidingView` để bàn phím không che ô đang nhập
- So khớp mật khẩu: `.refine(...)` với `path: ['confirm']`
- Kiểm tra ở app chưa đủ: API vẫn phải kiểm tra lại

---

## Slide 11: Vibe coding cho quy tắc nghiệp vụ
**Nội dung chính**:
- 1. Viết đặc tả bằng lời
- 2. Nhờ Copilot sinh schema Zod, thông báo lỗi tiếng Việt
- 3. **Tự viết bảng trường hợp biên** và thử từng dòng
- 4. Sửa schema chỗ AI sai, ghi `PROMPTS.md`
**Ví dụ**:
- Số điện thoại 9, 10, 11 chữ số; mật khẩu 7 và 8 ký tự
**Ghi chú giảng viên**:
- Liên hệ kỹ thuật giá trị biên ở môn Kiểm thử phần mềm.

---

## Slide 12: Thực hành có hướng dẫn
**Nội dung chính**:
- Store giỏ hàng; nút "Thêm vào giỏ"; tab Giỏ hàng có tổng tiền
- Badge số món trên tab
- Trang chủ dùng FlatList 2 cột, danh sách rỗng, kéo để tải lại
- Form ghi chú đơn hàng trong modal Xác nhận

---

## Slide 13: Thực hành không hướng dẫn & thử thách nhóm
**Nội dung chính**:
- **Cá nhân**: form Đăng ký đủ quy tắc, kèm bảng trường hợp biên đã thử
- **Nhóm**: store toàn cục + 1 form nghiệp vụ
- **Người làm backend**: khởi tạo NestJS, cài `mssql`, kết nối SQL Server, tạo bảng theo ERD sơ bộ

---

## Slide 14: Tóm tắt
**Nội dung chính**:
- Chọn đúng loại trạng thái trước khi viết mã
- Zustand cho dữ liệu dùng chung; luôn trả về mảng mới
- FlatList cho danh sách dài; luôn có trạng thái rỗng
- Zod mô tả quy tắc; tự kiểm tra trường hợp biên mã AI sinh ra
**Hoạt động**: Làm quiz Bài 04 ở cuối trang bài học

---

## Slide 15: Tài liệu của buổi
**Đọc thêm**:
- Giáo trình nội bộ, Chương 4: Quản lý trạng thái, danh sách và form
- Bài tập hướng dẫn theo dự án LHU Food (cuối Chương 4)
- SRS LHU Food: mục 4.7 (US-C01, C02, G02, G04), 5.4, BR-02, BR-07
**Ghi chú giảng viên**:
- Các file Word/Excel nằm ở mục Tài liệu của bài trên LMS và trang học phần (giao-trinh/, srs/, rubric/).
