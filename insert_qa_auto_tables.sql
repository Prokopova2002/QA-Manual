INSERT INTO qauto.car_brands (title) VALUES ("Audi R8");
INSERT INTO qauto.car_brands (title) VALUES ("BMW X5");
INSERT INTO qauto.car_brands (title) VALUES ("Ford Fiesta");
INSERT INTO qauto.car_brands (title) VALUES ("Porsche 911");
INSERT INTO qauto.car_brands (title) VALUES ("Fiat Ducato");
INSERT INTO qauto.car_models (car_brand_id, title) VALUES (12, "Audi R8");
INSERT INTO qauto.car_models (car_brand_id, title) VALUES (13, "BMW X5");
INSERT INTO qauto.car_models (car_brand_id, title) VALUES (14, "Ford Fiesta");
INSERT INTO qauto.car_models (car_brand_id, title) VALUES (15, "Porsche 911");
INSERT INTO qauto.car_models (car_brand_id, title) VALUES (16, "Fiat Ducato");
INSERT INTO qauto.cars (userId, carBrandId, carModelId, mileage, initialMilleage) VALUES (111, 12, 21, 1234, 1200);
INSERT INTO qauto.cars (userId, carBrandId, carModelId, mileage, initialMilleage) VALUES (222, 13, 31, 1235, 1201);
INSERT INTO qauto.cars (userId, carBrandId, carModelId, mileage, initialMilleage) VALUES (333, 14, 41, 1236, 1202);
INSERT INTO qauto.cars (userId, carBrandId, carModelId, mileage, initialMilleage) VALUES (444, 15, 51, 1237, 1203);
INSERT INTO qauto.cars (userId, carBrandId, carModelId, mileage, initialMilleage) VALUES (555, 16, 61, 1238, 1204);
INSERT INTO qauto.users (firstName, lastName, email, password) VALUES ("Ivan", "Petrenko", "ipetrenko92@gmail.com", "mypassword1234");
INSERT INTO qauto.users (firstName, lastName, email, password) VALUES ("Petro", "Shevchenko", "pshevchenko93@gmail.com", "mypassword1235");
INSERT INTO qauto.users (firstName, lastName, email, password) VALUES ("Taras", "Kovalenko", "tkovalenko94@gmail.com", "mypassword1236");
INSERT INTO qauto.users (firstName, lastName, email, password) VALUES ("Katerina", "Koval", "kkoval95@gmail.com", "mypassword1237");
INSERT INTO qauto.users (firstName, lastName, email, password) VALUES ("Olya", "Ivanenko", "oivanenko96@gmail.com", "mypassword1238");
ALTER TABLE cars ADD FOREIGN KEY (userId) REFERENCES users(id);
ALTER TABLE cars ADD FOREIGN KEY (carBrandId) REFERENCES car_brands(id);
ALTER TABLE cars ADD FOREIGN KEY (carModelId) REFERENCES car_models(id);