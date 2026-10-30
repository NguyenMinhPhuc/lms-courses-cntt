-- LHU Food - Bảng, khóa, ràng buộc, chỉ mục (SRS mục 7). Chạy lại nhiều lần không lỗi.
-- Yêu cầu: SQL Server 2019 trở lên.
SET NOCOUNT ON;
GO

IF OBJECT_ID(N'dbo.Categories', N'U') IS NULL
CREATE TABLE dbo.Categories (
  CategoryId INT IDENTITY(1,1) CONSTRAINT PK_Categories PRIMARY KEY,
  Name       NVARCHAR(100) NOT NULL CONSTRAINT UQ_Categories_Name UNIQUE,
  SortOrder  INT NOT NULL CONSTRAINT DF_Categories_SortOrder DEFAULT 0
);
GO

IF OBJECT_ID(N'dbo.Products', N'U') IS NULL
CREATE TABLE dbo.Products (
  ProductId   INT IDENTITY(1,1) CONSTRAINT PK_Products PRIMARY KEY,
  CategoryId  INT NOT NULL CONSTRAINT FK_Products_Categories REFERENCES dbo.Categories(CategoryId),
  Name        NVARCHAR(150) NOT NULL,
  Description NVARCHAR(500) NULL,
  Price       DECIMAL(12,0) NOT NULL CONSTRAINT CK_Products_Price CHECK (Price >= 0),
  ImageUrl    NVARCHAR(500) NULL,
  IsAvailable BIT NOT NULL CONSTRAINT DF_Products_IsAvailable DEFAULT 1,
  Stock       INT NOT NULL CONSTRAINT DF_Products_Stock DEFAULT 0 CONSTRAINT CK_Products_Stock CHECK (Stock >= 0),
  CreatedAt   DATETIME2 NOT NULL CONSTRAINT DF_Products_CreatedAt DEFAULT SYSDATETIME(),
  UpdatedAt   DATETIME2 NULL
);
GO

IF OBJECT_ID(N'dbo.Users', N'U') IS NULL
CREATE TABLE dbo.Users (
  UserId       INT IDENTITY(1,1) CONSTRAINT PK_Users PRIMARY KEY,
  FullName     NVARCHAR(100) NOT NULL,
  Email        NVARCHAR(255) NOT NULL CONSTRAINT UQ_Users_Email UNIQUE,
  PasswordHash NVARCHAR(255) NOT NULL,
  Role         NVARCHAR(20)  NOT NULL CONSTRAINT DF_Users_Role DEFAULT N'customer'
               CONSTRAINT CK_Users_Role CHECK (Role IN (N'customer', N'staff', N'admin')),
  AvatarUrl    NVARCHAR(500) NULL,
  IsLocked     BIT NOT NULL CONSTRAINT DF_Users_IsLocked DEFAULT 0,
  CreatedAt    DATETIME2 NOT NULL CONSTRAINT DF_Users_CreatedAt DEFAULT SYSDATETIME()
);
GO

IF OBJECT_ID(N'dbo.RefreshTokens', N'U') IS NULL
CREATE TABLE dbo.RefreshTokens (
  TokenId   INT IDENTITY(1,1) CONSTRAINT PK_RefreshTokens PRIMARY KEY,
  UserId    INT NOT NULL CONSTRAINT FK_RefreshTokens_Users REFERENCES dbo.Users(UserId),
  TokenHash CHAR(64) NOT NULL CONSTRAINT UQ_RefreshTokens_TokenHash UNIQUE,   -- SHA-256 dạng hex
  ExpiresAt DATETIME2 NOT NULL,
  RevokedAt DATETIME2 NULL,
  CreatedAt DATETIME2 NOT NULL CONSTRAINT DF_RefreshTokens_CreatedAt DEFAULT SYSDATETIME()
);
GO

IF OBJECT_ID(N'dbo.Counters', N'U') IS NULL
CREATE TABLE dbo.Counters (
  CounterId   INT IDENTITY(1,1) CONSTRAINT PK_Counters PRIMARY KEY,
  Name        NVARCHAR(100) NOT NULL,
  Description NVARCHAR(200) NULL,
  Latitude    DECIMAL(9,6) NOT NULL CONSTRAINT CK_Counters_Latitude CHECK (Latitude BETWEEN -90 AND 90),
  Longitude   DECIMAL(9,6) NOT NULL CONSTRAINT CK_Counters_Longitude CHECK (Longitude BETWEEN -180 AND 180),
  IsActive    BIT NOT NULL CONSTRAINT DF_Counters_IsActive DEFAULT 1
);
GO

IF OBJECT_ID(N'dbo.Orders', N'U') IS NULL
CREATE TABLE dbo.Orders (
  OrderId      INT IDENTITY(1,1) CONSTRAINT PK_Orders PRIMARY KEY,
  UserId       INT NOT NULL CONSTRAINT FK_Orders_Users REFERENCES dbo.Users(UserId),
  CounterId    INT NULL CONSTRAINT FK_Orders_Counters REFERENCES dbo.Counters(CounterId),
  Status       NVARCHAR(20) NOT NULL CONSTRAINT DF_Orders_Status DEFAULT N'pending'
               CONSTRAINT CK_Orders_Status CHECK (Status IN (N'pending', N'preparing', N'ready', N'completed', N'cancelled')),
  Note         NVARCHAR(200) NULL,
  CancelReason NVARCHAR(200) NULL,
  CreatedAt    DATETIME2 NOT NULL CONSTRAINT DF_Orders_CreatedAt DEFAULT SYSDATETIME(),
  UpdatedAt    DATETIME2 NULL
);
GO

IF OBJECT_ID(N'dbo.OrderItems', N'U') IS NULL
CREATE TABLE dbo.OrderItems (
  OrderId   INT NOT NULL CONSTRAINT FK_OrderItems_Orders REFERENCES dbo.Orders(OrderId),
  ProductId INT NOT NULL CONSTRAINT FK_OrderItems_Products REFERENCES dbo.Products(ProductId),
  Quantity  INT NOT NULL CONSTRAINT CK_OrderItems_Quantity CHECK (Quantity > 0),
  UnitPrice DECIMAL(12,0) NOT NULL,
  CONSTRAINT PK_OrderItems PRIMARY KEY (OrderId, ProductId)
);
GO

IF OBJECT_ID(N'dbo.Favorites', N'U') IS NULL
CREATE TABLE dbo.Favorites (
  UserId    INT NOT NULL CONSTRAINT FK_Favorites_Users REFERENCES dbo.Users(UserId),
  ProductId INT NOT NULL CONSTRAINT FK_Favorites_Products REFERENCES dbo.Products(ProductId),
  CreatedAt DATETIME2 NOT NULL CONSTRAINT DF_Favorites_CreatedAt DEFAULT SYSDATETIME(),
  CONSTRAINT PK_Favorites PRIMARY KEY (UserId, ProductId)
);
GO

IF OBJECT_ID(N'dbo.Notifications', N'U') IS NULL
CREATE TABLE dbo.Notifications (
  NotificationId INT IDENTITY(1,1) CONSTRAINT PK_Notifications PRIMARY KEY,
  UserId         INT NOT NULL CONSTRAINT FK_Notifications_Users REFERENCES dbo.Users(UserId),
  Title          NVARCHAR(100) NOT NULL,
  Body           NVARCHAR(300) NOT NULL,
  OrderId        INT NULL CONSTRAINT FK_Notifications_Orders REFERENCES dbo.Orders(OrderId),
  IsRead         BIT NOT NULL CONSTRAINT DF_Notifications_IsRead DEFAULT 0,
  CreatedAt      DATETIME2 NOT NULL CONSTRAINT DF_Notifications_CreatedAt DEFAULT SYSDATETIME()
);
GO

IF OBJECT_ID(N'dbo.Reviews', N'U') IS NULL
CREATE TABLE dbo.Reviews (
  ReviewId  INT IDENTITY(1,1) CONSTRAINT PK_Reviews PRIMARY KEY,
  OrderId   INT NOT NULL CONSTRAINT FK_Reviews_Orders REFERENCES dbo.Orders(OrderId),
  ProductId INT NOT NULL CONSTRAINT FK_Reviews_Products REFERENCES dbo.Products(ProductId),
  UserId    INT NOT NULL CONSTRAINT FK_Reviews_Users REFERENCES dbo.Users(UserId),
  Rating    TINYINT NOT NULL CONSTRAINT CK_Reviews_Rating CHECK (Rating BETWEEN 1 AND 5),
  Comment   NVARCHAR(500) NULL,
  CreatedAt DATETIME2 NOT NULL CONSTRAINT DF_Reviews_CreatedAt DEFAULT SYSDATETIME(),
  CONSTRAINT UQ_Reviews_Order_Product UNIQUE (OrderId, ProductId)
);
GO

-- Chỉ mục theo các thủ tục được gọi nhiều nhất (Chương 7)
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_Products_CategoryId')
  CREATE INDEX IX_Products_CategoryId ON dbo.Products (CategoryId) INCLUDE (Name, Price, ImageUrl, IsAvailable, Stock);
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_Orders_UserId_CreatedAt')
  CREATE INDEX IX_Orders_UserId_CreatedAt ON dbo.Orders (UserId, CreatedAt DESC);
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_Orders_Status_CreatedAt')
  CREATE INDEX IX_Orders_Status_CreatedAt ON dbo.Orders (Status, CreatedAt DESC);
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_Notifications_UserId')
  CREATE INDEX IX_Notifications_UserId ON dbo.Notifications (UserId, IsRead, CreatedAt DESC);
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_RefreshTokens_UserId')
  CREATE INDEX IX_RefreshTokens_UserId ON dbo.RefreshTokens (UserId) WHERE RevokedAt IS NULL;
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_Reviews_ProductId')
  CREATE INDEX IX_Reviews_ProductId ON dbo.Reviews (ProductId, CreatedAt DESC);
GO
