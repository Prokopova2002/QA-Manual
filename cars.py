import random
class Car:
    def __init__(self, model, color, economy, mileage=0, fuel=100):
        self.mileage = mileage
        self.model = model
        self.economy = economy
        self.fuel = fuel
        self.color = color
    def drive(self, distance):
        fuel_needed = distance / self.economy
        if fuel_needed > self.fuel: print("Error: not enough fuel")
        else:
            self.mileage += distance
            self.fuel -= fuel_needed
    def distance_left(self):
        return f"The car {self.model} can drive {self.fuel * self.economy} km с taking into account the current fuel supply"
    def fuel_up(self):
        self.fuel += 20
models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
cars = []
for _ in range(10):
    model = random.choice(models)
    color = random.choice(["green", "red", "black", "pink", "blue"])
    economy = random.randint(5, 15)
    car = Car(model, color, economy)
    cars.append(car)
for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)
max_fuel_car = max(cars, key=lambda x: x.fuel)
print(f"Car with the most fuel: {max_fuel_car.model}, {max_fuel_car.color}, mileage: {max_fuel_car.mileage} km, remaining fuel: {max_fuel_car.fuel}%")