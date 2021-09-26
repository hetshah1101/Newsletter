drop table if exists users;
	create table users (
		email text primary key not null,
		name text not null
);