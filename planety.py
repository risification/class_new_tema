class Planet:

    def __init__(self,name,position,size):
        self.name = name
        self.position = position
        self.size = size
        self.humanity = False
        self.monsters = True
        self.water = False
        self.oxygen = False
        self.sun = True #Вращается ли вокруг солнца какого нибудь
        self.temp = -273
        self.gasoline = True

    def description(self):
        print(f'Имя: {self.name}, местонахождение: {self.position}, размер: {self.size}, человечество: {self.humanity}, '
              f'монстры: {self.monsters}, вода: {self.water}, кислород: {self.oxygen}, вокруг солнца: {self.sun}, температура: {self.temp}, '
              f'газы: {self.gasoline}')

planet1 = Planet('Pluton','solar system',20)
planet1.description()

