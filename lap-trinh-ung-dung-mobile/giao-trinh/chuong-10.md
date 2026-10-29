# Chương 10. Kiểm thử, gỡ lỗi và tối ưu hiệu năng

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Thiết lập Jest và React Native Testing Library cho dự án Expo.
- Viết unit test cho logic nghiệp vụ, component test cho giao diện và mock API.
- Kiểm thử stored procedure bằng kịch bản T-SQL với giá trị hợp lệ, không hợp lệ và giá trị biên.
- Gỡ lỗi ứng dụng bằng React Native DevTools, log, request mạng và sự kiện socket; ghi bug log.
- Đo và cải thiện hiệu năng danh sách; bổ sung khả năng truy cập (accessibility).
- Kiểm chứng bộ test do trợ lý AI sinh ra bằng mutation thủ công.

## 10.1. Kiểm thử trong một dự án di động

### 10.1.1. Vì sao cần test tự động

Đến Sprint 4, LHU Food đã có hàng chục màn hình, hàng chục thủ tục và nhiều người cùng sửa mã. Mỗi thay đổi có thể làm hỏng một chức năng đang chạy tốt mà không ai nhận ra cho đến khi demo. Test tự động là các đoạn mã kiểm tra mã khác: chạy trong vài giây, chạy lại mỗi khi sửa, và báo ngay chức năng nào bị hỏng.

Học phần Kiểm thử phần mềm đã giới thiệu test plan, test case và báo cáo lỗi. Chương này áp dụng các khái niệm đó vào ứng dụng di động và backend của nhóm.

### 10.1.2. Các tầng kiểm thử

| Tầng | Kiểm tra gì | Công cụ | Ví dụ trong LHU Food |
|---|---|---|---|
| Unit test | Một hàm hoặc một store, không có giao diện | Jest | Tổng tiền giỏ hàng, hàm định dạng giá |
| Component test | Một component: hiển thị và phản hồi thao tác | React Native Testing Library | `ProductCard` gọi `onAdd` khi bấm nút |
| Kiểm thử thủ tục | Stored procedure với nhiều bộ tham số | Script T-SQL | `sp_Order_Create` chặn đặt quá tồn kho |
| Kiểm thử thủ công | Luồng đầy đủ trên thiết bị thật | Điện thoại Android, kịch bản kiểm thử | Đăng nhập → đặt món → nhận thông báo |
| Kiểm thử đầu-cuối (mở rộng) | Kịch bản thao tác tự động trên emulator | Maestro | Tự động chạy luồng đặt món |

Unit test và component test nhiều, nhanh, rẻ; kiểm thử thủ công ít hơn nhưng không thể bỏ, vì chỉ nó phát hiện được lỗi về quyền, mạng, cảm biến trên thiết bị thật.

## 10.2. Thiết lập Jest cho dự án Expo

### 10.2.1. Cài đặt

Theo hướng dẫn của Expo, dùng preset `jest-expo` (cấu hình sẵn Jest để chạy mã React Native):

```bash
npx expo install jest-expo jest @types/jest -- --save-dev
npx expo install @testing-library/react-native -- --save-dev
```

Thêm vào `package.json`:

```json
{
  "scripts": {
    "test": "jest --watchAll"
  },
  "jest": {
    "preset": "jest-expo",
    "setupFiles": ["./jest.setup.ts"]
  }
}
```

Jest tìm file trong thư mục `__tests__/` hoặc có tên kết thúc bằng `.test.ts`, `.test.tsx`. Chạy `npm test`; Jest theo dõi thay đổi và chạy lại các test liên quan. Muốn chạy một lần (ví dụ trước khi tạo pull request), dùng `npx jest`.

### 10.2.2. Mock thư viện native

Môi trường Jest chạy trên Node.js, không có mã native của Android. Thư viện cần mã native như AsyncStorage (giỏ hàng lưu trữ, Chương 7) phải được thay bằng bản giả. AsyncStorage cung cấp sẵn mock:

`jest.setup.ts`:

```ts
jest.mock('@react-native-async-storage/async-storage', () =>
  require('@react-native-async-storage/async-storage/jest/async-storage-mock'),
);
```

Các module Expo thường được `jest-expo` mock sẵn. Nếu một thư viện báo lỗi kiểu "native module cannot be null" khi chạy test, tra mục testing trong tài liệu của thư viện đó hoặc tự mock bằng `jest.mock(...)`.

## 10.3. Unit test

### 10.3.1. Cấu trúc một test

```ts
test('mô tả hành vi mong đợi', () => {
  // Chuẩn bị (Arrange): dữ liệu, trạng thái ban đầu
  // Thực hiện (Act): gọi hàm cần kiểm tra
  // Khẳng định (Assert): so sánh kết quả với mong đợi
  expect(actual).toBe(expected);
});
```

Một số hàm khẳng định thường dùng:

| Hàm | Ý nghĩa |
|---|---|
| `toBe(x)` | Bằng đúng (so sánh `===`), dùng cho số, chuỗi, boolean |
| `toEqual(obj)` | Bằng về nội dung, dùng cho mảng, đối tượng |
| `toHaveLength(n)` | Mảng hoặc chuỗi có độ dài `n` |
| `toBeTruthy()`, `toBeNull()` | Có giá trị, là `null` |
| `toThrow()` | Hàm ném lỗi |
| `toHaveBeenCalledWith(...)` | Hàm giả được gọi với tham số cho trước |

Tên test nên mô tả **hành vi** bằng ngôn ngữ nghiệp vụ ("thêm trùng món thì cộng dồn số lượng"), để khi test đỏ, người đọc biết ngay quy tắc nào bị vi phạm.

### 10.3.2. Test store giỏ hàng

Store `useCart` (Chương 4, Chương 7) chứa logic quan trọng nhất phía ứng dụng: cộng dồn, giảm, xóa, tính tổng.

`stores/__tests__/cart.test.ts`:

```ts
import { useCart } from '../cart';

const comGa = { id: 1, name: 'Cơm gà', price: 35000 };
const traDao = { id: 2, name: 'Trà đào', price: 20000 };

beforeEach(() => {
  useCart.setState({ items: [] });
});

test('thêm món mới thì số lượng là 1', () => {
  useCart.getState().add(comGa);
  expect(useCart.getState().items).toEqual([{ ...comGa, quantity: 1 }]);
});

test('thêm trùng món thì cộng dồn số lượng', () => {
  useCart.getState().add(comGa);
  useCart.getState().add(comGa);
  expect(useCart.getState().items).toHaveLength(1);
  expect(useCart.getState().items[0].quantity).toBe(2);
});

test('tổng tiền bằng tổng giá nhân số lượng', () => {
  useCart.getState().add(comGa);
  useCart.getState().add(comGa);
  useCart.getState().add(traDao);
  expect(useCart.getState().total()).toBe(90000);
  expect(useCart.getState().count()).toBe(3);
});

test('giảm số lượng về 0 thì xóa món khỏi giỏ', () => {
  useCart.getState().add(traDao);
  useCart.getState().decrease(2);
  expect(useCart.getState().items).toEqual([]);
});

test('xóa một món không ảnh hưởng món khác', () => {
  useCart.getState().add(comGa);
  useCart.getState().add(traDao);
  useCart.getState().remove(1);
  expect(useCart.getState().items.map((i) => i.id)).toEqual([2]);
});
```

Store Zustand là một biến dùng chung cho cả file test. Nếu không đặt lại trong `beforeEach`, món thêm ở test trước còn lại ở test sau, và kết quả phụ thuộc thứ tự chạy. **Mỗi test phải độc lập.**

### 10.3.3. Tách logic ra hàm thuần

Logic nằm lẫn trong component (tính phí, kiểm tra giờ mở cửa, định dạng ngày) khó test vì phải vẽ cả màn hình. Tách thành hàm thuần (chỉ phụ thuộc tham số, không đọc state hay gọi mạng) trong `lib/`:

```ts
// lib/format.ts
export function formatPrice(value: number) {
  return value.toLocaleString('vi-VN') + ' đ';
}

// lib/__tests__/format.test.ts
import { formatPrice } from '../format';

test('định dạng giá theo kiểu Việt Nam', () => {
  expect(formatPrice(35000)).toBe('35.000 đ');
});
```

Kết quả định dạng số phụ thuộc dữ liệu ngôn ngữ của môi trường chạy. Nếu test này đỏ trên máy một thành viên nhưng xanh trên máy khác, đó là dấu hiệu môi trường khác nhau, không phải lỗi của hàm.

## 10.4. Component test

### 10.4.1. Nguyên tắc của React Native Testing Library

React Native Testing Library vẽ component trong môi trường test và cho phép tìm phần tử, thao tác **như người dùng**:

- Tìm theo chữ hiển thị (`getByText`), theo nhãn accessibility (`getByLabelText`), theo vai trò (`getByRole`).
- Thao tác bằng `fireEvent.press`, `fireEvent.changeText`.
- Kiểm tra thứ người dùng thấy, không kiểm tra state bên trong hay tên biến.

Test viết theo cách này vẫn đúng khi bạn đổi cách cài đặt bên trong (đổi `useState` sang Zustand chẳng hạn), miễn là hành vi không đổi.

### 10.4.2. Test `ProductCard`

`components/__tests__/ProductCard.test.tsx`:

```tsx
import { render, screen, fireEvent } from '@testing-library/react-native';
import { ProductCard } from '../ProductCard';

test('hiển thị tên và giá món', () => {
  render(<ProductCard name="Bún bò Huế" price={40000} onAdd={() => {}} />);
  expect(screen.getByText('Bún bò Huế')).toBeTruthy();
  expect(screen.getByText(/40.000/)).toBeTruthy();
});

test('bấm "Thêm vào giỏ" thì gọi onAdd đúng một lần', () => {
  const onAdd = jest.fn();
  render(<ProductCard name="Bún bò Huế" price={40000} onAdd={onAdd} />);
  fireEvent.press(screen.getByText('Thêm vào giỏ'));
  expect(onAdd).toHaveBeenCalledTimes(1);
});
```

`jest.fn()` tạo **hàm giả** ghi lại số lần và tham số được gọi. Test không cần biết `onAdd` thật làm gì, chỉ cần biết component gọi nó đúng lúc.

### 10.4.3. Mock API cho màn hình có gọi mạng

Màn hình Trang chủ gọi API qua `lib/api` (Chương 5) và TanStack Query. Test không được gọi server thật: chậm, phụ thuộc mạng, dữ liệu thay đổi. Thay module `api` bằng bản giả:

`app/__tests__/home.test.tsx`:

```tsx
import { render, screen } from '@testing-library/react-native';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { api } from '@/lib/api';
import HomeScreen from '../(tabs)/index';

jest.mock('@/lib/api');
const mockedApi = api as jest.MockedFunction<typeof api>;

function renderWithQuery(ui: React.ReactElement) {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(<QueryClientProvider client={client}>{ui}</QueryClientProvider>);
}

test('hiển thị danh sách món lấy từ API', async () => {
  mockedApi.mockResolvedValue([{ productId: 1, name: 'Cơm gà', price: 35000 }]);
  renderWithQuery(<HomeScreen />);
  expect(await screen.findByText('Cơm gà')).toBeTruthy();
});

test('hiển thị thông báo khi API lỗi', async () => {
  mockedApi.mockRejectedValue(new Error('Network request failed'));
  renderWithQuery(<HomeScreen />);
  expect(await screen.findByText(/Không tải được thực đơn/)).toBeTruthy();
});
```

- `findByText` (có `find`) **chờ** phần tử xuất hiện, dùng cho dữ liệu tải bất đồng bộ; `getByText` tìm ngay lập tức.
- Tắt `retry` của TanStack Query trong test, nếu không truy vấn lỗi sẽ thử lại nhiều lần và test chạy chậm.
- Màn hình dùng Expo Router (`useRouter`, `Link`) có thể cần mock thêm router; xem mục testing trong tài liệu Expo Router.
- Đường dẫn import và chữ hiển thị trong ví dụ cần chỉnh theo đúng cấu trúc dự án của nhóm.

## 10.5. Kiểm thử stored procedure

### 10.5.1. CSDL kiểm thử

Logic dữ liệu quan trọng nhất (kiểm tra tồn kho, giao dịch, phân quyền theo người dùng) nằm trong stored procedure, nên thủ tục cũng phải có test. Không chạy test trên CSDL mà cả nhóm đang dùng: test sửa dữ liệu (đặt tồn kho, tạo đơn).

Tạo một CSDL riêng `LhuFood_Test` bằng chính các script trong `database/` (Chương 7). Đây cũng là cách kiểm tra script dựng lại được CSDL từ đầu.

### 10.5.2. Thiết kế ca kiểm thử

Áp dụng kỹ thuật phân lớp tương đương và giá trị biên cho `sp_Order_Create`:

| Mã | Loại | Dữ liệu vào | Kết quả mong đợi |
|---|---|---|---|
| TC-01 | Hợp lệ | Món còn 5 suất, đặt 2 | Tạo đơn, tồn kho còn 3 |
| TC-02 | Biên | Món còn 1 suất, đặt 1 | Tạo đơn, tồn kho về 0 |
| TC-03 | Biên | Món còn 1 suất, đặt 2 | Lỗi 50409, không tạo đơn, tồn kho giữ nguyên |
| TC-04 | Không hợp lệ | `@ItemsJson` không phải JSON | Lỗi 50400 |
| TC-05 | Không hợp lệ | Số lượng bằng 0 hoặc âm | Lỗi 50400, không tạo đơn |
| TC-06 | Không hợp lệ | Món đã ngừng bán | Lỗi 50409 |

Mỗi ca kiểm tra **cả** kết quả (đơn được tạo hay không, tồn kho) **và** mã lỗi, vì `DatabaseService` (Chương 5) dựa vào mã lỗi để trả HTTP 400/404/409 cho ứng dụng.

### 10.5.3. Kịch bản T-SQL

`database/tests/test-order-create.sql`:

```sql
USE LhuFood_Test;
SET NOCOUNT ON;

-- Chuẩn bị
UPDATE Products SET Stock = 1, IsAvailable = 1 WHERE ProductId = 1;
DECLARE @orders INT;

-- TC-03: đặt quá tồn kho
SET @orders = (SELECT COUNT(*) FROM Orders);
BEGIN TRY
  EXEC sp_Order_Create @UserId = 1, @ItemsJson = N'[{"productId":1,"quantity":2}]';
  PRINT N'FAIL TC-03: không báo lỗi';
END TRY
BEGIN CATCH
  IF ERROR_NUMBER() = 50409
     AND (SELECT COUNT(*) FROM Orders) = @orders
     AND (SELECT Stock FROM Products WHERE ProductId = 1) = 1
    PRINT N'PASS TC-03';
  ELSE
    PRINT N'FAIL TC-03: ' + CAST(ERROR_NUMBER() AS NVARCHAR) + N' ' + ERROR_MESSAGE();
END CATCH;

-- TC-04: JSON không hợp lệ
BEGIN TRY
  EXEC sp_Order_Create @UserId = 1, @ItemsJson = N'không phải json';
  PRINT N'FAIL TC-04: không báo lỗi';
END TRY
BEGIN CATCH
  IF ERROR_NUMBER() = 50400 PRINT N'PASS TC-04';
  ELSE PRINT N'FAIL TC-04: ' + ERROR_MESSAGE();
END CATCH;

-- TC-02: đặt đúng bằng tồn kho
EXEC sp_Order_Create @UserId = 1, @ItemsJson = N'[{"productId":1,"quantity":1}]';
IF (SELECT Stock FROM Products WHERE ProductId = 1) = 0
  PRINT N'PASS TC-02';
ELSE
  PRINT N'FAIL TC-02';
```

Chạy bằng SQL Server Management Studio hoặc `sqlcmd -S localhost -d LhuFood_Test -i database/tests/test-order-create.sql`. Kết quả chỉ gồm các dòng `PASS`/`FAIL`, dễ đọc và dễ dán vào báo cáo. Thứ tự ca trong script có chủ đích: TC-03 và TC-04 chạy trước khi TC-02 làm tồn kho về 0.

Khi một thành viên sửa thủ tục, chạy lại script trước khi tạo pull request. Mã kiểm thử nằm trong `database/tests/`, không nằm trong các script `01`–`99` dựng CSDL, để không bao giờ chạy nhầm trên server thật.

## 10.6. Gỡ lỗi

### 10.6.1. Công cụ

- **React Native DevTools:** trong cửa sổ `npx expo start`, nhấn `j` để mở. Có Console (log của ứng dụng), Sources (đặt breakpoint, chạy từng dòng), Components (cây component và props), Profiler (đo thời gian vẽ).
- **Màn hình đỏ (RedBox) và vàng (LogBox):** màn hình đỏ là lỗi làm dừng ứng dụng; đọc thông báo lỗi và dòng đầu tiên của stack trace **thuộc mã của bạn**, bỏ qua các dòng trong `node_modules`. Cảnh báo vàng không làm dừng ứng dụng nhưng không nên bỏ qua.
- **Log của backend:** cửa sổ chạy NestJS hiển thị request và exception; lỗi từ SQL Server kèm mã lỗi.
- **Swagger:** gọi lại đúng request mà ứng dụng gửi để biết lỗi ở ứng dụng hay ở API.

### 10.6.2. Gỡ lỗi mạng và socket

Thêm log có kiểm soát ở `lib/api.ts` khi đang phát triển:

```ts
if (!res.ok) {
  const body = await res.json().catch(() => ({}));
  if (__DEV__) console.warn('[API]', init?.method ?? 'GET', path, res.status, body);
  // ... ném lỗi như Chương 5
}
```

`__DEV__` chỉ đúng khi chạy chế độ phát triển, nên log không xuất hiện ở bản phát hành. Không log token hay mật khẩu (Chương 6).

Với Socket.IO (Chương 9), lắng nghe sự kiện lỗi kết nối để biết nguyên nhân:

```ts
socket.on('connect_error', (err) => {
  if (__DEV__) console.warn('[Socket]', err.message);
});
```

Các nguyên nhân thường gặp: sai địa chỉ (vẫn trỏ `localhost` trên điện thoại), token hết hạn bị gateway từ chối, khác phiên bản chính giữa client và server, mạng chặn cổng.

### 10.6.3. Quy trình xử lý một lỗi

1. **Tái hiện.** Ghi lại các bước, dữ liệu, thiết bị, phiên bản Android, bản build. Lỗi không tái hiện được thì gần như không sửa được.
2. **Khoanh vùng.** Đi qua từng ranh giới: ứng dụng gửi đúng request chưa? API nhận và gọi đúng thủ tục chưa? Thủ tục trả đúng dữ liệu chưa? Mỗi câu trả lời loại bỏ một nửa khả năng.
3. **Viết test tái hiện lỗi.** Test phải **đỏ** với mã hiện tại.
4. **Sửa mã,** chạy lại: test chuyển xanh và các test cũ vẫn xanh.
5. **Ghi bug log** và commit kèm mã lỗi.

`docs/bug-log.md`:

```markdown
## BUG-07: Tổng tiền sai khi giảm số lượng
- Ngày phát hiện: 2026-05-12 · Người phát hiện: Trần Thị B · Mức độ: Cao
- Tái hiện: thêm 2 Cơm gà → giảm 1 → tổng vẫn 70.000 đ
- Nguyên nhân: decrease sửa trực tiếp mảng items, giao diện không cập nhật
- Cách sửa: dùng map/filter trả mảng mới; thêm test "giảm số lượng cập nhật tổng tiền"
- Commit: a1b2c3d
```

Bug log là minh chứng cho phần kiểm thử trong báo cáo đồ án và cho vai trò của từng thành viên (CLO4).

## 10.7. Tối ưu hiệu năng

### 10.7.1. Ứng dụng chậm vì đâu

Mỗi lần state của một component đổi, React vẽ lại component đó **và toàn bộ component con**, kể cả khi props của con không đổi. Với màn hình Trang chủ có ô tìm kiếm và danh sách 200 món, mỗi ký tự gõ vào có thể làm 200 thẻ món vẽ lại. Trên máy mạnh không thấy, trên máy Android tầm trung thì gõ chữ bị giật.

Các nguyên nhân phổ biến khác: ảnh quá lớn, danh sách không dùng `FlatList`, tính toán nặng trong mỗi lần vẽ, log quá nhiều.

### 10.7.2. Đo trước khi sửa

Không tối ưu theo cảm giác. Dùng **Profiler** trong React Native DevTools:

1. Bấm ghi (record), thực hiện thao tác chậm (gõ 5 ký tự vào ô tìm kiếm), dừng ghi.
2. Xem component nào được vẽ lại, bao nhiêu lần, mỗi lần mất bao lâu.
3. Ghi số liệu vào bảng **trước**; sửa; đo lại và ghi số liệu **sau**.

Chế độ phát triển chậm hơn bản phát hành nhiều lần. Khi cần số liệu gần thực tế, chạy `npx expo start --no-dev --minify` và đo trên điện thoại thật.

### 10.7.3. `React.memo` và `useCallback`

```tsx
// components/ProductCard.tsx
import React from 'react';

export const ProductCard = React.memo(function ProductCard({ name, price, onAdd }: Props) {
  // ... như Chương 1
});
```

`React.memo` bỏ qua việc vẽ lại nếu props không đổi (so sánh nông từng prop). Nhưng nếu màn hình cha truyền `onAdd={() => add(item)}`, mỗi lần vẽ tạo ra **một hàm mới**, props luôn "đổi" và memo vô tác dụng. Giữ nguyên tham chiếu bằng `useCallback`:

```tsx
const add = useCart((s) => s.add);

const renderItem = useCallback(
  ({ item }: { item: Product }) => (
    <ProductItem product={item} onAdd={add} />
  ),
  [add],
);
```

Ở đây `ProductItem` là component đã bọc `React.memo`, nhận cả đối tượng `product` và tự gọi `onAdd(product)` khi bấm. Hàm `add` của Zustand là tham chiếu ổn định, nên thẻ chỉ vẽ lại khi dữ liệu món thay đổi.

Đừng bọc `memo` cho mọi component: so sánh props cũng tốn chi phí. Chỉ dùng cho component vẽ nhiều lần (thẻ trong danh sách) hoặc vẽ tốn kém, và chỉ sau khi Profiler cho thấy cần.

### 10.7.4. Tối ưu `FlatList`

| Thuộc tính | Tác dụng |
|---|---|
| `keyExtractor={(item) => String(item.productId)}` | Khóa ổn định giúp React nhận ra phần tử nào đổi |
| `initialNumToRender` | Số phần tử vẽ lần đầu; vừa đủ một màn hình (khoảng 8–10) |
| `windowSize` | Số "màn hình" giữ trong bộ nhớ quanh vùng đang xem; giảm để tiết kiệm bộ nhớ |
| `getItemLayout` | Khai báo chiều cao cố định của dòng, FlatList không phải đo từng dòng |
| `onEndReached` + phân trang | Tải thêm khi cuộn gần cuối (Chương 4, Chương 5), không tải 1.000 món một lần |

### 10.7.5. Ảnh

- Server trả ảnh có kích thước gần với kích thước hiển thị; không dùng ảnh 4000×3000 cho thẻ 80×80.
- Ảnh người dùng chụp nên được nén trước khi tải lên (Chương 8 dùng tham số `quality` của ImagePicker).
- Thư viện `expo-image` có bộ nhớ đệm trên đĩa và hiệu ứng chuyển ảnh, thay thế được `Image` mặc định với cú pháp tương tự.

### 10.7.6. Phía backend

Ứng dụng chậm có thể do API chậm. Kiểm tra thời gian phản hồi trong Swagger hoặc log; với thủ tục chậm, xem lại chỉ mục (Chương 7) và phân trang. Đo thời gian chạy thủ tục bằng `SET STATISTICS TIME ON` trong SQL Server Management Studio.

## 10.8. Khả năng truy cập (accessibility)

Ứng dụng tốt phải dùng được cho cả người khiếm thị, người lớn tuổi dùng cỡ chữ lớn, người dùng ngoài trời nắng. React Native cung cấp các thuộc tính accessibility ánh xạ sang TalkBack trên Android:

```tsx
<Pressable
  onPress={toggleFavorite}
  accessibilityRole="button"
  accessibilityLabel={isFavorite ? 'Bỏ khỏi yêu thích' : 'Thêm vào yêu thích'}
  hitSlop={12}
>
  <Ionicons name={isFavorite ? 'heart' : 'heart-outline'} size={24} />
</Pressable>
```

Danh sách kiểm tra:

- **Nút chỉ có biểu tượng** phải có `accessibilityLabel`; TalkBack đọc nhãn này thay cho biểu tượng.
- **Vai trò:** `accessibilityRole` (`button`, `link`, `header`, `image`) giúp TalkBack đọc đúng loại phần tử.
- **Cỡ chữ hệ thống:** bật cỡ chữ lớn nhất trong cài đặt Android, kiểm tra chữ không bị cắt, nút không chồng lên nhau. Tránh đặt chiều cao cố định cho vùng chứa chữ.
- **Vùng chạm:** tối thiểu khoảng 44–48 dp; mở rộng vùng chạm của biểu tượng nhỏ bằng `hitSlop`.
- **Độ tương phản:** chữ xám nhạt trên nền trắng khó đọc ngoài trời; không chỉ dùng màu để truyền tải thông tin (ví dụ trạng thái đơn nên có cả chữ, không chỉ chấm màu).

Nhãn accessibility còn có lợi cho kiểm thử: `screen.getByLabelText('Thêm vào yêu thích')` tìm đúng nút mà không phụ thuộc biểu tượng.

## 10.9. Test do trợ lý AI sinh ra

### 10.9.1. Lợi ích và rủi ro

GitHub Copilot Chat và Google Antigravity sinh test rất nhanh: chọn file, yêu cầu "viết test Jest cho store này, gồm trường hợp biên". Đây là cách dùng AI hiệu quả, nhưng test do AI sinh hay mắc các lỗi:

- Khẳng định quá yếu: `expect(result).toBeTruthy()` đúng với hầu hết mọi giá trị.
- Tính kết quả mong đợi bằng chính logic cần kiểm tra (copy công thức từ mã nguồn vào test), nên mã sai thì test cũng sai theo.
- Mock quá nhiều, đến mức test chỉ kiểm tra bản mock.
- Bỏ sót trường hợp biên quan trọng của nghiệp vụ (giảm về 0, giỏ trống).

### 10.9.2. Mutation thủ công

Cách đơn giản để biết một bộ test có giá trị: **cố ý làm sai mã và xem test có bắt được không**.

1. Chọn một chỗ trong logic, sửa sai có chủ đích. Ví dụ trong `total()`: đổi `i.price * i.quantity` thành `i.price + i.quantity`; trong `decrease`: bỏ `.filter((i) => i.quantity > 0)`.
2. Chạy test. Ít nhất một test phải **đỏ**.
3. Nếu tất cả vẫn xanh, bộ test không bảo vệ được logic đó: bổ sung test hoặc khẳng định cho đến khi bản sai bị bắt.
4. Hoàn lại mã đúng.

| Lỗi cố ý | Test bắt được | Bổ sung |
|---|---|---|
| `price + quantity` trong `total` | "tổng tiền bằng tổng giá nhân số lượng" | |
| Bỏ `filter` trong `decrease` | Không có | Thêm test "giảm về 0 thì xóa món" |
| `add` luôn thêm dòng mới | "thêm trùng món thì cộng dồn" | |

Bảng này là sản phẩm của bài thực hành không hướng dẫn buổi 10. Ghi prompt sinh test vào `PROMPTS.md` cùng nhận xét: AI bỏ sót trường hợp nào.

## 10.10. Mã nguồn bổ sung của chương

```text
lhu-food/
├── jest.setup.ts
├── lib/__tests__/format.test.ts
├── stores/__tests__/cart.test.ts
├── components/__tests__/ProductCard.test.tsx
└── app/__tests__/home.test.tsx

lhu-food-api/
└── database/tests/test-order-create.sql

docs/
└── bug-log.md
```

## Tóm tắt chương

- Test tự động giúp phát hiện ngay chức năng bị hỏng khi sửa mã; kết hợp unit test, component test, kiểm thử thủ tục và kiểm thử thủ công trên thiết bị thật.
- Dự án Expo dùng preset `jest-expo`; thư viện native như AsyncStorage phải được mock.
- Unit test kiểm tra store và hàm thuần; mỗi test độc lập nhờ `beforeEach`.
- Component test tìm phần tử và thao tác như người dùng; mock API để không phụ thuộc server.
- Stored procedure được kiểm thử bằng kịch bản T-SQL trên CSDL kiểm thử riêng, kiểm tra cả kết quả lẫn mã lỗi.
- Gỡ lỗi theo quy trình: tái hiện, khoanh vùng, viết test đỏ, sửa, ghi bug log.
- Tối ưu hiệu năng phải đo trước và sau; `React.memo` chỉ có tác dụng khi props giữ nguyên tham chiếu.
- Accessibility: nhãn, vai trò, cỡ chữ hệ thống, vùng chạm, độ tương phản.
- Test do AI sinh phải được kiểm chứng bằng mutation thủ công.

## Câu hỏi ôn tập

1. Nêu sự khác nhau giữa unit test, component test và kiểm thử thủ công. Mỗi loại phát hiện được lỗi gì mà loại khác không phát hiện được?
2. Vì sao cần mock AsyncStorage và `lib/api` khi chạy Jest?
3. Điều gì xảy ra nếu không đặt lại store giỏ hàng trong `beforeEach`?
4. `getByText` và `findByText` khác nhau thế nào? Khi nào phải dùng `findByText`?
5. Vì sao kịch bản kiểm thử `sp_Order_Create` phải kiểm tra cả mã lỗi lẫn số đơn trong bảng `Orders`?
6. Giải thích vì sao `React.memo` không có tác dụng khi truyền một hàm mũi tên mới làm prop.
7. Nêu ba lỗi thường gặp của test do AI sinh ra và cách phát hiện bằng mutation thủ công.

## Bài tập

1. **Test cho module tự chọn.** Chọn một module của đề tài (form đăng ký với Zod, store xác thực, hàm tính khoảng cách…). Viết ít nhất 5 test; thực hiện mutation thủ công với ít nhất 3 lỗi cố ý và lập bảng kết quả như mục 10.9.2.
2. **Kịch bản kiểm thử thủ tục.** Viết bảng ca kiểm thử và script T-SQL cho thủ tục hủy đơn (Chương 7): hủy đơn của mình khi chưa chuẩn bị, hủy đơn của người khác, hủy đơn đã chuẩn bị; kiểm tra tồn kho được hoàn lại.
3. **Cải tiến hiệu năng.** Dùng Profiler đo một màn hình danh sách của đề tài, áp dụng ít nhất một kỹ thuật ở mục 10.7, ghi bảng số liệu trước/sau vào báo cáo.
4. **Kiểm tra accessibility.** Bật TalkBack và cỡ chữ lớn nhất, đi qua luồng chính của ứng dụng; ghi các vấn đề tìm được vào bug log và sửa ít nhất 3 vấn đề.

## Tài liệu tham khảo

- Expo - Unit testing with Jest: https://docs.expo.dev/develop/unit-testing/
- React Native Testing Library: https://callstack.github.io/react-native-testing-library/
- Jest - Expect: https://jestjs.io/docs/expect
- Jest - Mock functions: https://jestjs.io/docs/mock-functions
- React Native - Debugging: https://reactnative.dev/docs/debugging
- React Native - Performance overview: https://reactnative.dev/docs/performance
- React Native - Optimizing FlatList configuration: https://reactnative.dev/docs/optimizing-flatlist-configuration
- React Native - Accessibility: https://reactnative.dev/docs/accessibility
- React - memo: https://react.dev/reference/react/memo
- React - useCallback: https://react.dev/reference/react/useCallback
- AsyncStorage - Jest integration: https://react-native-async-storage.github.io/async-storage/docs/advanced/jest
