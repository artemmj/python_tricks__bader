from collections import namedtuple

Car = namedtuple('Авто', [
    'цвет',
    'пробег'
])

my_car = Car('красный', 999.99)
print(my_car)
print(*my_car)
print(my_car.цвет)
print(my_car.пробег)

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.цвет == 'красный':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('красный', 1234)
print(c.hexcolor())


ElectricCar = namedtuple('ЭлектрическоеАвто', Car._fields + ('заряд',))
ecar = ElectricCar('красный', 1234, 45.0)
print(ecar)
ecar._replace(цвет='XXXXX')
print(ecar._asdict())

import json
json.dumps(ecar._asdict(), ensure_ascii=False)  # False для кириллицы

Car._make(['красный', 999])
