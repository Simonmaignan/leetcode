-- https://leetcode.com/problems/students-and-examinations
SELECT 
    st.student_id,
    st.student_name,
    s.subject_name,
    COUNT(e.student_id) as attended_exams
FROM Subjects s
CROSS JOIN Students st 
LEFT JOIN Examinations e
ON s.subject_name = e.subject_name
AND st.student_id = e.student_id
GROUP BY st.student_id, st.student_name, s.subject_name
ORDER BY st.student_id, s.subject_name