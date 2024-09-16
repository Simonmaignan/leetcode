-- https://leetcode.com/problems/project-employees-i
SELECT 
    project_id,
    round(cast(avg(experience_years) AS numeric), 2) AS average_years
FROM Project p LEFT JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY project_id