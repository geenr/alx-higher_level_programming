-- a script that lists the no of records with the same score in adescending order using GROUP BY
-- the number of records are saved as numbers
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
