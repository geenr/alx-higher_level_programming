-- a script that lists all cities of california 
-- the states table can only one record where name=california but id may change
-- esults must be sorted in ascending order by cities.id using ASC
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
