<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 09 - Màn hình quầy thời gian thực với Socket.IO (5 tiết: 1 LT / 4 TH) · Checkpoint Sprint 3</strong></p>
        <p><em>Màn hình quầy đang tự tải lại 15 giây một lần. Giờ cao điểm, 15 giây là đủ để ba sinh viên đứng chờ trước quầy mà nhân viên chưa thấy đơn. Hôm nay đơn đặt từ điện thoại hiện lên màn hình quầy trong chưa đầy một giây, kèm tiếng "ting". Hai nhân viên đứng hai đầu quầy luôn thấy cùng một danh sách.</em></p>
        <p><strong>Mục tiêu:</strong> Tích hợp được Socket.IO vào Client Component có xác thực; xử lý được kết nối lại và token hết hạn; phân tích được luồng realtime giữa web, mobile và backend bằng sơ đồ tuần tự; kiểm thử được realtime với nhiều phiên; báo cáo được kết quả Sprint 3 và điều chỉnh kế hoạch Sprint 4.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Socket.IO trong Next.js:</strong> chỉ chạy ở Client Component, lấy token kết nối từ server, kết nối lại.</li>
            <li><strong>Ý chính 2 - Màn hình quầy realtime:</strong> <code>order:new</code> kèm âm báo, <code>order:updated</code> đồng bộ nhiều nhân viên, làm mới dữ liệu khi kết nối lại.</li>
            <li><strong>Ý chính 3 - Sơ đồ tuần tự:</strong> luồng realtime web và mobile trên cùng backend.</li>
            <li><strong>Ý chính 4 - Kiểm thử realtime và báo cáo Sprint 3:</strong> nhiều tab, mất mạng, token hết hạn; kế hoạch Sprint 4.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Màn hình quầy nhận đơn mới ngay lập tức (US-S02) và đồng bộ trạng thái giữa các nhân viên (US-S03); nhóm demo được web và mobile cùng chạy trên backend nhóm và hoàn thành Checkpoint Sprint 3.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2, CLO3, CLO4.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Socket.IO trong Next.js</h3>
            <p>Hai quy tắc của Chương 9 giáo trình di động vẫn giữ nguyên trên web: <strong>socket chỉ để báo tin</strong> (mọi thao tác ghi vẫn qua REST API và stored procedure), và <strong>lưu trước, gửi sau</strong>. Điểm khác trên web:</p>
            <ul>
                <li>Kết nối socket sống trong trình duyệt, nên chỉ tạo trong <strong>Client Component</strong>, trong <code>useEffect</code>, và đóng khi component bị gỡ.</li>
                <li>Access token nằm trong cookie <code>httpOnly</code> (bài 05), JavaScript không đọc được. Client xin token qua một Route Handler cùng tên miền. Token chỉ được giữ trong bộ nhớ của kết nối, không ghi vào <code>localStorage</code>.</li>
                <li>Server từ chối kết nối khi token sai hoặc hết hạn (lỗi <code>connect_error</code>), và trong trường hợp này client <strong>không tự kết nối lại</strong>. Phải xin token mới rồi gọi <code>socket.connect()</code>.</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/api/socket-token/route.ts: trả access token hiện tại cho kết nối socket
import { getCurrentUser } from '@/lib/dal';
import { getAccessToken } from '@/lib/session';

export async function GET() {
  const user = await getCurrentUser();                       // backend xác minh token
  if (!user || (user.role !== 'staff' &amp;&amp; user.role !== 'admin')) return Response.json({}, { status: 401 });
  return Response.json({ token: await getAccessToken() }, { headers: { 'Cache-Control': 'no-store' } });
}
// Thêm '/api/socket-token' vào matcher của proxy.ts để access token hết hạn được làm mới trước khi tới đây</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># .env.local: địa chỉ socket không phải bí mật nên được dùng NEXT_PUBLIC_
NEXT_PUBLIC_SOCKET_URL=http://&lt;địa-chỉ-backend-nhóm&gt;:3000

npm install socket.io-client      # cùng phiên bản chính với server (v4)</code></pre>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Màn hình quầy realtime</h3>
            <p>Danh sách đơn vẫn do Server Component lấy từ <code>GET /orders/staff</code> (bài 06). Client Component dưới đây chỉ lắng nghe sự kiện, và khi có tin thì gọi <code>router.refresh()</code> để Server Component lấy lại danh sách. Dữ liệu luôn đến từ API, socket chỉ là "chuông báo".</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/admin/orders/orders-realtime.tsx
'use client';
import { useEffect, useRef, useState } from 'react';
import { useRouter } from 'next/navigation';
import { io } from 'socket.io-client';

type Conn = 'connecting' | 'online' | 'offline';
const LABEL: Record&lt;Conn, string&gt; = { connecting: 'Đang kết nối…', online: 'Đang nhận đơn trực tiếp', offline: 'Mất kết nối, đang thử lại…' };

export function OrdersRealtime() {
  const router = useRouter();
  const [conn, setConn] = useState&lt;Conn&gt;('connecting');
  const [lastOrder, setLastOrder] = useState&lt;number | null&gt;(null);
  const soundOn = useRef(false);

  useEffect(() =&gt; {
    const socket = io(process.env.NEXT_PUBLIC_SOCKET_URL!, {
      transports: ['websocket'],
      // auth dạng hàm: được gọi lại ở MỖI lần (kết nối lại), nên luôn có token mới
      auth: (cb) =&gt; {
        fetch('/api/socket-token', { cache: 'no-store' })
          .then((r) =&gt; (r.ok ? r.json() : { token: '' }))
          .then((d) =&gt; cb({ token: d.token }));
      },
    });

    socket.on('connect', () =&gt; { setConn('online'); router.refresh(); });   // bù các đơn lỡ khi mất kết nối
    socket.on('disconnect', () =&gt; setConn('offline'));
    socket.on('connect_error', () =&gt; {
      setConn('offline');
      setTimeout(() =&gt; socket.connect(), 3000);              // token bị từ chối: tự thử lại
    });
    socket.on('order:new', (e: { orderId: number }) =&gt; {
      setLastOrder(e.orderId);
      if (soundOn.current) beep();
      router.refresh();
    });
    socket.on('order:updated', () =&gt; router.refresh());     // nhân viên khác vừa đổi trạng thái

    return () =&gt; { socket.disconnect(); };
  }, [router]);

  return (
    &lt;div className="flex items-center gap-3"&gt;
      &lt;p aria-live="polite" className="text-sm"&gt;{LABEL[conn]}{lastOrder &amp;&amp; ` · Đơn mới nhất #${lastOrder}`}&lt;/p&gt;
      &lt;button onClick={() =&gt; { soundOn.current = true; beep(); }} className="rounded border px-2 py-1 text-sm"&gt;
        Bật âm báo
      &lt;/button&gt;
    &lt;/div&gt;
  );
}

function beep() {
  const ctx = new AudioContext();
  const osc = ctx.createOscillator();
  osc.frequency.value = 880;
  osc.connect(ctx.destination);
  osc.start();
  osc.stop(ctx.currentTime + 0.2);
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Bỏ bộ hẹn giờ 15 giây của bài 06; đặt <code>&lt;OrdersRealtime /&gt;</code> ở đầu trang <code>/admin/orders</code>.</li>
                <li><strong>Âm báo cần người dùng bấm trước:</strong> trình duyệt chặn phát âm thanh khi chưa có tương tác, nên có nút "Bật âm báo" ở đầu ca.</li>
                <li>Trạng thái kết nối hiện bằng chữ, có <code>aria-live</code>: nhân viên biết khi nào màn hình không còn "trực tiếp".</li>
                <li>Ở chế độ phát triển, React Strict Mode chạy <code>useEffect</code> hai lần. Thấy kết nối rồi ngắt ngay một lần là bình thường, nhờ hàm dọn dẹp <code>socket.disconnect()</code>.</li>
                <li><strong>Backend nhóm cần bổ sung</strong> (nếu làm theo Chương 9 di động): gateway cho cả <code>admin</code> vào room <code>staff</code>; phát <code>toStaff('order:updated', { orderId, status })</code> sau khi đổi trạng thái hoặc hủy đơn. API mẫu của giảng viên đã làm sẵn hai việc này.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Sơ đồ tuần tự: web và mobile trên cùng backend</h3>
            <p>Sơ đồ tuần tự là phần phân tích bắt buộc của Checkpoint 3 (CLO1). Nó cho thấy ai gọi ai, theo thứ tự nào, qua kênh nào (REST hay socket):</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>App khách (mobile)    API (NestJS)        SQL Server       Web quầy (2 nhân viên)
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
     │                      │── order:updated (room staff) ───────────▶│ màn hình B tự cập nhật</code></pre>
            <p style="margin-bottom: 0;">Trong báo cáo, vẽ lại bằng công cụ vẽ sơ đồ (draw.io, PlantUML, Mermaid), đánh số hình, kèm chú thích từng thông điệp. Thêm một sơ đồ cho tình huống lỗi: hai nhân viên cùng bấm, người sau nhận 409 (bài 06).</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Kiểm thử realtime và báo cáo Sprint 3</h3>
            <p>Realtime không kiểm được bằng một trình duyệt. Chuẩn bị: hai cửa sổ web (một thường, một ẩn danh) đăng nhập hai tài khoản staff, một điện thoại chạy ứng dụng di động của nhóm đăng nhập customer.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mã</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Tình huống</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Kết quả mong đợi</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-51</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Khách đặt món trên điện thoại (US-S02)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Cả hai cửa sổ quầy hiện đơn trong khoảng 2 giây, có âm báo nếu đã bật</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-52</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhân viên A bấm "Bắt đầu làm" (US-S03)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Cửa sổ B chuyển đơn sang "Đang chuẩn bị" không cần tải lại; điện thoại khách nhận thông báo</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-53</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tắt mạng cửa sổ A 30 giây (DevTools → Offline), trong lúc đó khách đặt một đơn, rồi bật lại</td><td style="border: 1px solid #ffd6ad; padding: 6px;">A hiện "Mất kết nối", khi có mạng tự kết nối lại và hiện đơn đã lỡ</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-54</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Để màn hình quầy mở quá 15 phút (token hết hạn), rồi khởi động lại backend</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Kết nối lại thành công bằng token mới, không phải đăng nhập lại</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-55</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Kết nối socket bằng token customer (script nhỏ dùng <code>socket.io-client</code>)</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Không nhận sự kiện <code>order:new</code> của room staff</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">TC-56</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Kết nối socket không có token hoặc token sửa một ký tự</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Bị từ chối (<code>connect_error</code>), không vào room nào</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Báo cáo Sprint 3 (CLO3)</strong> theo cấu trúc 6 mục, thêm: phân tích module quản trị (bảng mục 2.1 bài 07), ERD phần quản trị, danh mục stored procedure, sơ đồ tuần tự realtime, kết quả hồi quy khi chuyển sang backend nhóm.</p>
            <p style="margin-bottom: 0;"><strong>Điều chỉnh kế hoạch Sprint 4 (CLO4).</strong> Sprint 4 là sprint cuối: kiểm thử tự động, triển khai lên server Khoa, báo cáo đồ án và Demo Day chung với học phần di động. Cập nhật bảng velocity ba sprint, đưa các story "Could" chưa làm ra khỏi phạm vi nếu không đủ năng lực, và dành thời gian cho sửa lỗi và viết báo cáo. Bản nháp báo cáo vai trò cá nhân cập nhật thêm phần việc Sprint 3.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 09: Màn hình quầy thời gian thực với Socket.IO</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tiêu chí US-S02, S03, US-SYS01; chức năng F08.1 (kết nối và xác thực socket), F09.1–F09.2 (màn hình quầy); mục 8: danh mục API.</span>
            </a>
            <a href="{{LINK_AGILE_SCRUM}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🗂 Kế hoạch Agile &amp; Product Backlog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Release burndown, phạm vi Sprint 4, Definition of Done cho bản phát hành.</span>
            </a>
            <a href="{{LINK_RUBRIC}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📊 Rubric chấm điểm</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đối chiếu sản phẩm Checkpoint 3 với tiêu chí CLO1–CLO4 trước khi nộp.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://socket.io/how-to/use-with-nextjs" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Socket.IO - How to use with Next.js</span><br>
                <span style="color: #6c757d; font-size: 13px;">Kết nối từ Client Component, dọn dẹp khi gỡ component.</span>
            </a>
            <a href="https://socket.io/docs/v4/client-options/#auth" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Socket.IO - Client options (auth)</span><br>
                <span style="color: #6c757d; font-size: 13px;">auth dạng hàm, kết nối lại, xử lý connect_error.</span>
            </a>
            <a href="https://developer.mozilla.org/docs/Web/API/Web_Audio_API" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 MDN - Web Audio API</span><br>
                <span style="color: #6c757d; font-size: 13px;">Phát âm báo, chính sách tự phát âm thanh của trình duyệt.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Màn hình quầy nhận đơn trực tiếp</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tạo Route Handler <code>/api/socket-token</code>, thêm vào <code>matcher</code> của <code>proxy.ts</code>.</li>
                <li>Cài <code>socket.io-client</code>, tạo <code>OrdersRealtime</code>, gắn vào <code>/admin/orders</code>, bỏ bộ hẹn giờ 15 giây.</li>
                <li>Bổ sung backend nhóm: <code>admin</code> vào room <code>staff</code>, phát <code>order:updated</code>.</li>
                <li>Chạy TC-51…TC-56 với hai cửa sổ web và một điện thoại; ghi kết quả.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Dashboard tự cập nhật</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Trang <code>/admin</code> có 4 thẻ số liệu của ngày: số đơn chờ xác nhận, đang chuẩn bị, sẵn sàng, đã hoàn tất. Số liệu lấy từ API ở Server Component; khi có <code>order:new</code> hoặc <code>order:updated</code> thì tự cập nhật. Mỗi thẻ có nhãn bằng chữ; hiện trạng thái kết nối.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp link repo, video ngắn (dưới 1 phút) quay cảnh đặt món làm số liệu thay đổi, và kết quả 3 test case: đơn mới, đổi trạng thái, mất mạng rồi có lại.</p>
            <a href="{{LINK_NOP_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🏁 Checkpoint Sprint 3 (1 tiết)</strong></p>
            <ul style="margin: 0 0 8px 0; color: #495057;">
                <li>Demo: trang quản trị và màn hình quầy realtime; web và ứng dụng di động cùng chạy trên backend nhóm.</li>
                <li><strong>Phân tích (CLO1):</strong> phân tích module quản trị, ERD phần quản trị, danh mục stored procedure, sơ đồ tuần tự realtime.</li>
                <li><strong>Kiểm thử (CLO2):</strong> test case quản trị (TC-41…49), realtime (TC-51…56), kết quả hồi quy trên backend nhóm.</li>
                <li><strong>Báo cáo sprint 3 (CLO3)</strong> đúng cấu trúc và quy định định dạng.</li>
                <li><strong>Kế hoạch Sprint 4 (CLO4):</strong> velocity ba sprint, phạm vi phát hành, lịch chuẩn bị Demo Day; bản nháp báo cáo vai trò cá nhân cập nhật.</li>
            </ul>
            <a href="{{LINK_NOP_CHECKPOINT_3}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp Checkpoint 3</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Khi nhận <code>order:new</code>, màn hình quầy gọi lại API thay vì chèn thẳng dữ liệu trong sự kiện vào danh sách. Cách này chậm hơn một chút. Vì sao học phần vẫn chọn cách này? Có trường hợp nào nên dùng dữ liệu trong sự kiện không?</p>
            <a href="{{LINK_DIEN_DAN_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập Socket.IO trên web, xác thực kết nối, kết nối lại, sơ đồ tuần tự và kiểm thử realtime.</p>
            <a href="{{LINK_QUIZ_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 09</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Kết nối bị từ chối liên tục:</strong> mở <code>/api/socket-token</code> trên trình duyệt xem có trả token không; kiểm tra backend dùng cùng <code>JWT_SECRET</code> cho REST và socket; phiên bản <code>socket.io-client</code> cùng phiên bản chính với server.</p>
        <p><strong>Lỗi CORS khi kết nối socket:</strong> khác với REST, socket kết nối thẳng từ trình duyệt tới backend. Thêm địa chỉ web (ví dụ <code>http://localhost:3001</code>) vào cấu hình CORS của gateway Socket.IO.</p>
        <p><strong>Nhận mỗi sự kiện hai lần:</strong> tạo socket ngoài <code>useEffect</code> hoặc thiếu <code>socket.disconnect()</code> ở hàm dọn dẹp, nên mỗi lần render thêm một kết nối.</p>
        <p><strong>Nhân viên không nhận <code>order:new</code> nhưng khách vẫn nhận <code>order:status</code>:</strong> tài khoản chưa được đưa vào room <code>staff</code> (kiểm tra vai trò, đặc biệt <code>admin</code>), hoặc backend phát vào sai tên room.</p>
        <p><strong>Kiến thức mở rộng:</strong> "vé kết nối" (socket ticket) sống 30 giây do backend cấp, thay cho việc đưa access token xuống trình duyệt; Redis adapter để Socket.IO chạy trên nhiều máy chủ.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Rút dây mạng màn hình quầy trong một phút giờ cao điểm. Khi cắm lại, nhân viên có thấy đủ mọi đơn không? Test case nào của nhóm chứng minh điều đó?</p>
    </div>
</details>
