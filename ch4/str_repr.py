class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # def __str__(self):
    #     return f'{self.color} car (__str__)'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r}) (__repr__)')

car = Car('red', 99999)
print(car)
print(repr(car))
print([car])
