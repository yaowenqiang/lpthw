class Date(object):
    def get_date(self):
        return "2018-12-09"

class Time(Date):
    def get_time(self):
        return '23:21:00'


dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())


class Animal(object):
    def __init__(self, name):
        self.name = name


    def eat(self, food):
        print(f"{self.name} is eating {food}." )


class Dog(Animal):
    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}!")

class Cat(Animal):
    def swatstring(self):
        print(f"{self.name} shreds the string!")

r = Dog("Rover")
f = Cat("Fluffy")

r.fetch('paper')
#r.swatstring()
f.eat('dog foot')
f.swatstring()
