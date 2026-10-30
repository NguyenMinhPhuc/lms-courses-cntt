// JWT: ký, xác thực và middleware phân quyền. Payload { sub: userId, role } giống Chương 6.
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const config = require('./config');
const { unauthorized, forbidden } = require('./errors');

const ROLES = ['customer', 'staff', 'admin'];

const signAccessToken = (user) =>
  jwt.sign({ sub: user.userId, role: user.role }, config.jwt.secret, { expiresIn: config.jwt.expiresIn });

const signRefreshToken = (user) =>
  jwt.sign({ sub: user.userId, role: user.role, jti: crypto.randomUUID() }, config.jwt.refreshSecret, {
    expiresIn: `${config.jwt.refreshExpiresDays}d`,
  });

const verifyAccessToken = (token) => jwt.verify(token, config.jwt.secret);
const verifyRefreshToken = (token) => jwt.verify(token, config.jwt.refreshSecret);
const sha256 = (value) => crypto.createHash('sha256').update(value).digest('hex');

function readBearer(req) {
  const header = req.headers.authorization || '';
  return header.startsWith('Bearer ') ? header.slice(7).trim() : null;
}

/** Gắn req.user nếu có token hợp lệ; không có token thì bỏ qua (endpoint công khai). */
function optionalAuth(req, _res, next) {
  const token = readBearer(req);
  if (!token) return next();
  try {
    req.user = verifyAccessToken(token);
  } catch {
    req.user = undefined; // endpoint công khai: token hết hạn không làm hỏng request
  }
  return next();
}

/** Bắt buộc đăng nhập. */
function requireAuth(req, _res, next) {
  const token = readBearer(req);
  if (!token) return next(unauthorized());
  try {
    req.user = verifyAccessToken(token);
    return next();
  } catch (err) {
    return next(unauthorized(err.name === 'TokenExpiredError' ? 'Phiên đăng nhập đã hết hạn' : 'Token không hợp lệ'));
  }
}

/** Bắt buộc một trong các vai trò. Quản lý (admin) có mọi quyền của nhân viên (staff). */
function requireRoles(roles) {
  const allowed = new Set(roles);
  if (allowed.has('staff')) allowed.add('admin');
  return (req, _res, next) => {
    if (!req.user) return next(unauthorized());
    if (!allowed.has(req.user.role)) return next(forbidden());
    return next();
  };
}

const isStaff = (user) => user && (user.role === 'staff' || user.role === 'admin');

module.exports = {
  ROLES,
  signAccessToken,
  signRefreshToken,
  verifyAccessToken,
  verifyRefreshToken,
  sha256,
  optionalAuth,
  requireAuth,
  requireRoles,
  isStaff,
};
