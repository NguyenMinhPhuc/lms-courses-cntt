// Nhận ảnh tải lên bằng multer: chỉ JPEG/PNG/WebP, giới hạn dung lượng, tên file do server đặt
// (không dùng tên client gửi lên để tránh trùng hoặc chèn "../"). CSDL chỉ lưu đường dẫn /uploads/....
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const multer = require('multer');
const config = require('./config');
const { badRequest } = require('./errors');

const EXT = { 'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp' };

function imageUpload({ folder, field = 'file', maxMb = 2, namePrefix = () => 'img' }) {
  const dir = path.join(config.uploadDir, folder);
  fs.mkdirSync(dir, { recursive: true });
  const upload = multer({
    storage: multer.diskStorage({
      destination: dir,
      filename: (req, file, cb) =>
        cb(null, `${namePrefix(req)}-${Date.now()}-${crypto.randomBytes(3).toString('hex')}${EXT[file.mimetype]}`),
    }),
    limits: { fileSize: maxMb * 1024 * 1024, files: 1 },
    fileFilter: (_req, file, cb) => cb(null, Boolean(EXT[file.mimetype])),
  }).single(field);

  const middleware = (req, res, next) =>
    upload(req, res, (err) => {
      if (err) return next(err);
      if (!req.file) return next(badRequest('Chỉ nhận ảnh JPEG, PNG hoặc WebP trong trường "' + field + '"'));
      return next();
    });

  return {
    field,
    description: `Ảnh JPEG/PNG/WebP, tối đa ${maxMb} MB`,
    middleware,
    publicUrl: (file) => `/uploads/${folder}/${file.filename}`,
  };
}

module.exports = { imageUpload };
