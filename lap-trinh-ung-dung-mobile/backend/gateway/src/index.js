// API Gateway: điểm vào duy nhất cho ứng dụng di động và web (EXPO_PUBLIC_API_URL trỏ vào đây).
// - Định tuyến theo tiền tố đường dẫn tới từng microservice (giữ nguyên đường dẫn).
// - REST và Socket.IO dùng chung một địa chỉ, một cổng (Chương 9, Chương 11).
// - Giới hạn tần suất, CORS, request id, chặn /internal/*, gộp Swagger UI (/docs) và health (/health).
const http = require('http');
const crypto = require('crypto');
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const swaggerUi = require('swagger-ui-express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const { config, createLogger, errors } = require('@lhufood/shared');

const logger = createLogger('gateway');

// Bảng định tuyến: tiền tố → service. Thứ tự không quan trọng vì các tiền tố không chồng nhau.
const SERVICES = [
  { name: 'identity', url: config.urls.identity, prefixes: ['/auth', '/users', '/admin/users', '/uploads/avatars'] },
  {
    name: 'catalog',
    url: config.urls.catalog,
    prefixes: ['/categories', '/products', '/counters', '/favorites', '/admin/categories', '/admin/products', '/admin/counters', '/uploads/products'],
  },
  { name: 'order', url: config.urls.order, prefixes: ['/orders', '/reports', '/reviews'] },
  { name: 'notification', url: config.urls.notification, prefixes: ['/notifications', '/socket.io'] },
];

const matches = (path, prefix) => path === prefix || path.startsWith(`${prefix}/`) || path.startsWith(`${prefix}?`);

const app = express();
app.disable('x-powered-by');
app.set('trust proxy', true);
app.use(helmet({ contentSecurityPolicy: false, crossOriginResourcePolicy: { policy: 'cross-origin' } }));
app.use(cors({ origin: config.corsOrigins === '*' ? true : config.corsOrigins.split(',').map((s) => s.trim()) }));

// Request id + log (không đọc body: gateway chuyển nguyên body cho service)
app.use((req, res, next) => {
  req.headers['x-request-id'] = req.headers['x-request-id'] || crypto.randomUUID();
  res.setHeader('x-request-id', req.headers['x-request-id']);
  const start = Date.now();
  res.on('finish', () => {
    if (req.path === '/health') return;
    logger.info('request', { requestId: req.headers['x-request-id'], method: req.method, path: req.path, status: res.statusCode, ms: Date.now() - start });
  });
  next();
});

const tooMany = (req, res) => res.status(429).json(errors.errorBody(429, 'Bạn gửi quá nhiều yêu cầu, vui lòng thử lại sau ít phút'));
app.use(['/auth/login', '/auth/register'], rateLimit({ windowMs: 60_000, limit: config.rateLimit.authPerMinute, standardHeaders: 'draft-7', legacyHeaders: false, handler: tooMany }));
app.use(rateLimit({ windowMs: 60_000, limit: config.rateLimit.perMinute, standardHeaders: 'draft-7', legacyHeaders: false, handler: tooMany, skip: (req) => req.path.startsWith('/socket.io') }));

// Endpoint nội bộ của service không bao giờ được mở ra ngoài
app.use('/internal', (req, res) => res.status(404).json(errors.errorBody(404, 'Không tìm thấy')));

// ---------- Trang chủ, health, tài liệu ----------
app.get('/', (_req, res) =>
  res.json({
    name: 'LHU Food API',
    docs: '/docs',
    health: '/health',
    socket: { path: '/socket.io', auth: '{ token: <accessToken> }' },
    services: SERVICES.map((s) => ({ name: s.name, prefixes: s.prefixes })),
  }),
);

async function fetchJson(url, timeoutMs = 2500) {
  const res = await fetch(url, { signal: AbortSignal.timeout(timeoutMs) });
  return { status: res.status, body: await res.json() };
}

app.get('/health', async (_req, res) => {
  const results = await Promise.all(
    SERVICES.map(async (s) => {
      try {
        const { status, body } = await fetchJson(`${s.url}/health`);
        return [s.name, { status: status === 200 ? 'ok' : 'error', db: body.db, cache: body.cache, ms: body.ms }];
      } catch (err) {
        return [s.name, { status: 'down', error: err.name === 'TimeoutError' ? 'timeout' : err.message }];
      }
    }),
  );
  const services = Object.fromEntries(results);
  const ok = Object.values(services).every((s) => s.status === 'ok');
  res.status(ok ? 200 : 503).json({ status: ok ? 'ok' : 'degraded', time: new Date().toISOString(), services });
});

// Gộp OpenAPI của các service thành một tài liệu; Swagger UI gọi API qua chính gateway
let specCache = { at: 0, spec: null };
async function mergedSpec() {
  if (specCache.spec && Date.now() - specCache.at < 30_000) return specCache.spec;
  const spec = {
    openapi: '3.0.3',
    info: {
      title: 'LHU Food API',
      version: '1.0.0',
      description: [
        'API mẫu của dự án **LHU Food** (SRS), do giảng viên triển khai sẵn cho sinh viên học phần Lập trình ứng dụng di động.',
        '',
        '- Kiến trúc microservice: gateway → identity, catalog, order, notification. Mọi truy cập dữ liệu qua stored procedure trên SQL Server.',
        '- Xác thực: gọi `POST /auth/login`, bấm **Authorize** và dán `accessToken` (không cần chữ Bearer). Access token hết hạn sau 15 phút; dùng `POST /auth/refresh`.',
        '- Lỗi: `{ statusCode, message, error }`; 400 dữ liệu sai, 401 chưa đăng nhập, 403 sai vai trò, 404 không tìm thấy, 409 xung đột nghiệp vụ.',
        '- Realtime: Socket.IO tại cùng địa chỉ, `io(API_URL, { auth: { token }, transports: ["websocket"] })`. Khách nhận `order:status`; nhân viên nhận `order:new`, `order:updated`.',
      ].join('\n'),
    },
    servers: [{ url: '/', description: 'Qua API Gateway' }],
    tags: [],
    paths: {},
    components: {
      securitySchemes: { bearerAuth: { type: 'http', scheme: 'bearer', bearerFormat: 'JWT' } },
    },
  };
  for (const s of SERVICES) {
    try {
      const { body } = await fetchJson(`${s.url}/openapi.json`);
      spec.tags.push(...(body.tags || []).filter((t) => t.name !== 'Internal'));
      for (const [path, ops] of Object.entries(body.paths || {})) {
        if (path.startsWith('/internal')) continue;
        spec.paths[path] = { ...spec.paths[path], ...ops };
      }
    } catch (err) {
      spec.tags.push({ name: `${s.name} (không truy cập được)`, description: err.message });
    }
  }
  specCache = { at: Date.now(), spec };
  return spec;
}

app.get('/openapi.json', async (_req, res) => res.json(await mergedSpec()));
app.use(
  '/docs',
  swaggerUi.serve,
  swaggerUi.setup(null, {
    customSiteTitle: 'LHU Food API',
    swaggerOptions: { url: '/openapi.json', persistAuthorization: true, displayRequestDuration: true },
  }),
);

// ---------- Định tuyến tới microservice ----------
const proxies = SERVICES.map((s) =>
  createProxyMiddleware({
    target: s.url,
    changeOrigin: true,
    ws: s.name === 'notification',
    pathFilter: (path) => s.prefixes.some((p) => matches(path, p)),
    proxyTimeout: 15_000,
    on: {
      error: (err, req, res) => {
        logger.error('Service không phản hồi', { service: s.name, path: req.url, error: err.code || err.message });
        if (res && typeof res.status === 'function' && !res.headersSent) {
          res.status(502).json(errors.errorBody(502, `Dịch vụ ${s.name} tạm thời không phản hồi`));
        } else if (res && typeof res.destroy === 'function') {
          res.destroy(); // kết nối WebSocket
        }
      },
    },
  }),
);
for (const proxy of proxies) app.use(proxy);

app.use((req, res) => res.status(404).json(errors.errorBody(404, `Không có endpoint ${req.method} ${req.path}`)));

const server = http.createServer(app);
// WebSocket (Socket.IO) đi qua cùng cổng với REST
const wsProxy = proxies[SERVICES.findIndex((s) => s.name === 'notification')];
server.on('upgrade', wsProxy.upgrade);

server.listen(config.ports.gateway, '0.0.0.0', () => {
  logger.info(`Gateway chạy tại cổng ${config.ports.gateway}`, { docs: `http://localhost:${config.ports.gateway}/docs` });
});

const shutdown = () => server.close(() => process.exit(0));
process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);
