// order-service: đặt món, lịch sử, chi tiết, hủy, xử lý đơn của nhân viên, báo cáo, đánh giá
// (SRS M04, M09, M10, F07.4). Sau khi ghi CSDL, gọi notification-service (thông báo) và
// catalog-service (xóa cache tồn kho) qua HTTP nội bộ; lỗi ở đó không làm hỏng đơn hàng.
const { createService, config, sql, z, schemas, auth, callInternal } = require('@lhufood/shared');

const { id, page, pageSize, dateString } = schemas;

const tags = [
  { name: 'Orders', description: 'Đặt món, lịch sử, chi tiết, hủy đơn của khách hàng (F04.1–F04.4)' },
  { name: 'Staff - Orders', description: 'Màn hình đơn của nhân viên: danh sách, đổi trạng thái, hủy kèm lý do (F09.1, F09.2)' },
  { name: 'Reports', description: 'Doanh thu, món bán chạy, thống kê trạng thái (F10), có cache 60 giây' },
  { name: 'Reviews', description: 'Đánh giá món đã nhận (F07.4, mở rộng)' },
];

const STATUS_LABEL = {
  preparing: 'đang được chuẩn bị',
  ready: 'đã sẵn sàng, mời bạn đến nhận',
  completed: 'đã hoàn tất',
  cancelled: 'đã bị hủy',
};

const today = () => new Date().toISOString().slice(0, 10);
const sqlDate = (s) => new Date(`${s}T00:00:00Z`);

function routes({ db, cache, logger }) {
  // Gọi service khác không chờ kết quả: đơn hàng đã lưu thành công thì phải trả về cho khách ngay
  const background = (label, promise) =>
    promise.catch((err) => logger.warn(`${label} thất bại`, { error: err.message }));

  const notifyUser = (order, title, body) =>
    background(
      'Gửi thông báo cho khách',
      callInternal(config.urls.notification, '/internal/notify-user', {
        userId: order.userId, title, body, orderId: order.orderId,
        event: 'order:status', payload: { order: { orderId: order.orderId, userId: order.userId, status: order.status } },
      }),
    );
  const notifyStaff = (event, payload) =>
    background('Gửi sự kiện cho nhân viên', callInternal(config.urls.notification, '/internal/notify-staff', { event, payload }));
  const refreshStock = (productIds) =>
    background('Xóa cache tồn kho', callInternal(config.urls.catalog, '/internal/cache/products', { productIds }));

  const getOrder = async (orderId, userId) => {
    const [[order], items] = await db.executeMulti('sp_Order_GetById', {
      OrderId: { type: sql.Int, value: orderId },
      UserId: { type: sql.Int, value: userId ?? null },
    });
    return { ...order, items };
  };
  const productIdsOf = async (orderId) => (await getOrder(orderId)).items.map((i) => i.productId);

  const report = (res, key, loader) =>
    cache.wrap(`order:report:${key}`, 60, loader).then(({ value, hit }) => {
      res.setHeader('X-Cache', hit ? 'HIT' : 'MISS');
      return value;
    });
  const rangeFields = z.object({
    from: dateString.default(today).describe('Từ ngày (YYYY-MM-DD), mặc định hôm nay'),
    to: dateString.default(today).describe('Đến ngày (YYYY-MM-DD), mặc định hôm nay'),
  });
  const validRange = [(q) => q.from <= q.to, { message: 'Ngày bắt đầu phải trước hoặc bằng ngày kết thúc', path: ['from'] }];
  const range = rangeFields.refine(...validRange);
  const topRange = rangeFields.extend({ top: z.coerce.number().int().min(1).max(50).default(5) }).refine(...validRange);

  const orderDetailExample = {
    orderId: 12, userId: 3, customerName: 'Nguyễn Văn A', status: 'pending', note: 'Ít cay', cancelReason: null,
    counterId: 1, counterName: 'Căn tin cơ sở 1', createdAt: '2026-10-30T10:15:00.000Z', updatedAt: null, total: 75000,
    items: [
      { productId: 1, name: 'Cơm gà xối mỡ', imageUrl: null, quantity: 1, unitPrice: 35000, lineTotal: 35000 },
      { productId: 5, name: 'Bún bò Huế', imageUrl: null, quantity: 1, unitPrice: 40000, lineTotal: 40000 },
    ],
  };

  return [
    // ---------- Khách hàng ----------
    {
      method: 'post', path: '/orders', tags: ['Orders'], auth: true,
      summary: 'Đặt món',
      description:
        'US-C04, US-C05. Giá lấy từ CSDL tại thời điểm đặt; thiếu tồn kho hoặc món ngừng bán trả 409 và không lưu gì (giao dịch). ' +
        'Thành công: nhân viên nhận sự kiện socket `order:new`.',
      body: z.object({
        items: z
          .array(z.object({ productId: id('Mã món'), quantity: z.number().int().min(1).max(50) }))
          .min(1, 'Đơn hàng phải có ít nhất một món').max(30),
        note: z.string().trim().max(200).optional(),
        counterId: id('Mã quầy').optional(),
      }),
      errors: [404, 409],
      example: { orderId: 12, userId: 3, status: 'pending', createdAt: '2026-10-30T10:15:00.000Z', total: 75000, itemCount: 2 },
      handler: async ({ user, body }) => {
        const [order] = await db.execute('sp_Order_Create', {
          UserId: { type: sql.Int, value: user.sub },
          Note: { type: sql.NVarChar(200), value: body.note || null },
          CounterId: { type: sql.Int, value: body.counterId ?? null },
          ItemsJson: { type: sql.NVarChar(sql.MAX), value: JSON.stringify(body.items) },
        });
        notifyStaff('order:new', { orderId: order.orderId, createdAt: order.createdAt, itemCount: order.itemCount, total: order.total });
        refreshStock(body.items.map((i) => i.productId));
        return order;
      },
    },
    {
      method: 'get', path: '/orders', tags: ['Orders'], auth: true,
      summary: 'Lịch sử đơn của tôi',
      description: 'US-C06. Trả về **mảng**, mới nhất trước; hết trang khi số phần tử < pageSize (Chương 5).',
      query: z.object({ page, pageSize: pageSize(100, 20) }),
      example: [{ orderId: 12, createdAt: '2026-10-30T10:15:00.000Z', status: 'pending', counterName: 'Căn tin cơ sở 1', total: 75000, itemCount: 2 }],
      handler: ({ user, query }) =>
        db.execute('sp_Order_GetHistory', {
          UserId: { type: sql.Int, value: user.sub },
          Page: { type: sql.Int, value: query.page },
          PageSize: { type: sql.Int, value: query.pageSize },
        }),
    },
    {
      method: 'get', path: '/orders/staff', tags: ['Staff - Orders'], auth: ['staff'],
      summary: 'Đơn cần xử lý trong ngày',
      description: 'US-S02, US-S06. Không truyền status: mọi đơn pending/preparing/ready của ngày.',
      query: z.object({
        status: z.enum(['pending', 'preparing', 'ready', 'completed', 'cancelled']).optional(),
        date: dateString.optional().describe('Ngày cần xem, mặc định hôm nay'),
      }),
      example: [{ orderId: 12, status: 'pending', note: 'Ít cay', createdAt: '2026-10-30T10:15:00.000Z', customerName: 'Nguyễn Văn A', counterName: 'Căn tin cơ sở 1', total: 75000, itemCount: 2, summary: 'Cơm gà xối mỡ x1, Bún bò Huế x1' }],
      handler: ({ query }) =>
        db.execute('sp_Order_GetListForStaff', {
          Status: { type: sql.NVarChar(20), value: query.status ?? null },
          Date: { type: sql.Date, value: query.date ? sqlDate(query.date) : null },
        }),
    },
    {
      method: 'get', path: '/orders/:id', tags: ['Orders'], auth: true,
      summary: 'Chi tiết đơn', description: 'US-C07. Khách chỉ xem đơn của mình (đơn người khác trả 404); nhân viên xem mọi đơn.',
      params: z.object({ id: id('Mã đơn') }), errors: [404], example: orderDetailExample,
      handler: ({ user, params }) => getOrder(params.id, auth.isStaff(user) ? null : user.sub),
    },
    {
      method: 'post', path: '/orders/:id/cancel', tags: ['Orders'], auth: true, status: 200,
      summary: 'Khách hủy đơn (chỉ khi pending)', description: 'US-C08. Hoàn tồn kho; đơn của người khác hoặc đã chuẩn bị trả 409.',
      params: z.object({ id: id('Mã đơn') }), errors: [409],
      example: { orderId: 12, userId: 3, status: 'cancelled' },
      handler: async ({ user, params }) => {
        const [order] = await db.execute('sp_Order_Cancel', {
          OrderId: { type: sql.Int, value: params.id },
          UserId: { type: sql.Int, value: user.sub },
        });
        notifyUser(order, 'Cập nhật đơn hàng', `Bạn đã hủy đơn #${order.orderId}`);
        notifyStaff('order:updated', { orderId: order.orderId, status: order.status });
        background('Xóa cache tồn kho', productIdsOf(order.orderId).then(refreshStock));
        return order;
      },
    },

    // ---------- Nhân viên ----------
    {
      method: 'patch', path: '/orders/:id/status', tags: ['Staff - Orders'], auth: ['staff'],
      summary: 'Chuyển trạng thái đơn (đúng trình tự)',
      description:
        'US-S03. Chỉ cho phép pending → preparing → ready → completed (BR-15), sai trình tự trả 409. ' +
        'Lưu thông báo rồi gửi `order:status` tới khách (BR-14).',
      params: z.object({ id: id('Mã đơn') }),
      body: z.object({ status: z.enum(['preparing', 'ready', 'completed']) }),
      errors: [404, 409], example: { orderId: 12, userId: 3, status: 'preparing' },
      handler: async ({ params, body }) => {
        const [order] = await db.execute('sp_Order_UpdateStatus', {
          OrderId: { type: sql.Int, value: params.id },
          Status: { type: sql.NVarChar(20), value: body.status },
        });
        notifyUser(order, 'Cập nhật đơn hàng', `Đơn #${order.orderId} ${STATUS_LABEL[order.status]}`);
        notifyStaff('order:updated', { orderId: order.orderId, status: order.status });
        await cache.delPrefix('order:report:');
        return order;
      },
    },
    {
      method: 'post', path: '/orders/:id/staff-cancel', tags: ['Staff - Orders'], auth: ['staff'], status: 200,
      summary: 'Nhân viên hủy đơn kèm lý do', description: 'US-S07. Chỉ đơn pending/preparing; hoàn tồn kho; khách nhận thông báo kèm lý do.',
      params: z.object({ id: id('Mã đơn') }),
      body: z.object({ reason: z.string().trim().min(3, 'Nhập lý do hủy').max(200) }),
      errors: [404, 409], example: { orderId: 12, userId: 3, status: 'cancelled', cancelReason: 'Hết nguyên liệu' },
      handler: async ({ params, body }) => {
        const [order] = await db.execute('sp_Order_CancelByStaff', {
          OrderId: { type: sql.Int, value: params.id },
          Reason: { type: sql.NVarChar(200), value: body.reason },
        });
        notifyUser(order, 'Đơn hàng bị hủy', `Đơn #${order.orderId} đã bị hủy: ${order.cancelReason}`);
        notifyStaff('order:updated', { orderId: order.orderId, status: order.status });
        background('Xóa cache tồn kho', productIdsOf(order.orderId).then(refreshStock));
        await cache.delPrefix('order:report:');
        return order;
      },
    },

    // ---------- Báo cáo ----------
    {
      method: 'get', path: '/reports/revenue', tags: ['Reports'], auth: ['staff'],
      summary: 'Doanh thu theo ngày', description: 'US-S08, US-A05. Mặc định hôm nay. Không tính đơn hủy.',
      query: range, example: [{ day: '2026-10-30', orderCount: 42, revenue: 1580000 }],
      handler: ({ query }, _req, res) =>
        report(res, `revenue:${query.from}:${query.to}`, () =>
          db.execute('sp_Report_RevenueByDay', {
            FromDate: { type: sql.Date, value: sqlDate(query.from) },
            ToDate: { type: sql.Date, value: sqlDate(query.to) },
          }),
        ),
    },
    {
      method: 'get', path: '/reports/top-products', tags: ['Reports'], auth: ['staff'],
      summary: 'Món bán chạy',
      query: topRange,
      example: [{ id: 1, name: 'Cơm gà xối mỡ', quantity: 18, revenue: 630000 }],
      handler: ({ query }, _req, res) =>
        report(res, `top:${query.from}:${query.to}:${query.top}`, () =>
          db.execute('sp_Report_TopProducts', {
            FromDate: { type: sql.Date, value: sqlDate(query.from) },
            ToDate: { type: sql.Date, value: sqlDate(query.to) },
            Top: { type: sql.Int, value: query.top },
          }),
        ),
    },
    {
      method: 'get', path: '/reports/order-status', tags: ['Reports'], auth: ['staff'],
      summary: 'Số đơn theo trạng thái và tỉ lệ', description: 'US-A06.',
      query: range, example: [{ status: 'completed', orderCount: 38, percentage: 90.48 }],
      handler: ({ query }, _req, res) =>
        report(res, `status:${query.from}:${query.to}`, () =>
          db.execute('sp_Report_OrderStatus', {
            FromDate: { type: sql.Date, value: sqlDate(query.from) },
            ToDate: { type: sql.Date, value: sqlDate(query.to) },
          }),
        ),
    },

    // ---------- Đánh giá ----------
    {
      method: 'post', path: '/reviews', tags: ['Reviews'], auth: true,
      summary: 'Đánh giá món của đơn đã nhận', description: 'US-C17. Mỗi món trong một đơn đánh giá một lần; đơn phải completed.',
      body: z.object({
        orderId: id('Mã đơn'),
        productId: id('Mã món'),
        rating: z.number().int().min(1).max(5),
        comment: z.string().trim().max(500).optional(),
      }),
      errors: [404, 409],
      example: { id: 3, orderId: 12, productId: 1, rating: 5, comment: 'Ngon, giao nhanh', createdAt: '2026-10-30T11:00:00.000Z' },
      handler: async ({ user, body }) => {
        const [row] = await db.execute('sp_Review_Create', {
          UserId: { type: sql.Int, value: user.sub },
          OrderId: { type: sql.Int, value: body.orderId },
          ProductId: { type: sql.Int, value: body.productId },
          Rating: { type: sql.TinyInt, value: body.rating },
          Comment: { type: sql.NVarChar(500), value: body.comment || null },
        });
        background('Xóa cache món', callInternal(config.urls.catalog, '/internal/cache/products', { productIds: [body.productId] }));
        return row;
      },
    },
    {
      method: 'get', path: '/reviews', tags: ['Reviews'],
      summary: 'Đánh giá của một món',
      query: z.object({ productId: id('Mã món'), page, pageSize: pageSize(50, 20) }),
      example: [{ id: 3, rating: 5, comment: 'Ngon, giao nhanh', createdAt: '2026-10-30T11:00:00.000Z', userName: 'Nguyễn Văn A', userAvatarUrl: null }],
      handler: ({ query }) =>
        db.execute('sp_Review_GetByProduct', {
          ProductId: { type: sql.Int, value: query.productId },
          Page: { type: sql.Int, value: query.page },
          PageSize: { type: sql.Int, value: query.pageSize },
        }),
    },
  ];
}

createService({
  name: 'order-service',
  port: config.ports.order,
  title: 'LHU Food - Order Service',
  description: 'Đơn hàng (giao dịch chống đặt quá tồn kho), xử lý đơn của nhân viên, báo cáo, đánh giá.',
  tags,
  routes,
});
