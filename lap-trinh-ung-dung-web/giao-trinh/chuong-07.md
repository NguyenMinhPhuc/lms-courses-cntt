# Chương 7. Module quản trị trên backend của nhóm

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Phân tích nghiệp vụ quản trị từ SRS thành thay đổi CSDL, stored procedure, API và trang web.
- Tìm khoảng trống giữa backend hiện có và yêu cầu mới.
- Viết script CSDL phiên bản mới, chạy lại nhiều lần không lỗi.
- Viết stored procedure quản trị có ràng buộc nghiệp vụ và mã lỗi thống nhất.
- Xây dựng API quản trị trên NestJS có phân quyền `admin` và tài liệu Swagger.
- So khớp hợp đồng API, chuyển web sang backend của nhóm và kiểm thử hồi quy.

## 7.1. Phân tích nghiệp vụ quản trị

### 7.1.1. Năm tầng của một story quản trị

Từ Sprint 3, nhóm không dùng API mẫu nữa mà tự chịu trách nhiệm từ CSDL tới giao diện. Mỗi user story quản trị được lần theo năm tầng: dữ liệu → stored procedure → API → trang web. Bảng này là phần "phân tích module quản trị" của báo cáo (CLO1) và đồng thời là danh sách việc của Sprint 3.

| Story | Dữ liệu | Stored procedure | API (admin) | Trang web |
|---|---|---|---|---|
| US-A01 danh mục | Categories | `sp_Category_Create/Update/Delete` | `POST/PUT/DELETE /admin/categories` | `/admin/categories` |
| US-A02 món | Products (ImageUrl, IsAvailable) | `sp_Product_Create/Update/SetAvailability/UpdateImage` | `/admin/products`, `.../image` | `/admin/products` (Chương 8) |
| US-A03 quầy | Counters (tọa độ, IsActive) | `sp_Counter_Create/Update` | `/admin/counters` | `/admin/counters` |
| US-A04 tài khoản | Users (Role admin, IsLocked) | `sp_User_CreateStaff/GetList/SetLocked` | `/admin/users`, `.../lock` | `/admin/users` (Chương 8) |
| US-A05, A06 báo cáo | Orders, OrderItems | `sp_Report_*` | `/reports/*` | `/admin/reports` (Chương 8) |

Nguồn để điền bảng: SRS mục 5.12 (M11 Quản trị, chức năng F11.1–F11.4), 5.10–5.11 (F09.3, F10), mục 7 (dữ liệu), mục 8 (danh mục API).

### 7.1.2. Khoảng trống của backend hiện tại

Backend của nhóm được xây trong học phần di động (Chương 5–7 giáo trình di động) phục vụ khách hàng và nhân viên. Đối chiếu với nhu cầu quản trị, có những khoảng trống điển hình:

- Cột `Users.Role` chỉ cho phép `customer` và `staff`: chưa có vai trò quản lý.
- Chưa có cột khóa tài khoản, trong khi tiêu chí US-A04 yêu cầu tài khoản bị khóa không đăng nhập và không làm mới token được.
- Chưa có thủ tục thêm, sửa, xóa danh mục; quy tắc "không xóa danh mục còn món" và BR-16 "món đã có trong đơn chỉ được ngừng bán" chưa được thể hiện.
- Bảng `Counters` do Chương 8 giáo trình di động tạo chỉ có tên và tọa độ, chưa có mô tả và trạng thái hoạt động.

Tìm khoảng trống trước khi code giúp nhóm ước lượng Sprint 3 sát thực tế và tránh viết lại những gì đã có.

## 7.2. Script CSDL theo phiên bản

### 7.2.1. Quy tắc

Giáo trình di động (Chương 7) đã đặt quy tắc cho thư mục `database/`: chạy lần lượt các script theo số thứ tự trên CSDL trống phải ra đúng CSDL của nhóm; thay đổi cấu trúc thì **thêm file mới**, không sửa file đã được các thành viên chạy; mỗi lệnh đổi cấu trúc kiểm tra trước để chạy lại không lỗi.

Giáo trình di động dùng các số 01–09 (`05-favorites`, `06-avatar`, `07-counters`, `08-notifications`, `09-health`). Module quản trị của web dùng số từ **20** để không trùng: `database/20-admin.sql`.

### 7.2.2. Mở rộng vai trò và khóa tài khoản

```sql
-- database/20-admin.sql: vai trò admin, khóa tài khoản, quản trị danh mục
-- 1) Mở rộng ràng buộc vai trò (ràng buộc cũ không đặt tên nên tìm theo nội dung)
IF OBJECT_ID('dbo.CK_Users_Role') IS NULL
BEGIN
  DECLARE @ck SYSNAME = (SELECT TOP 1 name FROM sys.check_constraints
                         WHERE parent_object_id = OBJECT_ID('dbo.Users') AND definition LIKE '%customer%');
  IF @ck IS NOT NULL EXEC('ALTER TABLE dbo.Users DROP CONSTRAINT ' + QUOTENAME(@ck));
  ALTER TABLE dbo.Users ADD CONSTRAINT CK_Users_Role CHECK (Role IN (N'customer', N'staff', N'admin'));
END;
GO
-- 2) Khóa tài khoản
IF COL_LENGTH('dbo.Users', 'IsLocked') IS NULL
  ALTER TABLE dbo.Users ADD IsLocked BIT NOT NULL CONSTRAINT DF_Users_IsLocked DEFAULT 0;
GO
```

Ràng buộc `CHECK` ở Chương 6 giáo trình di động không được đặt tên, nên SQL Server tự sinh một tên ngẫu nhiên khác nhau trên mỗi máy. Script tìm ràng buộc theo nội dung trong `sys.check_constraints` rồi xóa, sau đó tạo lại với tên cố định `CK_Users_Role` [1]. Từ nay nên luôn đặt tên cho ràng buộc.

## 7.3. Stored procedure quản trị

### 7.3.1. Ràng buộc nghiệp vụ trong thủ tục

```sql
CREATE OR ALTER PROCEDURE dbo.sp_Category_Create @Name NVARCHAR(100)
AS
BEGIN
  SET NOCOUNT ON;
  IF LEN(LTRIM(RTRIM(@Name))) < 2 THROW 50400, N'Tên danh mục tối thiểu 2 ký tự', 1;
  IF EXISTS (SELECT 1 FROM dbo.Categories WHERE Name = @Name)
    THROW 50409, N'Tên danh mục đã tồn tại', 1;
  INSERT INTO dbo.Categories (Name)
  OUTPUT inserted.CategoryId AS id, inserted.Name AS name
  VALUES (@Name);
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Category_Delete @CategoryId INT
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Categories WHERE CategoryId = @CategoryId)
    THROW 50404, N'Không tìm thấy danh mục', 1;
  IF EXISTS (SELECT 1 FROM dbo.Products WHERE CategoryId = @CategoryId)
    THROW 50409, N'Danh mục còn món, không xóa được', 1;
  DELETE FROM dbo.Categories WHERE CategoryId = @CategoryId;
END;
GO
-- sp_Category_Update: kiểm tra 50404 và trùng tên 50409 (trừ chính nó), OUTPUT dòng đã sửa

CREATE OR ALTER PROCEDURE dbo.sp_User_SetLocked @UserId INT, @IsLocked BIT, @ActorId INT
AS
BEGIN
  SET NOCOUNT ON;
  IF @UserId = @ActorId THROW 50400, N'Không thể tự khóa tài khoản của mình', 1;
  IF NOT EXISTS (SELECT 1 FROM dbo.Users WHERE UserId = @UserId)
    THROW 50404, N'Không tìm thấy tài khoản', 1;
  UPDATE dbo.Users SET IsLocked = @IsLocked
  OUTPUT inserted.UserId AS userId, inserted.FullName AS fullName, inserted.Role AS role, inserted.IsLocked AS isLocked
  WHERE UserId = @UserId;
  IF @IsLocked = 1                                                          -- thu hồi phiên đang mở
    UPDATE dbo.RefreshTokens SET RevokedAt = SYSDATETIME() WHERE UserId = @UserId AND RevokedAt IS NULL;
END;
GO
```

- `THROW` phát lỗi với mã tự đặt; mã từ 50000 trở lên dành cho lỗi của người dùng [2].
- `OUTPUT inserted....` trả về ngay dòng vừa thêm hoặc sửa, API không cần gọi thêm thủ tục đọc.
- Khóa tài khoản đồng thời thu hồi refresh token: nhân viên bị khóa sẽ bị đẩy ra khi access token hết hạn (tối đa 15 phút).
- Tài khoản admin đầu tiên tạo bằng script seed riêng có mật khẩu đã băm bcrypt, không tạo qua API (vì API tạo tài khoản quản trị đòi hỏi đã có admin).

### 7.3.2. Mã lỗi thống nhất

`DatabaseService` của giáo trình di động chuyển mã lỗi trong thủ tục thành mã HTTP:

| Mã lỗi trong thủ tục | HTTP | Ví dụ trong module quản trị |
|---|---|---|
| `50400` | 400 Bad Request | Tự khóa chính mình; tọa độ ngoài phạm vi |
| `50404` | 404 Not Found | Sửa danh mục không tồn tại |
| `50409` | 409 Conflict | Trùng tên danh mục; xóa danh mục còn món |

Ràng buộc nghiệp vụ đặt trong thủ tục nên web, ứng dụng di động hay Swagger gọi vào đều bị kiểm tra như nhau. Nếu chỉ đặt ở giao diện web (ẩn nút Xóa), ai đó gọi thẳng API vẫn xóa được.

### 7.3.3. Danh mục stored procedure

Báo cáo đồ án cần bảng **danh mục stored procedure** của module quản trị (CLO1):

| Thủ tục | Tham số | Kết quả | Mã lỗi |
|---|---|---|---|
| `sp_Category_Create` | `@Name` | Dòng vừa thêm (`id`, `name`) | 50400, 50409 |
| `sp_Category_Delete` | `@CategoryId` | Không có | 50404, 50409 |
| `sp_User_SetLocked` | `@UserId`, `@IsLocked`, `@ActorId` | Tài khoản sau khi đổi | 50400, 50404 |

Kèm theo là **ERD phần quản trị**: các bảng Users, Categories, Products, Counters và quan hệ của chúng, có đánh dấu cột mới thêm ở Sprint 3.

## 7.4. API quản trị trên NestJS

### 7.4.1. Controller và DTO

Học phần khuyến khích dùng chung backend NestJS với đồ án di động. Nhóm dùng backend khác (Express, ASP.NET…) vẫn phải gọi stored procedure, phân quyền ở server và có Swagger.

```ts
// src/admin/dto/category.dto.ts
import { ApiProperty } from '@nestjs/swagger';
import { IsString, Length } from 'class-validator';

export class CategoryDto {
  @ApiProperty({ example: 'Đồ uống' })
  @IsString() @Length(2, 100)
  name!: string;
}

// src/admin/admin-categories.controller.ts
@ApiTags('Admin - Categories')
@ApiBearerAuth()
@Controller('admin/categories')
@UseGuards(AuthGuard, RolesGuard)
@Roles(['admin'])                                   // áp dụng cho mọi route của controller
export class AdminCategoriesController {
  constructor(private readonly db: DatabaseService) {}

  @Post()
  async create(@Body() dto: CategoryDto) {
    const [row] = await this.db.execute('sp_Category_Create', { Name: { type: sql.NVarChar(100), value: dto.name } });
    return row;
  }

  @Put(':id')
  async update(@Param('id', ParseIntPipe) id: number, @Body() dto: CategoryDto) {
    const [row] = await this.db.execute('sp_Category_Update', {
      CategoryId: { type: sql.Int, value: id }, Name: { type: sql.NVarChar(100), value: dto.name },
    });
    return row;
  }

  @Delete(':id') @HttpCode(204)
  async remove(@Param('id', ParseIntPipe) id: number) {
    await this.db.execute('sp_Category_Delete', { CategoryId: { type: sql.Int, value: id } });
  }
}
```

DTO với `class-validator` kiểm tra dữ liệu vào; `ValidationPipe` với `whitelist: true` loại bỏ trường thừa (cấu hình ở Chương 5 giáo trình di động). `@ApiProperty` và `@ApiTags` sinh tài liệu Swagger [3].

### 7.4.2. Phân quyền admin

`RolesGuard` của giáo trình di động so khớp **đúng tên vai trò**, nên `admin` không tự có quyền của `staff`. Có hai cách, nhóm chọn một và ghi quyết định vào báo cáo:

- Sửa các route nhân viên thành `@Roles(['staff', 'admin'])` theo ma trận phân quyền ở Chương 5.
- Sửa guard để coi `admin` bao gồm `staff` (API mẫu của giảng viên làm theo cách này).

Khi `@Roles` đặt trên controller thay vì trên từng phương thức, guard phải đọc metadata ở cả hai nơi: `reflector.getAllAndOverride(Roles, [context.getHandler(), context.getClass()])` [4].

### 7.4.3. Khóa tài khoản trong luồng xác thực

- `sp_User_GetByEmail` trả thêm cột `IsLocked`; `AuthService.login` trả 403 "Tài khoản đã bị khóa" khi `IsLocked = 1`.
- Làm mới token cũng kiểm tra lại trạng thái khóa.
- Mã người quản lý thực hiện (`@ActorId`) lấy từ token (`req.user.sub`), không lấy từ body.

### 7.4.4. Swagger là hợp đồng

Swagger tại `/api` của backend nhóm là **hợp đồng** giữa người làm backend, người làm web và người làm mobile: mỗi route có ví dụ body, ví dụ phản hồi và các mã lỗi có thể trả về. Thay đổi hợp đồng phải được cả nhóm biết trước.

## 7.5. Chuyển web sang backend của nhóm

### 7.5.1. So khớp hợp đồng API

Đổi `API_URL` trong `.env.local` là bước **cuối cùng**, không phải bước đầu. Trước đó, so khớp từng endpoint web đang dùng giữa API mẫu (`/docs`) và backend nhóm (`/api`):

| Endpoint web đang dùng | Điểm cần so khớp | Ví dụ khác biệt hay gặp |
|---|---|---|
| `GET /products` | Tham số lọc, kiểu trả về (mảng hay object phân trang), tên trường | Nhóm chưa hỗ trợ `keyword`, `includeUnavailable` |
| `GET /counters` | Tên trường tọa độ | `lat`/`lng` (Chương 8 di động) so với `latitude`/`longitude` |
| `POST /auth/login` | Dạng phản hồi, mã lỗi 401/403 | Không trả `role` ở ngoài, chỉ có trong token |
| `GET /orders/staff` | Đường dẫn, các trường hiển thị | Thiếu `summary`, `customerName` |

### 7.5.2. Hai cách xử lý khác biệt

- **Sửa backend** cho đúng hợp đồng chung. Đây là cách ưu tiên, vì ứng dụng di động cũng dùng backend này.
- **Thêm hàm chuyển đổi** trong `lib/api.ts`, để chỉ một chỗ biết khác biệt và trang web không phải sửa:

```ts
// lib/api.ts
type CounterDto = { id: number; name: string; lat: number; lng: number };
export const toCounter = (c: CounterDto): Counter =>
  ({ id: c.id, name: c.name, latitude: c.lat, longitude: c.lng, isActive: true });
```

Nhờ quy tắc "mọi lời gọi API đi qua `lib/api.ts`" từ Chương 3, việc chuyển backend chỉ ảnh hưởng một thư mục.

### 7.5.3. Kiểm thử hồi quy

**Kiểm thử hồi quy** (regression testing) chạy lại các test đã đạt để chắc chắn thay đổi mới không làm hỏng chức năng cũ. Sau khi đổi `API_URL`, chạy lại toàn bộ test case Sprint 1–2 (TC-01…05, 11…17, 21…28, 31…37) trên backend nhóm và ghi vào cột "Kết quả trên backend nhóm". Test nào trước đạt mà giờ không đạt là một **lỗi hồi quy**, phải có thẻ trên board. Chương 10 tự động hóa việc chạy lại này.

### 7.5.4. Trang quản lý danh mục

Trang `/admin/categories` dùng lại mẫu Server Action của Chương 6: `requireRole('admin')`, gọi `apiAuth('/admin/categories', …)`, bắt `ApiError` 409 để hiện "Danh mục còn món, không xóa được", rồi `revalidatePath`. Nút xóa đặt trong hộp thoại xác nhận.

## Tóm tắt chương

- Story quản trị được phân tích theo năm tầng: dữ liệu, thủ tục, API, trang; bảng phân tích là danh sách việc của Sprint 3.
- Tìm khoảng trống của backend hiện tại trước khi code.
- Script CSDL phiên bản mới (`20-admin.sql`), kiểm tra trước khi đổi cấu trúc, đặt tên cho ràng buộc.
- Ràng buộc nghiệp vụ nằm trong thủ tục với mã lỗi 50400/50404/50409; `DatabaseService` chuyển thành HTTP.
- API quản trị có `@Roles(['admin'])`, DTO, Swagger; quyết định rõ quyền của admin so với staff.
- So khớp hợp đồng API trước khi đổi `API_URL`; kiểm thử hồi quy sau khi đổi.

## Câu hỏi ôn tập

1. Liệt kê năm tầng khi phân tích US-A04 và điền nội dung cho từng tầng.
2. Vì sao script quản trị không sửa thẳng file `03-auth.sql` đã có?
3. `IF COL_LENGTH('dbo.Users', 'IsLocked') IS NULL` dùng để làm gì?
4. Quy tắc "không xóa danh mục còn món" nên đặt ở đâu? Nếu chỉ ẩn nút Xóa trên web thì sao?
5. Vì sao tài khoản admin đầu tiên không tạo được qua API?
6. Hai cách xử lý khi tên trường của backend nhóm khác API mẫu là gì? Bạn ưu tiên cách nào?
7. Kiểm thử hồi quy là gì? Khi nào phải làm?

## Bài tập

1. **Quản lý quầy.** Bổ sung cột `Description`, `IsActive` cho `Counters` (có kiểm tra trước), thủ tục `sp_Counter_Create/Update` kiểm tra tọa độ, API `/admin/counters` chỉ cho admin.
2. **Danh mục thủ tục.** Lập danh mục stored procedure đầy đủ cho module quản trị của nhóm.
3. **Hồi quy.** Chạy lại toàn bộ test case Sprint 1–2 trên backend nhóm, mở thẻ cho mọi lỗi hồi quy.

## Tài liệu tham khảo

[1] Microsoft, “sys.check_constraints (Transact-SQL),” *Microsoft Learn*. Accessed: Oct. 30, 2026. [Online]. Available: https://learn.microsoft.com/sql/relational-databases/system-catalog-views/sys-check-constraints-transact-sql

[2] Microsoft, “THROW (Transact-SQL),” *Microsoft Learn*. Accessed: Oct. 30, 2026. [Online]. Available: https://learn.microsoft.com/sql/t-sql/language-elements/throw-transact-sql

[3] NestJS, “OpenAPI: Introduction,” *NestJS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.nestjs.com/openapi/introduction

[4] NestJS, “Authorization,” *NestJS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.nestjs.com/security/authorization
