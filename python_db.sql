create database Python_Db;
create table users(
	id int unique auto_increment,
    username varchar(255),
    nombre varchar(255),
    password varchar(255),
    rol varchar(20),
    primary key (ID)
);
drop table users;