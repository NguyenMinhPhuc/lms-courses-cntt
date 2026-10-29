# Chương 1. Tổng quan phát triển ứng dụng di động và khởi động dự án

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- So sánh các hướng phát triển ứng dụng di động: native, cross-platform và PWA.
- Giải thích cách React Native hiển thị giao diện native và vai trò của Expo.
- Cài đặt môi trường, tạo và chạy dự án Expo đầu tiên trên điện thoại Android.
- Chuyển cách viết component từ React web sang React Native.
- Thiết lập quy trình vibe coding có kiểm soát và bảng phân vai cho dự án nhóm.

## 1.1. Các hướng phát triển ứng dụng di động

Một ứng dụng di động có thể được xây dựng theo ba hướng chính. Không có hướng nào tốt nhất cho mọi trường hợp; lựa chọn phụ thuộc vào yêu cầu sản phẩm, kỹ năng của đội và thời gian.

| Hướng | Công nghệ tiêu biểu | Ưu điểm | Hạn chế |
|---|---|---|---|
| Native | Kotlin/Java (Android), Swift (iOS) | Truy cập đầy đủ API thiết bị; hiệu năng và trải nghiệm tốt nhất | Hai mã nguồn riêng, cần hai nhóm kỹ năng |
| Cross-platform | React Native, Flutter | Một mã nguồn cho nhiều nền tảng; giao diện là thành phần native (React Native) | Tính năng đặc thù có thể cần thư viện hoặc mã native |
| PWA | HTML, CSS, JavaScript | Dùng lại hoàn toàn kỹ năng web; không cần phát hành qua cửa hàng | Truy cập phần cứng hạn chế, nhất là trên iOS |

Ứng dụng LHU Food cần danh sách món mượt, camera, vị trí, thông báo và chạy trên Android. Hướng cross-platform đáp ứng đủ các yêu cầu này. Học phần chọn **React Native** vì bạn đã quen React: cách tư duy component, props, state và hook được giữ nguyên.

## 1.2. React Native hoạt động như thế nào

### 1.2.1. Từ component đến view native

Trong React web, `<div>` cuối cùng trở thành một phần tử DOM trong trình duyệt. Trong React Native, bạn viết `<View>` và `<Text>`; React Native tạo ra **view native** tương ứng của hệ điều hành. Trên Android, `<Text>` là một `TextView` thật, `<View>` là một `ViewGroup`. Ứng dụng không phải một trang web chạy trong khung nhúng.

Mã JavaScript/TypeScript của bạn chạy trên một **JavaScript engine** (mặc định là Hermes, được tối ưu cho React Native). Engine này giao tiếp với phần native để tạo, cập nhật và xóa view khi state thay đổi.

### 1.2.2. Kiến trúc mới (New Architecture)

Các phiên bản React Native hiện nay dùng **New Architecture**, gồm:

- **JSI (JavaScript Interface):** cho phép JavaScript gọi trực tiếp hàm native, thay cho cơ chế "cầu nối" gửi thông điệp bất đồng bộ trước đây.
- **Fabric:** hệ thống hiển thị mới, cập nhật giao diện nhanh và nhất quán hơn.
- **TurboModules:** module native được nạp khi cần, giúp ứng dụng khởi động nhanh hơn.

Ở mức học phần, bạn không cần lập trình trực tiếp với các thành phần này. Điều quan trọng là hiểu: giao diện React Native là native thật, và thư viện bạn dùng cần tương thích với New Architecture.

### 1.2.3. Expo

**Expo** là bộ công cụ và thư viện xây dựng trên React Native. Tài liệu chính thức của React Native khuyến nghị dùng một framework như Expo khi bắt đầu dự án mới. Expo cung cấp:

- **Expo SDK:** các thư viện truy cập thiết bị (camera, vị trí, thông báo, lưu trữ bảo mật…) đã được kiểm tra tương thích với nhau. Mỗi phiên bản SDK đi kèm một phiên bản React Native cụ thể.
- **Expo Go:** ứng dụng cài trên điện thoại, chạy thử dự án ngay bằng cách quét mã QR, không cần build.
- **Development build:** bản ứng dụng riêng của dự án, dùng khi cần thư viện native mà Expo Go không có sẵn.
- **Expo Router:** điều hướng dựa trên cấu trúc thư mục (Chương 3).
- **EAS (Expo Application Services):** EAS Build tạo file cài đặt APK/AAB trên máy chủ của Expo; EAS Update phát hành cập nhật qua mạng.

> **Trong học phần:** Mỗi sinh viên tự đăng ký **tài khoản Expo miễn phí**. Gói miễn phí giới hạn số lượt build trên EAS, vì vậy khi phát triển hãy dùng Expo Go hoặc development build, chỉ build APK khi cần nộp hoặc cần thử trên máy người khác.

## 1.3. Cài đặt môi trường và tạo dự án

### 1.3.1. Công cụ cần có

| Công cụ | Mục đích | Ghi chú |
|---|---|---|
| Node.js (bản LTS) | Chạy công cụ Expo và quản lý gói npm | Kiểm tra: `node -v` |
| Git và tài khoản GitHub | Quản lý mã nguồn, làm việc nhóm | Cấu hình `user.name`, `user.email` |
| VS Code | Soạn mã, tích hợp GitHub Copilot | Cài extension ESLint, Prettier |
| Expo Go (trên điện thoại Android) | Chạy thử ứng dụng | Tải từ Google Play |
| Android Studio (tùy chọn) | Tạo Android emulator khi không có điện thoại | Dùng Device Manager để tạo máy ảo |

### 1.3.2. Tạo dự án LHU Food

```bash
npx create-expo-app@latest lhu-food
cd lhu-food
npx expo start
```

Lệnh `npx expo start` khởi động **Metro** (bộ đóng gói JavaScript) và hiển thị mã QR. Mở Expo Go trên điện thoại, quét mã QR; điện thoại và máy tính phải cùng mạng Wi-Fi. Trong cửa sổ terminal:

- Nhấn `a` để mở trên Android emulator.
- Nhấn `r` để tải lại ứng dụng.
- Nhấn `j` để mở công cụ gỡ lỗi.

Nếu mạng phòng lab chặn kết nối giữa các máy, chạy `npx expo start --tunnel`.

Dự án mới tạo có sẵn các màn hình mẫu. Để bắt đầu từ thư mục `app/` trống, chạy `npm run reset-project`: lệnh này chuyển mã mẫu sang thư mục `app-example/` và tạo `app/index.tsx` đơn giản. Mã nguồn ở mục 1.7 giả định bạn đã chạy lệnh này.

### 1.3.3. Cấu trúc thư mục

| Thư mục/file | Vai trò |
|---|---|
| `app/` | Các màn hình; mỗi file là một màn hình (Expo Router) |
| `components/` | Component dùng chung |
| `constants/` | Hằng số như màu sắc, khoảng cách |
| `assets/` | Ảnh, biểu tượng, phông chữ |
| `app.json` | Cấu hình ứng dụng: tên, biểu tượng, scheme, package Android |
| `package.json` | Danh sách thư viện và lệnh |

Khi bạn lưu một file, **Fast Refresh** cập nhật ứng dụng trên điện thoại trong vài giây mà vẫn giữ state hiện tại. Đây là lý do vòng lặp "sửa mã → xem kết quả" trên React Native rất nhanh.

## 1.4. Từ React web sang React Native

### 1.4.1. Bảng tương ứng

| React web | React Native | Khác biệt cần nhớ |
|---|---|---|
| `<div>` | `<View>` | Khung chứa; mặc định xếp các phần tử con theo cột |
| `<p>`, `<span>`, `<h1>` | `<Text>` | Mọi chữ **bắt buộc** nằm trong `<Text>` |
| `<img>` | `<Image>` | Ảnh từ URL phải khai báo `width` và `height` |
| `<button onClick>` | `<Pressable onPress>` | Sự kiện chạm thay cho click chuột |
| `<input>` | `<TextInput>` | Dùng `onChangeText` thay cho `onChange` |
| File CSS, `className` | `StyleSheet.create`, `style` | Viết bằng JavaScript; thuộc tính camelCase; style không kế thừa như CSS (trừ trong `<Text>` lồng nhau) |

### 1.4.2. Một lỗi điển hình

```tsx
// SAI: chữ nằm trực tiếp trong View
<View>Xin chào</View>

// ĐÚNG
<View>
  <Text>Xin chào</Text>
</View>
```

Dòng đầu gây lỗi "Text strings must be rendered within a `<Text>` component". Lỗi này thường xuất hiện khi chép mã JSX từ dự án web sang, hoặc khi có khoảng trắng thừa giữa các thẻ.

## 1.5. Vibe coding có kiểm soát

### 1.5.1. Khái niệm

**Vibe coding** là cách lập trình trong đó bạn mô tả bằng ngôn ngữ tự nhiên điều mình muốn, và trợ lý AI sinh mã. Học phần dùng **Google Antigravity** và **GitHub Copilot Chat**. AI giúp viết nhanh phần lặp lại và gợi ý cách làm, nhưng AI có thể sinh mã chạy được mà sai nghiệp vụ, thiếu kiểm tra lỗi hoặc không an toàn. **Người chịu trách nhiệm về mã vẫn là bạn.**

### 1.5.2. Quy trình năm bước

1. **Cho AI ngữ cảnh** bằng file quy ước dự án.
2. **Viết prompt cụ thể:** màn hình nào, dữ liệu gì, ràng buộc gì, tiêu chí hoàn thành ra sao.
3. **Đọc và chạy thử** mã AI sinh ra; sửa chỗ sai thay vì chấp nhận nguyên văn.
4. **Ghi lại prompt chính** và nhận xét vào `PROMPTS.md`.
5. **Không hiểu thì không merge:** trước khi gộp vào nhánh chính, bạn phải giải thích được từng dòng.

### 1.5.3. File quy ước dự án

`AGENTS.md` đặt ở gốc repo, mô tả dự án cho trợ lý AI. GitHub Copilot đọc thêm `.github/copilot-instructions.md`; nội dung hai file có thể giống nhau.

```markdown
# LHU Food - Quy ước dự án

## Công nghệ
- React Native + Expo, TypeScript, điều hướng bằng Expo Router (thư mục app/).
- Trạng thái toàn cục: Zustand. Dữ liệu server: TanStack Query.
- Backend NestJS; truy cập SQL Server CHỈ qua stored procedure bằng thư viện mssql.

## Quy ước
- Component dùng chung đặt trong components/, mỗi file một component, tên PascalCase.
- Style dùng StyleSheet.create; màu và khoảng cách lấy từ constants/theme.ts.
- Chuỗi hiển thị bằng tiếng Việt có dấu.
- Không thêm thư viện mới khi chưa được nhóm đồng ý.
- Không viết câu lệnh SQL trực tiếp trong mã backend.
```

### 1.5.4. Mẫu ghi `PROMPTS.md`

```markdown
## 2026-02-10 - Màn hình Chi tiết món (Nguyễn Văn A)
**Công cụ:** GitHub Copilot Chat
**Prompt:** Dựng màn hình Chi tiết món theo ảnh đính kèm, dùng theme và Button có sẵn...
**Kết quả:** Dùng được khoảng 70%.
**Đã sửa:** AI viết cứng màu nút; quên SafeAreaView; đổi lại theo theme.
```

### 1.5.5. Làm việc nhóm với Git

- Mỗi tính năng một nhánh: `feature/product-detail`.
- Commit nhỏ, thông điệp rõ ràng: `feat: thêm màn hình chi tiết món`.
- Tạo Pull Request; ít nhất một bạn trong nhóm review trước khi merge.
- Lịch sử commit và PR là căn cứ đánh giá vai trò cá nhân (CLO4).

## 1.6. Dự án PBL và phân vai

Học phần tổ chức theo **học tập dựa trên dự án (PBL)**: nhóm 4–5 sinh viên phát triển một ứng dụng qua 4 sprint, mỗi sprint 3 buổi. Khuyến khích chọn cùng đề tài với học phần Lập trình ứng dụng Web để dùng chung backend.

**Project Brief (1 trang)** gồm:

- Vấn đề cần giải quyết và người dùng chính.
- 5–7 tính năng chính, đánh dấu tính năng cần dữ liệu thời gian thực.
- Các vai trò người dùng (ví dụ: khách hàng, nhân viên).

**Vai trò gợi ý trong nhóm:** mobile UI, mobile logic, backend API, cơ sở dữ liệu và stored procedure, kiểm thử và phát hành. Mỗi thành viên có ít nhất một vai chính.

## 1.7. Mã nguồn LHU Food của chương

`components/ProductCard.tsx`:

```tsx
import { View, Text, Pressable, StyleSheet } from 'react-native';

type Props = {
  name: string;
  price: number;
  onAdd: () => void;
};

export function ProductCard({ name, price, onAdd }: Props) {
  return (
    <View style={styles.card}>
      <Text style={styles.name}>{name}</Text>
      <Text style={styles.price}>{price.toLocaleString('vi-VN')} đ</Text>
      <Pressable
        style={({ pressed }) => [styles.button, pressed && styles.pressed]}
        onPress={onAdd}
      >
        <Text style={styles.buttonText}>Thêm vào giỏ</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 16, borderRadius: 12, backgroundColor: '#fff', gap: 4 },
  name: { fontSize: 18, fontWeight: 'bold' },
  price: { color: '#6C757D' },
  button: { marginTop: 8, padding: 10, borderRadius: 8, backgroundColor: '#013D88' },
  pressed: { opacity: 0.8 },
  buttonText: { color: '#fff', textAlign: 'center', fontWeight: '600' },
});
```

`app/index.tsx` (màn hình đầu tiên, chưa dùng điều hướng):

```tsx
import { Alert, ScrollView, StyleSheet, Text } from 'react-native';
import { ProductCard } from '@/components/ProductCard';

const products = [
  { id: 1, name: 'Cơm gà xối mỡ', price: 35000 },
  { id: 2, name: 'Bún bò Huế', price: 40000 },
];

export default function HomeScreen() {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>LHU Food</Text>
      {products.map((p) => (
        <ProductCard
          key={p.id}
          name={p.name}
          price={p.price}
          onAdd={() => Alert.alert('Đã thêm', p.name)}
        />
      ))}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { padding: 16, gap: 12 },
  title: { fontSize: 24, fontWeight: 'bold' },
});
```

Tiền tố `@/` là bí danh đường dẫn tới thư mục gốc, được cấu hình sẵn trong `tsconfig.json` của dự án Expo mới.

## Tóm tắt chương

- React Native dùng một mã nguồn để tạo giao diện native thật trên Android và iOS, dựa trên kỹ năng React sẵn có.
- Expo cung cấp SDK, Expo Go để chạy thử, Expo Router để điều hướng và EAS để build.
- Khi chuyển từ web: `View` thay `div`, mọi chữ nằm trong `Text`, `onPress` thay `onClick`, `StyleSheet` thay file CSS.
- Vibe coding có kiểm soát: cho AI ngữ cảnh, prompt cụ thể, kiểm tra mã, ghi `PROMPTS.md`, không hiểu thì không merge.
- Dự án PBL bắt đầu bằng Project Brief, bảng phân vai và repo chung có file quy ước cho AI.

## Câu hỏi ôn tập

1. Nêu ưu điểm và hạn chế của hướng native so với cross-platform.
2. Vì sao nói giao diện React Native "không phải trang web nhúng"?
3. Expo Go và development build khác nhau thế nào? Khi nào cần development build?
4. Liệt kê năm khác biệt khi viết component trên React Native so với React web.
5. Vì sao cần file `AGENTS.md` khi dùng trợ lý AI trong dự án nhóm?
6. Nguyên tắc "không hiểu thì không merge" bảo vệ nhóm khỏi rủi ro nào?

## Bài tập

1. **Thẻ giới thiệu bản thân.** Tạo ứng dụng Expo hiển thị ảnh đại diện, họ tên, lớp, 3 kỹ năng và nút "Liên hệ" mở hộp thoại `Alert`. Chạy trên điện thoại Android, đẩy lên GitHub cá nhân kèm `PROMPTS.md`.
2. **Chuyển component web.** Chọn một component React đã viết ở học phần Lập trình Frontend, chuyển sang React Native. Ghi lại các chỗ phải thay đổi và lý do.
3. **Khởi động dự án nhóm.** Viết Project Brief 1 trang, bảng phân vai, tạo repo nhóm có `AGENTS.md`, `.github/copilot-instructions.md` và `PROMPTS.md`.

## Tài liệu tham khảo

- React Native - Introduction: https://reactnative.dev/docs/getting-started
- React Native - Core Components and Native Components: https://reactnative.dev/docs/intro-react-native-components
- Expo - Get started: https://docs.expo.dev/get-started/introduction/
- Expo - Expo Go và development build: https://docs.expo.dev/develop/development-builds/introduction/
