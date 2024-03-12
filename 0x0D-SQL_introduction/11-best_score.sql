-- lists all scores above 10 in a descending order together with their names
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
