create table countries(
country_id serial,
country_name varchar(50)
)

insert into countries(country_name)values
('italy'),('germany'),('france'),('poland')

SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
FROM actors1
INNER JOIN countries
ON actors1.id=countries.country_id

SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
FROM actors1
LEFT OUTER JOIN countries
ON actors1.id=countries.country_id

SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
FROM actors1
RIGHT OUTER JOIN countries
ON actors1.id=countries.country_id

SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
FROM actors1
FULL JOIN countries
ON actors1.id=countries.country_id

