// Chạy 5 tiến trình như dịch vụ nền bằng pm2 (npm install -g pm2):
//   pm2 start ecosystem.config.js      khởi động
//   pm2 logs                           xem log
//   pm2 save                           lưu danh sách để tự khởi động lại
// Trên Windows Server, cách đăng ký pm2 (hoặc công cụ khác) thành dịch vụ khởi động cùng máy
// thực hiện theo hướng dẫn của bộ phận hỗ trợ triển khai của Khoa.
const app = (name, script) => ({
  name: `lhufood-${name}`,
  script,
  cwd: __dirname,
  instances: 1,
  autorestart: true,
  max_restarts: 20,
  restart_delay: 2000,
  max_memory_restart: '300M',
  out_file: `logs/${name}.out.log`,
  error_file: `logs/${name}.err.log`,
  time: true,
  env: { NODE_ENV: 'production' },
});

module.exports = {
  apps: [
    app('identity', 'services/identity/src/index.js'),
    app('catalog', 'services/catalog/src/index.js'),
    app('order', 'services/order/src/index.js'),
    app('notification', 'services/notification/src/index.js'),
    app('gateway', 'gateway/src/index.js'),
  ],
};
