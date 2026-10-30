# Bài 10: Kiểm thử ứng dụng web, hiệu năng & accessibility
Sprint 4 · Chất lượng & Phát hành

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Kế hoạch kiểm thử và ma trận truy vết
- Kiểm thử đơn vị, component, đầu-cuối
- Kiểm chứng test do AI sinh bằng đột biến
- Đo và cải thiện hiệu năng, SEO, accessibility
**Ghi chú giảng viên**:
- 2 tiết lý thuyết, 3 tiết thực hành. CLO2. Liên hệ học phần Kiểm thử phần mềm.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Gần 50 test case chạy tay
- Sửa một dòng → không ai chạy lại hết
- AI viết test trong một phút: test đó kiểm tra được gì?

---

## Slide 3: Chọn mức kiểm thử
**Nội dung chính**:
- Đơn vị (Vitest): hàm, schema, store
- Component (Testing Library): Client Component
- Server Action: API giả, xử lý 400/409
- Đầu-cuối (Playwright): luồng nghiệp vụ, Server Component async
- Thủ công: âm báo, điện thoại, mất mạng

---

## Slide 4: Ma trận truy vết (CLO2)
**Nội dung chính**:
- Story → tiêu chí nghiệm thu → test → mức → kết quả → lỗi
- Mỗi tiêu chí có ít nhất một test
- Phần trung tâm của báo cáo kiểm thử
**Hoạt động**: Nhóm lập ma trận cho 5 story quan trọng nhất

---

## Slide 5: Cài Vitest
**Nội dung chính**:
```text
npm install -D vitest @vitejs/plugin-react jsdom vite-tsconfig-paths
  @testing-library/react @testing-library/dom @testing-library/user-event
```
- vitest.config.mts: tsconfigPaths, react, environment jsdom
- "test": "vitest run"

---

## Slide 6: Test đơn vị giỏ hàng
**Nội dung chính**:
```ts
it('thêm cùng một món hai lần thì một dòng, số lượng 2', () => {
  useCart.getState().add(com);
  useCart.getState().add(com);
  expect(useCart.getState().items[0].quantity).toBe(2);
});
```
- Tên test theo tiêu chí nghiệm thu, bằng tiếng Việt

---

## Slide 7: Test component
**Nội dung chính**:
- render(<AddToCartButton product={...stock: 0} />)
- getByRole('button', { name: 'Hết món' })
- Nút bị vô hiệu, bấm không thêm vào giỏ
- Không tìm được nút = lỗi accessibility

---

## Slide 8: Test Server Action
**Nội dung chính**:
- vi.mock('server-only'), vi.mock('@/lib/session')
- vi.stubGlobal('fetch', ...) trả 409
- Mong đợi: "Có món đã hết hoặc không đủ số lượng"
- Giỏ rỗng: bị từ chối, không gọi API

---

## Slide 9: Playwright
**Nội dung chính**:
- npm init playwright@latest
- webServer: build + start, baseURL
- Hai browser context: khách và nhân viên
- Báo cáo HTML: minh chứng cho báo cáo kiểm thử

---

## Slide 10: Kịch bản đặt món đầu-cuối
**Nội dung chính**:
- Khách: menu → thêm vào giỏ → checkout (ghi chú riêng) → đặt
- Nhân viên: thấy đơn có ghi chú đó, không tải lại trang
- Bấm "Bắt đầu làm" → "Đang chuẩn bị"
- Tài khoản thử trong .env.test, CSDL thử

---

## Slide 11: Test do AI sinh có giá trị không?
**Nội dung chính**:
- AI hay viết test "luôn đạt"
- Đột biến: cố ý làm hỏng mã, chạy lại test
- Bị bắt: test có giá trị; lọt: viết thêm test
- Ghi bảng đột biến vào báo cáo

---

## Slide 12: Core Web Vitals
**Nội dung chính**:
- LCP ≤ 2,5 s: next/image, Server Component, cache
- INP ≤ 200 ms: ít JavaScript ở client
- CLS ≤ 0,1: ảnh có kích thước, khung chờ đúng cỡ
- Đo trên bản production, lấy trung vị 3 lần

---

## Slide 13: SEO
**Nội dung chính**:
- generateMetadata: tiêu đề theo tên món
- app/sitemap.ts: chỉ trang công khai
- Không đưa /admin vào sitemap

---

## Slide 14: Accessibility
**Nội dung chính**:
- Ô nhập có label; lỗi gắn aria-describedby
- Dùng được hoàn toàn bằng bàn phím
- Tương phản ≥ 4,5:1; trạng thái không chỉ bằng màu
- @axe-core/playwright + thử tay

---

## Slide 15: Báo cáo kiểm thử
**Nội dung chính**:
- Kế hoạch: phạm vi, mức, công cụ, môi trường, dữ liệu
- Ma trận truy vết; kết quả; bảng đột biến
- Lỗi và khắc phục (thẻ board, PR)
- Lighthouse trước/sau → Chương 5 báo cáo đồ án

---

## Slide 16: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: Vitest (giỏ, schema, nút, action), Playwright, 3 đột biến, Lighthouse
- **Không hướng dẫn**: 5 test có giá trị + 3 đột biến cho module tự chọn
- **Nhóm**: bộ test luồng chính, báo cáo kiểm thử

---

## Slide 17: Tổng kết
**Nội dung chính**:
- Đúng mức kiểm thử cho đúng việc
- Mỗi test truy vết tới một tiêu chí
- Đột biến để biết test có giá trị
- Buổi sau: triển khai server Khoa, hoàn thiện báo cáo

---

## Slide 18: Tài liệu của buổi
**Đọc thêm**:
- SRS LHU Food: tiêu chí nghiệm thu; mục 9 (phi chức năng)
- Next.js: Setting up Vitest; Playwright: Getting started
- Testing Library: Queries; web.dev: Web Vitals; W3C WCAG
**Ghi chú giảng viên**:
- Chuẩn bị CSDL thử riêng cho E2E để không làm bẩn dữ liệu demo của nhóm.
