<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 07 - Module quản trị trên backend của nhóm (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Hai sprint đầu, web của nhóm sống nhờ API mẫu của giảng viên. Từ hôm nay nhóm tự chịu trách nhiệm toàn bộ: CSDL, stored procedure, API và trang web. Backend của đồ án di động chưa biết "quản lý" là ai, chưa khóa được tài khoản, chưa xóa được danh mục. Việc đầu tiên không phải là viết code, mà là tìm ra backend còn thiếu những gì.</em></p>
        <p><strong>Mục tiêu:</strong> Phân tích được nghiệp vụ quản trị từ SRS thành thay đổi CSDL, stored procedure và API; viết được script CSDL phiên bản mới chạy lại an toàn; xây dựng được API quản trị có phân quyền <code>admin</code> và tài liệu Swagger; chuyển được web từ API mẫu sang backend của nhóm và kiểm thử hồi quy.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Phân tích nghiệp vụ quản trị:</strong> từ user story US-A01…A04 tới dữ liệu, thủ tục, API, trang; tìm khoảng trống của backend hiện tại.</li>
            <li><strong>Ý chính 2 - Stored procedure quản trị:</strong> CRUD có ràng buộc nghiệp vụ, mã lỗi 50400/50404/50409, script phiên bản mới.</li>
            <li><strong>Ý chính 3 - API quản trị:</strong> phân quyền <code>admin</code>, DTO, Swagger, khóa tài khoản.</li>
            <li><strong>Ý chính 4 - Chuyển web sang backend nhóm:</strong> so khớp hợp đồng API, lớp chuyển đổi, kiểm thử hồi quy Sprint 1–2.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Backend nhóm có module quản trị danh mục, quầy và tài khoản (gọi stored procedure, phân quyền admin); web chạy trên backend nhóm, các test case Sprint 1–2 vẫn đạt.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Phân tích nghiệp vụ quản trị</h3>
            <p>Mỗi user story quản trị được lần theo năm tầng. Bảng này là phần "phân tích module quản trị" của báo cáo (CLO1) và là danh sách việc của Sprint 3.</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Story</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Dữ liệu</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Stored procedure</th><th style="border: 1px solid #ffd6ad; padding: 6px;">API (admin)</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Trang web</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A01 danh mục</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Categories</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>sp_Category_Create/Update/Delete</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>POST/PUT/DELETE /admin/categories</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/categories</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A02 món</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Products (ImageUrl, IsAvailable)</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>sp_Product_Create/Update/SetAvailability/UpdateImage</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/products</code>, <code>…/image</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/products</code> (bài 08)</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A03 quầy</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Counters (tọa độ, IsActive)</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>sp_Counter_Create/Update</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/counters</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/counters</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A04 tài khoản</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Users (Role admin, IsLocked)</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>sp_User_CreateStaff/GetList/SetLocked</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/users</code>, <code>…/lock</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/users</code> (bài 08)</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;">US-A05, A06 báo cáo</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Orders, OrderItems</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>sp_Report_*</code> (đã có từ Chương 7 di động)</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/reports/*</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>/admin/reports</code> (bài 08)</td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;"><strong>Khoảng trống của backend hiện tại.</strong> Đối chiếu với CSDL đã xây trong học phần di động (Chương 5–7):</p>
            <ul style="margin-bottom: 0;">
                <li>Cột <code>Users.Role</code> chỉ cho phép <code>customer</code> và <code>staff</code>: chưa có vai trò quản lý.</li>
                <li>Chưa có cột khóa tài khoản; BR của US-A04 yêu cầu tài khoản bị khóa không đăng nhập và không làm mới token được.</li>
                <li>Chưa có thủ tục thêm, sửa, xóa danh mục. Quy tắc: không xóa danh mục còn món (409); món đã có trong đơn chỉ được ngừng bán, không xóa hẳn (BR-16).</li>
                <li>Bảng <code>Counters</code> do Chương 8 di động tạo (<code>07-counters.sql</code>) chưa có cột mô tả và trạng thái hoạt động.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Script CSDL và stored procedure quản trị</h3>
            <p>Thay đổi CSDL viết thành <strong>file mới</strong>, không sửa file mà các thành viên đã chạy. Giáo trình di động dùng các số 01–09, nên module quản trị của web dùng số từ 20 để không trùng: <code>database/20-admin.sql</code>. Mỗi lệnh đổi cấu trúc đều kiểm tra trước, chạy lại nhiều lần không lỗi.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>-- database/20-admin.sql: vai trò admin, khóa tài khoản, quản trị danh mục
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

-- 3) Danh mục: thêm, sửa, xóa có ràng buộc
CREATE OR ALTER PROCEDURE dbo.sp_Category_Create @Name NVARCHAR(100)
AS
BEGIN
  SET NOCOUNT ON;
  IF LEN(LTRIM(RTRIM(@Name))) &lt; 2 THROW 50400, N'Tên danh mục tối thiểu 2 ký tự', 1;
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

-- 4) Khóa / mở khóa tài khoản; không cho tự khóa chính mình
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
-- Tài khoản admin đầu tiên: tạo bằng script seed riêng (mật khẩu đã băm bcrypt), không tạo qua API</code></pre>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px; margin-top: 10px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Mã lỗi trong thủ tục</th><th style="border: 1px solid #ffd6ad; padding: 6px;">HTTP (DatabaseService)</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Ví dụ trong module quản trị</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>50400</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">400 Bad Request</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tự khóa chính mình; tọa độ ngoài phạm vi</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>50404</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">404 Not Found</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Sửa danh mục không tồn tại</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>50409</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">409 Conflict</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Trùng tên danh mục; xóa danh mục còn món</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;">Ràng buộc nghiệp vụ đặt trong thủ tục (và ràng buộc CSDL) nên web, ứng dụng di động hay Swagger gọi vào đều bị kiểm tra như nhau. Tên thủ tục và tham số theo quy ước <code>sp_&lt;Đối tượng&gt;_&lt;Hành động&gt;</code> của Chương 5 giáo trình di động.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. API quản trị trên NestJS</h3>
            <p>Học phần khuyến khích dùng chung backend NestJS với đồ án di động. Nhóm dùng backend khác (Express, ASP.NET…) vẫn phải gọi stored procedure, phân quyền ở server và có Swagger.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// src/admin/dto/category.dto.ts
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
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>RolesGuard của giáo trình di động</strong> so khớp đúng tên vai trò, nên <code>admin</code> không tự có quyền của <code>staff</code>. Sửa các route nhân viên thành <code>@Roles(['staff', 'admin'])</code> theo ma trận phân quyền bài 05, hoặc cho guard coi <code>admin</code> bao gồm <code>staff</code>. Ghi quyết định này vào báo cáo.</li>
                <li><strong>Khóa tài khoản:</strong> <code>sp_User_GetByEmail</code> trả thêm <code>IsLocked</code>; <code>AuthService.login</code> trả 403 "Tài khoản đã bị khóa" khi <code>IsLocked = 1</code>; làm mới token cũng kiểm tra lại. Nếu <code>@Roles</code> đặt trên controller, đọc bằng <code>reflector.getAllAndOverride(Roles, [context.getHandler(), context.getClass()])</code>.</li>
                <li><strong>Mã người quản lý</strong> (<code>@ActorId</code>) lấy từ token (<code>req.user.sub</code>), không lấy từ body.</li>
                <li>Swagger (<code>/api</code>) là hợp đồng giữa người làm backend, người làm web và người làm mobile: mỗi route có ví dụ body và mã lỗi.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Chuyển web sang backend của nhóm</h3>
            <p>Đổi <code>API_URL</code> trong <code>.env.local</code> là bước cuối cùng, không phải bước đầu. Trước đó, so khớp hợp đồng API giữa API mẫu (tài liệu tại <code>/docs</code>) và backend nhóm (<code>/api</code>):</p>
            <table style="border-collapse: collapse; width: 100%; max-width: 860px; font-size: 13px;">
                <thead><tr style="background-color: #ffe8d1;"><th style="border: 1px solid #ffd6ad; padding: 6px;">Endpoint web đang dùng</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Điểm cần so khớp</th><th style="border: 1px solid #ffd6ad; padding: 6px;">Ví dụ khác biệt hay gặp</th></tr></thead>
                <tbody>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>GET /products</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tham số lọc, kiểu trả về (mảng hay object phân trang), tên trường</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Nhóm chưa hỗ trợ <code>keyword</code>, <code>includeUnavailable</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>GET /counters</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Tên trường tọa độ</td><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>lat</code>/<code>lng</code> (Chương 8 di động) so với <code>latitude</code>/<code>longitude</code></td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>POST /auth/login</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Dạng phản hồi, mã lỗi 401/403</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Không trả <code>role</code> ở ngoài, chỉ có trong token</td></tr>
                    <tr><td style="border: 1px solid #ffd6ad; padding: 6px;"><code>GET /orders/staff</code></td><td style="border: 1px solid #ffd6ad; padding: 6px;">Đường dẫn, các trường hiển thị</td><td style="border: 1px solid #ffd6ad; padding: 6px;">Thiếu <code>summary</code>, <code>customerName</code></td></tr>
                </tbody>
            </table>
            <p style="margin-top: 10px;">Hai cách xử lý khác biệt: <strong>sửa backend</strong> cho đúng hợp đồng chung (ưu tiên, vì ứng dụng di động cũng dùng), hoặc thêm hàm chuyển đổi trong <code>lib/api.ts</code> để trang web không phải sửa:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/api.ts: chỉ một chỗ biết khác biệt giữa backend và kiểu dữ liệu của web
type CounterDto = { id: number; name: string; lat: number; lng: number };
export const toCounter = (c: CounterDto): Counter =&gt;
  ({ id: c.id, name: c.name, latitude: c.lat, longitude: c.lng, isActive: true });</code></pre>
            <p><strong>Kiểm thử hồi quy.</strong> Sau khi đổi <code>API_URL</code>, chạy lại toàn bộ test case Sprint 1–2 (TC-01…05, 11…17, 21…28, 31…37) trên backend nhóm, ghi vào cột "Kết quả trên backend nhóm". Test nào trước đạt mà giờ không đạt là một lỗi hồi quy, phải có thẻ trên board.</p>
            <p style="margin-bottom: 0;">Trang <code>/admin/categories</code> dùng lại mẫu Server Action của bài 06: <code>requireRole('admin')</code>, gọi <code>apiAuth('/admin/categories', …)</code>, bắt 409 để hiện "Danh mục còn món, không xóa được", rồi <code>revalidatePath</code>.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_07}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 07: Module quản trị trên backend của nhóm</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Tài liệu dự án</p>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Module quản trị (F09.3, F10, F11), user story US-A01…A04, quy tắc BR-16; mục 8: các endpoint /admin.</span>
            </a>
            <a href="{{LINK_AGILE_SCRUM}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🗂 Kế hoạch Agile &amp; Product Backlog</span><br>
                <span style="color: #6c757d; font-size: 13px;">Epic quản trị và story của Sprint 3.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.nestjs.com/security/authorization" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - Authorization</span><br>
                <span style="color: #6c757d; font-size: 13px;">Roles decorator, RolesGuard, đọc metadata ở cả handler và controller.</span>
            </a>
            <a href="https://docs.nestjs.com/openapi/introduction" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - OpenAPI (Swagger)</span><br>
                <span style="color: #6c757d; font-size: 13px;">ApiProperty, ApiTags, ApiBearerAuth, ví dụ request và response.</span>
            </a>
            <a href="https://learn.microsoft.com/sql/t-sql/language-elements/throw-transact-sql" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Microsoft Learn - THROW (Transact-SQL)</span><br>
                <span style="color: #6c757d; font-size: 13px;">Phát lỗi có mã tự đặt từ stored procedure.</span>
            </a>
        </div>
    </div>
</details>

<details style="border: 1px solid #28a745; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #eafaf1; color: #28a745; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>💡 3. Hoạt động &amp; Thực hành trên lớp</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Quản lý danh mục từ CSDL đến web</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Viết <code>database/20-admin.sql</code>, chạy hai lần liên tiếp trên CSDL nhóm để chứng minh chạy lại không lỗi; tạo tài khoản admin bằng script seed.</li>
                <li>Chạy thử từng thủ tục trong SSMS: xóa danh mục còn món phải nhận lỗi 50409.</li>
                <li>Tạo <code>AdminCategoriesController</code>, DTO, cập nhật <code>RolesGuard</code>; thử trên Swagger bằng token admin và token staff (mong đợi 403).</li>
                <li>Trang <code>/admin/categories</code> trên web: danh sách, thêm, sửa, xóa qua Server Action, gọi backend nhóm.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Quản lý quầy</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Bổ sung vào <code>20-admin.sql</code> các cột <code>Description</code>, <code>IsActive</code> cho bảng <code>Counters</code> (có kiểm tra trước), thủ tục <code>sp_Counter_Create</code> và <code>sp_Counter_Update</code> (tên 2–100 ký tự, vĩ độ −90…90, kinh độ −180…180, sai thì <code>THROW 50400</code>); API <code>POST/PUT /admin/counters</code> chỉ cho admin, có Swagger.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp link repo, ảnh chụp Swagger và kết quả 4 lần gọi: tạo hợp lệ (201), vĩ độ 91 (400), sửa quầy không tồn tại (404), gọi bằng token staff (403).</p>
            <a href="{{LINK_NOP_BAI_07}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <p style="margin: 0; color: #495057;">Hoàn thành bảng phân tích mục 2.1 cho đề tài nhóm; vẽ <strong>ERD phần quản trị</strong> và lập <strong>danh mục stored procedure</strong> (tên, tham số, kết quả, mã lỗi) (CLO1). Xây module quản trị trên backend nhóm, chuyển web sang backend nhóm, chạy hồi quy và mở thẻ cho mọi lỗi hồi quy.</p>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Quy tắc "không xóa danh mục còn món" nên đặt ở đâu: trang web (ẩn nút Xóa), API (kiểm tra trước khi gọi thủ tục) hay stored procedure? Nếu chỉ đặt ở một nơi, bạn chọn nơi nào và vì sao?</p>
            <a href="{{LINK_DIEN_DAN_BAI_07}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập phân tích module quản trị, script phiên bản, stored procedure, phân quyền admin và hợp đồng API.</p>
            <a href="{{LINK_QUIZ_BAI_07}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 07</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Lỗi 547 khi thêm ràng buộc <code>CK_Users_Role</code>:</strong> trong bảng đã có dòng mang vai trò khác ba giá trị cho phép. Tìm bằng <code>SELECT DISTINCT Role FROM dbo.Users</code> và sửa dữ liệu trước.</p>
        <p><strong>Token admin vẫn nhận 403 ở route nhân viên:</strong> <code>RolesGuard</code> so khớp đúng tên vai trò. Thêm <code>'admin'</code> vào <code>@Roles</code> hoặc sửa guard (mục 2.3).</p>
        <p><strong>Lỗi 500 thay vì 409:</strong> thủ tục dùng <code>RAISERROR</code> hoặc mã lỗi khác 50400/50404/50409, nên <code>DatabaseService</code> không chuyển được thành mã HTTP. Dùng <code>THROW</code> với đúng mã.</p>
        <p><strong>Web lỗi sau khi đổi <code>API_URL</code>:</strong> mở tab Network của trình duyệt không thấy gì vì Next.js gọi API từ server. Xem log ở terminal chạy <code>npm run dev</code> và so với Swagger của nhóm.</p>
        <p><strong>Kiến thức mở rộng:</strong> nhật ký thao tác quản trị (bảng <code>AuditLogs</code> ghi ai sửa gì, lúc nào) bằng trigger hoặc ghi trong thủ tục; kiểm thử hợp đồng API tự động bằng cách so file OpenAPI của hai backend.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Một thành viên mới chạy lần lượt mọi script trong <code>database/</code> trên CSDL trống. Họ có được đúng CSDL của nhóm, kể cả tài khoản admin, không?</p>
    </div>
</details>
