CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    bio TEXT,
    country VARCHAR(3)
);
insert into users (email, bio, country)
values (
	'hello@world.com',
    'i love kalabina',
    'MA'
);
select * from users;