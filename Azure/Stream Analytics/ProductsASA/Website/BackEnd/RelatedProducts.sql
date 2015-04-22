USE [ziv-promotions-db]
GO

IF OBJECT_ID('RelatedProducts') IS NOT NULL DROP TABLE RelatedProducts
GO

CREATE TABLE RelatedProducts(
	ProductId BIGINT,
	RelatedProductId BIGINT
	PRIMARY KEY (ProductId, RelatedProductId)
)
GO

INSERT INTO RelatedProducts VALUES(1726268, 1872715)
INSERT INTO RelatedProducts VALUES(1726268, 1908846)
INSERT INTO RelatedProducts VALUES(1872715, 1908846)
GO
