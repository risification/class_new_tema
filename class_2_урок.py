class Person:

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.stamina = 100
        self.agility = 100
        self.strenght = 100
        self.health = 100
        self.intellegence = 100
        self.level = 1
        self.armor = 20
        self.speed = 20
        self.damage = 40
        self.expirience = 0

    def lvlup(self, exp):
        exp_list = [20, 30, 40, 100, 500, 1000]
        for i in range(len(exp_list)):
            i = self.level - 1
            if exp_list[i] <= exp:
                exp -= exp_list[i]

                self.level += 1
                self.stamina += 13
                self.agility += 13
                self.strenght += 13
                self.intellegence += 13
                self.expirience = exp

    def equip(self, item):

        if item == 'sword':
            self.damage += 50
            self.strenght += 40
        elif item == 'boots':
            self.speed += 10
        elif item == 'heavy_armor':
            self.armor += 50
            self.stamina -= 50
            self.speed -= 20
            self.health += 500
            self.strenght += 50
        elif item == 'light_armor':
            self.armor += 10
            self.stamina += 50
            self.health += 200
            self.strenght += 20
            self.agility += 10

        elif item == 'bow':
            self.agility += 40
            self.damage += 50

        elif item == 'staff':
            self.intellegence += 100
            self.health += 70

        elif item == 'potion':
            self.stamina += 2
            self.agility += 2
            self.strenght += 2
            self.health += 2
            self.intellegence += 2
            self.armor += 2
            self.speed += 2
            self.damage += 2


class Warrior(Person):
    def __init__(self, name, race='warrior'):
        super().__init__(name, race)
        self.stamina = 130
        self.agility = 80
        self.strenght = 160
        self.health = 160
        self.intellegence = 40
        self.speed = 30
        self.damage = 50

    def lvlup(self, exp):
        exp_list = [20, 30, 40, 100, 500, 1000]
        for i in range(len(exp_list)):
            i = self.level - 1
            if exp_list[i] <= exp:
                exp -= exp_list[i]
                self.level += 1
                self.stamina += 10
                self.agility += 6
                self.damage += 10
                self.armor += 18
                self.strenght += 21
                self.intellegence += 5
                self.health += 23
                self.expirience = exp

    def equip(self, item):
        if item == 'The Leveller':
            self.damage += 20
            self.speed += 5
            self.strenght += 10

        elif item == 'Mind Breaker':
            self.damage += 25
            self.speed += 15
            self.health += 10
            self.strenght += 7

        elif item == 'Spell Prism':
            self.stamina += 12
            self.agility += 12
            self.strenght += 12
            self.health += 12
            self.intellegence += 12
            self.armor += 12
            self.speed += 12
            self.damage += 12

        elif item == 'Cloak of Flames':
            self.armor += 50
            self.health += 25
            self.speed -= 10

        elif item == 'amulet_health':
            self.health += 100

        elif item == 'books exp':
            self.expirience += 200

        elif item == 'heavy_armor':
            self.armor += 150
            self.speed -= 20
            self.health -= 30


class Tank(Person):
    def __init__(self, name, race='tank'):
        super().__init__(name, race)
        self.stamina = 30
        self.agility = 37
        self.strenght = 85
        self.health = 350
        self.intellegence = 50
        self.armor = 120
        self.speed = 30
        self.damage = 40

    def lvlup(self, exp):
        exp_list = [20, 30, 40, 100, 500, 1000]
        for i in range(len(exp_list)):
            i = self.level - 1
            if exp_list[i] <= exp:
                exp -= exp_list[i]
                self.level += 1
                self.stamina += 10
                self.agility += 9
                self.damage += 10
                self.strenght += 14
                self.intellegence += 3
                self.health += 50
                self.expirience = exp

    def equip(self, item):
        if item == 'heavy_armor':
            self.armor += 100
            self.speed -= 5
            self.agility -= 25
            self.health += 20
        elif item == 'dubinka':
            self.damage += 30
            self.strenght += 20
            self.speed += 10
        elif item == 'boots':
            self.speed += 20
            self.stamina += 20
            self.armor += 10
            self.agility += 15
        elif item == 'books_lvlup':
            self.level += 1


person1 = Person(name='abrakadabra', race='human')
warrior1 = Warrior(name='nalsurun', race='warrior')
tank1 = Tank(name='grok', race='tank')
print(tank1.name, tank1.race, 'speed', tank1.speed, 'level', tank1.level, 'agility', tank1.agility,
      'strenght ', tank1.strenght,
      'stamina', tank1.stamina,
      'damage', tank1.damage,
      'health', tank1.health, 'intellegence', tank1.intellegence, 'armor', tank1.armor, 'expririence', tank1.expirience
      )
print(person1.name, person1.race, 'speed', person1.speed, 'level', person1.level, 'agility', person1.agility,
      'strenght ', person1.strenght,
      'stamina', person1.stamina,
      'damage', person1.damage,
      'health', person1.health, 'intellegence', person1.intellegence, 'armor', person1.armor, 'expririence',
      person1.expirience
      )
print(warrior1.name, warrior1.race, 'speed', warrior1.speed, 'level', warrior1.level, 'agility', warrior1.agility,
      'strenght ', warrior1.strenght,
      'stamina', warrior1.stamina,
      'damage', warrior1.damage,
      'health', warrior1.health, 'intellegence', warrior1.intellegence, 'armor', warrior1.armor, 'expririence',
      warrior1.expirience,
      '\n')

print(tank1.name, tank1.race, 'speed', tank1.speed, 'level', tank1.level, 'agility', tank1.agility,
      'strenght ', tank1.strenght,
      'stamina', tank1.stamina,
      'damage', tank1.damage,
      'health', tank1.health, 'intellegence', tank1.intellegence, 'armor', tank1.armor, 'expririence', tank1.expirience
      )
print(person1.name, person1.race, 'speed', person1.speed, 'level', person1.level, 'agility', person1.agility,
      'strenght ', person1.strenght,
      'stamina', person1.stamina,
      'damage', person1.damage,
      'health', person1.health, 'intellegence', person1.intellegence, 'armor', person1.armor, 'expririence',
      person1.expirience
      )
print(warrior1.name, warrior1.race, 'speed', warrior1.speed, 'level', warrior1.level, 'agility', warrior1.agility,
      'strenght ', warrior1.strenght,
      'stamina', warrior1.stamina,
      'damage', warrior1.damage,
      'health', warrior1.health, 'intellegence', warrior1.intellegence, 'armor', warrior1.armor, 'expririence',
      warrior1.expirience
      )
