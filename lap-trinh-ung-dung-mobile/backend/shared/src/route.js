// Khai báo route một lần, sinh ra cả Express router (kèm kiểm tra dữ liệu bằng Zod, phân quyền)
// và tài liệu OpenAPI cho Swagger UI. Mỗi service chỉ viết mảng định nghĩa route.
const express = require('express');
const { z } = require('zod');
const { optionalAuth, requireAuth, requireRoles } = require('./auth');
const { HttpError } = require('./errors');

const asyncHandler = (fn) => (req, res, next) => Promise.resolve(fn(req, res, next)).catch(next);

// io 'input': schema của dữ liệu client gửi (trường có default là không bắt buộc);
// 'output' cho tham số đường dẫn/query để z.coerce.number() hiện đúng kiểu number.
const toJsonSchema = (schema, io = 'input') => {
  const json = z.toJSONSchema(schema, { target: 'openapi-3.0', io, unrepresentable: 'any' });
  delete json.$schema;
  return json;
};

/** Thông báo lỗi Zod → mảng chuỗi tiếng Việt kiểu NestJS ValidationPipe. */
function zodMessages(error) {
  return error.issues.map((i) => (i.path.length ? `${i.path.join('.')}: ${i.message}` : i.message));
}

function parse(schema, data) {
  if (!schema) return data;
  const result = schema.safeParse(data ?? {});
  if (!result.success) throw new HttpError(400, 'Dữ liệu không hợp lệ', zodMessages(result.error));
  return result.data;
}

function parameters(schema, location) {
  if (!schema) return [];
  return Object.entries(schema.shape).map(([name, field]) => ({
    name,
    in: location,
    // không bắt buộc khi trường optional hoặc có default (undefined vẫn hợp lệ)
    required: location === 'path' ? true : !field.safeParse(undefined).success,
    description: field.description,
    schema: toJsonSchema(field, 'output'),
  }));
}

const ERROR_RESPONSES = {
  400: 'Dữ liệu không hợp lệ (mã 50400 từ thủ tục hoặc lỗi kiểm tra Zod)',
  401: 'Chưa đăng nhập hoặc token hết hạn',
  403: 'Không đủ quyền theo vai trò',
  404: 'Không tìm thấy (mã 50404)',
  409: 'Xung đột nghiệp vụ (mã 50409)',
};

function openapiOperation(def) {
  const op = {
    tags: def.tags,
    summary: def.summary,
    description: def.description,
    parameters: [...parameters(def.params, 'path'), ...parameters(def.query, 'query')],
    responses: {
      [def.status || (def.method === 'post' ? 201 : 200)]: {
        description: 'Thành công',
        ...(def.example !== undefined ? { content: { 'application/json': { example: def.example } } } : {}),
      },
    },
  };
  if (def.auth) op.security = [{ bearerAuth: [] }];
  if (def.internal) op.security = [{ internalKey: [] }];
  if (def.body) {
    op.requestBody = { required: true, content: { 'application/json': { schema: toJsonSchema(def.body) } } };
  }
  if (def.upload) {
    op.requestBody = {
      required: true,
      content: {
        'multipart/form-data': {
          schema: {
            type: 'object',
            required: [def.upload.field],
            properties: { [def.upload.field]: { type: 'string', format: 'binary', description: def.upload.description } },
          },
        },
      },
    };
  }
  const codes = new Set([400]);
  if (def.auth) codes.add(401);
  if (Array.isArray(def.auth)) codes.add(403);
  for (const c of def.errors || []) codes.add(c);
  for (const c of [...codes].sort()) op.responses[c] = { description: ERROR_RESPONSES[c] };
  return op;
}

/**
 * def: {
 *   method, path ('/products/:id'), summary, description, tags,
 *   auth: false | true | ['staff'] (vai trò), optionalAuth: true,
 *   params, query, body: zod object, upload: { field, middleware },
 *   internal: middleware khóa nội bộ, status, example, errors: [404, 409],
 *   handler: async (ctx, req, res) => giá trị trả về (JSON)
 * }
 * ctx = { params, query, body, user, file }
 */
function buildRoutes(defs) {
  const router = express.Router();
  const paths = {};

  for (const def of defs) {
    const chain = [];
    if (def.internal) chain.push(def.internal);
    if (def.auth) chain.push(requireAuth);
    else if (def.optionalAuth) chain.push(optionalAuth);
    if (Array.isArray(def.auth)) chain.push(requireRoles(def.auth));
    if (def.upload) chain.push(def.upload.middleware);

    chain.push(
      asyncHandler(async (req, res) => {
        const ctx = {
          params: parse(def.params, req.params),
          query: parse(def.query, req.query),
          body: parse(def.body, req.body),
          user: req.user,
          file: req.file,
        };
        const value = await def.handler(ctx, req, res);
        if (res.headersSent) return;
        res.status(def.status || (def.method === 'post' ? 201 : 200)).json(value ?? { success: true });
      }),
    );
    router[def.method](def.path, ...chain);

    if (!def.hidden) {
      const openPath = def.path.replace(/:(\w+)/g, '{$1}');
      paths[openPath] = paths[openPath] || {};
      paths[openPath][def.method] = openapiOperation(def);
    }
  }
  return { router, paths };
}

// Các schema hay dùng
const id = (label = 'Mã') => z.coerce.number({ error: `${label} phải là số` }).int(`${label} phải là số nguyên`).positive(`${label} phải lớn hơn 0`);
const page = z.coerce.number().int().min(1).default(1).describe('Trang, bắt đầu từ 1');
const pageSize = (max = 100, def = 20) => z.coerce.number().int().min(1).max(max).default(def).describe('Số dòng mỗi trang');
const dateString = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, 'Định dạng ngày YYYY-MM-DD');
const booleanish = z
  .union([z.boolean(), z.enum(['true', 'false', '1', '0'])])
  .transform((v) => v === true || v === 'true' || v === '1');

module.exports = { z, buildRoutes, asyncHandler, schemas: { id, page, pageSize, dateString, booleanish } };
