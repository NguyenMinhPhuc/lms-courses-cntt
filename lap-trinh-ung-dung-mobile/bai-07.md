<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 07 - CSDL SQL Server nâng cao &amp; đồng bộ dữ liệu qua backend (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Hai bạn cùng đặt suất cơm gà cuối cùng trong cùng một giây. Ai được phần? Và nếu hệ thống tạo đơn xong nhưng trừ tồn kho thất bại, đơn hàng đó có còn đúng không?</em></p>
        <p><strong>Mục tiêu:</strong> Hoàn thiện được thiết kế CSDL SQL Server cho nghiệp vụ thực tế (ràng buộc, chỉ mục); viết được stored procedure có giao dịch và xử lý lỗi cho nghiệp vụ nhiều bảng và báo cáo thống kê; đồng bộ được dữ liệu giữa ứng dụng và server mà không lưu CSDL trên thiết bị.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Toàn vẹn dữ liệu:</strong> ràng buộc <code>CHECK</code>, <code>UNIQUE</code>, khóa ngoại, giá trị mặc định; chỉ mục cho các truy vấn ứng dụng gọi nhiều.</li>
            <li><strong>Ý chính 2 - Giao dịch trong stored procedure:</strong> đặt hàng = tạo đơn + chi tiết đơn + trừ tồn kho trong một giao dịch; <code>TRY...CATCH</code>, <code>ROLLBACK</code>, <code>THROW</code>.</li>
            <li><strong>Ý chính 3 - Thủ tục báo cáo và script phiên bản:</strong> doanh thu theo ngày, món bán chạy; script tạo CSDL đánh số thứ tự để cả nhóm có cùng CSDL.</li>
            <li><strong>Ý chính 4 - Đồng bộ ứng dụng với server:</strong> dữ liệu chuẩn luôn ở SQL Server; optimistic update; giữ giỏ hàng khi tắt app bằng AsyncStorage.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> LHU Food đặt hàng an toàn khi nhiều người đặt cùng lúc; nhân viên xem được thống kê doanh thu; nhóm có ERD phiên bản cuối và script CSDL + thủ tục chạy lại được từ đầu.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Toàn vẹn dữ liệu và chỉ mục</h3>
            <p>Quy tắc dữ liệu nào đặt được ở CSDL thì đặt ở CSDL: dù request đến từ app, web hay công cụ khác, dữ liệu sai vẫn bị chặn.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>-- Tồn kho không được âm
ALTER TABLE Products ADD Stock INT NOT NULL CONSTRAINT DF_Products_Stock DEFAULT 0
  CONSTRAINT CK_Products_Stock CHECK (Stock &gt;= 0);

-- Trạng thái đơn chỉ nhận các giá trị đã thống nhất
ALTER TABLE Orders ADD CONSTRAINT CK_Orders_Status
  CHECK (Status IN (N'pending', N'preparing', N'ready', N'completed', N'cancelled'));

-- Chỉ mục cho truy vấn hay dùng: lịch sử đơn của một người, mới nhất trước
CREATE INDEX IX_Orders_UserId_CreatedAt ON Orders (UserId, CreatedAt DESC);
CREATE INDEX IX_Products_CategoryId ON Products (CategoryId) WHERE IsAvailable = 1;</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Chỉ mục</strong> giúp SQL Server tìm nhanh mà không đọc toàn bảng. Đặt chỉ mục theo đúng điều kiện <code>WHERE</code> và <code>ORDER BY</code> mà thủ tục hay dùng.</li>
                <li>Đừng tạo chỉ mục cho mọi cột: mỗi chỉ mục làm thao tác ghi chậm hơn một chút và tốn dung lượng.</li>
                <li>Đặt tên ràng buộc rõ ràng (<code>CK_...</code>, <code>DF_...</code>, <code>IX_...</code>) để thông báo lỗi dễ hiểu và dễ sửa về sau.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Giao dịch trong stored procedure</h3>
            <p><strong>Giao dịch (transaction)</strong> gói nhiều câu lệnh thành một khối: <strong>hoặc tất cả thành công, hoặc không có gì thay đổi</strong>. Đặt hàng gồm ba bước (tạo đơn, tạo chi tiết đơn, trừ tồn kho); nếu bước ba lỗi mà hai bước đầu vẫn được lưu, dữ liệu sẽ sai.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>CREATE OR ALTER PROCEDURE sp_Order_Create
  @UserId INT, @Note NVARCHAR(200) = NULL, @ItemsJson NVARCHAR(MAX)
AS
BEGIN
  SET NOCOUNT ON;
  SET XACT_ABORT ON;                     -- lỗi bất kỳ sẽ hủy toàn bộ giao dịch
  IF ISJSON(@ItemsJson) = 0
    THROW 50400, N'Danh sách món không hợp lệ', 1;

  DECLARE @Items TABLE (ProductId INT PRIMARY KEY, Quantity INT NOT NULL);
  INSERT INTO @Items (ProductId, Quantity)
  SELECT productId, SUM(quantity)
  FROM OPENJSON(@ItemsJson) WITH (productId INT '$.productId', quantity INT '$.quantity')
  GROUP BY productId;

  IF NOT EXISTS (SELECT 1 FROM @Items) OR EXISTS (SELECT 1 FROM @Items WHERE Quantity &lt;= 0)
    THROW 50400, N'Số lượng món không hợp lệ', 1;

  BEGIN TRY
    BEGIN TRAN;

    -- Khóa các dòng món đang đặt để hai đơn cùng lúc không cùng trừ một suất cuối
    IF EXISTS (
      SELECT 1 FROM @Items i
      LEFT JOIN Products p WITH (UPDLOCK, HOLDLOCK) ON p.ProductId = i.ProductId
      WHERE p.ProductId IS NULL OR p.IsAvailable = 0 OR p.Stock &lt; i.Quantity)
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
    IF @@TRANCOUNT &gt; 0 ROLLBACK;
    THROW;                               -- ném lại lỗi gốc (giữ mã 50409) cho backend
  END CATCH
END;
GO</code></pre>
            <ul style="margin-bottom: 0;">
                <li><code>UPDLOCK, HOLDLOCK</code>: khóa các dòng món cho tới khi giao dịch kết thúc; đơn thứ hai phải chờ, nên không có chuyện hai người cùng lấy suất cuối.</li>
                <li><code>THROW;</code> không tham số trong <code>CATCH</code> ném lại đúng lỗi gốc; <code>DatabaseService</code> vẫn nhận mã 50409 và trả <code>409 Conflict</code> cho app.</li>
                <li>Backend <strong>chỉ gọi một thủ tục</strong>; toàn bộ giao dịch nằm trong SQL Server. Danh sách món cũng có thể truyền bằng tham số kiểu bảng (table-valued parameter) thay cho JSON.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Thủ tục báo cáo và script phiên bản</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>CREATE OR ALTER PROCEDURE sp_Report_RevenueByDay
  @FromDate DATE, @ToDate DATE
AS
BEGIN
  SET NOCOUNT ON;
  SELECT CAST(o.CreatedAt AS DATE)        AS day,
         COUNT(DISTINCT o.OrderId)        AS orderCount,
         SUM(oi.Quantity * oi.UnitPrice)  AS revenue
  FROM Orders o
  JOIN OrderItems oi ON oi.OrderId = o.OrderId
  WHERE o.Status &lt;&gt; N'cancelled'
    AND o.CreatedAt &gt;= @FromDate AND o.CreatedAt &lt; DATEADD(DAY, 1, @ToDate)
  GROUP BY CAST(o.CreatedAt AS DATE)
  ORDER BY day;
END;
GO</code></pre>
            <p>Tương tự, <code>sp_Report_TopProducts</code> trả về 5 món bán chạy nhất trong khoảng thời gian. Endpoint thống kê chỉ cho vai trò <code>staff</code> (RolesGuard, bài 06).</p>
            <p><strong>Script phiên bản:</strong> đặt mọi script trong thư mục <code>database/</code> của repo API, đánh số theo thứ tự chạy:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>database/
├── 01-tables.sql          bảng và ràng buộc
├── 02-procedures.sql      thủ tục sản phẩm, đơn hàng
├── 03-auth.sql            Users, RefreshTokens và thủ tục xác thực
├── 04-stock-reports.sql   tồn kho, chỉ mục, thủ tục báo cáo
└── 99-seed.sql            dữ liệu mẫu</code></pre>
            <p style="margin-bottom: 0;">Chạy lần lượt từ <code>01</code> đến <code>99</code> trên CSDL trống phải tạo ra đúng CSDL của nhóm. Bài 11 dùng chính các script này để triển khai lên Windows Server của Khoa.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Đồng bộ ứng dụng với server</h3>
            <p><strong>Nguyên tắc:</strong> nguồn dữ liệu chuẩn luôn là SQL Server. Ứng dụng không có CSDL riêng; ứng dụng chỉ giữ <strong>bản sao tạm</strong> để hiển thị nhanh.</p>
            <p><strong>Optimistic update</strong> (cập nhật lạc quan): đổi giao diện ngay khi người dùng bấm, gửi API ở nền; nếu API lỗi thì trả giao diện về như cũ.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>const queryClient = useQueryClient();
const addFavorite = useMutation({
  mutationFn: (productId: number) =&gt; api(`/favorites/${productId}`, { method: 'POST' }),
  onMutate: async (productId) =&gt; {
    await queryClient.cancelQueries({ queryKey: ['favorites'] });
    const previous = queryClient.getQueryData&lt;number[]&gt;(['favorites']);
    queryClient.setQueryData&lt;number[]&gt;(['favorites'], (old = []) =&gt; [...old, productId]);
    return { previous };
  },
  onError: (_err, _id, context) =&gt; queryClient.setQueryData(['favorites'], context?.previous),
  onSettled: () =&gt; queryClient.invalidateQueries({ queryKey: ['favorites'] }),
});</code></pre>
            <p><strong>Giữ giỏ hàng khi tắt app:</strong> giỏ hàng chưa đặt là dữ liệu tạm của riêng máy, lưu bằng middleware <code>persist</code> của Zustand với AsyncStorage (<code>npx expo install @react-native-async-storage/async-storage</code>):</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>import AsyncStorage from '@react-native-async-storage/async-storage';
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';

export const useCart = create&lt;CartState&gt;()(
  persist(
    (set, get) =&gt; ({ /* items, add, remove... như bài 04 */ }),
    { name: 'lhufood-cart', storage: createJSONStorage(() =&gt; AsyncStorage) },
  ),
);</code></pre>
            <p style="margin-bottom: 0;">Khi đặt hàng, server vẫn kiểm tra lại giá và tồn kho; giỏ hàng trên máy chỉ là "ý định mua", không phải dữ liệu chuẩn.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_07}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 07: CSDL SQL Server nâng cao &amp; đồng bộ dữ liệu</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://learn.microsoft.com/sql/t-sql/language-elements/try-catch-transact-sql" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Microsoft Learn - TRY...CATCH (Transact-SQL)</span><br>
                <span style="color: #6c757d; font-size: 13px;">Xử lý lỗi và giao dịch trong thủ tục.</span>
            </a>
            <a href="https://learn.microsoft.com/sql/relational-databases/indexes/indexes" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Microsoft Learn - Indexes</span><br>
                <span style="color: #6c757d; font-size: 13px;">Khi nào và cách tạo chỉ mục.</span>
            </a>
            <a href="https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 TanStack Query - Optimistic Updates</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cập nhật giao diện trước, hoàn tác khi lỗi.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Đặt hàng an toàn &amp; thống kê</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Chạy script thêm cột <code>Stock</code>, ràng buộc trạng thái và chỉ mục (mục 2.1); cập nhật dữ liệu mẫu có tồn kho.</li>
                <li>Viết lại <code>sp_Order_Create</code> có giao dịch (mục 2.2). Thử: đặt số lượng lớn hơn tồn kho → nhận lỗi 50409, kiểm tra trong SSMS không có đơn nào bị tạo.</li>
                <li>Mở hai cửa sổ SSMS cùng đặt suất cuối của một món để thấy đơn thứ hai bị từ chối.</li>
                <li>Viết <code>sp_Report_RevenueByDay</code>, endpoint <code>GET /reports/revenue</code> chỉ cho <code>staff</code>, màn hình Thống kê trong app.</li>
                <li>Giỏ hàng dùng <code>persist</code>: tắt hẳn app, mở lại vẫn còn món trong giỏ.</li>
                <li>Cập nhật ERD (cột <code>Stock</code>, ràng buộc) và thư mục <code>database/</code>.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Món yêu thích</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Thiết kế bảng <code>Favorites</code> (quan hệ n-n giữa người dùng và món, không cho trùng), viết các thủ tục thêm, xóa, lấy danh sách; API <code>POST/DELETE /favorites/:productId</code> và <code>GET /favorites</code> (lấy người dùng từ token); nút trái tim trong app dùng optimistic update.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> bấm trái tim đổi màu ngay; tắt mạng rồi bấm thì giao diện tự trở lại trạng thái cũ và báo lỗi; thêm trùng một món không tạo hai dòng; mã backend không có câu SQL trực tiếp.</p>
            <a href="{{LINK_NOP_BAI_07}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Rà soát CSDL của nhóm: ràng buộc, chỉ mục, thủ tục có giao dịch cho nghiệp vụ chính, ít nhất 1 thủ tục báo cáo.</li>
                <li>Tìm trong mã backend các chuỗi <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>query(</code>: <strong>không được còn</strong>.</li>
                <li>Nộp <strong>ERD phiên bản cuối</strong> và thư mục <code>database/</code> (script tạo CSDL + thủ tục + dữ liệu mẫu) chạy lại được từ đầu.</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Nghiệp vụ nào trong đề tài của nhóm có nguy cơ "hai người cùng lúc" giống suất cơm cuối? Nhóm xử lý trong thủ tục như thế nào?</p>
            <a href="{{LINK_DIEN_DAN_BAI_07}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập ràng buộc, chỉ mục, giao dịch, thủ tục báo cáo và đồng bộ dữ liệu.</p>
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
        <p><strong>Lỗi "Transaction count after EXECUTE indicates a mismatching number of BEGIN and COMMIT":</strong> có nhánh thoát khỏi thủ tục mà chưa <code>COMMIT</code> hoặc <code>ROLLBACK</code>. Dùng khuôn <code>BEGIN TRY ... COMMIT ... END TRY BEGIN CATCH IF @@TRANCOUNT &gt; 0 ROLLBACK; THROW; END CATCH</code> như mục 2.2.</p>
        <p><strong>Thêm cột <code>Stock</code> báo lỗi vì bảng đã có dữ liệu:</strong> cột <code>NOT NULL</code> phải đi kèm <code>DEFAULT</code> như ví dụ để các dòng cũ có giá trị.</p>
        <p><strong>Giỏ hàng không được khôi phục:</strong> kiểm tra đã dùng cú pháp <code>create&lt;CartState&gt;()(persist(...))</code> (có thêm cặp ngoặc) và đã cài AsyncStorage bằng <code>npx expo install</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu mức cô lập giao dịch (isolation level) và cách xem kế hoạch thực thi (execution plan) trong SSMS để đánh giá chỉ mục.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu xóa dòng <code>WITH (UPDLOCK, HOLDLOCK)</code>, tình huống hai người cùng đặt suất cuối có thể dẫn tới kết quả gì?</p>
    </div>
</details>
