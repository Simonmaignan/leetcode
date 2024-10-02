SET NOCOUNT ON;


/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
-- SELECT *
SELECT g.GasStation_Name
FROM GasStation g
LEFT JOIN GasStationDailyPrice p
ON g.GasStation_ID = p.GasStation_ID
WHERE p.Price IS NULL;

go