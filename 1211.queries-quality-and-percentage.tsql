-- https://leetcode.com/problems/queries-quality-and-percentage
WITH updated_queries AS (SELECT *,
    "poor_rating" = CASE 
    WHEN rating < 3 THEN 1.0
    ELSE 0.0
    END
FROM Queries)
SELECT
    query_name,
    ROUND(avg(CAST(rating as numeric) / CAST(position as numeric)), 2) as quality,
    ROUND(avg(poor_rating) * 100.0, 2) as poor_query_percentage
FROM updated_queries
WHERE query_name is not null
GROUP BY query_name