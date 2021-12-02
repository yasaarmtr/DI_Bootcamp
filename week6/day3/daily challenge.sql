create table customer(
customer_id serial primary key,
customer_uname varchar(50) not null
);

create table customer_profile(
pk_customer_id integer not null primary key,
customer_fname varchar(50) not null,
customer_lname varchar(50) not null,
CONSTRAINT fk_customer_id FOREIGN KEY (pk_customer_id) REFERENCES customer (customer_id)
);

INSERT INTO customer(customer_uname) VALUES
('varsh'),
('oce'),
('adv'),
('saad'),
('yash');

INSERT INTO customer_profile(pk_customer_id, customer_fname, customer_lname) VALUES
((SELECT customer_id FROM customer WHERE customer_uname = 'varsh'), 'varshana','gopal'),
((SELECT customer_id FROM customer WHERE customer_uname = 'oce'), 'oceance', 'lai');

SELECT customer.customer_uname, customer_profile.customer_fname, customer_profile.customer_lname as varchar
FROM customer
FULL OUTER JOIN customer_profile
ON customer.customer_id = customer_profile.pk_customer_id;

CREATE TABLE product (
product_id SERIAL,	
product_name VARCHAR(30) NOT NULL,
PRIMARY KEY (product_id)
);

INSERT INTO product(product_name) VALUES
('kit kat'),
('Toblerone'),
('Mars'),
('Snickers'),
('Twix'),
('Ferrero Rocher');

CREATE TABLE orderr (
customer_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
order_id INTEGER NOT NULL,
PRIMARY KEY (customer_id, product_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE,
FOREIGN KEY (product_id) REFERENCES product(product_id) ON UPDATE CASCADE
);

INSERT INTO orderr(customer_id, product_id, order_id) VALUES
((SELECT customer_id FROM customer  WHERE customer_uname = 'varsh'), (SELECT product_id FROM product WHERE product_name = 'Twix'), 5),
((SELECT customer_id FROM customer  WHERE customer_uname = 'oce'), (SELECT product_id FROM product WHERE product_name = 'Snickers'), 2),
((SELECT customer_id FROM customer  WHERE customer_uname = 'saad'), (SELECT product_id FROM product WHERE product_name = 'Mars'), 1);
SELECT customer_uname, product_name FROM (customer JOIN orderr ON customer.customer_id = orderr.customer_id) join product ON orderr.product_id = product.product_id;
