USE world;
SELECT countries.name FROM countries 
JOIN languages ON countries.id = languages.country_id
WHERE language = 'Slovene';

SELECT countries.name, COUNT(cities.id) name FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id;

SELECT cities.name, cities.population FROM cities
JOIN countries ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY population DESC;

SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE percentage > 89;

SELECT name, surface_area, population FROM countries
WHERE population > 100000 AND surface_area < 501;

SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;