# Chương 9. Màn hình quầy thời gian thực với Socket.IO

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- So sánh làm mới định kỳ (polling) và kết nối thời gian thực cho màn hình quầy.
- Tích hợp Socket.IO vào Client Component của Next.js với xác thực bằng access token.
- Xử lý kết nối lại, token hết hạn và làm mới dữ liệu sau khi mất kết nối.
- Phân tích luồng realtime giữa web, mobile và backend bằng sơ đồ tuần tự.
- Kiểm thử realtime với nhiều phiên; báo cáo Sprint 3 và điều chỉnh kế hoạch Sprint 4.

## 9.1. Từ làm mới định kỳ đến thời gian thực

### 9.1.1. Giới hạn của polling

Ở Chương 6, màn hình quầy gọi `router.refresh()` 15 giây một lần. Cách này gọi là **polling**: đơn giản nhưng có hai nhược điểm. Đơn mới có thể chờ tới 15 giây mới hiện, giờ cao điểm là đủ để sinh viên đứng chờ trước quầy. Và mỗi màn hình đang mở gọi API liên tục dù không có gì thay đổi.

### 9.1.2. Socket.IO

Chương 9 giáo trình di động đã giới thiệu Socket.IO: một thư viện xây trên WebSocket, giữ một kết nối hai chiều giữa client và server, có sự kiện có tên, **room**, tự kết nối lại và gửi kèm thông tin xác thực khi bắt tay [1]. Backend của LHU Food đã có sẵn:

- Mỗi kết nối gửi access token trong `auth` khi bắt tay; token sai hoặc hết hạn thì bị từ chối (US-SYS01).
- Kết nối hợp lệ được đưa vào room `user:<id>`; nhân viên (và quản lý) vào thêm room `staff`.
- Khi có đơn mới, backend phát `order:new` vào room `staff`; khi đổi trạng thái, phát `order:status` vào room của khách và `order:updated` vào room `staff`.

### 9.1.3. Hai quy tắc giữ nguyên trên web

1. **Socket chỉ để báo tin.** Mọi thao tác ghi (đổi trạng thái, hủy đơn) vẫn đi qua REST API và stored procedure như Chương 6, có xác thực và kiểm tra quyền.
2. **Lưu trước, gửi sau.** Backend lưu dữ liệu vào SQL Server rồi mới phát sự kiện. Màn hình mất kết nối vẫn lấy lại đủ dữ liệu từ API khi kết nối lại.

## 9.2. Socket.IO trong Next.js

### 9.2.1. Những điểm khác so với ứng dụng di động

- Kết nối socket sống trong trình duyệt, nên chỉ tạo trong **Client Component**, bên trong `useEffect`, và đóng ở hàm dọn dẹp khi component bị gỡ [2].
- Access token nằm trong cookie `httpOnly` (Chương 5), JavaScript không đọc được. Client xin token qua một Route Handler cùng tên miền. Token chỉ được giữ trong bộ nhớ của kết nối, không ghi vào `localStorage`.
- Khi server từ chối kết nối (lỗi `connect_error` do middleware xác thực), client Socket.IO **không tự kết nối lại** [3]. Ứng dụng phải xin token mới rồi gọi `socket.connect()`.
- Socket kết nối thẳng từ trình duyệt tới backend, khác với REST (Next.js gọi từ server). Vì vậy địa chỉ socket là biến `NEXT_PUBLIC_` và backend phải mở CORS cho địa chỉ web.

### 9.2.2. Route Handler cấp token cho socket

```ts
// app/api/socket-token/route.ts: trả access token hiện tại cho kết nối socket
import { getCurrentUser } from '@/lib/dal';
import { getAccessToken } from '@/lib/session';

export async function GET() {
  const user = await getCurrentUser();                       // backend xác minh token
  if (!user || (user.role !== 'staff' && user.role !== 'admin')) return Response.json({}, { status: 401 });
  return Response.json({ token: await getAccessToken() }, { headers: { 'Cache-Control': 'no-store' } });
}
// Thêm '/api/socket-token' vào matcher của proxy.ts để access token hết hạn được làm mới trước khi tới đây
```

Cách này đưa access token (sống 15 phút) vào bộ nhớ trình duyệt trong thời gian kết nối. Đó là một đánh đổi có ý thức: token chỉ cấp cho nhân viên đã đăng nhập, không được lưu lại, và hết hạn nhanh. Cách an toàn hơn là backend cấp một "vé kết nối" chỉ sống vài chục giây và chỉ dùng được cho socket; nhóm có thể làm ở phần mở rộng.

```text
# .env.local: địa chỉ socket không phải bí mật nên được dùng NEXT_PUBLIC_
NEXT_PUBLIC_SOCKET_URL=http://<địa-chỉ-backend-nhóm>:3000
```

Cài `socket.io-client` cùng phiên bản chính với server (v4): `npm install socket.io-client`.

## 9.3. Màn hình quầy realtime

### 9.3.1. Socket là chuông báo

Danh sách đơn vẫn do Server Component lấy từ `GET /orders/staff` (Chương 6). Client Component dưới đây chỉ lắng nghe sự kiện, và khi có tin thì gọi `router.refresh()` để Server Component lấy lại danh sách. Dữ liệu luôn đến từ API; socket chỉ là "chuông báo". Cách này chậm hơn một chút so với chèn thẳng dữ liệu trong sự kiện, nhưng đảm bảo chỉ có một nguồn sự thật và không lệch dữ liệu khi lỡ sự kiện.

```tsx
// app/admin/orders/orders-realtime.tsx
'use client';
import { useEffect, useRef, useState } from 'react';
import { useRouter } from 'next/navigation';
import { io } from 'socket.io-client';

type Conn = 'connecting' | 'online' | 'offline';
const LABEL: Record<Conn, string> = { connecting: 'Đang kết nối…', online: 'Đang nhận đơn trực tiếp', offline: 'Mất kết nối, đang thử lại…' };

export function OrdersRealtime() {
  const router = useRouter();
  const [conn, setConn] = useState<Conn>('connecting');
  const [lastOrder, setLastOrder] = useState<number | null>(null);
  const soundOn = useRef(false);

// … (trích 15/60 dòng; mã đầy đủ ở Phụ lục A, mục A.6)
```

### 9.3.2. Phân tích các quyết định

- **Tùy chọn auth dạng hàm:** Socket.IO gọi hàm này ở mỗi lần bắt tay, kể cả khi kết nối lại; nhờ đó token luôn mới dù màn hình mở cả ca làm việc [3].
- **Làm mới khi kết nối:** trong lúc mất kết nối có thể có đơn mới; lấy lại danh sách từ API khi kết nối lại thì không lỡ đơn nào.
- **Chỉ dùng WebSocket (transports):** bỏ bước long-polling ban đầu, tránh lỗi khi đi qua một số proxy.
- **Âm báo cần người dùng bấm trước:** trình duyệt chặn phát âm thanh khi người dùng chưa tương tác với trang [4], nên có nút "Bật âm báo" ở đầu ca.
- **Trạng thái kết nối bằng chữ, có aria-live:** nhân viên biết khi nào màn hình không còn "trực tiếp"; trình đọc màn hình đọc thông báo khi trạng thái đổi.
- **React Strict Mode** chạy `useEffect` hai lần khi phát triển: thấy kết nối rồi ngắt ngay một lần là bình thường, nhờ hàm dọn dẹp `socket.disconnect()`.

Đặt `<OrdersRealtime />` ở đầu trang `/admin/orders` và bỏ bộ hẹn giờ 15 giây của Chương 6.

### 9.3.3. Backend nhóm cần bổ sung

Nếu backend nhóm làm theo Chương 9 giáo trình di động, cần thêm:

- Gateway đưa cả `admin` vào room `staff` (giáo trình di động chỉ có `staff`).
- Phát `toStaff('order:updated', { orderId, status })` sau khi đổi trạng thái hoặc hủy đơn, để các màn hình quầy khác đồng bộ.
- Cấu hình CORS của Socket.IO cho phép địa chỉ web (ví dụ `http://localhost:3001` khi phát triển).

API mẫu của giảng viên đã làm sẵn ba việc này; nhóm có thể đối chiếu.

## 9.4. Sơ đồ tuần tự

### 9.4.1. Vì sao cần sơ đồ tuần tự

Luồng realtime đi qua nhiều thành phần (app di động, API, SQL Server, nhiều trình duyệt) và hai kênh (REST và socket). **Sơ đồ tuần tự** (sequence diagram) của UML thể hiện ai gửi thông điệp cho ai, theo thứ tự thời gian, qua kênh nào [5]. Đây là phần phân tích bắt buộc của Checkpoint 3 (CLO1, tiêu chí 1.7 của rubric).

### 9.4.2. Luồng đặt món và xử lý

```text
App khách (mobile)    API (NestJS)        SQL Server       Web quầy (2 nhân viên)
     │ POST /orders ───────▶│                    │                     │
     │                      │ sp_Order_Create ──▶│ (giao dịch, trừ kho) │
     │                      │◀── đơn #12 ────────│                     │
     │◀── 201 {orderId:12} ─│                    │                     │
     │                      │── order:new (room staff) ───────────────▶│ ting! router.refresh()
     │                      │◀──────────── GET /orders/staff ──────────│
     │                      │                    │                     │
     │                      │◀─── PATCH /orders/12/status (preparing) ─│ nhân viên A
     │                      │ sp_Order_UpdateStatus ▶ sp_Notification_Create
     │◀ order:status (room user:3)               │                     │
     │                      │── order:updated (room staff) ───────────▶│ màn hình B tự cập nhật
```

Trong báo cáo, vẽ lại bằng công cụ vẽ sơ đồ (draw.io, PlantUML hoặc Mermaid), đánh số hình và chú thích từng thông điệp. Vẽ thêm một sơ đồ cho tình huống lỗi: hai nhân viên cùng bấm một đơn, người sau nhận 409 (Chương 6).

## 9.5. Kiểm thử realtime và báo cáo Sprint 3

### 9.5.1. Chuẩn bị

Realtime không kiểm được bằng một trình duyệt. Chuẩn bị: hai cửa sổ web (một thường, một ẩn danh) đăng nhập hai tài khoản staff, một điện thoại chạy ứng dụng di động của nhóm đăng nhập customer. Web và app trỏ tới cùng backend.

### 9.5.2. Test case realtime (CLO2)

| Mã | Tình huống | Kết quả mong đợi |
|---|---|---|
| TC-51 | Khách đặt món trên điện thoại (US-S02) | Cả hai cửa sổ quầy hiện đơn trong khoảng 2 giây, có âm báo nếu đã bật |
| TC-52 | Nhân viên A bấm "Bắt đầu làm" (US-S03) | Cửa sổ B chuyển đơn sang "Đang chuẩn bị" không cần tải lại; điện thoại khách nhận thông báo |
| TC-53 | Tắt mạng cửa sổ A 30 giây (DevTools → Offline), trong lúc đó khách đặt một đơn, rồi bật lại | A hiện "Mất kết nối", khi có mạng tự kết nối lại và hiện đơn đã lỡ |
| TC-54 | Để màn hình quầy mở quá 15 phút (token hết hạn), rồi khởi động lại backend | Kết nối lại thành công bằng token mới, không phải đăng nhập lại |
| TC-55 | Kết nối socket bằng token customer (script nhỏ dùng `socket.io-client`) | Không nhận sự kiện `order:new` của room staff |
| TC-56 | Kết nối socket không có token hoặc token sửa một ký tự | Bị từ chối (`connect_error`), không vào room nào |

TC-55 và TC-56 kiểm tra yêu cầu bảo mật US-SYS01 ở tầng socket, tương tự TC-24 kiểm tra REST ở Chương 5.

### 9.5.3. Báo cáo Sprint 3 (CLO3)

Theo cấu trúc 6 mục của các báo cáo sprint trước, bổ sung: phân tích module quản trị (bảng năm tầng, Chương 7), ERD phần quản trị, danh mục stored procedure, sơ đồ tuần tự realtime, kết quả hồi quy khi chuyển sang backend nhóm, test case quản trị và realtime.

### 9.5.4. Điều chỉnh kế hoạch Sprint 4 (CLO4)

Sprint 4 là sprint cuối: kiểm thử tự động (Chương 10), triển khai lên server Khoa và báo cáo đồ án (Chương 11), Demo Day chung với học phần di động (Chương 12). Khi lập kế hoạch:

- Cập nhật bảng velocity ba sprint; cam kết Sprint 4 không vượt trung bình velocity.
- Đưa các story Could chưa làm ra khỏi phạm vi phát hành nếu không đủ năng lực; ghi rõ lý do trong báo cáo.
- Dành thời gian cho sửa lỗi, triển khai (thường phát sinh lỗi không có trên máy phát triển) và viết báo cáo.
- Cập nhật bản nháp báo cáo vai trò cá nhân với phần việc Sprint 3.

## Tóm tắt chương

- Polling đơn giản nhưng chậm và tốn tài nguyên; Socket.IO cho đơn mới hiện ngay.
- Socket chỉ báo tin, dữ liệu luôn lấy lại từ API; thao tác ghi vẫn qua REST và stored procedure.
- Trên web: socket chỉ trong Client Component, token xin qua Route Handler, `auth` dạng hàm, tự kết nối lại khi bị từ chối, làm mới dữ liệu khi kết nối lại.
- Sơ đồ tuần tự thể hiện luồng realtime giữa web, mobile và backend.
- Kiểm thử realtime cần nhiều phiên: nhiều tab, mất mạng, token hết hạn, token sai.

## Câu hỏi ôn tập

1. Nêu hai nhược điểm của polling 15 giây cho màn hình quầy.
2. Vì sao màn hình quầy gọi lại API khi nhận `order:new` thay vì chèn thẳng dữ liệu trong sự kiện?
3. Vì sao Client Component không đọc được access token, và bài này giải quyết thế nào?
4. Tùy chọn `auth` dạng hàm giải quyết vấn đề gì?
5. Khi server từ chối kết nối, client Socket.IO có tự kết nối lại không? Mã trong bài xử lý thế nào?
6. Vì sao cần nút "Bật âm báo"?
7. Sơ đồ tuần tự khác sơ đồ chức năng ở điểm nào?

## Bài tập

1. **Dashboard tự cập nhật.** Trang `/admin` có 4 thẻ số đơn theo trạng thái trong ngày, tự cập nhật khi có `order:new` hoặc `order:updated`.
2. **Sơ đồ lỗi.** Vẽ sơ đồ tuần tự cho tình huống hai nhân viên cùng bấm một đơn.
3. **Script kiểm thử socket.** Viết script Node.js nhỏ dùng `socket.io-client` để thực hiện TC-55 và TC-56, in kết quả ra màn hình.

## Tài liệu tham khảo

[1] Socket.IO, “Introduction,” *Socket.IO Documentation (v4)*. Accessed: Oct. 30, 2026. [Online]. Available: https://socket.io/docs/v4/

[2] Socket.IO, “How to use with Next.js,” *Socket.IO Documentation (v4)*. Accessed: Oct. 30, 2026. [Online]. Available: https://socket.io/how-to/use-with-nextjs

[3] Socket.IO, “Client options,” *Socket.IO Documentation (v4)*. Accessed: Oct. 30, 2026. [Online]. Available: https://socket.io/docs/v4/client-options/

[4] MDN Web Docs, “Autoplay guide for media and Web Audio APIs,” *MDN Web Docs*. Accessed: Oct. 30, 2026. [Online]. Available: https://developer.mozilla.org/docs/Web/Media/Guides/Autoplay

[5] Object Management Group, “Unified Modeling Language (UML) Specification, Version 2.5.1,” Dec. 2017. Accessed: Oct. 30, 2026. [Online]. Available: https://www.omg.org/spec/UML/2.5.1
