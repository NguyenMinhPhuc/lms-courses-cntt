# Chương 7. CSDL SQL Server nâng cao và đồng bộ dữ liệu qua backend

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Bảo vệ toàn vẹn dữ liệu bằng ràng buộc và tăng tốc truy vấn bằng chỉ mục.
- Viết stored procedure có giao dịch, xử lý lỗi và chống tranh chấp khi nhiều người thao tác cùng lúc.
- Viết thủ tục báo cáo và quản lý script cơ sở dữ liệu theo phiên bản.
- Đồng bộ dữ liệu giữa ứng dụng và server: cache, optimistic update, lưu trạng thái tạm trên thiết bị.

## 7.1. Toàn vẹn dữ liệu

### 7.1.1. Vì sao đặt quy tắc ở cơ sở dữ liệu

Một quy tắc như "tồn kho không âm" có thể được kiểm tra ở ứng dụng, ở API và ở CSDL. Kiểm tra ở ứng dụng giúp người dùng sửa lỗi nhanh; kiểm tra ở API chặn request sai; nhưng chỉ **ràng buộc ở CSDL** mới chặn được mọi nguồn ghi dữ liệu: ứng dụng mobile, ứng dụng web của nhóm, script nhập liệu, hay một thủ tục viết sót điều kiện.

### 7.1.2. Các loại ràng buộc

| Ràng buộc | Tác dụng | Ví dụ trong LHU Food |
|---|---|---|
| `PRIMARY KEY` | Định danh duy nhất mỗi dòng | `OrderId`, `(OrderId, ProductId)` |
| `FOREIGN KEY` | Giá trị phải tồn tại ở bảng khác | `Orders.UserId` → `Users.UserId` |
| `UNIQUE` | Không trùng | `Users.Email` |
| `CHECK` | Điều kiện trên giá trị | `Stock >= 0`, `Quantity > 0` |
| `DEFAULT` | Giá trị mặc định khi không truyền | `Status = N'pending'`, `CreatedAt = SYSDATETIME()` |
| `NOT NULL` | Bắt buộc có giá trị | `Products.Name` |

Đặt tên ràng buộc theo quy ước (`PK_`, `FK_`, `UQ_`, `CK_`, `DF_`) để thông báo lỗi dễ đọc và dễ xóa/sửa sau này.

`database/04-stock-reports.sql` (phần ràng buộc):

```sql
ALTER TABLE Products ADD Stock INT NOT NULL
  CONSTRAINT DF_Products_Stock DEFAULT 0
  CONSTRAINT CK_Products_Stock CHECK (Stock >= 0);

ALTER TABLE Orders ADD CONSTRAINT CK_Orders_Status
  CHECK (Status IN (N'pending', N'preparing', N'ready', N'completed', N'cancelled'));
```

Khi thêm cột `NOT NULL` vào bảng đã có dữ liệu, bắt buộc kèm `DEFAULT` để các dòng cũ có giá trị.

## 7.2. Chỉ mục

### 7.2.1. Chỉ mục là gì

**Chỉ mục (index)** giống mục lục của một cuốn sách: thay vì đọc toàn bộ bảng, SQL Server tra chỉ mục để đến thẳng các dòng cần tìm.

- **Clustered index:** sắp xếp chính dữ liệu của bảng; mỗi bảng có tối đa một. Khóa chính mặc định tạo clustered index.
- **Nonclustered index:** cấu trúc riêng trỏ tới dữ liệu; một bảng có thể có nhiều.
- **Filtered index:** chỉ mục chỉ chứa các dòng thỏa điều kiện, nhỏ và nhanh hơn.

### 7.2.2. Chọn chỉ mục theo thủ tục

Nhìn vào điều kiện `WHERE` và `ORDER BY` của các thủ tục được gọi nhiều nhất:

| Thủ tục | Điều kiện | Chỉ mục phù hợp |
|---|---|---|
| `sp_Order_GetHistory` | `WHERE UserId = @UserId ORDER BY CreatedAt DESC` | `(UserId, CreatedAt DESC)` |
| `sp_Product_GetList` | `WHERE IsAvailable = 1 AND CategoryId = @CategoryId` | `(CategoryId) WHERE IsAvailable = 1` |

```sql
CREATE INDEX IX_Orders_UserId_CreatedAt ON Orders (UserId, CreatedAt DESC);
CREATE INDEX IX_Products_CategoryId ON Products (CategoryId) WHERE IsAvailable = 1;
```

Mỗi chỉ mục làm thao tác `INSERT`/`UPDATE` chậm thêm một chút và tốn dung lượng, nên chỉ tạo khi có truy vấn thật cần nó. Trong SSMS, bật **Include Actual Execution Plan** khi chạy thủ tục để xem SQL Server có dùng chỉ mục hay đang quét toàn bảng (Table Scan).

## 7.3. Giao dịch trong stored procedure

### 7.3.1. Khái niệm và tính chất ACID

**Giao dịch (transaction)** là một nhóm câu lệnh được thực hiện như một đơn vị. Giao dịch đảm bảo bốn tính chất **ACID**:

- **Atomicity (nguyên tử):** tất cả thành công hoặc không có gì thay đổi.
- **Consistency (nhất quán):** dữ liệu luôn thỏa các ràng buộc sau giao dịch.
- **Isolation (cô lập):** các giao dịch đồng thời không nhìn thấy trạng thái dở dang của nhau.
- **Durability (bền vững):** đã `COMMIT` thì dữ liệu được lưu kể cả khi server khởi động lại.

Đặt hàng gồm ba thao tác: tạo `Orders`, tạo `OrderItems`, trừ `Stock`. Phiên bản ở Chương 5 thiếu giao dịch, nên nếu thao tác sau lỗi thì dữ liệu dở dang vẫn được lưu.

### 7.3.2. Khuôn mẫu xử lý lỗi

```sql
SET XACT_ABORT ON;
BEGIN TRY
  BEGIN TRAN;
  -- các câu lệnh thay đổi dữ liệu
  COMMIT;
END TRY
BEGIN CATCH
  IF @@TRANCOUNT > 0 ROLLBACK;
  THROW;
END CATCH
```

- `SET XACT_ABORT ON`: khi có lỗi thời gian chạy, SQL Server tự hủy toàn bộ giao dịch; tránh trường hợp giao dịch "treo" giữa chừng.
- `@@TRANCOUNT > 0`: chỉ `ROLLBACK` khi đang có giao dịch mở.
- `THROW;` (không tham số) ném lại **đúng lỗi gốc**, giữ nguyên mã như 50409, để `DatabaseService` (Chương 5) chuyển thành mã HTTP.

### 7.3.3. Tranh chấp đồng thời: suất cơm cuối cùng

Giả sử món còn 1 suất và hai khách cùng đặt trong cùng một thời điểm. Nếu cả hai giao dịch cùng đọc `Stock = 1` trước khi bên nào kịp trừ, cả hai đều thấy "đủ hàng" và tồn kho bị trừ thành -1 (hoặc một giao dịch lỗi ở ràng buộc `CHECK` với thông báo khó hiểu).

Gợi ý khóa `WITH (UPDLOCK, HOLDLOCK)` khi đọc tồn kho:

- `UPDLOCK`: đặt khóa cập nhật lên các dòng đọc được; giao dịch khác muốn khóa cập nhật cùng dòng phải chờ.
- `HOLDLOCK`: giữ khóa tới hết giao dịch.

Kết quả: giao dịch thứ hai chờ giao dịch thứ nhất `COMMIT`, sau đó đọc `Stock = 0` và báo lỗi 50409 rõ ràng.

### 7.3.4. Thủ tục đặt hàng hoàn chỉnh

```sql
CREATE OR ALTER PROCEDURE sp_Order_Create
  @UserId    INT,
  @Note      NVARCHAR(200) = NULL,
  @ItemsJson NVARCHAR(MAX)
AS
BEGIN
  SET NOCOUNT ON;
  SET XACT_ABORT ON;
  IF ISJSON(@ItemsJson) = 0
    THROW 50400, N'Danh sách món không hợp lệ', 1;

  -- Gộp món trùng trong JSON thành một dòng
  DECLARE @Items TABLE (ProductId INT PRIMARY KEY, Quantity INT NOT NULL);
  INSERT INTO @Items (ProductId, Quantity)
  SELECT productId, SUM(quantity)
  FROM OPENJSON(@ItemsJson) WITH (productId INT '$.productId', quantity INT '$.quantity')
  GROUP BY productId;

  IF NOT EXISTS (SELECT 1 FROM @Items) OR EXISTS (SELECT 1 FROM @Items WHERE Quantity <= 0)
    THROW 50400, N'Số lượng món không hợp lệ', 1;

  BEGIN TRY
    BEGIN TRAN;

    IF EXISTS (
      SELECT 1 FROM @Items i
      LEFT JOIN Products p WITH (UPDLOCK, HOLDLOCK) ON p.ProductId = i.ProductId
      WHERE p.ProductId IS NULL OR p.IsAvailable = 0 OR p.Stock < i.Quantity)
      THROW 50409, N'Có món đã hết hoặc không đủ số lượng', 1;

    DECLARE @OrderId INT;
    INSERT INTO Orders (UserId, Note) VALUES (@UserId, @Note);
    SET @OrderId = CAST(SCOPE_IDENTITY() AS INT);

    INSERT INTO OrderItems (OrderId, ProductId, Quantity, UnitPrice)
    SELECT @OrderId, i.ProductId, i.Quantity, p.Price
    FROM @Items i JOIN Products p ON p.ProductId = i.ProductId;

    UPDATE p SET p.Stock = p.Stock - i.Quantity
    FROM Products p JOIN @Items i ON i.ProductId = p.ProductId;

    COMMIT;
    SELECT @OrderId AS orderId;
  END TRY
  BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    THROW;
  END CATCH
END;
GO
```

Biến bảng `@Items` có khóa chính `ProductId` nên tự gộp món trùng; giá luôn lấy từ `Products`. Backend NestJS không thay đổi: `OrdersService.create` vẫn chỉ gọi một thủ tục.

### 7.3.5. Hủy đơn và hoàn tồn kho

Áp dụng cùng khuôn mẫu cho thao tác ngược lại:

```sql
CREATE OR ALTER PROCEDURE sp_Order_Cancel
  @OrderId INT, @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  SET XACT_ABORT ON;
  BEGIN TRY
    BEGIN TRAN;
    IF NOT EXISTS (SELECT 1 FROM Orders WITH (UPDLOCK)
                   WHERE OrderId = @OrderId AND UserId = @UserId AND Status = N'pending')
      THROW 50409, N'Chỉ hủy được đơn của bạn khi đơn chưa được chuẩn bị', 1;

    UPDATE Orders SET Status = N'cancelled' WHERE OrderId = @OrderId;

    UPDATE p SET p.Stock = p.Stock + oi.Quantity
    FROM Products p JOIN OrderItems oi ON oi.ProductId = p.ProductId
    WHERE oi.OrderId = @OrderId;

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    THROW;
  END CATCH
END;
GO
```

Điều kiện `UserId = @UserId` đảm bảo người dùng chỉ hủy được đơn của chính mình; `@UserId` được backend lấy từ token (Chương 6).

### 7.3.6. Tham số kiểu bảng (tùy chọn)

Thay cho chuỗi JSON, SQL Server hỗ trợ **table-valued parameter**: khai báo kiểu bảng (`CREATE TYPE OrderItemType AS TABLE (...)`), thủ tục nhận tham số `@Items OrderItemType READONLY`, và thư viện `mssql` truyền bằng `new sql.Table()`. Cách này có kiểu dữ liệu chặt chẽ hơn JSON nhưng phức tạp hơn khi khai báo; học phần chấp nhận cả hai cách.

## 7.4. Thủ tục báo cáo

### 7.4.1. Doanh thu theo ngày

```sql
CREATE OR ALTER PROCEDURE sp_Report_RevenueByDay
  @FromDate DATE, @ToDate DATE
AS
BEGIN
  SET NOCOUNT ON;
  IF @FromDate > @ToDate
    THROW 50400, N'Khoảng thời gian không hợp lệ', 1;

  SELECT CAST(o.CreatedAt AS DATE)       AS day,
         COUNT(DISTINCT o.OrderId)       AS orderCount,
         SUM(oi.Quantity * oi.UnitPrice) AS revenue
  FROM Orders o
  JOIN OrderItems oi ON oi.OrderId = o.OrderId
  WHERE o.Status <> N'cancelled'
    AND o.CreatedAt >= @FromDate
    AND o.CreatedAt < DATEADD(DAY, 1, @ToDate)
  GROUP BY CAST(o.CreatedAt AS DATE)
  ORDER BY day;
END;
GO
```

Điều kiện `CreatedAt < DATEADD(DAY, 1, @ToDate)` lấy trọn ngày cuối, kể cả đơn đặt lúc 23:59. Không dùng `CAST(o.CreatedAt AS DATE) BETWEEN ...` trong `WHERE`, vì biến đổi cột làm SQL Server khó dùng chỉ mục.

### 7.4.2. Món bán chạy

```sql
CREATE OR ALTER PROCEDURE sp_Report_TopProducts
  @FromDate DATE, @ToDate DATE, @Top INT = 5
AS
BEGIN
  SET NOCOUNT ON;
  SELECT TOP (@Top) p.ProductId AS id, p.Name AS name, SUM(oi.Quantity) AS quantity
  FROM OrderItems oi
  JOIN Orders o   ON o.OrderId = oi.OrderId
  JOIN Products p ON p.ProductId = oi.ProductId
  WHERE o.Status <> N'cancelled'
    AND o.CreatedAt >= @FromDate AND o.CreatedAt < DATEADD(DAY, 1, @ToDate)
  GROUP BY p.ProductId, p.Name
  ORDER BY quantity DESC;
END;
GO
```

### 7.4.3. API báo cáo chỉ dành cho nhân viên

```ts
@Controller('reports')
@UseGuards(AuthGuard, RolesGuard)
@Roles(['staff'])
export class ReportsController {
  constructor(private readonly db: DatabaseService) {}

  @Get('revenue')
  revenue(@Query('from') from: string, @Query('to') to: string) {
    return this.db.execute('sp_Report_RevenueByDay', {
      FromDate: { type: sql.Date, value: new Date(from) },
      ToDate: { type: sql.Date, value: new Date(to) },
    });
  }
}
```

Đặt `@Roles` ở cấp class áp dụng cho mọi endpoint trong controller; khi đó `RolesGuard` (Chương 6) cần đọc metadata bằng `reflector.getAllAndOverride(Roles, [context.getHandler(), context.getClass()])` thay cho `reflector.get` chỉ đọc ở hàm.

## 7.5. Script CSDL theo phiên bản

### 7.5.1. Tổ chức thư mục

```text
database/
├── 01-tables.sql          bảng và ràng buộc ban đầu
├── 02-procedures.sql      thủ tục sản phẩm, đơn hàng
├── 03-auth.sql            Users, RefreshTokens, thủ tục xác thực
├── 04-stock-reports.sql   tồn kho, chỉ mục, thủ tục báo cáo
└── 99-seed.sql            dữ liệu mẫu
```

Quy tắc:

- Chạy lần lượt từ `01` đến `99` trên một CSDL trống phải tạo ra đúng CSDL của nhóm.
- Thay đổi cấu trúc thì **thêm file mới** (`05-...sql`), không sửa file đã được các thành viên chạy.
- Thủ tục dùng `CREATE OR ALTER` nên chạy lại nhiều lần không lỗi.
- Script thay đổi bảng nên kiểm tra trước khi chạy để có thể chạy lại an toàn:

```sql
IF COL_LENGTH('dbo.Products', 'Stock') IS NULL
  ALTER TABLE Products ADD Stock INT NOT NULL CONSTRAINT DF_Products_Stock DEFAULT 0;
```

### 7.5.2. Vì sao quan trọng

- Mọi thành viên có cùng CSDL; lỗi "máy em chạy được" giảm hẳn.
- Chương 11 triển khai lên Windows Server của Khoa bằng chính các script này.
- Script là minh chứng CLO2 khi chấm cuối kỳ: CSDL phải dựng lại được từ đầu.

## 7.6. Đồng bộ ứng dụng với server

### 7.6.1. Nguồn dữ liệu chuẩn

Trong học phần, **nguồn dữ liệu chuẩn (source of truth) luôn là SQL Server**. Ứng dụng không có CSDL trên thiết bị; những gì ứng dụng giữ chỉ là bản sao tạm:

| Dữ liệu trên thiết bị | Nơi lưu | Tính chất |
|---|---|---|
| Cache dữ liệu server (thực đơn, đơn hàng) | Bộ nhớ của TanStack Query | Tạm thời, mất khi tắt app, tải lại từ API |
| Giỏ hàng chưa đặt | AsyncStorage (Zustand `persist`) | "Ý định mua" của riêng máy; server kiểm tra lại khi đặt |
| Token đăng nhập | SecureStore | Bí mật, mã hóa |

### 7.6.2. Độ "tươi" của cache

TanStack Query coi dữ liệu là cũ ngay sau khi tải (`staleTime: 0`) và tự tải lại khi màn hình được mở lại. Với dữ liệu ít thay đổi như danh mục món, có thể đặt `staleTime` dài hơn để giảm số lần gọi API:

```ts
useQuery({ queryKey: ['categories'], queryFn: () => api('/categories'), staleTime: 5 * 60 * 1000 });
```

Dữ liệu thay đổi do người khác (trạng thái đơn hàng) không dựa vào `staleTime`, mà được làm mới bằng sự kiện realtime (Chương 9).

### 7.6.3. Optimistic update

**Cập nhật lạc quan** đổi giao diện ngay khi người dùng thao tác, gửi API ở nền, và hoàn tác nếu API lỗi. Phù hợp với thao tác nhỏ, hầu như luôn thành công: thêm yêu thích, đánh dấu đã đọc.

```ts
export function useToggleFavorite() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ productId, liked }: { productId: number; liked: boolean }) =>
      api(`/favorites/${productId}`, { method: liked ? 'DELETE' : 'POST' }),
    onMutate: async ({ productId, liked }) => {
      await queryClient.cancelQueries({ queryKey: ['favorites'] });
      const previous = queryClient.getQueryData<number[]>(['favorites']);
      queryClient.setQueryData<number[]>(['favorites'], (old = []) =>
        liked ? old.filter((id) => id !== productId) : [...old, productId],
      );
      return { previous };
    },
    onError: (_err, _vars, context) => {
      queryClient.setQueryData(['favorites'], context?.previous);
      Alert.alert('Không cập nhật được', 'Vui lòng kiểm tra kết nối mạng.');
    },
    onSettled: () => queryClient.invalidateQueries({ queryKey: ['favorites'] }),
  });
}
```

- `cancelQueries`: hủy lần tải đang chạy để nó không ghi đè lên giá trị lạc quan.
- `onMutate` trả về `previous` để `onError` hoàn tác.
- `onSettled`: dù thành công hay lỗi, tải lại để khớp với server.

**Không** dùng optimistic update cho đặt hàng: kết quả phụ thuộc tồn kho mà chỉ server biết, nên phải chờ server trả lời.

### 7.6.4. Giữ giỏ hàng khi tắt ứng dụng

```ts
import AsyncStorage from '@react-native-async-storage/async-storage';
import { create } from 'zustand';
import { createJSONStorage, persist } from 'zustand/middleware';

export const useCart = create<CartState>()(
  persist(
    (set, get) => ({
      items: [],
      // add, decrease, remove, clear, total, count như Chương 4
    }),
    {
      name: 'lhufood-cart',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({ items: state.items }),   // chỉ lưu dữ liệu, không lưu hàm
    },
  ),
);
```

Cú pháp `create<CartState>()(persist(...))` có thêm một cặp ngoặc so với Chương 4; đây là yêu cầu của Zustand khi dùng middleware với TypeScript. Khi đăng xuất, gọi `useCart.getState().clear()` để giỏ hàng của người này không sang người khác trên cùng máy.

## 7.7. Mã nguồn bổ sung của chương

`database/05-favorites.sql`:

```sql
CREATE TABLE Favorites (
  UserId    INT NOT NULL REFERENCES Users(UserId),
  ProductId INT NOT NULL REFERENCES Products(ProductId),
  CreatedAt DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
  CONSTRAINT PK_Favorites PRIMARY KEY (UserId, ProductId)
);
GO

CREATE OR ALTER PROCEDURE sp_Favorite_GetList @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  SELECT ProductId AS productId FROM Favorites WHERE UserId = @UserId ORDER BY CreatedAt DESC;
END;
GO
```

Khóa chính `(UserId, ProductId)` chặn một người thêm trùng một món. Thủ tục thêm và xóa là bài tập của chương.

## Tóm tắt chương

- Ràng buộc ở CSDL chặn dữ liệu sai từ mọi nguồn; đặt tên ràng buộc theo quy ước.
- Chỉ mục chọn theo `WHERE`/`ORDER BY` của thủ tục hay dùng; kiểm tra bằng execution plan.
- Giao dịch: `XACT_ABORT`, `TRY...CATCH`, `ROLLBACK`, `THROW;`; dùng `UPDLOCK, HOLDLOCK` để chống tranh chấp tồn kho.
- Thủ tục báo cáo lọc theo khoảng thời gian mà không biến đổi cột; API báo cáo chỉ cho `staff`.
- Script CSDL đánh số, thêm file mới khi thay đổi, chạy lại được từ đầu.
- SQL Server là nguồn dữ liệu chuẩn; ứng dụng chỉ giữ cache, giỏ hàng tạm và token; optimistic update cho thao tác nhỏ.

## Câu hỏi ôn tập

1. Vì sao ràng buộc `CHECK (Stock >= 0)` vẫn cần dù API đã kiểm tra tồn kho?
2. Khi nào nên dùng filtered index? Cho ví dụ.
3. Giải thích bốn tính chất ACID bằng ví dụ đặt hàng.
4. Điều gì xảy ra nếu bỏ `WITH (UPDLOCK, HOLDLOCK)` khỏi `sp_Order_Create` và hai người cùng đặt suất cuối?
5. Vì sao dùng `THROW;` không tham số trong khối `CATCH`?
6. Vì sao không dùng optimistic update cho thao tác đặt hàng?

## Bài tập

1. **Món yêu thích.** Viết `sp_Favorite_Add` (không lỗi nếu đã tồn tại), `sp_Favorite_Remove`; API `POST/DELETE /favorites/:productId`, `GET /favorites`; nút trái tim dùng optimistic update như mục 7.6.3.
2. **Hủy đơn.** Thêm endpoint `POST /orders/:id/cancel` gọi `sp_Order_Cancel`; nút "Hủy đơn" chỉ hiện khi đơn đang `pending`. Kiểm tra tồn kho được hoàn lại.
3. **Màn hình Thống kê.** Màn hình cho nhân viên hiển thị doanh thu 7 ngày gần nhất và 5 món bán chạy, gọi hai thủ tục báo cáo.
4. **Kiểm tra tranh chấp.** Viết script mở hai phiên SSMS cùng gọi `sp_Order_Create` cho món còn 1 suất; ghi lại kết quả của từng phiên và giải thích.

## Tài liệu tham khảo

- Microsoft Learn - Transactions (Transact-SQL): https://learn.microsoft.com/sql/t-sql/language-elements/transactions-transact-sql
- Microsoft Learn - TRY...CATCH (Transact-SQL): https://learn.microsoft.com/sql/t-sql/language-elements/try-catch-transact-sql
- Microsoft Learn - SET XACT_ABORT: https://learn.microsoft.com/sql/t-sql/statements/set-xact-abort-transact-sql
- Microsoft Learn - Table hints: https://learn.microsoft.com/sql/t-sql/queries/hints-transact-sql-table
- Microsoft Learn - Indexes: https://learn.microsoft.com/sql/relational-databases/indexes/indexes
- TanStack Query - Optimistic Updates: https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates
- Zustand - persist middleware: https://zustand.docs.pmnd.rs/middlewares/persist
