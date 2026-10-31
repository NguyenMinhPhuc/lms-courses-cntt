<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 08 - Trang quản trị: CRUD, tải ảnh, báo cáo &amp; biểu đồ (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Cuối tuần, quản lý căn tin muốn biết: tuần này bán được bao nhiêu, món nào bán chạy, bao nhiêu đơn bị hủy. Họ không mở SSMS, cũng không đọc JSON. Họ cần một trang quản trị: thêm món mới kèm ảnh trong một phút, nhìn biểu đồ là hiểu, bấm một nút là có file Excel gửi cho kế toán.</em></p>
        <p><strong>Mục tiêu:</strong> Xây dựng được trang quản trị CRUD theo một mẫu thống nhất; tải được ảnh lên API có kiểm tra định dạng và dung lượng; trình bày được số liệu báo cáo bằng biểu đồ và xuất được file CSV; kiểm thử được các ràng buộc nghiệp vụ quản trị.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Mẫu trang CRUD:</strong> danh sách, tạo, sửa, ngừng bán; một form dùng chung cho tạo và sửa; hộp thoại xác nhận.</li>
            <li><strong>Ý chính 2 - Tải ảnh món:</strong> <code>FormData</code> qua Server Action tới API, xem trước, giới hạn định dạng và dung lượng.</li>
            <li><strong>Ý chính 3 - Báo cáo và biểu đồ:</strong> doanh thu, món bán chạy, tỉ lệ trạng thái bằng Recharts; chọn khoảng ngày; xuất CSV.</li>
            <li><strong>Ý chính 4 - Tài khoản nhân viên và test case quản trị:</strong> tạo, khóa, mở khóa (US-A04); kiểm thử các ràng buộc.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Trang quản lý món (US-A02) có ảnh, trang báo cáo (US-A05, A06) có biểu đồ và nút xuất CSV, trang tài khoản nhân viên (US-A04), chạy trên backend nhóm; bộ test case quản trị kèm kết quả.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Mẫu trang CRUD</h3>
            <p>Mọi trang quản trị (món, danh mục, quầy, tài khoản) dùng cùng một cấu trúc. Người dùng học một lần là dùng được mọi trang, nhóm viết một lần là nhân bản được:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>app/admin/products/
  page.tsx             danh sách (Server Component, bảng bài 06)
  new/page.tsx         tạo mới  → &lt;ProductForm /&gt;
  [id]/edit/page.tsx   sửa      → &lt;ProductForm product={product} /&gt;
  product-form.tsx     form dùng chung (Client Component)
  actions.ts           saveProduct, uploadProductImage, toggleAvailability</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/products/actions.ts
'use server';
import { redirect } from 'next/navigation';
import { revalidatePath } from 'next/cache';
import { productSchema } from '@/lib/schemas';
import { requireRole } from '@/lib/dal';
import { apiAuth, ApiError } from '@/lib/api';

export type FormState = { ok: boolean; message?: string; fieldErrors?: Record&lt;string, string[]&gt; };

// id có giá trị: sửa; không có: tạo mới. Gắn id bằng saveProduct.bind(null, product?.id)
export async function saveProduct(id: number | undefined, _prev: FormState, formData: FormData): Promise&lt;FormState&gt; {
  await requireRole('admin');
  const parsed = productSchema.safeParse(Object.fromEntries(formData));   // price, categoryId: z.coerce.number()
  if (!parsed.success) return { ok: false, fieldErrors: parsed.error.flatten().fieldErrors };
  try {
    await apiAuth(id ? `/admin/products/${id}` : '/admin/products', {
      method: id ? 'PUT' : 'POST', body: JSON.stringify(parsed.data),
    });
  } catch (e) {
    if (e instanceof ApiError &amp;&amp; e.status === 404) return { ok: false, message: 'Danh mục hoặc món không còn tồn tại' };
    return { ok: false, message: 'Chưa lưu được món, vui lòng thử lại' };
  }
  revalidatePath('/admin/products');
  revalidatePath('/menu');                           // thực đơn của khách cũng đổi
  redirect('/admin/products');
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Form dùng <code>useActionState(saveProduct.bind(null, product?.id), { ok: false })</code>; <code>defaultValue</code> lấy từ <code>product</code> khi sửa. Lỗi từng trường lấy từ <code>state.fieldErrors</code>.</li>
                <li><strong>Không có nút "Xóa món".</strong> Món đã có trong đơn chỉ được ngừng bán (BR-16), dùng nút bật/tắt của bài 06. Thao tác không hoàn tác được (xóa danh mục, khóa tài khoản) phải qua <code>AlertDialog</code> của shadcn/ui ghi rõ hậu quả.</li>
                <li>Sau khi lưu, thông báo ngắn (toast) "Đã lưu món Cơm gà xối mỡ" và quay về danh sách.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Tải ảnh món</h3>
            <p>Trình duyệt gửi file tới Server Action, Server Action kiểm tra rồi chuyển tiếp tới API kèm token. API (Multer, trường <code>file</code>) lưu ảnh và stored procedure cập nhật <code>ImageUrl</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/products/actions.ts (tiếp; thêm import { getAccessToken } from '@/lib/session')
const IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp'];
const MAX_BYTES = 2 * 1024 * 1024;

export async function uploadProductImage(productId: number, _prev: FormState, formData: FormData): Promise&lt;FormState&gt; {
  await requireRole('admin');
  const file = formData.get('file');
  if (!(file instanceof File) || file.size === 0) return { ok: false, message: 'Chọn một ảnh' };
  if (!IMAGE_TYPES.includes(file.type)) return { ok: false, message: 'Chỉ nhận ảnh JPG, PNG hoặc WEBP' };
  if (file.size &gt; MAX_BYTES) return { ok: false, message: 'Ảnh tối đa 2 MB' };

  const body = new FormData();
  body.append('file', file);
  const res = await fetch(`${process.env.API_URL}/admin/products/${productId}/image`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${await getAccessToken()}` },   // KHÔNG tự đặt Content-Type
    body,
  });
  if (!res.ok) return { ok: false, message: res.status === 413 ? 'Ảnh vượt quá dung lượng cho phép' : 'Tải ảnh thất bại' };
  revalidatePath('/admin/products');
  return { ok: true, message: 'Đã cập nhật ảnh' };
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// next.config.ts
const nextConfig = {
  experimental: { serverActions: { bodySizeLimit: '3mb' } },     // mặc định 1 MB
  images: { remotePatterns: [new URL(`${process.env.API_URL}/uploads/**`)] },  // cho phép next/image
};
export default nextConfig;</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Không tự đặt <code>Content-Type</code></strong> khi gửi <code>FormData</code>: <code>fetch</code> tự sinh <code>multipart/form-data; boundary=…</code>. Vì vậy upload không dùng <code>apiAuth</code> (hàm đó luôn đặt JSON), giống lưu ý ở Chương 8 giáo trình di động.</li>
                <li><strong>Xem trước</strong> ở client: <code>&lt;input type="file" accept="image/jpeg,image/png,image/webp"&gt;</code>, khi chọn file thì <code>URL.createObjectURL(file)</code> rồi hiện bằng <code>&lt;img&gt;</code>; gọi <code>URL.revokeObjectURL</code> khi đổi file.</li>
                <li>Kiểm tra định dạng ở ba nơi: thuộc tính <code>accept</code> (tiện cho người dùng), Server Action (chặn sớm), API (chặn thật). Không tin phần mở rộng tên file.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Báo cáo và biểu đồ</h3>
            <p>Trang <code>/admin/reports?from=2026-10-01&amp;to=2026-10-31</code>: Server Component đọc khoảng ngày từ URL, gọi ba API báo cáo cùng lúc, truyền dữ liệu cho biểu đồ (Client Component). Recharts vẽ bằng JavaScript nên bắt buộc chạy ở client.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/reports/page.tsx
export default async function ReportsPage({ searchParams }: { searchParams: Promise&lt;{ from?: string; to?: string }&gt; }) {
  await requireRole('admin');
  const { from = firstDayOfMonth(), to = today() } = await searchParams;
  if (from &gt; to) return &lt;p role="alert"&gt;Ngày bắt đầu phải trước hoặc bằng ngày kết thúc.&lt;/p&gt;;
  const q = `from=${from}&amp;to=${to}`;
  const [revenue, top, status] = await Promise.all([
    apiAuth&lt;{ day: string; orderCount: number; revenue: number }[]&gt;(`/reports/revenue?${q}`),
    apiAuth&lt;{ id: number; name: string; quantity: number; revenue: number }[]&gt;(`/reports/top-products?${q}&amp;top=5`),
    apiAuth&lt;{ status: string; orderCount: number; percentage: number }[]&gt;(`/reports/order-status?${q}`),
  ]);
  return &lt;ReportView revenue={revenue} top={top} status={status} from={from} to={to} /&gt;;
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/reports/revenue-chart.tsx   (npm install recharts)
'use client';
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const vnd = (n: number) =&gt; `${n.toLocaleString('vi-VN')} đ`;

export function RevenueChart({ data }: { data: { day: string; revenue: number }[] }) {
  return (
    &lt;figure&gt;
      &lt;figcaption className="font-bold"&gt;Doanh thu theo ngày (không tính đơn đã hủy)&lt;/figcaption&gt;
      &lt;ResponsiveContainer width="100%" height={280}&gt;
        &lt;BarChart data={data}&gt;
          &lt;CartesianGrid vertical={false} strokeDasharray="3 3" /&gt;
          &lt;XAxis dataKey="day" tickFormatter={(d: string) =&gt; d.slice(8, 10) + '/' + d.slice(5, 7)} /&gt;
          &lt;YAxis tickFormatter={(n: number) =&gt; `${n / 1000}k`} /&gt;
          &lt;Tooltip formatter={(n: number) =&gt; vnd(n)} labelFormatter={(d: string) =&gt; `Ngày ${d}`} /&gt;
          &lt;Bar dataKey="revenue" name="Doanh thu" fill="#1e3a8a" radius={[4, 4, 0, 0]} /&gt;
        &lt;/BarChart&gt;
      &lt;/ResponsiveContainer&gt;
    &lt;/figure&gt;
  );
}</code></pre>
            <ul>
                <li><strong>Chọn biểu đồ theo câu hỏi:</strong> doanh thu theo thời gian dùng cột hoặc đường; món bán chạy dùng cột ngang, sắp xếp giảm dần; tỉ lệ trạng thái (US-A06) dùng cột chồng 100% hoặc bảng có phần trăm. Biểu đồ tròn chỉ hợp khi có ít nhóm.</li>
                <li>Một màu cho một chuỗi số liệu; không dùng màu để phân biệt các ngày. Luôn có tiêu đề, đơn vị và bảng số liệu bên dưới cho người không xem được biểu đồ.</li>
                <li>Số liệu phải <strong>khớp với truy vấn trực tiếp trên CSDL</strong> (tiêu chí US-A05). Đây là một test case bắt buộc.</li>
            </ul>
            <p><strong>Xuất CSV cho Excel</strong> bằng Route Handler, vì cần trả về file chứ không phải trang:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/reports/export/route.ts   → &lt;a href={`/admin/reports/export?from=${from}&amp;to=${to}`}&gt;
export async function GET(req: Request) {
  await requireRole('admin');
  const { searchParams } = new URL(req.url);
  const q = `from=${searchParams.get('from')}&amp;to=${searchParams.get('to')}`;
  const rows = await apiAuth&lt;{ day: string; orderCount: number; revenue: number }[]&gt;(`/reports/revenue?${q}`);
  const csv = ['Ngày,Số đơn,Doanh thu', ...rows.map((r) =&gt; `${r.day},${r.orderCount},${r.revenue}`)].join('\r\n');
  return new Response('﻿' + csv, {                     // BOM: Excel đọc đúng tiếng Việt
    headers: {
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': `attachment; filename="doanh-thu-${searchParams.get('from')}.csv"`,
    },
  });
}</code></pre>
            <p style="margin-bottom: 0;">Thư mục <code>/admin</code> đã được <code>proxy.ts</code> bảo vệ, nhưng Route Handler vẫn gọi <code>requireRole</code> (nguyên tắc ba lớp của bài 05). Nếu nội dung có dấu phẩy (tên món), bọc giá trị trong dấu nháy kép.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Tài khoản nhân viên và test case quản trị</h3>
            <p>Trang <code>/admin/users</code> (US-A04): danh sách lọc theo vai trò, tạo tài khoản staff, khóa và mở khóa. Mật khẩu ban đầu do quản lý đặt, được băm bằng bcrypt ở backend; web không bao giờ hiển thị lại mật khẩu.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mã</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Story</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Bước thực hiện</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả mong đợi</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-41</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A01</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Xóa danh mục còn món</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Danh mục còn món, không xóa được"; danh mục vẫn còn</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-42</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A02</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tạo món giá 0 đ / giá âm</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Báo lỗi dưới ô Giá, không gọi API</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-43</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A02</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tải file PDF đổi tên thành <code>.jpg</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Bị từ chối, ảnh cũ giữ nguyên</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-44</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A02</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tải ảnh 2,5 MB</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Ảnh tối đa 2 MB"</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-45</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A05</td><td style="border: 1px solid #ffd6ad; padding: 6px;">So doanh thu một ngày trên web với <code>SELECT SUM</code> trực tiếp trên CSDL (bỏ đơn <code>cancelled</code>)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Hai số bằng nhau</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-46</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A05</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Chọn ngày bắt đầu sau ngày kết thúc</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thông báo lỗi, không gọi API</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-47</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Khóa nhân viên đang đăng nhập, chờ access token hết hạn</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Làm mới token bị từ chối, nhân viên về trang đăng nhập và không đăng nhập lại được</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-48</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Quản lý tự khóa tài khoản của mình</td><td style="border: 1px solid #ffd6ad; padding: 6px;">"Không thể tự khóa tài khoản của mình" (400)</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-49</td><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A05</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Mở file CSV vừa xuất bằng Excel</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tiêu đề cột tiếng Việt hiển thị đúng dấu, số liệu khớp trang</td></tr>
                </tbody>
            </table>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 08: Trang quản trị: CRUD, tải ảnh, báo cáo &amp; biểu đồ</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tiêu chí US-A01, A02, A04, A05, A06; quy tắc BR-16 (ngừng bán thay vì xóa); mục 8: /admin, /reports.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - serverActions (bodySizeLimit)</span><br>
                <span style="color: #6c757d; font-size: 13px;">Giới hạn kích thước dữ liệu gửi tới Server Action.</span>
            </a>
            <a href="https://nextjs.org/docs/app/getting-started/route-handlers" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Route Handlers</span><br>
                <span style="color: #6c757d; font-size: 13px;">Trả về file, header Content-Disposition.</span>
            </a>
            <a href="https://recharts.github.io/en-US/guide/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Recharts - Guide</span><br>
                <span style="color: #6c757d; font-size: 13px;">BarChart, LineChart, ResponsiveContainer, Tooltip.</span>
            </a>
            <a href="https://ui.shadcn.com/docs/components/alert-dialog" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 shadcn/ui - Alert Dialog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Hộp thoại xác nhận cho thao tác không hoàn tác được.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Quản lý món và báo cáo doanh thu</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Thêm <code>productSchema</code> vào <code>lib/schemas.ts</code>; tạo <code>product-form.tsx</code>, trang <code>new</code> và <code>[id]/edit</code> dùng chung form.</li>
                <li>Khối tải ảnh trên trang sửa món: chọn file, xem trước, gửi qua <code>uploadProductImage</code>; cấu hình <code>next.config.ts</code>.</li>
                <li>Trang <code>/admin/reports</code>: bộ chọn khoảng ngày (form GET), biểu đồ doanh thu, bảng 5 món bán chạy, bảng tỉ lệ trạng thái.</li>
                <li>Route Handler xuất CSV; mở bằng Excel.</li>
                <li>Chạy TC-41…TC-46, TC-49; ghi kết quả.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Quản lý tài khoản nhân viên</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Trang <code>/admin/users</code>: danh sách tài khoản lọc theo vai trò và tìm theo tên/email, có phân trang qua URL; form tạo tài khoản staff (họ tên, email, mật khẩu ban đầu tối thiểu 8 ký tự; email trùng hiện "Email đã được sử dụng"); nút Khóa/Mở khóa có hộp thoại xác nhận; trạng thái khóa hiển thị bằng chữ.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp link repo và kết quả TC-47, TC-48 cùng ít nhất 3 test case tự viết cho form tạo tài khoản.</p>
            <a href="{{LINK_NOP_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <p style="margin: 0; color: #495057;">Hoàn thiện các trang quản trị của đề tài nhóm theo mẫu CRUD thống nhất. Mỗi ràng buộc nghiệp vụ trong danh mục stored procedure (bài 07) có ít nhất một test case trên giao diện web kèm kết quả (CLO2). Ảnh chụp biểu đồ đưa vào báo cáo phải có số hình và chú thích.</p>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Quản lý căn tin muốn biết "món nào nên nấu ít lại". Báo cáo hiện có trả lời được câu hỏi đó chưa? Nếu chưa, cần thêm số liệu gì và biểu đồ nào?</p>
            <a href="{{LINK_DIEN_DAN_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập mẫu CRUD, tải ảnh, biểu đồ, xuất CSV và kiểm thử ràng buộc quản trị.</p>
            <a href="{{LINK_QUIZ_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 08</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Lỗi "Body exceeded 1 MB limit" khi tải ảnh:</strong> chưa tăng <code>serverActions.bodySizeLimit</code> trong <code>next.config.ts</code>, hoặc chưa khởi động lại <code>npm run dev</code> sau khi sửa.</p>
        <p><strong>API báo "Không có file" dù đã chọn ảnh:</strong> đã tự đặt <code>Content-Type</code>, hoặc tên trường không phải <code>file</code>, hoặc thiếu thuộc tính <code>name="file"</code> trên ô chọn file.</p>
        <p><strong>next/image báo "hostname is not configured":</strong> thêm địa chỉ API vào <code>images.remotePatterns</code>. Khi <code>imageUrl</code> rỗng, hiện ảnh thay thế.</p>
        <p><strong>Biểu đồ trống hoặc báo lỗi "window is not defined":</strong> component Recharts thiếu <code>'use client'</code>; hoặc <code>ResponsiveContainer</code> nằm trong khối không có chiều cao.</p>
        <p><strong>Kiến thức mở rộng:</strong> xuất file <code>.xlsx</code> có định dạng bằng thư viện ExcelJS trong Route Handler; nén ảnh trước khi tải lên bằng canvas ở client để giảm dung lượng.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu một người bạn mở trang quản trị của nhóm lần đầu, họ có thêm được một món kèm ảnh và tìm được doanh thu tuần trước mà không cần hỏi không?</p>
    </div>
</details>
