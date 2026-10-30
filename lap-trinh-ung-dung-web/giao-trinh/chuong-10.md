# Chương 10. Kiểm thử ứng dụng web, hiệu năng và accessibility

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Lập kế hoạch kiểm thử, chọn mức kiểm thử phù hợp cho từng yêu cầu và lập ma trận truy vết.
- Viết kiểm thử đơn vị, kiểm thử component và kiểm thử Server Action bằng Vitest và Testing Library.
- Viết kịch bản kiểm thử đầu-cuối nhiều vai trò bằng Playwright.
- Kiểm chứng giá trị của bộ test (kể cả test do AI sinh) bằng đột biến thủ công.
- Đo và cải thiện hiệu năng (Core Web Vitals), SEO và accessibility.
- Lập báo cáo kiểm thử làm Chương 5 của báo cáo đồ án.

## 10.1. Kế hoạch kiểm thử

### 10.1.1. Vì sao cần kiểm thử tự động

Ba sprint qua, nhóm đã viết gần 50 test case và chạy tay từng cái. Mỗi lần sửa một dòng mã, chạy lại hết mất cả buổi, nên trên thực tế không ai chạy lại. Kiểm thử tự động biến bộ test case thành mã: một lệnh chạy toàn bộ trong vài chục giây, chạy lại được sau mỗi thay đổi. Đây cũng là cách làm kiểm thử hồi quy (Chương 7) bền vững.

### 10.1.2. Chọn mức kiểm thử

Không phải mọi thứ đều cần test tự động, và không phải test nào cũng chạy ở cùng một mức. Chọn mức theo việc cần kiểm tra:

| Mức | Công cụ | Dùng cho | Ví dụ LHU Food |
|---|---|---|---|
| Đơn vị | Vitest | Hàm thuần, schema, store; chạy hàng trăm test trong vài giây | Giỏ hàng cộng dồn, `registerSchema` biên 7/8 ký tự |
| Component | Vitest + Testing Library | Client Component hiển thị và phản hồi đúng | Nút "Hết món" bị vô hiệu |
| Server Action | Vitest, API giả | Xử lý lỗi 400/409, kiểm tra dữ liệu ở server | `placeOrder` trả "Có món đã hết" khi API trả 409 |
| Đầu-cuối (E2E) | Playwright | Luồng nghiệp vụ qua trình duyệt thật, backend thật; Server Component async | Khách đặt món → nhân viên xử lý |
| Thủ công | Kịch bản test case | Âm báo, hiển thị trên điện thoại, mất mạng | TC-53 (Chương 9) |

Test đơn vị nhanh, rẻ, chỉ ra chính xác chỗ sai nhưng không chứng minh các phần ghép với nhau chạy đúng. Test đầu-cuối chứng minh luồng nghiệp vụ nhưng chậm và dễ hỏng vì lý do ngoài mã (mạng, dữ liệu). Bộ test tốt có nhiều test đơn vị, một số test component, ít test đầu-cuối cho các luồng quan trọng nhất.

Vitest hiện chưa hỗ trợ Server Component `async`; các trang loại này được kiểm bằng Playwright [1].

### 10.1.3. Ma trận truy vết

**Ma trận truy vết** nối mỗi tiêu chí chấp nhận trong SRS (mục 4.7) với test kiểm tra nó và kết quả lần chạy cuối. Đây là phần trung tâm của báo cáo kiểm thử (CLO2), cùng cách làm với học phần Kiểm thử phần mềm:

| Story | Tiêu chí chấp nhận | Test | Mức | Kết quả | Lỗi liên quan |
|---|---|---|---|---|---|
| US-C01 | Thêm trùng thì cộng dồn | `cart-store.test.ts` › cộng dồn | Đơn vị | Đạt | – |
| US-C04 | Thiếu tồn kho trả 409, không tạo đơn | `checkout.test.ts`; `order-flow.spec.ts` | Action, E2E | Đạt | #23 (đã sửa) |
| US-S03 | Sai trình tự trạng thái trả 409 | `order-flow.spec.ts` › hai nhân viên | E2E | … | … |

Ma trận cho phép trả lời hai câu hỏi: tiêu chí nào chưa có test (lỗ hổng kiểm thử), và test nào không gắn với yêu cầu nào (test thừa).

### 10.1.4. Nội dung kế hoạch kiểm thử

Kế hoạch kiểm thử ngắn gọn gồm: phạm vi (story nào, khu vực nào), mức và công cụ, môi trường (CSDL thử riêng, tài khoản thử), dữ liệu thử, tiêu chí kết thúc (ví dụ: mọi story Must có ít nhất một test tự động đạt), người phụ trách.

## 10.2. Vitest và Testing Library

### 10.2.1. Cài đặt

```bash
npm install -D vitest @vitejs/plugin-react jsdom vite-tsconfig-paths \
  @testing-library/react @testing-library/dom @testing-library/user-event
```

```ts
// vitest.config.mts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  plugins: [tsconfigPaths(), react()],        // hiểu alias @/ của Next.js
  test: { environment: 'jsdom', exclude: ['e2e/**', 'node_modules/**'] },
});
```

Thêm vào `package.json`: `"test": "vitest run"` (chạy một lần) và `"test:watch": "vitest"` (chạy lại khi sửa file) [1].

### 10.2.2. Kiểm thử đơn vị

```ts
// lib/cart-store.test.ts
import { beforeEach, describe, expect, it } from 'vitest';
import { useCart, cartTotal } from './cart-store';

const com = { id: 1, name: 'Cơm gà xối mỡ', price: 35000, isAvailable: true, stock: 10 } as any;

describe('Giỏ hàng (US-C01, US-C02)', () => {
  beforeEach(() => useCart.getState().clear());

  it('thêm cùng một món hai lần thì một dòng, số lượng 2', () => {
    useCart.getState().add(com);
    useCart.getState().add(com);
    expect(useCart.getState().items).toEqual([{ productId: 1, name: 'Cơm gà xối mỡ', price: 35000, quantity: 2 }]);
  });

  it('giảm số lượng về 0 thì xóa món', () => {
    useCart.getState().add(com);
    useCart.getState().setQuantity(1, 0);
    expect(useCart.getState().items).toHaveLength(0);
  });

  it('tổng tiền bằng tổng giá × số lượng', () => {
    expect(cartTotal([{ productId: 1, name: 'A', price: 35000, quantity: 2 }, { productId: 2, name: 'B', price: 15000, quantity: 1 }]))
      .toBe(85000);
  });
});
```

- Đặt tên test bằng tiếng Việt, theo đúng tiêu chí chấp nhận; kết quả chạy dán thẳng vào báo cáo được.
- Store Zustand dùng chung giữa các test; `beforeEach` xóa giỏ để các test không ảnh hưởng nhau.
- Mỗi test theo cấu trúc chuẩn bị – thực hiện – kiểm tra (Arrange – Act – Assert).

### 10.2.3. Kiểm thử component

```tsx
// components/add-to-cart-button.test.tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { expect, it } from 'vitest';
import { AddToCartButton } from './add-to-cart-button';
import { useCart } from '@/lib/cart-store';

it('món hết hàng: nút ghi "Hết món" và không bấm được (US-G03)', async () => {
  render(<AddToCartButton product={{ id: 2, name: 'Bún bò', price: 40000, isAvailable: true, stock: 0 } as any} />);
  const button = screen.getByRole('button', { name: 'Hết món' });   // tìm như người dùng thấy
  expect((button as HTMLButtonElement).disabled).toBe(true);   // hoặc toBeDisabled() nếu cài @testing-library/jest-dom
  await userEvent.click(button);
  expect(useCart.getState().items).toHaveLength(0);
});
```

Testing Library khuyến khích tìm phần tử **như người dùng thấy**: theo vai trò và tên hiển thị (`getByRole`, `getByLabelText`), không theo class CSS [2]. Test vừa kiểm chức năng vừa kiểm accessibility: một nút không có tên đọc được thì test không tìm thấy nó.

### 10.2.4. Kiểm thử Server Action với API giả

```ts
// app/(shop)/checkout/actions.test.ts
import { afterEach, expect, it, vi } from 'vitest';
vi.mock('server-only', () => ({}));                                   // gói này chặn mọi môi trường ngoài server
vi.mock('@/lib/session', () => ({ getAccessToken: async () => 'token-gia' }));
import { placeOrder } from './actions';

afterEach(() => vi.unstubAllGlobals());

it('API trả 409 thì báo "Có món đã hết hoặc không đủ số lượng" (US-C04)', async () => {
  vi.stubGlobal('fetch', vi.fn(async () => new Response('{}', { status: 409 })));
  const result = await placeOrder({ items: [{ productId: 1, quantity: 99 }] });
  expect(result).toEqual({ ok: false, message: 'Có món đã hết hoặc không đủ số lượng' });
});

it('giỏ rỗng bị từ chối ngay ở server, không gọi API', async () => {
  const fetchMock = vi.fn();
  vi.stubGlobal('fetch', fetchMock);
  const result = await placeOrder({ items: [] });
  expect(result.ok).toBe(false);
  expect(fetchMock).not.toHaveBeenCalled();
});
```

`vi.stubGlobal('fetch', …)` thay `fetch` bằng hàm giả trả kết quả mong muốn, nhờ vậy kiểm được cách Server Action xử lý lỗi 409 mà không cần backend thật hay dữ liệu hết hàng thật. Test thứ hai chứng minh server tự kiểm tra dữ liệu (Chương 4).

## 10.3. Kiểm thử đầu-cuối với Playwright

### 10.3.1. Cài đặt và cấu hình

```bash
npm init playwright@latest        # chọn thư mục e2e, TypeScript
```

```ts
// playwright.config.ts (phần chính)
export default defineConfig({
  testDir: './e2e',
  use: { baseURL: 'http://localhost:3000', trace: 'on-first-retry' },
  webServer: { command: 'npm run build && npm run start', url: 'http://localhost:3000', reuseExistingServer: true },
  reporter: [['html', { open: 'never' }]],
});
```

`webServer` tự khởi động bản production trước khi chạy test. `trace` ghi lại từng bước khi test thất bại để xem lại [3].

### 10.3.2. Kịch bản nhiều vai trò

```ts
// e2e/order-flow.spec.ts
import { test, expect, type Page } from '@playwright/test';

async function login(page: Page, email: string, password: string) {
  await page.goto('/login');
  await page.getByLabel('Email').fill(email);
  await page.getByLabel('Mật khẩu').fill(password);
  await page.getByRole('button', { name: 'Đăng nhập' }).click();
}

test('khách đặt món, nhân viên nhận và chuyển sang Đang chuẩn bị (US-C04, S02, S03)', async ({ browser }) => {
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
});
```

- Mỗi `browser.newContext()` là một phiên trình duyệt độc lập với cookie riêng, như hai người dùng trên hai máy [4].
- Ghi chú có dấu thời gian giúp tìm đúng đơn vừa tạo giữa nhiều đơn khác.
- `expect(...).toBeVisible()` tự chờ tới khi điều kiện đúng hoặc hết thời gian, không cần `sleep`.
- Tài khoản thử đặt trong biến môi trường (`.env.test`, không commit). Chạy trên **CSDL thử**, không chạy trên CSDL đang dùng để demo.

Chạy `npx playwright test`, xem báo cáo bằng `npx playwright show-report`. Ảnh chụp báo cáo HTML là minh chứng cho báo cáo kiểm thử. Lệnh `npx playwright codegen localhost:3000` ghi thao tác thành mã, tiện để bắt đầu nhưng phải sửa lại cách tìm phần tử theo vai trò và nhãn.

## 10.4. Kiểm chứng test do AI sinh

### 10.4.1. Test "luôn đạt"

AI viết test rất nhanh, nhưng hay viết test **luôn đạt**: kiểm tra lại đúng cái mã vừa viết (sao chép logic vào test), chỉ kiểm tra "không ném lỗi", hoặc dùng `expect` vô nghĩa (`expect(result).toBeDefined()`). Một bộ test toàn màu xanh chưa chắc kiểm tra được gì.

### 10.4.2. Đột biến thủ công

Kiểm thử đột biến (mutation testing) đánh giá bộ test bằng cách cố ý tạo lỗi nhỏ trong mã (đột biến) rồi xem test có phát hiện không [5]. Làm thủ công:

| Đột biến (sửa tạm mã) | Test phải bắt được | Kết quả |
|---|---|---|
| Đổi `.min(8)` thành `.min(7)` trong `registerSchema` | Test biên mật khẩu 7 ký tự | Bị bắt / Lọt |
| Bỏ nhánh `quantity <= 0` trong `setQuantity` | "giảm về 0 thì xóa món" | … |
| Xóa `disabled={soldOut}` | Test nút "Hết món" | … |
| Bỏ `requireRole` trong `advanceStatus` | Test truy cập trái phép của Server Action | … |

Đột biến **bị bắt** (test chuyển đỏ): test có giá trị. Đột biến **lọt** (test vẫn xanh): chưa có test nào kiểm tra hành vi đó; viết thêm test, rồi hoàn tác đột biến. Bảng đột biến là bằng chứng trong báo cáo kiểm thử rằng bộ test thật sự kiểm tra yêu cầu.

## 10.5. Hiệu năng, SEO và accessibility

### 10.5.1. Đo hiệu năng

Đo trên **bản production** (`npm run build && npm start`), cửa sổ ẩn danh, bằng Lighthouse trong Chrome DevTools. Bản `npm run dev` chậm hơn nhiều và không phản ánh thực tế. Đo ba lần, lấy trung vị.

**Core Web Vitals** là ba chỉ số Google dùng để đánh giá trải nghiệm thực tế [6]:

| Chỉ số | Ý nghĩa | Mức tốt | Cách cải thiện trong LHU Food |
|---|---|---|---|
| LCP | Thời gian hiện phần nội dung lớn nhất | ≤ 2,5 giây | `next/image` có kích thước; ảnh đầu trang tải sớm; Server Component; cache danh mục |
| INP | Độ trễ phản hồi khi bấm, gõ | ≤ 200 ms | Ít JavaScript ở client; không lọc danh sách lớn trên mỗi phím gõ |
| CLS | Độ "nhảy" bố cục khi tải | ≤ 0,1 | Ảnh có `width`/`height`; khung chờ cùng kích thước nội dung thật |

Component `next/image` tự chọn kích thước và định dạng ảnh phù hợp với thiết bị, tải lười ảnh ngoài màn hình và giữ chỗ cho ảnh để bố cục không nhảy. Ghi bảng số đo trước và sau mỗi tối ưu vào báo cáo kiểm thử.

### 10.5.2. SEO

```tsx
// app/(shop)/product/[id]/page.tsx: tiêu đề theo tên món
export async function generateMetadata({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const p = await apiGet<Product>(`/products/${id}`, 60);
  return { title: `${p.name} - LHU Food`, description: p.description ?? `Giá ${p.price.toLocaleString('vi-VN')} đ` };
}

// app/sitemap.ts: danh sách trang công khai cho công cụ tìm kiếm (không đưa /admin vào)
export default async function sitemap() {
  const products = await apiGet<Product[]>('/products?pageSize=100', 3600);
  return [{ url: `${process.env.SITE_URL}/menu` },
          ...products.map((p) => ({ url: `${process.env.SITE_URL}/product/${p.id}` }))];
}
```

`generateMetadata` đặt tiêu đề và mô tả theo dữ liệu; `app/sitemap.ts` sinh file `sitemap.xml` [7]. Trang quản trị không đưa vào sitemap.

### 10.5.3. Accessibility

Accessibility (khả năng tiếp cận) bảo đảm mọi người dùng được ứng dụng, kể cả người dùng bàn phím, trình đọc màn hình, người nhìn kém. Hướng dẫn chuẩn là WCAG của W3C [8]. Những điểm tối thiểu cho LHU Food:

- Mỗi ô nhập có `<label>`; lỗi gắn với ô bằng `aria-describedby`; thông báo chung có `role="alert"`.
- Dùng được hoàn toàn bằng bàn phím: Tab đi đúng thứ tự, thấy rõ phần tử đang được chọn, hộp thoại giữ tiêu điểm bên trong (shadcn/ui đã làm sẵn).
- Tương phản chữ/nền tối thiểu 4,5:1; trạng thái không chỉ dùng màu (màn hình quầy ghi chữ "Đang chuẩn bị"); ảnh món có `alt` là tên món.
- `<html lang="vi">` để trình đọc màn hình đọc đúng tiếng Việt.

Kiểm tự động thêm bằng `@axe-core/playwright` trong kịch bản E2E; vẫn phải thử tay bằng bàn phím vì công cụ tự động chỉ phát hiện được một phần lỗi.

## 10.6. Báo cáo kiểm thử (CLO2)

Báo cáo kiểm thử là Chương 5 của báo cáo đồ án, gồm:

1. **Kế hoạch:** phạm vi, mức, công cụ, môi trường, dữ liệu thử, tiêu chí kết thúc.
2. **Ma trận truy vết:** mọi story Must của web có ít nhất một test.
3. **Kết quả:** số test, đạt, không đạt; ảnh kết quả Vitest và báo cáo HTML của Playwright.
4. **Bảng đột biến:** đột biến nào bị bắt, đột biến nào lọt và đã bổ sung test gì.
5. **Lỗi và khắc phục:** danh sách lỗi tìm được, liên kết thẻ trên board và Pull Request sửa lỗi.
6. **Kiểm thử phi chức năng:** số đo Lighthouse trước và sau tối ưu, kết quả kiểm tra accessibility.

## Tóm tắt chương

- Chọn mức kiểm thử theo việc cần kiểm tra; nhiều test đơn vị, ít test đầu-cuối cho luồng quan trọng.
- Ma trận truy vết nối tiêu chí chấp nhận – test – kết quả, chỉ ra lỗ hổng kiểm thử.
- Vitest cho hàm, store, component, Server Action (API giả); Playwright cho luồng nhiều vai trò trên trình duyệt thật.
- Đột biến thủ công kiểm chứng bộ test, đặc biệt test do AI sinh.
- Đo Core Web Vitals trên bản production; SEO bằng metadata và sitemap; accessibility theo WCAG.

## Câu hỏi ôn tập

1. Vì sao không viết toàn bộ bộ test bằng Playwright?
2. Trang thực đơn là Server Component async. Kiểm thử nó bằng công cụ nào? Vì sao?
3. Ma trận truy vết giúp phát hiện hai loại vấn đề nào?
4. Vì sao Testing Library khuyến khích `getByRole` thay cho tìm theo class CSS?
5. Viết một đột biến cho `staffCancel` (Chương 6) và test phải bắt được nó.
6. Ba chỉ số Core Web Vitals là gì? Mức tốt của từng chỉ số?
7. Nêu ba lỗi accessibility hay gặp trên trang quản trị và cách sửa.

## Bài tập

1. **Năm test có giá trị.** Viết 5 test tự động cho một module bạn phụ trách, mỗi test truy vết tới một tiêu chí; kiểm chứng bằng 3 đột biến.
2. **Kịch bản phân quyền E2E.** Viết kịch bản Playwright cho TC-21 và TC-22 (Chương 5).
3. **Tối ưu LCP.** Đo Lighthouse trang `/menu`, thực hiện một tối ưu, đo lại và giải thích kết quả.

## Tài liệu tham khảo

[1] Vercel, “How to set up Vitest with Next.js,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/guides/testing/vitest

[2] Testing Library, “About Queries,” *Testing Library Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://testing-library.com/docs/queries/about

[3] Microsoft, “Installation,” *Playwright Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://playwright.dev/docs/intro

[4] Microsoft, “Isolation,” *Playwright Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://playwright.dev/docs/browser-contexts

[5] Stryker Mutator, “What is mutation testing?,” *Stryker Mutator Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://stryker-mutator.io/docs/

[6] Google, “Web Vitals,” *web.dev*. Accessed: Oct. 30, 2026. [Online]. Available: https://web.dev/articles/vitals

[7] Vercel, “Metadata and OG images,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/metadata-and-og-images

[8] W3C Web Accessibility Initiative, “WCAG 2 Overview,” *W3C*. Accessed: Oct. 30, 2026. [Online]. Available: https://www.w3.org/WAI/standards-guidelines/wcag/
