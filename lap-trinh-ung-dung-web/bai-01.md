<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 01 - Ứng dụng web hiện đại với Next.js &amp; khởi động dự án (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Bạn đã viết được ứng dụng React chạy trong trình duyệt. Nhưng trang thực đơn LHU Food cần hiện ngay khi mở, được Google tìm thấy, còn trang quản trị của căn tin lại cần tương tác nhiều và chỉ quản lý mới được vào. Một framework làm được cả hai việc đó như thế nào?</em></p>
        <p><strong>Mục tiêu:</strong> So sánh được các mô hình render web; giải thích được vai trò của Next.js App Router; phân tích được phạm vi web của LHU Food từ SRS; lập được kế hoạch Sprint 1 và phân vai cho nhóm.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Mô hình render web:</strong> CSR, SSR, SSG, ISR và React Server Components; khi nào cần một framework như Next.js.</li>
            <li><strong>Ý chính 2 - Next.js App Router:</strong> thư mục <code>app/</code>, <code>page.tsx</code>, <code>layout.tsx</code>, Server Component mặc định, <code>"use client"</code>.</li>
            <li><strong>Ý chính 3 - Phân tích phạm vi web của LHU Food:</strong> actor, user story web trong SRS, kiến trúc Next.js ↔ API ↔ SQL Server.</li>
            <li><strong>Ý chính 4 - Lập kế hoạch dự án và vibe coding:</strong> Product Backlog, kế hoạch sprint, board công việc; <code>AGENTS.md</code> cho dự án Next.js.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Dự án <code>lhu-food-web</code> chạy được, có repo và <code>AGENTS.md</code>; nhóm có danh sách story web, kế hoạch Sprint 1 trên board và bảng phân vai.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO4.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Các mô hình render web</h3>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 14px;">
                <thead>
                    <tr style="background-color: #ffe8d1;">
                        <th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Mô hình</th>
                        <th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">HTML được tạo ở đâu, khi nào</th>
                        <th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Phù hợp trong LHU Food</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;"><strong>CSR</strong> (React SPA đã học)</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Trình duyệt tải JavaScript rồi mới vẽ giao diện</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Phần tương tác nhiều: giỏ hàng, màn hình quầy</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;"><strong>SSR</strong></td><td style="border: 1px solid #ffd6ad; padding: 8px;">Server tạo HTML cho từng request</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Trang đơn của tôi, dữ liệu theo người dùng</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;"><strong>SSG / ISR</strong></td><td style="border: 1px solid #ffd6ad; padding: 8px;">Tạo sẵn HTML lúc build; ISR làm mới định kỳ</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Trang giới thiệu, thực đơn làm mới vài chục giây một lần</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;"><strong>React Server Components</strong></td><td style="border: 1px solid #ffd6ad; padding: 8px;">Component chạy trên server, chỉ gửi kết quả xuống trình duyệt, không gửi mã</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Mặc định cho mọi trang; chỉ phần cần tương tác mới chạy ở trình duyệt</td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;"><strong>Next.js</strong> là framework React cho phép kết hợp các mô hình trên trong cùng một ứng dụng: trang thực đơn render trên server (tải nhanh, tốt cho tìm kiếm), trang quản trị có các "đảo" tương tác chạy ở trình duyệt.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Next.js App Router</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>npx create-next-app@latest lhu-food-web --ts --tailwind --eslint --app --import-alias "@/*"
cd lhu-food-web
npm run dev          # mở http://localhost:3000</code></pre>
            <p>Mỗi thư mục trong <code>app/</code> là một đoạn đường dẫn; file <code>page.tsx</code> là trang, <code>layout.tsx</code> bọc các trang con:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>app/
  layout.tsx        bố cục gốc (thẻ &lt;html&gt;, &lt;body&gt;)
  page.tsx          /
  menu/
    page.tsx        /menu
  admin/
    page.tsx        /admin</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/page.tsx: Server Component (mặc định), chạy trên server
export default function HomePage() {
  return (
    &lt;main className="mx-auto max-w-4xl p-6"&gt;
      &lt;h1 className="text-3xl font-bold text-blue-900"&gt;LHU Food&lt;/h1&gt;
      &lt;p className="mt-2 text-slate-600"&gt;Đặt món căn tin, nhận món không cần xếp hàng.&lt;/p&gt;
    &lt;/main&gt;
  );
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Server Component (mặc định):</strong> chạy trên server, đọc dữ liệu được, không dùng <code>useState</code>, sự kiện <code>onClick</code>.</li>
                <li><strong>Client Component:</strong> file bắt đầu bằng <code>"use client"</code>, dùng được state và sự kiện; chỉ dùng cho phần cần tương tác.</li>
                <li>Next.js thay đổi nhanh giữa các phiên bản. Kiểm tra phiên bản bằng <code>npx next --version</code> và đọc tài liệu đúng phiên bản trên nextjs.org. Học phần dùng <strong>App Router</strong>; không trộn với Pages Router (thư mục <code>pages/</code>).</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Phân tích phạm vi web của LHU Food</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>Trình duyệt ──▶ Next.js (lhu-food-web) ──HTTP──▶ API (gateway) ──▶ SQL Server
                 Server/Client Components          chỉ gọi stored procedure
                 KHÔNG kết nối CSDL trực tiếp</code></pre>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 14px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Khu vực web</th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Actor</th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">User story (SRS)</th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Mức</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Trang quản trị</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Quản lý căn tin</td><td style="border: 1px solid #ffd6ad; padding: 8px;">US-A01…A07: danh mục, món, quầy, nhân viên, báo cáo, tình trạng hệ thống</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Bắt buộc</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Màn hình quầy</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Nhân viên</td><td style="border: 1px solid #ffd6ad; padding: 8px;">US-S02, S03, S05, S06, S07: đơn mới realtime, đổi trạng thái, tồn kho, lọc, hủy có lý do</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Bắt buộc</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Web đặt món</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Khách vãng lai, khách hàng</td><td style="border: 1px solid #ffd6ad; padding: 8px;">US-G01…G05, C01, C02, C04, C06, C07, C08, C13</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Cơ bản</td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;">Sprint 1–2 dùng <strong>API mẫu của giảng viên</strong> (địa chỉ thông báo trên Moodle, tài liệu tại <code>/docs</code>); Sprint 3–4 nhóm tự xây module quản trị trên backend của nhóm. Phân tích phạm vi là bước đầu của CLO1: mọi trang làm ra phải truy vết được tới một user story.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Lập kế hoạch dự án và vibe coding</h3>
            <p><strong>Sắp xếp công việc (CLO4):</strong> chọn story web từ Product Backlog dùng chung (kế hoạch Agile LHU Food), ước lượng story point, đặt <strong>Sprint Goal</strong>, đưa vào <strong>board</strong> (GitHub Projects hoặc Jira) với cột Cần làm, Đang làm, Chờ review, Xong. Mỗi thẻ có người phụ trách và liên kết tới Pull Request.</p>
            <p><strong>File quy ước cho AI</strong> (<code>AGENTS.md</code>, chép sang <code>.github/copilot-instructions.md</code>):</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># LHU Food Web - Quy ước dự án
## Công nghệ
- Next.js App Router (thư mục app/), TypeScript, Tailwind CSS + shadcn/ui.
- KHÔNG dùng Pages Router, KHÔNG kết nối SQL Server; dữ liệu lấy qua API (biến API_URL).
## Quy ước
- Server Component mặc định; chỉ thêm "use client" khi cần state hoặc sự kiện.
- Gọi API tập trung trong lib/api.ts; kiểu dữ liệu trong lib/types.ts.
- Chuỗi hiển thị tiếng Việt có dấu; không thêm thư viện khi nhóm chưa đồng ý.</code></pre>
            <p style="margin-bottom: 0;">Lỗi AI hay mắc với Next.js: trộn mã Pages Router (<code>getServerSideProps</code>), dùng hook trong Server Component, quên <code>"use client"</code> hoặc thêm tràn lan. Mỗi đoạn mã AI sinh phải được bạn hiểu và giải thích được; prompt chính ghi vào <code>PROMPTS.md</code>.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 01: Ứng dụng web hiện đại với Next.js &amp; khởi động dự án</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đọc mục 2.4 (phân vai mobile/web), mục 3 (actor), mục 4 (user story [W] và [M+W]), mục 5.14.2 (trang web).</span>
            </a>
            <a href="{{LINK_AGILE_SCRUM}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🗂 Kế hoạch Agile &amp; Product Backlog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Thang story point, MoSCoW, Definition of Ready/Done, backlog để chọn story web cho Sprint 1.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/getting-started/installation" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Installation</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tạo dự án bằng create-next-app, cấu trúc thư mục.</span>
            </a>
            <a href="https://nextjs.org/docs/app/getting-started/server-and-client-components" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Server and Client Components</span><br>
                <span style="color: #6c757d; font-size: 13px;">Khi nào dùng Server Component, khi nào dùng Client Component.</span>
            </a>
            <a href="https://docs.github.com/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 GitHub Projects</span><br>
                <span style="color: #6c757d; font-size: 13px;">Board quản lý công việc liên kết với issue và Pull Request.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Khởi tạo LHU Food Web</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Cài Node.js bản LTS; tạo dự án <code>lhu-food-web</code> bằng lệnh ở mục 2.2; chạy <code>npm run dev</code>.</li>
                <li>Sửa <code>app/page.tsx</code> thành trang chủ LHU Food; tạo thêm <code>app/menu/page.tsx</code> và <code>app/admin/page.tsx</code> (nội dung tạm).</li>
                <li>Tạo repo GitHub, viết <code>AGENTS.md</code> theo mẫu, commit đầu tiên.</li>
                <li>Mở tài liệu API mẫu tại <code>&lt;địa chỉ API&gt;/docs</code>, thử <code>GET /categories</code> và <code>GET /products</code>.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Hồ sơ cá nhân nhiều trang</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Tạo ứng dụng Next.js "Hồ sơ cá nhân" có trang chủ, <code>/gioi-thieu</code>, <code>/du-an</code>, <code>/lien-he</code>, dùng chung một layout có thanh điều hướng.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> 4 trang chạy được, điều hướng bằng <code>Link</code>, đẩy lên GitHub cá nhân, có ít nhất một prompt trong <code>PROMPTS.md</code>.</p>
            <a href="{{LINK_NOP_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà): Khởi động phần web của đồ án</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Dùng chung nhóm và đề tài với đồ án di động; tạo repo web của nhóm, mời giảng viên.</li>
                <li>Chọn các story web từ backlog, lập bảng phạm vi (khu vực, actor, story, mức bắt buộc/cơ bản).</li>
                <li><strong>Kế hoạch Sprint 1:</strong> Sprint Goal, story đã ước lượng, board công việc có người phụ trách từng thẻ.</li>
                <li>Bảng phân vai phần web (quản trị, màn hình quầy, web khách, kiểm thử, báo cáo).</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Trang nào của LHU Food nên render trên server, trang nào cần chạy phía trình duyệt? Giải thích bằng một ví dụ cụ thể.</p>
            <a href="{{LINK_DIEN_DAN_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập mô hình render, App Router, phạm vi web của LHU Food và lập kế hoạch sprint.</p>
            <a href="{{LINK_QUIZ_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 01</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Lỗi "You're importing a component that needs useState…":</strong> bạn dùng hook trong Server Component. Tách phần tương tác ra một file riêng có <code>"use client"</code> ở dòng đầu.</p>
        <p><strong>Cổng 3000 đã bị dùng:</strong> chạy <code>npm run dev -- -p 3001</code>; API mẫu chạy ở máy khác nên không xung đột.</p>
        <p><strong>AI sinh mã có <code>getServerSideProps</code> hoặc thư mục <code>pages/</code>:</strong> đó là Pages Router; nhắc AI đọc <code>AGENTS.md</code> và yêu cầu viết theo App Router.</p>
        <p><strong>Kiến thức mở rộng:</strong> Đọc mục "Rendering" trong tài liệu Next.js để so sánh cách Next.js quyết định render tĩnh hay động cho từng route khi build.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Bạn có chỉ ra được mỗi trang mình sắp làm ứng với user story nào trong SRS và ai trong nhóm phụ trách không?</p>
    </div>
</details>
