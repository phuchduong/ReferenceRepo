USE [ziv-promotions-db]
GO

IF OBJECT_ID('Promotions') IS NOT NULL DROP TABLE Promotions
GO

CREATE TABLE Promotions(
	Id INT IDENTITY(1,1) PRIMARY KEY,
	CustomerId BIGINT,
	ProductId BIGINT,
	NewPrice INT,
	Promotion NVARCHAR(10),
	[Count] BIGINT
)
GO

INSERT INTO Promotions VALUES(1, 1726268, 70, '$10', 2)
GO
