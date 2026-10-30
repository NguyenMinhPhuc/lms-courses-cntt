<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 10 - Kiểm thử ứng dụng web, hiệu năng &amp; accessibility (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Ba sprint qua, nhóm đã viết gần 50 test case và chạy tay từng cái. Mỗi lần sửa một dòng mã, chạy lại hết mất cả buổi, nên không ai chạy lại. Hôm nay máy làm việc đó: bấm một lệnh, 30 giây sau biết ngay chức năng nào vừa hỏng. Và câu hỏi khó hơn: AI viết test cho bạn trong một phút, nhưng làm sao biết test đó thật sự kiểm tra được gì?</em></p>
        <p><strong>Mục tiêu:</strong> Lập được kế hoạch kiểm thử và ma trận truy vết yêu cầu – test case – kết quả; thực hiện được kiểm thử đơn vị, component và đầu-cuối; kiểm chứng được giá trị của test bằng đột biến thủ công; đo và cải thiện được hiệu năng, SEO, accessibility; lập được báo cáo kiểm thử.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Kế hoạch kiểm thử và ma trận truy vết:</strong> chọn mức kiểm thử cho từng yêu cầu, truy vết tới tiêu chí nghiệm thu.</li>
            <li><strong>Ý chính 2 - Vitest và Testing Library:</strong> kiểm thử hàm, schema, component, Server Action với API giả.</li>
            <li><strong>Ý chính 3 - Playwright:</strong> kịch bản đầu-cuối nhiều vai trò, báo cáo HTML, đột biến thủ công để kiểm chứng test do AI sinh.</li>
            <li><strong>Ý chính 4 - Hiệu năng, SEO và accessibility:</strong> Lighthouse, Core Web Vitals, <code>next/image</code>, metadata, sitemap, nhãn form, bàn phím, tương phản.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Dự án có bộ test tự động chạy bằng một lệnh, một kịch bản Playwright cho luồng đặt món, số đo Lighthouse trước và sau tối ưu; nhóm có bản nháp báo cáo kiểm thử.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO2.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Kế hoạch kiểm thử và ma trận truy vết</h3>
            <p>Không phải mọi thứ đều cần test tự động, và không phải test nào cũng chạy ở cùng một mức. Chọn mức theo việc cần kiểm tra:</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mức</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Công cụ</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Dùng cho</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Ví dụ LHU Food</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Đơn vị</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Vitest</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Hàm thuần, schema, store; nhanh, chạy hàng trăm test trong vài giây</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Giỏ hàng cộng dồn, <code>registerSchema</code> biên 7/8 ký tự</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Component</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Vitest + Testing Library</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Client Component hiển thị và phản hồi đúng</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nút "Hết món" bị vô hiệu</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Server Action</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Vitest, API giả</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Xử lý lỗi 400/409, kiểm tra dữ liệu ở server</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>placeOrder</code> trả "Có món đã hết" khi API trả 409</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Đầu-cuối</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Playwright</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Luồng nghiệp vụ qua trình duyệt thật, backend thật; Server Component <code>async</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Khách đặt món → nhân viên xử lý</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Thủ công</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Kịch bản test case</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Âm báo, hiển thị trên điện thoại, mất mạng</td><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-53 (bài 09)</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;">Vitest chưa hỗ trợ Server Component <code>async</code>; các trang loại này được kiểm bằng Playwright. <strong>Ma trận truy vết</strong> nối mỗi tiêu chí nghiệm thu trong SRS với test kiểm tra nó và kết quả lần chạy cuối. Đây là phần trung tâm của báo cáo kiểm thử (CLO2), cùng cách làm với học phần Kiểm thử phần mềm:</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Story</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Tiêu chí nghiệm thu</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Test</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Mức</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Lỗi liên quan</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-C01</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thêm trùng thì cộng dồn</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>cart-store.test.ts</code> › cộng dồn</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đơn vị</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đạt</td><td style="border: 1px solid #ffd6ad; padding: 6px;">–</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-C04</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thiếu tồn kho trả 409, không tạo đơn</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>checkout.test.ts</code>; <code>order-flow.spec.ts</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Action, E2E</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đạt</td><td style="border: 1px solid #ffd6ad; padding: 6px;">#23 (đã sửa)</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-S03</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Sai trình tự trạng thái trả 409</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>order-flow.spec.ts</code> › hai nhân viên</td><td style="border: 1px solid #ffd6ad; padding: 6px;">E2E</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                </tbody>
            </table>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Vitest và Testing Library</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>npm install -D vitest @vitejs/plugin-react jsdom vite-tsconfig-paths \
  @testing-library/react @testing-library/dom @testing-library/user-event

// vitest.config.mts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  plugins: [tsconfigPaths(), react()],        // hiểu alias @/ của Next.js
  test: { environment: 'jsdom', exclude: ['e2e/**', 'node_modules/**'] },
});

// package.json → "scripts": { "test": "vitest run", "test:watch": "vitest" }</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/cart-store.test.ts: kiểm thử đơn vị, mỗi test gắn với một tiêu chí
import { beforeEach, describe, expect, it } from 'vitest';
import { useCart, cartTotal } from './cart-store';

const com = { id: 1, name: 'Cơm gà xối mỡ', price: 35000, isAvailable: true, stock: 10 } as any;

describe('Giỏ hàng (US-C01, US-C02)', () =&gt; {
  beforeEach(() =&gt; useCart.getState().clear());

  it('thêm cùng một món hai lần thì một dòng, số lượng 2', () =&gt; {
    useCart.getState().add(com);
    useCart.getState().add(com);
    expect(useCart.getState().items).toEqual([{ productId: 1, name: 'Cơm gà xối mỡ', price: 35000, quantity: 2 }]);
  });

  it('giảm số lượng về 0 thì xóa món', () =&gt; {
    useCart.getState().add(com);
    useCart.getState().setQuantity(1, 0);
    expect(useCart.getState().items).toHaveLength(0);
  });

  it('tổng tiền bằng tổng giá × số lượng', () =&gt; {
    expect(cartTotal([{ productId: 1, name: 'A', price: 35000, quantity: 2 }, { productId: 2, name: 'B', price: 15000, quantity: 1 }]))
      .toBe(85000);
  });
});</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// components/add-to-cart-button.test.tsx: kiểm thử component
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { expect, it } from 'vitest';
import { AddToCartButton } from './add-to-cart-button';
import { useCart } from '@/lib/cart-store';

it('món hết hàng: nút ghi "Hết món" và không bấm được (US-G03)', async () =&gt; {
  render(&lt;AddToCartButton product={{ id: 2, name: 'Bún bò', price: 40000, isAvailable: true, stock: 0 } as any} /&gt;);
  const button = screen.getByRole('button', { name: 'Hết món' });   // tìm như người dùng thấy
  expect((button as HTMLButtonElement).disabled).toBe(true);   // hoặc toBeDisabled() nếu cài @testing-library/jest-dom
  await userEvent.click(button);
  expect(useCart.getState().items).toHaveLength(0);
});</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/(shop)/checkout/actions.test.ts: Server Action với API giả
import { afterEach, expect, it, vi } from 'vitest';
vi.mock('server-only', () =&gt; ({}));                                   // gói này chặn mọi môi trường ngoài server
vi.mock('@/lib/session', () =&gt; ({ getAccessToken: async () =&gt; 'token-gia' }));
import { placeOrder } from './actions';

afterEach(() =&gt; vi.unstubAllGlobals());

it('API trả 409 thì báo "Có món đã hết hoặc không đủ số lượng" (US-C04)', async () =&gt; {
  vi.stubGlobal('fetch', vi.fn(async () =&gt; new Response('{}', { status: 409 })));
  const result = await placeOrder({ items: [{ productId: 1, quantity: 99 }] });
  expect(result).toEqual({ ok: false, message: 'Có món đã hết hoặc không đủ số lượng' });
});

it('giỏ rỗng bị từ chối ngay ở server, không gọi API', async () =&gt; {
  const fetchMock = vi.fn();
  vi.stubGlobal('fetch', fetchMock);
  const result = await placeOrder({ items: [] });
  expect(result.ok).toBe(false);
  expect(fetchMock).not.toHaveBeenCalled();
});</code></pre>
            <p style="margin-bottom: 0;">Tìm phần tử bằng <code>getByRole</code> và tên hiển thị, không bằng class CSS: test vừa kiểm chức năng vừa kiểm luôn accessibility (nút không có tên thì không tìm được). Đặt tên test bằng tiếng Việt, theo tiêu chí nghiệm thu, để kết quả chạy dán thẳng vào báo cáo.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Playwright và kiểm chứng test do AI sinh</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>npm init playwright@latest        # chọn thư mục e2e, TypeScript

// playwright.config.ts (phần chính)
export default defineConfig({
  testDir: './e2e',
  use: { baseURL: 'http://localhost:3000', trace: 'on-first-retry' },
  webServer: { command: 'npm run build &amp;&amp; npm run start', url: 'http://localhost:3000', reuseExistingServer: true },
  reporter: [['html', { open: 'never' }]],
});</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// e2e/order-flow.spec.ts: hai vai trò, hai phiên trình duyệt độc lập
import { test, expect, type Page } from '@playwright/test';

async function login(page: Page, email: string, password: string) {
  await page.goto('/login');
  await page.getByLabel('Email').fill(email);
  await page.getByLabel('Mật khẩu').fill(password);
  await page.getByRole('button', { name: 'Đăng nhập' }).click();
}

test('khách đặt món, nhân viên nhận và chuyển sang Đang chuẩn bị (US-C04, S02, S03)', async ({ browser }) =&gt; {
  const customer = await (await browser.newContext()).newPage();
  const staff = await (await browser.newContext()).newPage();
  await login(customer, process.env.E2E_CUSTOMER_EMAIL!, process.env.E2E_CUSTOMER_PASSWORD!);
  await login(staff, process.env.E2E_STAFF_EMAIL!, process.env.E2E_STAFF_PASSWORD!);
  await expect(staff).toHaveURL(/\/admin\/orders/);

  const note = `E2E ${Date.now()}`;                         // dữ liệu riêng để tìm đúng đơn
  await customer.goto('/menu');
  await customer.getByRole('button', { name: 'Thêm vào giỏ' }).first().click();
  await customer.goto('/checkout');
  await customer.getByLabel('Ghi chú').fill(note);
  await customer.getByRole('button', { name: 'Đặt món' }).click();
  await expect(customer).toHaveURL(/\/orders\/\d+/);

  const card = staff.getByRole('article').filter({ hasText: note });
  await expect(card).toBeVisible({ timeout: 5000 });          // realtime: không tải lại trang
  await card.getByRole('button', { name: 'Bắt đầu làm' }).click();
  await expect(card).toContainText('Đang chuẩn bị');
});</code></pre>
            <ul>
                <li>Tài khoản thử đặt trong biến môi trường (<code>.env.test</code>, không commit); chạy trên CSDL thử, không chạy trên CSDL đang demo.</li>
                <li>Chạy <code>npx playwright test</code>, xem báo cáo bằng <code>npx playwright show-report</code>. Ảnh chụp báo cáo HTML là minh chứng cho báo cáo kiểm thử.</li>
                <li><code>npx playwright codegen localhost:3000</code> ghi lại thao tác thành mã: tiện để bắt đầu, nhưng phải sửa lại cách tìm phần tử theo vai trò và nhãn.</li>
            </ul>
            <p><strong>Đột biến thủ công (mutation): test do AI sinh có giá trị không?</strong> AI viết test rất nhanh, nhưng hay viết test "luôn đạt": kiểm tra lại đúng cái mã vừa làm, hoặc không có <code>expect</code> nào có ý nghĩa. Cách kiểm chứng: cố ý làm hỏng mã, chạy lại test.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Đột biến (sửa tạm mã)</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Test phải bắt được</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Đổi <code>.min(8)</code> thành <code>.min(7)</code> trong <code>registerSchema</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Test biên mật khẩu 7 ký tự</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Bị bắt / Lọt</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Bỏ nhánh <code>quantity &lt;= 0</code> trong <code>setQuantity</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">"giảm về 0 thì xóa món"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">Xóa <code>disabled={soldOut}</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Test nút "Hết món"</td><td style="border: 1px solid #ffd6ad; padding: 6px;">…</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;">Đột biến "lọt" nghĩa là chưa có test nào kiểm tra hành vi đó: viết thêm test, rồi hoàn tác đột biến. Ghi bảng đột biến vào báo cáo kiểm thử như bằng chứng bộ test có giá trị.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Hiệu năng, SEO và accessibility</h3>
            <p>Đo trên <strong>bản production</strong> (<code>npm run build &amp;&amp; npm start</code>), cửa sổ ẩn danh, bằng Lighthouse trong Chrome DevTools. Bản <code>npm run dev</code> chậm hơn nhiều và không phản ánh thực tế.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Chỉ số Core Web Vitals</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Ý nghĩa</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Mức tốt</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Cách cải thiện trong LHU Food</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">LCP</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thời gian hiện phần nội dung lớn nhất</td><td style="border: 1px solid #ffd6ad; padding: 6px;">≤ 2,5 giây</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>next/image</code> có kích thước, ảnh đầu trang tải sớm; Server Component; cache danh mục</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">INP</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Độ trễ phản hồi khi bấm, gõ</td><td style="border: 1px solid #ffd6ad; padding: 6px;">≤ 200 ms</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Ít JavaScript ở client; không lọc danh sách lớn trên mỗi phím gõ</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">CLS</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Độ "nhảy" bố cục khi tải</td><td style="border: 1px solid #ffd6ad; padding: 6px;">≤ 0,1</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Ảnh có <code>width</code>/<code>height</code>; khung chờ cùng kích thước nội dung thật</td></tr>
                </tbody>
            </table>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// SEO: tiêu đề theo tên món
// app/(shop)/product/[id]/page.tsx
export async function generateMetadata({ params }: { params: Promise&lt;{ id: string }&gt; }) {
  const { id } = await params;
  const p = await apiGet&lt;Product&gt;(`/products/${id}`, 60);
  return { title: `${p.name} - LHU Food`, description: p.description ?? `Giá ${p.price.toLocaleString('vi-VN')} đ` };
}

// app/sitemap.ts: danh sách trang công khai cho công cụ tìm kiếm (không đưa /admin vào)
export default async function sitemap() {
  const products = await apiGet&lt;Product[]&gt;('/products?pageSize=100', 3600);
  return [{ url: `${process.env.SITE_URL}/menu` },
          ...products.map((p) =&gt; ({ url: `${process.env.SITE_URL}/product/${p.id}` }))];
}</code></pre>
            <p><strong>Accessibility (khả năng tiếp cận)</strong>: mọi người dùng được, kể cả người dùng bàn phím, trình đọc màn hình, người nhìn kém.</p>
            <ul>
                <li>Mỗi ô nhập có <code>&lt;label&gt;</code>; lỗi gắn với ô bằng <code>aria-describedby</code>; thông báo chung có <code>role="alert"</code>.</li>
                <li>Dùng được hoàn toàn bằng bàn phím: Tab đi đúng thứ tự, thấy rõ ô đang được chọn, hộp thoại giữ tiêu điểm bên trong (shadcn/ui đã làm sẵn).</li>
                <li>Tương phản chữ/nền tối thiểu 4,5:1; trạng thái không chỉ dùng màu; ảnh món có <code>alt</code> là tên món.</li>
                <li>Kiểm tự động thêm bằng <code>@axe-core/playwright</code> trong kịch bản E2E; vẫn phải thử tay bằng bàn phím.</li>
            </ul>
            <p style="margin-bottom: 0;"><strong>Báo cáo kiểm thử (CLO2)</strong> gồm: kế hoạch (phạm vi, mức, công cụ, môi trường, dữ liệu thử); ma trận truy vết; kết quả (số test, đạt, không đạt, ảnh báo cáo Vitest và Playwright); bảng đột biến; lỗi tìm được và cách khắc phục (liên kết thẻ trên board); số đo Lighthouse trước và sau tối ưu. Báo cáo này là Chương 5 của báo cáo đồ án.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 10: Kiểm thử ứng dụng web, hiệu năng &amp; accessibility</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tiêu chí nghiệm thu của mọi story web (nguồn của ma trận truy vết); mục 9: yêu cầu phi chức năng.</span>
            </a>
            <a href="{{LINK_RUBRIC}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📊 Rubric chấm điểm</span><br>
                <span style="color: #6c757d; font-size: 13px;">Các tiêu chí CLO2: kế hoạch, ma trận truy vết, kết quả, lỗi và khắc phục.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://nextjs.org/docs/app/guides/testing/vitest" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Next.js - Setting up Vitest</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cấu hình Vitest cho App Router, giới hạn với Server Component async.</span>
            </a>
            <a href="https://playwright.dev/docs/intro" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Playwright - Getting started</span><br>
                <span style="color: #6c757d; font-size: 13px;">Locator theo vai trò, browser context, báo cáo HTML, codegen.</span>
            </a>
            <a href="https://testing-library.com/docs/queries/about" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Testing Library - Queries</span><br>
                <span style="color: #6c757d; font-size: 13px;">Thứ tự ưu tiên khi tìm phần tử: getByRole, getByLabelText…</span>
            </a>
            <a href="https://web.dev/articles/vitals" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 web.dev - Web Vitals</span><br>
                <span style="color: #6c757d; font-size: 13px;">LCP, INP, CLS và ngưỡng đánh giá.</span>
            </a>
            <a href="https://www.w3.org/WAI/standards-guidelines/wcag/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 W3C - WCAG Overview</span><br>
                <span style="color: #6c757d; font-size: 13px;">Hướng dẫn tiếp cận nội dung web: nhãn, bàn phím, tương phản.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Test tự động và đo Lighthouse</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Cài Vitest; viết test cho giỏ hàng, <code>registerSchema</code> (biên), <code>AddToCartButton</code>, <code>placeOrder</code> với API giả; chạy <code>npm test</code>.</li>
                <li>Cài Playwright; viết <code>order-flow.spec.ts</code> với hai phiên; xem báo cáo HTML.</li>
                <li>Thử ba đột biến ở bảng mục 2.3, ghi kết quả, hoàn tác.</li>
                <li>Đo Lighthouse trang <code>/menu</code> trên bản production; sửa ảnh (<code>next/image</code>, kích thước), thêm <code>generateMetadata</code>; đo lại, ghi bảng trước/sau.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): 5 test có giá trị</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Chọn một module bạn phụ trách (ví dụ quản lý quầy, hủy đơn, báo cáo). Viết 5 test tự động ở mức phù hợp, mỗi test truy vết tới một tiêu chí nghiệm thu. Được dùng AI để sinh test, nhưng phải kiểm chứng bằng ít nhất 3 đột biến thủ công.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp link repo, ảnh kết quả chạy test, bảng truy vết 5 test và bảng đột biến (đột biến nào lọt thì đã viết thêm test gì).</p>
            <a href="{{LINK_NOP_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <p style="margin: 0; color: #495057;">Xây bộ test cho các luồng chính của web nhóm (ít nhất: đặt món, phân quyền, màn hình quầy, một chức năng quản trị). Viết <strong>báo cáo kiểm thử</strong> theo cấu trúc cuối mục 2.4 (CLO2). Mọi lỗi tìm được có thẻ trên board và liên kết Pull Request sửa lỗi.</p>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Chia sẻ một test do AI sinh mà bạn phát hiện là "luôn đạt" nhờ đột biến thủ công. Test đó sai ở đâu, và bạn đã sửa thế nào?</p>
            <a href="{{LINK_DIEN_DAN_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập mức kiểm thử, ma trận truy vết, Vitest, Playwright, đột biến, Core Web Vitals và accessibility.</p>
            <a href="{{LINK_QUIZ_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 10</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Lỗi "This module cannot be imported from a Client Component module" khi chạy Vitest:</strong> file được test có <code>import 'server-only'</code>. Thêm <code>vi.mock('server-only', () =&gt; ({}))</code> ở đầu file test.</p>
        <p><strong>Test giỏ hàng ảnh hưởng lẫn nhau:</strong> store Zustand dùng chung giữa các test; gọi <code>clear()</code> trong <code>beforeEach</code>.</p>
        <p><strong>Playwright báo không tìm thấy phần tử dù trang có hiển thị:</strong> tên nút hoặc nhãn trong test khác chữ trên giao diện; thiếu <code>&lt;label&gt;</code> cho ô nhập. Sửa giao diện cho có nhãn là sửa luôn một lỗi accessibility.</p>
        <p><strong>Điểm Lighthouse dao động mỗi lần đo:</strong> đo 3 lần lấy trung vị, cùng máy, cùng chế độ (Mobile/Desktop), tắt tiện ích trình duyệt.</p>
        <p><strong>Kiến thức mở rộng:</strong> chạy test tự động trên GitHub Actions mỗi khi mở Pull Request; công cụ đột biến tự động Stryker cho JavaScript.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu xóa một dòng quan trọng bất kỳ trong module của bạn, có ít nhất một test chuyển sang đỏ không?</p>
    </div>
</details>
