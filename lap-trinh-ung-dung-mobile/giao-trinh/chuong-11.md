# Chương 11. Triển khai backend lên server Khoa, build và phát hành ứng dụng

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Dựng CSDL SQL Server trên Windows Server của Khoa từ các script trong `database/` và cấu hình tài khoản chỉ có quyền `EXECUTE`.
- Triển khai backend NestJS (REST API và Socket.IO) thành dịch vụ chạy nền, kiểm tra được từ máy khác.
- Cấu hình ứng dụng Expo theo môi trường bằng `app.config.ts` và `eas.json`.
- Build file APK, AAB bằng EAS Build; phát hành bản cập nhật OTA bằng EAS Update.
- Chuẩn bị hồ sơ phát hành và theo dõi lỗi sau phát hành.

## 11.1. Từ máy phát triển đến server

### 11.1.1. Kiến trúc khi triển khai

Trong mười buổi trước, backend và SQL Server chạy trên máy cá nhân; điện thoại phải cùng mạng Wi-Fi mới gọi được API. Sau chương này:

```text
Điện thoại Android (APK)
   │  HTTP REST + Socket.IO (cùng địa chỉ, cùng cổng)
   ▼
Windows Server của Khoa
   ├── Backend NestJS (dịch vụ nền, đọc .env)
   │     └── mssql → chỉ gọi stored procedure
   ├── SQL Server (CSDL của nhóm, login chỉ có quyền EXECUTE)
   └── Thư mục uploads/ (ảnh tải lên)
```

Mỗi nhóm được Khoa cấp quyền truy cập một server (hoặc một phần server) và có **bộ phận hỗ trợ triển khai**. Các thao tác cần quyền quản trị server (tạo login cấp server, mở cổng firewall, đăng ký dịch vụ) thực hiện theo hướng dẫn hoặc với sự hỗ trợ của bộ phận này. Chương này mô tả **những gì cần làm và cách kiểm tra**; công cụ cụ thể theo quy định của Khoa.

### 11.1.2. Thông tin cần có trước khi triển khai

| Thông tin | Nguồn |
|---|---|
| Địa chỉ server (IP hoặc tên miền), cách truy cập (Remote Desktop…) | Bộ phận hỗ trợ |
| Tên instance SQL Server, tài khoản để chạy script | Bộ phận hỗ trợ |
| Cổng được cấp cho API của nhóm | Bộ phận hỗ trợ |
| Phiên bản Node.js trên server | Kiểm tra bằng `node -v`, so với máy phát triển |
| Repo backend, nhánh phát hành | Nhóm |
| Danh sách biến môi trường | README của backend |

Nhóm nên chuẩn bị đủ các thông tin này trước buổi 11, để thời gian trên lớp dùng cho việc triển khai và kiểm thử.

## 11.2. Triển khai CSDL

### 11.2.1. Dựng CSDL từ script

Chương 7 đã tổ chức thư mục `database/` theo phiên bản. Trên server:

1. Tạo CSDL trống, ví dụ `LhuFood`.
2. Chạy lần lượt các script theo thứ tự số: `01-tables.sql`, `02-procedures.sql`, `03-auth.sql`, …, `08-notifications.sql`, cuối cùng `99-seed.sql`.
3. Kiểm tra: số bảng, số thủ tục, dữ liệu mẫu đúng như trên máy phát triển.

Có thể chạy bằng SQL Server Management Studio (mở từng file, chọn đúng CSDL, Execute) hoặc bằng `sqlcmd` trong PowerShell:

```powershell
Get-ChildItem .\database\*.sql | Sort-Object Name | ForEach-Object {
  Write-Host "Chạy $($_.Name)"
  sqlcmd -S localhost -d LhuFood -E -b -f 65001 -i $_.FullName
}
```

- `-E`: đăng nhập bằng tài khoản Windows hiện tại (hoặc dùng `-U`, `-P` theo tài khoản được cấp).
- `-b`: dừng với mã lỗi khi script lỗi, không chạy tiếp script sau trên CSDL dở dang.
- `-f 65001`: đọc file theo UTF-8 để chuỗi tiếng Việt (`N'Cơm gà'`) không bị lỗi phông.
- Thư mục `database/tests/` (Chương 10) **không** được chạy trên server thật; vòng lặp trên chỉ lấy file ở cấp `database/`.

Nếu một script lỗi giữa chừng trên CSDL trống, cách nhanh nhất là xóa CSDL, sửa script và chạy lại từ đầu. Đó cũng là lý do script phải dựng được CSDL từ con số không.

### 11.2.2. Tài khoản cho backend

Như Chương 6, backend dùng login riêng chỉ có quyền thực thi thủ tục:

```sql
CREATE LOGIN lhufood_api WITH PASSWORD = N'<mật khẩu mạnh>';
GO
USE LhuFood;
CREATE USER lhufood_api FOR LOGIN lhufood_api;
GRANT EXECUTE ON SCHEMA::dbo TO lhufood_api;
```

Kiểm tra quyền bằng cách đăng nhập SQL Server Management Studio với `lhufood_api`:

```sql
SELECT * FROM Products;              -- phải báo lỗi: The SELECT permission was denied
EXEC sp_Product_GetList @Page = 1, @PageSize = 5;   -- chạy được
```

Mật khẩu trên server **khác** mật khẩu trên máy phát triển, chỉ lưu trong `.env` của server và không gửi qua nhóm chat công khai.

### 11.2.3. Cập nhật CSDL sau lần triển khai đầu

Sau khi đã có dữ liệu thật trên server, **không** xóa CSDL để chạy lại từ đầu. Thay đổi cấu trúc được viết thành script mới (`09-...sql`) có kiểm tra trước khi chạy (Chương 7) và chỉ chạy script mới đó. Trước mỗi lần cập nhật, yêu cầu sao lưu CSDL theo quy trình của Khoa.

## 11.3. Triển khai backend NestJS

### 11.3.1. Build và cấu hình

Trên server, lấy mã nguồn từ repo (nhánh phát hành) rồi:

```powershell
npm ci            # cài đúng phiên bản trong package-lock.json
npm run build     # biên dịch TypeScript ra thư mục dist/
```

`npm ci` khác `npm install` ở chỗ cài **đúng** phiên bản đã khóa trong `package-lock.json` và báo lỗi nếu file này không khớp `package.json`. Vì vậy `package-lock.json` phải được commit.

Tạo file `.env` cạnh `package.json` (file này không có trong repo):

```text
PORT=3000
DB_SERVER=localhost
DB_NAME=LhuFood
DB_USER=lhufood_api
DB_PASSWORD=<mật khẩu của server>
JWT_SECRET=<chuỗi ngẫu nhiên dài, khác máy phát triển>
```

Tạo chuỗi ngẫu nhiên cho `JWT_SECRET` bằng Node.js:

```powershell
node -e "console.log(require('crypto').randomBytes(48).toString('hex'))"
```

Đổi `JWT_SECRET` làm mọi token cũ mất hiệu lực, nên token cấp ở máy phát triển không dùng được trên server, đúng như mong muốn.

### 11.3.2. Chạy thử

```powershell
node dist/main.js
```

Trên chính server, mở `http://localhost:3000/docs` (Swagger, Chương 5). Đăng nhập bằng tài khoản mẫu, gọi API danh sách món, tạo đơn thử. Nếu API không khởi động, đọc lỗi đầu tiên trong cửa sổ: thường là thiếu biến môi trường, sai mật khẩu SQL, hoặc cổng đã bị chương trình khác dùng.

Thêm một endpoint kiểm tra sức khỏe để bộ phận hỗ trợ và nhóm biết nhanh API có đang chạy và kết nối được CSDL:

```ts
// src/health/health.controller.ts
import { Controller, Get } from '@nestjs/common';
import { DatabaseService } from '../database/database.service';

@Controller('health')
export class HealthController {
  constructor(private readonly db: DatabaseService) {}

  @Get()
  async check() {
    await this.db.execute('sp_Health_Check');
    return { status: 'ok', time: new Date().toISOString() };
  }
}
```

```sql
-- database/09-health.sql
CREATE OR ALTER PROCEDURE sp_Health_Check
AS
BEGIN
  SET NOCOUNT ON;
  SELECT 1 AS ok;
END;
```

Thủ tục này giữ đúng quy tắc của học phần: kể cả kiểm tra kết nối cũng đi qua stored procedure.

### 11.3.3. Chạy thành dịch vụ nền

Chạy `node dist/main.js` trong một cửa sổ PowerShell chỉ phù hợp để thử: đóng cửa sổ, đăng xuất Remote Desktop hoặc server khởi động lại là API dừng. Khi triển khai, API phải chạy như **dịch vụ nền** có các tính chất:

- Tự khởi động khi Windows Server khởi động.
- Tự chạy lại khi tiến trình Node.js bị lỗi và thoát.
- Ghi đầu ra (log) ra file để xem lại sau.
- Đọc được file `.env` (thư mục làm việc là thư mục chứa mã backend).

Trên Windows, có nhiều cách đạt được điều này (đăng ký Windows Service bằng một công cụ quản lý dịch vụ, hoặc trình quản lý tiến trình cho Node.js). Nhóm thực hiện **theo công cụ và hướng dẫn của bộ phận hỗ trợ triển khai**, rồi ghi lại vào README:

- Tên dịch vụ, cách khởi động, dừng, khởi động lại.
- Vị trí file log.
- Các bước cập nhật phiên bản mới (mục 11.3.5).

Kiểm tra: khởi động lại dịch vụ (hoặc nhờ bộ phận hỗ trợ khởi động lại server), sau đó mở `/health` mà không đăng nhập vào server.

### 11.3.4. Mở cổng và kiểm tra từ máy khác

Chương 5 đã cấu hình `app.listen(port, '0.0.0.0')` để API lắng nghe trên mọi địa chỉ mạng, không chỉ `localhost`. Ngoài ra, Windows Firewall mặc định chặn kết nối đến từ bên ngoài; cổng của API phải được mở (thường do bộ phận hỗ trợ thực hiện theo yêu cầu của nhóm, kèm số cổng).

Socket.IO (Chương 9) chạy trên **cùng server HTTP và cùng cổng** với REST API, nên chỉ cần mở một cổng.

Kiểm tra theo thứ tự, mỗi bước loại trừ một nguyên nhân:

| Bước | Kiểm tra | Nếu lỗi |
|---|---|---|
| 1 | Trên server: `http://localhost:<cổng>/health` | API chưa chạy hoặc lỗi CSDL: xem log dịch vụ |
| 2 | Trên server: `http://<IP-server>:<cổng>/health` | API chỉ lắng nghe `localhost`: kiểm tra `main.ts` |
| 3 | Từ máy khác trong mạng: `http://<IP-server>:<cổng>/docs` | Firewall chặn cổng |
| 4 | Từ điện thoại dùng 4G (nếu server cho phép truy cập từ ngoài) | Mạng Khoa chỉ cho truy cập nội bộ: hỏi bộ phận hỗ trợ |

### 11.3.5. Cập nhật phiên bản backend

```powershell
git pull                      # lấy mã mới trên nhánh phát hành
npm ci
npm run build
# chạy script CSDL mới (nếu có)
# khởi động lại dịch vụ theo README
```

Chỉ triển khai mã đã qua pull request và đã chạy test (Chương 10). Ghi phiên bản và ngày triển khai vào `CHANGELOG.md` hoặc phần Releases của repo.

### 11.3.6. Ảnh tải lên

Thư mục `uploads/` (Chương 8) nằm cạnh mã backend trên server. Lưu ý:

- Không xóa thư mục này khi cập nhật mã.
- Thư mục cần được sao lưu cùng CSDL: CSDL chỉ lưu đường dẫn, mất thư mục là ảnh mất mà đường dẫn vẫn còn.
- Tài khoản chạy dịch vụ phải có quyền ghi vào thư mục.

## 11.4. Cấu hình ứng dụng cho bản phát hành

### 11.4.1. Từ `app.json` sang `app.config.ts`

`app.json` là cấu hình tĩnh. Đổi sang `app.config.ts` để viết cấu hình bằng TypeScript và đọc biến môi trường khi cần:

```ts
// app.config.ts
import { ExpoConfig } from 'expo/config';

const config: ExpoConfig = {
  name: 'LHU Food',
  slug: 'lhu-food',
  version: '1.0.0',
  orientation: 'portrait',
  icon: './assets/icon.png',
  scheme: 'lhufood',
  splash: {
    image: './assets/splash.png',
    resizeMode: 'contain',
    backgroundColor: '#ffffff',
  },
  android: {
    package: 'vn.edu.lhu.lhufood',
    versionCode: 1,
    adaptiveIcon: {
      foregroundImage: './assets/adaptive-icon.png',
      backgroundColor: '#ffffff',
    },
    config: {
      googleMaps: { apiKey: process.env.GOOGLE_MAPS_API_KEY },
    },
  },
  plugins: ['expo-router' /* , các plugin của Chương 8, 9 */],
  extra: {
    eas: { projectId: '<sinh ra khi chạy eas init>' },
  },
};

export default config;
```

Khi chuyển, chép đủ nội dung `app.json` hiện có (quyền, plugin camera, vị trí, thông báo) sang file mới rồi xóa `app.json`.

| Trường | Ý nghĩa |
|---|---|
| `name` | Tên hiển thị dưới biểu tượng |
| `slug` | Tên dự án trên Expo |
| `version` | Phiên bản người dùng thấy (1.0.0, 1.0.1…) |
| `android.package` | Định danh duy nhất của ứng dụng trên Android và Google Play; **không đổi** sau khi phát hành |
| `android.versionCode` | Số nguyên, **tăng** mỗi lần đưa bản mới lên cửa hàng |
| `icon`, `adaptiveIcon`, `splash` | Biểu tượng và màn hình khởi động |

`GOOGLE_MAPS_API_KEY` (bản đồ, Chương 8) không có tiền tố `EXPO_PUBLIC_`: nó chỉ dùng khi build để ghi vào cấu hình Android. Tạo khóa trong Google Cloud Console theo hướng dẫn MapView của Expo và giới hạn khóa theo package name.

### 11.4.2. Địa chỉ API theo môi trường

`lib/api.ts` (Chương 5) và `useRealtime` (Chương 9) đều đọc `process.env.EXPO_PUBLIC_API_URL`. Giá trị này khác nhau theo môi trường:

| Môi trường | `EXPO_PUBLIC_API_URL` | Khai báo ở |
|---|---|---|
| Phát triển | `http://192.168.1.10:3000` (máy cá nhân) | `.env` của dự án ứng dụng |
| Bản preview (APK) | `http://<IP-server-Khoa>:<cổng>` | `eas.json`, profile `preview` |
| Bản production | `https://<tên-miền>` | `eas.json`, profile `production` |

Biến `EXPO_PUBLIC_*` được **thay vào mã khi đóng gói**. Đổi địa chỉ server sau khi build thì phải build lại hoặc gửi EAS Update (mục 11.6), không có chỗ nào để sửa trong APK đã cài.

### 11.4.3. Kết nối HTTP không mã hóa

Từ Android 9, ứng dụng mặc định **không được** kết nối HTTP không mã hóa (cleartext). Khi chạy bằng Expo Go hoặc bản phát triển, giới hạn này được nới để tiện phát triển; bản APK build cho người dùng thì không. Hiện tượng: Swagger mở được trên trình duyệt, nhưng APK báo "Network request failed".

- **Cách đúng:** server Khoa cung cấp HTTPS (chứng chỉ, tên miền). Hỏi bộ phận hỗ trợ trước.
- **Nếu chỉ có HTTP trong phạm vi đồ án:** cho phép cleartext trong bản build bằng plugin `expo-build-properties` (tùy chọn `android.usesCleartextTraffic`), theo hướng dẫn trong tài liệu Expo. Ghi rõ trong báo cáo đây là cấu hình tạm cho môi trường học tập; bản phát hành thật phải dùng HTTPS.

## 11.5. EAS Build

### 11.5.1. Chuẩn bị

EAS Build biên dịch ứng dụng trên máy chủ của Expo, nên không cần cài Android Studio. Mỗi sinh viên dùng tài khoản Expo miễn phí đã đăng ký.

```bash
npm install -g eas-cli
eas login
eas init                # tạo dự án trên Expo, ghi projectId vào cấu hình
eas build:configure     # tạo eas.json
```

Dự án Expo thuộc tài khoản của người chạy `eas init`. Nhóm thống nhất một tài khoản sở hữu dự án; các thành viên khác có thể được mời vào dự án theo hướng dẫn trên trang Expo.

### 11.5.2. Profile trong `eas.json`

```json
{
  "cli": { "appVersionSource": "local" },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal",
      "channel": "preview",
      "android": { "buildType": "apk" },
      "env": {
        "EXPO_PUBLIC_API_URL": "http://<IP-server-Khoa>:<cổng>"
      }
    },
    "production": {
      "channel": "production",
      "android": { "buildType": "app-bundle" },
      "env": {
        "EXPO_PUBLIC_API_URL": "https://<tên-miền>"
      }
    }
  }
}
```

| Profile | Đầu ra | Dùng cho |
|---|---|---|
| `development` | APK có công cụ phát triển | Thay Expo Go khi cần thư viện native (mở rộng) |
| `preview` | **APK** | Cài trực tiếp lên điện thoại để kiểm thử và Demo Day (**bắt buộc**) |
| `production` | **AAB** (Android App Bundle) | Tải lên Google Play; không cài trực tiếp được |

Khóa `GOOGLE_MAPS_API_KEY` là bí mật dùng khi build, nên không ghi vào `eas.json` (file nằm trong repo). Khai báo nó thành biến môi trường của dự án trên trang Expo (EAS environment variables) theo hướng dẫn của Expo.

### 11.5.3. Build APK

```bash
eas build -p android --profile preview
```

Lệnh tải mã nguồn lên Expo, xếp hàng và build. Khi xong, terminal và trang Expo hiển thị **link tải và mã QR**; quét mã trên điện thoại Android để tải và cài APK (cần cho phép cài ứng dụng từ nguồn này trong cài đặt Android).

Kiểm tra trên APK, không phải Expo Go:

1. Đăng nhập, xem danh sách món: kết nối API trên server Khoa.
2. Đặt món: kiểm tra đơn trong SQL Server trên server.
3. Đổi trạng thái đơn từ tài khoản nhân viên: nhận thông báo realtime (Socket.IO).
4. Camera, ảnh, vị trí, bản đồ: quyền được hỏi đúng, bản đồ không trắng.
5. Tắt mở lại ứng dụng: phiên đăng nhập và giỏ hàng còn.

### 11.5.4. Ký ứng dụng

Mỗi bản cài Android phải được **ký** bằng một khóa (keystore). Ở lần build đầu, EAS đề nghị tạo keystore và lưu trên máy chủ Expo; chọn đồng ý. Lưu ý:

- Mọi bản cập nhật của ứng dụng phải ký bằng **cùng** keystore. Android từ chối cài đè bản ký bằng khóa khác; Google Play từ chối bản cập nhật.
- Keystore gắn với tài khoản sở hữu dự án; không xóa dự án trên Expo khi chưa tải keystore về sao lưu (`eas credentials`).

### 11.5.5. Lượt build miễn phí

Tài khoản Expo miễn phí có **giới hạn số lượt build mỗi tháng** và build phải xếp hàng (có khi vài chục phút). Hạn mức cụ thể xem trên trang giá của Expo vì có thể thay đổi. Để không hết lượt build sát ngày Demo:

- Kiểm thử kỹ bằng Expo Go hoặc bản development trước khi build preview.
- Chạy `npx expo-doctor` để phát hiện lỗi cấu hình và phiên bản thư viện không tương thích.
- Kiểm tra `eas.json`, `app.config.ts` (địa chỉ API, quyền, khóa bản đồ) trước mỗi lần build.
- Thay đổi chỉ ở JavaScript thì dùng EAS Update thay vì build lại.
- Phân công: không để cả nhóm cùng build trong một ngày.
- Mở rộng: build cục bộ (`eas build --local`) không tốn lượt build nhưng cần cài Android SDK và Java trên máy.

### 11.5.6. iOS (phần mở rộng)

Android là bắt buộc; iOS là phần mở rộng. Để cài lên iPhone thật qua TestFlight cần tài khoản Apple Developer (trả phí). Nhóm không có tài khoản có thể demo trên iOS Simulator (cần máy Mac) bằng `eas build -p ios --profile development` với tùy chọn build cho simulator theo hướng dẫn của Expo. Kiểm tra các khác biệt đã gặp: quyền (chuỗi giải thích trong `ios.infoPlist`), vùng an toàn (tai thỏ), bàn phím che ô nhập.

## 11.6. EAS Update

### 11.6.1. Cập nhật qua mạng (OTA)

Ứng dụng React Native gồm hai phần: **mã native** (đã biên dịch trong APK) và **gói JavaScript** (giao diện và logic). EAS Update cho phép gửi gói JavaScript mới tới các bản đã cài mà không build lại. Ứng dụng kiểm tra bản cập nhật khi mở và áp dụng ở lần mở tiếp theo (hành vi mặc định).

```bash
npx expo install expo-updates
eas update:configure      # thêm cấu hình updates và runtimeVersion
```

Sau khi cấu hình, **build lại** một lần để bản APK có khả năng nhận cập nhật. Từ đó, mỗi lần sửa lỗi JavaScript:

```bash
eas update --channel preview --message "Sửa lỗi hiển thị tổng tiền"
```

### 11.6.2. Channel và runtime version

- **Channel:** bản build profile `preview` gắn channel `preview` (khai báo trong `eas.json`), chỉ nhận bản cập nhật gửi lên channel đó. Gửi nhầm channel thì người dùng không nhận được.
- **Runtime version:** đánh dấu phần native mà gói JavaScript tương thích. Bản cập nhật chỉ đến các bản build cùng runtime version, tránh gửi mã JavaScript cần một thư viện native mà APK cũ không có.

### 11.6.3. Khi nào phải build lại

| Thay đổi | EAS Update | Build lại |
|---|---|---|
| Sửa giao diện, chữ, màu, logic trong mã TypeScript | ✔ | |
| Sửa địa chỉ API trong biến `EXPO_PUBLIC_*` | ✔ (biến được thay khi tạo gói cập nhật) | |
| Thêm thư viện có mã native (camera, bản đồ, thông báo…) | | ✔ |
| Thêm hoặc đổi quyền, plugin, icon, splash, tên, package | | ✔ |
| Đổi phiên bản Expo SDK | | ✔ |

Với tài khoản miễn phí, EAS Update là cách tiết kiệm lượt build khi sửa lỗi trong tuần cuối trước Demo Day. Gửi bản cập nhật cũng phải qua kiểm thử: một bản cập nhật lỗi đến tay mọi người dùng ngay lần mở ứng dụng sau.

## 11.7. Hồ sơ phát hành

### 11.7.1. Hồ sơ cửa hàng

Đồ án không bắt buộc đưa ứng dụng lên Google Play (cần tài khoản nhà phát triển trả phí và quy trình duyệt), nhưng nhóm chuẩn bị hồ sơ như khi phát hành thật, đặt trong thư mục `store-listing/` của repo ứng dụng:

| Thành phần | Yêu cầu |
|---|---|
| Tên ứng dụng | Ngắn, đúng với tên trong `app.config.ts` |
| Mô tả ngắn | Một câu, tối đa 80 ký tự |
| Mô tả đầy đủ | Chức năng chính, đối tượng người dùng; không phóng đại |
| Biểu tượng | 512 × 512 px, PNG |
| Ảnh nổi bật (feature graphic) | 1024 × 500 px |
| Ảnh chụp màn hình | Ít nhất 4 ảnh thật từ điện thoại, thể hiện luồng chính |
| Chính sách quyền riêng tư | Xem mục 11.7.2 |

Kích thước và giới hạn có thể thay đổi; đối chiếu trang hướng dẫn của Google Play Console khi phát hành thật.

### 11.7.2. Chính sách quyền riêng tư

Ứng dụng thu thập dữ liệu cá nhân (tài khoản, ảnh, vị trí) phải có chính sách quyền riêng tư công khai. Nội dung tối thiểu:

- Dữ liệu thu thập: họ tên, email, mật khẩu (lưu dạng băm), ảnh đại diện, vị trí khi chọn nơi nhận, lịch sử đơn hàng.
- Mục đích: xác thực, xử lý đơn hàng, gửi thông báo trạng thái đơn.
- Nơi lưu: SQL Server trên server của Khoa CNTT, Trường Đại học Lạc Hồng; ứng dụng không lưu dữ liệu cá nhân trên thiết bị ngoài token đăng nhập (SecureStore) và giỏ hàng.
- Chia sẻ: không chia sẻ với bên thứ ba (trừ dịch vụ bản đồ khi hiển thị bản đồ).
- Quyền của người dùng: xem, sửa thông tin; yêu cầu xóa tài khoản và cách liên hệ.
- Giải thích từng quyền: camera (chụp ảnh đánh giá món), vị trí (chọn nơi nhận), thông báo (trạng thái đơn).

Chính sách phải **đúng với ứng dụng thật**. Xin quyền mà chính sách không nhắc tới, hoặc chính sách nói "không thu thập vị trí" trong khi ứng dụng có, là lỗi nghiêm trọng khi phát hành thật.

## 11.8. Vận hành sau phát hành

### 11.8.1. Log phía backend

NestJS có sẵn lớp `Logger`. Ghi log có ngữ cảnh ở các chỗ quan trọng, đặc biệt trong `DatabaseService` khi thủ tục lỗi ngoài các mã nghiệp vụ:

```ts
import { Logger } from '@nestjs/common';

private readonly logger = new Logger(DatabaseService.name);

// trong khối catch của execute(), ngay trước dòng `throw err;`
// (các mã 50400/50404/50409 đã được chuyển thành HTTP ở các dòng phía trên)
this.logger.error(`${procedure} lỗi ${err?.number}: ${err?.message}`);
throw err;
```

Lỗi nghiệp vụ (50400/50404/50409) là bình thường, không cần ghi mức `error`. Đầu ra của tiến trình được dịch vụ nền ghi ra file (mục 11.3.3); khi có sự cố, xem file log trên server trước khi đoán nguyên nhân. Không ghi mật khẩu, token, dữ liệu cá nhân vào log.

### 11.8.2. Lỗi phía ứng dụng

Lỗi trên điện thoại người dùng không hiện trong terminal của bạn. Tối thiểu:

- Hiển thị thông báo thân thiện thay vì màn hình trắng khi một màn hình gặp lỗi (Expo Router hỗ trợ khai báo `ErrorBoundary` cho từng route).
- Cho người dùng gửi phản hồi kèm phiên bản ứng dụng (`expo-application` hoặc `expo-constants` đọc được phiên bản).
- Mở rộng: tích hợp dịch vụ theo dõi lỗi như Sentry để nhận báo cáo lỗi kèm stack trace.

### 11.8.3. Quy trình khi người dùng báo lỗi

1. Ghi vào bug log (Chương 10) với phiên bản ứng dụng, thiết bị, thời điểm.
2. Đối chiếu log backend tại thời điểm đó.
3. Tái hiện, viết test, sửa.
4. Lỗi JavaScript: gửi EAS Update; lỗi native hoặc cấu hình: build bản mới, tăng `versionCode`.
5. Lỗi ở API hoặc thủ tục: triển khai lại backend theo mục 11.3.5; ứng dụng không cần cập nhật.

## 11.9. Mã nguồn và tài liệu bổ sung của chương

```text
lhu-food/
├── app.config.ts            (thay cho app.json)
├── eas.json
└── store-listing/
    ├── icon-512.png
    ├── feature-graphic.png
    ├── screenshots/
    ├── description.md
    └── privacy-policy.md

lhu-food-api/
├── src/health/health.controller.ts
├── database/09-health.sql
└── README.md                (mục "Triển khai trên Windows Server")
```

Mục README "Triển khai trên Windows Server" gồm: yêu cầu (phiên bản Node.js, SQL Server), thứ tự chạy script CSDL, tạo login `EXECUTE`, danh sách biến môi trường (không ghi giá trị bí mật), lệnh build, cách chạy dịch vụ nền, cổng cần mở, cách cập nhật phiên bản, vị trí file log. Tiêu chí: một người không thuộc nhóm đọc README là triển khai lại được.

## Tóm tắt chương

- CSDL trên server được dựng từ các script `database/` chạy theo thứ tự số; backend dùng login chỉ có quyền `EXECUTE`.
- Backend build bằng `npm ci` và `npm run build`, đọc `.env` riêng của server, chạy thành dịch vụ nền theo hướng dẫn của bộ phận hỗ trợ; REST API và Socket.IO dùng chung một cổng.
- Kiểm tra triển khai theo từng bước: localhost, IP server, máy khác, mạng ngoài.
- `app.config.ts` khai báo tên, package, phiên bản, icon; `EXPO_PUBLIC_API_URL` khác nhau theo profile trong `eas.json`.
- Android chặn HTTP không mã hóa trong bản build; dùng HTTPS hoặc cấu hình tạm cho đồ án.
- EAS Build: profile `preview` tạo APK (bắt buộc), `production` tạo AAB; giữ keystore; tiết kiệm lượt build miễn phí.
- EAS Update gửi thay đổi JavaScript qua mạng; thay đổi native và cấu hình phải build lại.
- Hồ sơ phát hành gồm mô tả, hình ảnh và chính sách quyền riêng tư đúng với ứng dụng; sau phát hành theo dõi log và lỗi.

## Câu hỏi ôn tập

1. Vì sao backend không dùng tài khoản `sa` mà dùng login chỉ có quyền `EXECUTE`? Kiểm tra quyền của login đó bằng cách nào?
2. Nêu các tính chất mà một dịch vụ nền chạy API cần có. Vì sao không để API chạy trong cửa sổ PowerShell?
3. Swagger mở được trên server nhưng không mở được từ máy khác. Nêu các nguyên nhân có thể và thứ tự kiểm tra.
4. `android.package` và `android.versionCode` khác nhau thế nào? Trường nào được đổi giữa các lần phát hành?
5. Vì sao APK báo "Network request failed" trong khi Expo Go trên cùng điện thoại kết nối được API?
6. So sánh profile `preview` và `production`. Nhóm cần file nào cho Demo Day?
7. Những thay đổi nào gửi được bằng EAS Update và những thay đổi nào phải build lại? Giải thích dựa trên cấu trúc ứng dụng React Native.
8. Chính sách quyền riêng tư của LHU Food cần nêu những nội dung gì?

## Bài tập

1. **Triển khai của nhóm.** Triển khai backend và CSDL của đề tài lên Windows Server của Khoa; chụp màn hình bảng kiểm tra 4 bước ở mục 11.3.4 và kết quả `/health` sau khi khởi động lại dịch vụ.
2. **README triển khai.** Viết mục "Triển khai trên Windows Server" cho repo backend. Nhờ một thành viên nhóm khác (hoặc một nhóm khác) đọc và góp ý những bước chưa rõ.
3. **APK cho người ngoài nhóm.** Build APK profile `preview`; nhờ một người không thuộc nhóm cài và thực hiện luồng chính trên điện thoại của họ. Ghi lại các lỗi gặp phải vào bug log.
4. **EAS Update.** Cấu hình EAS Update, build lại một lần, sau đó gửi một bản cập nhật sửa giao diện; chứng minh bản APK đã cài nhận được thay đổi mà không cài lại.
5. **Hồ sơ cửa hàng.** Hoàn thành thư mục `store-listing/` theo mục 11.7.

## Tài liệu tham khảo

- Expo - Create your first build: https://docs.expo.dev/build/setup/
- Expo - Configure EAS Build with eas.json: https://docs.expo.dev/build/eas-json/
- Expo - Build APKs for Android emulators and devices: https://docs.expo.dev/build-reference/apk/
- Expo - App config (app.json / app.config.ts): https://docs.expo.dev/workflow/configuration/
- Expo - Environment variables in Expo: https://docs.expo.dev/guides/environment-variables/
- Expo - Environment variables in EAS: https://docs.expo.dev/eas/environment-variables/
- Expo - App signing / credentials: https://docs.expo.dev/app-signing/app-credentials/
- Expo - BuildProperties (expo-build-properties): https://docs.expo.dev/versions/latest/sdk/build-properties/
- Expo - MapView (Google Maps API key): https://docs.expo.dev/versions/latest/sdk/map-view/
- Expo - Get started with EAS Update: https://docs.expo.dev/eas-update/getting-started/
- Expo - Runtime versions and updates: https://docs.expo.dev/eas-update/runtime-versions/
- NestJS - Configuration: https://docs.nestjs.com/techniques/configuration
- NestJS - Logger: https://docs.nestjs.com/techniques/logger
- Microsoft - sqlcmd utility: https://learn.microsoft.com/sql/tools/sqlcmd/sqlcmd-utility
- Google Play Console Help - Add preview assets: https://support.google.com/googleplay/android-developer/answer/9866151
