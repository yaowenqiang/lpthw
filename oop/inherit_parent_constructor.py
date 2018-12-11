import random
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eating  {food}")


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)

        self.bread = random.choice(["Shih Tzu","Beagle","Mutt"])


    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")


d = Dog("dogname")

print(d.name)
print(d.bread)
