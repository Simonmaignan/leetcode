-- https://leetcode.com/problems/biggest-single-number
SELECT MAX(num) as num
FROM (
    SELECT num, COUNT(num) as count_num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) <= 1
) AS MySingleNumbers