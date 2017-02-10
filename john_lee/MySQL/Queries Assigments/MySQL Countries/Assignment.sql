Use world;
-- All countries that speak Slovene. Return name of country, language, and language percentage(descending order)
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY languages.percentage DESC;

-- Total number of cities of each country. Name of country and total # of cities (descending)
SELECT COUNT(cities.name), countries.name
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.name) DESC;

-- All cities in Mexico with pop greater than 500,000 (descending). 
SELECT countries.name, cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico'
AND cities.population < 500000
GROUP BY cities.name
ORDER BY (cities.population) DESC;

-- All languages in each country with percentage greater than 89% (desending order
SELECT countries.name, languages.percentage, languages.language
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
GROUP BY languages.language
ORDER BY (languages.percentage) DESC;

-- All countries with surface area below 501 and population greater than 100,000
SELECT countries.name, countries.surface_area, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.population < 100000
AND countries.surface_area < 501
GROUP BY countries.name;

-- Countries with only COnstitutional Monarchy, captial reater than 200, and life expectancy greater than 75 years
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy'
AND countries.capital > 200
AND countries.life_expectancy > 75
GROUP BY countries.name;

-- ALL cities of Argentina inside Buenos Aires district and hav pop of 500,000. Return County name, CIty ame, DIstrict, and population
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
AND cities.district = 'Buenos Aires'
AND cities.population < 500000
GROUP BY cities.name;

-- Summarize all the countries in a region, display name of region and number of countries, desc
SELECT COUNT(countries.region), countries.region
FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.region) DESC;

