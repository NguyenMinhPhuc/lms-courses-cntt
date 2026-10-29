# Bài 01: Tổng quan phát triển ứng dụng di động & khởi động dự án
Từ React web đến ứng dụng Android, cùng quy trình vibe coding có kiểm soát

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- So sánh 3 hướng phát triển ứng dụng di động
- Giải thích kiến trúc React Native và vai trò của Expo
- Chuyển cách viết React web sang React Native
- Thiết lập môi trường, quy trình vibe coding và phân vai nhóm
**Ghi chú giảng viên**:
- Thời lượng: 2 tiết lý thuyết, 3 tiết thực hành.
- CLO liên quan: CLO1, CLO4.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Bạn đã viết web app bằng React
- Cần học thêm gì để chạy trên điện thoại Android?
- AI giúp bạn nhanh hơn, nhưng ai chịu trách nhiệm về mã?
**Hoạt động**: Hỏi nhanh 3 sinh viên: ứng dụng di động nào bạn dùng nhiều nhất mỗi ngày?
**Ghi chú giảng viên**:
- Ghi lại các ứng dụng sinh viên kể, dùng làm ví dụ cho slide 3.

---

## Slide 3: Ba hướng phát triển ứng dụng di động
**Nội dung chính**:
- **Native**: Kotlin (Android), Swift (iOS); hiệu năng tốt nhất, nhưng 2 mã nguồn
- **Cross-platform**: React Native, Flutter; 1 mã nguồn, giao diện native
- **PWA**: web app cài lên màn hình chính; truy cập thiết bị hạn chế
**Ví dụ**:
- Ứng dụng đặt món cần camera, vị trí, thông báo: cross-platform đáp ứng đủ
**Ghi chú giảng viên**:
- Nhấn mạnh: không có lựa chọn tốt nhất cho mọi trường hợp; học phần chọn React Native vì sinh viên đã biết React.

---

## Slide 4: React Native hoạt động thế nào?
**Nội dung chính**:
- Mã JavaScript/TypeScript mô tả giao diện bằng component
- React Native chuyển component thành **view native** của Android/iOS
- `<Text>` trên Android là một TextView thật, không phải trang web
- New Architecture (JSI, Fabric, TurboModules): gọi mã native trực tiếp, nhanh hơn
**Ghi chú giảng viên**:
- Không đi sâu vào New Architecture; chỉ cần sinh viên hiểu "không phải web nhúng".

---

## Slide 5: Expo giúp gì?
**Nội dung chính**:
- **Expo Go**: chạy thử dự án ngay trên điện thoại, không cần build
- **Development build**: bản app riêng khi cần thư viện native mà Expo Go không có
- **EAS Build / Update**: build APK, AAB và cập nhật ứng dụng qua mạng
**Hoạt động**: Mỗi sinh viên đăng ký tài khoản Expo miễn phí ngay trên lớp
**Ghi chú giảng viên**:
- Gói miễn phí giới hạn lượt build: khi phát triển dùng Expo Go, chỉ build APK khi cần nộp.
- Android bắt buộc, iOS là phần mở rộng.

---

## Slide 6: Từ React web sang React Native
**Nội dung chính**:
- `<div>` → `<View>` (mặc định xếp theo cột)
- `<p>`, `<span>` → `<Text>` (mọi chữ **bắt buộc** nằm trong Text)
- `<img>` → `<Image>` (ảnh từ URL cần width, height)
- `onClick` → `onPress` trên `<Pressable>`
- File CSS → `StyleSheet.create`, thuộc tính camelCase, không kế thừa
**Ghi chú giảng viên**:
- Hỏi: điều gì xảy ra nếu đặt chữ trực tiếp trong View? (báo lỗi)

---

## Slide 7: Ví dụ thẻ món ăn LHU Food
**Nội dung chính**:
- Component, props, hàm xử lý giữ nguyên như React web
```tsx
<View style={styles.card}>
  <Text style={styles.name}>{name}</Text>
  <Text>{price.toLocaleString('vi-VN')} đ</Text>
  <Pressable style={styles.button} onPress={onAdd}>
    <Text style={styles.buttonText}>Thêm vào giỏ</Text>
  </Pressable>
</View>
```
**Ghi chú giảng viên**:
- Mở code đầy đủ trong bài học (mục 2.3), chạy trực tiếp trên Expo Go cho lớp xem.

---

## Slide 8: Vibe coding là gì?
**Nội dung chính**:
- Mô tả điều mình muốn bằng ngôn ngữ tự nhiên, AI sinh mã
- Công cụ của học phần: **Google Antigravity**, **GitHub Copilot Chat**
- AI viết nhanh, nhưng **người chịu trách nhiệm về mã vẫn là bạn**
**Ghi chú giảng viên**:
- Demo nhanh: nhờ Copilot sinh một component đơn giản, chỉ ra một chỗ AI làm chưa đúng.

---

## Slide 9: Quy trình vibe coding có kiểm soát
**Nội dung chính**:
- 1. Cho AI ngữ cảnh: `AGENTS.md`, `.github/copilot-instructions.md`
- 2. Prompt cụ thể: màn hình nào, dữ liệu gì, tiêu chí hoàn thành
- 3. Đọc và chạy thử, sửa chỗ sai
- 4. Ghi prompt và nhận xét vào `PROMPTS.md`
- 5. **Không hiểu thì không merge**
**Ghi chú giảng viên**:
- Quy tắc 5 là căn cứ cho phần bảo vệ kỹ thuật ở Demo Day.

---

## Slide 10: Ví dụ AGENTS.md
**Nội dung chính**:
```markdown
# LHU Food - Quy ước dự án
- React Native + Expo, TypeScript, Expo Router (app/).
- Component dùng chung trong components/, tên PascalCase.
- Style dùng StyleSheet; màu lấy từ constants/theme.ts.
- Không thêm thư viện mới khi chưa hỏi nhóm.
```
**Ghi chú giảng viên**:
- Sinh viên sẽ tự viết AGENTS.md cho LHU Food trong phần thực hành.

---

## Slide 11: Dự án PBL của học phần
**Nội dung chính**:
- Nhóm 4–5 sinh viên, 1 đề tài, 4 sprint × 3 buổi
- Khuyến khích dùng chung đề tài và backend với môn Lập trình ứng dụng Web
- Backend NestJS + SQL Server do nhóm tự xây, truy cập CSDL qua stored procedure
- Cuối kỳ: APK chạy trên Android, kết nối server Khoa cấp
**Ghi chú giảng viên**:
- Giới thiệu lộ trình 4 sprint và 3 checkpoint (buổi 03, 06, 09).

---

## Slide 12: Phân vai trong nhóm
**Nội dung chính**:
- Mobile UI · Mobile logic · Backend API · CSDL & stored procedure · Kiểm thử & phát hành
- Mỗi người ít nhất một vai chính
- Điểm CLO4 cuối kỳ chấm theo vai trò cá nhân: commit/PR và phần tự trình bày
**Hoạt động**: Nhóm thống nhất bảng phân vai trước khi rời lớp

---

## Slide 13: Thực hành có hướng dẫn: Khởi tạo LHU Food
**Nội dung chính**:
- `npx create-expo-app@latest lhu-food`
- `npx expo start`, quét QR bằng Expo Go (cùng mạng Wi-Fi)
- Đọc cấu trúc: `app/`, `components/`, `assets/`, `app.json`
- Viết `AGENTS.md` bằng AI, tạo repo GitHub, commit đầu tiên
**Ghi chú giảng viên**:
- Mạng phòng lab chặn kết nối: dùng `npx expo start --tunnel`.

---

## Slide 14: Thực hành không hướng dẫn & thử thách nhóm
**Nội dung chính**:
- **Cá nhân**: ứng dụng "Thẻ giới thiệu bản thân" chạy trên Android, có `PROMPTS.md`
- **Nhóm**: Project Brief 1 trang, bảng phân vai, repo nhóm có `AGENTS.md`
**Hoạt động**: Nộp link repo qua Moodle

---

## Slide 15: Tóm tắt
**Nội dung chính**:
- React Native: một mã nguồn, giao diện native, dùng lại kỹ năng React
- Expo: Expo Go để chạy thử, EAS để build
- Chữ phải nằm trong Text; onPress thay onClick; StyleSheet thay CSS
- Vibe coding: AI sinh mã, bạn hiểu và chịu trách nhiệm
**Hoạt động**: Làm quiz Bài 01 (10 câu) ở cuối trang bài học
