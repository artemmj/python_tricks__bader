class MyClass:
    def method(self):
        return 'вызван метод экземпляра', self

    @classmethod
    def classmethod(cls):
        return 'вызван метод класса', cls

    @staticmethod
    def staticmethod():
        return 'вызван статический метод', None

obj = MyClass()
print(obj.method())
print(MyClass.method(obj))
print(obj.classmethod())
print(MyClass.staticmethod())
print(obj.staticmethod())
print('===')
print(MyClass.classmethod())
print(MyClass.staticmethod())
# print(MyClass.method())

import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.radius!r}, {self.ingredients!r})'

    @classmethod
    def margherita(cls, radius):
        return cls(radius, ['моцарелла', 'помидоры'])

    @classmethod
    def prosciutto(cls, radius):
        return cls(radius, ['моцарелла', 'помидоры', 'ветчина'])

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    def area(self):
        return self.circle_area(self.radius)

Pizza(4, ['сыр', 'помидоры'])
Pizza.margherita(4)
Pizza.prosciutto(4)

p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
print(Pizza.circle_area(4))
