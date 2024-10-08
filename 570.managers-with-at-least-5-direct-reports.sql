-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports
WITH managers_5 AS 
(
    SELECT 
        managerId 
    FROM Employee
    GROUP BY managerId
    HAVING count(id) >= 5
)
SELECT e.name
FROM managers_5 m
JOIN Employee e
ON e.id = m.managerId