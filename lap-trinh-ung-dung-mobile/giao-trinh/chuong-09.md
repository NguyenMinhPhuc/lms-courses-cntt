# Chương 9. Thông báo thời gian thực với Socket.IO

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- So sánh polling, WebSocket và Socket.IO; giải thích sự kiện, room và xác thực kết nối.
- Thiết kế bảng và stored procedure lưu thông báo trên SQL Server.
- Xây dựng NestJS Gateway có xác thực JWT, gửi sự kiện tới đúng người dùng hoặc nhóm người dùng.
- Kết nối Socket.IO từ ứng dụng React Native, cập nhật dữ liệu và hiển thị thông báo cục bộ.
- Trình bày luồng dữ liệu realtime bằng sơ đồ tuần tự.

## 9.1. Giao tiếp thời gian thực

### 9.1.1. Vì sao cần realtime

Trong mô hình request–response của REST API, **ứng dụng luôn là bên hỏi**: server không thể chủ động báo "đơn của bạn đã xong". Với LHU Food, khách hàng cần biết ngay khi món sẵn sàng; nhân viên cần thấy ngay khi có đơn mới.

### 9.1.2. Ba cách tiếp cận

| Cách | Hoạt động | Độ trễ | Chi phí |
|---|---|---|---|
| Polling | Ứng dụng gọi API định kỳ (ví dụ 10 giây/lần) | Tới một chu kỳ | Nhiều request vô ích, tốn pin và tải server |
| WebSocket | Một kết nối hai chiều mở liên tục giữa ứng dụng và server | Gần như tức thời | Một kết nối cho mỗi thiết bị; phải tự xử lý kết nối lại, xác thực |
| Socket.IO | Thư viện xây trên WebSocket | Gần như tức thời | Có sẵn sự kiện có tên, room, tự kết nối lại, gửi kèm thông tin xác thực |

Học phần **bắt buộc** dùng Socket.IO cho thông báo realtime [1].

### 9.1.3. Khái niệm của Socket.IO

- **Kết nối (socket):** mỗi thiết bị đang mở ứng dụng có một kết nối tới server.
- **Sự kiện (event):** thông điệp có tên và dữ liệu JSON. Server gửi bằng `emit('order:status', data)`; client nhận bằng `on('order:status', handler)`. Quy ước đặt tên `<đối tượng>:<hành động>`.
- **Room:** nhóm kết nối do server quản lý; client không tự vào room. Server gửi tới room thì mọi kết nối trong room đều nhận.
- **Handshake:** bước bắt tay khi kết nối, client gửi kèm dữ liệu trong `auth` (dùng để gửi JWT).
- **Tự kết nối lại:** khi mất mạng rồi có mạng lại, client Socket.IO tự kết nối lại; server chạy lại bước xác thực và đưa vào room.

Socket.IO có giao thức riêng trên WebSocket, nên client phải dùng thư viện `socket.io-client` (không dùng `WebSocket` thuần) và **cùng phiên bản chính** với server (hiện là v4) [1], [2].

## 9.2. Thiết kế luồng thông báo

### 9.2.1. Nguyên tắc

1. **Socket chỉ để báo tin.** Mọi thao tác ghi (đổi trạng thái đơn, đánh dấu đã đọc) vẫn đi qua REST API và stored procedure, có xác thực và kiểm tra quyền như Chương 6.
2. **Lưu trước, gửi sau.** Thông báo được lưu vào SQL Server rồi mới gửi qua socket. Người dùng đang tắt app không nhận được sự kiện, nhưng mở app sẽ thấy đủ lịch sử.
3. **Gửi đúng người.** Mỗi người dùng một room riêng; nhân viên có thêm room chung.

### 9.2.2. Sơ đồ tuần tự

Sơ đồ tuần tự (sequence diagram) thể hiện thứ tự các thông điệp giữa các thành phần theo thời gian. Luồng "nhân viên đổi trạng thái đơn":

```text
App nhân viên        API NestJS                 SQL Server             App khách hàng
     │ PATCH /orders/12/status │                         │                       │
     │ {status: "ready"}       │                         │                       │
     │────────────────────────▶│ AuthGuard + RolesGuard  │                       │
     │                         │ EXEC sp_Order_UpdateStatus                      │
     │                         │────────────────────────▶│                       │
     │                         │◀──── {orderId, userId}  │                       │
     │                         │ EXEC sp_Notification_Create                     │
     │                         │────────────────────────▶│                       │
     │                         │◀──── {notification}     │                       │
     │                         │ emit 'order:status' → room user:5               │
     │                         │────────────────────────────────────────────────▶│
     │◀──────── 200 OK ────────│                         │  hiện thông báo,      │
     │                         │                         │  làm mới đơn hàng     │
```

Vẽ lại bằng draw.io (nhóm hình UML → Sequence) cho luồng realtime của đề tài. Sơ đồ là minh chứng CLO3 và là một phần của bộ thiết kế nộp cuối kỳ.

## 9.3. Cơ sở dữ liệu cho thông báo

`database/08-notifications.sql`:

```sql
CREATE TABLE Notifications (
  NotificationId INT IDENTITY(1,1) PRIMARY KEY,
  UserId         INT NOT NULL REFERENCES Users(UserId),
  Title          NVARCHAR(100) NOT NULL,
  Body           NVARCHAR(300) NOT NULL,
  OrderId        INT NULL REFERENCES Orders(OrderId),
  IsRead         BIT NOT NULL CONSTRAINT DF_Notifications_IsRead DEFAULT 0,
  CreatedAt      DATETIME2 NOT NULL CONSTRAINT DF_Notifications_CreatedAt DEFAULT SYSDATETIME()
);
CREATE INDEX IX_Notifications_UserId ON Notifications (UserId, IsRead, CreatedAt DESC);
GO

CREATE OR ALTER PROCEDURE sp_Order_UpdateStatus
  @OrderId INT, @Status NVARCHAR(20)
AS
-- … (trích 15/73 dòng; mã đầy đủ ở Phụ lục A, mục A.7)
```

- Mệnh đề `OUTPUT inserted....` trả về dòng vừa thêm/sửa, giúp backend có ngay dữ liệu để gửi qua socket mà không cần gọi thêm thủ tục.
- `sp_Order_UpdateStatus` chặn đổi trạng thái đơn đã kết thúc; ràng buộc `CK_Orders_Status` (Chương 7) chặn trạng thái không hợp lệ.
- `sp_Notification_MarkRead` kiểm tra `UserId` để người dùng không đánh dấu được thông báo của người khác.

## 9.4. Socket.IO trong NestJS

### 9.4.1. Cài đặt

Tham khảo [5].

```bash
npm install @nestjs/websockets @nestjs/platform-socket.io socket.io
```

### 9.4.2. Gateway

`src/notifications/notifications.gateway.ts`:

```ts
import { Logger } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { OnGatewayConnection, WebSocketGateway, WebSocketServer } from '@nestjs/websockets';
import { Server, Socket } from 'socket.io';

@WebSocketGateway()
export class NotificationsGateway implements OnGatewayConnection {
  @WebSocketServer() server!: Server;
  private readonly logger = new Logger(NotificationsGateway.name);

  constructor(private readonly jwt: JwtService) {}

  async handleConnection(client: Socket) {
    try {
      const payload = await this.jwt.verifyAsync<{ sub: number; role: string }>(client.handshake.auth?.token);
      client.data.user = payload;
      await client.join(`user:${payload.sub}`);
      if (payload.role === 'staff') await client.join('staff');
    } catch {
      this.logger.warn(`Từ chối kết nối ${client.id}: token không hợp lệ`);
      client.disconnect(true);
    }
  }

  toUser(userId: number, event: string, data: unknown) {
    this.server.to(`user:${userId}`).emit(event, data);
  }

  toStaff(event: string, data: unknown) {
    this.server.to('staff').emit(event, data);
  }
}
```

- `@WebSocketGateway()` không truyền cổng thì chạy chung HTTP server với API, nên ứng dụng dùng chung `EXPO_PUBLIC_API_URL`.
- Xác thực ở `handleConnection`: token sai hoặc hết hạn thì ngắt ngay; không bao giờ đưa kết nối chưa xác thực vào room.
- Không log nội dung token.

`src/notifications/notifications.module.ts`:

```ts
@Module({
  providers: [NotificationsGateway, NotificationsService],
  controllers: [NotificationsController],
  exports: [NotificationsGateway],
})
export class NotificationsModule {}
```

`OrdersModule` import `NotificationsModule` để `OrdersService` dùng được Gateway. `JwtService` có sẵn nhờ `JwtModule` đăng ký `global: true` ở Chương 6 [3], [5].

### 9.4.3. Gửi thông báo khi đổi trạng thái đơn

`src/orders/orders.service.ts`:

```ts
const STATUS_LABEL: Record<string, string> = {
  preparing: 'đang được chuẩn bị',
  ready: 'đã sẵn sàng, mời bạn đến nhận',
  completed: 'đã hoàn tất',
  cancelled: 'đã bị hủy',
};

@Injectable()
export class OrdersService {
  constructor(private readonly db: DatabaseService, private readonly gateway: NotificationsGateway) {}

  async updateStatus(orderId: number, status: string) {
    const [order] = await this.db.execute<{ orderId: number; userId: number; status: string }>(
      'sp_Order_UpdateStatus',
      { OrderId: { type: sql.Int, value: orderId }, Status: { type: sql.NVarChar(20), value: status } },
    );
    const [notification] = await this.db.execute('sp_Notification_Create', {
      UserId: { type: sql.Int, value: order.userId },
      Title: { type: sql.NVarChar(100), value: 'Cập nhật đơn hàng' },
      Body: { type: sql.NVarChar(300), value: `Đơn #${orderId} ${STATUS_LABEL[status] ?? status}` },
      OrderId: { type: sql.Int, value: orderId },
    });
    this.gateway.toUser(order.userId, 'order:status', { order, notification });
    return order;
  }

  async create(userId: number, dto: CreateOrderDto) {
    const [row] = await this.db.execute<{ orderId: number }>('sp_Order_Create', { /* như Chương 7 */ });
    this.gateway.toStaff('order:new', { orderId: row.orderId });
    return row;
  }
}
```

Endpoint `PATCH /orders/:id/status` có `@Roles(['staff'])` như Chương 6. Endpoint cho màn hình Thông báo: `GET /notifications?page=`, `GET /notifications/unread-count`, `POST /notifications/:id/read`, đều lấy `userId` từ token.

## 9.5. Phía ứng dụng

### 9.5.1. Cài đặt

Tham khảo [4].

```bash
npx expo install socket.io-client expo-notifications
```

### 9.5.2. Hook kết nối realtime

`hooks/useRealtime.ts`:

```ts
import { useEffect } from 'react';
import { io } from 'socket.io-client';
import { useQueryClient } from '@tanstack/react-query';
import * as Notifications from 'expo-notifications';
import { useAuth } from '@/stores/auth';

type OrderStatusEvent = {
  order: { orderId: number; status: string };
  notification: { id: number; title: string; body: string };
};

export function useRealtime() {
  const token = useAuth((s) => s.token);
  const role = useAuth((s) => s.role);
  const queryClient = useQueryClient();
// … (trích 15/43 dòng; mã đầy đủ ở Phụ lục A, mục A.8)
```

- **Vòng đời kết nối theo đăng nhập:** effect phụ thuộc `token`. Đăng xuất (`token = null`) thì ngắt; làm mới token (Chương 6) thì effect chạy lại và kết nối bằng token mới [4].
- **Sự kiện `connect`** xảy ra cả khi kết nối lần đầu và khi tự kết nối lại sau mất mạng; làm mới danh sách thông báo lúc này để không bỏ sót sự kiện trong thời gian mất kết nối.
- `transports: ['websocket']` bỏ qua bước long-polling ban đầu, phù hợp với môi trường React Native.
- Gọi `useRealtime()` một lần trong component gốc (`app/_layout.tsx`), bên trong `QueryClientProvider`.

### 9.5.3. Thông báo cục bộ và mở đúng màn hình

`app/_layout.tsx` (phần liên quan):

```tsx
import * as Notifications from 'expo-notifications';
import { router } from 'expo-router';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowBanner: true,
    shouldShowList: true,
    shouldPlaySound: true,
    shouldSetBadge: false,
  }),
});

function RealtimeBridge() {
  useRealtime();

  useEffect(() => {
    const sub = Notifications.addNotificationResponseReceivedListener((response) => {
      const url = response.notification.request.content.data?.url;
      if (typeof url === 'string') router.push(url);
    });
    return () => sub.remove();
  }, []);

  return null;
}
```

- `setNotificationHandler` quyết định thông báo có hiện khi ứng dụng **đang mở** hay không; mặc định thông báo bị ẩn khi app ở foreground. Tên các tùy chọn có thể khác giữa các phiên bản Expo SDK; đối chiếu tài liệu của phiên bản đang dùng [6].
- `trigger: null` hiện thông báo ngay. Đây là **thông báo cục bộ** (do chính ứng dụng tạo), chạy được trong Expo Go.
- Trên Android, có thể tạo kênh thông báo riêng (`Notifications.setNotificationChannelAsync`) để người dùng chỉnh mức độ ưu tiên trong Cài đặt.
- Xin quyền thông báo bằng `Notifications.requestPermissionsAsync()` ở thời điểm hợp lý, ví dụ sau khi người dùng đặt đơn đầu tiên.

### 9.5.4. Badge số thông báo chưa đọc

```tsx
const { data } = useQuery({
  queryKey: ['notifications', 'unread'],
  queryFn: () => api<{ unread: number }>('/notifications/unread-count'),
  enabled: !!token,
});

<Tabs.Screen name="notifications" options={{ title: 'Thông báo', tabBarBadge: data?.unread || undefined }} />
```

Khi nhận sự kiện socket, `invalidateQueries({ queryKey: ['notifications'] })` làm mới cả danh sách và số chưa đọc, vì cả hai đều có key bắt đầu bằng `['notifications']`.

## 9.6. Trải nghiệm người dùng với thông báo

- **Báo điều người dùng quan tâm:** đơn của tôi sẵn sàng, bị hủy. Không báo mọi thay đổi nhỏ; thông báo quá nhiều khiến người dùng tắt toàn bộ.
- **Nội dung cụ thể:** "Đơn #12 đã sẵn sàng, mời bạn đến nhận tại Quầy A" tốt hơn "Có cập nhật mới".
- **Bấm vào mở đúng nơi:** thông báo về đơn hàng mở chi tiết đơn đó.
- **Cho phép kiểm soát:** công tắc bật/tắt trong Cài đặt của ứng dụng; tôn trọng lựa chọn tắt thông báo của hệ điều hành.

## 9.7. Mở rộng: push notification khi ứng dụng đã tắt

Socket chỉ nhận sự kiện khi ứng dụng đang mở hoặc vừa chạy nền. Để nhận thông báo cả khi ứng dụng đã tắt cần **push notification** [7]:

1. Ứng dụng lấy **Expo Push Token** của thiết bị và gửi lên API để lưu vào bảng (qua thủ tục).
2. Khi có sự kiện, backend gửi request tới dịch vụ push của Expo kèm token; dịch vụ chuyển tiếp qua Firebase Cloud Messaging (Android) hoặc APNs (iOS).
3. Hệ điều hành hiển thị thông báo, kể cả khi ứng dụng không chạy.

Push notification cần development build (không chạy trong Expo Go trên Android ở các phiên bản SDK gần đây) và cấu hình thông tin xác thực FCM. Đây là phần **mở rộng**, không bắt buộc; phần bắt buộc của học phần là thông báo realtime bằng Socket.IO kết hợp thông báo cục bộ.

## 9.8. Checkpoint Sprint 3

Cuối buổi 09, mỗi nhóm:

- Demo **ít nhất một luồng thông báo realtime bằng Socket.IO** phù hợp nghiệp vụ, có lưu lịch sử trên SQL Server.
- Demo tính năng thiết bị (Chương 8) trên máy Android thật.
- Nộp sơ đồ tuần tự của luồng realtime trong `docs/`.
- Thực hiện Sprint Review và Retrospective; cập nhật backlog Sprint 4 (kiểm thử, triển khai, báo cáo); nộp `PROMPTS.md`.

## Tóm tắt chương

- Polling chậm và lãng phí; WebSocket/Socket.IO cho phép server chủ động gửi sự kiện gần như tức thời.
- Socket.IO: sự kiện có tên, room do server quản lý, gửi JWT qua `auth` khi bắt tay, tự kết nối lại.
- Socket chỉ báo tin; thao tác ghi đi qua API và thủ tục. Lưu thông báo vào SQL Server trước, gửi socket sau.
- Gateway xác thực ở `handleConnection`, đưa kết nối vào room `user:<id>` và `staff`.
- Ứng dụng kết nối theo token, làm mới cache khi nhận sự kiện và khi kết nối lại, hiện thông báo cục bộ, bấm vào mở đúng màn hình.
- Push notification khi ứng dụng đã tắt là phần mở rộng, cần development build.

## Câu hỏi ôn tập

1. So sánh polling và WebSocket về độ trễ và chi phí.
2. Room trong Socket.IO là gì? Vì sao client không được tự chọn room?
3. Vì sao phải lưu thông báo vào SQL Server trước khi gửi qua socket?
4. Gateway xử lý thế nào khi token gửi trong `auth` hết hạn?
5. Vì sao ứng dụng làm mới danh sách thông báo khi nhận sự kiện `connect`?
6. Thông báo cục bộ và push notification khác nhau thế nào?

## Bài tập

1. **Màn hình Thông báo.** Danh sách thông báo cuộn vô hạn, bấm một thông báo thì đánh dấu đã đọc và mở đơn hàng; badge chưa đọc trên tab; công tắc bật/tắt thông báo lưu bằng AsyncStorage.
2. **Đơn mới cho nhân viên.** Màn hình "Đơn mới" của nhân viên tự hiện đơn vừa đặt (sự kiện `order:new`), có âm báo bằng thông báo cục bộ.
3. **Sơ đồ và kiểm thử.** Vẽ sơ đồ tuần tự cho luồng realtime của đề tài; viết kịch bản kiểm thử: ứng dụng đang mở, chạy nền, đã tắt rồi mở lại, mất mạng rồi có mạng; ghi kết quả mong đợi cho từng trường hợp.

## Tài liệu tham khảo

[1] Socket.IO, “Introduction,” *Socket.IO Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://socket.io/docs/v4/

[2] Socket.IO, “Rooms,” *Socket.IO Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://socket.io/docs/v4/rooms/

[3] Socket.IO, “Middlewares: Sending credentials,” *Socket.IO Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://socket.io/docs/v4/middlewares/#sending-credentials

[4] Socket.IO, “How to use with React Native,” *Socket.IO Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://socket.io/how-to/use-with-react-native

[5] NestJS, “Gateways,” *NestJS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.nestjs.com/websockets/gateways

[6] Expo, “Notifications,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/versions/latest/sdk/notifications/

[7] Expo, “Expo push notifications: Overview,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/push-notifications/overview/
