// Kiểm thử khói toàn hệ thống qua API Gateway (cần CSDL đã dựng bằng npm run db:setup và 5 tiến trình đang chạy).
//   npm run test:smoke            (mặc định http://localhost:3000)
//   BASE_URL=http://server:3000 npm run test:smoke
// Có tạo dữ liệu thật (một tài khoản thử, vài đơn hàng) nên chỉ chạy trên CSDL phát triển.
const { io } = require('socket.io-client');
require('../shared/src/config');

const BASE = process.env.BASE_URL || `http://localhost:${process.env.GATEWAY_PORT || 3000}`;
const results = [];

async function call(method, path, { token, body, expect } = {}) {
  const res = await fetch(`${BASE}${path}`, {
    method,
    headers: { ...(body ? { 'Content-Type': 'application/json' } : {}), ...(token ? { Authorization: `Bearer ${token}` } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => null);
  if (expect !== undefined && res.status !== expect) {
    throw new Error(`${method} ${path}: mong đợi ${expect}, nhận ${res.status} ${JSON.stringify(data)?.slice(0, 200)}`);
  }
  return { status: res.status, data, headers: res.headers };
}

async function step(name, fn) {
  try {
    const note = await fn();
    results.push({ ok: true, name, note });
    console.log(`  PASS  ${name}${note ? ` (${note})` : ''}`);
  } catch (err) {
    results.push({ ok: false, name, note: err.message });
    console.log(`  FAIL  ${name}\n        ${err.message}`);
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function connectSocket(token) {
  return new Promise((resolve, reject) => {
    const socket = io(BASE, { auth: { token }, transports: ['websocket'], reconnection: false, timeout: 5000 });
    socket.once('connected', () => resolve(socket));
    socket.once('connect_error', (err) => reject(new Error(`Socket: ${err.message}`)));
  });
}

const waitEvent = (socket, event, predicate = () => true, ms = 5000) =>
  new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`Không nhận được ${event} trong ${ms} ms`)), ms);
    const handler = (data) => {
      if (!predicate(data)) return;
      clearTimeout(timer);
      socket.off(event, handler);
      resolve(data);
    };
    socket.on(event, handler);
  });

async function main() {
  console.log(`Smoke test: ${BASE}\n`);
  const ctx = {};

  await step('Gateway /health: mọi service và CSDL ok', async () => {
    const { status, data } = await call('GET', '/health');
    assert(status === 200, JSON.stringify(data));
    return Object.entries(data.services).map(([k, v]) => `${k}:${v.cache}`).join(', ');
  });

  await step('Swagger gộp có đủ endpoint, không lộ /internal', async () => {
    const { data } = await call('GET', '/openapi.json', { expect: 200 });
    const paths = Object.keys(data.paths);
    assert(paths.includes('/auth/login') && paths.includes('/orders/{id}/status') && paths.includes('/notifications'), 'thiếu endpoint');
    assert(!paths.some((p) => p.startsWith('/internal')), 'lộ /internal');
    return `${paths.length} đường dẫn`;
  });

  await step('Đăng nhập khách, nhân viên, quản lý (seed)', async () => {
    const login = async (email, password) => (await call('POST', '/auth/login', { body: { email, password }, expect: 200 })).data;
    ctx.customer = await login(process.env.SEED_CUSTOMER_EMAIL || 'sv@lhufood.local', process.env.SEED_CUSTOMER_PASSWORD || 'Sinhvien@123');
    ctx.staff = await login(process.env.SEED_STAFF_EMAIL || 'staff@lhufood.local', process.env.SEED_STAFF_PASSWORD || 'Staff@123');
    ctx.admin = await login(process.env.SEED_ADMIN_EMAIL || 'admin@lhufood.local', process.env.SEED_ADMIN_PASSWORD || 'Admin@123');
    assert(ctx.customer.role === 'customer' && ctx.staff.role === 'staff' && ctx.admin.role === 'admin', 'sai vai trò');
  });

  await step('Sai mật khẩu → 401 với thông báo chung', async () => {
    const { data } = await call('POST', '/auth/login', { body: { email: 'sv@lhufood.local', password: 'sai-mat-khau' }, expect: 401 });
    assert(data.message === 'Email hoặc mật khẩu không đúng', data.message);
  });

  await step('Đăng ký: dữ liệu sai → 400; email trùng → 409', async () => {
    await call('POST', '/auth/register', { body: { fullName: 'A', email: 'khong-phai-email', password: '123' }, expect: 400 });
    const email = `smoke.${Date.now()}@lhufood.local`;
    await call('POST', '/auth/register', { body: { fullName: 'Smoke Test', email, password: 'Smoke@1234' }, expect: 201 });
    await call('POST', '/auth/register', { body: { fullName: 'Smoke Test', email, password: 'Smoke@1234' }, expect: 409 });
  });

  await step('Danh mục: lần 2 lấy từ cache (X-Cache: HIT)', async () => {
    await call('GET', '/categories', { expect: 200 });
    const { data, headers } = await call('GET', '/categories', { expect: 200 });
    assert(headers.get('x-cache') === 'HIT', `X-Cache=${headers.get('x-cache')}`);
    return `${data.length} danh mục`;
  });

  await step('Món: danh sách, tìm "com ga" không dấu, chi tiết, 404', async () => {
    const { data: list } = await call('GET', '/products?pageSize=50', { expect: 200 });
    assert(Array.isArray(list) && list.length > 0, 'danh sách rỗng');
    ctx.product = list.find((p) => p.stock >= 5);
    assert(ctx.product, 'không có món nào còn ít nhất 5 suất để thử đặt hàng');
    const { data: found } = await call('GET', `/products?keyword=${encodeURIComponent('com ga')}`, { expect: 200 });
    assert(found.some((p) => p.name.includes('Cơm gà')), 'tìm không dấu thất bại');
    const { data: detail } = await call('GET', `/products/${ctx.product.id}`, { expect: 200 });
    assert(detail.id === ctx.product.id && 'avgRating' in detail, 'chi tiết sai');
    await call('GET', '/products/999999', { expect: 404 });
    return `${list.length} món đang bán`;
  });

  await step('Quầy và yêu thích (thêm, liệt kê, bỏ)', async () => {
    const { data: counters } = await call('GET', '/counters', { expect: 200 });
    ctx.counterId = counters[0]?.id;
    const t = ctx.customer.accessToken;
    await call('POST', `/favorites/${ctx.product.id}`, { token: t, expect: 200 });
    const { data: favs } = await call('GET', '/favorites', { token: t, expect: 200 });
    assert(favs.some((f) => f.productId === ctx.product.id), 'không thấy món yêu thích');
    await call('DELETE', `/favorites/${ctx.product.id}`, { token: t, expect: 200 });
  });

  await step('Phân quyền: chưa đăng nhập 401, khách gọi API nhân viên 403', async () => {
    await call('GET', '/orders', { expect: 401 });
    await call('GET', '/orders/staff', { token: ctx.customer.accessToken, expect: 403 });
    await call('GET', '/admin/users', { token: ctx.staff.accessToken, expect: 403 });
  });

  await step('Socket: token sai bị từ chối; khách và nhân viên kết nối được', async () => {
    await connectSocket('token-sai').then(
      (s) => { s.close(); throw new Error('token sai vẫn kết nối được'); },
      () => undefined,
    );
    ctx.customerSocket = await connectSocket(ctx.customer.accessToken);
    ctx.staffSocket = await connectSocket(ctx.staff.accessToken);
  });

  await step('Đặt món: tạo đơn, trừ tồn kho, nhân viên nhận order:new', async () => {
    const before = (await call('GET', `/products/${ctx.product.id}`)).data.stock;
    const newOrder = waitEvent(ctx.staffSocket, 'order:new');
    const { data } = await call('POST', '/orders', {
      token: ctx.customer.accessToken,
      body: { items: [{ productId: ctx.product.id, quantity: 2 }], note: 'Ít cay', counterId: ctx.counterId },
      expect: 201,
    });
    ctx.orderId = data.orderId;
    const event = await newOrder;
    assert(event.orderId === ctx.orderId, 'order:new sai đơn');
    await new Promise((r) => setTimeout(r, 300)); // chờ catalog xóa cache tồn kho
    const after = (await call('GET', `/products/${ctx.product.id}`)).data.stock;
    assert(after === before - 2, `tồn kho ${before} → ${after}`);
    return `đơn #${ctx.orderId}, tồn kho ${before} → ${after}`;
  });

  await step('Đặt quá tồn kho → 409, không tạo đơn', async () => {
    const { data } = await call('POST', '/orders', {
      token: ctx.customer.accessToken,
      body: { items: [{ productId: ctx.product.id, quantity: 50 }] },
    });
    assert(data.statusCode === 409 || data.statusCode === 400, JSON.stringify(data));
    return data.message;
  });

  await step('Nhân viên: danh sách đơn, chuyển preparing → khách nhận order:status', async () => {
    const { data: list } = await call('GET', '/orders/staff', { token: ctx.staff.accessToken, expect: 200 });
    assert(list.some((o) => o.orderId === ctx.orderId), 'không thấy đơn trong danh sách nhân viên');
    const status = waitEvent(ctx.customerSocket, 'order:status', (d) => d.order?.orderId === ctx.orderId);
    await call('PATCH', `/orders/${ctx.orderId}/status`, { token: ctx.staff.accessToken, body: { status: 'preparing' }, expect: 200 });
    const event = await status;
    assert(event.order.status === 'preparing' && event.notification?.id, 'payload thiếu notification');
    return event.notification.body;
  });

  await step('Sai trình tự (preparing → completed) → 409; khách không hủy được nữa → 409', async () => {
    await call('PATCH', `/orders/${ctx.orderId}/status`, { token: ctx.staff.accessToken, body: { status: 'completed' }, expect: 409 });
    await call('POST', `/orders/${ctx.orderId}/cancel`, { token: ctx.customer.accessToken, expect: 409 });
  });

  await step('Hoàn tất đơn: ready → completed; chi tiết đơn đúng', async () => {
    await call('PATCH', `/orders/${ctx.orderId}/status`, { token: ctx.staff.accessToken, body: { status: 'ready' }, expect: 200 });
    await call('PATCH', `/orders/${ctx.orderId}/status`, { token: ctx.staff.accessToken, body: { status: 'completed' }, expect: 200 });
    const { data } = await call('GET', `/orders/${ctx.orderId}`, { token: ctx.customer.accessToken, expect: 200 });
    assert(data.status === 'completed' && data.items.length === 1 && data.total === data.items[0].lineTotal, JSON.stringify(data));
  });

  await step('Đánh giá món của đơn đã nhận; đánh giá lần 2 → 409', async () => {
    const body = { orderId: ctx.orderId, productId: ctx.product.id, rating: 5, comment: 'Smoke test' };
    await call('POST', '/reviews', { token: ctx.customer.accessToken, body, expect: 201 });
    await call('POST', '/reviews', { token: ctx.customer.accessToken, body, expect: 409 });
  });

  await step('Khách hủy đơn pending → hoàn tồn kho', async () => {
    const before = (await call('GET', `/products/${ctx.product.id}`)).data.stock;
    const { data } = await call('POST', '/orders', { token: ctx.customer.accessToken, body: { items: [{ productId: ctx.product.id, quantity: 1 }] }, expect: 201 });
    await call('POST', `/orders/${data.orderId}/cancel`, { token: ctx.customer.accessToken, expect: 200 });
    await new Promise((r) => setTimeout(r, 300));
    const after = (await call('GET', `/products/${ctx.product.id}`)).data.stock;
    assert(after === before, `tồn kho ${before} → ${after}`);
  });

  await step('Lịch sử đơn, thông báo, số chưa đọc, đánh dấu đã đọc', async () => {
    const t = ctx.customer.accessToken;
    const { data: history } = await call('GET', '/orders?page=1', { token: t, expect: 200 });
    assert(Array.isArray(history) && history[0].orderId, 'lịch sử rỗng');
    const { data: list } = await call('GET', '/notifications', { token: t, expect: 200 });
    const { data: count } = await call('GET', '/notifications/unread-count', { token: t, expect: 200 });
    await call('POST', `/notifications/${list[0].id}/read`, { token: t, expect: 200 });
    return `${list.length} thông báo, ${count.unread} chưa đọc`;
  });

  await step('Báo cáo doanh thu, món bán chạy (nhân viên)', async () => {
    const { data } = await call('GET', '/reports/revenue', { token: ctx.staff.accessToken, expect: 200 });
    await call('GET', '/reports/top-products?top=3', { token: ctx.staff.accessToken, expect: 200 });
    return `${data[0]?.orderCount ?? 0} đơn hôm nay`;
  });

  await step('Refresh token xoay vòng: dùng lại token cũ → 401', async () => {
    const old = ctx.customer.refreshToken;
    const { data } = await call('POST', '/auth/refresh', { body: { refreshToken: old }, expect: 200 });
    assert(data.accessToken && data.refreshToken !== old, 'không cấp token mới');
    await call('POST', '/auth/refresh', { body: { refreshToken: old }, expect: 401 });
    await call('POST', '/auth/logout', { body: { refreshToken: data.refreshToken }, expect: 200 });
  });

  await step('Endpoint nội bộ không truy cập được qua gateway', async () => {
    await call('POST', '/internal/notify-staff', { body: { event: 'x' }, expect: 404 });
  });

  ctx.customerSocket?.close();
  ctx.staffSocket?.close();
  const failed = results.filter((r) => !r.ok).length;
  console.log(`\n${results.length - failed}/${results.length} bước đạt`);
  process.exit(failed ? 1 : 0);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
