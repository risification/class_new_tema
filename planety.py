class Planet:

    def __init__(self, name, position, size):
        self.name = name
        self.position = position
        self.size = size
        self.humanity = False
        self.monsters = True
        self.water = False
        self.oxygen = True
        self.sun = True  # Вращается ли вокруг солнца какого нибудь
        self.temp = 10
        self.gasoline = True
        self.meteor = 19
        self.destroyed = False

    def oxygen_check(self):
        if self.name == 'zemly':
            self.oxygen = True
            return self.oxygen
        else:
            self.oxygen = False
            return self.oxygen

    def have_people(self):
        if self.name == 'zemly':
            self.humanity = True
            return self.humanity
        else:
            self.humanity = False
            return self.humanity

    def have_monster(self):
        if self.position != 'zemly':
            self.monsters = True
            return self.monsters
        else:
            self.monsters = True
            return self.monsters

    def check_which_system(self):
        if self.position == 'solar system':
            self.sun = True
            return self.sun
        else:
            self.sun = False
            return self.sun

    def water_in_planet(self):
        if self.position == 'solar system':
            self.water = True
            return self.water
        else:
            self.water = False
            return self.water

    def meteor_vs_planet(self):
        if self.meteor >= self.size:
            self.destroyed = True
            return self.destroyed
        else:
            self.destroyed = False
            return self.destroyed

    def description(self):
        print(
            f'Имя: {self.name}, местонахождение: {self.position}, размер: {self.size}, человечество: {self.humanity}, '
            f'монстры: {self.monsters}, вода: {self.water}, кислород: {self.oxygen}, вокруг солнца: {self.sun},температура: {self.temp}, '
            f'газы: {self.gasoline}, метеорид:{self.meteor}')


planet1 = Planet('zemly', 'solar system', 20)
planet1.water_in_planet()
planet1.check_which_system()
planet1.have_monster()
planet1.oxygen_check()
print(planet1.meteor_vs_planet())
planet1.description()
