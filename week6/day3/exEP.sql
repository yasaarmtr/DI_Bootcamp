select * from language;

select film.title, film.description, language.name from film
inner join language 
on film.language_id = language.language_id;

create table new_film(
new_film_id serial primary key,
new_film_name varchar(50)
)
insert into new_film(new_film_name) values
('Red notice'),('Madagascar3'),('nemo'),('scoody doo');

create table customer_review(
review_id serial primary key not null,
film_id integer,
language_id integer,
title varchar(100),
review_text text,
score integer not null,
check (score >= 0 and score < 11),
last_update timestamp default current_timestamp,
foreign key (film_id) references new_film(new_film_id),
foreign key (language_id) references language(language_id)
)
insert into customer_review(film_id, language_id,title,score,review_text)values
(1, 1, 'Madagascar3', 10, 'great film with amazing songs and animation',),
(2, 3, 'nemo', 10, 'amazing movie with great life lessons to learn from it'),
(3, 1, 'scoody doo', 10, 'great songs + amazing animation'),
(4, 1, 'Red Notice',9,'well-directed with great sense of humour');
Delete from new_film where new_film_name = 'Red notice';

ex2-------------------------------------
UPDATE film
SET language_id = 5
WHERE film_id = 25 or film_id = 100
returning film

select count(rental_id) from rental where return_date is null

select rental.rental_id,film.title, film.rental_rate
FROM rental
inner join inventory
ON inventory.inventory_id = rental.inventory_id
inner join film
ON film.film_id = inventory.film_id
WHERE rental.return_date is NULL
order by film.rental_rate DESC limit 30

select title
from film
inner join film_actor
on film.film_id = film_actor.film_id
inner join actor
on actor.actor_id = film_actor.actor_id
where description ilike '%sumo%' and first_name='Penelope' and last_name='Monroe';

SELECT title ,length ,rating from film WHERE description ilike '%documentary%' and length<60 and rating= 'R';

select film.title
from film
join inventory
on film.film_id = inventory.film_id
join rental on
inventory.inventory_id = rental.inventory_id
join customer
on rental.customer_id = customer.customer_id
where customer.first_name = 'Matthew' and rental.return_date between '2005-07-28' and '2005-08-01' and film.rental_rate > 4;

select film.title, rental.rental_id
from customer
inner join rental on customer.customer_id = rental.customer_id
inner join film on film.film_id = customer.customer_id
where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and film.rental_rate >= 4.00 and rental.return_date < '2005-08-01' and rental.return_date >= '2005-07-28'
limit 1;

select distinct film.title,film.description,film.replacement_cost
from film
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
join customer on rental.customer_id = customer.customer_id
where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and film.description ilike '%boat%' or film.title ilike '%boat%'
order by film.replacement_cost desc limit 1;