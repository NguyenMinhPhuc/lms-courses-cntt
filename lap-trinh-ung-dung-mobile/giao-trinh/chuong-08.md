# Chương 8. Tính năng thiết bị: Camera, Ảnh, Vị trí và Bản đồ

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Giải thích mô hình quyền truy cập trên Android và cách xin quyền đúng cách.
- Chụp hoặc chọn ảnh, nén ảnh và tải lên API NestJS; lưu thông tin ảnh vào SQL Server qua stored procedure.
- Lấy vị trí hiện tại, hiển thị bản đồ và tính khoảng cách giữa hai tọa độ.
- Quyết định khi nào dùng Expo Go, khi nào cần development build.

## 8.1. Quyền truy cập trên thiết bị

### 8.1.1. Mô hình quyền

Từ Android 6.0, các quyền nhạy cảm (camera, vị trí, micro, ảnh) là **quyền thời gian chạy (runtime permission)**: ứng dụng phải hỏi người dùng khi cần, và người dùng có thể từ chối hoặc thu hồi bất cứ lúc nào trong Cài đặt. Android có thể cho người dùng chọn "Chỉ lần này" hoặc chỉ cấp quyền chọn một số ảnh thay vì toàn bộ thư viện. iOS có mô hình tương tự và bắt buộc lời giải thích cho từng quyền.

Mỗi lần xin quyền có ba kết quả cần xử lý:

| Trạng thái | Ý nghĩa | Ứng dụng nên làm |
|---|---|---|
| `granted` | Đã cho phép | Tiếp tục tính năng |
| `denied`, `canAskAgain = true` | Từ chối lần này | Giải thích lại, cho phép thử lần sau |
| `denied`, `canAskAgain = false` | Từ chối và không hỏi lại | Hướng dẫn mở Cài đặt bằng `Linking.openSettings()` |

### 8.1.2. Nguyên tắc xin quyền

1. **Xin đúng lúc:** khi người dùng bấm chức năng cần quyền, không xin tất cả ngay lúc mở app.
2. **Giải thích trước:** cho người dùng biết vì sao cần quyền, bằng một dòng chữ hoặc màn hình ngắn trước hộp thoại của hệ thống.
3. **Xin ít nhất có thể:** vị trí "khi dùng ứng dụng" thay cho vị trí nền; chọn ảnh từ thư viện thường không cần quyền đọc toàn bộ thư viện.
4. **Ứng dụng vẫn chạy khi bị từ chối:** chỉ tính năng đó bị hạn chế.

### 8.1.3. Khai báo quyền trong app.json

Các thư viện Expo cấu hình quyền qua **config plugin** trong `app.json`. Lời giải thích hiển thị trên iOS và được dùng khi build bản cài đặt:

```json
{
  "expo": {
    "plugins": [
      ["expo-image-picker", {
        "photosPermission": "LHU Food cần truy cập ảnh để bạn chọn ảnh đại diện.",
        "cameraPermission": "LHU Food cần camera để bạn chụp ảnh đại diện."
      }],
      ["expo-location", {
        "locationWhenInUsePermission": "LHU Food dùng vị trí để tìm quầy căn tin gần bạn."
      }]
    ]
  }
}
```

Sau khi sửa phần `plugins`, khởi động lại `npx expo start`. Với development build, cần build lại thì cấu hình native mới có hiệu lực.

## 8.2. Chụp và chọn ảnh

### 8.2.1. expo-image-picker

Cài đặt: `npx expo install expo-image-picker`.

`hooks/useAvatarPicker.ts`:

```ts
import * as ImagePicker from 'expo-image-picker';
import { Alert, Linking } from 'react-native';

const OPTIONS: ImagePicker.ImagePickerOptions = {
  mediaTypes: ['images'],
  allowsEditing: true,
  aspect: [1, 1],
  quality: 0.6,
};

async function ensureCameraPermission(): Promise<boolean> {
  const { status, canAskAgain } = await ImagePicker.requestCameraPermissionsAsync();
  if (status === 'granted') return true;
  if (canAskAgain) {
    Alert.alert('Chưa có quyền camera', 'Bạn cần cho phép camera để chụp ảnh đại diện.');
  } else {
    Alert.alert('Chưa có quyền camera', 'Hãy bật quyền camera cho LHU Food trong Cài đặt.', [
      { text: 'Để sau', style: 'cancel' },
      { text: 'Mở Cài đặt', onPress: () => Linking.openSettings() },
    ]);
  }
  return false;
}

export async function pickImage(fromCamera: boolean): Promise<string | null> {
  if (fromCamera && !(await ensureCameraPermission())) return null;
  const result = fromCamera
    ? await ImagePicker.launchCameraAsync(OPTIONS)
    : await ImagePicker.launchImageLibraryAsync(OPTIONS);
  return result.canceled ? null : result.assets[0].uri;
}
```

- `allowsEditing` + `aspect: [1, 1]`: cho người dùng cắt ảnh vuông.
- `quality: 0.6`: nén JPEG; ảnh đại diện không cần chất lượng gốc vài MB.
- `result.assets[0].uri` là đường dẫn tệp tạm trên thiết bị, dùng để hiển thị và tải lên.

Để thu nhỏ kích thước điểm ảnh (ví dụ tối đa 512 × 512) trước khi gửi, dùng thêm `expo-image-manipulator`.

### 8.2.2. Tải ảnh lên server

Ảnh được gửi dưới dạng `multipart/form-data`. Trong React Native, phần tử file của `FormData` là một đối tượng `{ uri, name, type }`:

```ts
import { useAuth } from '@/stores/auth';

export async function uploadAvatar(uri: string): Promise<string> {
  const form = new FormData();
  form.append('file', { uri, name: 'avatar.jpg', type: 'image/jpeg' } as any);

  const res = await fetch(`${process.env.EXPO_PUBLIC_API_URL}/users/me/avatar`, {
    method: 'POST',
    body: form,
    headers: { Authorization: `Bearer ${useAuth.getState().token}` },
  });
  if (!res.ok) throw new Error('Tải ảnh lên thất bại');
  const { avatarUrl } = await res.json();
  return avatarUrl;
}
```

**Không tự đặt** header `Content-Type`: `fetch` tự sinh `multipart/form-data; boundary=...`; nếu đặt tay mà thiếu `boundary`, server không tách được file. Vì lý do này, upload gọi `fetch` trực tiếp thay cho hàm `api()` của Chương 5 (hàm đó luôn đặt `Content-Type: application/json`).

### 8.2.3. Nhận file trong NestJS

Cài kiểu dữ liệu cho Multer: `npm install -D @types/multer`.

`src/users/users.controller.ts`:

```ts
import { BadRequestException, Controller, Post, Req, UploadedFile, UseGuards, UseInterceptors } from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { diskStorage } from 'multer';
import * as sql from 'mssql';

@Controller('users')
@UseGuards(AuthGuard)
export class UsersController {
  constructor(private readonly db: DatabaseService) {}

  @Post('me/avatar')
  @UseInterceptors(FileInterceptor('file', {
    storage: diskStorage({
      destination: './uploads/avatars',
      filename: (req: any, _file, cb) => cb(null, `${req.user.sub}-${Date.now()}.jpg`),
    }),
    limits: { fileSize: 2 * 1024 * 1024 },
    fileFilter: (_req, file, cb) => cb(null, /^image\/(jpeg|png)$/.test(file.mimetype)),
  }))
  async uploadAvatar(@Req() req, @UploadedFile() file?: Express.Multer.File) {
    if (!file) throw new BadRequestException('Chỉ nhận ảnh JPEG hoặc PNG');
    const avatarUrl = `/uploads/avatars/${file.filename}`;
    await this.db.execute('sp_User_UpdateAvatar', {
      UserId: { type: sql.Int, value: req.user.sub },
      AvatarUrl: { type: sql.NVarChar(500), value: avatarUrl },
    });
    return { avatarUrl };
  }
}
```

- `FileInterceptor('file')`: tên trường phải trùng với `form.append('file', ...)`.
- `limits.fileSize`: ảnh vượt 2 MB bị Multer từ chối với lỗi `413 Payload Too Large`.
- `fileFilter`: trả `false` khi không phải ảnh, nên `file` là `undefined` và API báo lỗi rõ ràng.
- **Tên file do server tự đặt** theo mã người dùng và thời điểm; không dùng tên do ứng dụng gửi lên, vì có thể trùng hoặc chứa ký tự như `../` gây ghi đè file khác.
- Thư mục `uploads/avatars` phải tồn tại trước khi chạy (tạo sẵn hoặc tạo bằng `fs.mkdirSync` lúc khởi động).

### 8.2.4. Phục vụ file tĩnh và lưu đường dẫn

`src/main.ts`:

```ts
import { NestExpressApplication } from '@nestjs/platform-express';

const app = await NestFactory.create<NestExpressApplication>(AppModule);
app.useStaticAssets('uploads', { prefix: '/uploads' });
```

`database/06-avatar.sql`:

```sql
IF COL_LENGTH('dbo.Users', 'AvatarUrl') IS NULL
  ALTER TABLE Users ADD AvatarUrl NVARCHAR(500) NULL;
GO

CREATE OR ALTER PROCEDURE sp_User_UpdateAvatar
  @UserId INT, @AvatarUrl NVARCHAR(500)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE Users SET AvatarUrl = @AvatarUrl WHERE UserId = @UserId;
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy người dùng', 1;
END;
GO
```

CSDL **chỉ lưu đường dẫn**, không lưu nội dung ảnh trong bảng. Ứng dụng hiển thị ảnh bằng cách ghép địa chỉ API (`EXPO_PUBLIC_API_URL`) với `avatarUrl` làm `uri` của `<Image>`. Khi triển khai thật (Chương 11), thư mục `uploads` nằm trên Windows Server của Khoa và cần được sao lưu cùng CSDL.

## 8.3. Vị trí và bản đồ

### 8.3.1. Lấy vị trí hiện tại

Cài đặt: `npx expo install expo-location`.

```ts
import * as Location from 'expo-location';

export async function getMyLocation() {
  const { status } = await Location.requestForegroundPermissionsAsync();
  if (status !== 'granted') return null;
  const pos = await Location.getCurrentPositionAsync({ accuracy: Location.Accuracy.Balanced });
  return { latitude: pos.coords.latitude, longitude: pos.coords.longitude };
}
```

- `requestForegroundPermissionsAsync`: quyền vị trí khi đang dùng ứng dụng. Vị trí nền (`requestBackgroundPermissionsAsync`) chỉ dùng khi thật sự cần theo dõi liên tục và phải giải trình khi đưa lên cửa hàng.
- `Accuracy.Balanced` cho sai số vài chục mét, đủ cho bản đồ khuôn viên và tiết kiệm pin hơn `Highest`.
- Trên Android emulator, đặt tọa độ giả trong **Extended controls → Location**.

### 8.3.2. Dữ liệu quầy căn tin

`database/07-counters.sql`:

```sql
CREATE TABLE Counters (
  CounterId INT IDENTITY(1,1) PRIMARY KEY,
  Name      NVARCHAR(100) NOT NULL,
  Latitude  DECIMAL(9,6) NOT NULL CHECK (Latitude BETWEEN -90 AND 90),
  Longitude DECIMAL(9,6) NOT NULL CHECK (Longitude BETWEEN -180 AND 180)
);
GO

CREATE OR ALTER PROCEDURE sp_Counter_GetList
AS
BEGIN
  SET NOCOUNT ON;
  SELECT CounterId AS id, Name AS name, Latitude AS lat, Longitude AS lng FROM Counters ORDER BY Name;
END;
GO
```

`DECIMAL(9,6)` lưu tọa độ chính xác tới khoảng 0,1 mét, đủ cho mọi ứng dụng thông thường.

### 8.3.3. Tính khoảng cách

Khoảng cách giữa hai điểm trên mặt đất tính bằng **công thức Haversine**:

```ts
export function distanceKm(a: { lat: number; lng: number }, b: { lat: number; lng: number }) {
  const R = 6371; // bán kính Trái Đất (km)
  const toRad = (deg: number) => (deg * Math.PI) / 180;
  const dLat = toRad(b.lat - a.lat);
  const dLng = toRad(b.lng - a.lng);
  const h =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(a.lat)) * Math.cos(toRad(b.lat)) * Math.sin(dLng / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(h));
}
```

Dùng hàm này để sắp xếp danh sách quầy theo khoảng cách tới vị trí người dùng và hiển thị "cách bạn 120 m".

### 8.3.4. Màn hình bản đồ

Cài đặt: `npx expo install react-native-maps`.

`app/map.tsx`:

```tsx
import { useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import MapView, { Marker } from 'react-native-maps';
import { useQuery } from '@tanstack/react-query';
import { api } from '@/lib/api';
import { getMyLocation } from '@/lib/location';
import { distanceKm } from '@/lib/distance';

type Counter = { id: number; name: string; lat: number; lng: number };

export default function MapScreen() {
  const { data: counters = [] } = useQuery({ queryKey: ['counters'], queryFn: () => api<Counter[]>('/counters') });
  const [me, setMe] = useState<{ lat: number; lng: number } | null>(null);

  useEffect(() => {
    getMyLocation().then((pos) => pos && setMe({ lat: pos.latitude, lng: pos.longitude }));
  }, []);

  const first = counters[0];
  if (!first) return <Text style={{ padding: 16 }}>Chưa có dữ liệu quầy.</Text>;

  const nearest = me ? [...counters].sort((a, b) => distanceKm(me, a) - distanceKm(me, b))[0] : null;

  return (
    <View style={{ flex: 1 }}>
      <MapView
        style={StyleSheet.absoluteFill}
        showsUserLocation
        initialRegion={{ latitude: first.lat, longitude: first.lng, latitudeDelta: 0.01, longitudeDelta: 0.01 }}
      >
        {counters.map((c) => (
          <Marker key={c.id} coordinate={{ latitude: c.lat, longitude: c.lng }} title={c.name} />
        ))}
      </MapView>
      {nearest && me && (
        <View style={styles.banner}>
          <Text>Quầy gần bạn nhất: {nearest.name} ({Math.round(distanceKm(me, nearest) * 1000)} m)</Text>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  banner: { position: 'absolute', left: 16, right: 16, bottom: 24, padding: 12, borderRadius: 12, backgroundColor: '#fff' },
});
```

Khi người dùng từ chối quyền vị trí, bản đồ vẫn hiển thị các quầy; chỉ phần "gần bạn nhất" bị ẩn.

**Lưu ý khi build bản cài đặt Android:** `react-native-maps` dùng Google Maps trên Android. Chạy trong Expo Go không cần cấu hình thêm, nhưng bản APK/AAB cần **Google Maps API key** khai báo trong `app.json` (`android.config.googleMaps.apiKey`). Xem hướng dẫn trong tài liệu Expo về MapView trước khi build ở Chương 11.

## 8.4. Expo Go và development build

### 8.4.1. So sánh

| | Expo Go | Development build |
|---|---|---|
| Bản chất | Ứng dụng dùng chung, đóng gói sẵn các thư viện native của Expo SDK | Bản ứng dụng riêng của dự án, chứa đúng các thư viện native dự án cần |
| Ưu điểm | Không cần build; quét QR là chạy | Dùng được mọi thư viện native; cấu hình native riêng |
| Hạn chế | Chỉ thư viện có trong Expo SDK; không thông báo đẩy từ xa | Mỗi lần thêm thư viện native phải build lại (tốn lượt EAS Build) |
| Dùng khi | Hầu hết nội dung học phần | Thư viện ngoài SDK, push notification, cấu hình native đặc biệt |

### 8.4.2. Tạo development build (khi cần)

```bash
npx expo install expo-dev-client
npx eas-cli build --profile development --platform android
```

Lệnh build tạo file APK cài lên điện thoại; sau đó chạy `npx expo start` và mở dự án bằng ứng dụng vừa cài thay cho Expo Go. Mã JavaScript vẫn cập nhật bằng Fast Refresh; chỉ khi thêm thư viện native mới phải build lại.

### 8.4.3. Chọn thư viện thông minh

- Ưu tiên thư viện thuộc **Expo SDK** (tài liệu tại docs.expo.dev) để tiếp tục dùng Expo Go và tiết kiệm lượt build.
- Khi trợ lý AI gợi ý một thư viện, kiểm tra: có trong Expo SDK không, có hỗ trợ New Architecture không, lần cập nhật gần nhất khi nào.
- Cài bằng `npx expo install` để Expo chọn phiên bản tương thích với SDK của dự án.

## Tóm tắt chương

- Quyền thời gian chạy: xin đúng lúc, giải thích, xin ít nhất, xử lý cả ba trạng thái; khai báo lời giải thích qua config plugin.
- Ảnh: `expo-image-picker` chụp/chọn, cắt và nén; tải lên bằng `FormData` mà không tự đặt `Content-Type`.
- NestJS nhận file bằng `FileInterceptor`, giới hạn kích thước và loại file, tự đặt tên; SQL Server chỉ lưu đường dẫn qua thủ tục.
- Vị trí khi dùng ứng dụng với `expo-location`; bản đồ `react-native-maps`; khoảng cách bằng công thức Haversine.
- Expo Go đủ cho hầu hết bài học; development build khi cần thư viện native ngoài SDK hoặc push notification.

## Câu hỏi ôn tập

1. Nêu ba trạng thái kết quả khi xin quyền và cách ứng dụng xử lý từng trạng thái.
2. Vì sao không nên xin mọi quyền ngay khi mở ứng dụng lần đầu?
3. Vì sao không tự đặt header `Content-Type` khi gửi `FormData`?
4. Vì sao server không dùng tên file do ứng dụng gửi lên?
5. Phân biệt quyền vị trí foreground và background; LHU Food cần loại nào?
6. Khi nào bắt buộc phải dùng development build?

## Bài tập

1. **Báo cáo sự cố.** Màn hình cho phép chụp ảnh, tự lấy vị trí, nhập mô tả và gửi lên API; API lưu ảnh và gọi `sp_Incident_Create`. Từ chối quyền camera hoặc vị trí vẫn gửi được phần còn lại.
2. **Quầy gần nhất.** Danh sách quầy sắp xếp theo khoảng cách, hiển thị "cách bạn x m"; bấm một quầy mở bản đồ và căn giữa vào quầy đó.
3. **Ảnh món ăn.** Cho nhân viên cập nhật ảnh món ăn (vai trò `staff`), lưu đường dẫn qua `sp_Product_UpdateImage`; thực đơn hiển thị ảnh mới.

## Tài liệu tham khảo

- Android Developers - Request runtime permissions: https://developer.android.com/training/permissions/requesting
- Expo - Permissions: https://docs.expo.dev/guides/permissions/
- Expo - ImagePicker: https://docs.expo.dev/versions/latest/sdk/imagepicker/
- Expo - Location: https://docs.expo.dev/versions/latest/sdk/location/
- Expo - MapView: https://docs.expo.dev/versions/latest/sdk/map-view/
- Expo - Development builds: https://docs.expo.dev/develop/development-builds/introduction/
- NestJS - File upload: https://docs.nestjs.com/techniques/file-upload
