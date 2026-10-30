// catalog-service: danh mục, món, quầy, yêu thích, quản trị thực đơn (SRS M02, M05, M06, F09.3, F11.1–F11.3).
// Dữ liệu đọc nhiều (thực đơn, quầy) đi qua caching layer; mọi thao tác ghi xóa cache liên quan.
const { createService, config, sql, z, schemas, auth, requireInternalKey, imageUpload } = require('@lhufood/shared');

const { id, page, pageSize, booleanish } = schemas;
const TTL = { categories: 300, counters: 300, products: 30, product: 30 };

const tags = [
  { name: 'Categories', description: 'Danh mục món (F02.1)' },
  { name: 'Products', description: 'Thực đơn, tìm kiếm, chi tiết; nhân viên bật/tắt món và cập nhật tồn kho (F02.2–F02.4, F09.3)' },
  { name: 'Counters', description: 'Quầy nhận món và tọa độ cho bản đồ (F06.1)' },
  { name: 'Favorites', description: 'Món yêu thích của khách hàng (F05.1, F05.2)' },
  { name: 'Admin - Catalog', description: 'Quản trị danh mục, món, quầy (F11.1–F11.3), chỉ quản lý' },
  { name: 'Internal', description: 'Endpoint nội bộ giữa các service, cần header x-internal-key' },
];

const productImage = imageUpload({ folder: 'products', maxMb: 5, namePrefix: (req) => `p${Number.parseInt(req.params.id, 10) || 0}` });

const productExample = {
  id: 1, categoryId: 1, categoryName: 'Cơm', name: 'Cơm gà xối mỡ', description: 'Đùi gà chiên giòn, cơm chiên, dưa leo',
  price: 35000, imageUrl: null, isAvailable: true, stock: 40,
};
const counterExample = { id: 1, name: 'Căn tin cơ sở 1', description: 'Tầng trệt, gần cổng chính', lat: 10.946915, lng: 106.82429, isActive: true };

function routes({ db, cache }) {
  const sendCached = async (res, key, ttl, loader) => {
    const { value, hit } = await cache.wrap(key, ttl, loader);
    res.setHeader('X-Cache', hit ? 'HIT' : 'MISS');
    return value;
  };
  const invalidateMenu = () => Promise.all([cache.delPrefix('catalog:products'), cache.delPrefix('catalog:product:'), cache.del('catalog:categories')]);
  const invalidateProduct = (productId) => Promise.all([cache.delPrefix('catalog:products'), cache.del(`catalog:product:${productId}`)]);
  const invalidateCounters = () => cache.delPrefix('catalog:counters');
  const getProduct = (productId) => db.execute('sp_Product_GetById', { ProductId: { type: sql.Int, value: productId } }).then((r) => r[0]);

  const productBody = z.object({
    categoryId: id('Mã danh mục'),
    name: z.string().trim().min(2).max(150),
    description: z.string().trim().max(500).optional(),
    price: z.number().int().min(0, 'Giá không được âm').max(10_000_000),
  });
  const counterBody = z.object({
    name: z.string().trim().min(2).max(100),
    description: z.string().trim().max(200).optional(),
    lat: z.number().min(-90).max(90),
    lng: z.number().min(-180).max(180),
  });

  return [
    // ---------- Danh mục ----------
    {
      method: 'get', path: '/categories', tags: ['Categories'],
      summary: 'Danh sách danh mục (có cache)',
      example: [{ id: 1, name: 'Cơm', sortOrder: 1, productCount: 4 }],
      handler: (_ctx, _req, res) => sendCached(res, 'catalog:categories', TTL.categories, () => db.execute('sp_Category_GetList')),
    },

    // ---------- Món ----------
    {
      method: 'get', path: '/products', tags: ['Products'], optionalAuth: true,
      summary: 'Danh sách món, lọc danh mục, tìm kiếm, phân trang (có cache)',
      description:
        'US-G01, US-G02. Trả về **mảng** món (tương thích Chương 5). Hết trang khi số phần tử < pageSize. ' +
        'Tìm kiếm không phân biệt hoa thường và dấu ("com ga" tìm được "Cơm gà"). ' +
        '`includeUnavailable=true` chỉ có tác dụng với token nhân viên/quản lý.',
      query: z.object({
        categoryId: id('Mã danh mục').optional(),
        keyword: z.string().trim().max(100).optional().describe('Từ khóa tìm theo tên món'),
        includeUnavailable: booleanish.optional().describe('Nhân viên xem cả món ngừng bán'),
        page,
        pageSize: pageSize(100, 20),
      }),
      example: [productExample],
      handler: (ctx, _req, res) => {
        const q = ctx.query;
        const includeUnavailable = Boolean(q.includeUnavailable && auth.isStaff(ctx.user));
        const keyword = q.keyword || null;
        const key = `catalog:products:${q.categoryId ?? ''}:${keyword ?? ''}:${includeUnavailable ? 1 : 0}:${q.page}:${q.pageSize}`;
        return sendCached(res, key, TTL.products, () =>
          db.execute('sp_Product_GetList', {
            CategoryId: { type: sql.Int, value: q.categoryId ?? null },
            Keyword: { type: sql.NVarChar(100), value: keyword },
            IncludeUnavailable: { type: sql.Bit, value: includeUnavailable },
            Page: { type: sql.Int, value: q.page },
            PageSize: { type: sql.Int, value: q.pageSize },
          }),
        );
      },
    },
    {
      method: 'get', path: '/products/:id', tags: ['Products'],
      summary: 'Chi tiết món (có cache)', description: 'US-G03. Gồm tồn kho, điểm đánh giá trung bình.',
      params: z.object({ id: id('Mã món') }), errors: [404],
      example: { ...productExample, avgRating: 4.5, reviewCount: 12 },
      handler: ({ params }, _req, res) => sendCached(res, `catalog:product:${params.id}`, TTL.product, () => getProduct(params.id)),
    },
    {
      method: 'patch', path: '/products/:id/availability', tags: ['Products'], auth: ['staff'],
      summary: 'Bật/tắt món còn bán (nhân viên)', description: 'US-S04.',
      params: z.object({ id: id('Mã món') }), body: z.object({ isAvailable: booleanish }), errors: [404],
      example: { id: 13, isAvailable: false, stock: 0 },
      handler: async ({ params, body }) => {
        const [row] = await db.execute('sp_Product_SetAvailability', {
          ProductId: { type: sql.Int, value: params.id },
          IsAvailable: { type: sql.Bit, value: body.isAvailable },
        });
        await invalidateMenu();
        return row;
      },
    },
    {
      method: 'patch', path: '/products/:id/stock', tags: ['Products'], auth: ['staff'],
      summary: 'Cập nhật số suất còn lại (nhân viên)', description: 'US-S05.',
      params: z.object({ id: id('Mã món') }),
      body: z.object({ stock: z.number().int().min(0, 'Tồn kho không được âm').max(100000) }), errors: [404],
      example: { id: 1, isAvailable: true, stock: 50 },
      handler: async ({ params, body }) => {
        const [row] = await db.execute('sp_Product_UpdateStock', {
          ProductId: { type: sql.Int, value: params.id },
          Stock: { type: sql.Int, value: body.stock },
        });
        await invalidateProduct(params.id);
        return row;
      },
    },

    // ---------- Quầy ----------
    {
      method: 'get', path: '/counters', tags: ['Counters'],
      summary: 'Danh sách quầy đang hoạt động (có cache)', description: 'US-G06. Trả lat/lng cho bản đồ (Chương 8).',
      example: [counterExample],
      handler: (_ctx, _req, res) =>
        sendCached(res, 'catalog:counters:active', TTL.counters, () =>
          db.execute('sp_Counter_GetList', { IncludeInactive: { type: sql.Bit, value: false } }),
        ),
    },

    // ---------- Yêu thích ----------
    {
      method: 'get', path: '/favorites', tags: ['Favorites'], auth: true,
      summary: 'Món yêu thích của tôi',
      example: [{ productId: 5, name: 'Bún bò Huế', price: 40000, imageUrl: null, isAvailable: true, createdAt: '2026-10-30T08:00:00.000Z' }],
      handler: ({ user }) => db.execute('sp_Favorite_GetList', { UserId: { type: sql.Int, value: user.sub } }),
    },
    {
      method: 'post', path: '/favorites/:productId', tags: ['Favorites'], auth: true, status: 200,
      summary: 'Thêm món yêu thích', description: 'Thêm lần hai không lỗi.',
      params: z.object({ productId: id('Mã món') }), errors: [404], example: { success: true },
      handler: async ({ user, params }) => {
        await db.execute('sp_Favorite_Add', {
          UserId: { type: sql.Int, value: user.sub },
          ProductId: { type: sql.Int, value: params.productId },
        });
        return { success: true };
      },
    },
    {
      method: 'delete', path: '/favorites/:productId', tags: ['Favorites'], auth: true,
      summary: 'Bỏ món yêu thích', params: z.object({ productId: id('Mã món') }), example: { success: true },
      handler: async ({ user, params }) => {
        await db.execute('sp_Favorite_Remove', {
          UserId: { type: sql.Int, value: user.sub },
          ProductId: { type: sql.Int, value: params.productId },
        });
        return { success: true };
      },
    },

    // ---------- Quản trị ----------
    {
      method: 'post', path: '/admin/categories', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Thêm danh mục',
      body: z.object({ name: z.string().trim().min(2).max(100), sortOrder: z.number().int().min(0).default(0) }),
      errors: [409], example: { id: 6, name: 'Chè', sortOrder: 6 },
      handler: async ({ body }) => {
        const [row] = await db.execute('sp_Category_Create', {
          Name: { type: sql.NVarChar(100), value: body.name },
          SortOrder: { type: sql.Int, value: body.sortOrder },
        });
        await invalidateMenu();
        return row;
      },
    },
    {
      method: 'put', path: '/admin/categories/:id', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Sửa danh mục', params: z.object({ id: id('Mã danh mục') }),
      body: z.object({ name: z.string().trim().min(2).max(100), sortOrder: z.number().int().min(0).default(0) }),
      errors: [404, 409], example: { id: 6, name: 'Chè - Tráng miệng', sortOrder: 6 },
      handler: async ({ params, body }) => {
        const [row] = await db.execute('sp_Category_Update', {
          CategoryId: { type: sql.Int, value: params.id },
          Name: { type: sql.NVarChar(100), value: body.name },
          SortOrder: { type: sql.Int, value: body.sortOrder },
        });
        await invalidateMenu();
        return row;
      },
    },
    {
      method: 'delete', path: '/admin/categories/:id', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Xóa danh mục (chỉ khi không còn món)', params: z.object({ id: id('Mã danh mục') }),
      errors: [404, 409], example: { success: true },
      handler: async ({ params }) => {
        await db.execute('sp_Category_Delete', { CategoryId: { type: sql.Int, value: params.id } });
        await invalidateMenu();
        return { success: true };
      },
    },
    {
      method: 'post', path: '/admin/products', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Thêm món',
      body: productBody.extend({
        stock: z.number().int().min(0).default(0),
        isAvailable: z.boolean().default(true),
      }),
      errors: [404], example: productExample,
      handler: async ({ body }) => {
        const [row] = await db.execute('sp_Product_Create', {
          CategoryId: { type: sql.Int, value: body.categoryId },
          Name: { type: sql.NVarChar(150), value: body.name },
          Description: { type: sql.NVarChar(500), value: body.description ?? null },
          Price: { type: sql.Decimal(12, 0), value: body.price },
          Stock: { type: sql.Int, value: body.stock },
          IsAvailable: { type: sql.Bit, value: body.isAvailable },
        });
        await invalidateMenu();
        return row;
      },
    },
    {
      method: 'put', path: '/admin/products/:id', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Sửa món (tên, mô tả, giá, danh mục)',
      description: 'Ngừng bán dùng PATCH /products/{id}/availability; món đã có trong đơn không xóa hẳn (BR-16).',
      params: z.object({ id: id('Mã món') }), body: productBody, errors: [404], example: productExample,
      handler: async ({ params, body }) => {
        const [row] = await db.execute('sp_Product_Update', {
          ProductId: { type: sql.Int, value: params.id },
          CategoryId: { type: sql.Int, value: body.categoryId },
          Name: { type: sql.NVarChar(150), value: body.name },
          Description: { type: sql.NVarChar(500), value: body.description ?? null },
          Price: { type: sql.Decimal(12, 0), value: body.price },
        });
        await invalidateMenu();
        return row;
      },
    },
    {
      method: 'post', path: '/admin/products/:id/image', tags: ['Admin - Catalog'], auth: ['admin'], status: 200,
      summary: 'Tải ảnh món (multipart, trường "file")',
      params: z.object({ id: id('Mã món') }), upload: productImage, errors: [404, 413],
      example: { id: 1, imageUrl: '/uploads/products/p1-1730275200000-a1b2c3.jpg' },
      handler: async ({ params, file }) => {
        const [row] = await db.execute('sp_Product_UpdateImage', {
          ProductId: { type: sql.Int, value: params.id },
          ImageUrl: { type: sql.NVarChar(500), value: productImage.publicUrl(file) },
        });
        await invalidateProduct(params.id);
        return row;
      },
    },
    {
      method: 'get', path: '/admin/counters', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Tất cả quầy, kể cả ngừng hoạt động', example: [counterExample],
      handler: () => db.execute('sp_Counter_GetList', { IncludeInactive: { type: sql.Bit, value: true } }),
    },
    {
      method: 'post', path: '/admin/counters', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Thêm quầy', body: counterBody, example: counterExample,
      handler: async ({ body }) => {
        const [row] = await db.execute('sp_Counter_Create', {
          Name: { type: sql.NVarChar(100), value: body.name },
          Description: { type: sql.NVarChar(200), value: body.description ?? null },
          Latitude: { type: sql.Decimal(9, 6), value: body.lat },
          Longitude: { type: sql.Decimal(9, 6), value: body.lng },
        });
        await invalidateCounters();
        return row;
      },
    },
    {
      method: 'put', path: '/admin/counters/:id', tags: ['Admin - Catalog'], auth: ['admin'],
      summary: 'Sửa quầy', params: z.object({ id: id('Mã quầy') }),
      body: counterBody.extend({ isActive: z.boolean().default(true) }), errors: [404], example: counterExample,
      handler: async ({ params, body }) => {
        const [row] = await db.execute('sp_Counter_Update', {
          CounterId: { type: sql.Int, value: params.id },
          Name: { type: sql.NVarChar(100), value: body.name },
          Description: { type: sql.NVarChar(200), value: body.description ?? null },
          Latitude: { type: sql.Decimal(9, 6), value: body.lat },
          Longitude: { type: sql.Decimal(9, 6), value: body.lng },
          IsActive: { type: sql.Bit, value: body.isActive },
        });
        await invalidateCounters();
        return row;
      },
    },

    // ---------- Nội bộ ----------
    {
      method: 'post', path: '/internal/cache/products', tags: ['Internal'], internal: requireInternalKey, status: 200,
      summary: 'Xóa cache món (order-service gọi khi tồn kho thay đổi)',
      body: z.object({ productIds: z.array(z.number().int().positive()).default([]) }),
      example: { success: true },
      handler: async ({ body }) => {
        await Promise.all([cache.delPrefix('catalog:products'), ...body.productIds.map((pid) => cache.del(`catalog:product:${pid}`))]);
        return { success: true };
      },
    },
  ];
}

createService({
  name: 'catalog-service',
  port: config.ports.catalog,
  title: 'LHU Food - Catalog Service',
  description: 'Thực đơn, quầy, yêu thích, quản trị thực đơn. Dữ liệu đọc nhiều có cache (header X-Cache: HIT/MISS).',
  tags,
  uploadFolders: ['products'],
  routes,
});
