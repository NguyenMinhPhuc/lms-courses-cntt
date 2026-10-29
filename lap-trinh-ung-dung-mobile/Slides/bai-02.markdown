# Bài 02: Core Components, Styling & Layout với Flexbox
Từ bản thiết kế Figma đến màn hình chạy trên Android

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Sử dụng các core component của React Native
- Dựng bố cục responsive bằng Flexbox
- Xây design system: theme và component dùng chung
- Chuyển thiết kế Figma thành mã bằng vibe coding; vẽ sơ đồ chức năng
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1, CLO3.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Bản Figma của nhóm ở môn UI/UX đã đẹp
- Làm sao để màn hình trên điện thoại giống thiết kế?
- Và vẫn đúng trên cả máy nhỏ lẫn máy màn hình lớn?
**Ghi chú giảng viên**:
- Chiếu một bản Figma mẫu LHU Food và hỏi sinh viên sẽ chia màn hình thành những khối nào.

---

## Slide 3: Core components thường dùng
**Nội dung chính**:
- `View`: khung chứa · `Text`: chữ · `Image`: ảnh
- `ScrollView`: nội dung dài, cuộn được (không dùng cho danh sách dài)
- `TextInput`: ô nhập (`keyboardType`, `secureTextEntry`)
- `Pressable`: vùng bấm được, đổi style khi đang bấm
**Ghi chú giảng viên**:
- Danh sách dài sẽ học FlatList ở bài 04.

---

## Slide 4: Vùng an toàn (safe area)
**Nội dung chính**:
- Điện thoại có tai thỏ, thanh trạng thái, thanh điều hướng
- Dùng `SafeAreaView` của `react-native-safe-area-context`
- Thư viện đã có sẵn trong dự án Expo
**Ví dụ**:
- Không có safe area: tiêu đề màn hình bị tai thỏ che mất

---

## Slide 5: Flexbox trên mobile khác web
**Nội dung chính**:
- Mặc định `flexDirection: 'column'` (xếp dọc)
- Xếp ngang: `flexDirection: 'row'`
- `flex: 1`: chiếm phần không gian còn lại
- `justifyContent` (trục chính), `alignItems` (trục phụ), `gap`
- Số không đơn vị là **dp**, tự co giãn theo mật độ màn hình
**Ghi chú giảng viên**:
- Demo trực tiếp: đổi flexDirection và justifyContent, cho lớp đoán kết quả trước khi lưu.

---

## Slide 6: Responsive theo kích thước màn hình
**Nội dung chính**:
- `useWindowDimensions()` trả về chiều rộng hiện tại
```tsx
const { width } = useWindowDimensions();
const columns = width >= 600 ? 3 : 2;
const itemWidth = (width - 16 * (columns + 1)) / columns;
```
**Ví dụ**:
- Lưới món ăn: 2 cột trên điện thoại nhỏ, 3 cột trên máy rộng

---

## Slide 7: Design system: theme.ts
**Nội dung chính**:
- Gom màu, khoảng cách, cỡ chữ về một file
```ts
export const colors = { primary: '#013D88', accent: '#FFC627' };
export const spacing = { xs: 4, sm: 8, md: 16, lg: 24 };
export const fontSize = { body: 16, title: 20, heading: 24 };
```
- Đổi một chỗ, cả app đổi theo; AI sinh mã đúng màu của nhóm

---

## Slide 8: Component dùng chung
**Nội dung chính**:
- `Button`: biến thể chính/phụ, trạng thái vô hiệu
- `Card`: khung nội dung bo góc
- `Input`: có nhãn và dòng báo lỗi
- Dark mode: `useColorScheme()` để chọn bảng màu sáng/tối
**Hoạt động**: Hỏi lớp: màn hình Trang chủ LHU Food dùng lại được những component nào?

---

## Slide 9: Từ Figma đến mã bằng vibe coding
**Nội dung chính**:
- 1. Xuất ảnh màn hình từ Figma, ghi đặc tả
- 2. Prompt có ràng buộc: dùng theme, dùng component có sẵn, không thêm thư viện
- 3. Chạy thử, **đặt cạnh ảnh thiết kế** để so
- 4. Sửa chỗ lệch, tách component, ghi `PROMPTS.md`
**Ghi chú giảng viên**:
- Demo prompt mẫu ở mục 2.4 của bài học với Copilot Chat.

---

## Slide 10: Lỗi AI hay mắc khi dựng giao diện
**Nội dung chính**:
- Viết cứng màu thay vì lấy từ theme
- Dùng thư viện UI ngoài không được phép
- Đặt chữ ngoài `<Text>`
- Quên safe area
**Hoạt động**: Sinh viên tìm lỗi trong một đoạn mã AI sinh ra do giảng viên chuẩn bị

---

## Slide 11: Sơ đồ chức năng
**Nội dung chính**:
- Chia ứng dụng thành nhóm chức năng và chức năng con
- Là cơ sở để thiết kế màn hình, API và dữ liệu
- Minh chứng cho CLO1 và CLO3
**Ví dụ**:
- LHU Food: Khách hàng (thực đơn, giỏ hàng, đặt hàng, theo dõi đơn) · Nhân viên (đơn mới, cập nhật trạng thái, quản lý món, thống kê) · Tài khoản

---

## Slide 12: Thực hành có hướng dẫn
**Nội dung chính**:
- Tạo `theme.ts` và 3 component: Button, Card, ProductCard
- Dựng Trang chủ (lời chào, tìm kiếm, lưới món) và Chi tiết món
- Sinh màn hình Chi tiết từ Figma bằng Copilot, so và sửa
- Vẽ sơ đồ chức năng LHU Food bằng draw.io, lưu vào `docs/`

---

## Slide 13: Thực hành không hướng dẫn & thử thách nhóm
**Nội dung chính**:
- **Cá nhân**: màn hình Hồ sơ theo thiết kế, đúng trên 2 kích thước màn hình
- **Nhóm**: UI kit (theme + 5 component), 3 màn hình chính theo Figma, sơ đồ chức năng
**Ghi chú giảng viên**:
- Nhắc nộp 2 ảnh chụp màn hình ở 2 kích thước khác nhau.

---

## Slide 14: Tóm tắt
**Nội dung chính**:
- Mọi chữ trong Text; ảnh URL cần kích thước; safe area để không bị che
- Flexbox mặc định xếp dọc; `flex: 1` lấp đầy
- Theme + component dùng chung = giao diện nhất quán
- AI dựng nhanh, bạn so với thiết kế và sửa
**Hoạt động**: Làm quiz Bài 02 ở cuối trang bài học
