// Lỗi HTTP và middleware xử lý lỗi. Định dạng phản hồi giống NestJS ({ statusCode, message, error })
// để mã ứng dụng trong giáo trình (đọc body.message) dùng được nguyên vẹn.
const STATUS_TEXT = {
  400: 'Bad Request',
  401: 'Unauthorized',
  403: 'Forbidden',
  404: 'Not Found',
  409: 'Conflict',
  413: 'Payload Too Large',
  429: 'Too Many Requests',
  500: 'Internal Server Error',
  502: 'Bad Gateway',
  503: 'Service Unavailable',
};

class HttpError extends Error {
  constructor(statusCode, message, details) {
    super(message);
    this.statusCode = statusCode;
    this.details = details;
  }
}

const badRequest = (message, details) => new HttpError(400, message, details);
const unauthorized = (message = 'Bạn cần đăng nhập') => new HttpError(401, message);
const forbidden = (message = 'Bạn không có quyền thực hiện thao tác này') => new HttpError(403, message);
const notFound = (message = 'Không tìm thấy') => new HttpError(404, message);
const conflict = (message) => new HttpError(409, message);

function errorBody(statusCode, message) {
  return { statusCode, message, error: STATUS_TEXT[statusCode] || 'Error' };
}

function notFoundHandler(req, res) {
  res.status(404).json(errorBody(404, `Không có endpoint ${req.method} ${req.path}`));
}

function createErrorHandler(logger) {
  // eslint-disable-next-line no-unused-vars
  return (err, req, res, next) => {
    if (err instanceof HttpError) {
      return res.status(err.statusCode).json(errorBody(err.statusCode, err.details || err.message));
    }
    if (err?.name === 'MulterError') {
      const status = err.code === 'LIMIT_FILE_SIZE' ? 413 : 400;
      const message = err.code === 'LIMIT_FILE_SIZE' ? 'File vượt quá dung lượng cho phép' : err.message;
      return res.status(status).json(errorBody(status, message));
    }
    if (err?.type === 'entity.parse.failed') {
      return res.status(400).json(errorBody(400, 'Body không phải JSON hợp lệ'));
    }
    // Lỗi 4xx của middleware Express (file tĩnh không tồn tại, body quá lớn...)
    const status = err?.status || err?.statusCode;
    if (status >= 400 && status < 500) {
      return res.status(status).json(errorBody(status, status === 404 ? 'Không tìm thấy file' : err.message));
    }
    logger.error('Lỗi không xử lý được', {
      requestId: req.id,
      method: req.method,
      path: req.path,
      error: err?.message,
      sqlNumber: err?.number,
      procedure: err?.procedure,
    });
    return res.status(500).json(errorBody(500, 'Lỗi máy chủ, vui lòng thử lại sau'));
  };
}

module.exports = {
  HttpError,
  badRequest,
  unauthorized,
  forbidden,
  notFound,
  conflict,
  errorBody,
  notFoundHandler,
  createErrorHandler,
};
