# Chương 2. Core Components, Styling và Layout với Flexbox

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Sử dụng đúng các core component của React Native.
- Dựng bố cục bằng Flexbox, hiển thị đúng trên nhiều kích thước màn hình.
- Xây dựng design system gồm theme và component dùng chung.
- Chuyển thiết kế Figma thành mã bằng vibe coding và kiểm tra lại kết quả.
- Trình bày sơ đồ chức năng của ứng dụng bằng công cụ đồ họa.

## 2.1. Core components

React Native cung cấp một nhóm component cơ bản (core components). Mọi giao diện, dù phức tạp, đều được ghép từ các component này.

### 2.1.1. View và Text

`View` là khung chứa, tương tự `div`. `Text` hiển thị chữ và là nơi duy nhất được đặt chuỗi ký tự. Một vài thuộc tính hữu ích của `Text`:

- `numberOfLines={2}`: cắt chữ quá dài, thêm dấu "…".
- `selectable`: cho phép người dùng chọn và sao chép chữ.
- Style của `Text` cha được kế thừa bởi `Text` con lồng bên trong; đây là trường hợp kế thừa style duy nhất trong React Native.

```tsx
<Text style={{ fontSize: 16 }}>
  Giá: <Text style={{ fontWeight: 'bold' }}>35.000 đ</Text>
</Text>
```

### 2.1.2. Image

```tsx
// Ảnh trong dự án: kích thước lấy từ file ảnh
<Image source={require('@/assets/images/logo.png')} />

// Ảnh từ URL: bắt buộc khai báo kích thước
<Image source={{ uri: product.imageUrl }} style={{ width: '100%', height: 180 }} resizeMode="cover" />
```

`resizeMode` quyết định cách ảnh lấp khung: `cover` (lấp đầy, có thể cắt bớt), `contain` (vừa khung, có thể có khoảng trống).

### 2.1.3. ScrollView

`ScrollView` cho phép cuộn nội dung dài hơn màn hình. `ScrollView` vẽ toàn bộ nội dung bên trong ngay khi hiển thị, nên chỉ phù hợp với nội dung có độ dài giới hạn như trang chi tiết hoặc form. Danh sách dài dùng `FlatList` (Chương 4).

### 2.1.4. TextInput

```tsx
<TextInput
  value={keyword}
  onChangeText={setKeyword}
  placeholder="Tìm món..."
  keyboardType="default"       // 'email-address', 'phone-pad', 'numeric'...
  returnKeyType="search"
  autoCapitalize="none"
/>
```

Với ô mật khẩu, dùng `secureTextEntry` để ẩn ký tự.

### 2.1.5. Pressable

`Pressable` biến bất kỳ vùng nào thành vùng bấm được. Thuộc tính `style` có thể nhận một hàm để đổi giao diện khi đang bấm:

```tsx
<Pressable
  onPress={onAdd}
  style={({ pressed }) => [styles.button, pressed && { opacity: 0.7 }]}
  hitSlop={8}
>
  <Text style={styles.buttonText}>Thêm vào giỏ</Text>
</Pressable>
```

`hitSlop` mở rộng vùng nhận chạm ra ngoài khung nhìn thấy, giúp nút nhỏ dễ bấm hơn.

### 2.1.6. Vùng an toàn

Điện thoại hiện nay có tai thỏ, camera đục lỗ, thanh trạng thái và thanh điều hướng cử chỉ. Nội dung đặt sát mép trên hoặc dưới có thể bị che. Dùng `SafeAreaView` của thư viện `react-native-safe-area-context` (có sẵn trong dự án Expo):

```tsx
import { SafeAreaView } from 'react-native-safe-area-context';

export default function ProfileScreen() {
  return (
    <SafeAreaView style={{ flex: 1 }} edges={['top']}>
      {/* nội dung */}
    </SafeAreaView>
  );
}
```

`edges` chọn cạnh cần chừa khoảng an toàn. Màn hình nằm trong Stack có thanh tiêu đề thường không cần cạnh `top`.

## 2.2. Flexbox trong React Native

### 2.2.1. Khác biệt so với CSS trên web

React Native dùng Flexbox để bố cục, với một số mặc định khác web:

| Thuộc tính | Mặc định trên web | Mặc định trên React Native |
|---|---|---|
| `flexDirection` | `row` | `column` |
| `alignContent` | `stretch` | `flex-start` |
| `flexShrink` | `1` | `0` |
| Đơn vị kích thước | px, %, rem… | Số không đơn vị (dp) hoặc phần trăm |

**dp (density-independent pixel)** là đơn vị độc lập mật độ điểm ảnh. `padding: 16` hiển thị gần như cùng kích thước vật lý trên máy màn hình thường và máy màn hình mật độ cao.

### 2.2.2. Các thuộc tính chính

- `flex: 1`: chiếm toàn bộ không gian còn lại theo trục chính. Màn hình gốc thường có `flex: 1` để phủ kín.
- `justifyContent`: căn theo trục chính (`flex-start`, `center`, `space-between`…).
- `alignItems`: căn theo trục phụ (`stretch`, `center`, `flex-start`…).
- `flexWrap: 'wrap'`: cho phép phần tử xuống dòng khi hết chỗ.
- `gap`, `rowGap`, `columnGap`: khoảng cách giữa các phần tử con.
- `position: 'absolute'` cùng `top`, `bottom`, `left`, `right`: đặt phần tử nổi, ví dụ nút cố định ở cuối màn hình.

### 2.2.3. Ví dụ: màn hình Chi tiết món

```tsx
<View style={{ flex: 1 }}>
  <ScrollView contentContainerStyle={{ paddingBottom: 96 }}>
    <Image source={{ uri: product.imageUrl }} style={{ width: '100%', height: 240 }} />
    <View style={{ padding: 16, gap: 8 }}>
      <Text style={{ fontSize: 22, fontWeight: 'bold' }}>{product.name}</Text>
      <Text style={{ fontSize: 18, color: '#013D88' }}>{product.price.toLocaleString('vi-VN')} đ</Text>
      <Text>{product.description}</Text>
    </View>
  </ScrollView>
  <View style={{ position: 'absolute', left: 16, right: 16, bottom: 16 }}>
    <Button title="Thêm vào giỏ" onPress={onAdd} />
  </View>
</View>
```

`paddingBottom: 96` chừa chỗ để nội dung cuối cùng không bị nút cố định che mất.

### 2.2.4. Bố cục theo kích thước màn hình

Hook `useWindowDimensions()` trả về `width` và `height` hiện tại, tự cập nhật khi xoay màn hình. Dùng nó để đổi số cột, cỡ ảnh hoặc ẩn bớt thành phần trên màn hình nhỏ:

```tsx
const { width } = useWindowDimensions();
const columns = width >= 600 ? 3 : 2;
const itemWidth = (width - 16 * (columns + 1)) / columns;
```

## 2.3. Design system: theme và component dùng chung

### 2.3.1. Vì sao cần theme

Nếu mã màu `#013D88` xuất hiện ở hai mươi file, mỗi lần đổi màu chủ đạo bạn phải sửa hai mươi chỗ, và chắc chắn sẽ sót. Gom các giá trị thiết kế về một file giúp:

- Đổi một chỗ, cả ứng dụng thay đổi theo.
- Giao diện nhất quán giữa các thành viên trong nhóm.
- Trợ lý AI sinh mã đúng màu và khoảng cách khi `AGENTS.md` yêu cầu dùng theme.

### 2.3.2. File theme

`constants/theme.ts`:

```ts
export const colors = {
  primary: '#013D88',
  primaryDark: '#01295C',
  accent: '#FFC627',
  text: '#212529',
  muted: '#6C757D',
  border: '#DEE2E6',
  background: '#F8F9FA',
  surface: '#FFFFFF',
  danger: '#DC3545',
};

export const spacing = { xs: 4, sm: 8, md: 16, lg: 24, xl: 32 };
export const radius = { sm: 6, md: 12, lg: 20 };
export const fontSize = { caption: 12, body: 16, title: 20, heading: 24 };
```

### 2.3.3. Chế độ sáng và tối

`useColorScheme()` trả về `'light'` hoặc `'dark'` theo cài đặt của máy. Có thể khai báo hai bảng màu và chọn theo kết quả này. Khi bật hỗ trợ chế độ tối, hãy kiểm tra độ tương phản của chữ trên nền ở cả hai chế độ.

### 2.3.4. Component dùng chung

`components/Button.tsx`:

```tsx
import { Pressable, StyleSheet, Text } from 'react-native';
import { colors, radius, spacing, fontSize } from '@/constants/theme';

type Props = {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
};

export function Button({ title, onPress, variant = 'primary', disabled }: Props) {
  const isPrimary = variant === 'primary';
  return (
    <Pressable
      onPress={onPress}
      disabled={disabled}
      style={({ pressed }) => [
        styles.base,
        isPrimary ? styles.primary : styles.secondary,
        (pressed || disabled) && { opacity: 0.6 },
      ]}
    >
      <Text style={[styles.text, { color: isPrimary ? '#fff' : colors.primary }]}>{title}</Text>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  base: { paddingVertical: spacing.md, borderRadius: radius.md, alignItems: 'center' },
  primary: { backgroundColor: colors.primary },
  secondary: { backgroundColor: colors.surface, borderWidth: 1, borderColor: colors.primary },
  text: { fontSize: fontSize.body, fontWeight: '600' },
});
```

Theo cùng cách, nhóm xây `Card` (khung bo góc có bóng nhẹ), `Input` (có nhãn và dòng báo lỗi), `Badge`, `EmptyState`. Bộ component này là **UI kit** của dự án.

## 2.4. Từ Figma đến mã bằng vibe coding

### 2.4.1. Quy trình

1. Xuất ảnh màn hình từ Figma; ghi đặc tả: thành phần, dữ liệu mẫu, hành vi khi bấm.
2. Viết prompt có ràng buộc, ví dụ: *"Dựng màn hình Chi tiết món theo ảnh đính kèm. Dùng màu, khoảng cách trong constants/theme.ts và component Button có sẵn. Không thêm thư viện UI mới. Nút Thêm vào giỏ cố định ở cuối màn hình."*
3. Chạy thử, đặt cạnh ảnh thiết kế để so khoảng cách, cỡ chữ, màu, căn lề.
4. Sửa chỗ lệch; tách phần lặp lại thành component; ghi prompt và nhận xét vào `PROMPTS.md`.

### 2.4.2. Lỗi trợ lý AI hay mắc khi dựng giao diện

| Lỗi | Cách phát hiện |
|---|---|
| Viết cứng mã màu thay vì lấy từ theme | Tìm chuỗi `#` trong file màn hình |
| Dùng thư viện UI không được phép | Kiểm tra `import` và `package.json` |
| Đặt chữ ngoài `<Text>` | Ứng dụng báo lỗi khi chạy |
| Quên vùng an toàn | Nội dung bị tai thỏ che trên máy thật |
| Kích thước cố định theo pixel của bản thiết kế | Giao diện vỡ trên máy màn hình nhỏ |

## 2.5. Sơ đồ chức năng

### 2.5.1. Khái niệm

**Sơ đồ chức năng** (sơ đồ phân rã chức năng) chia hệ thống thành các nhóm chức năng, mỗi nhóm chia tiếp thành chức năng con. Sơ đồ dạng cây, gốc là tên ứng dụng. Đây là đầu vào để:

- Thiết kế danh sách màn hình và điều hướng (Chương 3).
- Thiết kế API và stored procedure (Chương 5).
- Phân công công việc trong nhóm.

### 2.5.2. Sơ đồ chức năng LHU Food

- **LHU Food**
  - **Khách hàng:** xem thực đơn; xem chi tiết món; tìm kiếm; quản lý giỏ hàng; đặt hàng; theo dõi đơn hàng; nhận thông báo.
  - **Nhân viên căn tin:** xem đơn mới; cập nhật trạng thái đơn; quản lý món; xem thống kê.
  - **Tài khoản:** đăng ký; đăng nhập; cập nhật hồ sơ; đăng xuất.

Vẽ bằng draw.io (dạng cây, trên xuống) hoặc FigJam. Lưu cả file nguồn và ảnh xuất ra trong thư mục `docs/` của repo; sơ đồ là một minh chứng chấm CLO1 và CLO3.

## Tóm tắt chương

- Core components: `View`, `Text`, `Image`, `ScrollView`, `TextInput`, `Pressable`; chữ luôn nằm trong `Text`, ảnh URL luôn có kích thước.
- Flexbox trên React Native mặc định xếp theo cột; `flex: 1` lấp đầy; `useWindowDimensions` để thích ứng kích thước màn hình.
- Theme và UI kit giúp giao diện nhất quán và giúp AI sinh mã đúng quy ước.
- AI dựng giao diện nhanh, nhưng bạn phải so với thiết kế và sửa các lỗi điển hình.
- Sơ đồ chức năng là bước đầu của thiết kế màn hình, API và dữ liệu.

## Câu hỏi ôn tập

1. Vì sao không nên dùng `ScrollView` cho danh sách hàng trăm phần tử?
2. Nêu ba khác biệt giữa Flexbox trên web và trên React Native.
3. Đơn vị dp là gì? Vì sao dùng dp thay cho pixel?
4. Khi nào cần `SafeAreaView`? Thuộc tính `edges` dùng để làm gì?
5. Lợi ích của việc gom màu và khoảng cách vào `theme.ts` là gì, xét cả khi làm việc với AI?
6. Sơ đồ chức năng giúp gì cho việc thiết kế API và cơ sở dữ liệu?

## Bài tập

1. **Màn hình Hồ sơ.** Dựng màn hình Hồ sơ người dùng (ảnh tròn, họ tên, email, số điện thoại, danh sách cài đặt, nút Đăng xuất) theo ảnh thiết kế. Hiển thị đúng trên hai kích thước màn hình Android; nộp hai ảnh chụp màn hình.
2. **UI kit.** Xây `Card`, `Input` (có nhãn và lỗi) và `EmptyState` theo `theme.ts`. Viết một màn hình demo hiển thị tất cả biến thể.
3. **Sơ đồ chức năng.** Vẽ sơ đồ chức năng cho đề tài của nhóm, ít nhất 3 nhóm chức năng và 12 chức năng con.

## Tài liệu tham khảo

- React Native - Core Components and APIs: https://reactnative.dev/docs/components-and-apis
- React Native - Layout with Flexbox: https://reactnative.dev/docs/flexbox
- React Native - Style: https://reactnative.dev/docs/style
- Expo - Safe areas: https://docs.expo.dev/develop/user-interface/safe-areas/
