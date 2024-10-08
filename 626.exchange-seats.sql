-- https://leetcode.com/problems/exchange-seats
SELECT
    if(id = MAX(id), id, if(id % 2 = 0, id - 1, id + 1)) as id,
    student
FROM Seat
ORDER BY id