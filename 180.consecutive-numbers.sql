-- https://leetcode.com/problems/consecutive-numbers
WITH next_nums AS 
(
    SELECT
        l1.id,
        l1.num,
        l2.num AS next_num,
        l3.num AS next_next_num
    FROM Logs l1
    LEFT JOIN Logs l2
    ON l2.id = l1.id + 1
    LEFT JOIN Logs l3
    ON l3.id = l1.id + 2
)
SELECT DISTINCT num AS ConsecutiveNums
FROM next_nums
WHERE num = next_num AND next_num = next_next_num