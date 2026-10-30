<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 02 - Routing, layout &amp; giao diện với Tailwind CSS (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Quản lý căn tin cần một khu quản trị có thanh menu bên trái, còn sinh viên cần trang thực đơn gọn trên điện thoại. Hai khu vực, hai bố cục, nhưng cùng một ứng dụng. Bắt đầu từ đâu: vẽ giao diện, hay phân tích xem có những trang nào và ai được vào?</em></p>
        <p><strong>Mục tiêu:</strong> Phân tích được chức năng thành sitemap và hệ thống route; xây dựng được route lồng nhau, route group, route động và layout dùng chung; dựng được giao diện responsive bằng Tailwind CSS và shadcn/ui.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Từ sơ đồ chức năng đến route:</strong> sitemap, bảng ánh xạ chức năng ↔ route ↔ vai trò.</li>
            <li><strong>Ý chính 2 - Routing của App Router:</strong> route lồng nhau, route group, route động, <code>loading</code>, <code>error</code>, <code>not-found</code>.</li>
            <li><strong>Ý chính 3 - Layout dùng chung và cây component:</strong> layout quản trị, layout khách, metadata.</li>
            <li><strong>Ý chính 4 - Tailwind CSS và shadcn/ui:</strong> utility class, responsive, component có sẵn; từ Figma đến mã.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Khung route và layout của LHU Food Web (quản trị và khách) với dữ liệu giả; nhóm có sơ đồ chức năng web, sitemap và bảng ánh xạ route.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Từ sơ đồ chức năng đến route</h3>
            <p>Phân tích trước khi code (CLO1): mỗi chức năng trong sơ đồ chức năng thành một hoặc vài trang; mỗi trang có đường dẫn, vai trò được vào, và dữ liệu lấy từ đâu.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 14px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Chức năng (SRS)</th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Route</th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Vai trò</th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">API</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Xem thực đơn (US-G01)</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>/menu</code></td><td style="border: 1px solid #ffd6ad; padding: 8px;">Mọi người</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>GET /products</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Chi tiết món (US-G03)</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>/product/[id]</code></td><td style="border: 1px solid #ffd6ad; padding: 8px;">Mọi người</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>GET /products/:id</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Quản lý món (US-A02)</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>/admin/products</code></td><td style="border: 1px solid #ffd6ad; padding: 8px;">admin</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>/admin/products</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Màn hình quầy (US-S02, S03)</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>/admin/orders</code></td><td style="border: 1px solid #ffd6ad; padding: 8px;">staff, admin</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>GET /orders/staff</code></td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;">Bảng này là minh chứng CLO1 trong báo cáo (bảng ánh xạ route – chức năng – vai trò – API) và là đầu vào để phân quyền ở bài 05.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Routing của App Router</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>app/
  layout.tsx                 layout gốc
  (shop)/                    route group: không xuất hiện trong URL
    layout.tsx               header cho khách
    menu/page.tsx            /menu
    product/[id]/page.tsx    /product/12   (route động)
  admin/
    layout.tsx               sidebar quản trị
    page.tsx                 /admin        (dashboard)
    products/page.tsx        /admin/products
    orders/page.tsx          /admin/orders
  not-found.tsx              trang 404</code></pre>
            <p>Route động đọc tham số qua <code>params</code>. Từ Next.js 15, <code>params</code> là Promise nên phải <code>await</code>:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(shop)/product/[id]/page.tsx
import { notFound } from 'next/navigation';
import { mockProducts } from '@/lib/mock';

export default async function ProductPage({ params }: { params: Promise&lt;{ id: string }&gt; }) {
  const { id } = await params;
  const product = mockProducts.find((p) =&gt; p.id === Number(id));
  if (!product) notFound();               // hiển thị not-found.tsx
  return &lt;h1 className="text-2xl font-bold"&gt;{product.name}&lt;/h1&gt;;
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li><code>loading.tsx</code>: giao diện chờ trong lúc trang đang tải dữ liệu (dùng ở bài 03).</li>
                <li><code>error.tsx</code>: giao diện khi trang lỗi; bắt buộc là Client Component.</li>
                <li>Điều hướng bằng <code>&lt;Link href="/menu"&gt;</code> (tải trước, không tải lại toàn trang); trong Client Component có thể dùng <code>useRouter()</code>.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Layout dùng chung và cây component</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/layout.tsx
import Link from 'next/link';

const MENU = [
  { href: '/admin', label: 'Tổng quan' },
  { href: '/admin/orders', label: 'Màn hình quầy' },
  { href: '/admin/products', label: 'Món ăn' },
];

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  return (
    &lt;div className="flex min-h-screen"&gt;
      &lt;aside className="hidden w-60 bg-blue-950 p-4 text-white md:block"&gt;
        &lt;p className="mb-6 font-bold"&gt;LHU Food · Quản trị&lt;/p&gt;
        &lt;nav className="space-y-1"&gt;
          {MENU.map((m) =&gt; (
            &lt;Link key={m.href} href={m.href} className="block rounded px-3 py-2 hover:bg-blue-800"&gt;{m.label}&lt;/Link&gt;
          ))}
        &lt;/nav&gt;
      &lt;/aside&gt;
      &lt;main className="flex-1 bg-slate-50 p-6"&gt;{children}&lt;/main&gt;
    &lt;/div&gt;
  );
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Layout giữ nguyên khi chuyển giữa các trang con (sidebar không vẽ lại); mỗi khu vực có layout riêng.</li>
                <li>Tiêu đề trang: <code>export const metadata = { title: 'Món ăn | LHU Food' }</code> trong <code>page.tsx</code> hoặc <code>layout.tsx</code>.</li>
                <li><strong>Cây component</strong> (layout → trang → thành phần như <code>ProductCard</code>, <code>OrderTable</code>) là một phần phân tích thành phần ở CLO1; vẽ lại cho các trang chính của nhóm.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Tailwind CSS và shadcn/ui</h3>
            <p><strong>Tailwind CSS</strong> viết giao diện bằng utility class ngay trong JSX: <code>p-4</code> (padding), <code>text-xl</code>, <code>bg-blue-950</code>, <code>grid grid-cols-1 md:grid-cols-3</code> (1 cột trên điện thoại, 3 cột từ màn hình vừa). Tiền tố <code>sm:</code>, <code>md:</code>, <code>lg:</code> áp dụng từ kích thước đó trở lên (mobile-first).</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>npx shadcn@latest init            # cấu hình shadcn/ui cho dự án
npx shadcn@latest add button card table dialog</code></pre>
            <p><strong>shadcn/ui</strong> chép mã nguồn component vào <code>components/ui/</code> của dự án (không phải thư viện cài sẵn), nên nhóm sửa được theo nhận diện LHU. Dùng <code>Card</code> cho thẻ món, <code>Table</code> cho danh sách quản trị, <code>Dialog</code> cho xác nhận.</p>
            <p style="margin-bottom: 0;"><strong>Từ Figma đến mã bằng vibe coding:</strong> đưa ảnh thiết kế, bảng route và <code>AGENTS.md</code> cho AI; yêu cầu dùng component shadcn/ui có sẵn và class Tailwind, không viết CSS riêng. Kiểm tra: màu, khoảng cách khớp thiết kế; responsive ở 3 kích thước; không có thư viện UI lạ.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 02: Routing, layout &amp; giao diện với Tailwind CSS</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đọc mục 5.1 (module), 5.14.2 (danh sách trang web), mục 8 (danh mục API) để lập bảng ánh xạ route.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/getting-started/layouts-and-pages" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Layouts and Pages</span><br>
                <span style="color: #6c757d; font-size: 13px;">Trang, layout lồng nhau, route động, liên kết giữa các trang.</span>
            </a>
            <a href="https://nextjs.org/docs/app/api-reference/file-conventions/route-groups" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Route Groups</span><br>
                <span style="color: #6c757d; font-size: 13px;">Gom route theo khu vực mà không đổi URL, mỗi nhóm có layout riêng.</span>
            </a>
            <a href="https://tailwindcss.com/docs/responsive-design" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Tailwind CSS - Responsive design</span><br>
                <span style="color: #6c757d; font-size: 13px;">Breakpoint sm, md, lg và cách thiết kế mobile-first.</span>
            </a>
            <a href="https://ui.shadcn.com/docs/installation/next" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 shadcn/ui - Next.js</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cài đặt và thêm component vào dự án Next.js.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Khung giao diện LHU Food Web</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Cài shadcn/ui và thêm <code>button</code>, <code>card</code>, <code>table</code>.</li>
                <li>Tạo cây thư mục như mục 2.2 với dữ liệu giả trong <code>lib/mock.ts</code>.</li>
                <li>Layout quản trị có sidebar (ẩn trên điện thoại, hiện từ <code>md</code>), layout khách có header.</li>
                <li>Trang <code>/menu</code> dạng lưới thẻ món bằng <code>Card</code>; trang <code>/product/[id]</code> với <code>notFound()</code> khi sai mã.</li>
                <li>Lập bảng ánh xạ route – chức năng – vai trò – API cho các trang vừa tạo.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Danh sách quầy</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Tạo <code>/counters</code> (danh sách quầy dạng thẻ) và <code>/counters/[id]</code> (chi tiết quầy) với dữ liệu giả, dùng layout khách; responsive 1 cột (điện thoại), 2 cột (máy tính bảng), 3 cột (máy tính).</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> route động hoạt động, mã quầy sai hiện trang 404; ảnh chụp ở 3 kích thước màn hình; prompt ghi trong <code>PROMPTS.md</code>.</p>
            <a href="{{LINK_NOP_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Sơ đồ chức năng web và sitemap của đề tài (draw.io, lưu file nguồn trong <code>docs/</code>).</li>
                <li>Bảng ánh xạ route – chức năng – vai trò – API cho toàn bộ phạm vi web.</li>
                <li>Khung route, layout quản trị và layout khách của web nhóm; cập nhật board Sprint 1.</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Nhóm bạn đặt màn hình quầy ở <code>/admin/orders</code> hay một route group riêng? Lựa chọn đó ảnh hưởng thế nào tới layout và phân quyền?</p>
            <a href="{{LINK_DIEN_DAN_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập routing, route group, route động, layout và Tailwind CSS.</p>
            <a href="{{LINK_QUIZ_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 02</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Lỗi kiểu dữ liệu <code>params</code>:</strong> từ Next.js 15, <code>params</code> và <code>searchParams</code> là Promise; khai báo <code>Promise&lt;{ id: string }&gt;</code> và <code>await</code>. Mã AI sinh theo phiên bản cũ thường thiếu bước này.</p>
        <p><strong>Class Tailwind không có tác dụng:</strong> kiểm tra file CSS toàn cục đã được import trong <code>app/layout.tsx</code>; tên class phải viết đầy đủ trong mã (không ghép chuỗi động như <code>`bg-${color}-500`</code>).</p>
        <p><strong>Hai trang cùng đường dẫn:</strong> route group không đổi URL, nên <code>(shop)/menu</code> và <code>(admin)/menu</code> xung đột. Đặt tên trang khác nhau.</p>
        <p><strong>Kiến thức mở rộng:</strong> Parallel Routes và Intercepting Routes (mở chi tiết món dạng modal mà vẫn có URL riêng).</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Mỗi route trong web của nhóm đã có trong bảng ánh xạ với đúng vai trò và API chưa?</p>
    </div>
</details>
