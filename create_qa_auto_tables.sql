CREATE schema qauto;
CREATE TABLE car_brands(
id int PRIMARY KEY AUTO_INCREMENT,
title varchar(255) NOT NULL
);
CREATE TABLE car_models(
id int PRIMARY KEY AUTO_INCREMENT,
car_brand_id int NOT NULL,
title varchar(255) NOT NULL
);
CREATE TABLE users(
id int PRIMARY KEY AUTO_INCREMENT,
firstName varchar(255) NOT NULL,
lastName varchar(255) NOT NULL,
email varchar(255) NOT NULL,
password varchar(255) NOT NULL
);
CREATE TABLE cars(
id int PRIMARY KEY AUTO_INCREMENT,
userId int NOT NULL,
carBrandId int NOT NULL,
carModelId int NOT NULL,
mileage int,
initialMilleage int
);