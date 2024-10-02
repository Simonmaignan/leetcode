SET NOCOUNT ON;


WITH 
    GasStationRawPriceWithDate AS(
        SELECT *, CONVERT(date, Price_DateTime) as Price_Date
        FROM GasStationRawPrice
    ),
    OrderedPrices AS(
        SELECT *,
        ROW_NUMBER() OVER (PARTITION BY GasStation_ID, Product_ID, Price_Date ORDER BY Price_DateTime DESC) AS 'Row_Number'
        FROM GasStationRawPriceWithDate
    )
SELECT GasStation_ID, Product_ID, Price_DateTime, Price
-- SELECT *
FROM OrderedPrices
WHERE Row_Number = 1
;
go