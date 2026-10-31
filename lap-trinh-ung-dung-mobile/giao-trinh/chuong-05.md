# Chương 5. Thiết kế CSDL, stored procedure, API NestJS và kết nối ứng dụng

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Hoàn thiện thiết kế cơ sở dữ liệu SQL Server từ ERD sơ bộ.
- Viết stored procedure có tham số, phân trang và báo lỗi bằng mã tự đặt.
- Xây dựng REST API NestJS chỉ truy cập dữ liệu qua stored procedure bằng thư viện `mssql`.
- Kết nối ứng dụng React Native với API và quản lý dữ liệu server bằng TanStack Query.

## 5.1. Kiến trúc ba lớp của LHU Food

```text
Ứng dụng React Native
   │  HTTP + JSON  (TanStack Query: useQuery, useMutation)
   ▼
API NestJS
   Controller  →  Service  →  DatabaseService
   │  mssql: request.input(...) + request.execute('sp_...')
   ▼
SQL Server
   Stored procedure  →  Bảng
```

Mỗi lớp có một trách nhiệm và một giới hạn:

| Lớp | Được làm | Không được làm |
|---|---|---|
| Ứng dụng | Hiển thị, kiểm tra dữ liệu nhập, gọi API | Kết nối trực tiếp SQL Server; giữ bí mật |
| API NestJS | Xác thực, phân quyền, kiểm tra dữ liệu, gọi thủ tục | Viết câu lệnh SQL; dùng ORM để sinh truy vấn |
| Stored procedure | Toàn bộ câu lệnh đọc/ghi, ràng buộc nghiệp vụ trên dữ liệu | Biết gì về HTTP hay giao diện |

## 5.2. Hoàn thiện thiết kế cơ sở dữ liệu

### 5.2.1. Từ ERD sơ bộ đến lược đồ

Ở Chương 3, ERD sơ bộ có tên thực thể, khóa và quan hệ. Bước này bổ sung:

- **Kiểu dữ liệu:** `NVARCHAR` cho chuỗi tiếng Việt (có tiền tố `N` khi viết hằng chuỗi: `N'Cơm gà'`); `DECIMAL(12,0)` cho tiền đồng; `DATETIME2` cho thời gian; `BIT` cho đúng/sai.
- **Ràng buộc:** `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`, khóa ngoại `REFERENCES`.
- **Khóa chính tự tăng:** `INT IDENTITY(1,1)`.

### 5.2.2. Script tạo bảng

`database/01-tables.sql`:

```sql
CREATE TABLE Categories (
  CategoryId INT IDENTITY(1,1) PRIMARY KEY,
  Name       NVARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Products (
  ProductId   INT IDENTITY(1,1) PRIMARY KEY,
  CategoryId  INT NOT NULL REFERENCES Categories(CategoryId),
  Name        NVARCHAR(150) NOT NULL,
  Description NVARCHAR(500) NULL,
  Price       DECIMAL(12,0) NOT NULL CHECK (Price >= 0),
  ImageUrl    NVARCHAR(500) NULL,
  IsAvailable BIT NOT NULL DEFAULT 1
);

CREATE TABLE Orders (
  OrderId   INT IDENTITY(1,1) PRIMARY KEY,
  UserId    INT NOT NULL,                  -- khóa ngoại tới Users được thêm ở Chương 6
  Status    NVARCHAR(20) NOT NULL DEFAULT N'pending',
  Note      NVARCHAR(200) NULL,
  CreatedAt DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

CREATE TABLE OrderItems (
  OrderId   INT NOT NULL REFERENCES Orders(OrderId),
  ProductId INT NOT NULL REFERENCES Products(ProductId),
  Quantity  INT NOT NULL CHECK (Quantity > 0),
  UnitPrice DECIMAL(12,0) NOT NULL,
  PRIMARY KEY (OrderId, ProductId)
);
```

**Vì sao `OrderItems` lưu `UnitPrice`?** Giá món có thể thay đổi. Đơn hàng đã đặt phải giữ đúng giá tại thời điểm đặt, nên giá được chép vào chi tiết đơn.

**Vì sao khóa chính của `OrderItems` gồm hai cột?** Mỗi món chỉ xuất hiện một lần trong một đơn; đặt thêm thì tăng `Quantity`.

### 5.2.3. ERD hoàn chỉnh

Vẽ lại ERD bằng dbdiagram.io hoặc draw.io với đầy đủ kiểu dữ liệu, khóa và ký hiệu quan hệ. Đặt file nguồn và ảnh trong `docs/`. ERD là minh chứng chính cho CLO2 (thiết kế CSDL) và CLO3 (trình bày bằng đồ họa), và phải luôn khớp với script thật.

## 5.3. Stored procedure

### 5.3.1. Vì sao bắt buộc dùng stored procedure

1. **Tách logic dữ liệu khỏi mã backend.** Đổi câu truy vấn, thêm chỉ mục, tối ưu… mà không phải sửa và triển khai lại API.
2. **Phân quyền tối thiểu.** Tài khoản SQL Server của API chỉ cần quyền `EXECUTE`; nếu API bị lộ thông tin đăng nhập, kẻ tấn công cũng không đọc hay xóa trực tiếp được bảng (Chương 6).
3. **Chống SQL injection.** Giá trị luôn đi vào tham số có kiểu, không bao giờ ghép vào chuỗi lệnh.
4. **Một nơi duy nhất cho quy tắc dữ liệu**, dùng chung cho cả ứng dụng mobile và web của nhóm.

### 5.3.2. Quy ước

- Tên: `sp_<Thực thể>_<Hành động>`, ví dụ `sp_Product_GetList`, `sp_Order_Create` [3].
- Mở đầu bằng `SET NOCOUNT ON;` để không trả về thông điệp "n rows affected" thừa.
- Dùng `CREATE OR ALTER PROCEDURE` để chạy lại script nhiều lần không lỗi.
- Thủ tục trả dữ liệu cho ứng dụng **đặt bí danh cột theo camelCase** (`ProductId AS id`), để JSON từ API khớp với kiểu dữ liệu trong ứng dụng.
- Báo lỗi nghiệp vụ bằng `THROW` với mã từ 50000 trở lên. Quy ước của học phần: `50400` dữ liệu không hợp lệ, `50404` không tìm thấy, `50409` trùng lặp.
- Lệnh đứng ngay trước `THROW` phải kết thúc bằng dấu `;`.

### 5.3.3. Thủ tục đọc dữ liệu

`database/02-procedures.sql`:

```sql
CREATE OR ALTER PROCEDURE sp_Category_GetList
AS
BEGIN
  SET NOCOUNT ON;
  SELECT CategoryId AS id, Name AS name FROM Categories ORDER BY Name;
END;
GO

CREATE OR ALTER PROCEDURE sp_Product_GetList
  @CategoryId INT = NULL,
  @Page       INT = 1,
  @PageSize   INT = 20
AS
BEGIN
  SET NOCOUNT ON;
-- … (trích 15/42 dòng; mã đầy đủ ở Phụ lục A, mục A.1)
```

`OFFSET ... FETCH NEXT` (có từ SQL Server 2012) phân trang dựa trên `ORDER BY`. Luôn sắp xếp theo một cột duy nhất để trang sau không lặp lại phần tử của trang trước [2].

### 5.3.4. Thủ tục ghi dữ liệu

Danh sách món trong đơn được truyền vào thủ tục dưới dạng chuỗi JSON và đọc bằng `OPENJSON` (SQL Server 2016 trở lên). Giá món được lấy từ bảng `Products`, **không** tin giá do ứng dụng gửi lên [4].

```sql
CREATE OR ALTER PROCEDURE sp_Order_Create
  @UserId    INT,
  @Note      NVARCHAR(200) = NULL,
  @ItemsJson NVARCHAR(MAX)          -- [{"productId":1,"quantity":2}, ...]
AS
BEGIN
  SET NOCOUNT ON;
  IF ISJSON(@ItemsJson) = 0
    THROW 50400, N'Danh sách món không hợp lệ', 1;

  DECLARE @OrderId INT;
  INSERT INTO Orders (UserId, Note) VALUES (@UserId, @Note);
  SET @OrderId = CAST(SCOPE_IDENTITY() AS INT);

  INSERT INTO OrderItems (OrderId, ProductId, Quantity, UnitPrice)
  SELECT @OrderId, j.productId, j.quantity, p.Price
  FROM OPENJSON(@ItemsJson) WITH (productId INT '$.productId', quantity INT '$.quantity') AS j
  JOIN Products p ON p.ProductId = j.productId AND p.IsAvailable = 1;

  SELECT @OrderId AS orderId;
END;
GO
```

Phiên bản này chưa gói hai lệnh `INSERT` trong một **giao dịch**: nếu lệnh thứ hai lỗi, đơn hàng rỗng vẫn bị tạo. Chương 7 hoàn thiện thủ tục với `BEGIN TRAN`, `TRY...CATCH` và kiểm tra tồn kho.

### 5.3.5. Chạy thử trong SSMS

Viết xong thủ tục nào, chạy thử ngay trước khi viết API:

```sql
EXEC sp_Product_GetList @Page = 1, @PageSize = 5;
EXEC sp_Product_GetById @ProductId = 999;     -- phải báo lỗi 50404
EXEC sp_Order_Create @UserId = 1, @ItemsJson = N'[{"productId":1,"quantity":2}]';
```

### 5.3.6. Danh mục stored procedure

Mỗi nhóm duy trì bảng danh mục thủ tục trong `docs/procedures.md`:

| Thủ tục | Tham số | Kết quả | Mã lỗi |
|---|---|---|---|
| `sp_Product_GetList` | `@CategoryId` (tùy chọn), `@Page`, `@PageSize` | Danh sách món | 50400 |
| `sp_Product_GetById` | `@ProductId` | Một món | 50404 |
| `sp_Order_Create` | `@UserId`, `@Note`, `@ItemsJson` | `orderId` | 50400 |

## 5.4. API NestJS với mssql

### 5.4.1. Chuẩn bị

```bash
npx @nestjs/cli new lhu-food-api
cd lhu-food-api
npm install mssql @nestjs/config @nestjs/swagger class-validator class-transformer
npm install -D @types/mssql
```

File `.env` (thêm vào `.gitignore`) [1]:

```text
DB_SERVER=localhost
DB_NAME=LhuFood
DB_USER=lhufood_api
DB_PASSWORD=<mật khẩu>
PORT=3000
```

### 5.4.2. DatabaseService dùng chung

`src/database/database.service.ts`:

```ts
import {
  BadRequestException, ConflictException, Injectable, NotFoundException,
  OnModuleDestroy, OnModuleInit,
} from '@nestjs/common';
import * as sql from 'mssql';

export type SqlParam = { type: sql.ISqlType | (() => sql.ISqlType); value: unknown };

@Injectable()
export class DatabaseService implements OnModuleInit, OnModuleDestroy {
  private pool!: sql.ConnectionPool;

  async onModuleInit() {
    this.pool = await new sql.ConnectionPool({
      server: process.env.DB_SERVER!,
// … (trích 15/44 dòng; mã đầy đủ ở Phụ lục A, mục A.2)
```

`src/database/database.module.ts`:

```ts
import { Global, Module } from '@nestjs/common';
import { DatabaseService } from './database.service';

@Global()
@Module({ providers: [DatabaseService], exports: [DatabaseService] })
export class DatabaseModule {}
```

`@Global()` cho phép mọi module dùng `DatabaseService` mà không cần import lại. Nạp biến môi trường bằng `ConfigModule.forRoot()` trong `AppModule`, đặt trước `DatabaseModule` [1].

### 5.4.3. Module Products

Tham khảo [5].

`src/products/products.service.ts`:

```ts
import { Injectable } from '@nestjs/common';
import * as sql from 'mssql';
import { DatabaseService } from '../database/database.service';

@Injectable()
export class ProductsService {
  constructor(private readonly db: DatabaseService) {}

  findAll(page: number, categoryId?: number) {
    return this.db.execute('sp_Product_GetList', {
      CategoryId: { type: sql.Int, value: categoryId ?? null },
      Page: { type: sql.Int, value: page },
      PageSize: { type: sql.Int, value: 20 },
    });
  }

  async findOne(id: number) {
    const [product] = await this.db.execute('sp_Product_GetById', {
      ProductId: { type: sql.Int, value: id },
    });
    return product;
  }
}
```

`src/products/products.controller.ts`:

```ts
import { Controller, DefaultValuePipe, Get, Param, ParseIntPipe, Query } from '@nestjs/common';
import { ProductsService } from './products.service';

@Controller('products')
export class ProductsController {
  constructor(private readonly products: ProductsService) {}

  @Get()
  findAll(
    @Query('page', new DefaultValuePipe(1), ParseIntPipe) page: number,
    @Query('categoryId', new ParseIntPipe({ optional: true })) categoryId?: number,
  ) {
    return this.products.findAll(page, categoryId);
  }

  @Get(':id')
  findOne(@Param('id', ParseIntPipe) id: number) {
    return this.products.findOne(id);
  }
}
```

### 5.4.4. Module Orders và DTO

`src/orders/dto/create-order.dto.ts`:

```ts
import { Type } from 'class-transformer';
import { ArrayMinSize, IsInt, IsOptional, IsString, MaxLength, Min, ValidateNested } from 'class-validator';

class OrderItemDto {
  @IsInt() productId!: number;
  @IsInt() @Min(1) quantity!: number;
}

export class CreateOrderDto {
  @ValidateNested({ each: true })
  @Type(() => OrderItemDto)
  @ArrayMinSize(1)
  items!: OrderItemDto[];

  @IsOptional() @IsString() @MaxLength(200)
  note?: string;
}
```

`src/orders/orders.service.ts`:

```ts
@Injectable()
export class OrdersService {
  constructor(private readonly db: DatabaseService) {}

  async create(userId: number, dto: CreateOrderDto) {
    const [row] = await this.db.execute<{ orderId: number }>('sp_Order_Create', {
      UserId: { type: sql.Int, value: userId },
      Note: { type: sql.NVarChar(200), value: dto.note ?? null },
      ItemsJson: { type: sql.NVarChar(sql.MAX), value: JSON.stringify(dto.items) },
    });
    return row;
  }
}
```

Trước khi có đăng nhập (Chương 6), controller tạm truyền `userId = 1` ứng với một người dùng mẫu [5].

### 5.4.5. Cấu hình khởi động

`src/main.ts`:

```ts
import { ValidationPipe } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(new ValidationPipe({ whitelist: true, transform: true }));

  const config = new DocumentBuilder().setTitle('LHU Food API').setVersion('1.0').addBearerAuth().build();
  SwaggerModule.setup('api', app, SwaggerModule.createDocument(app, config));

  // 0.0.0.0: nhận kết nối từ điện thoại trong cùng mạng, không chỉ từ máy này
  await app.listen(process.env.PORT ?? 3000, '0.0.0.0');
}
bootstrap();
```

- `whitelist: true` loại bỏ các trường không khai báo trong DTO [6].
- Swagger tại `http://<IP>:3000/api` là "hợp đồng" giữa người làm backend và người làm mobile.

### 5.4.6. Vibe coding cho backend

Đưa ERD và danh mục thủ tục cho trợ lý AI để sinh thủ tục, service, controller. Sau đó **review bắt buộc**:

- Mỗi thủ tục có `SET NOCOUNT ON`, đủ tham số, kiểm tra tồn tại/hợp lệ, bí danh camelCase.
- Tìm trong thư mục `src/` các chuỗi `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `query(`: **không được còn**.
- Kiểu tham số khớp kiểu cột (`sql.NVarChar(150)` cho `NVARCHAR(150)`).

Trợ lý AI rất hay "tiện tay" dùng `request.query('SELECT ...')` hoặc gợi ý cài ORM. Đây là vi phạm quy tắc của học phần và bị trừ điểm CLO2.

## 5.5. Kết nối ứng dụng với API

### 5.5.1. Địa chỉ API

Khai báo trong file `.env` của dự án Expo:

```text
EXPO_PUBLIC_API_URL=http://192.168.1.10:3000
```

| Môi trường chạy | Địa chỉ dùng |
|---|---|
| Điện thoại thật qua Expo Go | IP LAN của máy chạy API (xem bằng `ipconfig`) |
| Android emulator | `http://10.0.2.2:3000` |
| Bản cài đặt cuối kỳ | Địa chỉ Windows Server của Khoa (Chương 11) |

`localhost` trên điện thoại là **chính điện thoại**, nên không dùng được. Nếu điện thoại không gọi được API, thử mở `http://<IP>:3000/api` bằng trình duyệt trên điện thoại; nếu không mở được, kiểm tra hai máy cùng mạng và Windows Firewall đã mở cổng 3000.

Biến có tiền tố `EXPO_PUBLIC_` được **đóng gói vào ứng dụng**; ai có file APK đều đọc được. Không bao giờ đặt mật khẩu, khóa bí mật vào đây.

### 5.5.2. Hàm gọi API tập trung

`lib/api.ts`:

```ts
const API_URL = process.env.EXPO_PUBLIC_API_URL;

export async function api<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...init?.headers },
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    const message = Array.isArray(body.message) ? body.message.join('\n') : body.message;
    throw new Error(message ?? `Lỗi ${res.status}`);
  }
  return res.json() as Promise<T>;
}
```

NestJS trả lỗi kiểm tra DTO dưới dạng mảng `message`; hàm trên gộp thành một chuỗi để hiển thị.

### 5.5.3. TanStack Query

TanStack Query quản lý **dữ liệu server**: trạng thái đang tải, lỗi, cache, tải lại khi cần. Cài đặt: `npx expo install @tanstack/react-query` [7].

`app/_layout.tsx`:

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Stack } from 'expo-router';

const queryClient = new QueryClient();

export default function RootLayout() {
  return (
    <QueryClientProvider client={queryClient}>
      <Stack>{/* các Stack.Screen như Chương 3 */}</Stack>
    </QueryClientProvider>
  );
}
```

`hooks/useProducts.ts`:

```ts
import { useQuery } from '@tanstack/react-query';
import { api } from '@/lib/api';

export type Product = { id: number; categoryId: number; name: string; price: number; imageUrl: string | null };

export function useProducts(categoryId?: number) {
  return useQuery({
    queryKey: ['products', categoryId ?? 'all'],
    queryFn: () => api<Product[]>(`/products${categoryId ? `?categoryId=${categoryId}` : ''}`),
  });
}
```

`queryKey` là "địa chỉ" của dữ liệu trong cache: cùng key thì dùng chung dữ liệu, khác key (khác danh mục) thì tải riêng.

### 5.5.4. Bốn trạng thái của màn hình dữ liệu

```tsx
export default function HomeScreen() {
  const { data, isLoading, isError, error, refetch, isRefetching } = useProducts();

  if (isLoading) return <ActivityIndicator style={{ marginTop: 32 }} />;
  if (isError) {
    return (
      <View style={{ padding: 16, gap: 8 }}>
        <Text>Không tải được thực đơn: {error.message}</Text>
        <Button title="Thử lại" onPress={() => refetch()} />
      </View>
    );
  }
  return (
    <FlatList
      data={data}
      keyExtractor={(item) => String(item.id)}
      renderItem={({ item }) => <ProductCard name={item.name} price={item.price} onAdd={() => {}} />}
      ListEmptyComponent={<Text>Hiện chưa có món nào.</Text>}
      refreshing={isRefetching}
      onRefresh={refetch}
    />
  );
}
```

Màn hình nào lấy dữ liệu từ server cũng phải xử lý đủ: **đang tải**, **lỗi kèm nút thử lại**, **rỗng**, **có dữ liệu**.

### 5.5.5. Ghi dữ liệu với useMutation

```tsx
const queryClient = useQueryClient();
const clear = useCart((s) => s.clear);

const createOrder = useMutation({
  mutationFn: (body: { items: { productId: number; quantity: number }[]; note?: string }) =>
    api<{ orderId: number }>('/orders', { method: 'POST', body: JSON.stringify(body) }),
  onSuccess: () => {
    clear();
    queryClient.invalidateQueries({ queryKey: ['orders'] });
    router.replace('/orders');
  },
  onError: (err) => Alert.alert('Đặt hàng thất bại', err.message),
});
```

`invalidateQueries` đánh dấu dữ liệu `['orders']` đã cũ; màn hình Đơn hàng sẽ tự tải lại.

### 5.5.6. Cuộn vô hạn

```tsx
const orders = useInfiniteQuery({
  queryKey: ['orders'],
  initialPageParam: 1,
  queryFn: ({ pageParam }) => api<Order[]>(`/orders?page=${pageParam}`),
  getNextPageParam: (lastPage, allPages) => (lastPage.length < 20 ? undefined : allPages.length + 1),
});

<FlatList
  data={orders.data?.pages.flat()}
  onEndReached={() => orders.hasNextPage && !orders.isFetchingNextPage && orders.fetchNextPage()}
  onEndReachedThreshold={0.5}
  ListFooterComponent={orders.isFetchingNextPage ? <ActivityIndicator /> : null}
/>
```

Trang trả về ít hơn kích thước trang (20) nghĩa là đã hết dữ liệu, `getNextPageParam` trả về `undefined` để dừng tải.

## Tóm tắt chương

- Ứng dụng → API → stored procedure → bảng; mỗi lớp có giới hạn rõ ràng.
- Thiết kế CSDL: kiểu dữ liệu phù hợp, ràng buộc, khóa; lưu giá tại thời điểm đặt; ERD luôn khớp script.
- Stored procedure: `SET NOCOUNT ON`, tham số có kiểu, phân trang `OFFSET/FETCH`, bí danh camelCase, `THROW` mã 50400/50404/50409.
- `DatabaseService.execute()` là cách duy nhất truy cập CSDL; mã lỗi thủ tục được chuyển thành mã HTTP.
- Ứng dụng dùng IP LAN (máy thật) hoặc `10.0.2.2` (emulator); TanStack Query quản lý dữ liệu server; màn hình luôn có đủ bốn trạng thái.

## Câu hỏi ôn tập

1. Nêu bốn lý do học phần bắt buộc truy cập dữ liệu qua stored procedure.
2. Vì sao `sp_Order_Create` lấy giá từ bảng `Products` mà không dùng giá ứng dụng gửi lên?
3. Phiên bản `sp_Order_Create` trong chương này có rủi ro gì khi lệnh `INSERT` thứ hai thất bại?
4. `DatabaseService` chuyển lỗi `50404` thành gì? Vì sao nên làm việc này ở một chỗ duy nhất?
5. Vì sao điện thoại không gọi được `http://localhost:3000`? Emulator Android dùng địa chỉ nào?
6. Vai trò của `queryKey` trong TanStack Query là gì?

## Bài tập

1. **Lịch sử đơn hàng.** Viết `sp_Order_GetHistory` (`@UserId`, `@Page`, `@PageSize`, mới nhất trước, trả kèm tổng tiền mỗi đơn), endpoint `GET /orders?page=` và màn hình cuộn vô hạn.
2. **Chi tiết đơn hàng.** Viết `sp_Order_GetById` trả thông tin đơn và danh sách món (gợi ý: thủ tục trả hai tập kết quả; đọc bằng `result.recordsets` của mssql), endpoint và màn hình chi tiết.
3. **Dự án nhóm.** Hoàn thiện ERD, danh mục stored procedure, script `database/*.sql` và API có Swagger cho các tính năng chính; thay toàn bộ dữ liệu giả trong ứng dụng.

## Tài liệu tham khảo

[1] tediousjs, “mssql: Microsoft SQL Server client for Node.js,” *npm*. Accessed: Oct. 30, 2026. [Online]. Available: https://www.npmjs.com/package/mssql

[2] Microsoft, “CREATE PROCEDURE (Transact-SQL),” *Microsoft Learn*. Accessed: Oct. 30, 2026. [Online]. Available: https://learn.microsoft.com/sql/t-sql/statements/create-procedure-transact-sql

[3] Microsoft, “THROW (Transact-SQL),” *Microsoft Learn*. Accessed: Oct. 30, 2026. [Online]. Available: https://learn.microsoft.com/sql/t-sql/language-elements/throw-transact-sql

[4] Microsoft, “OPENJSON (Transact-SQL),” *Microsoft Learn*. Accessed: Oct. 30, 2026. [Online]. Available: https://learn.microsoft.com/sql/t-sql/functions/openjson-transact-sql

[5] NestJS, “Controllers,” *NestJS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.nestjs.com/controllers

[6] NestJS, “OpenAPI (Swagger),” *NestJS Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.nestjs.com/openapi/introduction

[7] TanStack, “Overview,” *TanStack Query Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://tanstack.com/query/latest/docs/framework/react/overview
