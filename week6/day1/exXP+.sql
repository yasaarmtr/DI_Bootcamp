create table students(
id serial primary key,
	last_name varchar(50),
	first_name varchar(50),
	birth_date date not null
)
insert into students(last_name,first_name,birth_date) values
('Benichou','Marc',02/11/1998),('Cohen','Yoan',03/12/2010),('Benichou','Lea',27/07/1987),('Dux','Amelia',07/04/1996),('Grez','David	',14/06/2003
),('Simpson	','Omer	',03/10/1980);