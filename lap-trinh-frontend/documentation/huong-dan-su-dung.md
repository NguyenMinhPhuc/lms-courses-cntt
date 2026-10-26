# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## HƯỚNG DẪN SỬ DỤNG BỘ HỌC LIỆU (User Guide)

> **Đơn vị:** Khoa Công nghệ Thông tin – Trường Đại học Lạc Hồng (LHU) · **Hệ thống LMS:** `https://learn.lhu.edu.vn`
> **Mã học phần:** Đang cập nhật · **Số tín chỉ:** Đang cập nhật · **Giảng viên:** Đang cập nhật
> **Thời lượng:** 60 tiết = 12 buổi × 5 tiết (225 phút) · 30% lý thuyết – 70% thực hành & đánh giá · **Mô hình:** Lớp học đảo ngược

---

Tài liệu này dành cho hai nhóm người đọc. **Sinh viên** đọc mục 1, 2 và 6 để biết học liệu nằm ở đâu và mỗi tuần cần làm gì. **Giảng viên và người quản trị khóa học** đọc thêm mục 3, 4, 5 (đưa nội dung lên Moodle, nhập quiz, cấu hình nhóm lớp) và mục 7, 8 (hướng dẫn Vibe Coding, tùy biến Ant Design).

---

## 1. TỔNG QUAN BỘ HỌC LIỆU

#### Học phần này dạy gì

Chúng ta xây dựng một sản phẩm thật xuyên suốt 12 buổi: **Smart Event Hub** – hệ thống đặt vé và quản lý sự kiện trực tuyến, dùng RESTful API Backend (Swagger) có sẵn do giảng viên cung cấp. Mỗi buổi thêm một lớp kỹ năng: SCSS & TypeScript → Wireframe → App Router → Dynamic Routing → Ant Design → Hooks → (giữa kỳ) → API → Form & Storage → Refactor → Deploy → (Hackathon cuối kỳ).

| Thành phần đánh giá | Trọng số | Thời điểm |
|---|---|---|
| Quá trình (quiz trước giờ, bài tập, BTVN, diễn đàn, chuyên cần) | 30% | Buổi 1–11 |
| Giữa kỳ – Báo cáo tiến độ 50% dự án | 30% | Buổi 7 |
| Cuối kỳ – Hackathon & Final Showcase | 40% | Buổi 12 |

Điểm cuối kỳ cá nhân = Điểm đồ án nhóm × 0.7 + Điểm phản biện cá nhân × 0.3.

#### Chuẩn đầu ra học phần

| CLO | PI | Mô tả |
|---|---|---|
| CLO1 | PI 1.4 | Phân tích yêu cầu, mô hình hóa UI/Wireframe và tổ chức kiến trúc component cho ứng dụng web |
| CLO2 | PI 2.3 | Xây dựng ứng dụng Front-End với Next.js, TypeScript, SCSS/Ant Design, quản lý state, kết nối REST API, sử dụng AI (Vibe Coding) có kiểm soát |
| CLO3 | PI 3.1 | Viết báo cáo kỹ thuật và thuyết trình/demo sản phẩm rõ ràng, chuyên nghiệp |
| CLO4 | PI 5.1 | Làm việc nhóm với Git (branch, PR, review), triển khai CI/CD lên Vercel và tối ưu SEO/Performance |

---

## 2. CẤU TRÚC THƯ MỤC `lap-trinh-frontend/`

#### Cây thư mục

```text
lap-trinh-frontend/
├── index.html                     # Landing page tổng hợp toàn bộ học phần
├── thong-tin-hoc-phan.md / .html  # Đề cương tóm tắt: mục tiêu, CLO, lịch 12 buổi, đánh giá
├── danh-gia-hoc-phan.md / .html   # Chuyên đề đánh giá: cơ cấu điểm, rubric giữa kỳ & cuối kỳ
├── bai-01.md / bai-01.html        # Bài 01 … Bài 12 (bản .md là nguồn, .html build tự động)
├── ...
├── bai-12.md / bai-12.html
├── Moodle_HTML/                         # Đoạn HTML 4 Accordion (inline style) để dán thẳng vào Moodle
│   ├── 00_Thong_tin_hoc_phan.html
│   ├── 01_SCSS_TypeScript_Vibe_Coding.html … 12_Hackathon_Final_Showcase.html
│   └── 13_Danh_gia_hoc_phan.html
├── quiz/
│   └── quiz-bai-01-aiken.txt …    # Ngân hàng câu hỏi Aiken, ≥10 câu/bài
├── discussion/
│   └── thao-luan-va-hoat-dong-nhom.md   # Chủ đề diễn đàn + Team Challenge 12 bài, quy trình Git/PR
├── assignment/
│   └── bai-tap-va-nhiem-vu.md           # Guided, Unguided, BTVN, mốc nộp, deliverable giữa/cuối kỳ
├── resources/
│   └── tai-nguyen-hoc-tap.md            # Readings, docs chính thức, công cụ, thư viện prompt, video
├── assessment/                          # Rubric, công cụ đánh giá và phản hồi
├── documentation/
│   ├── huong-dan-su-dung.md             # Tài liệu này
│   └── dac-ta-du-an-smart-event-hub.md  # Đặc tả dự án xuyên suốt
└── noi-dung-mon-hoc/                    # Tài liệu gốc (.docx): đề cương, lý thuyết, kế hoạch buổi, rubric
```

#### Mỗi thành phần dùng để làm gì

| Thành phần | Người dùng chính | Đưa lên LMS dưới dạng |
|---|---|---|
| `Moodle_HTML/XX_*.html` | Sinh viên | **Page** (dán vào chế độ mã nguồn HTML) |
| `bai-XX.html` | Sinh viên | Xem trực tiếp trên trình duyệt / landing page |
| `quiz/quiz-bai-XX-aiken.txt` | Giảng viên | **Question bank** → **Quiz** trước giờ học |
| `discussion/…` | SV + GV | **Forum** mỗi bài (chép câu hỏi mở vào mô tả diễn đàn) |
| `assignment/…` | SV + GV | **Assignment** mỗi BTVN; deliverable giữa kỳ/cuối kỳ |
| `resources/…` | Sinh viên | **Page** hoặc **URL** trong phần "Tài nguyên chung" |
| `Moodle_HTML/00_…`, `Moodle_HTML/13_…` (đề cương, đánh giá) | SV + GV | **Page** ở đầu khóa học |
| `documentation/dac-ta-du-an-smart-event-hub.md` | SV + GV | **Page** hoặc file đính kèm ở phần Dự án |

> 📝 File `.md` là bản nguồn để chỉnh sửa. File `bai-XX.html` và các file trong `Moodle_HTML/` được sinh tự động từ `.md` (bằng `marked`), vì vậy khi cần sửa nội dung, hãy sửa file `.md` rồi build lại, không sửa tay file `.html`.

---

## 3. ĐƯA BÀI HỌC LÊN MOODLE

### 3.1. Chọn Page hay Label

#### Quy ước sử dụng

* **Page (Trang):** dùng cho nội dung dài – mỗi bài học `Moodle_HTML/XX_*.html`, trang tài nguyên, đặc tả dự án. Sinh viên bấm vào để mở thành một trang riêng.
* **Label / Text and media area:** dùng cho đoạn ngắn hiển thị ngay trên trang khóa học – lời dẫn của từng tuần, nhắc hạn nộp, link nhanh tới repo mẫu.

Gợi ý bố trí mỗi section (tuần) trên Moodle theo đúng mô hình lớp học đảo ngược:

1. Label: "Tuần X – Bài XX: <tên bài>" và 2–3 dòng việc cần làm trước giờ.
2. Page: nội dung bài học `Moodle_HTML/XX_*.html`.
3. Quiz: quiz trước giờ học (5–10 câu).
4. Forum: chủ đề thảo luận của bài.
5. Assignment: BTVN của bài.

### 3.2. Dán nội dung HTML

#### Các bước

1. Bật **Edit mode** trong khóa học, tại section của tuần chọn **Add an activity or resource → Page**.
2. Đặt **Name** theo mẫu `Bài 01 – SCSS nâng cao, TypeScript căn bản & thiết lập Vibe Coding`.
3. Mở file `Moodle_HTML/01_SCSS_TypeScript_Vibe_Coding.html` bằng VS Code và sao chép **toàn bộ** nội dung. File này chỉ gồm 4 khối Accordion với inline style (không có `<html>`, `<head>`, class hay script) nên dán vào là hiển thị đúng.
4. Ở ô **Page content**, chuyển trình soạn thảo sang chế độ mã nguồn: với TinyMCE chọn **Tools → Source code**; với Atto bấm nút **HTML** (`</>`).
5. Dán nội dung, chuyển về chế độ hiển thị thường để xem trước, rồi **Save and display**.

> ⚠️ **Kiểm tra sau khi lưu:** mở bằng tài khoản vai trò sinh viên (hoặc *Switch role to… Student*) để xem phần đáp án `<details>` có còn đóng/mở được không, code block có giữ định dạng không. Nếu bộ lọc HTML của LMS loại bỏ thẻ `<details>`, liên hệ quản trị LMS để kiểm tra cấu hình, hoặc tải file `.html` lên dạng resource **File** để sinh viên mở trực tiếp.

* Ảnh (logo, ảnh minh họa) cần được tải lên qua nút chèn ảnh của trình soạn thảo, không dùng đường dẫn file trên máy cá nhân.
* Link giữa các file trong bộ học liệu (ví dụ `assignment/bai-tap-va-nhiem-vu.md`) cần được thay bằng link tới Page/Assignment tương ứng trên Moodle.

---

## 4. NHẬP QUIZ AIKEN VÀO QUESTION BANK

### 4.1. Import câu hỏi

#### Các bước

1. Trong khóa học, vào **More → Question bank** (Moodle 4.x) và tạo trước các **Category**: `Quiz Bài 01`, `Quiz Bài 02`, … `Quiz Bài 12`.
2. Chọn **Import**, tại **File format** chọn **Aiken format**.
3. Ở mục **General**, chọn category đích (ví dụ `Quiz Bài 01`).
4. Kéo thả file `quiz/quiz-bai-01-aiken.txt` (UTF-8) vào ô tải lên, bấm **Import**, kiểm tra danh sách câu hỏi Moodle hiển thị rồi bấm **Continue**.
5. Lặp lại cho các bài còn lại.

Mỗi câu Aiken gồm 1 dòng câu hỏi, 4 dòng phương án `A.`–`D.` và dòng `ANSWER: X`. Nếu Moodle báo lỗi ở một câu, hãy mở file bằng VS Code, kiểm tra câu đó có bị xuống dòng giữa chừng hoặc thiếu dòng trống ngăn cách không.

### 4.2. Tạo Quiz trước giờ học

#### Cấu hình gợi ý

| Thiết lập | Giá trị gợi ý |
|---|---|
| Câu hỏi | **Add → a random question** từ category của bài, 5–10 câu |
| Thời gian làm bài | 10–15 phút |
| Số lần làm | 1–2 lần, lấy điểm cao nhất |
| Thứ tự phương án | Shuffle within questions = Yes |
| Review options | Hiện đáp án đúng sau khi quiz đóng |
| Mở/đóng | Đặt theo lịch từng lớp bằng **Group overrides** (mục 5) |

Bộ câu hỏi đầy đủ (≥10 câu/bài) còn dùng được cho ôn tập giữa kỳ, cuối kỳ: tạo một quiz luyện tập lấy ngẫu nhiên từ nhiều category.

---

## 5. CẤU HÌNH NHÓM LỚP (MULTI-CLASS MANAGEMENT)

### 5.1. Một khóa học dùng cho nhiều lớp

#### Separate groups và Group overrides

Khi một khóa học LMS dùng chung cho nhiều lớp học phần, cấu hình như sau:

1. **Tạo Group theo lớp:** *Participants → Groups*, mỗi lớp học phần là một group (đặt đúng mã lớp). Có thể dùng **Auto-create groups** hoặc import danh sách.
2. **Chế độ nhóm riêng biệt:** trong *Settings* của khóa học, chọn **Group mode = Separate groups** và **Force group mode = Yes**. Sinh viên chỉ thấy bài nộp, diễn đàn và thành viên thuộc lớp của mình.
3. **Lịch và hạn nộp theo lớp (Group overrides):** tại mỗi Quiz hoặc Assignment, chọn **Overrides → Group overrides** và đặt thời gian mở/đóng, hạn nộp theo đúng lịch học của từng lớp. Ví dụ lớp học sáng thứ Hai thì quiz đóng trước 7h sáng thứ Hai, lớp học chiều thứ Năm thì đóng trước giờ học chiều thứ Năm.
4. **Quy tắc đặt tên file nộp:** `[MãLớp]_[Nhóm/MSSV]_[TênBài]`, ví dụ `24CT111_Nhom02_BaoCaoGiuaKy.pdf` (mã lớp chỉ là ví dụ).
5. **Lọc sổ điểm:** trong **Grades**, dùng dropdown chọn group để chấm và xuất Excel điểm riêng cho từng lớp.

### 5.2. Nhóm dự án 3–4 sinh viên

#### Grouping cho nhóm dự án

Nhóm dự án khác với nhóm lớp. Gợi ý tổ chức:

* Tạo các group dự án đặt tên `24CT111_Nhom01`, `24CT111_Nhom02`… và gom vào một **Grouping** riêng, ví dụ `Nhom-du-an-24CT111`.
* Với Assignment nộp theo nhóm (Wireframe, slide, báo cáo giữa kỳ/cuối kỳ, Test Cases): bật **Group submission settings → Students submit in groups = Yes** và chọn **Grouping for student groups** là grouping dự án. Một bạn nộp, cả nhóm cùng nhận trạng thái đã nộp.
* Với BTVN cá nhân (link PR): để Students submit in groups = No.
* Điểm phản biện cá nhân cuối kỳ (30%) nhập riêng cho từng sinh viên bằng một grade item thủ công.

---

## 6. LỘ TRÌNH HỌC TẬP THEO TUẦN (DÀNH CHO SINH VIÊN)

#### Nhịp mỗi tuần

* **Trước giờ (khoảng 1–1,5 giờ):** đọc readings của buổi trong `resources/`, xem video/slide GV đăng, làm quiz LMS.
* **Trên lớp (225 phút):** Lý thuyết & demo 60' → Guided 45' → Unguided 45' → Team Challenge 60' → Tổng kết 15'.
* **Sau giờ:** làm BTVN cá nhân, mở PR vào `dev`, đăng bài và phản hồi trên diễn đàn trước buổi sau.

#### Lịch 12 tuần

| Tuần | Bài | Trước giờ | Trọng tâm trên lớp | Sau giờ (nộp trước buổi sau) |
|---|---|---|---|---|
| 1 | 01 | Cài VS Code, Node.js LTS, Git, Cursor/Copilot; đọc Sass, TS Handbook | EventCard, HeaderNavigationBar, repo nhóm + Design Token | PR: Footer, EventCategoryBadge, SearchBar |
| 2 | 02 | Atomic Design, v0.dev docs | Wireframe → TSX; Wireframe 5 màn hình | Wireframe hoàn chỉnh + `/dev-preview/*` |
| 3 | 03 | Next.js Routing, Server Components | Layout chung, `(auth)`, `(admin)`, trang 404 | `error.tsx`, `global-error.tsx`, Skeleton |
| 4 | 04 | Dynamic Routes, Props patterns | `/events/[id]`, `/category/[slug]`, Button, Mock JSON | Tổ chức `components/ui`, `common`, `features` |
| 5 | 05 | Ant Design docs, AntD + Next.js | Theme `ConfigProvider`, BookingModal, `/admin/orders` | Responsive toàn bộ component AntD |
| 6 | 06 | React Hooks, You Might Not Need an Effect | TicketQuantitySelector, EventFilterBar, SeatMatrixPicker | Tích hợp 50% + slide giữa kỳ |
| 7 | 07 | Conventional Commits, Production Checklist | **Báo cáo giữa kỳ (30%)** | Sửa theo góp ý; đọc Swagger API |
| 8 | 08 | Next.js Data Fetching, Axios | `getEvents`, `getEventById`, categories, `POST /api/orders` | Xử lý Network Error / 500 |
| 9 | 09 | React Hook Form, Zod | LoginForm, `/admin/create-event`, Wishlist | Tài khoản Vercel + kết nối repo |
| 10 | 10 | Refactoring Guru, Responsive basics | PBL 1: Responsive, Refactor, Zero Warning | Test Cases Scenario |
| 11 | 11 | Metadata, Lighthouse | PBL 2: SEO, Deploy Vercel, Lighthouse > 85 | Báo cáo Word/PDF + slide cuối kỳ |
| 12 | 12 | Ôn rubric Hackathon | **Hackathon & Final Showcase (40%)** | Bài phản tư trên diễn đàn |

> 🧭 **Tự kiểm tra cuối mỗi tuần:** (1) Quiz đã làm chưa? (2) PR BTVN đã mở và có reviewer chưa? (3) Mình giải thích được từng dòng code mình commit tuần này chưa? Nếu câu (3) là "chưa", hãy dành 20 phút đọc lại và hỏi AI "giải thích đoạn này" trước buổi học.

---

## 7. HƯỚNG DẪN CHO GIẢNG VIÊN VỀ VIBE CODING

### 7.1. Nguyên tắc: AI không làm thay

#### Sinh viên là Architect, AI sinh khung

Đề cương xác định rõ: giảng viên hướng dẫn sinh viên đặt prompt ở vị trí người thiết kế (Architect), yêu cầu AI tạo khung và TypeScript interface trước. Sinh viên **bắt buộc phải review, hiểu và sửa lỗi (debug)** code do AI sinh ra, không copy-paste thụ động.

Prompt mẫu đề cương cung cấp cho sinh viên:

```text
Hãy tạo cho tôi 1 Component Next.js App Router bằng TypeScript sử dụng Ant Design v5 Card để hiển thị thông tin sự kiện gồm: tên, ngày, giá vé, nút đặt vé. Đảm bảo có Interface rõ ràng.
```

Khi demo trên lớp (phần lý thuyết 60'), nên làm trọn một vòng: viết prompt theo khung Context → Requirement → Constraints, nhận code, **cố ý chỉ ra lỗi** trong code AI (kiểu sai, `any`, thiếu `await params`, import sai phiên bản), sửa trước mặt sinh viên và giải thích lý do.

### 7.2. Cách kiểm soát việc dùng AI

#### Các biện pháp áp dụng trong học phần

* **Mục "Phần có dùng AI" trong mỗi PR:** công cụ, prompt chính, những gì đã sửa so với code AI. Mẫu PR có trong `discussion/thao-luan-va-hoat-dong-nhom.md`.
* **Phản biện cá nhân:** ở giữa kỳ (5 phút/nhóm) và cuối kỳ (Q&A), chọn ngẫu nhiên một file trong Git log của sinh viên và yêu cầu giải thích hoặc sửa nhỏ tại chỗ (đổi một prop, thêm một trường validation).
* **Lỗi cố ý trong bài tập:** Guided Practice Buổi 1 yêu cầu sửa type mismatch do AI gợi ý sai. Có thể chuẩn bị sẵn một đoạn code AI sinh có lỗi để cả lớp cùng tìm.
* **Dấu hiệu copy-paste thụ động:** commit một lần rất lớn, style code lệch hẳn phần còn lại của dự án, còn comment kiểu "Here is your component", dùng API của phiên bản cũ (Ant Design v4, Pages Router), sinh viên không trả lời được câu hỏi về chính file mình commit.

> 💡 **Điểm thưởng Vibe Coding (+0.5 đến +1.0 vào điểm quá trình)** theo rubric Hackathon: Vibe Coding Master, UI Innovation, Ultra Performance (Lighthouse 100/100). Nên công bố từ Buổi 1 để sinh viên có động lực xây prompt workflow riêng.

---

## 8. TÙY BIẾN ANT DESIGN THEME (TRÁNH THIẾT KẾ RẬP KHUÔN)

### 8.1. Design Token với `ConfigProvider`

#### Cấu hình đúng cú pháp

Đề cương hướng dẫn dùng `ConfigProvider` kết hợp SCSS Module để mỗi nhóm có nhận diện riêng. Lưu ý bản trích xuất của đề cương có lỗi gõ `token: {{ ... }}`; cú pháp đúng là `theme={{ token: { ... } }}` (ngoặc kép ngoài là cú pháp JSX, bên trong là một object).

Cách chắc chắn nhất là tách provider thành một Client Component rồi bọc trong Root Layout:

```tsx
// components/providers/AntdProvider.tsx
'use client';

import { ConfigProvider } from 'antd';
import type { ThemeConfig } from 'antd';
import type { ReactNode } from 'react';

const theme: ThemeConfig = {
  token: {
    colorPrimary: '#6366f1',
    borderRadius: 8,
  },
  components: {
    Button: { controlHeight: 40 },
  },
};

export default function AntdProvider({ children }: { children: ReactNode }) {
  return <ConfigProvider theme={theme}>{children}</ConfigProvider>;
}
```

```tsx
// app/layout.tsx
import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import { AntdRegistry } from '@ant-design/nextjs-registry';
import AntdProvider from '@/components/providers/AntdProvider';
import './globals.scss';

export const metadata: Metadata = {
  title: 'Smart Event Hub',
  description: 'Hệ thống đặt vé và quản lý sự kiện trực tuyến',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="vi">
      <body>
        <AntdRegistry>
          <AntdProvider>{children}</AntdProvider>
        </AntdRegistry>
      </body>
    </html>
  );
}
```

`AntdRegistry` (gói `@ant-design/nextjs-registry`) trích CSS ở phía server, tránh hiện tượng giao diện nháy không có style (FOUC) và lỗi Hydration mismatch.

### 8.2. Override bằng SCSS Module

#### Ghi đè cục bộ, không ảnh hưởng toàn cục

Sau khi đổi token, các nhóm tạo điểm nhấn bằng SCSS Module. Đặt class của mình làm "phạm vi" rồi dùng `:global()` để chạm tới class nội bộ của Ant Design, nhờ vậy chỉ component đó bị ảnh hưởng.

```scss
// components/features/BookingModal.module.scss
@use '../../styles/variables' as *;

.bookingModal {
  :global(.ant-modal-content) {
    border-radius: 16px;
    padding: 24px;
  }

  :global(.ant-modal-title) {
    font-weight: 700;
  }

  :global(.ant-btn-primary) {
    box-shadow: none;
  }
}
```

```tsx
// components/features/BookingModal.tsx (trích)
import styles from './BookingModal.module.scss';

<Modal className={styles.bookingModal} open={open} onCancel={onClose} title="Đặt vé">
  {/* Form đặt vé */}
</Modal>
```

> 🎨 **Gợi ý cho GV khi chấm tiêu chí "Giao diện & Vibe Coding":** mức Xuất sắc yêu cầu tùy biến Theme có dấu ấn riêng; mức Trung bình là giao diện nguyên bản của thư viện UI, chưa tùy biến. Có thể yêu cầu mỗi nhóm trình bày file theme và 2–3 chỗ override SCSS khi demo.
