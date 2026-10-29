# Bài 10: Kiểm thử, gỡ lỗi & tối ưu hiệu năng
Sprint 4 · Chất lượng sản phẩm

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Viết unit test và component test bằng Jest + React Native Testing Library
- Kiểm thử stored procedure bằng script T-SQL
- Gỡ lỗi bằng React Native DevTools, log, request mạng, sự kiện socket
- Đo và cải thiện hiệu năng; bổ sung accessibility
**Ghi chú giảng viên**:
- 2 tiết lý thuyết, 3 tiết thực hành. CLO1.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Tuần sau một bạn sửa hàm tính tổng tiền. Ai phát hiện nó tính sai?
- Trên điện thoại Android cũ, danh sách món còn cuộn mượt không?
- "Chạy được trên máy em" chưa phải là chất lượng

---

## Slide 3: Các tầng kiểm thử trong đồ án
**Nội dung chính**:
- **Unit test**: hàm, store (giỏ hàng, xác thực), không cần giao diện
- **Component test**: vẽ component, thao tác như người dùng
- **Kiểm thử thủ tục**: script T-SQL trên CSDL kiểm thử
- **Kiểm thử thủ công**: chạy luồng chính trên điện thoại thật
**Ghi chú giảng viên**:
- Liên hệ học phần Kiểm thử phần mềm: test plan, test case, bug report.

---

## Slide 4: Thiết lập Jest cho Expo
**Nội dung chính**:
```bash
npx expo install jest-expo jest @types/jest -- --save-dev
npx expo install @testing-library/react-native -- --save-dev
```
- package.json: preset là jest-expo, script test chạy jest
- File test: thư mục __tests__ hoặc tên *.test.tsx
- Thư viện native (AsyncStorage, SecureStore) phải mock

---

## Slide 5: Unit test cho store giỏ hàng
**Nội dung chính**:
```ts
beforeEach(() => useCart.setState({ items: [] }));

test('thêm trùng món thì cộng dồn', () => {
  useCart.getState().add({ id: 1, name: 'Cơm gà', price: 35000 });
  useCart.getState().add({ id: 1, name: 'Cơm gà', price: 35000 });
  expect(useCart.getState().items[0].quantity).toBe(2);
  expect(useCart.getState().total()).toBe(70000);
});
```
- beforeEach đặt lại state: các test độc lập với nhau

---

## Slide 6: Component test cho ProductCard
**Nội dung chính**:
```tsx
const onAdd = jest.fn();
render(<ProductCard name="Bún bò Huế" price={40000} onAdd={onAdd} />);
expect(screen.getByText('Bún bò Huế')).toBeTruthy();
fireEvent.press(screen.getByText('Thêm vào giỏ'));
expect(onAdd).toHaveBeenCalledTimes(1);
```
- Tìm phần tử theo chữ người dùng thấy hoặc accessibilityLabel
- Test hành vi, không test chi tiết cài đặt

---

## Slide 7: Mock API
**Nội dung chính**:
- jest.mock('@/lib/api') thay hàm gọi mạng bằng hàm giả
- Quy định dữ liệu trả về: danh sách món, lỗi 409
- Test không phụ thuộc server, chạy nhanh, kết quả ổn định
**Hoạt động**: Lớp liệt kê 3 tình huống API cần mock cho màn hình Đặt món

---

## Slide 8: Kiểm thử stored procedure
**Nội dung chính**:
```sql
BEGIN TRY
  EXEC sp_Order_Create @UserId = 1,
       @ItemsJson = N'[{"productId":1,"quantity":2}]';
  PRINT N'FAIL TC-01';
END TRY
BEGIN CATCH
  IF ERROR_NUMBER() = 50409 PRINT N'PASS TC-01';
END CATCH
```
- Chạy trên CSDL kiểm thử riêng, không chạy trên CSDL thật

---

## Slide 9: Thiết kế ca kiểm thử thủ tục
**Nội dung chính**:
- **Hợp lệ**: đặt 1 suất khi còn hàng → tạo đơn, trừ tồn kho
- **Không hợp lệ**: JSON sai, số lượng âm, món đã ngừng bán
- **Biên**: đặt đúng bằng tồn kho; vượt tồn kho 1 đơn vị
- Kiểm tra cả kết quả trả về lẫn mã lỗi THROW

---

## Slide 10: Công cụ gỡ lỗi
**Nội dung chính**:
- **React Native DevTools**: nhấn j trong cửa sổ expo start
- Console, breakpoint, cây component, Profiler
- **RedBox**: đọc dòng stack trace đầu tiên thuộc mã của bạn
- **Mạng**: log URL, mã trạng thái, lỗi trả về; đối chiếu bằng Swagger
- **Socket**: lắng nghe connect_error

---

## Slide 11: Quy trình xử lý một lỗi
**Nội dung chính**:
- 1. Tái hiện: bước, dữ liệu, thiết bị, phiên bản
- 2. Khoanh vùng: app, API, thủ tục hay dữ liệu?
- 3. Viết test tái hiện lỗi (đỏ) → sửa → test xanh
- 4. Ghi bug log: mô tả, mức độ, nguyên nhân, cách sửa, commit

---

## Slide 12: Vẽ lại thừa
**Nội dung chính**:
- State của màn hình cha đổi → mọi component con vẽ lại
- Gõ 1 ký tự tìm kiếm → 200 thẻ món vẽ lại
- **Đo trước khi sửa**: Profiler cho biết component nào vẽ lại, mất bao lâu
**Hoạt động**: Mở Profiler, gõ vào ô tìm kiếm, ghi số lần vẽ lại

---

## Slide 13: React.memo và useCallback
**Nội dung chính**:
```tsx
export const ProductCard = React.memo(function ProductCard(props: Props) {
  // ...
});
const handleAdd = useCallback((item: Product) => add(item), [add]);
```
- memo: chỉ vẽ lại khi props đổi
- useCallback: giữ nguyên hàm giữa các lần vẽ, nếu không memo vô tác dụng

---

## Slide 14: Tối ưu danh sách và ảnh
**Nội dung chính**:
- FlatList: keyExtractor ổn định, initialNumToRender vừa một màn hình
- getItemLayout khi các dòng cao bằng nhau
- Ảnh đúng kích thước từ server; expo-image có bộ nhớ đệm
- Đo ở chế độ gần thật: expo start --no-dev --minify, máy Android tầm trung

---

## Slide 15: Accessibility
**Nội dung chính**:
- Nút chỉ có biểu tượng: accessibilityLabel và accessibilityRole
- Thử bằng TalkBack trên Android
- Tăng cỡ chữ hệ thống: giao diện không được vỡ
- Vùng chạm khoảng 44–48 dp; hitSlop cho biểu tượng nhỏ
- Độ tương phản đủ để đọc ngoài trời

---

## Slide 16: Test do AI sinh có đáng tin?
**Nội dung chính**:
- Copilot sinh test rất nhanh, nhưng test có thể "luôn xanh"
- **Mutation thủ công**: cố ý sửa sai logic, ví dụ đổi nhân thành cộng
- Test vẫn xanh → test vô giá trị → thêm expect
- Ghi prompt sinh test vào PROMPTS.md
**Ghi chú giảng viên**:
- Nhấn mạnh nguyên tắc "không hiểu thì không merge" áp dụng cả cho test.

---

## Slide 17: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: test giỏ hàng, ProductCard, script sp_Order_Create, memo danh sách, accessibilityLabel
- **Không hướng dẫn**: ≥ 5 test cho module tự chọn + mutation thủ công với ≥ 3 lỗi cố ý
- **Nhóm**: test luồng chính, bug log, 1 cải tiến hiệu năng có số liệu trước/sau

---

## Slide 18: Tổng kết
**Nội dung chính**:
- Test tự động bảo vệ mã khỏi lỗi khi sửa sau này
- Thủ tục cũng cần kịch bản kiểm thử
- Đo trước, sửa sau, đo lại
- Buổi sau: triển khai lên server Khoa và build APK
**Ghi chú giảng viên**:
- Nhắc nhóm đăng ký tài khoản Expo và liên hệ bộ phận hỗ trợ lấy thông tin server trước bài 11.
