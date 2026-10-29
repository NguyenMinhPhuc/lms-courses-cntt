# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## ASSESSMENT – RUBRIC KIỂM TRA GIỮA KỲ (BUỔI 7)

> **Hình thức:** Báo cáo đồ án nhóm – tiến độ 50% dự án Smart Event Hub · **Trọng số:** 30% điểm học phần
> **Chuẩn đầu ra:** PI 1.4 (CLO1), PI 2.3 (CLO2), PI 5.1 (CLO4) · **Thời lượng mỗi nhóm:** 10 phút thuyết trình & demo + 5 phút phản biện cá nhân

---

### 1. Nội dung được đánh giá

Đến Buổi 7, Smart Event Hub đã có bản vẽ, bộ khung điều hướng và giao diện tĩnh, nhưng chưa nối API. Câu hỏi giảng viên đặt ra khi chấm rất đơn giản: **nếu ngày mai nhóm bắt đầu ghép Backend, nền móng hiện tại có đủ chắc không?**

Nhóm cần trình diễn:

* Wireframe 5 màn hình chính: Trang chủ, Chi tiết sự kiện, Đặt vé, Trang cá nhân, Admin Dashboard.
* Giao diện web thực tế: Ant Design + SCSS Custom, responsive Mobile/Desktop.
* Luồng điều hướng (Routing) mượt giữa các trang, gồm dynamic route `/events/[id]`, `/category/[slug]`.
* Minh chứng Git commit log của từng cá nhân.

---

### 2. Bảng rubric chi tiết (tổng 5.0 điểm)

Nguồn đề cương quy định 4 tiêu chí với điểm tối đa: Wireframe **1.5đ**, UI chuyên nghiệp **2.0đ**, Routing & Component Architecture **1.0đ**, Git Commit & Phối hợp nhóm **0.5đ**. Các mức mô tả dưới đây dùng cùng thang phần trăm với Rubric Hackathon để sinh viên dễ đối chiếu.

| Tiêu chí | Xuất sắc (85–100%) | Khá (70–84%) | Trung bình (55–69%) | Yếu (< 55%) |
|---|---|---|---|---|
| **1. Wireframe đủ 5 màn hình & cấu trúc chuẩn** (Max 1.5đ · CLO1) | **1.3–1.5đ** – Figma đủ 5 màn hình; vùng Header/Content/Sidebar/Footer rõ; có chú thích tên component; giao diện đã code khớp bản vẽ. | **1.05–1.25đ** – Đủ 5 màn hình, bố cục rõ; vài chi tiết chưa thống nhất với giao diện đã code. | **0.85–1.0đ** – Thiếu 1–2 màn hình hoặc vẽ tay sơ sài; chưa thể hiện cấu trúc layout. | **0–0.8đ** – Không có Wireframe hoặc bản vẽ không thể hiện bố cục cơ bản. |
| **2. UI chuyên nghiệp (AntD/Bootstrap + Responsive + Hot Reload)** (Max 2.0đ · CLO2) | **1.7–2.0đ** – Theme tùy biến qua ConfigProvider/SCSS Module có nhận diện riêng; responsive Mobile và Desktop; Hot Reload mượt, Console sạch; `npm run build` thành công. | **1.4–1.65đ** – Dùng thư viện UI đúng cách, theme cơ bản; còn lỗi nhỏ ở một kích thước màn hình hoặc vài warning vàng. | **1.1–1.35đ** – Giao diện mặc định của thư viện, chưa tùy biến; tràn ngang trên di động; còn hydration error. | **0–1.0đ** – Chưa áp dụng thư viện UI/SCSS; vỡ layout nặng; build thất bại. |
| **3. Routing & Component Architecture** (Max 1.0đ · CLO2) | **0.85–1.0đ** – App Router đúng chuẩn (layout, nested, dynamic route); có `not-found.tsx`, `loading.tsx`; component tách vào `/components/ui`, `/components/shared`; props có interface. | **0.7–0.8đ** – Điều hướng đủ các màn hình chính; vài component lặp code hoặc props thiếu type. | **0.55–0.65đ** – Routing chạy nhưng thư mục lộn xộn, ít component tái sử dụng. | **0–0.5đ** – Thiếu nhiều route; dùng thẻ `<a>` gây reload trang; code dồn vào một file. |
| **4. Git Commit & Phối hợp nhóm** (Max 0.5đ · CLO4 · **chấm cá nhân**) | **0.45–0.5đ** – Commit đều qua các buổi, đúng Conventional Commits, làm qua branch + PR; giải thích trôi chảy code mình đảm nhiệm. | **0.35–0.4đ** – Có commit riêng ở phần mình phụ trách; message chưa đều chuẩn; trả lời đúng phần lớn câu hỏi. | **0.3đ** – Ít commit, dồn sát buổi báo cáo; giải thích code còn lúng túng. | **0–0.25đ** – Không có commit cá nhân hoặc không giải thích được code mang tên mình. |

#### 2.1. Quy đổi điểm

```text
Điểm Giữa kỳ (thang 10) = (TC1 + TC2 + TC3 + TC4) × 2
```

* Tiêu chí 1–3 chấm chung cho nhóm. Tiêu chí 4 chấm riêng từng sinh viên dựa trên Git log và 5 phút phản biện.
* **Ví dụ:** Nhóm đạt TC1 = 1.25, TC2 = 1.6, TC3 = 0.8; bạn B đạt TC4 = 0.45 → (1.25 + 1.6 + 0.8 + 0.45) × 2 = **8.2**.
* Trường hợp một sinh viên không giải thích được phần code mình đảm nhiệm ở tiêu chí 2 hoặc 3, giảng viên có thể hạ một mức ở tiêu chí đó **riêng cho sinh viên này** và ghi rõ lý do trong phiếu chấm.

> ⚠️ **Lưu ý:** Dự án không chạy được `npm run build` tại thời điểm chấm thì tiêu chí 2 tối đa ở mức Trung bình. Đây là lý do 45 phút Guided của Buổi 7 dành riêng cho việc build thử và sửa lỗi TypeScript/ESLint.

---

### 3. Checklist hồ sơ nộp (hạn 23:59 ngày trước Buổi 7)

Trưởng nhóm nộp file `[MãLớp]_[NhomXX]_GiuaKy.pdf` lên LMS (ví dụ `24CT111_Nhom03_GiuaKy.pdf`), trong đó có đủ các mục sau:

* [ ] Link Figma Wireframe 5 màn hình (đã bật quyền xem cho giảng viên).
* [ ] Link GitHub repository, gắn tag `v0.5-midterm` ở commit nộp bài.
* [ ] `README.md` tại thư mục gốc: mô tả dự án (3–4 câu), bảng phân công (Họ tên, MSSV, Vai trò, Tính năng đảm nhiệm), hướng dẫn `npm install` / `npm run dev`, cấu trúc thư mục App Router, link Figma.
* [ ] Mục **Nhật ký Vibe Coding** trong README: 3–5 prompt chính đã dùng và phần code nhóm phải sửa lại.
* [ ] `npm run lint` và `npm run build` chạy thành công (chụp màn hình terminal đính kèm).
* [ ] Console trên DevTools không còn lỗi đỏ; đã xử lý hydration mismatch (ví dụ DatePicker/Modal của Ant Design).
* [ ] Commit message theo Conventional Commits, ví dụ `feat(event): implement seat matrix selection logic`, `fix(ui): repair responsive layout on mobile`.
* [ ] Link Preview/Demo giao diện (nếu đã có) và slide báo cáo 5–7 trang.

---

### 4. Phiếu chấm mẫu – Giữa kỳ

**Lớp:** ............ **Nhóm:** ............ **Tên dự án:** Smart Event Hub · **Giảng viên chấm:** ............ **Ngày:** ............

#### 4.1. Phần chấm nhóm (Tiêu chí 1–3)

| Tiêu chí | Điểm tối đa | Mức đạt (XS/K/TB/Y) | Điểm | Nhận xét / Minh chứng |
|---|---|---|---|---|
| 1. Wireframe 5 màn hình & cấu trúc | 1.5 | | | |
| 2. UI chuyên nghiệp, Responsive, Hot Reload | 2.0 | | | |
| 3. Routing & Component Architecture | 1.0 | | | |
| **Cộng điểm nhóm (TC1–3)** | **4.5** | | | |

**Kiểm tra kỹ thuật nhanh:**

| Hạng mục | Đạt | Chưa đạt | Ghi chú |
|---|---|---|---|
| `npm run build` thành công | ☐ | ☐ | |
| Console không lỗi đỏ khi demo | ☐ | ☐ | |
| Responsive 375px (Mobile) | ☐ | ☐ | |
| Responsive 1440px (Desktop) | ☐ | ☐ | |
| README đủ 5 mục + Nhật ký Vibe Coding | ☐ | ☐ | |

#### 4.2. Phần chấm cá nhân (Tiêu chí 4) & tổng điểm

| STT | Họ tên | MSSV | Số commit | Phần đảm nhiệm | Câu hỏi phản biện đã hỏi | TC4 (/0.5) | Điểm GK (/10) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |

#### 4.3. Góp ý cho nhóm trước Buổi 8

1. ..............................................................................
2. ..............................................................................
3. ..............................................................................

> Nhóm chuyển mỗi góp ý thành một GitHub Issue có nhãn `midterm-feedback` và đóng Issue bằng commit sửa lỗi trước Buổi 8.

---

### 5. Gợi ý câu hỏi phản biện cá nhân (5 phút/nhóm)

Giảng viên chọn 1–2 câu cho mỗi sinh viên, gắn với file mà sinh viên đó đã commit:

* "Mở file component em phụ trách. Interface props này có những trường nào bắt buộc, trường nào tùy chọn, vì sao?"
* "Vì sao trang này cần `'use client'`? Nếu bỏ đi thì lỗi gì xảy ra?"
* "Route `/events/[id]` lấy `id` ở đâu? Trong Next.js 15 vì sao phải `await params`?"
* "Đoạn SCSS này override class nào của Ant Design? Có cách nào làm qua `ConfigProvider` thay vì override không?"
* "Prompt nào em đã dùng để sinh đoạn code này, và em đã sửa gì sau khi AI trả kết quả?"

---

### ❓ Tự kiểm tra trước buổi báo cáo

**Câu hỏi:** Dự án của nhóm chạy `npm run dev` bình thường nhưng `npm run build` báo lỗi type. Theo rubric, điều gì xảy ra nếu nhóm demo trong tình trạng này?

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án:</b> Tiêu chí 2 (UI chuyên nghiệp) tối đa ở mức Trung bình (1.1–1.35đ).<br>
<b>Giải thích:</b> Chế độ dev không chạy toàn bộ type checker và ESLint như khi build production. Lỗi build đồng nghĩa với việc sản phẩm chưa thể triển khai, nên rubric giới hạn mức điểm. Hãy chạy <code>npm run lint</code> và <code>npm run build</code> ít nhất một ngày trước buổi báo cáo.
</details>
