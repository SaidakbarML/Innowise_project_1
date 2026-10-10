DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS rooms CASCADE;

--

create table rooms  (
	id int primary key,
	name varchar(255)
);

--

create table students (
	birthday timestamp, 
	id int primary key,
	name varchar(255),
	room int references rooms(id),
	sex char(1)
);
