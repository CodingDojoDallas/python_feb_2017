Use sakila;
#1
SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city_id
FROM country
JOIN city ON country.country_id = city.country_id
JOIN address ON city.city_id = address.city_id
JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;

#2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM category
JOIN film ON category.category_id = category.category_id
WHERE category.name = 'Comedy';

#3
SELECT film.title,film.description,film.release_year from film
JOIN film_actor ON film_actor.film_id = film.film_id
WHERE film_actor.actor_id=5;

#4
SELECT customer.first_name,customer.last_name,customer.email,customer.address_id FROM city
JOIN address ON address.city_id = city.city_id
JOIN customer ON customer.address_id = address.address_id
WHERE customer.store_id=1 AND city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459;

#5
SELECT title
FROM film
WHERE rating = 'G' AND special_features = 'behind the scenes';

#6
SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id;

#7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON category.category_id= film_category.category_id
WHERE category.name = "Drama" AND film.rental_rate='2.99';

#8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name , actor.first_name, actor.last_name from film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id= film_category.category_id
WHERE concat(actor.first_name, actor.last_name)= "SANDRAKILMER" AND category.name="Action" ;