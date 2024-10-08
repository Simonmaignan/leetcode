-- https://leetcode.com/problems/movie-rating
WITH nb_rated_movies AS 
(
    SELECT
        u.name,
        COUNT(r.movie_id) AS nb_rated_movies
    FROM MovieRating r
    JOIN Users u
    ON r.user_id = u.user_id
    GROUP BY r.user_id
    ORDER BY nb_rated_movies DESC, u.name
), highest_avg_rating AS
(
    SELECT
        m.title,
        AVG(r.rating) as avg_rating
    FROM MovieRating r
    JOIN Movies m
    ON r.movie_id = m.movie_id
    WHERE DATE_FORMAT(created_at,'%Y-%m') = '2020-02'
    GROUP BY m.title
    ORDER BY avg_rating DESC, m.title
)
(SELECT name as results FROM nb_rated_movies LIMIT 1)
UNION ALL
(SELECT title as results FROM highest_avg_rating LIMIT 1)
;