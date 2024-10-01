-- https://leetcode.com/problems/triangle-judgement
WITH TriangleDimension AS(
    SELECT
        *,
        x + y + z as sum_sides,
        GREATEST(x, y, z) as largest_side
    FROM Triangle
)
SELECT x, y, z,
    CASE
        WHEN largest_side < (sum_sides - largest_side) THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM TriangleDimension