class Parent:
    def altered(self):
        print("PARENT altered!")


class Child(Parent):
    def altered(self):
        print("CHILD before PARENT altered!")
        super(Child,self).altered()
        print("CHILD after PARENT altered!")

dad = Parent()
sun = Child()

dad.altered()
sun.altered()
