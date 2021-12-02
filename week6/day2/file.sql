-- SELECT * FROM items order by item_price ASC
-- SELECT * FROM items where item_price>= 80 order by item_price DESC
-- SELECT first_name, last_name FROM customers order by id ASC limit 3
-- SELECT last_name FROM customers order by last_name DESC

-- create table purchases(
-- purchase_id serial,
-- customer_id integer,
-- items_id integer,
-- primary key (purchase_id),
-- foreign key (customer_id) references customers(id),
-- foreign key (items_id) references items(id)
-- )
-- insert into purchases(customer_id, item_id)
-- values (1,) ********************

-- insert into purchases(customer_id, items_id) values
-- (4,1),(5,2);

-- select * from purchases/ not useful

select * from customers values (purchase_id);
select * from customers values (purchase_id=4);




select * from customers;
select first_name, last_name from customers as full_name;
select distinct create_date from customers;
select * from customers order by first_name desc;
select film_id, title, description, release_year, rental_rate from film order by rental_rate;
select address, phone from address where district = ‘Texas’;
select * from film where film_id = 15 or film_id = 150;
select film_id, title, description, length, rental_rate from film where title = ‘Titanic’;
select title from film; select film_id, title, description, length, rental_rate from film where title ilike ‘ti%’;
select title , rental_rate from film order by rental_rate ASC limit 15;
select title , rental_rate from film order by rental_rate offset 15 rows fetch next 10 rows only;
select customer.customer_id, customer.first_name, payment.amount, payment.payment_date from customer inner join payment on payment.customer_id = customer.customer_id order by customer_id; select film.film_id, film.title, inventory.film_id from film inner join inventory on inventory.film_id = film.film_id;
select title, film_id from film where film_id not in (select film_id from inventory);
select city.city, country.country_id, country.country from city inner join country on country.country_id = city.country_id;
select customer.first_name, customer.last_name, payment.customer_id, payment.amount, payment.payment_date, payment.staff_id from customer left join payment on payment.customer_id = customer.customer_id order by payment.staff_id;
