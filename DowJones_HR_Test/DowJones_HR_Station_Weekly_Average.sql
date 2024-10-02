SET NOCOUNT ON;

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
-- Weeks start on Saturday
SET DATEFIRST 6 ;
WITH Product1DailyPriceWithWeek AS
(    
    SELECT *, DATEPART(weekday, Price_Date) AS 'DayOfTheWeek', DATEPART(week, Price_Date) AS 'WeekNumber'
    FROM GasStationDailyPrice
    WHERE Product_ID = 1
)
SELECT GasStation_ID,
    MAX(Price_Date) AS 'LastDay',
    AVG(PRICE) AS 'AverageWeekPrice'
FROM Product1DailyPriceWithWeek
GROUP BY GasStation_ID, WeekNumber
ORDER BY GasStation_ID, LastDay
;
go