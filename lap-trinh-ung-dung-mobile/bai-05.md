<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 05 - Thiết kế CSDL, stored procedure, API NestJS &amp; kết nối ứng dụng (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Đến giờ LHU Food vẫn dùng dữ liệu giả trong một file TypeScript. Hôm nay dữ liệu chuyển về đúng chỗ của nó: SQL Server. Câu hỏi là: đi từ màn hình điện thoại tới một dòng trong bảng <code>Products</code> phải qua những lớp nào, và lớp nào được phép làm gì?</em></p>
        <p><strong>Mục tiêu:</strong> Thiết kế được CSDL SQL Server đáp ứng đặc tả và trình bày bằng ERD; viết được stored procedure cho các thao tác dữ liệu; xây dựng được REST API NestJS chỉ truy cập CSDL qua stored procedure; tích hợp và quản lý được dữ liệu server trong ứng dụng.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Thiết kế CSDL:</strong> khóa chính/ngoại, quan hệ 1-n và n-n, ràng buộc cơ bản; hoàn thiện ERD từ bản sơ bộ ở bài 03.</li>
            <li><strong>Ý chính 2 - Stored procedure:</strong> quy ước đặt tên, tham số, phân trang <code>OFFSET/FETCH</code>, báo lỗi bằng <code>THROW</code>; vì sao học phần bắt buộc dùng thủ tục.</li>
            <li><strong>Ý chính 3 - API NestJS với mssql:</strong> module, controller, service, DTO; <code>DatabaseService</code> dùng chung để gọi <code>request.execute()</code>.</li>
            <li><strong>Ý chính 4 - Kết nối ứng dụng:</strong> lớp <code>api</code> tập trung, địa chỉ API cho emulator và máy thật, TanStack Query (<code>useQuery</code>, <code>useMutation</code>, cuộn vô hạn).</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> LHU Food hiển thị thực đơn và đặt hàng qua API thật; nhóm có ERD hoàn chỉnh, danh mục stored procedure và API có Swagger.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2, CLO3.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Kiến trúc: dữ liệu đi qua những lớp nào?</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>Ứng dụng (React Native)
   │  HTTP + JSON   (useQuery / useMutation)
   ▼
API NestJS: Controller → Service → DatabaseService
   │  mssql: request.input(...) + request.execute('sp_...')
   ▼
SQL Server: Stored procedure → Bảng</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>App</strong> không bao giờ kết nối thẳng vào SQL Server; app chỉ gọi API.</li>
                <li><strong>API</strong> không viết câu SQL; API chỉ gọi stored procedure có tham số.</li>
                <li><strong>Stored procedure</strong> chứa toàn bộ câu lệnh đọc/ghi dữ liệu.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Hoàn thiện thiết kế CSDL</h3>
            <p>Từ ERD sơ bộ ở bài 03, bổ sung kiểu dữ liệu, khóa và ràng buộc. Dùng <code>NVARCHAR</code> cho chuỗi tiếng Việt, <code>DECIMAL</code> cho tiền.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>CREATE TABLE Categories (
  CategoryId INT IDENTITY(1,1) PRIMARY KEY,
  Name       NVARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Products (
  ProductId   INT IDENTITY(1,1) PRIMARY KEY,
  CategoryId  INT NOT NULL REFERENCES Categories(CategoryId),
  Name        NVARCHAR(150) NOT NULL,
  Price       DECIMAL(12,0) NOT NULL CHECK (Price &gt;= 0),
  ImageUrl    NVARCHAR(500) NULL,
  IsAvailable BIT NOT NULL DEFAULT 1
);

CREATE TABLE Orders (
  OrderId   INT IDENTITY(1,1) PRIMARY KEY,
  UserId    INT NOT NULL,          -- khóa ngoại tới Users (bài 06)
  Status    NVARCHAR(20) NOT NULL DEFAULT N'pending',
  Note      NVARCHAR(200) NULL,
  CreatedAt DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

CREATE TABLE OrderItems (
  OrderId   INT NOT NULL REFERENCES Orders(OrderId),
  ProductId INT NOT NULL REFERENCES Products(ProductId),
  Quantity  INT NOT NULL CHECK (Quantity &gt; 0),
  UnitPrice DECIMAL(12,0) NOT NULL,
  PRIMARY KEY (OrderId, ProductId)
);</code></pre>
            <p style="margin-bottom: 0;"><strong>💡 Vì sao lưu <code>UnitPrice</code> trong <code>OrderItems</code>?</strong> Giá món có thể đổi sau này; đơn hàng cũ phải giữ đúng giá tại thời điểm đặt. Vẽ lại ERD hoàn chỉnh bằng dbdiagram.io hoặc draw.io và lưu vào <code>docs/</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Stored procedure: quy ước và ví dụ</h3>
            <p><strong>Vì sao học phần bắt buộc dùng stored procedure?</strong></p>
            <ul>
                <li><strong>Tách logic dữ liệu</strong> khỏi mã nguồn backend; đổi câu truy vấn không cần build lại API.</li>
                <li><strong>Phân quyền chặt:</strong> tài khoản SQL Server của API chỉ cần quyền <code>EXECUTE</code>, không đọc/ghi bảng trực tiếp (bài 06).</li>
                <li><strong>Chống SQL injection:</strong> giá trị luôn đi vào tham số có kiểu, không ghép chuỗi.</li>
            </ul>
            <p><strong>Quy ước đặt tên:</strong> <code>sp_&lt;Thực thể&gt;_&lt;Hành động&gt;</code>, ví dụ <code>sp_Product_GetList</code>, <code>sp_Product_GetById</code>, <code>sp_Order_Create</code>, <code>sp_Order_GetHistory</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>CREATE OR ALTER PROCEDURE sp_Product_GetList
  @CategoryId INT = NULL,
  @Page       INT = 1,
  @PageSize   INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  SELECT ProductId AS id, CategoryId AS categoryId, Name AS name,
         Price AS price, ImageUrl AS imageUrl
  FROM Products
  WHERE IsAvailable = 1
    AND (@CategoryId IS NULL OR CategoryId = @CategoryId)
  ORDER BY ProductId
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO

CREATE OR ALTER PROCEDURE sp_Product_GetById
  @ProductId INT
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM Products WHERE ProductId = @ProductId)
    THROW 50404, N'Không tìm thấy món ăn', 1;

  SELECT ProductId AS id, CategoryId AS categoryId, Name AS name,
         Price AS price, ImageUrl AS imageUrl, IsAvailable AS isAvailable
  FROM Products WHERE ProductId = @ProductId;
END;
GO</code></pre>
            <p><strong>Bí danh camelCase</strong> (<code>ProductId AS id</code>): thủ tục trả dữ liệu cho app đặt tên cột theo quy ước JSON, để API trả thẳng kết quả mà app dùng được ngay, không cần viết mã chuyển đổi.</p>
            <p style="margin-bottom: 0;"><strong>Mã lỗi tự đặt</strong> (từ 50000 trở lên) giúp backend biết lỗi gì để trả mã HTTP phù hợp: ví dụ 50404 → <code>404 Not Found</code>. Viết xong thủ tục nào, chạy thử ngay trong SSMS bằng <code>EXEC sp_Product_GetList @Page = 1;</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. API NestJS gọi stored procedure bằng mssql</h3>
            <p>Cài thư viện: <code>npm install mssql</code>. Tạo một <code>DatabaseService</code> dùng chung giữ <strong>connection pool</strong> và chỉ có một cách gọi CSDL: chạy thủ tục với tham số có kiểu.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// src/database/database.service.ts
import { Injectable, OnModuleDestroy, OnModuleInit } from '@nestjs/common';
import * as sql from 'mssql';

type Param = { type: sql.ISqlType | (() =&gt; sql.ISqlType); value: unknown };

@Injectable()
export class DatabaseService implements OnModuleInit, OnModuleDestroy {
  private pool!: sql.ConnectionPool;

  async onModuleInit() {
    this.pool = await new sql.ConnectionPool({
      server: process.env.DB_SERVER!,
      database: process.env.DB_NAME!,
      user: process.env.DB_USER!,
      password: process.env.DB_PASSWORD!,
      options: { encrypt: false, trustServerCertificate: true },
    }).connect();
  }

  async onModuleDestroy() {
    await this.pool?.close();
  }

  async execute&lt;T&gt;(procedure: string, params: Record&lt;string, Param&gt; = {}): Promise&lt;T[]&gt; {
    const request = this.pool.request();
    for (const [name, p] of Object.entries(params)) {
      request.input(name, p.type, p.value);
    }
    const result = await request.execute&lt;T&gt;(procedure);
    return result.recordset;
  }
}</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// src/products/products.service.ts
import { Injectable, NotFoundException } from '@nestjs/common';
import * as sql from 'mssql';
import { DatabaseService } from '../database/database.service';

@Injectable()
export class ProductsService {
  constructor(private readonly db: DatabaseService) {}

  findAll(page = 1, categoryId?: number) {
    return this.db.execute('sp_Product_GetList', {
      CategoryId: { type: sql.Int, value: categoryId ?? null },
      Page: { type: sql.Int, value: page },
      PageSize: { type: sql.Int, value: 20 },
    });
  }

  async findOne(id: number) {
    try {
      const [product] = await this.db.execute('sp_Product_GetById', {
        ProductId: { type: sql.Int, value: id },
      });
      return product;
    } catch (err: any) {
      if (err.number === 50404) throw new NotFoundException(err.message);
      throw err;
    }
  }
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Controller</strong> nhận request (<code>@Get()</code>, <code>@Get(':id')</code>, <code>@Post()</code>), kiểm tra dữ liệu bằng DTO + <code>ValidationPipe</code>, gọi service.</li>
                <li><strong>Swagger</strong> (<code>@nestjs/swagger</code>) sinh tài liệu API tại <code>/api</code>, để người làm mobile biết endpoint và dữ liệu trả về.</li>
                <li><strong>Vibe coding:</strong> đưa ERD cho Antigravity sinh thủ tục và service; <strong>review từng thủ tục</strong> (đủ tham số, có <code>SET NOCOUNT ON</code>, có kiểm tra tồn tại) và tìm trong mã backend chuỗi <code>SELECT</code>/<code>INSERT</code> để chắc chắn AI không viết SQL trực tiếp.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Kết nối ứng dụng với API</h3>
            <p><strong>Địa chỉ API:</strong> khai báo trong file <code>.env</code> của dự án Expo: <code>EXPO_PUBLIC_API_URL=http://192.168.1.10:3000</code>. Biến có tiền tố <code>EXPO_PUBLIC_</code> được đưa vào ứng dụng, nên <strong>không bao giờ đặt mật khẩu hay khóa bí mật</strong> vào đây.</p>
            <ul>
                <li><strong>Điện thoại thật:</strong> dùng IP LAN của máy chạy API (<code>ipconfig</code>), không dùng <code>localhost</code> vì <code>localhost</code> trên điện thoại là chính điện thoại.</li>
                <li><strong>Android emulator:</strong> dùng <code>10.0.2.2</code> để trỏ về máy tính đang chạy emulator.</li>
                <li><strong>Tường lửa Windows</strong> có thể chặn cổng 3000; nếu điện thoại không gọi được, kiểm tra cổng đã được mở.</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// lib/api.ts
const API_URL = process.env.EXPO_PUBLIC_API_URL;

export async function api&lt;T&gt;(path: string, init?: RequestInit): Promise&lt;T&gt; {
  const res = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...init?.headers },
  });
  if (!res.ok) {
    const body = await res.json().catch(() =&gt; ({}));
    throw new Error(body.message ?? `Lỗi ${res.status}`);
  }
  return res.json();
}</code></pre>
            <p><strong>TanStack Query</strong> lo phần khó: đang tải, lỗi, cache, tải lại. Bọc ứng dụng trong <code>QueryClientProvider</code> ở <code>app/_layout.tsx</code>, sau đó:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// Đọc dữ liệu
const { data, isLoading, isError, refetch, isRefetching } = useQuery({
  queryKey: ['products'],
  queryFn: () =&gt; api&lt;Product[]&gt;('/products'),
});

// Ghi dữ liệu, xong thì làm mới danh sách đơn hàng
const queryClient = useQueryClient();
const createOrder = useMutation({
  mutationFn: (body: NewOrder) =&gt;
    api('/orders', { method: 'POST', body: JSON.stringify(body) }),
  onSuccess: () =&gt; queryClient.invalidateQueries({ queryKey: ['orders'] }),
});

// Cuộn vô hạn cho lịch sử đơn hàng
const orders = useInfiniteQuery({
  queryKey: ['orders'],
  initialPageParam: 1,
  queryFn: ({ pageParam }) =&gt; api&lt;Order[]&gt;(`/orders?page=${pageParam}`),
  getNextPageParam: (lastPage, pages) =&gt; (lastPage.length &lt; 20 ? undefined : pages.length + 1),
});
// &lt;FlatList data={orders.data?.pages.flat()} onEndReached={() =&gt; orders.hasNextPage &amp;&amp; orders.fetchNextPage()} /&gt;</code></pre>
            <p style="margin-bottom: 0;">Luôn xử lý đủ <strong>4 trạng thái</strong> trên màn hình: đang tải, lỗi (kèm nút thử lại), rỗng, có dữ liệu.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 05: CSDL, stored procedure, API NestJS &amp; kết nối ứng dụng</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">▶ Video 05: Dựng API LHU Food gọi stored procedure bằng mssql</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Giáo trình &amp; tài liệu dự án</p>
            <a href="{{LINK_GIAO_TRINH}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📘 Giáo trình nội bộ – Chương 5: Thiết kế CSDL, stored procedure, API NestJS và kết nối ứng dụng</span><br>
                <span style="color: #6c757d; font-size: 13px;">Lý thuyết chi tiết, mã nguồn LHU Food và bài tập hướng dẫn theo dự án ở cuối Chương 5 (file Word).</span>
            </a>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đọc SRS mục 5.3 (M02), 5.5 (F04.1, F04.2), mục 7 (bảng, script), mục 8 (danh mục API). User story của buổi: US-G01, US-G03, US-G07, US-C04 (bản đầu, chưa có giao dịch), US-C06.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://www.npmjs.com/package/mssql" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 mssql (node-mssql)</span><br>
                <span style="color: #6c757d; font-size: 13px;">Connection pool, kiểu dữ liệu tham số, gọi stored procedure với <code>execute</code>.</span>
            </a>
            <a href="https://docs.nestjs.com/controllers" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - Controllers, Providers, Validation</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cấu trúc module, controller, service và kiểm tra dữ liệu bằng DTO.</span>
            </a>
            <a href="https://tanstack.com/query/latest/docs/framework/react/overview" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 TanStack Query</span><br>
                <span style="color: #6c757d; font-size: 13px;">useQuery, useMutation, useInfiniteQuery và invalidate cache.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): API LHU Food</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Chạy script tạo bảng (mục 2.2) và dữ liệu mẫu trong SSMS; vẽ ERD hoàn chỉnh.</li>
                <li>Viết <code>sp_Product_GetList</code>, <code>sp_Product_GetById</code>, <code>sp_Category_GetList</code>, <code>sp_Order_Create</code> (bản đơn giản, chưa có giao dịch); chạy thử từng thủ tục bằng <code>EXEC</code>.</li>
                <li>Tạo <code>DatabaseService</code>, module <code>products</code> và <code>orders</code> trong NestJS; bật Swagger; thử API bằng Swagger.</li>
                <li>Trong app: tạo <code>lib/api.ts</code>, bọc <code>QueryClientProvider</code>, thay dữ liệu giả ở Trang chủ và Chi tiết món bằng <code>useQuery</code>.</li>
                <li>Nút "Xác nhận đặt hàng" gọi <code>useMutation</code>; đặt xong xóa giỏ hàng và chuyển sang tab Đơn hàng.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Lịch sử đơn hàng</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Viết thủ tục <code>sp_Order_GetHistory</code> (tham số <code>@UserId</code>, <code>@Page</code>, <code>@PageSize</code>, sắp xếp mới nhất trước), endpoint <code>GET /orders?page=</code> và màn hình Lịch sử đơn hàng cuộn vô hạn.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> mã backend không có câu SQL trực tiếp; cuộn tới cuối tự tải trang tiếp và dừng khi hết dữ liệu; có đủ trạng thái đang tải, lỗi kèm nút thử lại, rỗng.</p>
            <a href="{{LINK_NOP_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li><strong>ERD hoàn chỉnh</strong> của đề tài (file nguồn + ảnh) trong <code>docs/</code>.</li>
                <li><strong>Danh mục stored procedure</strong>: tên, tham số, kết quả trả về, mã lỗi; và script tạo thủ tục trong repo.</li>
                <li>API của nhóm có Swagger; app thay toàn bộ dữ liệu giả bằng API thật.</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Dán một stored procedure do AI sinh ra cho nhóm của bạn và chỉ ra ít nhất một điểm bạn đã phải sửa (thiếu kiểm tra, sai kiểu dữ liệu, thiếu phân trang…). Vì sao AI dễ bỏ sót điểm đó?</p>
            <a href="{{LINK_DIEN_DAN_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập thiết kế CSDL, stored procedure, DatabaseService với mssql và TanStack Query.</p>
            <a href="{{LINK_QUIZ_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 05</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>App báo "Network request failed":</strong> đang dùng <code>localhost</code> trên điện thoại; hoặc điện thoại và máy tính khác mạng; hoặc tường lửa chặn cổng API. Thử mở <code>http://&lt;IP&gt;:3000/api</code> bằng trình duyệt trên điện thoại trước.</p>
        <p><strong>API không kết nối được SQL Server:</strong> kiểm tra SQL Server đã bật TCP/IP và đăng nhập bằng SQL Server Authentication; tên server, cổng và mật khẩu trong <code>.env</code> đúng.</p>
        <p><strong>Lỗi "Could not find stored procedure":</strong> thủ tục chưa được tạo trong đúng CSDL, hoặc tên gọi trong <code>execute()</code> sai chính tả.</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu tham số OUTPUT của stored procedure và cách đọc bằng <code>request.output()</code> trong mssql.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu đổi tên cột <code>Price</code> thành <code>UnitPrice</code> trong bảng <code>Products</code>, bạn phải sửa những file nào? Câu trả lời đúng nên là: các stored procedure liên quan, không phải mã NestJS.</p>
    </div>
</details>
