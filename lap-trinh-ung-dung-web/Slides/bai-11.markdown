# Bài 11: Triển khai lên Windows Server của Khoa & hoàn thiện báo cáo
Sprint 4 · Chất lượng & Phát hành

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Build production, chế độ standalone
- Chạy trên Windows Server: dịch vụ, proxy, cookie, CORS
- Viết báo cáo đồ án đúng quy định
- Tổng kết kế hoạch và tiến độ
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1, CLO3, CLO4. Liên hệ bộ phận hỗ trợ triển khai trước buổi.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- "Trên máy em chạy được mà thầy"
- Demo Day: chạy trên server Khoa, mở từ máy bất kỳ
- Báo cáo: từ thư mục ảnh thành 30–50 trang đúng quy định

---

## Slide 3: Kiến trúc triển khai
**Nội dung chính**:
```text
Máy trong phòng ─HTTPS─▶ Reverse proxy ─▶ Next.js ─▶ API nhóm ─▶ SQL Server
App di động ────────────────────────────────────────▶ API nhóm
Trình duyệt quầy ─Socket.IO────────────────────────▶ API nhóm
```

---

## Slide 4: Chế độ standalone
**Nội dung chính**:
- next.config: output: 'standalone'
- npm ci → npm run build
- Chép public và .next/static vào .next/standalone
- Chạy: node .next/standalone/server.js (PORT, HOSTNAME)

---

## Slide 5: Biến môi trường
**Nội dung chính**:
- NEXT_PUBLIC_SOCKET_URL: đọc lúc build → đổi phải build lại
- API_URL, SITE_URL, COOKIE_SECURE: đọc lúc chạy, chỉ server
- PORT do bộ phận hỗ trợ cấp; HOSTNAME 0.0.0.0
- Không commit giá trị bí mật

---

## Slide 6: Làm việc với bộ phận hỗ trợ
**Nội dung chính**:
- Dịch vụ nền: tự chạy lại khi server khởi động lại
- Reverse proxy, HTTPS, WebSocket qua proxy
- Mở cổng firewall: gửi yêu cầu kèm số cổng
- Nhóm tự cấu hình CORS của API

---

## Slide 7: Cookie Secure và Server Actions
**Nội dung chính**:
- Cookie Secure không lưu qua HTTP → bị đẩy về /login
- COOKIE_SECURE=false chỉ là cấu hình tạm, ghi trong báo cáo
- Sau proxy: serverActions.allowedOrigins
- /api/health: web ok, api ok

---

## Slide 8: Danh sách kiểm tra sau triển khai
**Nội dung chính**:
- /api/health từ máy khác
- Cookie HttpOnly, Secure
- App đặt món → quầy nhận realtime
- Ảnh món hiển thị; khởi động lại server vẫn chạy
- Playwright chạy với địa chỉ server

---

## Slide 9: README triển khai
**Nội dung chính**:
- Yêu cầu: phiên bản Node.js, cổng
- Biến môi trường (không ghi giá trị bí mật)
- Build, chạy dịch vụ, cập nhật phiên bản, kiểm tra
- Người khác đọc là làm lại được
**Hoạt động**: Đổi README cho nhóm bên cạnh thử đọc và góp ý

---

## Slide 10: Báo cáo đồ án: 7 chương
**Nội dung chính**:
- 1–2: Giới thiệu, phân tích yêu cầu (CLO1)
- 3–4: Phân tích thiết kế thành phần, hiện thực (CLO1)
- 5: Kiểm thử (CLO2); 6: Triển khai (CLO1)
- 7: Kế hoạch và tiến độ (CLO4); cả báo cáo: CLO3

---

## Slide 11: Báo cáo sprint là nguyên liệu
**Nội dung chính**:
- Không ghép nối bốn báo cáo sprint
- Biên tập thành tài liệu liền mạch
- Mỗi hình, bảng có đoạn giải thích "cho thấy gì, vì sao"
- Mã dài để phụ lục hoặc repo

---

## Slide 12: Lỗi trình bày hay gặp
**Nội dung chính**:
- Gõ tay số tiêu đề → Heading có đánh số, mục lục tự động
- Hình không số → Insert Caption, Cross-reference
- Ảnh mờ, cả màn hình → cắt đúng vùng
- Thiếu trích dẫn IEEE; thiếu mục "Sử dụng AI"

---

## Slide 13: Kế hoạch và tiến độ (CLO4)
**Nội dung chính**:
- Bảng 4 sprint: cam kết, hoàn thành, chuyển sprint, nguyên nhân
- Burndown bản phát hành: kế hoạch và thực tế
- Phân công khớp báo cáo vai trò cá nhân
- Ba bài học cụ thể, có số liệu

---

## Slide 14: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: triển khai web mẫu lên server mẫu, danh sách kiểm tra, README
- **Không hướng dẫn**: Chương 6 "Triển khai" đúng định dạng
- **Nhóm**: web + backend trên server Khoa, bản nháp báo cáo đủ 7 chương

---

## Slide 15: Tổng kết
**Nội dung chính**:
- Biến lúc build khác biến lúc chạy
- HTTPS, cookie Secure, CORS phải tính trước
- Báo cáo có cấu trúc, có minh chứng, đúng định dạng
- Buổi sau: Demo Day chung với học phần di động

---

## Slide 16: Tài liệu của buổi
**Đọc thêm**:
- Next.js: Deploying, output standalone, Self-Hosting
- Giáo trình di động: Chương 11 (triển khai backend lên server Khoa)
- Trang Đánh giá học phần: quy định định dạng, cấu trúc báo cáo
**Ghi chú giảng viên**:
- Hẹn lịch góp ý bản nháp báo cáo trước Demo Day; nhắc nhóm kiểm tra server ít nhất một ngày trước buổi 12.
