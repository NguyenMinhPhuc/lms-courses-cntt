-- Thủ tục của order-service: đơn hàng, trạng thái, báo cáo, đánh giá (SRS M04, M09, M10, F07.4).
SET NOCOUNT ON;
GO

-- Đặt món trong một giao dịch: khóa dòng món, kiểm tra tồn kho, lưu giá tại thời điểm đặt (BR-07..BR-10)
CREATE OR ALTER PROCEDURE dbo.sp_Order_Create
  @UserId    INT,
  @Note      NVARCHAR(200) = NULL,
  @CounterId INT = NULL,
  @ItemsJson NVARCHAR(MAX)
AS
BEGIN
  SET NOCOUNT ON;
  SET XACT_ABORT ON;
  IF ISJSON(@ItemsJson) = 0
    THROW 50400, N'Danh sách món không hợp lệ', 1;
  IF EXISTS (SELECT 1 FROM OPENJSON(@ItemsJson) WITH (productId INT '$.productId', quantity INT '$.quantity')
             WHERE productId IS NULL OR quantity IS NULL OR quantity <= 0)
    THROW 50400, N'Số lượng món không hợp lệ', 1;
  IF @CounterId IS NOT NULL AND NOT EXISTS (SELECT 1 FROM dbo.Counters WHERE CounterId = @CounterId AND IsActive = 1)
    THROW 50404, N'Không tìm thấy quầy nhận', 1;

  DECLARE @Items TABLE (ProductId INT PRIMARY KEY, Quantity INT NOT NULL);
  INSERT INTO @Items (ProductId, Quantity)
  SELECT productId, SUM(quantity)
  FROM OPENJSON(@ItemsJson) WITH (productId INT '$.productId', quantity INT '$.quantity')
  GROUP BY productId;

  IF NOT EXISTS (SELECT 1 FROM @Items)
    THROW 50400, N'Đơn hàng phải có ít nhất một món', 1;

  BEGIN TRY
    BEGIN TRAN;

    IF EXISTS (
      SELECT 1 FROM @Items i
      LEFT JOIN dbo.Products p WITH (UPDLOCK, HOLDLOCK) ON p.ProductId = i.ProductId
      WHERE p.ProductId IS NULL OR p.IsAvailable = 0 OR p.Stock < i.Quantity)
      THROW 50409, N'Có món đã hết hoặc không đủ số lượng', 1;

    DECLARE @OrderId INT;
    INSERT INTO dbo.Orders (UserId, Note, CounterId) VALUES (@UserId, @Note, @CounterId);
    SET @OrderId = CAST(SCOPE_IDENTITY() AS INT);

    INSERT INTO dbo.OrderItems (OrderId, ProductId, Quantity, UnitPrice)
    SELECT @OrderId, i.ProductId, i.Quantity, p.Price
    FROM @Items i JOIN dbo.Products p ON p.ProductId = i.ProductId;

    UPDATE p SET p.Stock = p.Stock - i.Quantity
    FROM dbo.Products p JOIN @Items i ON i.ProductId = p.ProductId;

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    THROW;
  END CATCH

  SELECT o.OrderId AS orderId, o.UserId AS userId, o.Status AS status, o.CreatedAt AS createdAt,
         SUM(oi.Quantity * oi.UnitPrice) AS total, SUM(oi.Quantity) AS itemCount
  FROM dbo.Orders o JOIN dbo.OrderItems oi ON oi.OrderId = o.OrderId
  WHERE o.OrderId = @OrderId
  GROUP BY o.OrderId, o.UserId, o.Status, o.CreatedAt;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Order_GetHistory
  @UserId INT, @Page INT = 1, @PageSize INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  IF @Page < 1 OR @PageSize NOT BETWEEN 1 AND 100
    THROW 50400, N'Tham số phân trang không hợp lệ', 1;

  SELECT o.OrderId AS orderId, o.CreatedAt AS createdAt, o.Status AS status,
         c.Name AS counterName, t.Total AS total, t.ItemCount AS itemCount
  FROM dbo.Orders o
  LEFT JOIN dbo.Counters c ON c.CounterId = o.CounterId
  CROSS APPLY (SELECT SUM(Quantity * UnitPrice) AS Total, SUM(Quantity) AS ItemCount
               FROM dbo.OrderItems WHERE OrderId = o.OrderId) t
  WHERE o.UserId = @UserId
  ORDER BY o.CreatedAt DESC, o.OrderId DESC
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO

-- Hai tập kết quả: thông tin đơn, danh sách món. @UserId NULL = nhân viên xem mọi đơn.
CREATE OR ALTER PROCEDURE dbo.sp_Order_GetById
  @OrderId INT, @UserId INT = NULL
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Orders WHERE OrderId = @OrderId AND (@UserId IS NULL OR UserId = @UserId))
    THROW 50404, N'Không tìm thấy đơn hàng', 1;

  SELECT o.OrderId AS orderId, o.UserId AS userId, u.FullName AS customerName, o.Status AS status,
         o.Note AS note, o.CancelReason AS cancelReason, o.CounterId AS counterId, c.Name AS counterName,
         o.CreatedAt AS createdAt, o.UpdatedAt AS updatedAt,
         (SELECT SUM(Quantity * UnitPrice) FROM dbo.OrderItems WHERE OrderId = o.OrderId) AS total
  FROM dbo.Orders o
  JOIN dbo.Users u ON u.UserId = o.UserId
  LEFT JOIN dbo.Counters c ON c.CounterId = o.CounterId
  WHERE o.OrderId = @OrderId;

  SELECT oi.ProductId AS productId, p.Name AS name, p.ImageUrl AS imageUrl, oi.Quantity AS quantity,
         oi.UnitPrice AS unitPrice, oi.Quantity * oi.UnitPrice AS lineTotal
  FROM dbo.OrderItems oi JOIN dbo.Products p ON p.ProductId = oi.ProductId
  WHERE oi.OrderId = @OrderId
  ORDER BY p.Name;
END;
GO

-- Khách hủy đơn của mình khi còn pending, hoàn tồn kho (BR-11)
CREATE OR ALTER PROCEDURE dbo.sp_Order_Cancel
  @OrderId INT, @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  SET XACT_ABORT ON;
  BEGIN TRY
    BEGIN TRAN;
    IF NOT EXISTS (SELECT 1 FROM dbo.Orders WITH (UPDLOCK)
                   WHERE OrderId = @OrderId AND UserId = @UserId AND Status = N'pending')
      THROW 50409, N'Chỉ hủy được đơn của bạn khi đơn chưa được chuẩn bị', 1;

    UPDATE dbo.Orders SET Status = N'cancelled', UpdatedAt = SYSDATETIME() WHERE OrderId = @OrderId;
    UPDATE p SET p.Stock = p.Stock + oi.Quantity
    FROM dbo.Products p JOIN dbo.OrderItems oi ON oi.ProductId = p.ProductId
    WHERE oi.OrderId = @OrderId;
    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    THROW;
  END CATCH

  SELECT OrderId AS orderId, UserId AS userId, Status AS status FROM dbo.Orders WHERE OrderId = @OrderId;
END;
GO

-- Nhân viên hủy đơn chưa xong kèm lý do (US-S07), hoàn tồn kho
CREATE OR ALTER PROCEDURE dbo.sp_Order_CancelByStaff
  @OrderId INT, @Reason NVARCHAR(200)
AS
BEGIN
  SET NOCOUNT ON;
  SET XACT_ABORT ON;
  BEGIN TRY
    BEGIN TRAN;
    DECLARE @Current NVARCHAR(20) = (SELECT Status FROM dbo.Orders WITH (UPDLOCK) WHERE OrderId = @OrderId);
    IF @Current IS NULL
      THROW 50404, N'Không tìm thấy đơn hàng', 1;
    IF @Current NOT IN (N'pending', N'preparing')
      THROW 50409, N'Chỉ hủy được đơn đang chờ hoặc đang chuẩn bị', 1;

    UPDATE dbo.Orders SET Status = N'cancelled', CancelReason = @Reason, UpdatedAt = SYSDATETIME()
    WHERE OrderId = @OrderId;
    UPDATE p SET p.Stock = p.Stock + oi.Quantity
    FROM dbo.Products p JOIN dbo.OrderItems oi ON oi.ProductId = p.ProductId
    WHERE oi.OrderId = @OrderId;
    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    THROW;
  END CATCH

  SELECT OrderId AS orderId, UserId AS userId, Status AS status, CancelReason AS cancelReason
  FROM dbo.Orders WHERE OrderId = @OrderId;
END;
GO

-- Chuyển trạng thái đúng trình tự pending → preparing → ready → completed (BR-15)
CREATE OR ALTER PROCEDURE dbo.sp_Order_UpdateStatus
  @OrderId INT, @Status NVARCHAR(20)
AS
BEGIN
  SET NOCOUNT ON;
  DECLARE @Current NVARCHAR(20) = (SELECT Status FROM dbo.Orders WHERE OrderId = @OrderId);
  IF @Current IS NULL
    THROW 50404, N'Không tìm thấy đơn hàng', 1;
  IF @Current IN (N'completed', N'cancelled')
    THROW 50409, N'Đơn đã kết thúc, không thể đổi trạng thái', 1;
  IF NOT ((@Current = N'pending' AND @Status = N'preparing')
       OR (@Current = N'preparing' AND @Status = N'ready')
       OR (@Current = N'ready' AND @Status = N'completed'))
    THROW 50409, N'Trạng thái mới không đúng trình tự xử lý đơn', 1;

  UPDATE dbo.Orders SET Status = @Status, UpdatedAt = SYSDATETIME()
  OUTPUT inserted.OrderId AS orderId, inserted.UserId AS userId, inserted.Status AS status
  WHERE OrderId = @OrderId AND Status = @Current;   -- chặn hai nhân viên cùng đổi một đơn
  IF @@ROWCOUNT = 0
    THROW 50409, N'Đơn vừa được người khác cập nhật, vui lòng tải lại', 1;
END;
GO

-- Danh sách đơn cho màn hình nhân viên (F09.1). @Status NULL = mọi đơn chưa kết thúc.
CREATE OR ALTER PROCEDURE dbo.sp_Order_GetListForStaff
  @Status NVARCHAR(20) = NULL, @Date DATE = NULL
AS
BEGIN
  SET NOCOUNT ON;
  DECLARE @Day DATE = ISNULL(@Date, CAST(SYSDATETIME() AS DATE));

  SELECT o.OrderId AS orderId, o.Status AS status, o.Note AS note, o.CreatedAt AS createdAt,
         u.FullName AS customerName, c.Name AS counterName, t.Total AS total, t.ItemCount AS itemCount,
         t.Summary AS summary
  FROM dbo.Orders o
  JOIN dbo.Users u ON u.UserId = o.UserId
  LEFT JOIN dbo.Counters c ON c.CounterId = o.CounterId
  CROSS APPLY (SELECT SUM(oi.Quantity * oi.UnitPrice) AS Total, SUM(oi.Quantity) AS ItemCount,
                      STRING_AGG(CONCAT(p.Name, N' x', oi.Quantity), N', ') AS Summary
               FROM dbo.OrderItems oi JOIN dbo.Products p ON p.ProductId = oi.ProductId
               WHERE oi.OrderId = o.OrderId) t
  WHERE o.CreatedAt >= @Day AND o.CreatedAt < DATEADD(DAY, 1, @Day)
    AND ((@Status IS NULL AND o.Status IN (N'pending', N'preparing', N'ready')) OR o.Status = @Status)
  ORDER BY o.CreatedAt;
END;
GO

-- ---------- Báo cáo (không tính đơn hủy, BR-17) ----------
CREATE OR ALTER PROCEDURE dbo.sp_Report_RevenueByDay
  @FromDate DATE, @ToDate DATE
AS
BEGIN
  SET NOCOUNT ON;
  IF @FromDate > @ToDate
    THROW 50400, N'Khoảng thời gian không hợp lệ', 1;

  SELECT CAST(o.CreatedAt AS DATE)       AS day,
         COUNT(DISTINCT o.OrderId)       AS orderCount,
         SUM(oi.Quantity * oi.UnitPrice) AS revenue
  FROM dbo.Orders o
  JOIN dbo.OrderItems oi ON oi.OrderId = o.OrderId
  WHERE o.Status <> N'cancelled'
    AND o.CreatedAt >= @FromDate AND o.CreatedAt < DATEADD(DAY, 1, @ToDate)
  GROUP BY CAST(o.CreatedAt AS DATE)
  ORDER BY day;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Report_TopProducts
  @FromDate DATE, @ToDate DATE, @Top INT = 5
AS
BEGIN
  SET NOCOUNT ON;
  IF @FromDate > @ToDate OR @Top NOT BETWEEN 1 AND 50
    THROW 50400, N'Tham số báo cáo không hợp lệ', 1;

  SELECT TOP (@Top) p.ProductId AS id, p.Name AS name, SUM(oi.Quantity) AS quantity,
         SUM(oi.Quantity * oi.UnitPrice) AS revenue
  FROM dbo.OrderItems oi
  JOIN dbo.Orders o   ON o.OrderId = oi.OrderId
  JOIN dbo.Products p ON p.ProductId = oi.ProductId
  WHERE o.Status <> N'cancelled'
    AND o.CreatedAt >= @FromDate AND o.CreatedAt < DATEADD(DAY, 1, @ToDate)
  GROUP BY p.ProductId, p.Name
  ORDER BY quantity DESC, revenue DESC;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Report_OrderStatus
  @FromDate DATE, @ToDate DATE
AS
BEGIN
  SET NOCOUNT ON;
  IF @FromDate > @ToDate
    THROW 50400, N'Khoảng thời gian không hợp lệ', 1;

  SELECT Status AS status, COUNT(*) AS orderCount,
         CAST(100.0 * COUNT(*) / NULLIF(SUM(COUNT(*)) OVER (), 0) AS DECIMAL(5,2)) AS percentage
  FROM dbo.Orders
  WHERE CreatedAt >= @FromDate AND CreatedAt < DATEADD(DAY, 1, @ToDate)
  GROUP BY Status
  ORDER BY orderCount DESC;
END;
GO

-- ---------- Đánh giá món (mở rộng US-C17) ----------
CREATE OR ALTER PROCEDURE dbo.sp_Review_Create
  @UserId INT, @OrderId INT, @ProductId INT, @Rating TINYINT, @Comment NVARCHAR(500) = NULL
AS
BEGIN
  SET NOCOUNT ON;
  IF @Rating NOT BETWEEN 1 AND 5
    THROW 50400, N'Số sao từ 1 đến 5', 1;
  IF NOT EXISTS (SELECT 1 FROM dbo.Orders o JOIN dbo.OrderItems oi ON oi.OrderId = o.OrderId
                 WHERE o.OrderId = @OrderId AND o.UserId = @UserId AND oi.ProductId = @ProductId)
    THROW 50404, N'Không tìm thấy món trong đơn của bạn', 1;
  IF NOT EXISTS (SELECT 1 FROM dbo.Orders WHERE OrderId = @OrderId AND Status = N'completed')
    THROW 50409, N'Chỉ đánh giá được món của đơn đã nhận', 1;
  IF EXISTS (SELECT 1 FROM dbo.Reviews WHERE OrderId = @OrderId AND ProductId = @ProductId)
    THROW 50409, N'Bạn đã đánh giá món này trong đơn này', 1;

  INSERT INTO dbo.Reviews (OrderId, ProductId, UserId, Rating, Comment)
  OUTPUT inserted.ReviewId AS id, inserted.OrderId AS orderId, inserted.ProductId AS productId,
         inserted.Rating AS rating, inserted.Comment AS comment, inserted.CreatedAt AS createdAt
  VALUES (@OrderId, @ProductId, @UserId, @Rating, @Comment);
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Review_GetByProduct
  @ProductId INT, @Page INT = 1, @PageSize INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  IF @Page < 1 OR @PageSize NOT BETWEEN 1 AND 100
    THROW 50400, N'Tham số phân trang không hợp lệ', 1;

  SELECT r.ReviewId AS id, r.Rating AS rating, r.Comment AS comment, r.CreatedAt AS createdAt,
         u.FullName AS userName, u.AvatarUrl AS userAvatarUrl
  FROM dbo.Reviews r JOIN dbo.Users u ON u.UserId = r.UserId
  WHERE r.ProductId = @ProductId
  ORDER BY r.CreatedAt DESC
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO
