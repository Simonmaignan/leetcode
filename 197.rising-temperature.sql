-- https://leetcode.com/problems/rising-temperature
SELECT w2.id as Id
FROM Weather w1 LEFT JOIN Weather w2 ON w1.recordDate = w2.recordDate - 1
WHERE w1.temperature < w2.temperature