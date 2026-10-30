# Bài 05: Thiết kế CSDL, stored procedure, API NestJS & kết nối ứng dụng
Từ màn hình điện thoại tới một dòng trong SQL Server

---

## Slide 1: Mục tiêu buổi học
**Nội dung chính**:
- Hoàn thiện thiết kế CSDL SQL Server và ERD
- Viết stored procedure cho các thao tác dữ liệu
- Xây API NestJS chỉ gọi stored procedure bằng `mssql`
- Kết nối ứng dụng với API bằng TanStack Query
**Ghi chú giảng viên**:
- 2 tiết lý thuyết, 3 tiết thực hành. CLO1, CLO2, CLO3.

---

## Slide 2: Dữ liệu đi qua những lớp nào?
**Nội dung chính**:
```text
App React Native   --HTTP + JSON-->   API NestJS
   Controller → Service → DatabaseService
   --mssql: input(...) + execute('sp_...')-->
SQL Server: Stored procedure → Bảng
```
- App không kết nối thẳng SQL Server
- API không viết câu SQL; chỉ gọi thủ tục có tham số

---

## Slide 3: Hoàn thiện thiết kế CSDL
**Nội dung chính**:
- Từ ERD sơ bộ (bài 03): thêm kiểu dữ liệu, khóa, ràng buộc
- `NVARCHAR` cho chuỗi tiếng Việt, `DECIMAL` cho tiền
- `CHECK (Price >= 0)`, `CHECK (Quantity > 0)`, `UNIQUE`
- OrderItems: khóa chính (OrderId, ProductId), lưu `UnitPrice`
**Hoạt động**: Hỏi lớp: vì sao OrderItems phải lưu giá tại thời điểm đặt?

---

## Slide 4: Bảng Products
**Nội dung chính**:
```sql
CREATE TABLE Products (
  ProductId   INT IDENTITY(1,1) PRIMARY KEY,
  CategoryId  INT NOT NULL REFERENCES Categories(CategoryId),
  Name        NVARCHAR(150) NOT NULL,
  Price       DECIMAL(12,0) NOT NULL CHECK (Price >= 0),
  ImageUrl    NVARCHAR(500) NULL,
  IsAvailable BIT NOT NULL DEFAULT 1
);
```

---

## Slide 5: Vì sao bắt buộc stored procedure?
**Nội dung chính**:
- Tách logic dữ liệu khỏi mã backend
- API chỉ cần quyền `EXECUTE`, không chạm trực tiếp vào bảng
- Giá trị đi qua tham số có kiểu → chống SQL injection
- Quy ước tên: `sp_<Thực thể>_<Hành động>`
**Ví dụ**:
- `sp_Product_GetList`, `sp_Product_GetById`, `sp_Order_Create`

---

## Slide 6: sp_Product_GetList có phân trang
**Nội dung chính**:
```sql
CREATE OR ALTER PROCEDURE sp_Product_GetList
  @CategoryId INT = NULL, @Page INT = 1, @PageSize INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  SELECT ProductId AS id, CategoryId AS categoryId, Name AS name, Price AS price
  FROM Products
  WHERE IsAvailable = 1 AND (@CategoryId IS NULL OR CategoryId = @CategoryId)
  ORDER BY ProductId
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
```

---

## Slide 7: Báo lỗi bằng THROW
**Nội dung chính**:
```sql
IF NOT EXISTS (SELECT 1 FROM Products WHERE ProductId = @ProductId)
  THROW 50404, N'Không tìm thấy món ăn', 1;
```
- Mã lỗi tự đặt từ 50000 trở lên
- Backend đọc `err.number` → trả HTTP phù hợp (50404 → 404)
- Chạy thử trong SSMS: `EXEC sp_Product_GetById @ProductId = 999;`

---

## Slide 8: DatabaseService với mssql
**Nội dung chính**:
```ts
async execute<T>(procedure: string, params: Record<string, Param> = {}) {
  const request = this.pool.request();
  for (const [name, p] of Object.entries(params)) {
    request.input(name, p.type, p.value);
  }
  const result = await request.execute<T>(procedure);
  return result.recordset;
}
```
- Một connection pool cho cả ứng dụng, cấu hình từ `.env`
**Ghi chú giảng viên**:
- Mã đầy đủ (onModuleInit, onModuleDestroy) ở mục 2.4 của bài học.

---

## Slide 9: Service gọi thủ tục
**Nội dung chính**:
```ts
findAll(page = 1, categoryId?: number) {
  return this.db.execute('sp_Product_GetList', {
    CategoryId: { type: sql.Int, value: categoryId ?? null },
    Page: { type: sql.Int, value: page },
    PageSize: { type: sql.Int, value: 20 },
  });
}
```
- Controller nhận request, DTO + ValidationPipe kiểm tra dữ liệu
- Swagger: tài liệu API cho người làm mobile

---

## Slide 10: Vibe coding cho backend
**Nội dung chính**:
- Đưa ERD cho Antigravity sinh thủ tục và service
- Review từng thủ tục: đủ tham số, `SET NOCOUNT ON`, kiểm tra tồn tại
- Tìm chuỗi `SELECT`, `INSERT` trong mã backend → phải không còn
**Ghi chú giảng viên**:
- AI rất hay "tiện tay" viết câu SQL thẳng trong service; đây là lỗi bị trừ điểm CLO2.

---

## Slide 11: Địa chỉ API trong ứng dụng
**Nội dung chính**:
- `.env`: `EXPO_PUBLIC_API_URL=http://192.168.1.10:3000`
- Điện thoại thật: IP LAN, **không** dùng localhost
- Android emulator: `10.0.2.2`
- Tường lửa Windows có thể chặn cổng API
- Không đặt bí mật vào biến `EXPO_PUBLIC_`

---

## Slide 12: TanStack Query
**Nội dung chính**:
```ts
const { data, isLoading, isError, refetch } = useQuery({
  queryKey: ['products'],
  queryFn: () => api<Product[]>('/products'),
});
const createOrder = useMutation({
  mutationFn: (body: NewOrder) => api('/orders', { method: 'POST', body: JSON.stringify(body) }),
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ['orders'] }),
});
```

---

## Slide 13: Cuộn vô hạn và 4 trạng thái màn hình
**Nội dung chính**:
- `useInfiniteQuery` + `FlatList onEndReached` cho lịch sử đơn hàng
- Luôn xử lý: **đang tải**, **lỗi** (có nút thử lại), **rỗng**, **có dữ liệu**
**Hoạt động**: Lớp chỉ ra trạng thái nào còn thiếu trên màn hình mẫu

---

## Slide 14: Thực hành có hướng dẫn
**Nội dung chính**:
- Chạy script tạo bảng và dữ liệu mẫu; vẽ ERD hoàn chỉnh
- Viết 4 thủ tục; chạy thử bằng EXEC
- DatabaseService, module products và orders, Swagger
- App: `lib/api.ts`, QueryClientProvider, useQuery, useMutation

---

## Slide 15: Thực hành không hướng dẫn & thử thách nhóm
**Nội dung chính**:
- **Cá nhân**: `sp_Order_GetHistory` + endpoint + màn hình cuộn vô hạn
- **Nhóm**: ERD hoàn chỉnh, danh mục stored procedure, script tạo thủ tục, API có Swagger, app dùng dữ liệu thật

---

## Slide 16: Tóm tắt
**Nội dung chính**:
- App → API → stored procedure → bảng
- Mọi câu SQL nằm trong thủ tục; API chỉ `execute` có tham số
- localhost trên điện thoại là chính điện thoại
- TanStack Query lo tải, lỗi, cache; bạn lo 4 trạng thái màn hình
**Hoạt động**: Làm quiz Bài 05 ở cuối trang bài học

---

## Slide 17: Tài liệu của buổi
**Đọc thêm**:
- Giáo trình nội bộ, Chương 5: Thiết kế CSDL, stored procedure, API NestJS và kết nối ứng dụng
- Bài tập hướng dẫn theo dự án LHU Food (cuối Chương 5)
- SRS LHU Food: mục 5.3, 5.5, 7 (dữ liệu), 8 (danh mục API)
**Ghi chú giảng viên**:
- Các file Word/Excel nằm ở mục Tài liệu của bài trên LMS và trang học phần (giao-trinh/, srs/, rubric/).
