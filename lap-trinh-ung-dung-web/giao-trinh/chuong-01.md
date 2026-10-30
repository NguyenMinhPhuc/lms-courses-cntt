# Chương 1. Ứng dụng web hiện đại với Next.js và khởi động dự án

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- So sánh các mô hình render web: CSR, SSR, SSG/ISR và React Server Components.
- Giải thích vai trò của Next.js App Router và cấu trúc thư mục `app/`.
- Tạo dự án Next.js với TypeScript, Tailwind CSS và ESLint.
- Phân tích phạm vi web của LHU Food từ SRS và truy vết trang tới user story.
- Lập kế hoạch Sprint 1, tổ chức board công việc và viết file quy ước cho trợ lý AI.

## 1.1. Từ trang web đến ứng dụng web

### 1.1.1. Ứng dụng web khác trang web ở đâu

Một **trang web** chủ yếu trình bày nội dung: người đọc mở, đọc, chuyển trang. Một **ứng dụng web** cho phép người dùng làm việc: đăng nhập, thêm dữ liệu, thay đổi trạng thái, nhìn thấy dữ liệu của người khác cập nhật. Với LHU Food, cùng một hệ thống phải phục vụ ba kiểu người dùng rất khác nhau:

- **Khách** xem thực đơn: cần trang hiện nhanh trên điện thoại, được công cụ tìm kiếm tìm thấy.
- **Nhân viên căn tin** đứng ở quầy: cần danh sách đơn tự cập nhật, bấm một nút là đổi trạng thái.
- **Quản lý căn tin**: cần thêm món, xem báo cáo doanh thu, quản lý tài khoản nhân viên.

Không có một cách render nào tốt nhất cho cả ba. Đó là lý do học phần chọn một framework kết hợp được nhiều mô hình trong cùng một ứng dụng.

### 1.1.2. Các mô hình render

"Render" là quá trình biến dữ liệu và component thành HTML mà trình duyệt hiển thị. Câu hỏi quan trọng là HTML được tạo **ở đâu** và **khi nào** [1]:

| Mô hình | HTML được tạo ở đâu, khi nào | Ưu điểm | Hạn chế | Phù hợp trong LHU Food |
|---|---|---|---|---|
| CSR (Client-Side Rendering) | Trình duyệt tải JavaScript rồi mới vẽ giao diện | Tương tác mượt sau khi tải xong | Trang trắng lúc đầu; công cụ tìm kiếm khó đọc | Giỏ hàng, màn hình quầy |
| SSR (Server-Side Rendering) | Server tạo HTML cho từng request | Có dữ liệu mới nhất, hiện nội dung ngay | Mỗi request tốn tài nguyên server | Trang "Đơn của tôi" |
| SSG / ISR | Tạo sẵn HTML lúc build; ISR làm mới định kỳ | Rất nhanh, rẻ | Dữ liệu có thể cũ trong một khoảng thời gian | Thực đơn làm mới vài chục giây một lần |
| React Server Components | Component chạy trên server, chỉ gửi kết quả, không gửi mã | Ít JavaScript ở trình duyệt; đọc dữ liệu trực tiếp trên server | Không dùng được state, sự kiện | Mặc định cho mọi trang |

Ứng dụng React SPA bạn đã làm ở học phần Lập trình Frontend là CSR thuần: trình duyệt nhận một file HTML gần như rỗng và một gói JavaScript lớn. Next.js cho phép mỗi phần của trang chọn cách render phù hợp: trang thực đơn render trên server, còn nút "Thêm vào giỏ" là một "đảo" tương tác chạy ở trình duyệt.

### 1.1.3. React Server Components

React Server Components (RSC) là mô hình component mới của React, được Next.js App Router dùng làm mặc định [2]. Một **Server Component**:

- Chạy trên server (lúc build hoặc khi có request), có thể là hàm `async` và `await` dữ liệu.
- Đọc được biến môi trường bí mật, gọi API nội bộ mà trình duyệt không thấy.
- Chỉ gửi kết quả render xuống trình duyệt, không gửi mã của component.

Một **Client Component** bắt đầu bằng chỉ thị `"use client"`, dùng được `useState`, `useEffect`, sự kiện `onClick` và API trình duyệt. Mã của nó được gửi xuống trình duyệt. Quy tắc của học phần: trang để là Server Component, chỉ tách phần nhỏ cần tương tác thành Client Component. Chương 3 và Chương 4 phân tích ranh giới này kỹ hơn.

## 1.2. Next.js App Router

### 1.2.1. Tạo dự án

Next.js yêu cầu Node.js bản LTS. Tạo dự án bằng công cụ chính thức [3]:

```bash
npx create-next-app@latest lhu-food-web --ts --tailwind --eslint --app --import-alias "@/*"
cd lhu-food-web
npm run dev          # mở http://localhost:3000
npx next --version   # ghi phiên bản vào README của nhóm
```

Các tùy chọn: `--ts` dùng TypeScript, `--tailwind` cài sẵn Tailwind CSS, `--eslint` kiểm tra mã, `--app` dùng App Router, `--import-alias "@/*"` cho phép viết `import ... from '@/lib/api'` thay cho đường dẫn tương đối dài.

### 1.2.2. Điều hướng theo thư mục

App Router dùng **cấu trúc thư mục app/ làm bản đồ đường dẫn** [4]:

- Mỗi thư mục là một đoạn đường dẫn (segment).
- File `page.tsx` trong thư mục là trang hiển thị tại đường dẫn đó.
- File `layout.tsx` bọc mọi trang con, giữ nguyên khi chuyển giữa các trang con.

```text
app/
├── layout.tsx        bố cục gốc (thẻ <html>, <body>)
├── page.tsx          /
├── menu/
│   └── page.tsx      /menu
└── admin/
    └── page.tsx      /admin
```

```tsx
// app/page.tsx: Server Component (mặc định), chạy trên server
export default function HomePage() {
  return (
    <main className="mx-auto max-w-4xl p-6">
      <h1 className="text-3xl font-bold text-blue-900">LHU Food</h1>
      <p className="mt-2 text-slate-600">Đặt món căn tin, nhận món không cần xếp hàng.</p>
    </main>
  );
}
```

```tsx
// app/layout.tsx: bố cục gốc, bắt buộc có <html> và <body>
import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = { title: 'LHU Food', description: 'Đặt món căn tin Đại học Lạc Hồng' };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <body className="bg-slate-50 text-slate-900">{children}</body>
    </html>
  );
}
```

Đặt `lang="vi"` để trình đọc màn hình đọc đúng tiếng Việt (Chương 10). `metadata` là tiêu đề và mô tả của trang, dùng cho tab trình duyệt và công cụ tìm kiếm.

### 1.2.3. App Router và Pages Router

Next.js có hai bộ định tuyến: **Pages Router** (thư mục `pages/`, hàm `getServerSideProps`, `getStaticProps`) là cách cũ; **App Router** (thư mục `app/`) là cách hiện tại, hỗ trợ Server Components [4]. Học phần chỉ dùng App Router. Rất nhiều ví dụ trên mạng và mã do AI sinh vẫn dùng Pages Router; trộn hai kiểu trong một dự án gây lỗi khó hiểu.

### 1.2.4. Next.js thay đổi theo phiên bản

Next.js phát hành phiên bản lớn khá thường xuyên. Một số thay đổi ảnh hưởng trực tiếp tới mã trong giáo trình:

- Từ Next.js 15, `params` và `searchParams` của trang là `Promise`, phải `await` trước khi dùng (Chương 2).
- Từ Next.js 15, `fetch` không tự cache; muốn cache phải khai báo (Chương 3).
- Từ Next.js 16, file `middleware.ts` đổi tên thành `proxy.ts` (Chương 5).

Luôn ghi phiên bản Next.js của nhóm vào README và đọc tài liệu đúng phiên bản trên nextjs.org.

## 1.3. Phân tích phạm vi web của LHU Food

### 1.3.1. Kiến trúc tổng thể

SRS mục 2.3 mô tả kiến trúc chung của LHU Food. Phần web nằm ở vị trí sau:

```text
Trình duyệt ──▶ Next.js (lhu-food-web) ──HTTP──▶ API (NestJS) ──▶ SQL Server
                Server/Client Components          chỉ gọi stored procedure
                KHÔNG kết nối CSDL trực tiếp
App di động ──────────────────────────────────▶ cùng API
```

Next.js là một **client của API**, giống ứng dụng di động. Việc giữ Next.js không kết nối CSDL có ba lý do: mọi quy tắc nghiệp vụ nằm một chỗ (stored procedure), web và mobile luôn nhất quán, và tài khoản CSDL không bao giờ nằm trong mã frontend.

### 1.3.2. Phân vai giữa web và mobile

SRS mục 2.4 và mục 10.2 phân vai: các story đánh dấu **W** chỉ làm trên web, **M+W** làm trên cả hai. Từ đó, phạm vi web của học phần:

| Khu vực web | Actor | User story (SRS mục 4) | Mức |
|---|---|---|---|
| Trang quản trị | Quản lý căn tin | US-A01…A07: danh mục, món, quầy, nhân viên, báo cáo, tình trạng hệ thống | Bắt buộc |
| Màn hình quầy | Nhân viên | US-S02, S03, S05, S06, S07: đơn mới realtime, đổi trạng thái, tồn kho, lọc, hủy có lý do | Bắt buộc |
| Web đặt món | Khách vãng lai, khách hàng | US-G01…G05, C01, C02, C04, C06, C07, C08, C13 | Cơ bản |

### 1.3.3. Truy vết trang tới user story

Phân tích phạm vi là bước đầu tiên của CLO1. Mỗi trang nhóm làm ra phải trả lời được câu hỏi: *trang này phục vụ user story nào?* Một trang không truy vết được tới story nào là phần việc ngoài phạm vi; một story không có trang nào là phần việc còn thiếu. Bảng truy vết đơn giản ở Sprint 1:

| Trang dự kiến | User story | Actor | Sprint |
|---|---|---|---|
| `/menu` | US-G01, US-G02 | Khách vãng lai | 1 |
| `/product/[id]` | US-G03 | Khách vãng lai | 1 |
| `/admin/products` | US-A02 | Quản lý | 3 |
| `/admin/orders` | US-S02, US-S03 | Nhân viên | 2 |

Chương 2 mở rộng bảng này thành bảng ánh xạ route – chức năng – vai trò – API.

### 1.3.4. Backend theo từng sprint

- **Sprint 1–2:** nhóm dùng **API mẫu** do giảng viên cung cấp. Địa chỉ API và tài khoản thử được thông báo trên Moodle; tài liệu Swagger ở đường dẫn `/docs`. Nhờ vậy nhóm tập trung vào phần web mà không phải chờ backend.
- **Sprint 3–4:** nhóm tự xây **module quản trị** trên backend của nhóm. Học phần khuyến khích dùng chung backend NestJS với đồ án di động, nhưng không bắt buộc. Backend khác vẫn phải gọi stored procedure và có Swagger.

## 1.4. Lập kế hoạch dự án

### 1.4.1. Product Backlog dùng chung

Tài liệu *Kế hoạch Agile & Product Backlog* của LHU Food liệt kê các Epic và user story, mỗi story có tiêu chí chấp nhận dạng Given–When–Then, story point theo dãy Fibonacci (1, 2, 3, 5, 8, 13) và mức ưu tiên MoSCoW (Must, Should, Could, Won't). Nhóm không viết backlog từ đầu mà **chọn các story web** từ backlog dùng chung, rồi bổ sung story riêng nếu làm đề tài khác.

### 1.4.2. Kế hoạch Sprint 1 (CLO4)

Sắp xếp công việc là một chuẩn đầu ra của học phần. Các bước lập kế hoạch sprint:

1. **Đặt Sprint Goal:** một câu mô tả giá trị đạt được cuối sprint. Ví dụ Sprint 1: "Khách xem được thực đơn thật từ API trên điện thoại và máy tính; khung trang quản trị sẵn sàng".
2. **Chọn story:** ưu tiên story Must, tổng story point vừa với năng lực của nhóm. Sprint đầu chưa có số liệu, nên cam kết thận trọng.
3. **Chia việc:** mỗi story tách thành các thẻ nhỏ (giao diện, gọi API, test case), mỗi thẻ làm được trong một đến hai ngày.
4. **Đưa lên board:** GitHub Projects hoặc Jira với các cột *Cần làm → Đang làm → Chờ review → Xong*. Mỗi thẻ có người phụ trách và liên kết tới Pull Request.

### 1.4.3. Phân vai và quy trình Git

Nhóm 4–5 sinh viên phân vai theo khu vực (web khách, quản trị, màn hình quầy, kiểm thử và tài liệu), nhưng mọi thành viên đều phải viết mã và giải thích được phần mình làm. Quy trình làm việc:

- Mỗi tính năng một nhánh (`feature/menu-page`), commit nhỏ, thông điệp rõ ràng.
- Mở Pull Request, ít nhất một thành viên khác review trước khi merge.
- Không commit `.env.local`, mật khẩu, token.

## 1.5. Vibe coding với Next.js

### 1.5.1. File quy ước cho trợ lý AI

Trợ lý AI sinh mã tốt hơn nhiều khi biết quy ước của dự án. Đặt file `AGENTS.md` ở gốc dự án (chép sang `.github/copilot-instructions.md` cho GitHub Copilot):

```markdown
# LHU Food Web - Quy ước dự án

## Công nghệ
- Next.js App Router (thư mục app/), TypeScript, Tailwind CSS + shadcn/ui.
- KHÔNG dùng Pages Router, KHÔNG kết nối SQL Server; dữ liệu lấy qua API (biến API_URL).

## Quy ước
- Server Component mặc định; chỉ thêm "use client" khi cần state hoặc sự kiện.
- Gọi API tập trung trong lib/api.ts; kiểu dữ liệu trong lib/types.ts.
- Chuỗi hiển thị tiếng Việt có dấu; không thêm thư viện khi nhóm chưa đồng ý.
```

### 1.5.2. Lỗi AI hay mắc với Next.js

- Sinh mã Pages Router (`getServerSideProps`, thư mục `pages/`) trong dự án App Router.
- Dùng `useState` hoặc `onClick` trong Server Component, gây lỗi lúc build.
- Thêm `"use client"` tràn lan để "chữa" lỗi, làm mất lợi ích của Server Component.
- Gọi thẳng CSDL từ Next.js bằng thư viện ORM, vi phạm kiến trúc của học phần.

Mỗi đoạn mã AI sinh phải được bạn đọc, chạy thử và giải thích được. Prompt chính ghi vào `PROMPTS.md` kèm ghi chú bạn đã sửa gì. Nguyên tắc chung của học phần: **không hiểu thì không merge**.

## Tóm tắt chương

- CSR, SSR, SSG/ISR và Server Components khác nhau ở nơi và thời điểm tạo HTML; Next.js kết hợp được tất cả trong một ứng dụng.
- App Router: thư mục là đường dẫn, `page.tsx` là trang, `layout.tsx` bọc trang con; Server Component là mặc định.
- Next.js là client của API; không kết nối CSDL trực tiếp.
- Phạm vi web: trang quản trị và màn hình quầy (bắt buộc), web đặt món (cơ bản); mỗi trang truy vết tới một user story.
- Kế hoạch sprint: Sprint Goal, chọn story theo năng lực, chia thẻ nhỏ, theo dõi trên board.

## Câu hỏi ôn tập

1. Vì sao một ứng dụng React SPA thuần (CSR) không phù hợp cho trang thực đơn cần được tìm thấy trên công cụ tìm kiếm?
2. Phân biệt Server Component và Client Component theo ba tiêu chí: chạy ở đâu, dùng được gì, gửi gì xuống trình duyệt.
3. File `app/admin/orders/page.tsx` hiển thị ở đường dẫn nào?
4. Nêu ba lý do học phần không cho Next.js kết nối SQL Server trực tiếp.
5. Story US-S07 đánh dấu nền tảng **W**. Điều đó có ý nghĩa gì với nhóm làm web?
6. Một Sprint Goal tốt khác một danh sách công việc ở điểm nào?

## Bài tập

1. **Khảo sát mô hình render.** Với mỗi trang trong bảng mục 1.3.3, chọn mô hình render phù hợp và giải thích trong 2–3 câu.
2. **Truy vết phạm vi.** Đọc SRS mục 4.4 và 4.5, lập bảng truy vết đầy đủ các trang cho actor Nhân viên và Quản lý.
3. **Kế hoạch Sprint 1.** Viết Sprint Goal, chọn story, ước lượng story point và đưa lên board của nhóm.

## Tài liệu tham khảo

[1] Vercel, “Server and Client Components,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/server-and-client-components

[2] Meta Open Source, “Server Components,” *React Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react.dev/reference/rsc/server-components

[3] Vercel, “Installation,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/installation

[4] Vercel, “Project Structure,” *Next.js Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://nextjs.org/docs/app/getting-started/project-structure
