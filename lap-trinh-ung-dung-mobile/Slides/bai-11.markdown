# Bài 11: Triển khai backend lên server Khoa, build & phát hành
Sprint 4 · Đưa sản phẩm ra ngoài phòng máy

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Triển khai CSDL SQL Server và backend NestJS lên Windows Server của Khoa
- Cấu hình ứng dụng theo môi trường
- Build APK/AAB bằng EAS Build; cập nhật OTA bằng EAS Update
- Chuẩn bị hồ sơ phát hành
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1, CLO2. Kiểm tra nhóm đã có tài khoản Expo và thông tin server.

---

## Slide 2: Từ phòng máy ra thế giới
**Nội dung chính**:
- Hiện tại: app chỉ chạy khi máy bạn bật, cùng Wi-Fi
- Mục tiêu: người ngoài nhóm cài APK, đặt món qua mạng, nhận thông báo realtime
```text
Điện thoại (APK) → API NestJS trên Windows Server Khoa → SQL Server
                 ← Socket.IO (cùng server)
```

---

## Slide 3: Triển khai CSDL
**Nội dung chính**:
- Chạy theo thứ tự số: 01-tables.sql → 02-procedures.sql → … → 08-notifications.sql → 99-seed.sql
- Script chạy lại được: CREATE OR ALTER PROCEDURE, kiểm tra tồn tại
- Dùng SQL Server Management Studio hoặc sqlcmd

---

## Slide 4: Tài khoản chỉ có quyền EXECUTE
**Nội dung chính**:
```sql
CREATE LOGIN lhufood_api WITH PASSWORD = N'<mật khẩu mạnh>';
USE LhuFood;
CREATE USER lhufood_api FOR LOGIN lhufood_api;
GRANT EXECUTE ON SCHEMA::dbo TO lhufood_api;
```
- Không dùng sa; không cấp quyền trực tiếp trên bảng
- Kiểm tra: SELECT bị từ chối, EXEC thủ tục chạy được

---

## Slide 5: Chạy backend trên Windows Server
**Nội dung chính**:
- npm ci → npm run build → node dist/main.js
- File .env trên server: DB_USER, DB_PASSWORD, JWT_SECRET khác máy phát triển
- **Dịch vụ nền**: theo hướng dẫn của bộ phận hỗ trợ, tự chạy lại khi server khởi động lại
- **Firewall**: mở cổng API và socket
- Kiểm tra Swagger từ một máy khác
**Ghi chú giảng viên**:
- Các thao tác cấp server (login, firewall, service) phối hợp với bộ phận hỗ trợ triển khai của Khoa.

---

## Slide 6: README triển khai
**Nội dung chính**:
- Phiên bản Node.js, thứ tự chạy script CSDL
- Danh sách biến môi trường (không ghi giá trị bí mật)
- Cách khởi động lại dịch vụ, vị trí file log
- Người khác đọc README phải triển khai lại được

---

## Slide 7: app.config.ts
**Nội dung chính**:
```ts
const config: ExpoConfig = {
  name: 'LHU Food', slug: 'lhu-food', version: '1.0.0',
  icon: './assets/icon.png',
  android: { package: 'vn.edu.lhu.lhufood', versionCode: 1 },
};
```
- package duy nhất, không đổi sau khi phát hành
- versionCode tăng mỗi lần đưa bản mới lên cửa hàng

---

## Slide 8: Địa chỉ theo môi trường
**Nội dung chính**:
- Phát triển: EXPO_PUBLIC_API_URL trỏ về máy cá nhân
- Bản build: trỏ về server Khoa, khai báo trong eas.json
- EXPO_PUBLIC_* được nhúng vào app: không đặt mật khẩu, khóa bí mật
- HTTP bị Android chặn trong bản build: cho phép cleartext cho đồ án, phát hành thật dùng HTTPS
- Bản đồ (bài 08): cần API key Google Maps cho Android

---

## Slide 9: EAS Build
**Nội dung chính**:
```bash
npm install -g eas-cli
eas login
eas init
eas build:configure
eas build -p android --profile preview
```
- **preview**: APK, cài từ mã QR (bắt buộc)
- **production**: AAB cho Google Play

---

## Slide 10: Ký ứng dụng và lượt build miễn phí
**Nội dung chính**:
- Lần đầu EAS tạo keystore và lưu trên Expo
- Mất keystore → không cập nhật được app trên cửa hàng
- Tài khoản miễn phí: lượt build có giới hạn, phải xếp hàng
- Trước khi build: chạy thử kỹ, kiểm tra eas.json, chạy npx expo-doctor
- Phân công build từ tài khoản của các thành viên khác nhau

---

## Slide 11: EAS Update (OTA)
**Nội dung chính**:
```bash
npx expo install expo-updates
eas update:configure
eas update --channel preview --message "Sửa lỗi tổng tiền"
```
- Chỉ đến bản build cùng channel và runtime version
- **Không** dùng cho: thư viện native, quyền, icon, cấu hình

---

## Slide 12: Lỗi chỉ có trên APK
**Nội dung chính**:
- Lỗi mạng: biến môi trường chưa vào bản build, HTTP bị chặn
- Máy khác không vào API: firewall, API chỉ lắng nghe localhost
- Bản đồ trắng: thiếu API key Google Maps
- Thiếu quyền: chưa khai báo trong cấu hình
**Hoạt động**: Mỗi nhóm dự đoán lỗi dễ gặp nhất với ứng dụng của mình

---

## Slide 13: Hồ sơ cửa hàng
**Nội dung chính**:
- Tên, mô tả ngắn (≤ 80 ký tự), mô tả đầy đủ
- Icon 512×512, feature graphic, ≥ 4 ảnh chụp màn hình thật
- **Chính sách quyền riêng tư**: thu thập gì, dùng làm gì, lưu ở đâu, xóa tài khoản thế nào
- Lý do xin từng quyền: camera, vị trí, thông báo

---

## Slide 14: Vận hành sau phát hành
**Nội dung chính**:
- Backend ghi log: request lỗi, exception, thủ tục chậm
- App bắt lỗi toàn cục và gửi về API; mở rộng: Sentry
- Lỗi người dùng báo → bug log → EAS Update hoặc build mới
- iOS (mở rộng): TestFlight hoặc development build

---

## Slide 15: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: đưa LHU Food lên server mẫu, build APK, đặt món qua mạng, gửi EAS Update
- **Không hướng dẫn**: hồ sơ cửa hàng (store-listing/)
- **Nhóm**: backend + CSDL trên server Khoa; APK chạy trên máy người ngoài nhóm; README triển khai; bản nháp báo cáo

---

## Slide 16: Tổng kết
**Nội dung chính**:
- Backend chạy như dịch vụ, chỉ dùng quyền EXECUTE
- Một mã nguồn, nhiều môi trường qua biến môi trường
- APK để kiểm thử, AAB để phát hành; OTA tiết kiệm lượt build
- Buổi sau: Demo Day
**Ghi chú giảng viên**:
- Nhắc hạn nộp đồ án, báo cáo cá nhân; yêu cầu nhóm tập demo trên đúng thiết bị.
