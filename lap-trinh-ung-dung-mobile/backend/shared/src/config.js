// Cấu hình dùng chung, đọc một lần từ backend/.env (mọi service cùng một file).
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
require('dotenv').config({ path: path.join(ROOT, '.env') });

const env = (name, fallback) => {
  const value = process.env[name];
  return value === undefined || value === '' ? fallback : value;
};
const int = (name, fallback) => Number.parseInt(env(name, String(fallback)), 10);
const bool = (name, fallback) => String(env(name, String(fallback))).toLowerCase() === 'true';

const config = {
  root: ROOT,
  db: {
    server: env('DB_SERVER', 'localhost'),
    port: int('DB_PORT', 1433),
    database: env('DB_NAME', 'LhuFood_Dev'),
    user: env('DB_USER', 'sa'),
    password: env('DB_PASSWORD', ''),
    encrypt: bool('DB_ENCRYPT', false),
    trustServerCertificate: bool('DB_TRUST_SERVER_CERTIFICATE', true),
    adminUser: env('DB_ADMIN_USER', env('DB_USER', 'sa')),
    adminPassword: env('DB_ADMIN_PASSWORD', env('DB_PASSWORD', '')),
  },
  jwt: {
    secret: env('JWT_SECRET', 'change-me-access-secret'),
    refreshSecret: env('JWT_REFRESH_SECRET', 'change-me-refresh-secret'),
    expiresIn: env('JWT_EXPIRES_IN', '15m'),
    refreshExpiresDays: int('JWT_REFRESH_EXPIRES_DAYS', 7),
  },
  internalKey: env('INTERNAL_API_KEY', 'change-me-internal-key'),
  cache: {
    redisUrl: env('REDIS_URL', ''),
    ttlSeconds: int('CACHE_TTL_SECONDS', 60),
  },
  ports: {
    gateway: int('GATEWAY_PORT', 3000),
    identity: int('IDENTITY_PORT', 4001),
    catalog: int('CATALOG_PORT', 4002),
    order: int('ORDER_PORT', 4003),
    notification: int('NOTIFICATION_PORT', 4004),
  },
  urls: {
    identity: env('IDENTITY_URL', 'http://localhost:4001'),
    catalog: env('CATALOG_URL', 'http://localhost:4002'),
    order: env('ORDER_URL', 'http://localhost:4003'),
    notification: env('NOTIFICATION_URL', 'http://localhost:4004'),
  },
  corsOrigins: env('CORS_ORIGINS', '*'),
  rateLimit: {
    perMinute: int('RATE_LIMIT_PER_MINUTE', 300),
    authPerMinute: int('AUTH_RATE_LIMIT_PER_MINUTE', 20),
  },
  uploadDir: path.resolve(ROOT, env('UPLOAD_DIR', './uploads')),
};

const DEFAULT_SECRETS = ['change-me-access-secret', 'change-me-refresh-secret', 'change-me-internal-key'];
config.usingDefaultSecrets = [config.jwt.secret, config.jwt.refreshSecret, config.internalKey].some((s) =>
  DEFAULT_SECRETS.includes(s),
);

module.exports = config;
