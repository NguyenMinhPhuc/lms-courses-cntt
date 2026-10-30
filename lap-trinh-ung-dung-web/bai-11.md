<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 11 - Triển khai lên Windows Server của Khoa &amp; hoàn thiện báo cáo (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>"Trên máy em chạy được mà thầy." Đến Demo Day, câu này không còn giá trị: web của nhóm phải chạy trên server của Khoa, mở được từ máy bất kỳ trong phòng, đăng nhập được, nhận đơn realtime từ điện thoại. Song song, báo cáo đồ án phải đi từ một thư mục ảnh chụp màn hình thành một tài liệu 30–50 trang đúng quy định.</em></p>
        <p><strong>Mục tiêu:</strong> Triển khai được ứng dụng Next.js cùng backend nhóm lên Windows Server; cấu hình đúng biến môi trường, cookie, CORS cho môi trường triển khai; viết được tài liệu triển khai; hoàn thiện được báo cáo đồ án đúng quy định định dạng; đối chiếu được kế hoạch với tiến độ thực tế.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Build production:</strong> <code>next build</code>, chế độ <code>standalone</code>, biến môi trường theo môi trường.</li>
            <li><strong>Ý chính 2 - Chạy trên Windows Server:</strong> dịch vụ nền, reverse proxy và HTTPS theo bộ phận hỗ trợ; cookie <code>Secure</code>, CORS, kiểm tra sau triển khai.</li>
            <li><strong>Ý chính 3 - Báo cáo kỹ thuật:</strong> cấu trúc báo cáo đồ án, quy định định dạng, hình/bảng, trích dẫn IEEE, minh chứng.</li>
            <li><strong>Ý chính 4 - Tổng kết kế hoạch:</strong> burndown, velocity, kế hoạch so với thực tế, bài học quản lý công việc.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Web và backend nhóm chạy trên server Khoa, qua được danh sách kiểm tra sau triển khai; có README triển khai; có bản nháp báo cáo đồ án đủ 7 chương.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO3, CLO4.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Build production và chế độ standalone</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>Máy trong phòng ──HTTPS──▶ Reverse proxy (server Khoa) ──▶ Next.js :3001 ──▶ API nhóm :3000 ──▶ SQL Server
Điện thoại (app) ─────────────────────────────────────────────────────────────▶ API nhóm (REST + Socket.IO)
Trình duyệt quầy ──Socket.IO (wss)────────────────────────────────────────────▶ API nhóm</code></pre>
            <p>Chế độ <code>standalone</code> gom mã chạy và các gói cần thiết vào <code>.next/standalone</code>, chạy bằng <code>node server.js</code> mà không cần cài lại <code>node_modules</code> đầy đủ trên server.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// next.config.ts (bổ sung)
const nextConfig = {
  output: 'standalone',
  experimental: {
    serverActions: {
      bodySizeLimit: '3mb',
      allowedOrigins: ['&lt;ten-mien-web-nhom&gt;'],   // khi chạy sau reverse proxy có tên miền khác Host
    },
  },
};</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># PowerShell trên server (hoặc máy build), trong thư mục dự án
npm ci
$env:NEXT_PUBLIC_SOCKET_URL = 'https://&lt;dia-chi-api-nhom&gt;'   # ghi cứng vào mã lúc build
npm run build
Copy-Item -Recurse public .next\standalone\public
Copy-Item -Recurse .next\static .next\standalone\.next\static

# Chạy thử
$env:PORT = '3001'; $env:HOSTNAME = '0.0.0.0'
$env:API_URL = 'http://localhost:3000'; $env:SITE_URL = 'https://&lt;ten-mien-web-nhom&gt;'
node .next\standalone\server.js</code></pre>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Biến</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Đọc lúc</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Lưu ý</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>NEXT_PUBLIC_SOCKET_URL</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><strong>Build</strong></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Được chép thẳng vào JavaScript gửi xuống trình duyệt. Đổi giá trị phải build lại.</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>API_URL</code>, <code>SITE_URL</code>, <code>COOKIE_SECURE</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chạy</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chỉ server đọc; đặt trong cấu hình dịch vụ hoặc file môi trường trên server, không commit.</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>PORT</code>, <code>HOSTNAME</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chạy</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Cổng do bộ phận hỗ trợ cấp; <code>0.0.0.0</code> để nhận kết nối từ máy khác.</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;">Nếu web và API cùng nằm trên một server, <code>API_URL</code> trỏ về <code>http://localhost:&lt;cổng API&gt;</code> (Next.js gọi API từ server, không qua mạng ngoài). Trình duyệt chỉ cần tới API cho kết nối Socket.IO.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Chạy trên Windows Server của Khoa</h3>
            <p>Giống Chương 11 giáo trình di động: mỗi nhóm được cấp quyền trên server và có <strong>bộ phận hỗ trợ triển khai</strong>. Các thao tác cần quyền quản trị (đăng ký dịch vụ nền, mở cổng firewall, cấu hình reverse proxy, chứng chỉ HTTPS) làm theo hướng dẫn hoặc với sự hỗ trợ của bộ phận này. Bài học mô tả <strong>những gì cần đạt và cách kiểm tra</strong>.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Việc</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Yêu cầu</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Ai làm</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Dịch vụ nền</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Web tự chạy lại khi server khởi động lại hoặc tiến trình bị dừng</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhóm, theo công cụ bộ phận hỗ trợ chỉ định</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Reverse proxy, HTTPS</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tên miền trỏ tới cổng của web; bật hỗ trợ WebSocket nếu socket đi qua proxy</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Bộ phận hỗ trợ</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Firewall</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mở đúng cổng cần thiết (gửi yêu cầu kèm số cổng)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Bộ phận hỗ trợ</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">CORS của API</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Cho phép địa chỉ web của nhóm kết nối Socket.IO</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhóm (cấu hình backend)</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Cookie <code>Secure</code>.</strong> Bài 05 bật <code>secure</code> khi <code>NODE_ENV=production</code>. Trình duyệt không lưu cookie <code>Secure</code> qua HTTP thường, nên nếu server chưa có HTTPS thì đăng nhập "thành công" nhưng bị đẩy về <code>/login</code> ngay. Tách thành biến riêng để kiểm soát:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/session.ts và proxy.ts
secure: process.env.COOKIE_SECURE !== 'false',   // mặc định bật; chỉ tắt tạm khi server chưa có HTTPS

// app/api/health/route.ts: kiểm tra nhanh sau triển khai
export async function GET() {
  const api = await fetch(`${process.env.API_URL}/health`, { cache: 'no-store' }).then((r) =&gt; r.ok).catch(() =&gt; false);
  return Response.json({ web: 'ok', api: api ? 'ok' : 'down', time: new Date().toISOString() },
                       { status: api ? 200 : 503 });
}</code></pre>
            <p>Tắt <code>COOKIE_SECURE</code> là cấu hình tạm cho môi trường học tập; ghi rõ trong báo cáo, giống cách giáo trình di động xử lý HTTP không mã hóa.</p>
            <p><strong>Danh sách kiểm tra sau triển khai</strong> (ghi kết quả vào chương Triển khai của báo cáo):</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">#</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kiểm tra</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Mong đợi</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">1</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mở <code>/api/health</code> từ một máy khác trong phòng</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>{"web":"ok","api":"ok"}</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">2</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đăng nhập staff, xem cookie trong DevTools</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Có <code>HttpOnly</code>, có <code>Secure</code> khi dùng HTTPS</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">3</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đặt món từ app di động bản build</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Màn hình quầy trên server hiện đơn realtime</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">4</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tải ảnh món mới, mở thực đơn</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Ảnh hiển thị; <code>images.remotePatterns</code> đúng địa chỉ API thật</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">5</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhờ bộ phận hỗ trợ khởi động lại server</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Web và API tự chạy lại, kiểm tra 1–4 vẫn đạt</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">6</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chạy kịch bản Playwright với <code>baseURL</code> là địa chỉ server (CSDL thử)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Kịch bản đặt món đạt</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;"><strong>README triển khai</strong> trong repo, đủ để một người khác làm lại: yêu cầu (phiên bản Node.js, cổng), danh sách biến môi trường (không ghi giá trị bí mật), lệnh build, cách chạy dịch vụ, cách cập nhật phiên bản mới, cách kiểm tra (<code>/api/health</code>), người liên hệ. Cập nhật phiên bản: build lại, chép thư mục <code>standalone</code> mới, khởi động lại dịch vụ, chạy lại danh sách kiểm tra.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Viết báo cáo đồ án (CLO3)</h3>
            <p>Cấu trúc 7 chương và quy định định dạng ở trang <strong>Đánh giá học phần</strong> (mục 2.3–2.4) là chuẩn chấm. Các báo cáo sprint và báo cáo kiểm thử đã viết là nguyên liệu, không phải là báo cáo đồ án: phải biên tập lại thành một tài liệu liền mạch.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Chương</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Lấy từ</th><th style="border: 1px solid #ffd6ad; padding: 6px;">CLO</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">1. Giới thiệu · 2. Phân tích yêu cầu</td><td style="border: 1px solid #ffd6ad; padding: 6px;">SRS dùng chung, phạm vi web của nhóm (bài 01)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">CLO1</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">3. Phân tích và thiết kế thành phần</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Sơ đồ chức năng, sitemap, bảng route (bài 02), Server/Client (bài 04), ma trận phân quyền (bài 05), trạng thái đơn (bài 06), module quản trị, ERD, danh mục thủ tục (bài 07), sơ đồ tuần tự (bài 09)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">CLO1</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">4. Hiện thực</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Cấu trúc dự án, các quyết định kỹ thuật chính, ảnh giao diện; mã dài đưa vào phụ lục</td><td style="border: 1px solid #ffd6ad; padding: 6px;">CLO1</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">5. Kiểm thử</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Báo cáo kiểm thử (bài 10)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">CLO2</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">6. Triển khai</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mục 2.1–2.2 bài này, danh sách kiểm tra có kết quả</td><td style="border: 1px solid #ffd6ad; padding: 6px;">CLO1</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">7. Kế hoạch và tiến độ</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Báo cáo sprint 1–3, board, velocity, burndown (mục 2.4)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">CLO4</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Lỗi trình bày hay gặp và cách sửa trong Word:</strong></p>
            <ul style="margin-bottom: 0;">
                <li><strong>Tiêu đề gõ tay số và in đậm:</strong> dùng Heading 1/2/3 có đánh số tự động, rồi chèn mục lục tự động (References → Table of Contents).</li>
                <li><strong>Hình không số, không chú thích:</strong> dùng Insert Caption ("Hình 3.2. Ma trận phân quyền"), nhắc tới hình trong văn bản bằng Cross-reference trước khi hình xuất hiện; danh mục hình sinh tự động.</li>
                <li><strong>Ảnh chụp màn hình mờ, cả màn hình:</strong> cắt đúng vùng cần nói, chữ trong ảnh đọc được khi in.</li>
                <li><strong>Dán cả trang mã:</strong> chỉ trích đoạn ngắn minh họa quyết định, có chú thích; mã đầy đủ để ở repo hoặc phụ lục.</li>
                <li><strong>Liệt kê mà không giải thích:</strong> mỗi hình, bảng cần một đoạn trả lời "điều này cho thấy gì, vì sao chọn như vậy".</li>
                <li><strong>Trích dẫn thiếu:</strong> tài liệu chính thức (Next.js, NestJS, OWASP…) trích theo IEEE, số thứ tự trong ngoặc vuông [1] tại chỗ dùng.</li>
                <li><strong>Không khai báo dùng AI:</strong> mục "Sử dụng AI" ghi công cụ, việc dùng AI làm, cách đã kiểm chứng (theo quy định trang Đánh giá).</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Tổng kết kế hoạch và tiến độ (CLO4)</h3>
            <p>Chương 7 trả lời: nhóm đã lập kế hoạch thế nào, làm thực tế ra sao, chênh lệch vì sao, rút ra được gì. Số liệu lấy từ board, không viết theo trí nhớ.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 700px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Sprint</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Cam kết (SP)</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Hoàn thành (SP)</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Story chuyển sprint sau</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Nguyên nhân chính</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">1–4</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                </tbody>
            </table>
            <ul style="margin-bottom: 0;">
                <li><strong>Biểu đồ burndown của bản phát hành:</strong> trục ngang là sprint, trục dọc là story point còn lại; vẽ đường kế hoạch và đường thực tế. Chỗ hai đường tách xa là chỗ cần giải thích.</li>
                <li><strong>Phân công:</strong> bảng thành viên – story phụ trách – số PR – vai trò; khớp với báo cáo vai trò cá nhân.</li>
                <li><strong>Bài học quản lý công việc:</strong> ít nhất ba điều cụ thể có bằng chứng (ví dụ "Sprint 2 cam kết 34 SP nhưng chỉ xong 21 SP vì chưa tính thời gian review; Sprint 3 thêm 20% thời gian review và đạt 26/28 SP").</li>
            </ul>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 11: Triển khai lên Windows Server của Khoa &amp; hoàn thiện báo cáo</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_AGILE_SCRUM}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🗂 Kế hoạch Agile &amp; Product Backlog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Release burndown, velocity, Definition of Done cho bản phát hành.</span>
            </a>
            <a href="{{LINK_RUBRIC}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📊 Rubric chấm điểm</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tiêu chí CLO3 (định dạng, cấu trúc, trích dẫn) và CLO4 (kế hoạch, tiến độ, vai trò cá nhân).</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/getting-started/deploying" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Deploying</span><br>
                <span style="color: #6c757d; font-size: 13px;">Chạy bằng Node.js server, các lựa chọn triển khai tự quản.</span>
            </a>
            <a href="https://nextjs.org/docs/app/api-reference/config/next-config-js/output" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - output: standalone</span><br>
                <span style="color: #6c757d; font-size: 13px;">Thư mục standalone, chép public và .next/static, biến PORT/HOSTNAME.</span>
            </a>
            <a href="https://nextjs.org/docs/app/guides/self-hosting" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Self-Hosting</span><br>
                <span style="color: #6c757d; font-size: 13px;">Reverse proxy, biến môi trường lúc build và lúc chạy.</span>
            </a>
            <a href="https://support.microsoft.com/office/insert-a-caption-in-word-82fa82a4-f0f3-438f-a422-34bb5cef9c81" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Microsoft Support - Chèn chú thích trong Word</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đánh số hình, bảng tự động; danh mục hình.</span>
            </a>
        </div>
    </div>
</details>

<details style="border: 1px solid #28a745; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #eafaf1; color: #28a745; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>💡 3. Hoạt động &amp; Thực hành trên lớp</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Triển khai web LHU Food mẫu</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Bật <code>output: 'standalone'</code>, thêm <code>COOKIE_SECURE</code> và <code>/api/health</code>; build và chạy thử bản standalone trên máy mình.</li>
                <li>Theo hướng dẫn của bộ phận hỗ trợ, chép bản build lên server mẫu, đặt biến môi trường, đăng ký dịch vụ nền.</li>
                <li>Chạy danh sách kiểm tra 1–6, ghi kết quả.</li>
                <li>Viết README triển khai theo mục 2.2.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Chương "Triển khai" của báo cáo</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Viết Chương 6 của báo cáo nhóm đúng quy định định dạng: sơ đồ kiến trúc triển khai (có số hình, chú thích), bảng biến môi trường (không ghi giá trị bí mật), các bước triển khai, bảng kết quả danh sách kiểm tra kèm ảnh minh chứng, các cấu hình tạm (nếu có) và lý do.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp file Word của chương, dùng Heading có đánh số tự động, chú thích hình/bảng bằng Insert Caption, có ít nhất một trích dẫn IEEE.</p>
            <a href="{{LINK_NOP_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <p style="margin: 0; color: #495057;">Web và backend nhóm chạy trên server Khoa, qua đủ danh sách kiểm tra; app di động bản build trỏ tới cùng backend. Nộp <strong>bản nháp báo cáo đồ án</strong> đủ 7 chương để giảng viên góp ý trước Demo Day. Board cập nhật đến hết Sprint 4.</p>
            <a href="{{LINK_NOP_BAN_NHAP_BAO_CAO}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; margin-top: 8px; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bản nháp báo cáo</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Lỗi khó nhất nhóm gặp khi đưa web lên server là gì? Nó có xảy ra trên máy phát triển không, và vì sao?</p>
            <a href="{{LINK_DIEN_DAN_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập build production, biến môi trường, cookie Secure, kiểm tra sau triển khai, quy định báo cáo và burndown.</p>
            <a href="{{LINK_QUIZ_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 11</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Trang hiện nhưng mất CSS, ảnh:</strong> chưa chép <code>public</code> và <code>.next/static</code> vào thư mục <code>standalone</code>.</p>
        <p><strong>Đăng nhập xong bị đẩy về /login:</strong> cookie <code>Secure</code> qua HTTP. Dùng HTTPS, hoặc tạm đặt <code>COOKIE_SECURE=false</code> và ghi chú trong báo cáo.</p>
        <p><strong>Server Action báo lỗi "Invalid Server Actions request" sau reverse proxy:</strong> header <code>Origin</code> khác <code>Host</code>. Thêm tên miền vào <code>serverActions.allowedOrigins</code>, hoặc nhờ bộ phận hỗ trợ chuyển tiếp đúng header Host.</p>
        <p><strong>Màn hình quầy không kết nối socket trên server:</strong> <code>NEXT_PUBLIC_SOCKET_URL</code> vẫn là địa chỉ máy phát triển (phải build lại); CORS của API chưa có địa chỉ web; proxy chưa bật WebSocket.</p>
        <p><strong>Kiến thức mở rộng:</strong> tự động build và triển khai bằng GitHub Actions khi merge vào nhánh chính; giám sát lỗi phía trình duyệt bằng công cụ thu thập lỗi.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Một bạn ngoài nhóm chỉ có README triển khai của nhóm bạn. Họ có triển khai lại được web trong 30 phút không?</p>
    </div>
</details>
