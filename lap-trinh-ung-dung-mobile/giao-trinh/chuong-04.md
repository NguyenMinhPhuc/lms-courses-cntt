# Chương 4. Quản lý trạng thái, danh sách và form

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Phân biệt trạng thái cục bộ, trạng thái toàn cục và dữ liệu từ server.
- Quản lý trạng thái toàn cục bằng Zustand.
- Hiển thị danh sách lớn hiệu quả bằng `FlatList` và `SectionList`.
- Xây dựng form có kiểm tra dữ liệu bằng React Hook Form và Zod.
- Dùng AI sinh quy tắc kiểm tra và tự kiểm chứng bằng giá trị biên.

## 4.1. Ba loại trạng thái

Trạng thái (state) là dữ liệu thay đổi theo thời gian và làm giao diện thay đổi theo. Chọn sai nơi lưu state là nguyên nhân của nhiều lỗi khó tìm [1].

| Loại | Đặc điểm | Ví dụ LHU Food | Công cụ |
|---|---|---|---|
| Cục bộ | Chỉ một màn hình hoặc một component dùng | Số lượng đang chọn, chữ đang gõ trong ô tìm kiếm, modal đang mở | `useState`, `useReducer` |
| Toàn cục (client) | Nhiều màn hình cùng đọc/ghi, chỉ tồn tại trong ứng dụng | Giỏ hàng, thông tin người đăng nhập | Zustand hoặc React Context |
| Từ server | Bản gốc nằm ở SQL Server, ứng dụng chỉ giữ bản sao | Thực đơn, lịch sử đơn hàng | TanStack Query (Chương 5) |

**Quy tắc chọn:** bắt đầu từ `useState`. Chỉ đưa lên toàn cục khi có từ hai màn hình không cha-con cần cùng dữ liệu. Dữ liệu có bản gốc trên server thì không chép vào store toàn cục, mà để TanStack Query quản lý.

### 4.1.1. useReducer cho state có nhiều thao tác

Khi một state có nhiều cách thay đổi, `useReducer` gom logic về một chỗ:

```tsx
type State = { quantity: number };
type Action = { type: 'increase' } | { type: 'decrease' };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increase': return { quantity: state.quantity + 1 };
    case 'decrease': return { quantity: Math.max(1, state.quantity - 1) };
  }
}

const [state, dispatch] = useReducer(reducer, { quantity: 1 });
```

## 4.2. Trạng thái toàn cục với Zustand

### 4.2.1. Vì sao chọn Zustand

Zustand là thư viện quản lý state nhỏ gọn: không cần bọc ứng dụng trong Provider, khai báo store bằng một hàm, và component chỉ vẽ lại khi phần state nó chọn thay đổi. Cài đặt: `npx expo install zustand` [2].

### 4.2.2. Store giỏ hàng

Tham khảo [2].

`stores/cart.ts`:

```ts
import { create } from 'zustand';

export type CartItem = { id: number; name: string; price: number; quantity: number };

type CartState = {
  items: CartItem[];
  add: (product: Omit<CartItem, 'quantity'>) => void;
  decrease: (id: number) => void;
  remove: (id: number) => void;
  clear: () => void;
  total: () => number;
  count: () => number;
};

export const useCart = create<CartState>((set, get) => ({
  items: [],
  add: (product) =>
    set((state) => {
      const found = state.items.find((i) => i.id === product.id);
      return {
        items: found
          ? state.items.map((i) => (i.id === product.id ? { ...i, quantity: i.quantity + 1 } : i))
          : [...state.items, { ...product, quantity: 1 }],
      };
    }),
  decrease: (id) =>
    set((state) => ({
      items: state.items
        .map((i) => (i.id === id ? { ...i, quantity: i.quantity - 1 } : i))
        .filter((i) => i.quantity > 0),
    })),
  remove: (id) => set((state) => ({ items: state.items.filter((i) => i.id !== id) })),
  clear: () => set({ items: [] }),
  total: () => get().items.reduce((sum, i) => sum + i.price * i.quantity, 0),
  count: () => get().items.reduce((sum, i) => sum + i.quantity, 0),
}));
```

### 4.2.3. Nguyên tắc bất biến

Hàm cập nhật **luôn trả về mảng/đối tượng mới** (`map`, `filter`, toán tử spread), không sửa trực tiếp mảng cũ bằng `push` hay gán `items[0].quantity++`. React so sánh tham chiếu để biết state có đổi không; sửa trực tiếp làm giao diện không cập nhật.

### 4.2.4. Đọc store ở màn hình

```tsx
const items = useCart((state) => state.items);
const add = useCart((state) => state.add);
const count = useCart((state) => state.count());
```

Mỗi lần gọi `useCart` chỉ **chọn** phần cần dùng. Màn hình Chi tiết chỉ cần `add` sẽ không vẽ lại khi giỏ hàng thay đổi.

Hiển thị số món trên biểu tượng tab:

```tsx
<Tabs.Screen name="cart" options={{ title: 'Giỏ hàng', tabBarBadge: count > 0 ? count : undefined }} />
```

## 4.3. Danh sách với FlatList

### 4.3.1. Vì sao không dùng ScrollView cho danh sách dài

`ScrollView` dựng toàn bộ phần tử ngay khi hiển thị. `FlatList` là danh sách **ảo hóa (virtualized)**: chỉ dựng phần tử đang nằm trong vùng nhìn thấy và một ít phía trước, phía sau; phần tử cuộn ra khỏi màn hình được giải phóng. Nhờ đó danh sách hàng nghìn phần tử vẫn cuộn mượt và tiết kiệm bộ nhớ.

### 4.3.2. Các thuộc tính chính

Tham khảo [3].

| Thuộc tính | Vai trò |
|---|---|
| `data` | Mảng dữ liệu |
| `renderItem` | Hàm vẽ một phần tử: `({ item, index }) => ...` |
| `keyExtractor` | Trả về khóa duy nhất, ổn định (mã món), không dùng chỉ số mảng |
| `numColumns` | Số cột (lưới); kèm `columnWrapperStyle` để căn mỗi hàng |
| `ListHeaderComponent` / `ListFooterComponent` | Phần đầu, phần cuối danh sách |
| `ListEmptyComponent` | Nội dung khi danh sách rỗng |
| `refreshing`, `onRefresh` | Kéo xuống để tải lại |
| `onEndReached`, `onEndReachedThreshold` | Gọi khi cuộn gần cuối, dùng cho tải thêm |

### 4.3.3. Không lồng FlatList trong ScrollView cùng chiều

Đặt `FlatList` dọc bên trong `ScrollView` dọc làm mất cơ chế ảo hóa và React Native sẽ cảnh báo. Phần nội dung phía trên danh sách (lời chào, ô tìm kiếm, banner) đưa vào `ListHeaderComponent`.

### 4.3.4. SectionList

Tham khảo [4].

`SectionList` hiển thị danh sách chia nhóm có tiêu đề, ví dụ thực đơn theo từng danh mục:

```tsx
<SectionList
  sections={[
    { title: 'Cơm', data: comItems },
    { title: 'Đồ uống', data: drinkItems },
  ]}
  keyExtractor={(item) => String(item.id)}
  renderItem={({ item }) => <ProductRow {...item} />}
  renderSectionHeader={({ section }) => <Text style={styles.header}>{section.title}</Text>}
/>
```

## 4.4. Form với React Hook Form và Zod

### 4.4.1. Vai trò của từng thư viện

- **Zod** mô tả quy tắc dữ liệu bằng một **schema**: kiểu, độ dài, định dạng, thông báo lỗi. Từ schema có thể suy ra kiểu TypeScript bằng `z.infer`.
- **React Hook Form** quản lý giá trị các ô, trạng thái lỗi và việc gửi form, hạn chế vẽ lại không cần thiết.
- **@hookform/resolvers** nối Zod vào React Hook Form.

Cài đặt: `npx expo install react-hook-form zod @hookform/resolvers` [5].

### 4.4.2. Schema đăng ký tài khoản

```ts
import { z } from 'zod';

export const registerSchema = z
  .object({
    fullName: z.string().trim().min(2, 'Họ tên tối thiểu 2 ký tự').max(100, 'Họ tên tối đa 100 ký tự'),
    email: z.string().trim().email('Email không đúng định dạng'),
    phone: z.string().regex(/^0\d{9}$/, 'Số điện thoại gồm 10 chữ số, bắt đầu bằng 0'),
    password: z
      .string()
      .min(8, 'Mật khẩu tối thiểu 8 ký tự')
      .regex(/[A-Za-z]/, 'Mật khẩu phải có chữ cái')
      .regex(/\d/, 'Mật khẩu phải có chữ số'),
    confirm: z.string(),
  })
  .refine((data) => data.password === data.confirm, {
    message: 'Mật khẩu xác nhận không khớp',
    path: ['confirm'],
  });

export type RegisterForm = z.infer<typeof registerSchema>;
```

`.refine` kiểm tra điều kiện liên quan nhiều trường; `path` chỉ định lỗi hiển thị ở ô nào [6].

### 4.4.3. Gắn TextInput bằng Controller

React Native không có thẻ `<input>` với thuộc tính `name`, nên mỗi ô được nối qua `Controller` [5]:

```tsx
const { control, handleSubmit, formState: { errors, isSubmitting } } = useForm<RegisterForm>({
  resolver: zodResolver(registerSchema),
  defaultValues: { fullName: '', email: '', phone: '', password: '', confirm: '' },
});

<Controller
  control={control}
  name="email"
  render={({ field: { onChange, onBlur, value } }) => (
    <TextInput
      value={value}
      onChangeText={onChange}
      onBlur={onBlur}
      keyboardType="email-address"
      autoCapitalize="none"
      placeholder="Email"
    />
  )}
/>
{errors.email && <Text style={{ color: '#DC3545' }}>{errors.email.message}</Text>}

<Button title="Đăng ký" onPress={handleSubmit(onSubmit)} disabled={isSubmitting} />
```

`handleSubmit(onSubmit)` chỉ gọi `onSubmit` khi toàn bộ form hợp lệ; nếu không, lỗi hiện ngay dưới từng ô.

### 4.4.4. Bàn phím trên di động

- Chọn `keyboardType` theo dữ liệu: `email-address`, `phone-pad`, `numeric`.
- `autoCapitalize="none"` cho email và tên đăng nhập.
- Bọc form trong `KeyboardAvoidingView` để bàn phím không che ô đang nhập:

```tsx
<KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
  <ScrollView keyboardShouldPersistTaps="handled">{/* các ô nhập */}</ScrollView>
</KeyboardAvoidingView>
```

### 4.4.5. Kiểm tra ở ứng dụng chưa đủ

Kiểm tra ở ứng dụng giúp người dùng sửa lỗi nhanh, nhưng không bảo vệ được dữ liệu: request có thể được gửi thẳng tới API từ công cụ khác. API (Chương 5, 6) **luôn kiểm tra lại** bằng DTO và stored procedure.

## 4.5. Vibe coding cho quy tắc nghiệp vụ

### 4.5.1. Quy trình

1. Viết đặc tả bằng lời, rõ từng giới hạn.
2. Nhờ trợ lý AI sinh schema Zod với thông báo lỗi tiếng Việt.
3. **Tự lập bảng giá trị biên** và thử từng giá trị.
4. Sửa schema ở chỗ AI sai; ghi prompt và kết quả vào `PROMPTS.md`.

### 4.5.2. Bảng giá trị biên mẫu

| Trường | Giá trị thử | Mong đợi |
|---|---|---|
| Họ tên | "A" (1 ký tự) | Lỗi |
| Họ tên | "An" (2 ký tự) | Hợp lệ |
| Họ tên | "   " (chỉ khoảng trắng) | Lỗi (nhờ `trim`) |
| Số điện thoại | 9 chữ số | Lỗi |
| Số điện thoại | 10 chữ số bắt đầu bằng 0 | Hợp lệ |
| Số điện thoại | 11 chữ số | Lỗi |
| Mật khẩu | 7 ký tự có chữ và số | Lỗi |
| Mật khẩu | 8 ký tự chỉ có chữ | Lỗi |
| Mật khẩu | 8 ký tự có chữ và số | Hợp lệ |

Trợ lý AI thường viết biểu thức chính quy "gần đúng", ví dụ thiếu dấu `^` và `$` nên chuỗi dài hơn vẫn khớp, hoặc quên `trim`. Kỹ thuật phân tích giá trị biên từ học phần Kiểm thử phần mềm phát hiện các lỗi này nhanh.

## 4.6. Chuẩn bị backend cho Chương 5

Trong tuần này, thành viên phụ trách backend của nhóm:

1. Khởi tạo dự án: `npx @nestjs/cli new lhu-food-api`.
2. Cài thư viện: `npm install mssql` và `npm install @nestjs/config`.
3. Tạo file `.env` (không đưa lên Git) chứa `DB_SERVER`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`.
4. Tạo cơ sở dữ liệu và các bảng theo ERD sơ bộ trong SQL Server Management Studio.

## Tóm tắt chương

- Chọn đúng nơi lưu state: cục bộ trước; toàn cục khi nhiều màn hình cần; dữ liệu server để TanStack Query quản lý.
- Zustand: store là một hàm, component chọn phần state cần dùng, luôn cập nhật bất biến.
- `FlatList` ảo hóa danh sách; luôn có `keyExtractor` ổn định và trạng thái rỗng; không lồng trong `ScrollView` cùng chiều.
- React Hook Form + Zod: schema một chỗ, lỗi hiển thị ngay dưới ô, chỉ gửi khi hợp lệ; API vẫn phải kiểm tra lại.
- Mã kiểm tra do AI sinh cần được kiểm chứng bằng bảng giá trị biên.

## Câu hỏi ôn tập

1. Cho ba ví dụ về state cục bộ, hai ví dụ về state toàn cục và hai ví dụ về dữ liệu từ server trong đề tài của nhóm.
2. Vì sao hàm cập nhật trong Zustand phải trả về mảng mới?
3. "Ảo hóa danh sách" nghĩa là gì? Lợi ích của nó?
4. Vì sao không dùng chỉ số mảng làm `keyExtractor`?
5. `.refine` trong Zod dùng trong trường hợp nào?
6. Vì sao đã kiểm tra dữ liệu ở ứng dụng mà API vẫn phải kiểm tra lại?

## Bài tập

1. **Giỏ hàng hoàn chỉnh.** Màn hình Giỏ hàng có nút tăng/giảm số lượng, xóa món, tổng tiền, nút "Đặt hàng" bị vô hiệu khi giỏ trống; badge số món trên tab.
2. **Thực đơn theo danh mục.** Hiển thị thực đơn bằng `SectionList`, mỗi danh mục một nhóm, có ô tìm kiếm trong `ListHeaderComponent` của danh sách.
3. **Form Đăng ký.** Xây form theo mục 4.4.2, nộp kèm bảng giá trị biên đã thử (cột kết quả: đạt/không đạt).

## Tài liệu tham khảo

[1] Meta Platforms, Inc., “Choosing the State Structure,” *React Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react.dev/learn/choosing-the-state-structure

[2] Poimandres, “Introduction,” *Zustand Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://zustand.docs.pmnd.rs

[3] Meta Platforms, Inc., “FlatList,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/flatlist

[4] Meta Platforms, Inc., “SectionList,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/sectionlist

[5] React Hook Form, “Get Started: React Native,” *React Hook Form Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react-hook-form.com/get-started#ReactNative

[6] C. McDonnell, “Intro,” *Zod Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://zod.dev
