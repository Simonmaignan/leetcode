SELECT
    e.name,
    b.bonus
FROM Employee e LEFT JOIN Bonus b on e.empId = b.empId
WHERE b.bonus is null or b.bonus < 1000