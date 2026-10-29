# Bài 09: Thông báo thời gian thực với Socket.IO
Phần bắt buộc của học phần · Checkpoint Sprint 3

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- So sánh polling và WebSocket; nắm khái niệm của Socket.IO
- Xây NestJS Gateway có xác thực JWT, gửi theo room
- Lưu thông báo vào SQL Server qua stored procedure
- Nhận sự kiện trong app, hiện thông báo, mở đúng màn hình
**Ghi chú giảng viên**:
- 1 tiết lý thuyết, 4 tiết thực hành. CLO1, CLO3. Cuối buổi là Checkpoint Sprint 3.

---

## Slide 2: Câu hỏi mở đầu
**Nội dung chính**:
- Đặt món xong, ngồi chờ
- Không ai muốn 10 giây lại kéo màn hình một lần
- Nhân viên bấm "Sẵn sàng" → điện thoại của bạn sáng lên ngay?

---

## Slide 3: Polling và WebSocket
**Nội dung chính**:
- **Polling**: app hỏi định kỳ → chậm, tốn pin và tải server
- **WebSocket**: kết nối mở liên tục, server chủ động gửi → gần như tức thời
- **Socket.IO**: xây trên WebSocket, có sự kiện, room, tự kết nối lại, gửi auth

---

## Slide 4: Khái niệm Socket.IO
**Nội dung chính**:
- **Sự kiện**: thông điệp có tên, ví dụ `order:status`, kèm JSON
- **Room**: nhóm kết nối do server quản lý
- `user:<mã>` cho từng người; `staff` cho nhân viên
- **Handshake auth**: gửi JWT khi kết nối
**Hoạt động**: Lớp đề xuất room cho đề tài của nhóm mình

---

## Slide 5: Sơ đồ tuần tự
**Nội dung chính**:
```text
App nhân viên → PATCH /orders/12/status → API NestJS
API → EXEC sp_Order_UpdateStatus → SQL Server (trả userId)
API → EXEC sp_Notification_Create → SQL Server
API → emit 'order:status' tới room user:5 → App khách hàng
App khách hàng → hiện thông báo, làm mới đơn hàng
```
- Vẽ lại bằng draw.io: minh chứng CLO3

---

## Slide 6: Lưu thông báo trước, gửi sau
**Nội dung chính**:
- Bảng Notifications: UserId, Title, Body, OrderId, IsRead, CreatedAt
- `sp_Notification_Create`, `GetList`, `CountUnread`, `MarkRead`
- Người dùng đang tắt app vẫn xem lại được khi mở app
- `sp_Order_UpdateStatus` trả về `userId` người đặt bằng `OUTPUT`

---

## Slide 7: NestJS Gateway
**Nội dung chính**:
```ts
async handleConnection(client: Socket) {
  try {
    const payload = await this.jwt.verifyAsync(client.handshake.auth?.token);
    client.join(`user:${payload.sub}`);
    if (payload.role === 'staff') client.join('staff');
  } catch {
    client.disconnect();
  }
}
```

---

## Slide 8: Đổi trạng thái → thông báo → realtime
**Nội dung chính**:
```ts
const [order] = await this.db.execute('sp_Order_UpdateStatus', { ... });
const [notification] = await this.db.execute('sp_Notification_Create', { ... });
this.gateway.toUser(order.userId, 'order:status', { order, notification });
```
- Đơn mới: `toStaff('order:new', ...)`
- Socket chỉ **báo tin**; thao tác ghi vẫn qua API và thủ tục

---

## Slide 9: Kết nối từ ứng dụng
**Nội dung chính**:
```ts
useEffect(() => {
  if (!token) return;
  const socket = io(API_URL, { auth: { token }, transports: ['websocket'] });
  socket.on('order:status', ({ order, notification }) => {
    queryClient.invalidateQueries({ queryKey: ['orders'] });
    // hiện thông báo cục bộ
  });
  return () => { socket.disconnect(); };
}, [token]);
```

---

## Slide 10: Thông báo cục bộ
**Nội dung chính**:
- `Notifications.scheduleNotificationAsync({ content, trigger: null })`: hiện ngay
- `setNotificationHandler`: hiện cả khi app đang mở
- `content.data.url` + listener bấm thông báo → `router.push(url)`
- Chạy được trong Expo Go; đây là phần **bắt buộc**
**Ghi chú giảng viên**:
- Mở rộng: push notification khi app đã tắt cần development build.

---

## Slide 11: Trải nghiệm người dùng
**Nội dung chính**:
- Chỉ báo điều người dùng quan tâm
- Badge chưa đọc; mở màn hình Thông báo thì đánh dấu đã đọc
- Cho phép tắt từng loại thông báo
- Xin quyền thông báo sau đơn đầu tiên, có giải thích

---

## Slide 12: Thực hành có hướng dẫn
**Nội dung chính**:
- Bảng Notifications và thủ tục; chạy thử bằng EXEC
- NotificationsGateway; PATCH /orders/:id/status cho staff
- useRealtime, setNotificationHandler, xử lý bấm thông báo
- Hai thiết bị: nhân viên đổi trạng thái → khách nhận thông báo
- Vẽ sơ đồ tuần tự

---

## Slide 13: Thực hành không hướng dẫn
**Nội dung chính**:
- Màn hình Thông báo: lịch sử từ API, cuộn vô hạn
- Bấm thông báo: đánh dấu đã đọc, mở đơn hàng
- Badge chưa đọc cập nhật theo sự kiện socket
- Công tắc bật/tắt thông báo
- Người dùng A không đánh dấu được thông báo của B

---

## Slide 14: Checkpoint Sprint 3
**Nội dung chính**:
- **Bắt buộc**: ít nhất 1 luồng realtime bằng Socket.IO, có lưu lịch sử
- Nộp sơ đồ tuần tự trong `docs/`
- Demo tính năng thiết bị và realtime trên Android thật
- Cập nhật backlog Sprint 4; nộp `PROMPTS.md`

---

## Slide 15: Tóm tắt
**Nội dung chính**:
- WebSocket/Socket.IO thay polling cho thông báo tức thời
- Gateway xác thực JWT, gửi theo room người dùng/vai trò
- Lưu thông báo vào SQL Server trước, gửi socket sau
- App: kết nối theo token, làm mới cache, hiện thông báo, mở đúng màn hình
**Hoạt động**: Làm quiz Bài 09 ở cuối trang bài học
