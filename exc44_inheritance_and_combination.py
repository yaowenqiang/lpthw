class Parent:
    def altered(self):
        print("PARENT altered!")


class Child(Parent):
    def altered(self):
        print("CHILD before PARENT altered!")
        super(Child, self).altered()
        print("CHILD after PARENT altered!")

dad = Parent()
sun = Child()

dad.altered()
sun.altered()


class Other():
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child():
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print("CHILD,BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD,AFTER OTHER altered()")

son1 = Child()
son1.override()
son1.implicit()
son1.altered()
