-- This script creates a table users with 3 columns
CREATE TABLE IF NOT EXISTS `users`(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id));
