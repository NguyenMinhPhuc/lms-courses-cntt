# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 1: NỀN TẢNG & MÔ HÌNH HÓA GIAO DIỆN
### Bài 02: Tư duy Wireframe/Modeling UI & chuyển Figma thành Next.js Component

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Lớp học đảo ngược · **Chuẩn đầu ra:** PI 1.4 (CLO1), PI 2.3 (CLO2)
> **Dự án xuyên suốt:** Smart Event Hub – Mô hình hóa Wireframe 5 màn hình chính và chuyển hóa sang React Component bằng AI.

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Trình bày được quy tắc phân rã giao diện thành các khối Layout và năm cấp độ của Atomic Design (Atoms → Molecules → Organisms → Templates → Pages).
> * **[Bloom 3/4 - Kỹ năng]:** Phân tích một bản Wireframe thành cây DOM Semantic và cây component; dùng Vision AI (v0.dev, Claude, Cursor) sinh khung TSX/SCSS từ ảnh Wireframe.
> * **[Bloom 5/6 - Năng lực]:** Đánh giá và refactor code AI sinh ra (tách component, bỏ inline style, thay magic number bằng biến); cùng nhóm hoàn thiện bộ Wireframe 5 màn hình làm cơ sở cho PI 1.4.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Một bạn trong nhóm chụp ảnh màn hình Trang chủ của một website bán vé nổi tiếng, dán vào AI và nhận về 400 dòng TSX trong một file duy nhất. Trang chạy được, nhìn khá giống. Nhưng tuần sau, khi cần dùng lại khung tìm kiếm ở trang Danh sách sự kiện, cả nhóm không tách được, vì nút bấm, ô nhập và danh sách card dính chặt vào nhau, màu sắc thì viết thẳng `style={{ color: '#ff6600' }}` ở khắp nơi.

Câu hỏi đặt ra cho buổi học: **trước khi đưa ảnh cho AI, chúng ta cần "nhìn" giao diện như thế nào để code sinh ra có thể tái sử dụng?** Câu trả lời nằm ở tư duy Wireframe và mô hình hóa UI theo Atomic Design.

> 🧭 **Trước giờ học (Flipped Classroom):**
> * Xem video Nguyên tắc UX Wireframing và Cấu trúc UI Layout (Header, Content, Sidebar, Footer).
> * Đọc Atomic Design Methodology (Brad Frost) và tài liệu v0.dev ở mục 5.
> * Tạo tài khoản Figma (gói miễn phí) và v0.dev; làm Quiz nhanh 5–10 câu trên LMS.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Tư duy Wireframing: phân rã giao diện thành khối Layout

* **Khái niệm:** Wireframe là bản phác thảo trắng đen thể hiện **bố cục và thứ tự thông tin**, chưa quan tâm màu sắc hay hình ảnh thật. Mục tiêu là trả lời "cái gì nằm ở đâu" trước khi hỏi "trông nó ra sao".
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Quy tắc phân rã từ ngoài vào trong: **Header → Hero Section → Main Content → Sidebar → Footer**, sau đó mới chia nhỏ từng khối.
  * Mỗi khối Layout được ánh xạ sang một thẻ HTML Semantic: `<header>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`. Làm bước này **trước khi gõ code** giúp trang dễ đọc với trình đọc màn hình và tốt cho SEO.
  * Ghi chú lên Wireframe: tỉ lệ cột (70/30), phần tử cố định khi cuộn (sticky), hành vi trên mobile (cột phải xuống dưới).

```text
Wireframe "Chi tiết Sự kiện" → cây DOM Semantic
<header>                    Logo · Menu · Nút Đăng nhập
<main>
  <section> Hero            Banner 16:9 + Tiêu đề sự kiện
  <div> 2 cột
    <article> 70%           Thông tin BTC · Diễn giả · Nội dung chi tiết · Sơ đồ vé
    <aside> 30% (sticky)    Giá vé · Hạn đặt · Nút "Đặt vé ngay"
<footer>                    Bản quyền · Mạng xã hội
```

* **💡 Ví dụ thực tế (Real-world Example):**
  > Khi phân tích trang Chi tiết sự kiện, nhóm nhận ra khung đặt vé bên phải cũng xuất hiện ở trang Giỏ hàng. Ghi chú điều này ngay trên Wireframe giúp nhóm quyết định tách nó thành component `BookingSidebar` từ đầu, thay vì viết hai lần.

#### 2.2. Mô hình hóa UI theo Atomic Design

* **Khái niệm:** Atomic Design (Brad Frost) chia giao diện thành 5 cấp độ, từ nhỏ đến lớn. Cấp lớn được ghép từ cấp nhỏ hơn, giống nguyên tử ghép thành phân tử.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Atoms:** phần tử nhỏ nhất, không chia được nữa: `Button`, `Input`, `Badge`.
  * **Molecules:** nhóm atom có một chức năng: `SearchBar` = `Input` + `Button`; `EventCard`.
  * **Organisms:** khối giao diện hoàn chỉnh: `Header` = Logo + Nav + `SearchBar`; `EventGrid`.
  * **Templates:** khung bố cục trang, chưa có dữ liệu thật. **Pages:** template đổ dữ liệu cụ thể.
  * Lợi ích tái sử dụng: sửa `Button` một lần, mọi `SearchBar`, `Header`, `BookingSidebar` dùng nó đều được cập nhật.

```text
components/
  ├── ui/          (Atoms: Button.tsx, Badge.tsx, Input.tsx)
  ├── molecules/   (SearchBar.tsx, EventCard.tsx)
  └── organisms/   (Header.tsx, EventGrid.tsx, HeroBanner.tsx)
```

```tsx
// components/molecules/SearchBar.tsx – Molecule ghép từ 2 Atom
import Button from '@/components/ui/Button';
import Input from '@/components/ui/Input';
import styles from './SearchBar.module.scss';

interface SearchBarProps {
  placeholder?: string;
}

export default function SearchBar({ placeholder = 'Tìm sự kiện, nghệ sĩ, địa điểm...' }: SearchBarProps) {
  return (
    <form role="search" action="/events/search" className={styles.searchBar}>
      <Input name="q" placeholder={placeholder} aria-label="Từ khóa tìm kiếm" />
      <Button type="submit">Tìm kiếm</Button>
    </form>
  );
}
```

> **Gợi ý:** `Button` và `Input` nên nhận toàn bộ thuộc tính HTML gốc bằng cách mở rộng `ButtonHTMLAttributes<HTMLButtonElement>` và `InputHTMLAttributes<HTMLInputElement>`. Kỹ thuật này sẽ được trình bày kỹ ở Bài 04.

#### 2.3. Workflow chuyển Wireframe/Figma sang Next.js bằng Vision AI

* **Khái niệm:** Multimodal AI Prompting là gửi **ảnh** (Wireframe, ảnh chụp Figma, SVG export) kèm **văn bản mô tả** cho các mô hình có khả năng đọc hình như Claude, v0.dev hoặc Cursor để khởi tạo mã React TSX.
* **Chi tiết kỹ thuật / Quy trình 5 bước:**
  1. **Chuẩn bị ảnh:** export frame Figma (PNG 2x) hoặc copy SVG; chụp ảnh giấy phải rõ nét, thẳng góc.
  2. **Viết prompt có cấu trúc:** nêu vai trò, tên các component cần tách, công nghệ style, yêu cầu Semantic và Mock Data.
  3. **Sinh code:** v0.dev cho phép xem trước giao diện ngay; Cursor/Claude phù hợp khi muốn sinh thẳng vào dự án.
  4. **Đối chiếu:** đặt ảnh Wireframe cạnh trình duyệt, đánh giá độ giống (mục tiêu >85%).
  5. **Refactor:** tách component, đổi tên biến, thay inline style và magic number (mục 2.4).

* **💡 Ví dụ thực tế (Real-world Example):**
  > v0.dev thường sinh code bằng Tailwind và các component của shadcn/ui. Nếu nhóm đã chọn SCSS Module, hãy ghi rõ ràng buộc "chỉ dùng SCSS Module, không dùng Tailwind" trong prompt, nếu không các bạn sẽ mất thời gian chuyển đổi lại toàn bộ class.

#### 2.4. Clean-up code AI: bỏ inline style và magic number

* **Khái niệm:** Code AI sinh từ ảnh thường "đúng hình nhưng sai cấu trúc": một file quá dài, tên biến chung chung (`data`, `item1`), style viết trực tiếp, số đo cố định khắp nơi.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Chuyển `style={{ ... }}` sang class trong SCSS Module.
  * Thay magic number (`#ff6600`, `24px`, `1140px`) bằng biến trong `_variables.scss` của Bài 01.
  * Tách component khi file vượt khoảng 150 dòng hoặc có khối lặp lại.
  * Đổi tên theo nghiệp vụ: `data` → `featuredEvents`, `Box1` → `HeroBanner`.

```tsx
// ❌ Trước: code AI sinh ra
<div style={{ display: 'flex', gap: 24, background: '#ff6600', padding: '12px 32px' }}>
  <button style={{ color: '#fff' }}>Đặt vé ngay</button>
</div>

// ✅ Sau: dùng SCSS Module + biến dùng chung
<div className={styles.bookingBar}>
  <Button variant="primary">Đặt vé ngay</Button>
</div>
```

```scss
// BookingSidebar.module.scss – bố cục 70/30 với khung đặt vé sticky
@use '../../styles/variables' as *;
@use '../../styles/mixins' as *;

.layout {
  display: grid;
  grid-template-columns: 1fr;          // Mobile: khung đặt vé nằm dưới nội dung
  gap: $space-lg;
  @include respond-to('desktop') { grid-template-columns: 7fr 3fr; }
}

.sidebar {
  align-self: start;                   // cần thiết để sticky hoạt động trong grid
  @include respond-to('desktop') { position: sticky; top: 88px; } // chừa chiều cao Header
}
```

> **Lưu ý:** `position: sticky` sẽ không hoạt động nếu một phần tử cha có `overflow: hidden` hoặc nếu `aside` bị kéo giãn bằng chiều cao cột trái. Đây là lỗi AI hay mắc nhất khi sinh "Sticky Sidebar".

#### 2.5. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

Prompt dùng trong phần Guided (gửi kèm ảnh Wireframe Trang chủ):

```text
[Gửi kèm ảnh phác thảo Wireframe màn hình Trang chủ]
Bạn là một Senior UI/UX Developer. Hãy chuyển đổi hình ảnh Wireframe này thành React Component (Next.js App Router, TypeScript).

Yêu cầu chi tiết:
1. Hãy phân rã giao diện thành 3 Component nhỏ: HeroBanner, FeaturedEventsSection, CategoryFilter.
2. Sử dụng TailwindCSS hoặc SCSS Module để tái hiện lại chính xác bố cục lưới (Grid) như ảnh.
3. Tạo dữ liệu giả (Mock Data) bằng TypeScript với 4 phần tử mẫu.
4. Đảm bảo cấu trúc HTML chuẩn Semantic (<header>, <main>, <section>, <article>).
```

Prompt ngắn cho màn hình Chi tiết sự kiện (tài liệu lý thuyết):

```text
Tôi gửi kèm ảnh phác thảo Wireframe màn hình Chi tiết sự kiện. Hãy chuyển thành React Component
Next.js App Router sử dụng SCSS Module. Phân rã thành 2 cột: Cột trái (70%) chứa thông tin,
Cột phải (30%) là Sticky Sidebar đặt vé.
```

* **Checklist refactor code AI sinh từ hình ảnh:**
  * Đã tách đúng các component được yêu cầu, mỗi file một trách nhiệm?
  * Còn `style={{ }}` hoặc mã màu/kích thước cứng nào không?
  * Thẻ Semantic đúng chỗ (`<main>` chỉ một lần, card là `<article>`, khung phụ là `<aside>`)?
  * Mock Data có Interface (dùng lại `EventItem` trong `types/event.ts`), không có `any`?
  * Ảnh có `alt`, dùng `next/image`; bố cục co về 1 cột trên mobile?

#### 2.6. Thực hành trên lớp

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Guided Practice | 45 phút | GV phác thảo Figma "Trang chủ Danh sách Sự kiện"; SV đưa ảnh/SVG vào v0.dev hoặc Claude sinh code, sau đó refactor | File TSX giống >85% bản Figma, không còn inline style rác |
| Unguided Practice | 45 phút | Tự phác thảo màn hình "Chi tiết Sự kiện" và dùng Vibe Coding sinh `EventDetailPageView.tsx` | Bố cục hoàn chỉnh, khung đặt vé sticky khi cuộn |
| Team Challenge | 60 phút | Thống nhất Wireframe 5 màn hình chính, lưu vào `docs/wireframes/` | Bộ Wireframe 5 màn hình đầy đủ thành phần UI trên repo nhóm |
| Tổng kết | 15 phút | Nhận xét Wireframe các nhóm, giao BTVN | Danh sách chỉnh sửa cho từng nhóm |

**Guided (45'):** giảng viên vẽ mẫu Trang chủ trên Figma, hướng dẫn copy SVG hoặc chụp ảnh đưa vào AI bằng prompt mục 2.5. Sinh viên đọc hiểu code trả về, đổi tên biến, tách component nhỏ nếu code quá dài.

**Unguided (45'):** tự phác thảo (giấy hoặc phần mềm Wireframe) màn hình Chi tiết sự kiện gồm: ảnh banner lớn, thông tin Ban tổ chức, nội dung chi tiết, sơ đồ vé, khung đặt vé cố định. Sau đó dùng prompt gợi ý:

```text
Tôi có ý tưởng thiết kế Màn hình Chi tiết Sự kiện như sau:
- Cột bên trái (70%): Banner sự kiện (16:9), Tiêu đề lớn, Thông tin chi tiết diễn giả (Avatar, Tên, Bio), Bài viết mô tả nội dung.
- Cột bên phải (30%): Thẻ Sticky chứa Giá vé từ X đồng, Hạn đặt vé, Nút "Đặt vé ngay" màu cam nổi bật.

Hãy sinh mã nguồn Next.js TypeScript và SCSS/Tailwind cho màn hình này.
```

**Team Challenge (60'):** nhóm họp và thống nhất Wireframe hoàn chỉnh cho 5 màn hình: (1) Trang chủ – Home Page; (2) Danh sách & Lọc sự kiện – Event Listing; (3) Chi tiết sự kiện – Event Detail; (4) Giỏ hàng & Đặt vé – Checkout & Booking; (5) Trang quản lý cá nhân – Ticket History. Nhóm nào còn thời gian phác thảo thêm Admin Dashboard để chuẩn bị cho Bài 03. Xuất file thiết kế hoặc ảnh chụp rõ nét vào `docs/wireframes/` trên repo nhóm. Bộ Wireframe này là **cơ sở chấm tiêu chí "Mô hình hóa Wireframe UI" (1.5đ, PI 1.4)** ở Buổi 7 và Buổi 12.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)

* 🔹 **Wireframe trước, code sau:** phân rã Header → Hero → Main → Sidebar → Footer và ánh xạ sang thẻ Semantic.
* 🔹 **Atomic Design:** Atoms → Molecules → Organisms → Templates → Pages; cấp lớn ghép từ cấp nhỏ, tăng khả năng tái sử dụng.
* 🔹 **Vision AI chỉ sinh khung:** prompt phải nêu tên component cần tách, công nghệ style và Mock Data có kiểu.
* 🔹 **Refactor là bắt buộc:** bỏ inline style, thay magic number bằng biến, đổi tên theo nghiệp vụ.
* 🔹 **Sticky Sidebar:** cần `align-self: start` trong grid và không có cha `overflow: hidden`.

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Theo Atomic Design, component `SearchBar` gồm một `Input` và một `Button` thuộc cấp độ nào?
- A. Atom
- B. Molecule
- C. Organism
- D. Template

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Molecule là nhóm các Atom kết hợp để thực hiện một chức năng. <code>Header</code> chứa <code>SearchBar</code> mới là Organism.
</details>

**Câu 2:** Khối "Giá vé + Nút Đặt vé ngay" nằm ở cột phải trang Chi tiết sự kiện nên dùng thẻ Semantic nào?
- A. `<header>`
- B. `<footer>`
- C. `<aside>`
- D. `<nav>`

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> <code>&lt;aside&gt;</code> dành cho nội dung bổ trợ, nằm cạnh nội dung chính trong <code>&lt;article&gt;</code>.
</details>

**Câu 3:** AI sinh `style={{ background: '#ff6600', padding: 24 }}` lặp lại ở nhiều nơi. Cách refactor phù hợp nhất là gì?
- A. Giữ nguyên vì code vẫn chạy đúng
- B. Chuyển sang class SCSS Module và dùng biến trong `_variables.scss`
- C. Chuyển toàn bộ sang `!important` trong file CSS global
- D. Đổi mã màu sang dạng `rgb()` cho dễ đọc

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Inline style và magic number khiến code khó bảo trì. Class SCSS Module kết hợp Design Token giúp đổi giao diện tập trung.
</details>

**Câu 4:** Khung đặt vé có `position: sticky; top: 88px` nhưng không dính khi cuộn. Nguyên nhân nào có khả năng nhất?
- A. Thiếu thuộc tính `z-index`
- B. Dùng `next/image` trong trang
- C. Thẻ `<aside>` không hỗ trợ sticky
- D. Phần tử cha có `overflow: hidden` hoặc `aside` bị kéo giãn hết chiều cao cột

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> Sticky cần phần tử có khoảng trống để "trượt" trong cha và không bị cha cắt bởi <code>overflow</code>. Trong grid, thêm <code>align-self: start</code> cho <code>aside</code>.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-02-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)

* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Đăng ảnh Wireframe màn hình Chi tiết sự kiện của bạn kèm cây component Atomic Design tương ứng. Theo bạn, những phần nào trong code AI sinh ra phải refactor nhiều nhất và vì sao? Nếu được viết lại prompt, bạn sẽ thêm ràng buộc gì?
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Hoàn thiện 5 file Wireframe (Figma hoặc ảnh chụp) theo góp ý của giảng viên, lưu trong `docs/wireframes/`.
  * Chuyển toàn bộ 5 Wireframe thành trang giao diện mẫu tĩnh (Static Component) trong thư mục `app/dev-preview/` của dự án Next.js, tổ chức component theo `components/ui`, `components/molecules`, `components/organisms`.
  * **Output:** mọi thành viên truy cập được `/dev-preview/home`, `/dev-preview/listing`, `/dev-preview/detail`, `/dev-preview/checkout`, `/dev-preview/profile` để xem dàn trang tĩnh.
  * **Hạn nộp:** trước buổi học tiếp theo; mỗi thành viên mở Pull Request vào nhánh `dev`, nộp link PR lên LMS.
  * **Quy tắc đặt tên:** nhánh `feature/<ho-ten-khong-dau>-dev-preview`, ảnh wireframe `01-home.png` … `05-profile.png`.
* **📚 Tài liệu đọc & tham khảo:**
  * Atomic Design Methodology by Brad Frost: https://atomicdesign.bradfrost.com/
  * v0.dev Generative UI Documentation: https://v0.dev/docs
  * MDN – HTML elements reference (Semantic): https://developer.mozilla.org/en-US/docs/Web/HTML/Element
  * **Câu hỏi tự kiểm tra khi đọc:** Tại sao phân rã giao diện theo Atomic Design giúp tăng khả năng tái sử dụng code? Cần chú ý những điểm gì khi refactor JSX/TSX do AI sinh ra từ hình ảnh Wireframe?
