# Phụ lục A. Mã nguồn đầy đủ

Các đoạn mã dài hơn 40 dòng được đặt ở phụ lục này để chương chính dễ đọc; trong chương chỉ giữ phần đầu của mỗi đoạn. Mã nguồn đầy đủ của dự án mẫu cũng có trong repo của học phần.

## A.1. 5.3.3. Thủ tục đọc dữ liệu (Chương 5)

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
  IF @Page < 1 OR @PageSize NOT BETWEEN 1 AND 100
    THROW 50400, N'Tham số phân trang không hợp lệ', 1;

  SELECT ProductId AS id, CategoryId AS categoryId, Name AS name,
         Price AS price, ImageUrl AS imageUrl
  FROM Products
  WHERE IsAvailable = 1
    AND (@CategoryId IS NULL OR CategoryId = @CategoryId)
  ORDER BY ProductId
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO

CREATE OR ALTER PROCEDURE sp_Product_GetById
  @ProductId INT
AS
BEGIN
  SET NOCOUNT ON;
  IF NOT EXISTS (SELECT 1 FROM Products WHERE ProductId = @ProductId)
    THROW 50404, N'Không tìm thấy món ăn', 1;

  SELECT ProductId AS id, CategoryId AS categoryId, Name AS name, Description AS description,
         Price AS price, ImageUrl AS imageUrl, IsAvailable AS isAvailable
  FROM Products
  WHERE ProductId = @ProductId;
END;
GO
```

## A.2. 5.4.2. DatabaseService dùng chung (Chương 5)

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
      database: process.env.DB_NAME!,
      user: process.env.DB_USER!,
      password: process.env.DB_PASSWORD!,
      options: { encrypt: false, trustServerCertificate: true },
    }).connect();
  }

  async onModuleDestroy() {
    await this.pool?.close();
  }

  /** Cách DUY NHẤT để truy cập CSDL: chạy stored procedure với tham số có kiểu. */
  async execute<T>(procedure: string, params: Record<string, SqlParam> = {}): Promise<T[]> {
    const request = this.pool.request();
    for (const [name, p] of Object.entries(params)) {
      request.input(name, p.type, p.value);
    }
    try {
      const result = await request.execute<T>(procedure);
      return result.recordset ?? [];
    } catch (err: any) {
      // Chuyển mã lỗi tự đặt trong thủ tục thành mã HTTP
      if (err?.number === 50400) throw new BadRequestException(err.message);
      if (err?.number === 50404) throw new NotFoundException(err.message);
      if (err?.number === 50409) throw new ConflictException(err.message);
      throw err;
    }
  }
}
```

## A.3. 6.3.2. Bảng và thủ tục (Chương 6)

```sql
CREATE TABLE Users (
  UserId       INT IDENTITY(1,1) PRIMARY KEY,
  FullName     NVARCHAR(100) NOT NULL,
  Email        NVARCHAR(255) NOT NULL UNIQUE,
  PasswordHash NVARCHAR(255) NOT NULL,
  Role         NVARCHAR(20)  NOT NULL DEFAULT N'customer'
               CHECK (Role IN (N'customer', N'staff')),
  CreatedAt    DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

ALTER TABLE Orders ADD CONSTRAINT FK_Orders_Users FOREIGN KEY (UserId) REFERENCES Users(UserId);

CREATE TABLE RefreshTokens (
  TokenId   INT IDENTITY(1,1) PRIMARY KEY,
  UserId    INT NOT NULL REFERENCES Users(UserId),
  TokenHash CHAR(64) NOT NULL UNIQUE,      -- SHA-256 dạng hex
  ExpiresAt DATETIME2 NOT NULL,
  RevokedAt DATETIME2 NULL
);
GO

CREATE OR ALTER PROCEDURE sp_User_Register
  @FullName NVARCHAR(100), @Email NVARCHAR(255), @PasswordHash NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  IF EXISTS (SELECT 1 FROM Users WHERE Email = @Email)
    THROW 50409, N'Email đã được sử dụng', 1;

  INSERT INTO Users (FullName, Email, PasswordHash) VALUES (@FullName, @Email, @PasswordHash);
  SELECT CAST(SCOPE_IDENTITY() AS INT) AS userId;
END;
GO

-- Thủ tục nội bộ cho backend: trả PasswordHash, không bao giờ gửi kết quả này cho ứng dụng
CREATE OR ALTER PROCEDURE sp_User_GetByEmail
  @Email NVARCHAR(255)
AS
BEGIN
  SET NOCOUNT ON;
  SELECT UserId, FullName, Email, PasswordHash, Role FROM Users WHERE Email = @Email;
END;
GO

CREATE OR ALTER PROCEDURE sp_RefreshToken_Save
  @UserId INT, @TokenHash CHAR(64), @ExpiresAt DATETIME2
AS
BEGIN
  SET NOCOUNT ON;
  INSERT INTO RefreshTokens (UserId, TokenHash, ExpiresAt) VALUES (@UserId, @TokenHash, @ExpiresAt);
END;
GO

CREATE OR ALTER PROCEDURE sp_RefreshToken_Use
  @TokenHash CHAR(64)
AS
BEGIN
  SET NOCOUNT ON;
  -- Mỗi refresh token chỉ dùng một lần: thu hồi bản cũ, trả về người dùng nếu còn hiệu lực
  UPDATE RefreshTokens SET RevokedAt = SYSDATETIME()
  OUTPUT inserted.UserId AS userId
  WHERE TokenHash = @TokenHash AND RevokedAt IS NULL AND ExpiresAt > SYSDATETIME();
END;
GO

CREATE OR ALTER PROCEDURE sp_RefreshToken_Revoke
  @TokenHash CHAR(64)
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE RefreshTokens SET RevokedAt = SYSDATETIME() WHERE TokenHash = @TokenHash AND RevokedAt IS NULL;
END;
GO
```

## A.4. 6.4.2. AuthService (Chương 6)

```ts
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';
import { createHash } from 'crypto';
import * as sql from 'mssql';
import { DatabaseService } from '../database/database.service';

type UserRow = { UserId: number; FullName: string; Email: string; PasswordHash: string; Role: string };
const sha256 = (value: string) => createHash('sha256').update(value).digest('hex');

@Injectable()
export class AuthService {
  constructor(private readonly db: DatabaseService, private readonly jwt: JwtService) {}

  async register(fullName: string, email: string, password: string) {
    const passwordHash = await bcrypt.hash(password, 10);
    const [row] = await this.db.execute<{ userId: number }>('sp_User_Register', {
      FullName: { type: sql.NVarChar(100), value: fullName },
      Email: { type: sql.NVarChar(255), value: email },
      PasswordHash: { type: sql.NVarChar(255), value: passwordHash },
    });
    return row;
  }

  async login(email: string, password: string) {
    const [user] = await this.db.execute<UserRow>('sp_User_GetByEmail', {
      Email: { type: sql.NVarChar(255), value: email },
    });
    if (!user || !(await bcrypt.compare(password, user.PasswordHash))) {
      throw new UnauthorizedException('Email hoặc mật khẩu không đúng');
    }
    return this.issueTokens(user.UserId, user.Role);
  }

  async refresh(refreshToken: string) {
    let payload: { sub: number; role: string };
    try {
      payload = await this.jwt.verifyAsync(refreshToken, { secret: process.env.JWT_REFRESH_SECRET });
    } catch {
      throw new UnauthorizedException();
    }
    const [row] = await this.db.execute<{ userId: number }>('sp_RefreshToken_Use', {
      TokenHash: { type: sql.Char(64), value: sha256(refreshToken) },
    });
    if (!row) throw new UnauthorizedException();
    return this.issueTokens(payload.sub, payload.role);
  }

  async logout(refreshToken: string) {
    await this.db.execute('sp_RefreshToken_Revoke', {
      TokenHash: { type: sql.Char(64), value: sha256(refreshToken) },
    });
  }

  private async issueTokens(userId: number, role: string) {
    const payload = { sub: userId, role };
    const accessToken = await this.jwt.signAsync(payload);
    const refreshToken = await this.jwt.signAsync(payload, {
      secret: process.env.JWT_REFRESH_SECRET,
      expiresIn: '7d',
    });
    await this.db.execute('sp_RefreshToken_Save', {
      UserId: { type: sql.Int, value: userId },
      TokenHash: { type: sql.Char(64), value: sha256(refreshToken) },
      ExpiresAt: { type: sql.DateTime2, value: new Date(Date.now() + 7 * 24 * 3600 * 1000) },
    });
    return { accessToken, refreshToken, role };
  }
}
```

## A.5. 7.3.4. Thủ tục đặt hàng hoàn chỉnh (Chương 7)

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

## A.6. 8.3.4. Màn hình bản đồ (Chương 8)

```tsx
import { useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import MapView, { Marker } from 'react-native-maps';
import { useQuery } from '@tanstack/react-query';
import { api } from '@/lib/api';
import { getMyLocation } from '@/lib/location';
import { distanceKm } from '@/lib/distance';

type Counter = { id: number; name: string; lat: number; lng: number };

export default function MapScreen() {
  const { data: counters = [] } = useQuery({ queryKey: ['counters'], queryFn: () => api<Counter[]>('/counters') });
  const [me, setMe] = useState<{ lat: number; lng: number } | null>(null);

  useEffect(() => {
    getMyLocation().then((pos) => pos && setMe({ lat: pos.latitude, lng: pos.longitude }));
  }, []);

  const first = counters[0];
  if (!first) return <Text style={{ padding: 16 }}>Chưa có dữ liệu quầy.</Text>;

  const nearest = me ? [...counters].sort((a, b) => distanceKm(me, a) - distanceKm(me, b))[0] : null;

  return (
    <View style={{ flex: 1 }}>
      <MapView
        style={StyleSheet.absoluteFill}
        showsUserLocation
        initialRegion={{ latitude: first.lat, longitude: first.lng, latitudeDelta: 0.01, longitudeDelta: 0.01 }}
      >
        {counters.map((c) => (
          <Marker key={c.id} coordinate={{ latitude: c.lat, longitude: c.lng }} title={c.name} />
        ))}
      </MapView>
      {nearest && me && (
        <View style={styles.banner}>
          <Text>Quầy gần bạn nhất: {nearest.name} ({Math.round(distanceKm(me, nearest) * 1000)} m)</Text>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  banner: { position: 'absolute', left: 16, right: 16, bottom: 24, padding: 12, borderRadius: 12, backgroundColor: '#fff' },
});
```

## A.7. 9.3. Cơ sở dữ liệu cho thông báo (Chương 9)

```sql
CREATE TABLE Notifications (
  NotificationId INT IDENTITY(1,1) PRIMARY KEY,
  UserId         INT NOT NULL REFERENCES Users(UserId),
  Title          NVARCHAR(100) NOT NULL,
  Body           NVARCHAR(300) NOT NULL,
  OrderId        INT NULL REFERENCES Orders(OrderId),
  IsRead         BIT NOT NULL CONSTRAINT DF_Notifications_IsRead DEFAULT 0,
  CreatedAt      DATETIME2 NOT NULL CONSTRAINT DF_Notifications_CreatedAt DEFAULT SYSDATETIME()
);
CREATE INDEX IX_Notifications_UserId ON Notifications (UserId, IsRead, CreatedAt DESC);
GO

CREATE OR ALTER PROCEDURE sp_Order_UpdateStatus
  @OrderId INT, @Status NVARCHAR(20)
AS
BEGIN
  SET NOCOUNT ON;
  DECLARE @Current NVARCHAR(20) = (SELECT Status FROM Orders WHERE OrderId = @OrderId);
  IF @Current IS NULL
    THROW 50404, N'Không tìm thấy đơn hàng', 1;
  IF @Current IN (N'completed', N'cancelled')
    THROW 50409, N'Đơn đã kết thúc, không thể đổi trạng thái', 1;

  UPDATE Orders SET Status = @Status
  OUTPUT inserted.OrderId AS orderId, inserted.UserId AS userId, inserted.Status AS status
  WHERE OrderId = @OrderId;
END;
GO

CREATE OR ALTER PROCEDURE sp_Notification_Create
  @UserId INT, @Title NVARCHAR(100), @Body NVARCHAR(300), @OrderId INT = NULL
AS
BEGIN
  SET NOCOUNT ON;
  INSERT INTO Notifications (UserId, Title, Body, OrderId)
  OUTPUT inserted.NotificationId AS id, inserted.Title AS title, inserted.Body AS body,
         inserted.OrderId AS orderId, inserted.IsRead AS isRead, inserted.CreatedAt AS createdAt
  VALUES (@UserId, @Title, @Body, @OrderId);
END;
GO

CREATE OR ALTER PROCEDURE sp_Notification_GetList
  @UserId INT, @Page INT = 1, @PageSize INT = 20
AS
BEGIN
  SET NOCOUNT ON;
  SELECT NotificationId AS id, Title AS title, Body AS body, OrderId AS orderId,
         IsRead AS isRead, CreatedAt AS createdAt
  FROM Notifications
  WHERE UserId = @UserId
  ORDER BY CreatedAt DESC
  OFFSET (@Page - 1) * @PageSize ROWS FETCH NEXT @PageSize ROWS ONLY;
END;
GO

CREATE OR ALTER PROCEDURE sp_Notification_CountUnread @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  SELECT COUNT(*) AS unread FROM Notifications WHERE UserId = @UserId AND IsRead = 0;
END;
GO

CREATE OR ALTER PROCEDURE sp_Notification_MarkRead @NotificationId INT, @UserId INT
AS
BEGIN
  SET NOCOUNT ON;
  UPDATE Notifications SET IsRead = 1
  WHERE NotificationId = @NotificationId AND UserId = @UserId;   -- chỉ thông báo của chính mình
  IF @@ROWCOUNT = 0
    THROW 50404, N'Không tìm thấy thông báo', 1;
END;
GO
```

## A.8. 9.5.2. Hook kết nối realtime (Chương 9)

```ts
import { useEffect } from 'react';
import { io } from 'socket.io-client';
import { useQueryClient } from '@tanstack/react-query';
import * as Notifications from 'expo-notifications';
import { useAuth } from '@/stores/auth';

type OrderStatusEvent = {
  order: { orderId: number; status: string };
  notification: { id: number; title: string; body: string };
};

export function useRealtime() {
  const token = useAuth((s) => s.token);
  const role = useAuth((s) => s.role);
  const queryClient = useQueryClient();

  useEffect(() => {
    if (!token) return;
    const socket = io(process.env.EXPO_PUBLIC_API_URL!, {
      auth: { token },
      transports: ['websocket'],
    });

    socket.on('order:status', async ({ order, notification }: OrderStatusEvent) => {
      queryClient.invalidateQueries({ queryKey: ['orders'] });
      queryClient.invalidateQueries({ queryKey: ['notifications'] });
      await Notifications.scheduleNotificationAsync({
        content: { title: notification.title, body: notification.body, data: { url: `/order/${order.orderId}` } },
        trigger: null,
      });
    });

    if (role === 'staff') {
      socket.on('order:new', () => queryClient.invalidateQueries({ queryKey: ['orders'] }));
    }

    socket.on('connect', () => queryClient.invalidateQueries({ queryKey: ['notifications'] }));

    return () => {
      socket.disconnect();
    };
  }, [token, role, queryClient]);
}
```

## A.9. 10.3.2. Test store giỏ hàng (Chương 10)

```ts
import { useCart } from '../cart';

const comGa = { id: 1, name: 'Cơm gà', price: 35000 };
const traDao = { id: 2, name: 'Trà đào', price: 20000 };

beforeEach(() => {
  useCart.setState({ items: [] });
});

test('thêm món mới thì số lượng là 1', () => {
  useCart.getState().add(comGa);
  expect(useCart.getState().items).toEqual([{ ...comGa, quantity: 1 }]);
});

test('thêm trùng món thì cộng dồn số lượng', () => {
  useCart.getState().add(comGa);
  useCart.getState().add(comGa);
  expect(useCart.getState().items).toHaveLength(1);
  expect(useCart.getState().items[0].quantity).toBe(2);
});

test('tổng tiền bằng tổng giá nhân số lượng', () => {
  useCart.getState().add(comGa);
  useCart.getState().add(comGa);
  useCart.getState().add(traDao);
  expect(useCart.getState().total()).toBe(90000);
  expect(useCart.getState().count()).toBe(3);
});

test('giảm số lượng về 0 thì xóa món khỏi giỏ', () => {
  useCart.getState().add(traDao);
  useCart.getState().decrease(2);
  expect(useCart.getState().items).toEqual([]);
});

test('xóa một món không ảnh hưởng món khác', () => {
  useCart.getState().add(comGa);
  useCart.getState().add(traDao);
  useCart.getState().remove(1);
  expect(useCart.getState().items.map((i) => i.id)).toEqual([2]);
});
```
