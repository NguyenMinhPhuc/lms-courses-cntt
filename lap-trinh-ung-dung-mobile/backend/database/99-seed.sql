-- Dữ liệu mẫu: danh mục, món, quầy. Chỉ thêm khi bảng đang trống, nên chạy lại không bị trùng.
-- Tài khoản mẫu (admin, staff, customer) được scripts/db-setup.js tạo vì mật khẩu phải băm bằng bcrypt.
SET NOCOUNT ON;
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Categories)
BEGIN
  INSERT INTO dbo.Categories (Name, SortOrder) VALUES
    (N'Cơm', 1), (N'Bún - Phở', 2), (N'Mì - Hủ tiếu', 3), (N'Đồ uống', 4), (N'Ăn vặt', 5);
END;
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Products)
BEGIN
  DECLARE @Com INT = (SELECT CategoryId FROM dbo.Categories WHERE Name = N'Cơm');
  DECLARE @Bun INT = (SELECT CategoryId FROM dbo.Categories WHERE Name = N'Bún - Phở');
  DECLARE @Mi  INT = (SELECT CategoryId FROM dbo.Categories WHERE Name = N'Mì - Hủ tiếu');
  DECLARE @Uong INT = (SELECT CategoryId FROM dbo.Categories WHERE Name = N'Đồ uống');
  DECLARE @Vat INT = (SELECT CategoryId FROM dbo.Categories WHERE Name = N'Ăn vặt');

  INSERT INTO dbo.Products (CategoryId, Name, Description, Price, Stock, IsAvailable) VALUES
    (@Com, N'Cơm gà xối mỡ', N'Đùi gà chiên giòn, cơm chiên, dưa leo', 35000, 40, 1),
    (@Com, N'Cơm tấm sườn bì', N'Sườn nướng, bì, chả, nước mắm chua ngọt', 38000, 40, 1),
    (@Com, N'Cơm chiên dương châu', N'Cơm chiên trứng, lạp xưởng, tôm', 32000, 30, 1),
    (@Com, N'Cơm gà luộc', N'Gà ta luộc, nước mắm gừng', 35000, 1, 1),
    (@Bun, N'Bún bò Huế', N'Bò, chả cua, giò heo, rau sống', 40000, 30, 1),
    (@Bun, N'Phở bò tái', N'Bánh phở, bò tái, hành, ngò', 40000, 30, 1),
    (@Bun, N'Bún thịt nướng', N'Thịt nướng, chả giò, rau, đậu phộng', 35000, 25, 1),
    (@Mi,  N'Mì xào bò', N'Mì xào giòn, thịt bò, rau cải', 38000, 20, 1),
    (@Mi,  N'Hủ tiếu Nam Vang', N'Tôm, thịt bằm, gan, trứng cút', 38000, 20, 1),
    (@Uong, N'Trà đào cam sả', N'Trà đào, cam vàng, sả', 20000, 60, 1),
    (@Uong, N'Cà phê sữa đá', N'Cà phê phin, sữa đặc', 18000, 60, 1),
    (@Uong, N'Nước ép cam', N'Cam tươi ép, không đường', 22000, 30, 1),
    (@Uong, N'Trà sữa trân châu', N'Trà sữa, trân châu đen', 25000, 0, 0),
    (@Vat, N'Bánh mì thịt', N'Bánh mì, pate, thịt nguội, đồ chua', 20000, 40, 1),
    (@Vat, N'Khoai tây chiên', N'Khoai tây chiên giòn, tương cà', 15000, 30, 1);
END;
GO

-- Tọa độ mẫu trong khuôn viên trường; quản lý cập nhật tọa độ thật bằng API /admin/counters
IF NOT EXISTS (SELECT 1 FROM dbo.Counters)
BEGIN
  INSERT INTO dbo.Counters (Name, Description, Latitude, Longitude) VALUES
    (N'Căn tin cơ sở 1', N'Tầng trệt, gần cổng chính', 10.946915, 106.824290),
    (N'Căn tin cơ sở 2', N'Khu nhà học B', 10.948560, 106.826120),
    (N'Quầy thư viện', N'Sảnh thư viện, chỉ bán đồ uống và ăn vặt', 10.947700, 106.825100);
END;
GO
