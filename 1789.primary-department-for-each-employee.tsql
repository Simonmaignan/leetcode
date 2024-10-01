WITH employees_nb_dep AS (
    SELECT 
        employee_id,
        COUNT(department_id) as nb_dep
    FROM Employee
    GROUP BY employee_id
)
SELECT 
    e.employee_id,
    e.department_id
FROM Employee e JOIN employees_nb_dep e2 ON e.employee_id = e2.employee_id
WHERE e2.nb_dep = 1 OR e2.nb_dep > 1 AND e.primary_flag = 'Y'