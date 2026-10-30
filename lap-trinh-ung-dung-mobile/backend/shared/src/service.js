// Khung chung cho mọi microservice: bảo mật cơ bản, log request, /health, /openapi.json, /docs,
// phục vụ ảnh tải lên, xử lý lỗi, tắt êm (graceful shutdown).
const http = require('http');
const crypto = require('crypto');
const path = require('path');
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const config = require('./config');
const db = require('./db');
const { createLogger } = require('./logger');
const { createCache } = require('./cache');
const { buildRoutes } = require('./route');
const { notFoundHandler, createErrorHandler } = require('./errors');

function requestLogger(logger) {
  return (req, res, next) => {
    req.id = req.headers['x-request-id'] || crypto.randomUUID();
    res.setHeader('x-request-id', req.id);
    const start = process.hrtime.bigint();
    res.on('finish', () => {
      if (req.path === '/health') return;
      const ms = Number(process.hrtime.bigint() - start) / 1e6;
      logger.info('request', {
        requestId: req.id,
        method: req.method,
        path: req.originalUrl.split('?')[0],
        status: res.statusCode,
        ms: Math.round(ms),
        userId: req.user?.sub,
      });
    });
    next();
  };
}

function corsOptions() {
  if (config.corsOrigins === '*') return { origin: true };
  return { origin: config.corsOrigins.split(',').map((s) => s.trim()) };
}

function buildOpenApi({ title, description, version = '1.0.0' }, paths, tags) {
  return {
    openapi: '3.0.3',
    info: { title, description, version },
    servers: [{ url: '/' }],
    tags,
    paths,
    components: {
      securitySchemes: {
        bearerAuth: { type: 'http', scheme: 'bearer', bearerFormat: 'JWT' },
        internalKey: { type: 'apiKey', in: 'header', name: 'x-internal-key' },
      },
    },
  };
}

/**
 * options: { name, port, title, description, tags, uploadFolders: ['avatars'],
 *            routes: (deps) => [định nghĩa route], onServer: (server, deps) => void }
 * deps: { db, cache, logger, config }
 */
async function createService(options) {
  const logger = createLogger(options.name);
  if (config.usingDefaultSecrets) {
    logger.warn('Đang dùng khóa bí mật mặc định trong .env.example. Đổi JWT_SECRET, JWT_REFRESH_SECRET, INTERNAL_API_KEY trước khi triển khai.');
  }
  const cache = await createCache(logger);
  const deps = { db, cache, logger, config };

  const app = express();
  app.disable('x-powered-by');
  app.set('trust proxy', true);
  app.use(helmet({ contentSecurityPolicy: false, crossOriginResourcePolicy: { policy: 'cross-origin' } }));
  app.use(cors(corsOptions()));
  app.use(express.json({ limit: '1mb' }));
  app.use(requestLogger(logger));

  for (const folder of options.uploadFolders || []) {
    app.use(`/uploads/${folder}`, express.static(path.join(config.uploadDir, folder), { maxAge: '7d', fallthrough: false }));
  }

  app.get('/health', async (_req, res) => {
    const started = Date.now();
    try {
      await db.execute('sp_Health_Check');
      res.json({ status: 'ok', service: options.name, db: 'ok', cache: cache.kind, ms: Date.now() - started });
    } catch (err) {
      logger.error('Health check lỗi CSDL', { error: err.message });
      res.status(503).json({ status: 'error', service: options.name, db: 'error', cache: cache.kind });
    }
  });

  const { router, paths } = buildRoutes(options.routes(deps));
  const spec = buildOpenApi(options, paths, options.tags);
  app.get('/openapi.json', (_req, res) => res.json(spec));
  app.use('/docs', swaggerUi.serve, swaggerUi.setup(spec, { customSiteTitle: options.title }));
  app.use(router);
  app.use(notFoundHandler);
  app.use(createErrorHandler(logger));

  const server = http.createServer(app);
  if (options.onServer) options.onServer(server, deps);

  await new Promise((resolve) => server.listen(options.port, '0.0.0.0', resolve));
  logger.info(`${options.name} chạy tại cổng ${options.port}`, { docs: `http://localhost:${options.port}/docs`, cache: cache.kind });

  // Kết nối CSDL sớm để báo lỗi cấu hình ngay khi khởi động (không dừng service nếu CSDL chưa sẵn sàng)
  db.getPool().catch((err) => logger.error('Chưa kết nối được SQL Server', { error: err.message, server: config.db.server }));

  const shutdown = async (signal) => {
    logger.info(`Nhận ${signal}, đang tắt`);
    server.close();
    await Promise.allSettled([db.closePool(), cache.close()]);
    process.exit(0);
  };
  process.on('SIGINT', () => shutdown('SIGINT'));
  process.on('SIGTERM', () => shutdown('SIGTERM'));

  return { app, server, deps };
}

module.exports = { createService };
