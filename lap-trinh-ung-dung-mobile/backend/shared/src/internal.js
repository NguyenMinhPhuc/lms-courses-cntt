// Giao tiếp nội bộ giữa các service: HTTP + header x-internal-key. Client bên ngoài không gọi được
// các endpoint /internal/* (gateway không chuyển tiếp chúng và service kiểm tra khóa).
const crypto = require('crypto');
const config = require('./config');
const { forbidden } = require('./errors');

function requireInternalKey(req, _res, next) {
  const key = req.headers['x-internal-key'];
  const ok =
    typeof key === 'string' &&
    key.length === config.internalKey.length &&
    crypto.timingSafeEqual(Buffer.from(key), Buffer.from(config.internalKey));
  return ok ? next() : next(forbidden('Endpoint nội bộ'));
}

/** Gọi endpoint nội bộ của service khác. Lỗi được ném ra để nơi gọi quyết định bỏ qua hay báo lỗi. */
async function callInternal(baseUrl, path, body, { timeoutMs = 3000 } = {}) {
  const res = await fetch(`${baseUrl}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'x-internal-key': config.internalKey },
    body: JSON.stringify(body ?? {}),
    signal: AbortSignal.timeout(timeoutMs),
  });
  if (!res.ok) throw new Error(`${path} trả về ${res.status}`);
  return res.json().catch(() => ({}));
}

module.exports = { requireInternalKey, callInternal };
