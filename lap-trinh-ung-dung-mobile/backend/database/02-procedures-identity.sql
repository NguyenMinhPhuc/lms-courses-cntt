-- Thủ tục của identity-service: tài khoản, refresh token (SRS M01, M07, F11.4).
SET NOCOUNT ON;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Health_Check
AS
BEGIN
  SET NOCOUNT ON;
  SELECT 1 AS ok;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_User_Register
  @FullName NVARCHAR(100), @Email NVARCHAR(255), @PasswordHash NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  IF EXISTS (SELECT 1 FROM dbo.Users WHERE Email = @Email)
    THROW 50409, N'Email đã được sử dụng', 1;

  INSERT INTO dbo.Users (FullName, Email, PasswordHash) VALUES (@FullName, @Email, @PasswordHash);
  SELECT CAST(SCOPE_IDENTITY() AS INT) AS userId;
END;
GO

-- Quản lý tạo tài khoản nhân viên/quản lý (cũng dùng để tạo dữ liệu mẫu)
CREATE OR ALTER PROCEDURE dbo.sp_User_CreateStaff
  @FullName NVARCHAR(100), @Email NVARCHAR(255), @PasswordHash NVARCHAR(255), @Role NVARCHAR(20)
AS
BEGIN
  SET NOCOUNT ON;
  IF @Role NOT IN (N'customer', N'staff', N'admin')
    THROW 50400, N'Vai trò không hợp lệ', 1;
  IF EXISTS (SELECT 1 FROM dbo.Users WHERE Email = @Email)
    THROW 50409, N'Email đã được sử dụng', 1;

  INSERT INTO dbo.Users (FullName, Email, PasswordHash, Role)
  OUTPUT inserted.UserId AS userId, inserted.FullName AS fullName, inserted.Email AS email, inserted.Role AS role
  VALUES (@FullName, @Email, @PasswordHash, @Role);
END;
GO

-- Thủ tục nội bộ: trả PasswordHash cho backend so sánh, không bao giờ gửi cho client
CREATE OR ALTER PROCEDURE dbo.sp_User_GetByEmail
  @Email NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  SELECT UserId, FullName, Email, PasswordHash, Role, AvatarUrl, IsLocked
  FROM dbo.Users WHERE Email = @Email;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_User_GetById
  @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Users WHERE UserId = @UserId)
    THROW 50404, N'Không tìm thấy người dùng', 1;

  SELECT UserId AS userId, FullName AS fullName, Email AS email, Role AS role,
         AvatarUrl AS avatarUrl, IsLocked AS isLocked, CreatedAt AS createdAt
  FROM dbo.Users WHERE UserId = @UserId;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_User_UpdateProfile
  @UserId INT, @FullName NVARCHAR(100)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE dbo.Users SET FullName = @FullName WHERE UserId = @UserId;
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy người dùng', 1;
  EXEC dbo.sp_User_GetById @UserId = @UserId;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_User_UpdateAvatar
  @UserId INT, @AvatarUrl NVARCHAR(500)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE dbo.Users SET AvatarUrl = @AvatarUrl
  OUTPUT inserted.AvatarUrl AS avatarUrl
  WHERE UserId = @UserId;
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy người dùng', 1;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_User_GetList
  @Role NVARCHAR(20) = NULL, @Keyword NVARCHAR(100) = NULL, @Page INT = 1, @PageSize INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  IF @Page < 1 OR @PageSize NOT BETWEEN 1 AND 100
    THROW 50400, N'Tham số phân trang không hợp lệ', 1;

  SELECT UserId AS userId, FullName AS fullName, Email AS email, Role AS role,
         AvatarUrl AS avatarUrl, IsLocked AS isLocked, CreatedAt AS createdAt
  FROM dbo.Users
  WHERE (@Role IS NULL OR Role = @Role)
    AND (@Keyword IS NULL
         OR FullName COLLATE Latin1_General_100_CI_AI LIKE N'%' + @Keyword + N'%'
         OR Email LIKE N'%' + @Keyword + N'%')
  ORDER BY UserId DESC
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO

-- Khóa tài khoản thì thu hồi mọi refresh token để người đó không làm mới phiên được nữa
CREATE OR ALTER PROCEDURE dbo.sp_User_SetLocked
  @UserId INT, @IsLocked BIT
AS
BEGIN
  SET NOCOUNT ON;
  SET XACT_ABORT ON;
  BEGIN TRY
    BEGIN TRAN;
    UPDATE dbo.Users SET IsLocked = @IsLocked WHERE UserId = @UserId;
    IF @@ROWCOUNT = 0
      THROW 50404, N'Không tìm thấy người dùng', 1;
    IF @IsLocked = 1
      UPDATE dbo.RefreshTokens SET RevokedAt = SYSDATETIME() WHERE UserId = @UserId AND RevokedAt IS NULL;
    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    THROW;
  END CATCH
  EXEC dbo.sp_User_GetById @UserId = @UserId;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_RefreshToken_Save
  @UserId INT, @TokenHash CHAR(64), @ExpiresAt DATETIME2
AS
BEGIN
  SET NOCOUNT ON;
  INSERT INTO dbo.RefreshTokens (UserId, TokenHash, ExpiresAt) VALUES (@UserId, @TokenHash, @ExpiresAt);
END;
GO

-- Xoay vòng: mỗi refresh token dùng một lần; tài khoản bị khóa thì không trả về gì
CREATE OR ALTER PROCEDURE dbo.sp_RefreshToken_Use
  @TokenHash CHAR(64)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE rt SET rt.RevokedAt = SYSDATETIME()
  OUTPUT inserted.UserId AS userId
  FROM dbo.RefreshTokens rt
  JOIN dbo.Users u ON u.UserId = rt.UserId
  WHERE rt.TokenHash = @TokenHash AND rt.RevokedAt IS NULL
    AND rt.ExpiresAt > SYSDATETIME() AND u.IsLocked = 0;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_RefreshToken_Revoke
  @TokenHash CHAR(64)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE dbo.RefreshTokens SET RevokedAt = SYSDATETIME() WHERE TokenHash = @TokenHash AND RevokedAt IS NULL;
END;
GO
