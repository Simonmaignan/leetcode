-- Write your MySQL query statement below
SELECT
    mgr.employee_id,
    mgr.name,
    COUNT(emp.employee_id) as reports_count,
    ROUND(AVG(emp.age), 0) as average_age
FROM
    Employees emp
    LEFT JOIN Employees mgr
    ON emp.reports_to = mgr.employee_id
WHERE mgr.employee_id is not null
GROUP BY mgr.employee_id, mgr.name
ORDER BY mgr.employee_id