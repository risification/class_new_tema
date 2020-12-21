class Car:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
        self.fuel = 100
        self.run = 0
        self.color = 'orange'
        self.no2 = False

    def move(self, distance):
        if distance > 0:
            result = 20 / 100
            result = distance * result
            self.fuel -= result
            self.run += distance


car = Car('tesla', 'XS', 90000)
print(car.run)
car.move(240)
print(car.run)
print(car.fuel)
