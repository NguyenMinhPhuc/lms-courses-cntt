<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 03 - Server Components &amp; lấy dữ liệu từ API (5 tiết: 1 LT / 4 TH) · Checkpoint Sprint 1</strong></p>
        <p><em>Trang thực đơn đang hiện 10 món giả. Hôm nay nó lấy món thật từ API của căn tin, ngay trên server, trước khi trình duyệt nhận HTML. Và trước khi demo, nhóm phải chứng minh trang đó đúng yêu cầu bằng test case, không phải bằng câu "em chạy thử thấy được".</em></p>
        <p><strong>Mục tiêu:</strong> Phân biệt được Server Component và Client Component; lấy được dữ liệu từ API mẫu với cache phù hợp; xử lý được trạng thái tải và lỗi; viết và chạy được test case từ tiêu chí nghiệm thu; trình bày được kết quả Sprint 1 bằng báo cáo theo mẫu.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Server và Client Component:</strong> chạy ở đâu, gửi gì xuống trình duyệt, ranh giới <code>"use client"</code>.</li>
            <li><strong>Ý chính 2 - Lấy dữ liệu từ API:</strong> <code>fetch</code> trong Server Component, biến môi trường, kiểu TypeScript, cache và <code>revalidate</code>.</li>
            <li><strong>Ý chính 3 - Trạng thái tải và lỗi:</strong> <code>loading.tsx</code>, <code>Suspense</code>, <code>error.tsx</code>.</li>
            <li><strong>Ý chính 4 - Kiểm thử và báo cáo sprint:</strong> test case từ tiêu chí nghiệm thu, báo cáo sprint theo mẫu, Sprint Review và kế hoạch Sprint 2.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Trang thực đơn và chi tiết món lấy dữ liệu thật; nhóm hoàn thành Checkpoint Sprint 1 với test case có kết quả, báo cáo sprint 1 và kế hoạch Sprint 2.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2, CLO3, CLO4.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Server Component và Client Component</h3>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 14px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;"></th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Server Component (mặc định)</th><th style="border: 1px solid #ffd6ad; padding: 8px; text-align: left;">Client Component (<code>"use client"</code>)</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Chạy ở đâu</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Server (lúc build hoặc mỗi request)</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Server lần đầu (HTML) rồi trình duyệt</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Dùng được</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>async/await</code>, biến môi trường bí mật, gọi API trực tiếp</td><td style="border: 1px solid #ffd6ad; padding: 8px;"><code>useState</code>, <code>useEffect</code>, sự kiện, API trình duyệt</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Gửi xuống trình duyệt</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Chỉ kết quả, không gửi mã</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Mã JavaScript của component</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 8px;">Ví dụ LHU Food</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Trang thực đơn, chi tiết món</td><td style="border: 1px solid #ffd6ad; padding: 8px;">Nút "Thêm vào giỏ", bộ lọc có hiệu ứng</td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;">Quy tắc: trang để là Server Component, chỉ tách phần nhỏ cần tương tác thành Client Component. Ranh giới <code>"use client"</code> và lý do chọn là nội dung "thiết kế component" trong báo cáo (CLO1).</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Lấy dữ liệu từ API mẫu</h3>
            <p>Địa chỉ API đặt trong <code>.env.local</code> (không commit). Biến không có tiền tố <code>NEXT_PUBLIC_</code> chỉ đọc được ở server, trình duyệt không thấy:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># .env.local
API_URL=http://&lt;địa-chỉ-API-mẫu&gt;:3000</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/types.ts: theo định dạng trả về của API mẫu (xem /docs)
export type Category = { id: number; name: string; productCount: number };
export type Product = {
  id: number; categoryId: number; categoryName: string; name: string;
  description: string | null; price: number; imageUrl: string | null;
  isAvailable: boolean; stock: number;
};

// lib/api.ts: chỉ dùng ở server
import 'server-only';

export async function apiGet&lt;T&gt;(path: string, revalidate = 30): Promise&lt;T&gt; {
  const res = await fetch(`${process.env.API_URL}${path}`, { next: { revalidate } });
  if (!res.ok) throw new Error(`API ${path} trả về ${res.status}`);
  return res.json() as Promise&lt;T&gt;;
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(shop)/menu/page.tsx
import Link from 'next/link';
import { apiGet } from '@/lib/api';
import type { Category, Product } from '@/lib/types';

type Props = { searchParams: Promise&lt;{ category?: string; q?: string }&gt; };

export default async function MenuPage({ searchParams }: Props) {
  const { category, q } = await searchParams;
  const query = new URLSearchParams({ pageSize: '50' });
  if (category) query.set('categoryId', category);
  if (q) query.set('keyword', q);

  const [categories, products] = await Promise.all([
    apiGet&lt;Category[]&gt;('/categories', 300),          // danh mục ít đổi: 5 phút
    apiGet&lt;Product[]&gt;(`/products?${query}`, 30),     // tồn kho đổi thường xuyên: 30 giây
  ]);

  return (
    &lt;main className="mx-auto max-w-5xl p-6"&gt;
      &lt;form action="/menu" className="mb-4"&gt;
        &lt;input name="q" defaultValue={q} placeholder="Tìm món…" className="w-full rounded border px-3 py-2" /&gt;
      &lt;/form&gt;
      &lt;nav className="mb-4 flex gap-2 overflow-x-auto"&gt;
        {categories.map((c) =&gt; (
          &lt;Link key={c.id} href={`/menu?category=${c.id}`} className="rounded-full border px-3 py-1"&gt;{c.name}&lt;/Link&gt;
        ))}
      &lt;/nav&gt;
      {products.length === 0 ? (
        &lt;p className="text-slate-500"&gt;Không tìm thấy món phù hợp.&lt;/p&gt;
      ) : (
        &lt;ul className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3"&gt;
          {products.map((p) =&gt; (
            &lt;li key={p.id} className="rounded-xl border bg-white p-4"&gt;
              &lt;Link href={`/product/${p.id}`} className="font-bold"&gt;{p.name}&lt;/Link&gt;
              &lt;p&gt;{p.price.toLocaleString('vi-VN')} đ&lt;/p&gt;
            &lt;/li&gt;
          ))}
        &lt;/ul&gt;
      )}
    &lt;/main&gt;
  );
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Form tìm kiếm dùng phương thức GET bình thường nên không cần JavaScript phía client; kết quả nằm trong URL (<code>/menu?q=com</code>), chia sẻ được.</li>
                <li><strong>Cache:</strong> từ Next.js 15, <code>fetch</code> không tự cache; <code>{ next: { revalidate: 30 } }</code> cho phép dùng lại kết quả 30 giây rồi làm mới. Chọn thời gian theo mức thay đổi của dữ liệu.</li>
                <li><code>imageUrl</code> của API là đường dẫn tương đối (<code>/uploads/...</code>), có thể rỗng; ghép với <code>API_URL</code> và có ảnh thay thế khi không có ảnh.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Trạng thái tải và lỗi</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(shop)/menu/loading.tsx: hiện ngay trong lúc trang chờ API
export default function Loading() {
  return &lt;p className="p-6 text-slate-500"&gt;Đang tải thực đơn…&lt;/p&gt;;
}

// app/(shop)/menu/error.tsx: bắt buộc là Client Component
'use client';
export default function MenuError({ reset }: { error: Error; reset: () =&gt; void }) {
  return (
    &lt;div className="p-6"&gt;
      &lt;p&gt;Không tải được thực đơn. Vui lòng thử lại.&lt;/p&gt;
      &lt;button onClick={reset} className="mt-2 rounded bg-blue-900 px-4 py-2 text-white"&gt;Thử lại&lt;/button&gt;
    &lt;/div&gt;
  );
}</code></pre>
            <p style="margin-bottom: 0;"><code>loading.tsx</code> dùng cơ chế <strong>streaming</strong>: layout và khung trang hiện ngay, phần dữ liệu đến sau. Có thể bọc riêng từng khối chậm bằng <code>&lt;Suspense fallback={...}&gt;</code> để phần nhanh không phải chờ phần chậm. Không hiển thị thông báo kỹ thuật của lỗi cho người dùng.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Kiểm thử và báo cáo sprint</h3>
            <p><strong>Test case từ tiêu chí nghiệm thu (CLO2).</strong> Mỗi tiêu chí trong SRS (mục 4.7) thành ít nhất một test case có kết quả mong đợi đo được:</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mã</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Story</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Bước thực hiện</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả mong đợi</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-01</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-G01</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mở <code>/menu</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thấy danh mục và món đang bán, giá dạng "35.000 đ"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đạt</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-02</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-G01</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chọn danh mục "Đồ uống"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chỉ còn món thuộc "Đồ uống"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đạt</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-03</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-G02</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tìm "com ga"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Có "Cơm gà xối mỡ"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-G03</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mở <code>/product/999999</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Trang 404 thân thiện</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-05</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-G01</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đổi <code>API_URL</code> sai, mở <code>/menu</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thông báo lỗi và nút Thử lại, không lộ lỗi kỹ thuật</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Báo cáo sprint (CLO3), 1–2 trang, đúng định dạng ở trang Đánh giá học phần:</strong></p>
            <ol>
                <li>Sprint Goal và kết quả: đạt/chưa đạt, link demo.</li>
                <li>Story đã hoàn thành (bảng: mã story, người phụ trách, PR).</li>
                <li>Phân tích thành phần của sprint (sơ đồ, bảng ánh xạ route) – có số hình, chú thích.</li>
                <li>Kiểm thử: số test case, số đạt, lỗi tìm thấy và đã sửa.</li>
                <li>Kế hoạch so với thực tế (story point cam kết và hoàn thành), nguyên nhân chênh lệch.</li>
                <li>Kế hoạch sprint sau và bài học rút ra (Retrospective).</li>
            </ol>
            <p style="margin-bottom: 0;"><strong>Sprint Review và kế hoạch Sprint 2 (CLO4):</strong> demo cho giảng viên, nhận góp ý, cập nhật backlog; chọn story Sprint 2 theo năng lực thực tế của Sprint 1 (velocity).</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 03: Server Components &amp; lấy dữ liệu từ API</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Mục 4.7: tiêu chí nghiệm thu US-G01, G02, G03 để viết test case; mục 8: định dạng API.</span>
            </a>
            <a href="{{LINK_AGILE_SCRUM}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🗂 Kế hoạch Agile &amp; Product Backlog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Definition of Done, Sprint Review, release burndown: chuẩn bị Checkpoint Sprint 1.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/getting-started/fetching-data" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Fetching Data</span><br>
                <span style="color: #6c757d; font-size: 13px;">Lấy dữ liệu trong Server Component, streaming, Suspense.</span>
            </a>
            <a href="https://nextjs.org/docs/app/getting-started/error-handling" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Error Handling</span><br>
                <span style="color: #6c757d; font-size: 13px;">error.tsx, not-found, xử lý lỗi dự kiến và không dự kiến.</span>
            </a>
            <a href="https://nextjs.org/docs/app/guides/environment-variables" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Environment Variables</span><br>
                <span style="color: #6c757d; font-size: 13px;">Biến chỉ ở server và biến NEXT_PUBLIC_ gửi xuống trình duyệt.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Thực đơn với dữ liệu thật</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tạo <code>.env.local</code>, <code>lib/types.ts</code>, <code>lib/api.ts</code> (cài <code>npm install server-only</code>).</li>
                <li>Trang <code>/menu</code> lấy danh mục và món từ API mẫu, lọc theo danh mục, tìm kiếm qua <code>searchParams</code>.</li>
                <li>Trang <code>/product/[id]</code> gọi <code>GET /products/:id</code>, hiện "Hết món" khi <code>isAvailable</code> sai hoặc <code>stock</code> bằng 0.</li>
                <li>Thêm <code>loading.tsx</code>, <code>error.tsx</code>; thử tắt mạng hoặc đổi <code>API_URL</code> sai.</li>
                <li>Viết và chạy 5 test case theo bảng mẫu, ghi kết quả.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Quầy với dữ liệu thật</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Chuyển trang <code>/counters</code> (bài 02) sang lấy dữ liệu từ <code>GET /counters</code>, có trạng thái tải, lỗi, rỗng; chọn thời gian <code>revalidate</code> phù hợp và giải thích.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> trang chạy với API mẫu; nộp 5 test case (có trường hợp lỗi API) kèm kết quả chạy.</p>
            <a href="{{LINK_NOP_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🏁 Checkpoint Sprint 1 (1 tiết)</strong></p>
            <ul style="margin: 0 0 8px 0; color: #495057;">
                <li>Demo khung web của nhóm với dữ liệu thật từ API mẫu (trang khách và khung quản trị).</li>
                <li><strong>Phân tích (CLO1):</strong> sơ đồ chức năng web, sitemap, bảng ánh xạ route – chức năng – vai trò – API.</li>
                <li><strong>Kiểm thử (CLO2):</strong> test case cho các story của Sprint 1 kèm kết quả chạy.</li>
                <li><strong>Báo cáo sprint 1 (CLO3)</strong> theo cấu trúc mục 2.4 và quy định định dạng.</li>
                <li><strong>Kế hoạch Sprint 2 (CLO4):</strong> board cập nhật, story chọn theo velocity Sprint 1.</li>
            </ul>
            <a href="{{LINK_NOP_CHECKPOINT_1}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp Checkpoint 1</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Thực đơn của nhóm bạn cache bao lâu? Nếu căn tin vừa tắt một món hết hàng, khách thấy thay đổi sau bao lâu và điều đó có chấp nhận được không?</p>
            <a href="{{LINK_DIEN_DAN_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập Server/Client Component, lấy dữ liệu, cache, trạng thái tải/lỗi, test case và báo cáo sprint.</p>
            <a href="{{LINK_QUIZ_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 03</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong><code>process.env.API_URL</code> là undefined:</strong> biến đặt sai file (phải là <code>.env.local</code> ở gốc dự án) hoặc chưa khởi động lại <code>npm run dev</code> sau khi sửa.</p>
        <p><strong>Lỗi "server-only cannot be imported from a Client Component":</strong> bạn gọi <code>lib/api.ts</code> trong file có <code>"use client"</code>. Lấy dữ liệu ở Server Component cha rồi truyền xuống qua props.</p>
        <p><strong>Dữ liệu không cập nhật sau khi sửa trên API:</strong> đang dùng kết quả cache; chờ hết thời gian <code>revalidate</code> hoặc giảm thời gian khi phát triển.</p>
        <p><strong>Kiến thức mở rộng:</strong> <code>generateStaticParams</code> để tạo sẵn trang chi tiết món khi build; <code>generateMetadata</code> để đặt tiêu đề trang theo tên món.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Mỗi test case của nhóm có truy vết được tới một tiêu chí nghiệm thu trong SRS, và có kết quả chạy thật không?</p>
    </div>
</details>
