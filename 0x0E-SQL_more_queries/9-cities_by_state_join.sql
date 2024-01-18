-- list all cities in hbtn_0d_usa
-- only the SELECT statement can be used
-- the order is by cities.id in the format of cities.id - cities.name - states.name
SELECT cities-id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.states_id ORDER BY cities.id
