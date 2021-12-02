create table orders(
	order_id serial primary key,
	order_name varchar(250) not null
);

create table items (
item_id int primary key,
item_name varchar(50),
item_quantity int,
item_price int,
order_id int,
foreign key (order_id) references orders (order_id)
);

insert into orders (order_id, order_name)
values
(1,'Varsh'),
(2,'Oce'),
(3,'Yasaaar');

insert into items
values
(1, 'shirt', 2, 700, 1),
(2, 'Sweater', 3, 900, 2),
(3, 'Shoe', 1, 1500, 3),
(4, 'Trouser', 6, 1000, 2);

create or replace function total_price(id int)
returns int as $calculation$
begin
return (select sum(item_price * item_quantity) from items where order_id = id);
end;
$calculation$ language plpgsql;

select * from total_price (1)