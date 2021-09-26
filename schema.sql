drop table if exists users;
	create table users (
		email text primary key not null unique,
		name text not null
);