# Bài 05: Xác thực, phân quyền & bảo mật web
Sprint 2 · Người dùng & Tương tác

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Phân tích phân quyền thành ma trận vai trò × chức năng
- Đăng nhập bằng JWT của backend, cookie httpOnly
- Bảo vệ route bằng proxy và kiểm tra lại ở server
- Nhận diện rủi ro web, kiểm thử truy cập trái phép
**Ghi chú giảng viên**:
- 2 tiết lý thuyết, 3 tiết thực hành. CLO1, CLO2. Chuẩn bị tài khoản customer, staff, admin trên API mẫu.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Menu quản trị đã ẩn với sinh viên
- Gõ thẳng /admin/products: trang có mở không?
- Ẩn menu không phải là phân quyền

---

## Slide 3: Luồng xác thực web
**Nội dung chính**:
```text
Form ─▶ Server Action ─POST /auth/login─▶ API
     ◀─ Set-Cookie: access_token, refresh_token (httpOnly)
Request sau: cookie ─▶ Next.js ─Bearer token─▶ API
```

---

## Slide 4: Cookie httpOnly
**Nội dung chính**:
- httpOnly: JavaScript không đọc được → XSS không lấy được token
- Secure: chỉ gửi qua HTTPS khi chạy thật
- SameSite=Lax: không gửi kèm POST từ trang khác
- Không lưu token trong localStorage

---

## Slide 5: loginAction
**Nội dung chính**:
- Kiểm tra Zod, gọi POST /auth/login
- 401 → "Email hoặc mật khẩu không đúng" (BR-03)
- 403 → "Tài khoản đã bị khóa"
- Ghi cookie, chuyển hướng theo vai trò hoặc tham số next an toàn

---

## Slide 6: Ma trận phân quyền (CLO1)
**Nội dung chính**:
- /menu: mọi người
- /checkout, /orders, /profile: đã đăng nhập
- /admin/orders: staff, admin
- /admin/products, /admin/users: chỉ admin
**Hoạt động**: Nhóm lập ma trận cho toàn bộ route của web nhóm

---

## Slide 7: Lớp 1 – proxy.ts
**Nội dung chính**:
- Next.js 16: proxy.ts, hàm proxy (bản 15: middleware.ts)
- Chưa đăng nhập → /login?next=...
- Sai vai trò → trang 403
- Chỉ đọc vai trò trong JWT, không xác minh chữ ký

---

## Slide 8: Vì sao không chỉ dùng proxy?
**Nội dung chính**:
- CVE-2025-29927: một header bỏ qua toàn bộ middleware
- Ứng dụng chỉ dựa vào middleware bị mở toang
- proxy chỉ để chuyển hướng sớm, cho trải nghiệm
- Bảo vệ thật nằm ở server và API

---

## Slide 9: Lớp 2 – Data Access Layer
**Nội dung chính**:
```ts
export const getCurrentUser = cache(async () => {
  const token = await getAccessToken();
  const res = await fetch(`${API}/users/me`, { headers: { Authorization: `Bearer ${token}` } });
  return res.ok ? res.json() : null;
});
// trong trang/Server Action: await requireRole('admin');
```

---

## Slide 10: Lớp 3 – API
**Nội dung chính**:
- Token không đủ quyền → 403
- Khách xem đơn của người khác → 404
- Ba lớp, ba nhiệm vụ: trải nghiệm, trang, dữ liệu

---

## Slide 11: Làm mới token
**Nội dung chính**:
- access_token: cookie 14 phút (JWT 15 phút)
- refresh_token: 7 ngày
- Hết access → proxy gọi POST /auth/refresh, ghi cặp mới
- Refresh thất bại → về /login

---

## Slide 12: Gọi API kèm token và đăng xuất
**Nội dung chính**:
- apiAuth: chỉ chạy ở server, cache: 'no-store'
- Không cache dữ liệu riêng của từng người
- Đăng xuất: POST /auth/logout, xóa cookie, xóa giỏ (US-C13)

---

## Slide 13: Rủi ro bảo mật web
**Nội dung chính**:
- Kiểm soát truy cập hỏng (OWASP A01): gõ URL, đổi mã đơn
- XSS: React tự mã hóa, tránh dangerouslySetInnerHTML
- CSRF: SameSite + Server Action kiểm tra Origin
- Lộ bí mật: NEXT_PUBLIC_* gửi xuống trình duyệt

---

## Slide 14: CORS và open redirect
**Nội dung chính**:
- Next.js gọi API từ server: không cần mở CORS
- Không bật CORS * cho API có xác thực
- next=https://trang-gia.com → chỉ nhận đường dẫn bắt đầu bằng "/"

---

## Slide 15: Test case phân quyền (CLO2)
**Nội dung chính**:
- TC-21 chưa đăng nhập vào /admin/orders → /login?next=
- TC-22 customer vào /admin/orders → 403
- TC-24 token customer gọi PATCH /orders/12/status → API 403
- TC-26 document.cookie không thấy access_token
- TC-28 đăng xuất rồi Back → không vào lại được

---

## Slide 16: Thực hành
**Nội dung chính**:
- **Có hướng dẫn**: /login, cookie, proxy, DAL, header, đăng xuất, TC-21…28
- **Không hướng dẫn**: trang /profile + 4 tình huống truy cập trái phép
- **Nhóm**: ma trận phân quyền, xác thực ba lớp, test case mọi ô "✘"

---

## Slide 17: Tổng kết
**Nội dung chính**:
- Token trong cookie httpOnly, không trong localStorage
- Ba lớp kiểm tra: proxy, DAL, API
- Mỗi ô "✘" trong ma trận cần một test case
- Buổi sau: Server Actions, màn hình quầy, Checkpoint Sprint 2

---

## Slide 18: Tài liệu của buổi
**Đọc thêm**:
- SRS LHU Food: tiêu chí US-G05, C13, S01, A01; BR-03; mục 8 (/auth)
- Next.js: Authentication, proxy.js
- OWASP Top 10
**Ghi chú giảng viên**:
- Cho sinh viên kiểm tra phiên bản Next.js trước khi tạo proxy.ts hay middleware.ts.
