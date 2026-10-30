// notification-service: REST thông báo + Socket.IO realtime (SRS M08).
// Client kết nối qua gateway (cùng địa chỉ, cùng cổng với REST), gửi access token trong handshake auth.
// Service khác gọi /internal/notify-* ; thông báo cho khách được LƯU SQL Server TRƯỚC rồi mới phát (BR-14).
const { Server } = require('socket.io');
const { createService, config, sql, z, schemas, auth, requireInternalKey } = require('@lhufood/shared');

const { id, page, pageSize } = schemas;
const tags = [
  { name: 'Notifications', description: 'Danh sách thông báo, số chưa đọc, đánh dấu đã đọc (F08.3)' },
  { name: 'Internal', description: 'Endpoint nội bộ cho order-service, cần header x-internal-key' },
];

let io = null; // gắn khi HTTP server khởi tạo xong (onServer)

function routes({ db, logger }) {
  const notificationExample = {
    id: 31, title: 'Cập nhật đơn hàng', body: 'Đơn #12 đã sẵn sàng, mời bạn đến nhận', orderId: 12,
    isRead: false, createdAt: '2026-10-30T10:25:00.000Z',
  };

  return [
    {
      method: 'get', path: '/notifications', tags: ['Notifications'], auth: true,
      summary: 'Thông báo của tôi (mới nhất trước)', description: 'US-C10. Trả về mảng, phân trang như lịch sử đơn.',
      query: z.object({ page, pageSize: pageSize(100, 20) }), example: [notificationExample],
      handler: ({ user, query }) =>
        db.execute('sp_Notification_GetList', {
          UserId: { type: sql.Int, value: user.sub },
          Page: { type: sql.Int, value: query.page },
          PageSize: { type: sql.Int, value: query.pageSize },
        }),
    },
    {
      method: 'get', path: '/notifications/unread-count', tags: ['Notifications'], auth: true,
      summary: 'Số thông báo chưa đọc (badge trên tab)', example: { unread: 3 },
      handler: async ({ user }) => {
        const [row] = await db.execute('sp_Notification_CountUnread', { UserId: { type: sql.Int, value: user.sub } });
        return row;
      },
    },
    {
      method: 'post', path: '/notifications/:id/read', tags: ['Notifications'], auth: true, status: 200,
      summary: 'Đánh dấu một thông báo đã đọc', description: 'Chỉ thông báo của chính mình, của người khác trả 404.',
      params: z.object({ id: id('Mã thông báo') }), errors: [404], example: { success: true },
      handler: async ({ user, params }) => {
        await db.execute('sp_Notification_MarkRead', {
          NotificationId: { type: sql.Int, value: params.id },
          UserId: { type: sql.Int, value: user.sub },
        });
        return { success: true };
      },
    },
    {
      method: 'post', path: '/notifications/read-all', tags: ['Notifications'], auth: true, status: 200,
      summary: 'Đánh dấu tất cả đã đọc', example: { updated: 3 },
      handler: async ({ user }) => {
        const [row] = await db.execute('sp_Notification_MarkAllRead', { UserId: { type: sql.Int, value: user.sub } });
        return row;
      },
    },

    // ---------- Nội bộ ----------
    {
      method: 'post', path: '/internal/notify-user', tags: ['Internal'], internal: requireInternalKey, status: 200,
      summary: 'Lưu thông báo cho một người dùng rồi phát sự kiện tới room user:<id>',
      body: z.object({
        userId: z.number().int().positive(),
        title: z.string().min(1).max(100),
        body: z.string().min(1).max(300),
        orderId: z.number().int().positive().optional(),
        event: z.string().default('order:status'),
        payload: z.record(z.string(), z.any()).default({}),
      }),
      example: { delivered: true },
      handler: async ({ body }) => {
        const [notification] = await db.execute('sp_Notification_Create', {
          UserId: { type: sql.Int, value: body.userId },
          Title: { type: sql.NVarChar(100), value: body.title },
          Body: { type: sql.NVarChar(300), value: body.body },
          OrderId: { type: sql.Int, value: body.orderId ?? null },
        });
        io?.to(`user:${body.userId}`).emit(body.event, { ...body.payload, notification });
        logger.info('Đã gửi thông báo', { userId: body.userId, event: body.event, notificationId: notification.id });
        return { delivered: true, notification };
      },
    },
    {
      method: 'post', path: '/internal/notify-staff', tags: ['Internal'], internal: requireInternalKey, status: 200,
      summary: 'Phát sự kiện tới room staff (order:new, order:updated)',
      body: z.object({ event: z.string().min(1), payload: z.record(z.string(), z.any()).default({}) }),
      example: { delivered: true },
      handler: ({ body }) => {
        io?.to('staff').emit(body.event, body.payload);
        return { delivered: true };
      },
    },
  ];
}

function attachSocket(server, { logger }) {
  io = new Server(server, {
    path: '/socket.io',
    cors: { origin: config.corsOrigins === '*' ? true : config.corsOrigins.split(',').map((s) => s.trim()) },
  });

  // Xác thực khi bắt tay: token sai hoặc hết hạn thì từ chối, không bao giờ vào room (US-SYS01)
  io.use((socket, next) => {
    const token = socket.handshake.auth?.token;
    try {
      socket.data.user = auth.verifyAccessToken(token);
      return next();
    } catch {
      logger.warn('Từ chối kết nối socket: token không hợp lệ', { socketId: socket.id });
      return next(new Error('Unauthorized'));
    }
  });

  io.on('connection', (socket) => {
    const { sub, role } = socket.data.user;
    socket.join(`user:${sub}`);
    if (role === 'staff' || role === 'admin') socket.join('staff');
    socket.emit('connected', { userId: sub, role, rooms: [...socket.rooms].filter((r) => r !== socket.id) });
  });
}

createService({
  name: 'notification-service',
  port: config.ports.notification,
  title: 'LHU Food - Notification Service',
  description:
    'Thông báo lưu trên SQL Server và gửi realtime bằng Socket.IO. ' +
    'Kết nối: io(API_URL, { auth: { token }, transports: ["websocket"] }). ' +
    'Sự kiện cho khách: order:status { order, notification }. Sự kiện cho nhân viên (room staff): order:new, order:updated.',
  tags,
  routes,
  onServer: attachSocket,
});
