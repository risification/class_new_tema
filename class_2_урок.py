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
        i = 0
        for i in range(len(exp_list)):
            i = self.level - 1
            if exp_list[i] <= exp:
                print(exp)
                exp -= exp_list[i]

                self.level += 1
                self.stamina += 13
                self.agility += 13
                self.strenght += 13
                self.intellegence += 13
                self.expirience = exp


    def equip(self, item):
        items_list = ['sword', 'boots', 'heavy_armor', 'light_armor', 'bow', 'staff', 'potion']

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


person1 = Person(name='abrakadabra', race='human')
person1.lvlup(2000)
print(person1.name, person1.race, person1.speed, person1.level, person1.agility,person1.strenght,person1.stamina,person1.damage,
      person1.health,person1.intellegence,person1.armor
      )
person1.equip('potion')