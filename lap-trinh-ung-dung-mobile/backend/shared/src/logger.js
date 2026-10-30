// Log dạng một dòng JSON để dịch vụ nền trên Windows Server ghi ra file và tìm kiếm dễ dàng.
// Không bao giờ log token, mật khẩu hay nội dung body.
function createLogger(service) {
  const write = (level, msg, extra) => {
    const line = JSON.stringify({ time: new Date().toISOString(), level, service, msg, ...extra });
    (level === 'error' ? console.error : console.log)(line);
  };
  return {
    info: (msg, extra) => write('info', msg, extra),
    warn: (msg, extra) => write('warn', msg, extra),
    error: (msg, extra) => write('error', msg, extra),
  };
}

module.exports = { createLogger };
