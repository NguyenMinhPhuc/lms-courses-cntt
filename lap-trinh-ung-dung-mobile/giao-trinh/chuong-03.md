# Chương 3. Điều hướng với Expo Router

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Giải thích các mô hình điều hướng trên di động: stack, tab, modal.
- Tổ chức màn hình theo cấu trúc thư mục của Expo Router.
- Dùng route động, truyền tham số và chuyển màn hình bằng mã.
- Cấu hình deep link cho ứng dụng.
- Vẽ sơ đồ luồng màn hình và ERD sơ bộ từ danh sách màn hình.

## 3.1. Mô hình điều hướng trên di động

Ứng dụng di động không có thanh địa chỉ. Người dùng di chuyển giữa các màn hình bằng chạm, nút Back của Android và cử chỉ vuốt. Ba mô hình cơ bản:

### 3.1.1. Stack

Màn hình mới được đặt **chồng** lên màn hình hiện tại. Nút Back (hoặc vuốt từ cạnh trái trên iOS) gỡ màn hình trên cùng và quay lại màn hình trước. Stack phù hợp cho luồng đi sâu dần: Danh sách món → Chi tiết món → Xác nhận.

### 3.1.2. Tab

Thanh điều hướng cố định ở cuối màn hình, mỗi tab là một khu vực chính của ứng dụng. Chuyển tab không làm mất trạng thái của tab kia. LHU Food có 4 tab: Trang chủ, Giỏ hàng, Đơn hàng, Tài khoản. Nên giới hạn 3–5 tab.

### 3.1.3. Modal

Màn hình trượt lên che màn hình hiện tại, dùng cho tác vụ ngắn và tách biệt như xác nhận đặt hàng hoặc chọn bộ lọc. Đóng modal đưa người dùng về đúng vị trí cũ.

### 3.1.4. Lồng các mô hình

Ứng dụng thật thường lồng các mô hình: **Stack gốc** chứa **nhóm Tab**; từ một tab có thể mở thêm màn hình chi tiết thuộc Stack gốc; modal cũng thuộc Stack gốc. Cách lồng này quyết định thanh tab có còn hiển thị ở màn hình chi tiết hay không.

## 3.2. Expo Router: điều hướng dựa trên file

### 3.2.1. Nguyên tắc

Expo Router xây dựng trên React Navigation và dùng **cấu trúc thư mục `app/` làm bản đồ điều hướng**:

- Mỗi file trong `app/` là một màn hình, đường dẫn tương ứng với vị trí file.
- File `index.tsx` là màn hình mặc định của thư mục chứa nó.
- File `_layout.tsx` khai báo cách sắp xếp các màn hình cùng cấp (Stack, Tabs).
- Thư mục có tên trong ngoặc như `(tabs)` là **nhóm route**: gom màn hình chung một layout, không xuất hiện trong đường dẫn.
- Tên file trong ngoặc vuông như `[id].tsx` là **route động**.

### 3.2.2. Cấu trúc thư mục của LHU Food

```text
app/
├── _layout.tsx            Stack gốc
├── login.tsx              /login          (Chương 6)
├── (tabs)/
│   ├── _layout.tsx        Thanh tab
│   ├── index.tsx          /               Trang chủ
│   ├── cart.tsx           /cart           Giỏ hàng
│   ├── orders.tsx         /orders         Đơn hàng
│   └── account.tsx        /account        Tài khoản
├── category/
│   └── [id].tsx           /category/3     Món theo danh mục
├── product/
│   └── [id].tsx           /product/12     Chi tiết món
└── confirm.tsx            /confirm        Modal xác nhận
```

### 3.2.3. Layout gốc

`app/_layout.tsx`:

```tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      <Stack.Screen name="category/[id]" options={{ title: 'Danh mục' }} />
      <Stack.Screen name="product/[id]" options={{ title: 'Chi tiết món' }} />
      <Stack.Screen name="confirm" options={{ presentation: 'modal', title: 'Xác nhận đặt hàng' }} />
    </Stack>
  );
}
```

`headerShown: false` cho nhóm `(tabs)` vì mỗi tab đã có thanh tiêu đề riêng; nếu không, màn hình sẽ hiện hai thanh tiêu đề chồng nhau.

### 3.2.4. Layout thanh tab

`app/(tabs)/_layout.tsx`:

```tsx
import { Tabs } from 'expo-router';
import Ionicons from '@expo/vector-icons/Ionicons';

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ tabBarActiveTintColor: '#013D88' }}>
      <Tabs.Screen
        name="index"
        options={{ title: 'Trang chủ', tabBarIcon: ({ color, size }) => <Ionicons name="home" color={color} size={size} /> }}
      />
      <Tabs.Screen
        name="cart"
        options={{ title: 'Giỏ hàng', tabBarIcon: ({ color, size }) => <Ionicons name="cart" color={color} size={size} /> }}
      />
      <Tabs.Screen
        name="orders"
        options={{ title: 'Đơn hàng', tabBarIcon: ({ color, size }) => <Ionicons name="receipt" color={color} size={size} /> }}
      />
      <Tabs.Screen
        name="account"
        options={{ title: 'Tài khoản', tabBarIcon: ({ color, size }) => <Ionicons name="person" color={color} size={size} /> }}
      />
    </Tabs>
  );
}
```

`@expo/vector-icons` có sẵn trong dự án Expo, cung cấp nhiều bộ biểu tượng như Ionicons, MaterialIcons.

## 3.3. Route động, tham số và chuyển màn hình

### 3.3.1. Đọc tham số

```tsx
// app/product/[id].tsx
import { useLocalSearchParams, Stack } from 'expo-router';

export default function ProductDetail() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const product = products.find((p) => String(p.id) === id);

  return (
    <>
      <Stack.Screen options={{ title: product?.name ?? 'Chi tiết món' }} />
      {/* nội dung màn hình */}
    </>
  );
}
```

Tham số trên đường dẫn luôn là **chuỗi**. Khi so với mã số, hãy chuyển kiểu cho thống nhất. `<Stack.Screen options>` đặt bên trong màn hình cho phép đổi tiêu đề theo dữ liệu.

### 3.3.2. Chuyển màn hình

**Bằng component `Link`:**

```tsx
import { Link } from 'expo-router';

<Link href={`/product/${item.id}`}>Xem chi tiết</Link>

// Bọc một component tùy ý
<Link href={`/product/${item.id}`} asChild>
  <Pressable><ProductCard {...item} /></Pressable>
</Link>
```

**Bằng mã, qua đối tượng `router`:**

| Lệnh | Tác dụng | Dùng khi |
|---|---|---|
| `router.push('/confirm')` | Thêm màn hình vào stack | Đi tới màn hình mới, có thể quay lại |
| `router.back()` | Quay lại màn hình trước | Nút "Hủy", sau khi lưu xong |
| `router.replace('/')` | Thay màn hình hiện tại | Sau khi đăng nhập: Back không quay về màn hình đăng nhập |
| `router.dismiss()` | Đóng modal | Hoàn tất tác vụ trong modal |

### 3.3.3. Deep link

Deep link cho phép một đường dẫn bên ngoài mở thẳng một màn hình trong ứng dụng. Khai báo `scheme` trong `app.json`:

```json
{
  "expo": {
    "name": "LHU Food",
    "scheme": "lhufood"
  }
}
```

Khi đó `lhufood://product/12` mở màn hình Chi tiết món 12. Expo Router tự ánh xạ đường dẫn này nhờ cấu trúc thư mục. Chương 9 dùng deep link để bấm thông báo mở đúng đơn hàng. Khi thử trong Expo Go, scheme có dạng khác; tham khảo tài liệu Expo về linking.

## 3.4. Từ màn hình đến dữ liệu

### 3.4.1. Sơ đồ luồng màn hình

Sơ đồ luồng màn hình (screen flow) vẽ mỗi màn hình là một khối và mũi tên thể hiện hành động chuyển màn hình (ví dụ "bấm món", "bấm Đặt ngay"). Sơ đồ này giúp nhóm:

- Thống nhất danh sách màn hình trước khi viết mã.
- Quyết định màn hình nào là tab, màn hình nào mở bằng stack hay modal.
- Phát hiện màn hình "cụt" (không có đường quay lại) hoặc vòng lặp.

### 3.4.2. Xác định thực thể và quan hệ

Mỗi màn hình hiển thị hoặc tạo ra dữ liệu. Liệt kê dữ liệu đó, ta có các **thực thể**:

| Màn hình | Dữ liệu cần | Thực thể |
|---|---|---|
| Trang chủ, Danh mục | Danh sách danh mục, món | Categories, Products |
| Chi tiết món | Thông tin món | Products |
| Giỏ hàng, Xác nhận | Món đã chọn, người đặt | Products, Users |
| Đơn hàng | Đơn, các món trong đơn | Orders, OrderItems |

**Quan hệ:**

- Một danh mục có nhiều món: Categories **1-n** Products.
- Một người dùng có nhiều đơn: Users **1-n** Orders.
- Một đơn có nhiều món, một món nằm trong nhiều đơn: Orders **n-n** Products, tách qua bảng trung gian **OrderItems** (chứa số lượng và đơn giá).

### 3.4.3. ERD sơ bộ

ERD sơ bộ gồm tên thực thể, khóa chính, khóa ngoại và quan hệ; chưa cần đủ kiểu dữ liệu. Ví dụ dạng DBML dùng cho dbdiagram.io:

```text
Table Categories { CategoryId int [pk]  Name nvarchar }
Table Products   { ProductId int [pk]  CategoryId int [ref: > Categories.CategoryId]  Name nvarchar  Price decimal }
Table Users      { UserId int [pk]  FullName nvarchar  Email nvarchar }
Table Orders     { OrderId int [pk]  UserId int [ref: > Users.UserId]  Status nvarchar }
Table OrderItems { OrderId int [ref: > Orders.OrderId]  ProductId int [ref: > Products.ProductId]  Quantity int }
```

Chương 5 hoàn thiện ERD này thành cơ sở dữ liệu SQL Server với đầy đủ kiểu dữ liệu, ràng buộc và stored procedure.

## 3.5. Checkpoint Sprint 1

Cuối buổi 03, mỗi nhóm trình bày:

- Khung ứng dụng đủ điều hướng, dùng dữ liệu giả (mock JSON).
- Sơ đồ luồng màn hình và ERD sơ bộ trong thư mục `docs/`.
- Demo 3 phút trên điện thoại Android.
- **Sprint Review:** đã hoàn thành gì so với kế hoạch, còn gì chưa xong.
- **Retrospective:** điều gì nên giữ, điều gì cần thay đổi ở Sprint 2.

## 3.6. Mã nguồn LHU Food của chương

`data/products.ts` (dữ liệu giả dùng đến hết Chương 4):

```ts
export type Product = { id: number; categoryId: number; name: string; price: number; imageUrl: string; description: string };

export const categories = [
  { id: 1, name: 'Cơm' },
  { id: 2, name: 'Bún - Phở' },
  { id: 3, name: 'Đồ uống' },
];

export const products: Product[] = [
  { id: 1, categoryId: 1, name: 'Cơm gà xối mỡ', price: 35000, imageUrl: 'https://picsum.photos/seed/1/600/400', description: 'Cơm chiên giòn, gà xối mỡ, dưa leo.' },
  { id: 2, categoryId: 2, name: 'Bún bò Huế', price: 40000, imageUrl: 'https://picsum.photos/seed/2/600/400', description: 'Nước dùng đậm vị, chả cua, giò heo.' },
  { id: 3, categoryId: 3, name: 'Trà đào', price: 20000, imageUrl: 'https://picsum.photos/seed/3/600/400', description: 'Trà đào cam sả, ít đường.' },
];
```

`app/category/[id].tsx`:

```tsx
import { Link, Stack, useLocalSearchParams } from 'expo-router';
import { Pressable, ScrollView, Text } from 'react-native';
import { categories, products } from '@/data/products';
import { ProductCard } from '@/components/ProductCard';

export default function CategoryScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const category = categories.find((c) => String(c.id) === id);
  const items = products.filter((p) => String(p.categoryId) === id);

  return (
    <ScrollView contentContainerStyle={{ padding: 16, gap: 12 }}>
      <Stack.Screen options={{ title: category?.name ?? 'Danh mục' }} />
      {items.length === 0 && <Text>Chưa có món nào trong danh mục này.</Text>}
      {items.map((item) => (
        <Link key={item.id} href={`/product/${item.id}`} asChild>
          <Pressable>
            <ProductCard name={item.name} price={item.price} onAdd={() => {}} />
          </Pressable>
        </Link>
      ))}
    </ScrollView>
  );
}
```

Ảnh mẫu dùng dịch vụ ảnh ngẫu nhiên picsum.photos để minh họa; trong dự án thật, ảnh lấy từ API (Chương 5).

## Tóm tắt chương

- Stack cho luồng đi sâu, Tab cho khu vực chính, Modal cho tác vụ ngắn; ứng dụng thật lồng các mô hình này.
- Expo Router: thư mục `app/` là bản đồ điều hướng; `_layout.tsx` khai báo Stack/Tabs; `(nhóm)` không vào đường dẫn; `[id]` là route động.
- Đọc tham số bằng `useLocalSearchParams` (luôn là chuỗi); chuyển màn hình bằng `Link` hoặc `router.push/back/replace`.
- `scheme` trong `app.json` bật deep link.
- Từ màn hình suy ra thực thể và quan hệ, tạo ERD sơ bộ cho Chương 5.

## Câu hỏi ôn tập

1. Phân biệt stack, tab và modal; cho mỗi loại một ví dụ trong ứng dụng của nhóm.
2. File `app/(tabs)/orders.tsx` ứng với đường dẫn nào? Vì sao?
3. Vì sao Stack gốc cần `headerShown: false` cho nhóm `(tabs)`?
4. Khi nào dùng `router.replace` thay cho `router.push`?
5. Tham số `id` đọc từ `useLocalSearchParams` có kiểu gì? Điều đó ảnh hưởng thế nào khi so sánh?
6. Vì sao quan hệ giữa Orders và Products cần bảng trung gian?

## Bài tập

1. **Luồng Danh mục.** Hoàn thiện luồng Trang chủ → Danh mục → Danh sách món → Chi tiết món; tiêu đề đổi theo danh mục; Back hoạt động đúng từng bước.
2. **Modal bộ lọc.** Thêm modal "Lọc theo giá" mở từ Trang chủ, có hai lựa chọn "Dưới 30.000 đ" và "Từ 30.000 đ"; đóng modal áp dụng bộ lọc.
3. **Sơ đồ và ERD.** Vẽ sơ đồ luồng màn hình và ERD sơ bộ cho đề tài của nhóm; ghi rõ quan hệ 1-n và n-n.

## Tài liệu tham khảo

- Expo Router - Introduction: https://docs.expo.dev/router/introduction/
- Expo Router - Navigation layouts (Stack, Tabs): https://docs.expo.dev/router/basics/layout/
- Expo Router - Navigating between pages: https://docs.expo.dev/router/basics/navigation/
- Expo - Linking và deep link: https://docs.expo.dev/linking/overview/
