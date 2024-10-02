SET NOCOUNT ON;

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
-- SELECT 
--     GasStation_ID, 
--     Product_ID,
--     MIN(Price_Date) AS FirstDate,
--     Price AS FirstPrice
-- FROM GasStationDailyPrice
-- GROUP BY GasStation_ID, Product_ID
WITH 
OrderedDailyPrice AS(
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY GasStation_ID, Product_ID ORDER BY Price_Date DESC) AS 'Row_Number_Desc',
        ROW_NUMBER() OVER (PARTITION BY GasStation_ID, Product_ID ORDER BY Price_Date) AS 'Row_Number_Asc'
    FROM GasStationDailyPrice
),
FirstReportedPrice AS(
    SELECT
        GasStation_ID,
        Product_ID,
        Price as FirstReportedPrice
    FROM OrderedDailyPrice
    WHERE Row_Number_Asc = 1
),
LastReportedPrice AS(
    SELECT
        GasStation_ID,
        Product_ID,
        Price as LastReportedPrice
    FROM OrderedDailyPrice
    WHERE Row_Number_Desc = 1
)
SELECT
    f.GasStation_ID,
    f.Product_ID,
    f.FirstReportedPrice,
    l.LastReportedPrice
FROM FirstReportedPrice f
JOIN LastReportedPrice l
ON f.GasStation_ID = l.GasStation_ID
AND f.Product_ID = l.Product_ID
;
go