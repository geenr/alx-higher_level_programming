-- a script that lists all genres and displays the number of shows linked to each
-- First column must be called genre second column number_of_shows and is sorted in a descending order
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genre
ORDER BY number_of_shows DESC;
