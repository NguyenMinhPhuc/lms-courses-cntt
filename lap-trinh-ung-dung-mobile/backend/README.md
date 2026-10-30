# LHU Food Backend (microservice)

Backend mẫu của dự án **LHU Food** theo tài liệu SRS (`../srs/`), do giảng viên triển khai sẵn để sinh viên học phần Lập trình ứng dụng di động (111114) gọi API từ ứng dụng React Native. Endpoint, định dạng dữ liệu và sự kiện Socket.IO khớp với mã nguồn trong giáo trình (Chương 5–11), nên mã sinh viên học trong chương gọi được ngay.

**Công nghệ:** Node.js 20+ (Express) · Microsoft SQL Server 2019+ (chỉ truy cập qua stored procedure, thư viện `mssql`) · JWT (access token + refresh token xoay vòng) · Swagger UI (OpenAPI 3) · caching layer (Redis hoặc bộ nhớ) · API Gateway · Socket.IO.

## 1. Kiến trúc

```text
                Ứng dụng di động / web  (EXPO_PUBLIC_API_URL = http://<server>:3000)
                                │  REST + Socket.IO (cùng địa chỉ, cùng cổng)
                                ▼
┌──────────────────────── API Gateway :3000 ────────────────────────┐
│ định tuyến theo tiền tố · rate limit · CORS · request id          │
│ Swagger gộp /docs · health gộp /health · chặn /internal/*         │
└──────┬──────────────┬───────────────┬──────────────────┬──────────┘
       ▼              ▼               ▼                  ▼
 identity :4001  catalog :4002   order :4003      notification :4004
 /auth /users    /categories     /orders          /notifications
 /admin/users    /products       /reports         /socket.io (realtime)
                 /counters       /reviews
                 /favorites      ── HTTP nội bộ (x-internal-key) ──▶ notification, catalog
                 /admin/...
       └──────────────┴───────┬───────┴──────────────────┘
                              ▼  chỉ gọi stored procedure
                  SQL Server (CSDL LHU Food)      Redis (tùy chọn, cache dùng chung)
```

| Service | Cổng | Trách nhiệm (SRS) | Cache |
|---|---|---|---|
| `gateway` | 3000 | Điểm vào duy nhất, định tuyến, giới hạn tần suất, Swagger/health gộp, chuyển tiếp WebSocket | |
| `identity` | 4001 | M01 Xác thực, M07 hồ sơ và ảnh đại diện, F11.4 quản lý tài khoản | |
| `catalog` | 4002 | M02 Thực đơn, M05 Yêu thích, M06 Quầy, F09.3 món hết hàng/tồn kho, F11.1–F11.3 quản trị | Danh mục, quầy 5 phút; món 30 giây; xóa khi ghi |
| `order` | 4003 | M04 Đơn hàng, M09 xử lý đơn của nhân viên, M10 Báo cáo, F07.4 đánh giá | Báo cáo 60 giây |
| `notification` | 4004 | M08 Thông báo: lưu SQL Server rồi phát Socket.IO | |

Nguyên tắc:

- **Dữ liệu chỉ qua stored procedure** (`database/*.sql`). Mã service không có câu SQL, không dùng ORM. Lỗi nghiệp vụ là `THROW 50400/50404/50409` trong thủ tục, được đổi thành HTTP 400/404/409.
- Các service dùng **chung một CSDL** để đơn giản cho môi trường học tập; mỗi service chỉ gọi thủ tục thuộc phạm vi của mình (tên file `02-procedures-identity.sql`, `03-procedures-catalog.sql`…).
- **Giao tiếp nội bộ** bằng HTTP + header `x-internal-key`. Lỗi ở service khác (ví dụ notification tạm dừng) không làm hỏng đơn hàng đã lưu.
- **Caching layer**: có `REDIS_URL` thì dùng Redis (các service xóa cache của nhau được); không có thì cache bộ nhớ trong từng service. Response có header `X-Cache: HIT|MISS`.

## 2. Cấu trúc thư mục

```text
backend/
├── gateway/src/index.js            API Gateway
├── services/
│   ├── identity/src/index.js
│   ├── catalog/src/index.js
│   ├── order/src/index.js
│   └── notification/src/index.js   REST + Socket.IO
├── shared/                         thư viện dùng chung
│   └── src/ config, db (stored procedure), auth (JWT), cache, route (Zod + OpenAPI), service, upload, internal
├── database/                       01-tables.sql, 02..05-procedures-*.sql, 99-seed.sql
├── scripts/                        db-setup.js, smoke-test.js, check-syntax.js
├── ecosystem.config.js             chạy nền bằng pm2
├── docker-compose.yml              (tùy chọn) SQL Server 2019 + Redis cho máy phát triển
└── .env.example
```

Mỗi route được khai báo một lần (đường dẫn, quyền, schema Zod, ví dụ phản hồi, hàm xử lý); `shared/src/route.js` sinh ra cả Express router (kiểm tra dữ liệu, phân quyền) và tài liệu OpenAPI.

## 3. Chạy trên máy phát triển

Yêu cầu: Node.js 20 trở lên, SQL Server 2019 trở lên (bật SQL Server Authentication và TCP 1433).

```powershell
cd backend
copy .env.example .env        # điền DB_*, đổi JWT_SECRET, JWT_REFRESH_SECRET, INTERNAL_API_KEY
npm install
npm run db:setup              # tạo CSDL, bảng, thủ tục, dữ liệu mẫu, 3 tài khoản mẫu
npm run dev                   # chạy cả 5 tiến trình
```

- Swagger UI: http://localhost:3000/docs · Health: http://localhost:3000/health
- Tài khoản mẫu (đổi trong `.env` trước khi `db:setup`): `admin@lhufood.local`, `staff@lhufood.local`, `sv@lhufood.local`.
- Kiểm thử toàn hệ thống (tạo dữ liệu thật, chỉ chạy trên CSDL phát triển): `npm run test:smoke`.
- Kiểm tra cú pháp: `npm run check`.

`npm run db:setup` chạy lại nhiều lần được. Tài khoản dùng cho bước này phải có quyền tạo bảng, thủ tục (và tạo CSDL nếu chưa có); khai báo riêng bằng `DB_ADMIN_USER`/`DB_ADMIN_PASSWORD` nếu khác tài khoản chạy service.

## 4. Triển khai trên Windows Server của Khoa

1. Cài Node.js LTS; lấy mã nguồn; `npm ci --omit=dev`.
2. Tạo `.env` trên server: khóa bí mật mới (`node -e "console.log(require('crypto').randomBytes(48).toString('hex'))"`), `CORS_ORIGINS` theo địa chỉ web app, `REDIS_URL=redis://<host>:6379` nếu có Redis.
3. Dựng CSDL bằng tài khoản quản trị: `npm run db:setup`.
4. Tạo login cho service chỉ có quyền thực thi thủ tục, rồi đổi `DB_USER`/`DB_PASSWORD` sang login này:
   ```powershell
   $env:DB_API_PASSWORD = "<mật khẩu mạnh>"
   npm run db:setup -- --create-login lhufood_api
   ```
5. Chạy nền bằng pm2 (`npm install -g pm2`, `pm2 start ecosystem.config.js`, `pm2 save`). Đăng ký khởi động cùng Windows theo hướng dẫn của bộ phận hỗ trợ triển khai. Log nằm trong `logs/`.
6. Chỉ mở cổng **3000** (gateway) trên Windows Firewall; các cổng 4001–4004 chỉ dùng nội bộ.
7. Kiểm tra từ máy khác: `http://<server>:3000/health`, `http://<server>:3000/docs`.

Thư mục `uploads/` chứa ảnh tải lên; sao lưu cùng CSDL.

## 5. Dành cho sinh viên: dùng API

**Địa chỉ:** giảng viên cung cấp, ví dụ `EXPO_PUBLIC_API_URL=http://<server>:3000`. Tài liệu đầy đủ, thử trực tiếp: `<địa chỉ>/docs`.

**Xác thực** (Chương 6):

```text
POST /auth/register  { fullName, email, password }                → 201 { userId }
POST /auth/login     { email, password }                          → { accessToken, refreshToken, role, user }
POST /auth/refresh   { refreshToken }                             → { accessToken, refreshToken, role }   (token cũ hết hiệu lực)
POST /auth/logout    { refreshToken }                             → { success: true }
Header cho API cần đăng nhập: Authorization: Bearer <accessToken>   (hết hạn sau 15 phút → 401 → gọi /auth/refresh)
```

**Endpoint chính:**

| Nhóm | Endpoint | Quyền |
|---|---|---|
| Thực đơn | `GET /categories`, `GET /products?categoryId=&keyword=&page=&pageSize=`, `GET /products/:id` | Công khai |
| Quầy | `GET /counters` | Công khai |
| Yêu thích | `GET /favorites`, `POST /favorites/:productId`, `DELETE /favorites/:productId` | Đăng nhập |
| Hồ sơ | `GET /users/me`, `PATCH /users/me`, `POST /users/me/avatar` (multipart, trường `file`) | Đăng nhập |
| Đơn hàng | `POST /orders { items:[{productId,quantity}], note?, counterId? }`, `GET /orders?page=`, `GET /orders/:id`, `POST /orders/:id/cancel` | Đăng nhập |
| Thông báo | `GET /notifications?page=`, `GET /notifications/unread-count`, `POST /notifications/:id/read`, `POST /notifications/read-all` | Đăng nhập |
| Đánh giá | `GET /reviews?productId=`, `POST /reviews { orderId, productId, rating, comment? }` | Công khai / Đăng nhập |
| Nhân viên | `GET /orders/staff?status=`, `PATCH /orders/:id/status { status }`, `POST /orders/:id/staff-cancel { reason }`, `PATCH /products/:id/availability`, `PATCH /products/:id/stock`, `GET /reports/revenue|top-products|order-status?from=&to=` | staff, admin |
| Quản trị | `/admin/users`, `/admin/categories`, `/admin/products`, `/admin/counters` | admin |

- Danh sách (`/products`, `/orders`, `/notifications`) trả **mảng**; hết dữ liệu khi số phần tử ít hơn `pageSize` (mặc định 20), đúng cách cuộn vô hạn ở Chương 5.
- Đường dẫn ảnh (`imageUrl`, `avatarUrl`) là đường dẫn tương đối `/uploads/...`; ghép với địa chỉ API để hiển thị.
- Lỗi luôn có dạng `{ statusCode, message, error }`; `message` là chuỗi tiếng Việt (hoặc mảng chuỗi khi dữ liệu gửi lên sai).

**Realtime** (Chương 9):

```ts
const socket = io(process.env.EXPO_PUBLIC_API_URL!, { auth: { token: accessToken }, transports: ['websocket'] });
socket.on('order:status', ({ order, notification }) => { /* khách: đơn đổi trạng thái */ });
socket.on('order:new', ({ orderId, total }) => { /* nhân viên: có đơn mới */ });
socket.on('order:updated', ({ orderId, status }) => { /* nhân viên: đơn được người khác cập nhật/hủy */ });
```

Token sai hoặc hết hạn bị từ chối khi kết nối (`connect_error`); khi đổi token (sau refresh) cần kết nối lại.

**Quy tắc nghiệp vụ API áp dụng** (SRS mục 6): giá lấy từ CSDL lúc đặt; đặt quá tồn kho trả 409 và không lưu gì; trạng thái đơn chỉ đi `pending → preparing → ready → completed`; khách chỉ hủy được đơn của mình khi `pending`; `userId` luôn lấy từ token.

## 6. Lưu ý vận hành đã kiểm chứng

- **Múi giờ:** thủ tục lưu giờ bằng `SYSDATETIME()` (giờ của SQL Server, như giáo trình); service đọc với `useUTC: false`. Máy chạy service và SQL Server phải cùng múi giờ (UTC+7), khi đó JSON trả về giờ ISO UTC đúng.
- **Tìm kiếm không dấu:** thủ tục dùng `COLLATE Latin1_General_100_CI_AI`. `Vietnamese_CI_AI` coi "ơ", "ư", "đ"… là chữ cái riêng nên "com ga" không tìm ra "Cơm gà".
- **Thủ tục tên `sp_`:** trên một số server, `CREATE OR ALTER PROCEDURE dbo.sp_...` báo lỗi 208 "Invalid object name" (SQL Server tìm tên `sp_` trong `master` trước). `npm run db:setup` tự xử lý bằng cách tạo thủ tục rỗng rồi `ALTER`; nếu chạy file `.sql` bằng SSMS và gặp lỗi này, đổi `CREATE OR ALTER` thành `ALTER` sau khi đã tạo thủ tục một lần. Giữ tiền tố `sp_` để khớp tên thủ tục trong giáo trình.
- **Redis:** `REDIS_URL` phải có dạng `redis://<host>:6379`; sai định dạng hoặc không kết nối được thì service tự dùng cache bộ nhớ và ghi cảnh báo.

## 7. Bảo mật và giới hạn

- Gateway giới hạn `RATE_LIMIT_PER_MINUTE` request/phút/IP (mặc định 300) và `AUTH_RATE_LIMIT_PER_MINUTE` cho đăng nhập, đăng ký (mặc định 20); vượt giới hạn trả 429.
- Mật khẩu băm bằng bcrypt; refresh token chỉ lưu SHA-256; khóa tài khoản thì thu hồi mọi refresh token.
- Ảnh tải lên: chỉ JPEG/PNG/WebP, tối đa 2 MB (avatar) và 5 MB (ảnh món), tên file do server đặt.
- Service cảnh báo trong log khi còn dùng khóa bí mật mặc định của `.env.example`.
- Không commit `.env`. API gọi qua HTTP trong mạng Khoa; khi công khai ra Internet cần đặt sau HTTPS (reverse proxy).
