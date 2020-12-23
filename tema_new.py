class Car:

    def __init__(self, name, model, price, speed):
        self.name = name
        self.model = model
        self.price = price
        self.state = 100
        self.fuel = 100
        self.run = 0
        self.color = 'orange'
        self.no2 = False
        self.broken = False
        self.speed = speed

    def move(self, distance):
        if distance > 0:
            result = 20 / 100
            result = distance * result
            self.fuel -= result
            self.run += distance

    def broke(self, item):
        if item == 'stolb':
            self.state = self.state - 20
            self.price -= 10000
        elif item == 'car':
            self.state = self.state - 40
            self.price -= 20000
        elif item == 'human':
            self.state = self.state - 10

    def check_broken(self):
        if self.state < 50:
            self.broken = True

    def build(self):
        self.no2 = True
        self.speed += 30
        self.price += 15000


car = Car('tesla', 'XS', 90000, 390)
car.broke('stolb')
car.broke('car')
car.check_broken()
car.build()
print(car.broken, car.state, car.price, car.speed, car.fuel)
