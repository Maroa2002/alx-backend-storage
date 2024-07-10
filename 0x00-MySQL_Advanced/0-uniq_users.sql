-- creates table users

-- create the users table if it doesnt exist
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)

);
