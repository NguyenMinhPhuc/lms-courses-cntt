-- Thủ tục của notification-service (SRS M08). Thông báo lưu vào SQL Server trước khi gửi socket (BR-14).
SET NOCOUNT ON;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Notification_Create
  @UserId INT, @Title NVARCHAR(100), @Body NVARCHAR(300), @OrderId INT = NULL
AS
BEGIN
  SET NOCOUNT ON;
  INSERT INTO dbo.Notifications (UserId, Title, Body, OrderId)
  OUTPUT inserted.NotificationId AS id, inserted.Title AS title, inserted.Body AS body,
         inserted.OrderId AS orderId, inserted.IsRead AS isRead, inserted.CreatedAt AS createdAt
  VALUES (@UserId, @Title, @Body, @OrderId);
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Notification_GetList
  @UserId INT, @Page INT = 1, @PageSize INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  IF @Page < 1 OR @PageSize NOT BETWEEN 1 AND 100
    THROW 50400, N'Tham số phân trang không hợp lệ', 1;

  SELECT NotificationId AS id, Title AS title, Body AS body, OrderId AS orderId,
         IsRead AS isRead, CreatedAt AS createdAt
  FROM dbo.Notifications
  WHERE UserId = @UserId
  ORDER BY CreatedAt DESC, NotificationId DESC
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Notification_CountUnread
  @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  SELECT COUNT(*) AS unread FROM dbo.Notifications WHERE UserId = @UserId AND IsRead = 0;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Notification_MarkRead
  @NotificationId INT, @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE dbo.Notifications SET IsRead = 1
  WHERE NotificationId = @NotificationId AND UserId = @UserId;   -- chỉ thông báo của chính mình
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy thông báo', 1;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Notification_MarkAllRead
  @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE dbo.Notifications SET IsRead = 1 WHERE UserId = @UserId AND IsRead = 0;
  SELECT @@ROWCOUNT AS updated;
END;
GO
