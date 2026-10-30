# Chương 11. Triển khai lên Windows Server của Khoa và hoàn thiện báo cáo

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Build ứng dụng Next.js cho môi trường production ở chế độ `standalone`.
- Phân biệt biến môi trường đọc lúc build và lúc chạy; cấu hình đúng cho server.
- Chạy web trên Windows Server của Khoa cùng backend nhóm; xử lý cookie `Secure`, CORS, reverse proxy.
- Kiểm tra sau triển khai theo danh sách và viết README triển khai.
- Hoàn thiện báo cáo đồ án đúng cấu trúc và quy định định dạng.
- Tổng kết kế hoạch và tiến độ bằng velocity và burndown.

## 11.1. Từ máy phát triển đến server

### 11.1.1. Kiến trúc khi triển khai

```text
Máy trong phòng ──HTTPS──▶ Reverse proxy (server Khoa) ──▶ Next.js :3001 ──▶ API nhóm :3000 ──▶ SQL Server
Điện thoại (app) ─────────────────────────────────────────────────────────────▶ API nhóm (REST + Socket.IO)
Trình duyệt quầy ──Socket.IO (wss)────────────────────────────────────────────▶ API nhóm
```

Backend và CSDL được triển khai theo Chương 11 giáo trình di động. Chương này trình bày phần web và những điểm web khác mobile: cookie, biến `NEXT_PUBLIC_`, reverse proxy và Server Actions.

### 11.1.2. Làm việc với bộ phận hỗ trợ

Giống học phần di động, mỗi nhóm được Khoa cấp quyền truy cập server và có **bộ phận hỗ trợ triển khai**. Các thao tác cần quyền quản trị (đăng ký dịch vụ nền, mở cổng firewall, cấu hình reverse proxy, chứng chỉ HTTPS) làm theo hướng dẫn hoặc với sự hỗ trợ của bộ phận này. Chương này mô tả **những gì cần đạt và cách kiểm tra**; công cụ cụ thể theo quy định của Khoa.

Thông tin cần xin trước khi triển khai: địa chỉ server và cách truy cập, cổng được cấp cho web và API, tên miền (nếu có), server có HTTPS hay chưa, công cụ chạy dịch vụ nền được dùng.

## 11.2. Build production

### 11.2.1. Chế độ standalone

`next build` tạo bản tối ưu cho production. Với tùy chọn `output: 'standalone'`, Next.js gom mã chạy và chỉ những gói thật sự cần vào thư mục `.next/standalone`, chạy bằng `node server.js` mà không cần cài lại toàn bộ `node_modules` trên server [1].

```ts
// next.config.ts (bổ sung)
const nextConfig = {
  output: 'standalone',
  experimental: {
    serverActions: {
      bodySizeLimit: '3mb',
      allowedOrigins: ['<ten-mien-web-nhom>'],   // khi chạy sau reverse proxy có tên miền khác Host
    },
  },
};
```

```powershell
# PowerShell trên server (hoặc máy build), trong thư mục dự án
npm ci
$env:NEXT_PUBLIC_SOCKET_URL = 'https://<dia-chi-api-nhom>'   # ghi cứng vào mã lúc build
npm run build
Copy-Item -Recurse public .next\standalone\public
Copy-Item -Recurse .next\static .next\standalone\.next\static

# Chạy thử
$env:PORT = '3001'; $env:HOSTNAME = '0.0.0.0'
$env:API_URL = 'http://localhost:3000'; $env:SITE_URL = 'https://<ten-mien-web-nhom>'
node .next\standalone\server.js
```

`npm ci` cài đúng phiên bản trong `package-lock.json`. Thư mục `standalone` không tự chép `public` và `.next/static`; thiếu bước chép thì trang hiện nhưng mất CSS và ảnh.

### 11.2.2. Biến môi trường lúc build và lúc chạy

| Biến | Đọc lúc | Lưu ý |
|---|---|---|
| `NEXT_PUBLIC_SOCKET_URL` | **Build** | Được chép thẳng vào JavaScript gửi xuống trình duyệt. Đổi giá trị phải build lại |
| `API_URL`, `SITE_URL`, `COOKIE_SECURE` | Chạy | Chỉ server đọc; đặt trong cấu hình dịch vụ hoặc file môi trường trên server, không commit |
| `PORT`, `HOSTNAME` | Chạy | Cổng do bộ phận hỗ trợ cấp; `0.0.0.0` để nhận kết nối từ máy khác |

Đây là lỗi triển khai hay gặp nhất với Next.js: build trên máy phát triển với `NEXT_PUBLIC_SOCKET_URL=http://localhost:3000` rồi chép lên server, màn hình quầy không kết nối được socket [2]. Nếu web và API cùng nằm trên một server, `API_URL` trỏ về `http://localhost:<cổng API>`: Next.js gọi API từ server, không qua mạng ngoài.

## 11.3. Chạy trên Windows Server

### 11.3.1. Những việc cần đạt

| Việc | Yêu cầu | Ai làm |
|---|---|---|
| Dịch vụ nền | Web tự chạy lại khi server khởi động lại hoặc tiến trình bị dừng | Nhóm, theo công cụ bộ phận hỗ trợ chỉ định |
| Reverse proxy, HTTPS | Tên miền trỏ tới cổng của web; bật hỗ trợ WebSocket nếu socket đi qua proxy | Bộ phận hỗ trợ |
| Firewall | Mở đúng cổng cần thiết (gửi yêu cầu kèm số cổng) | Bộ phận hỗ trợ |
| CORS của API | Cho phép địa chỉ web của nhóm kết nối Socket.IO | Nhóm (cấu hình backend) |

**Reverse proxy** là máy chủ đứng trước ứng dụng, nhận request từ người dùng (thường qua HTTPS, cổng 443) rồi chuyển tiếp tới cổng nội bộ của Next.js [3]. Nhờ đó nhiều nhóm dùng chung một server, mỗi nhóm một tên miền hoặc đường dẫn.

### 11.3.2. Cookie Secure

Chương 5 bật cờ `secure` khi `NODE_ENV=production`. Trình duyệt **không lưu** cookie `Secure` qua HTTP thường, nên nếu server chưa có HTTPS thì đăng nhập "thành công" nhưng người dùng bị đẩy về `/login` ngay. Tách thành biến riêng để kiểm soát:

```ts
// lib/session.ts và proxy.ts
secure: process.env.COOKIE_SECURE !== 'false',   // mặc định bật; chỉ tắt tạm khi server chưa có HTTPS
```

Tắt `COOKIE_SECURE` là cấu hình tạm cho môi trường học tập; ghi rõ trong báo cáo, giống cách giáo trình di động xử lý HTTP không mã hóa trên Android. Bản phát hành thật phải dùng HTTPS.

### 11.3.3. Server Actions sau reverse proxy

Next.js chống CSRF cho Server Actions bằng cách so sánh header `Origin` (tên miền người dùng thấy) với `Host` (tên miền server nhận). Sau reverse proxy, hai giá trị có thể khác nhau và mọi Server Action bị từ chối với lỗi "Invalid Server Actions request". Cách xử lý: khai báo tên miền trong `serverActions.allowedOrigins` (mục 11.2.1), hoặc nhờ bộ phận hỗ trợ cấu hình proxy chuyển tiếp đúng header `Host` [4].

### 11.3.4. Endpoint kiểm tra sức khỏe

```ts
// app/api/health/route.ts: kiểm tra nhanh sau triển khai
export async function GET() {
  const api = await fetch(`${process.env.API_URL}/health`, { cache: 'no-store' }).then((r) => r.ok).catch(() => false);
  return Response.json({ web: 'ok', api: api ? 'ok' : 'down', time: new Date().toISOString() },
                       { status: api ? 200 : 503 });
}
```

Một địa chỉ cho biết ngay web có chạy và có gọi được API không. Bộ phận hỗ trợ và nhóm dùng nó sau mỗi lần cập nhật hoặc khi có sự cố.

## 11.4. Kiểm tra sau triển khai

### 11.4.1. Danh sách kiểm tra

Ghi kết quả vào chương Triển khai của báo cáo, kèm ảnh có ngày giờ:

| # | Kiểm tra | Mong đợi |
|---|---|---|
| 1 | Mở `/api/health` từ một máy khác trong phòng | `{"web":"ok","api":"ok"}` |
| 2 | Đăng nhập staff, xem cookie trong DevTools | Có `HttpOnly`, có `Secure` khi dùng HTTPS |
| 3 | Đặt món từ app di động bản build | Màn hình quầy trên server hiện đơn realtime |
| 4 | Tải ảnh món mới, mở thực đơn | Ảnh hiển thị; `images.remotePatterns` đúng địa chỉ API thật |
| 5 | Nhờ bộ phận hỗ trợ khởi động lại server | Web và API tự chạy lại, kiểm tra 1–4 vẫn đạt |
| 6 | Chạy kịch bản Playwright với `baseURL` là địa chỉ server (CSDL thử) | Kịch bản đặt món đạt |

### 11.4.2. README triển khai

README triển khai trong repo phải đủ để một người ngoài nhóm làm lại được:

- Yêu cầu: phiên bản Node.js, cổng, phụ thuộc vào backend nào.
- Danh sách biến môi trường (tên, ý nghĩa, đọc lúc build hay lúc chạy), **không ghi giá trị bí mật**.
- Lệnh build và chạy; cách đăng ký dịch vụ nền theo hướng dẫn của Khoa.
- Cách cập nhật phiên bản: build lại, chép thư mục `standalone` mới, khởi động lại dịch vụ, chạy lại danh sách kiểm tra.
- Cách kiểm tra (`/api/health`) và người liên hệ.

## 11.5. Viết báo cáo đồ án (CLO3)

### 11.5.1. Từ báo cáo sprint đến báo cáo đồ án

Cấu trúc 7 chương và quy định định dạng ở trang **Đánh giá học phần** là chuẩn chấm. Các báo cáo sprint và báo cáo kiểm thử đã viết là nguyên liệu, không phải là báo cáo đồ án: không ghép nối bốn báo cáo sprint mà biên tập lại thành một tài liệu liền mạch, trình bày theo chủ đề.

| Chương | Lấy từ | CLO |
|---|---|---|
| 1. Giới thiệu · 2. Phân tích yêu cầu | SRS dùng chung, phạm vi web của nhóm (Chương 1) | CLO1 |
| 3. Phân tích và thiết kế thành phần | Sơ đồ chức năng, sitemap, bảng route (Chương 2), Server/Client (Chương 3–4), ma trận phân quyền (Chương 5), trạng thái đơn (Chương 6), module quản trị, ERD, danh mục thủ tục (Chương 7), sơ đồ tuần tự (Chương 9) | CLO1 |
| 4. Hiện thực | Cấu trúc dự án, quyết định kỹ thuật chính, ảnh giao diện; mã dài đưa vào phụ lục | CLO1 |
| 5. Kiểm thử | Báo cáo kiểm thử (Chương 10) | CLO2 |
| 6. Triển khai | Mục 11.2–11.4, danh sách kiểm tra có kết quả | CLO1 |
| 7. Kế hoạch và tiến độ | Báo cáo sprint 1–3, board, velocity, burndown (mục 11.6) | CLO4 |

### 11.5.2. Quy định định dạng

Báo cáo trình bày trên khổ A4; lề trái 3 cm, phải, trên, dưới 2 cm; Times New Roman cỡ 13; giãn dòng 1,3–1,5; tiêu đề chương, mục đánh số tự động; hình và bảng đánh số theo chương, có chú thích; có số trang; tài liệu tham khảo theo chuẩn IEEE; dài 30–50 trang không kể phụ lục. Chi tiết ở trang Đánh giá học phần.

### 11.5.3. Lỗi trình bày hay gặp và cách sửa trong Word

- **Tiêu đề gõ tay số và in đậm:** dùng kiểu Heading 1/2/3 có đánh số tự động, rồi chèn mục lục tự động (References → Table of Contents).
- **Hình không số, không chú thích:** dùng Insert Caption ("Hình 3.2. Ma trận phân quyền"), nhắc tới hình trong văn bản bằng Cross-reference trước khi hình xuất hiện; danh mục hình, danh mục bảng sinh tự động [5].
- **Ảnh chụp màn hình mờ, cả màn hình:** cắt đúng vùng cần nói, chữ trong ảnh đọc được khi in.
- **Dán cả trang mã:** chỉ trích đoạn ngắn minh họa quyết định, có chú thích; mã đầy đủ ở repo hoặc phụ lục.
- **Liệt kê mà không giải thích:** mỗi hình, bảng cần một đoạn trả lời "điều này cho thấy gì, vì sao chọn như vậy".
- **Trích dẫn thiếu:** tài liệu chính thức (Next.js, NestJS, OWASP…) trích theo IEEE, số thứ tự trong ngoặc vuông [1] tại chỗ dùng; danh mục tài liệu tham khảo xếp theo thứ tự trích dẫn.
- **Không khai báo dùng AI:** mục "Sử dụng AI" ghi công cụ, việc dùng AI làm, cách đã kiểm chứng.

### 11.5.4. Viết hợp lý và có minh chứng

Một chương tốt có cấu trúc mở – thân – kết: đoạn mở nói chương trình bày gì, phần thân đi từ phân tích tới quyết định, đoạn kết tóm tắt và nối sang chương sau. Mỗi khẳng định có minh chứng: "màn hình quầy cập nhật trong 2 giây" kèm kết quả TC-51; "phân quyền ba lớp" kèm ma trận và kết quả TC-21…TC-28. Văn phong khách quan, câu ngắn, thuật ngữ thống nhất trong toàn báo cáo.

## 11.6. Tổng kết kế hoạch và tiến độ (CLO4)

Chương 7 của báo cáo trả lời: nhóm đã lập kế hoạch thế nào, làm thực tế ra sao, chênh lệch vì sao, rút ra được gì. Số liệu lấy từ board, báo cáo sprint và lịch sử Pull Request, không viết theo trí nhớ.

| Sprint | Cam kết (SP) | Hoàn thành (SP) | Story chuyển sprint sau | Nguyên nhân chính |
|---|---|---|---|---|
| 1 | … | … | … | … |
| 2 | … | … | … | … |
| 3 | … | … | … | … |
| 4 | … | … | … | … |

- **Biểu đồ burndown của bản phát hành** (release burndown): trục ngang là sprint, trục dọc là story point còn lại của bản phát hành; vẽ đường kế hoạch và đường thực tế [6]. Chỗ hai đường tách xa là chỗ cần giải thích.
- **Phân công:** bảng thành viên – story phụ trách – số Pull Request – vai trò; khớp với báo cáo vai trò cá nhân của từng người.
- **Bài học quản lý công việc:** ít nhất ba điều cụ thể có số liệu, ví dụ "Sprint 2 cam kết 34 SP nhưng chỉ xong 21 SP vì chưa tính thời gian review; Sprint 3 thêm 20% thời gian review và đạt 26/28 SP".

## Tóm tắt chương

- `output: 'standalone'` cho bản chạy gọn bằng `node server.js`; nhớ chép `public` và `.next/static`.
- Biến `NEXT_PUBLIC_*` đọc lúc build, đổi phải build lại; biến server đọc lúc chạy, không commit.
- Thao tác quản trị server làm theo bộ phận hỗ trợ; nhóm lo CORS, cookie, cấu hình web.
- Cookie `Secure` cần HTTPS; Server Actions sau reverse proxy cần `allowedOrigins` hoặc header `Host` đúng.
- Danh sách kiểm tra sau triển khai và README triển khai là minh chứng của Chương 6 báo cáo.
- Báo cáo đồ án biên tập từ nguyên liệu các sprint, đúng định dạng, có minh chứng; Chương 7 dựa trên số liệu board.

## Câu hỏi ôn tập

1. Vì sao trang chạy bản standalone mất CSS? Cách sửa?
2. Biến nào đọc lúc build, biến nào đọc lúc chạy? Hậu quả khi nhầm?
3. Vì sao đăng nhập trên server HTTP bị đẩy về `/login` dù mật khẩu đúng?
4. Lỗi "Invalid Server Actions request" sau reverse proxy do đâu?
5. `/api/health` dùng để làm gì?
6. Báo cáo sprint và báo cáo đồ án khác nhau thế nào?
7. Biểu đồ burndown cho thấy điều gì về tiến độ của nhóm?

## Bài tập

1. **Chương Triển khai.** Viết Chương 6 của báo cáo nhóm: sơ đồ kiến trúc triển khai, bảng biến môi trường, các bước, bảng kết quả kiểm tra kèm ảnh, cấu hình tạm và lý do.
2. **README triển khai.** Viết README; nhờ một bạn nhóm khác đọc và thử làm theo, ghi lại chỗ họ bị vướng.
3. **Burndown.** Vẽ release burndown của nhóm từ số liệu board và viết đoạn giải thích.

## Tài liệu tham khảo

[1] Vercel, “output,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/config/next-config-js/output

[2] Vercel, “Environment Variables,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/guides/environment-variables

[3] Vercel, “How to self-host your Next.js application,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/guides/self-hosting

[4] Vercel, “serverActions,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions

[5] Microsoft, “Insert a caption,” *Microsoft Support*. Accessed: Oct. 30, 2026. [Online]. Available: https://support.microsoft.com/office/insert-a-caption-in-word-82fa82a4-f0f3-438f-a422-34bb5cef9c81

[6] K. Schwaber and J. Sutherland, “The Scrum Guide,” Nov. 2020. Accessed: Oct. 30, 2026. [Online]. Available: https://scrumguides.org/scrum-guide.html
