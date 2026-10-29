<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 09 - Thông báo thời gian thực với Socket.IO - BẮT BUỘC (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Bạn đặt món xong và ngồi chờ. Không ai muốn cứ 10 giây lại kéo màn hình để xem "món của mình xong chưa". Làm sao để ngay khi nhân viên căn tin bấm "Sẵn sàng", điện thoại của bạn sáng lên báo tin?</em></p>
        <p><strong>Mục tiêu:</strong> Giải thích được cơ chế giao tiếp thời gian thực (WebSocket/Socket.IO) và so sánh với polling; xây dựng được thông báo realtime từ NestJS tới ứng dụng, có xác thực và lưu lịch sử trên SQL Server; trình bày được luồng dữ liệu realtime bằng sơ đồ tuần tự.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Realtime là gì:</strong> polling và WebSocket; Socket.IO với kết nối, sự kiện, room, tự kết nối lại; sơ đồ tuần tự luồng thông báo.</li>
            <li><strong>Ý chính 2 - NestJS Gateway:</strong> <code>@WebSocketGateway</code>, xác thực kết nối bằng JWT, gửi sự kiện theo room người dùng/vai trò, lưu thông báo qua stored procedure.</li>
            <li><strong>Ý chính 3 - Phía ứng dụng:</strong> <code>socket.io-client</code>, kết nối theo trạng thái đăng nhập, cập nhật cache TanStack Query khi nhận sự kiện.</li>
            <li><strong>Ý chính 4 - Hiển thị thông báo:</strong> banner trong app, badge chưa đọc, thông báo cục bộ bằng <code>expo-notifications</code>, bấm thông báo mở đúng màn hình; mở rộng: push khi app đã tắt.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Khi nhân viên đổi trạng thái đơn, người đặt nhận thông báo ngay; màn hình đơn hàng tự cập nhật; nhóm hoàn thành <strong>Checkpoint Sprint 3</strong> với ít nhất một luồng realtime và sơ đồ tuần tự.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO3.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Polling, WebSocket và Socket.IO</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Cách làm</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Hoạt động</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Nhận xét</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Polling</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">App hỏi API định kỳ: "có gì mới không?"</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Đơn giản nhưng chậm (phụ thuộc chu kỳ hỏi), tốn pin và tải server khi không có gì mới</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>WebSocket</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Một kết nối mở liên tục; server chủ động gửi khi có sự kiện</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Gần như tức thời; phải tự xử lý kết nối lại, xác thực, nhóm người nhận</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Socket.IO</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Thư viện xây trên WebSocket</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Có sẵn sự kiện có tên, <strong>room</strong>, tự kết nối lại, gửi kèm dữ liệu xác thực khi kết nối</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 6px 0;"><strong>Khái niệm chính của Socket.IO:</strong></p>
            <ul>
                <li><strong>Sự kiện (event):</strong> thông điệp có tên, ví dụ <code>order:status</code>, kèm dữ liệu JSON.</li>
                <li><strong>Room:</strong> nhóm kết nối do server quản lý. Mỗi người dùng vào room <code>user:&lt;mã&gt;</code>; nhân viên vào thêm room <code>staff</code>. Gửi tới room thì mọi máy của người đó (hoặc mọi nhân viên) đều nhận.</li>
                <li><strong>Handshake auth:</strong> dữ liệu gửi kèm lúc kết nối; dùng để gửi JWT.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>💡 Sơ đồ tuần tự: nhân viên đổi trạng thái đơn</strong></p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>App nhân viên      API NestJS               SQL Server            App khách hàng
     │  PATCH /orders/12/status   │                        │                     │
     │──────────────────────────▶│ EXEC sp_Order_UpdateStatus                    │
     │                            │───────────────────────▶│ (trả userId người đặt)│
     │                            │ EXEC sp_Notification_Create                   │
     │                            │───────────────────────▶│                     │
     │                            │ emit 'order:status' tới room user:5           │
     │                            │─────────────────────────────────────────────▶│
     │        200 OK              │                        │   hiện thông báo,    │
     │◀──────────────────────────│                        │   làm mới đơn hàng   │</code></pre>
            <p style="margin-bottom: 0;">Vẽ lại sơ đồ này bằng draw.io (Sequence diagram) cho luồng realtime của nhóm; đây là minh chứng cho CLO3.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. CSDL và thủ tục cho thông báo</h3>
            <p>Thông báo được <strong>lưu vào SQL Server trước</strong> rồi mới gửi qua socket. Nhờ vậy người dùng đang tắt app vẫn xem lại được lịch sử khi mở app.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>CREATE TABLE Notifications (
  NotificationId INT IDENTITY(1,1) PRIMARY KEY,
  UserId         INT NOT NULL REFERENCES Users(UserId),
  Title          NVARCHAR(100) NOT NULL,
  Body           NVARCHAR(300) NOT NULL,
  OrderId        INT NULL REFERENCES Orders(OrderId),
  IsRead         BIT NOT NULL DEFAULT 0,
  CreatedAt      DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);
CREATE INDEX IX_Notifications_UserId ON Notifications (UserId, IsRead, CreatedAt DESC);
GO

CREATE OR ALTER PROCEDURE sp_Order_UpdateStatus
  @OrderId INT, @Status NVARCHAR(20)
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM Orders WHERE OrderId = @OrderId)
    THROW 50404, N'Không tìm thấy đơn hàng', 1;

  UPDATE Orders SET Status = @Status
  OUTPUT inserted.OrderId AS orderId, inserted.UserId AS userId, inserted.Status AS status
  WHERE OrderId = @OrderId;
END;
GO</code></pre>
            <p style="margin-bottom: 0;">Tương tự, viết <code>sp_Notification_Create</code> (trả về thông báo vừa tạo), <code>sp_Notification_GetList</code> (phân trang), <code>sp_Notification_CountUnread</code> và <code>sp_Notification_MarkRead</code> (chỉ đánh dấu được thông báo của chính <code>@UserId</code>). Ràng buộc <code>CK_Orders_Status</code> ở bài 07 tự chặn trạng thái không hợp lệ.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. NestJS Gateway</h3>
            <p>Cài: <code>npm install @nestjs/websockets @nestjs/platform-socket.io socket.io</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// src/notifications/notifications.gateway.ts
import { OnGatewayConnection, WebSocketGateway, WebSocketServer } from '@nestjs/websockets';
import { JwtService } from '@nestjs/jwt';
import { Server, Socket } from 'socket.io';

@WebSocketGateway()
export class NotificationsGateway implements OnGatewayConnection {
  @WebSocketServer() server!: Server;

  constructor(private readonly jwt: JwtService) {}

  async handleConnection(client: Socket) {
    try {
      const payload = await this.jwt.verifyAsync(client.handshake.auth?.token);
      client.data.user = payload;
      client.join(`user:${payload.sub}`);
      if (payload.role === 'staff') client.join('staff');
    } catch {
      client.disconnect();                 // không có token hợp lệ thì ngắt ngay
    }
  }

  toUser(userId: number, event: string, data: unknown) {
    this.server.to(`user:${userId}`).emit(event, data);
  }

  toStaff(event: string, data: unknown) {
    this.server.to('staff').emit(event, data);
  }
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// src/orders/orders.service.ts: đổi trạng thái → lưu thông báo → gửi realtime
const STATUS_LABEL: Record&lt;string, string&gt; = {
  preparing: 'đang được chuẩn bị', ready: 'đã sẵn sàng, mời bạn đến nhận',
  completed: 'đã hoàn tất', cancelled: 'đã bị hủy',
};

async updateStatus(orderId: number, status: string) {
  const [order] = await this.db.execute&lt;{ orderId: number; userId: number; status: string }&gt;(
    'sp_Order_UpdateStatus',
    { OrderId: { type: sql.Int, value: orderId }, Status: { type: sql.NVarChar(20), value: status } },
  );
  const [notification] = await this.db.execute('sp_Notification_Create', {
    UserId: { type: sql.Int, value: order.userId },
    Title: { type: sql.NVarChar(100), value: 'Cập nhật đơn hàng' },
    Body: { type: sql.NVarChar(300), value: `Đơn #${orderId}: ${STATUS_LABEL[status]}` },
    OrderId: { type: sql.Int, value: orderId },
  });
  this.gateway.toUser(order.userId, 'order:status', { order, notification });
  return order;
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Gateway mặc định chạy chung cổng với API (cùng HTTP server), nên app dùng chung địa chỉ <code>EXPO_PUBLIC_API_URL</code>.</li>
                <li>Khi khách đặt đơn mới, gọi <code>toStaff('order:new', …)</code> để màn hình của nhân viên hiện đơn ngay.</li>
                <li>Socket <strong>không thay</strong> API: mọi thao tác ghi vẫn đi qua API và stored procedure; socket chỉ dùng để <strong>báo tin</strong>.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Phía ứng dụng: kết nối và nhận sự kiện</h3>
            <p>Cài: <code>npx expo install socket.io-client expo-notifications</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// hooks/useRealtime.ts: gọi một lần trong app/_layout.tsx
import { useEffect } from 'react';
import { io } from 'socket.io-client';
import { useQueryClient } from '@tanstack/react-query';
import * as Notifications from 'expo-notifications';
import { useAuth } from '@/stores/auth';

export function useRealtime() {
  const token = useAuth((s) =&gt; s.token);
  const queryClient = useQueryClient();

  useEffect(() =&gt; {
    if (!token) return;                                   // chỉ kết nối khi đã đăng nhập
    const socket = io(process.env.EXPO_PUBLIC_API_URL!, {
      auth: { token },
      transports: ['websocket'],
    });

    socket.on('order:status', async ({ order, notification }) =&gt; {
      queryClient.invalidateQueries({ queryKey: ['orders'] });
      queryClient.invalidateQueries({ queryKey: ['notifications'] });
      await Notifications.scheduleNotificationAsync({
        content: {
          title: notification.title,
          body: notification.body,
          data: { url: `/order/${order.orderId}` },
        },
        trigger: null,                                    // hiện ngay
      });
    });

    return () =&gt; { socket.disconnect(); };                // đăng xuất hoặc đổi token
  }, [token, queryClient]);
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/_layout.tsx: hiện thông báo cả khi app đang mở, bấm thông báo mở đúng màn hình
Notifications.setNotificationHandler({
  handleNotification: async () =&gt; ({
    shouldShowBanner: true, shouldShowList: true, shouldPlaySound: true, shouldSetBadge: false,
  }),
});

useEffect(() =&gt; {
  Notifications.requestPermissionsAsync();
  const sub = Notifications.addNotificationResponseReceivedListener((response) =&gt; {
    const url = response.notification.request.content.data?.url;
    if (typeof url === 'string') router.push(url);
  });
  return () =&gt; sub.remove();
}, []);</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Thông báo cục bộ</strong> (do chính app tạo khi nhận sự kiện socket) chạy được trong Expo Go và là phần <strong>bắt buộc</strong>.</li>
                <li>Socket chỉ hoạt động khi app đang mở hoặc vừa chạy nền. Khi mở lại app, gọi lại API danh sách thông báo để không bỏ sót.</li>
                <li><strong>Mở rộng:</strong> nhận thông báo cả khi app đã tắt cần <strong>push notification</strong> (Expo Push Token, lưu token ở backend, gửi qua dịch vụ push của Expo) và development build; xem tài liệu Expo Notifications.</li>
                <li>Tên các tùy chọn của <code>setNotificationHandler</code> có thể khác giữa các phiên bản Expo SDK; đối chiếu tài liệu của phiên bản dự án đang dùng.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Trải nghiệm người dùng với thông báo</h3>
            <ul style="margin-bottom: 0;">
                <li><strong>Chỉ báo điều người dùng quan tâm:</strong> đơn của tôi sẵn sàng, đơn bị hủy. Không báo mọi thay đổi nhỏ.</li>
                <li><strong>Có badge chưa đọc</strong> trên tab hoặc biểu tượng chuông; mở màn hình Thông báo thì đánh dấu đã đọc.</li>
                <li><strong>Cho phép tắt</strong> từng loại thông báo trong Cài đặt của app.</li>
                <li><strong>Xin quyền có giải thích:</strong> hỏi quyền thông báo sau khi người dùng đặt đơn đầu tiên ("Bật thông báo để biết khi món sẵn sàng?"), không hỏi ngay khi mở app.</li>
            </ul>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 09: Thông báo thời gian thực với Socket.IO</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">▶ Video 09: Demo thông báo realtime LHU Food giữa app nhân viên và app khách hàng</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.nestjs.com/websockets/gateways" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - WebSockets Gateways</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tạo Gateway, vòng đời kết nối, gửi sự kiện.</span>
            </a>
            <a href="https://socket.io/docs/v4/rooms/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Socket.IO - Rooms</span><br>
                <span style="color: #6c757d; font-size: 13px;">Gửi sự kiện tới một nhóm kết nối.</span>
            </a>
            <a href="https://socket.io/docs/v4/middlewares/#sending-credentials" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Socket.IO - Sending credentials</span><br>
                <span style="color: #6c757d; font-size: 13px;">Gửi token khi kết nối qua <code>auth</code>.</span>
            </a>
            <a href="https://docs.expo.dev/versions/latest/sdk/notifications/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - Notifications</span><br>
                <span style="color: #6c757d; font-size: 13px;">Thông báo cục bộ, xử lý khi bấm thông báo, push notification (mở rộng).</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Đơn hàng realtime LHU Food</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tạo bảng <code>Notifications</code> và các thủ tục ở mục 2.2; chạy thử bằng <code>EXEC</code>.</li>
                <li>Tạo <code>NotificationsGateway</code> (mục 2.3); <code>PATCH /orders/:id/status</code> (chỉ <code>staff</code>) gọi <code>updateStatus</code>.</li>
                <li>Trong app: <code>useRealtime()</code>, <code>setNotificationHandler</code>, xử lý bấm thông báo.</li>
                <li>Dùng hai thiết bị (hoặc một máy thật + một emulator): một tài khoản <code>staff</code>, một tài khoản <code>customer</code>. Nhân viên đổi đơn sang "Sẵn sàng" → khách nhận thông báo, màn hình đơn hàng tự cập nhật.</li>
                <li>Đặt đơn mới từ máy khách → màn hình đơn mới của nhân viên hiện ngay (sự kiện <code>order:new</code>).</li>
                <li>Vẽ sơ đồ tuần tự của luồng vừa làm bằng draw.io.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Màn hình Thông báo</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Màn hình "Thông báo" hiển thị lịch sử lấy từ API (cuộn vô hạn), bấm một thông báo thì đánh dấu đã đọc và mở đơn hàng tương ứng; badge số chưa đọc trên tab cập nhật ngay khi có sự kiện socket; màn hình Cài đặt có công tắc bật/tắt thông báo (lưu bằng AsyncStorage).</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> tắt app, nhân viên đổi trạng thái 2 đơn, mở lại app vẫn thấy đủ 2 thông báo chưa đọc; người dùng A không đánh dấu đọc được thông báo của người dùng B (API kiểm tra qua thủ tục).</p>
            <a href="{{LINK_NOP_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🏁 Thử thách nhóm: Checkpoint Sprint 3</strong></p>
            <ul style="margin: 0 0 8px 0; color: #495057;">
                <li><strong>Bắt buộc:</strong> ít nhất 1 luồng thông báo realtime bằng Socket.IO phù hợp nghiệp vụ của đề tài, có lưu lịch sử trên SQL Server.</li>
                <li>Nộp <strong>sơ đồ tuần tự</strong> của luồng realtime trong <code>docs/</code>.</li>
                <li>Demo tính năng thiết bị (bài 08) và realtime trên máy Android thật; Sprint Review và Retrospective.</li>
                <li>Cập nhật backlog cho Sprint 4 (kiểm thử, triển khai, báo cáo); nộp <code>PROMPTS.md</code> của sprint 3.</li>
            </ul>
            <a href="{{LINK_NOP_CHECKPOINT_3}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp Checkpoint 3</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Trong đề tài của nhóm, sự kiện nào thật sự cần báo ngay (realtime), sự kiện nào chỉ cần người dùng xem khi mở app? Nếu báo mọi thứ, trải nghiệm người dùng sẽ ra sao?</p>
            <a href="{{LINK_DIEN_DAN_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập polling và WebSocket, Socket.IO room, Gateway có xác thực, thông báo cục bộ và sơ đồ tuần tự.</p>
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
        <p><strong>App không kết nối được socket:</strong> dùng cùng địa chỉ IP LAN như API, không dùng <code>localhost</code>; đặt <code>transports: ['websocket']</code>; kiểm tra phiên bản <code>socket.io-client</code> tương thích với <code>socket.io</code> phía server (cùng v4).</p>
        <p><strong>Kết nối được rồi bị ngắt ngay:</strong> token gửi trong <code>auth</code> không hợp lệ hoặc đã hết hạn; sau khi làm mới token (bài 06), effect trong <code>useRealtime</code> chạy lại và kết nối với token mới.</p>
        <p><strong>Nhận sự kiện nhưng không hiện thông báo:</strong> chưa xin quyền thông báo, hoặc chưa gọi <code>setNotificationHandler</code> nên thông báo bị ẩn khi app đang mở.</p>
        <p><strong>Kiến thức mở rộng:</strong> Push notification bằng Expo Push Service khi app đã tắt; Socket.IO adapter (ví dụ Redis) khi API chạy nhiều tiến trình.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu server gửi sự kiện realtime nhưng <em>không</em> lưu thông báo vào SQL Server, người dùng đang tắt app sẽ mất gì?</p>
    </div>
</details>
