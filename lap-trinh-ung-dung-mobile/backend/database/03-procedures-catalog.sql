-- Thủ tục của catalog-service: danh mục, món, quầy, yêu thích (SRS M02, M05, M06, F09.3, F11.1–F11.3).
SET NOCOUNT ON;
GO

-- ---------- Danh mục ----------
CREATE OR ALTER PROCEDURE dbo.sp_Category_GetList
AS
BEGIN
  SET NOCOUNT ON;
  SELECT c.CategoryId AS id, c.Name AS name, c.SortOrder AS sortOrder,
         (SELECT COUNT(*) FROM dbo.Products p WHERE p.CategoryId = c.CategoryId AND p.IsAvailable = 1) AS productCount
  FROM dbo.Categories c
  ORDER BY c.SortOrder, c.Name;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Category_Create
  @Name NVARCHAR(100), @SortOrder INT = 0
AS
BEGIN
  SET NOCOUNT ON;
  IF EXISTS (SELECT 1 FROM dbo.Categories WHERE Name = @Name)
    THROW 50409, N'Tên danh mục đã tồn tại', 1;

  INSERT INTO dbo.Categories (Name, SortOrder)
  OUTPUT inserted.CategoryId AS id, inserted.Name AS name, inserted.SortOrder AS sortOrder
  VALUES (@Name, @SortOrder);
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Category_Update
  @CategoryId INT, @Name NVARCHAR(100), @SortOrder INT = 0
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Categories WHERE CategoryId = @CategoryId)
    THROW 50404, N'Không tìm thấy danh mục', 1;
  IF EXISTS (SELECT 1 FROM dbo.Categories WHERE Name = @Name AND CategoryId <> @CategoryId)
    THROW 50409, N'Tên danh mục đã tồn tại', 1;

  UPDATE dbo.Categories SET Name = @Name, SortOrder = @SortOrder
  OUTPUT inserted.CategoryId AS id, inserted.Name AS name, inserted.SortOrder AS sortOrder
  WHERE CategoryId = @CategoryId;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Category_Delete
  @CategoryId INT
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

-- ---------- Món ----------
-- @IncludeUnavailable = 1 chỉ dành cho nhân viên/quản lý (API kiểm tra vai trò trước khi truyền)
CREATE OR ALTER PROCEDURE dbo.sp_Product_GetList
  @CategoryId INT = NULL,
  @Keyword NVARCHAR(100) = NULL,
  @IncludeUnavailable BIT = 0,
  @Page INT = 1,
  @PageSize INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  IF @Page < 1 OR @PageSize NOT BETWEEN 1 AND 100
    THROW 50400, N'Tham số phân trang không hợp lệ', 1;

  SELECT p.ProductId AS id, p.CategoryId AS categoryId, c.Name AS categoryName, p.Name AS name,
         p.Description AS description, p.Price AS price, p.ImageUrl AS imageUrl,
         p.IsAvailable AS isAvailable, p.Stock AS stock
  FROM dbo.Products p
  JOIN dbo.Categories c ON c.CategoryId = p.CategoryId
  WHERE (@IncludeUnavailable = 1 OR p.IsAvailable = 1)
    AND (@CategoryId IS NULL OR p.CategoryId = @CategoryId)
    AND (@Keyword IS NULL OR p.Name COLLATE Latin1_General_100_CI_AI LIKE N'%' + @Keyword + N'%')   -- không phân biệt hoa thường, dấu (Latin1_General_100_CI_AI coi "ơ", "đ" như "o", "d"; Vietnamese_CI_AI thì không)
  ORDER BY p.ProductId
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Product_GetById
  @ProductId INT
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Products WHERE ProductId = @ProductId)
    THROW 50404, N'Không tìm thấy món ăn', 1;

  SELECT p.ProductId AS id, p.CategoryId AS categoryId, c.Name AS categoryName, p.Name AS name,
         p.Description AS description, p.Price AS price, p.ImageUrl AS imageUrl,
         p.IsAvailable AS isAvailable, p.Stock AS stock,
         CAST(ISNULL(r.AvgRating, 0) AS DECIMAL(3,2)) AS avgRating, ISNULL(r.ReviewCount, 0) AS reviewCount
  FROM dbo.Products p
  JOIN dbo.Categories c ON c.CategoryId = p.CategoryId
  OUTER APPLY (SELECT AVG(CAST(Rating AS DECIMAL(4,2))) AS AvgRating, COUNT(*) AS ReviewCount
               FROM dbo.Reviews WHERE ProductId = p.ProductId) r
  WHERE p.ProductId = @ProductId;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Product_Create
  @CategoryId INT, @Name NVARCHAR(150), @Description NVARCHAR(500) = NULL,
  @Price DECIMAL(12,0), @Stock INT = 0, @IsAvailable BIT = 1
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Categories WHERE CategoryId = @CategoryId)
    THROW 50404, N'Không tìm thấy danh mục', 1;
  IF @Price < 0 OR @Stock < 0
    THROW 50400, N'Giá và tồn kho không được âm', 1;

  DECLARE @Id INT;
  INSERT INTO dbo.Products (CategoryId, Name, Description, Price, Stock, IsAvailable)
  VALUES (@CategoryId, @Name, @Description, @Price, @Stock, @IsAvailable);
  SET @Id = CAST(SCOPE_IDENTITY() AS INT);
  EXEC dbo.sp_Product_GetById @ProductId = @Id;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Product_Update
  @ProductId INT, @CategoryId INT, @Name NVARCHAR(150), @Description NVARCHAR(500) = NULL, @Price DECIMAL(12,0)
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Products WHERE ProductId = @ProductId)
    THROW 50404, N'Không tìm thấy món ăn', 1;
  IF NOT EXISTS (SELECT 1 FROM dbo.Categories WHERE CategoryId = @CategoryId)
    THROW 50404, N'Không tìm thấy danh mục', 1;
  IF @Price < 0
    THROW 50400, N'Giá không được âm', 1;

  UPDATE dbo.Products
  SET CategoryId = @CategoryId, Name = @Name, Description = @Description, Price = @Price, UpdatedAt = SYSDATETIME()
  WHERE ProductId = @ProductId;
  EXEC dbo.sp_Product_GetById @ProductId = @ProductId;
END;
GO

-- Nhân viên bật/tắt "còn bán" (US-S04). Món đã có trong đơn không bị xóa, chỉ ngừng bán (BR-16).
CREATE OR ALTER PROCEDURE dbo.sp_Product_SetAvailability
  @ProductId INT, @IsAvailable BIT
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE dbo.Products SET IsAvailable = @IsAvailable, UpdatedAt = SYSDATETIME()
  OUTPUT inserted.ProductId AS id, inserted.IsAvailable AS isAvailable, inserted.Stock AS stock
  WHERE ProductId = @ProductId;
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy món ăn', 1;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Product_UpdateStock
  @ProductId INT, @Stock INT
AS
BEGIN
  SET NOCOUNT ON;
  IF @Stock < 0
    THROW 50400, N'Tồn kho không được âm', 1;

  UPDATE dbo.Products SET Stock = @Stock, UpdatedAt = SYSDATETIME()
  OUTPUT inserted.ProductId AS id, inserted.IsAvailable AS isAvailable, inserted.Stock AS stock
  WHERE ProductId = @ProductId;
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy món ăn', 1;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Product_UpdateImage
  @ProductId INT, @ImageUrl NVARCHAR(500)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE dbo.Products SET ImageUrl = @ImageUrl, UpdatedAt = SYSDATETIME()
  OUTPUT inserted.ProductId AS id, inserted.ImageUrl AS imageUrl
  WHERE ProductId = @ProductId;
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy món ăn', 1;
END;
GO

-- ---------- Quầy ----------
CREATE OR ALTER PROCEDURE dbo.sp_Counter_GetList
  @IncludeInactive BIT = 0
AS
BEGIN
  SET NOCOUNT ON;
  SELECT CounterId AS id, Name AS name, Description AS description,
         Latitude AS lat, Longitude AS lng, IsActive AS isActive
  FROM dbo.Counters
  WHERE @IncludeInactive = 1 OR IsActive = 1
  ORDER BY Name;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Counter_Create
  @Name NVARCHAR(100), @Description NVARCHAR(200) = NULL, @Latitude DECIMAL(9,6), @Longitude DECIMAL(9,6)
AS
BEGIN
  SET NOCOUNT ON;
  IF @Latitude NOT BETWEEN -90 AND 90 OR @Longitude NOT BETWEEN -180 AND 180
    THROW 50400, N'Tọa độ không hợp lệ', 1;

  INSERT INTO dbo.Counters (Name, Description, Latitude, Longitude)
  OUTPUT inserted.CounterId AS id, inserted.Name AS name, inserted.Description AS description,
         inserted.Latitude AS lat, inserted.Longitude AS lng, inserted.IsActive AS isActive
  VALUES (@Name, @Description, @Latitude, @Longitude);
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Counter_Update
  @CounterId INT, @Name NVARCHAR(100), @Description NVARCHAR(200) = NULL,
  @Latitude DECIMAL(9,6), @Longitude DECIMAL(9,6), @IsActive BIT = 1
AS
BEGIN
  SET NOCOUNT ON;
  IF @Latitude NOT BETWEEN -90 AND 90 OR @Longitude NOT BETWEEN -180 AND 180
    THROW 50400, N'Tọa độ không hợp lệ', 1;

  UPDATE dbo.Counters
  SET Name = @Name, Description = @Description, Latitude = @Latitude, Longitude = @Longitude, IsActive = @IsActive
  OUTPUT inserted.CounterId AS id, inserted.Name AS name, inserted.Description AS description,
         inserted.Latitude AS lat, inserted.Longitude AS lng, inserted.IsActive AS isActive
  WHERE CounterId = @CounterId;
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy quầy', 1;
END;
GO

-- ---------- Yêu thích ----------
CREATE OR ALTER PROCEDURE dbo.sp_Favorite_GetList
  @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  SELECT f.ProductId AS productId, p.Name AS name, p.Price AS price, p.ImageUrl AS imageUrl,
         p.IsAvailable AS isAvailable, f.CreatedAt AS createdAt
  FROM dbo.Favorites f
  JOIN dbo.Products p ON p.ProductId = f.ProductId
  WHERE f.UserId = @UserId
  ORDER BY f.CreatedAt DESC;
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Favorite_Add
  @UserId INT, @ProductId INT
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM dbo.Products WHERE ProductId = @ProductId)
    THROW 50404, N'Không tìm thấy món ăn', 1;
  IF NOT EXISTS (SELECT 1 FROM dbo.Favorites WHERE UserId = @UserId AND ProductId = @ProductId)
    INSERT INTO dbo.Favorites (UserId, ProductId) VALUES (@UserId, @ProductId);
END;
GO

CREATE OR ALTER PROCEDURE dbo.sp_Favorite_Remove
  @UserId INT, @ProductId INT
AS
BEGIN
  SET NOCOUNT ON;
  DELETE FROM dbo.Favorites WHERE UserId = @UserId AND ProductId = @ProductId;
END;
GO
