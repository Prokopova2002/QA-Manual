SELECT * FROM hillel_qauto.user_profiles WHERE name LIKE "%am";
SELECT * FROM hillel_qauto.user_profiles WHERE name LIKE "am%";
SELECT * FROM hillel_qauto.user_profiles WHERE name LIKE "%am%";
SELECT MAX(totalCost) FROM hillel_qauto.car_brands INNER JOIN hillel_qauto.expenses ON hillel_qauto.car_brands.title LIKE "Audi" = hillel_qauto.expenses.totalCost;
SELECT cars.carBrandId AS car_id, COUNT(carModelId) AS count_models FROM hillel_qauto.car_brands LEFT JOIN hillel_qauto.cars ON car_brands.id = cars.carBrandId LEFT JOIN hillel_qauto.car_models ON cars.carModelId = car_models.id WHERE car_brands.title IN ('Audi', 'BMW') GROUP BY car_brands.id; 
SELECT car_models.title AS car_model, car_brands.title AS car_brand, COUNT(users.id) AS user_count FROM hillel_qauto.cars JOIN hillel_qauto.car_models ON cars.carModelId = car_models.id JOIN hillel_qauto.car_brands ON cars.userId = car_brands.id JOIN hillel_qauto.users ON userId = users.id GROUP BY car_models.title, car_brands.title; 
SELECT user_profiles.name AS user_name FROM hillel_qauto.cars JOIN hillel_qauto.user_profiles ON cars.userId = user_profiles.id;
