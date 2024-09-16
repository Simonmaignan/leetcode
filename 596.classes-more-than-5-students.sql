-- https://leetcode.com/problems/classes-more-than-5-students
SELECT class
FROM (
    SELECT
        class,
        count(student) as nb_students
    FROM Courses
    GROUP BY class
    )
WHERE nb_students >= 5