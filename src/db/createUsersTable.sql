CREATE DATABASE users;

CREATE TABLE users (
      UserId int NOT NULL AUTO_INCREMENT,
      FirstName text,
      LastName text,
      Adres text,
      PhoneNumber varchar(12),
      EmailAdress text,
      PRIMARY KEY (UserId)
   );

INSERT INTO Users (
		FirstName, 
		LastName, 
		Adres, 
		PhoneNumber, 
		EmailAdress
	) VALUES (
		'Adam', 
		'Pawlak', 
		'Moon', 
		123123123, 
		'kox123@essa.pl'
	);