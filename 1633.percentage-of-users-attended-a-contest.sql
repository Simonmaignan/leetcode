DECLARE @nb_users FLOAT;
SET @nb_users = (SELECT COUNT(*) FROM Users);

SELECT
    contest_id,
    ROUND(COUNT(user_id) / @nb_users * 100, 2) as percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id