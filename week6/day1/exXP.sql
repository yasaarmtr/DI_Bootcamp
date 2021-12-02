create table items(
id serial primary key,
	item_name varchar (50),
	item_price numeric
)
insert into items(item_name,item_price) values
('small desk', 100),('large desk', 300),('fan',80)

create table customers(
id serial primary key,
	first_name varchar(50),
	last_name varchar(50)
)
insert into customers(first_name, last_name) values
('Grey','Jones'),('Sandra','Jones'),('Scott','Scott'),('Trevor','Green'),('Melanie','Johnson')

select * from items;
select * from items where item_price > 80;
select * from items where item_price < 300;
select * from customers where last_name ilike 'Smith';
select * from customers where last_name ilike 'jones';
select * from customers where last_name not ilike 'scott';
