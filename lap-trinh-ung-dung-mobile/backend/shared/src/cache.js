// Caching layer: Redis khi có REDIS_URL (dùng chung giữa các service, xóa cache của nhau được),
// ngược lại cache trong bộ nhớ của từng service. Cùng một giao diện: get / set / del / delPrefix / wrap.
const config = require('./config');

function createMemoryStore({ maxEntries = 5000 } = {}) {
  const map = new Map();
  const timer = setInterval(() => {
    const now = Date.now();
    for (const [key, entry] of map) if (entry.expires <= now) map.delete(key);
  }, 60_000);
  timer.unref();
  return {
    kind: 'memory',
    async get(key) {
      const entry = map.get(key);
      if (!entry) return undefined;
      if (entry.expires <= Date.now()) {
        map.delete(key);
        return undefined;
      }
      return entry.value;
    },
    async set(key, value, ttlSeconds) {
      if (map.size >= maxEntries) map.delete(map.keys().next().value); // bỏ mục cũ nhất
      map.set(key, { value, expires: Date.now() + ttlSeconds * 1000 });
    },
    async del(key) {
      map.delete(key);
    },
    async delPrefix(prefix) {
      for (const key of map.keys()) if (key.startsWith(prefix)) map.delete(key);
    },
    async close() {
      clearInterval(timer);
    },
  };
}

async function createRedisStore(url, logger) {
  const { createClient } = require('redis');
  const client = createClient({ url, socket: { reconnectStrategy: (n) => Math.min(n * 200, 5000) } });
  client.on('error', (err) => logger.warn('Redis lỗi', { error: err.message }));
  await client.connect();
  return {
    kind: 'redis',
    async get(key) {
      const raw = await client.get(key);
      return raw === null ? undefined : JSON.parse(raw);
    },
    async set(key, value, ttlSeconds) {
      await client.set(key, JSON.stringify(value), { EX: ttlSeconds });
    },
    async del(key) {
      await client.del(key);
    },
    async delPrefix(prefix) {
      for await (const keys of client.scanIterator({ MATCH: `${prefix}*`, COUNT: 200 })) {
        const batch = Array.isArray(keys) ? keys : [keys];
        if (batch.length) await client.del(batch);
      }
    },
    async close() {
      await client.quit();
    },
  };
}

/**
 * Tạo cache cho một service. Khóa luôn có tiền tố "lhufood:" để không đụng dữ liệu khác trong Redis.
 * Lỗi cache không bao giờ làm hỏng request: lỗi thì coi như không có cache.
 */
async function createCache(logger) {
  let store;
  if (config.cache.redisUrl) {
    try {
      store = await createRedisStore(config.cache.redisUrl, logger);
    } catch (err) {
      logger.warn('Không kết nối được Redis, dùng cache bộ nhớ', { error: err.message });
    }
  }
  store = store || createMemoryStore();
  const k = (key) => `lhufood:${key}`;
  const stats = { hits: 0, misses: 0 };

  const safe = async (fn, fallback) => {
    try {
      return await fn();
    } catch (err) {
      logger.warn('Cache lỗi', { error: err.message });
      return fallback;
    }
  };

  return {
    kind: store.kind,
    stats,
    get: (key) => safe(() => store.get(k(key)), undefined),
    set: (key, value, ttl = config.cache.ttlSeconds) => safe(() => store.set(k(key), value, ttl)),
    del: (key) => safe(() => store.del(k(key))),
    delPrefix: (prefix) => safe(() => store.delPrefix(k(prefix))),
    close: () => safe(() => store.close()),
    /** Đọc cache; chưa có thì gọi loader, lưu lại. Trả { value, hit }. */
    async wrap(key, ttl, loader) {
      const cached = await safe(() => store.get(k(key)), undefined);
      if (cached !== undefined) {
        stats.hits += 1;
        return { value: cached, hit: true };
      }
      stats.misses += 1;
      const value = await loader();
      await safe(() => store.set(k(key), value, ttl));
      return { value, hit: false };
    },
  };
}

module.exports = { createCache };
