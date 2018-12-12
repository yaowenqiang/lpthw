class MyClass(object):
    count  = 0

    def __init__(self,val):
        self.val = self.filterInt(val)
        MyClass.count +=1

    def get_val(self):
        return self.val

    def get_count(self):
        return MyClass.count

    @classmethod
    def get_class_count(cls):
        return cls.count

    @staticmethod
    def filterInt(value):
        if not isinstance(value,int):
            return 0
        else:
            return value

a = MyClass(1)
b = MyClass(2)
c = MyClass(3)

for obj in (a,b,c):
    print(f"var of obj: {obj.get_val()}")
    print(f"count: {obj.get_count()}")
    print(f"count: {obj.get_class_count()}")

print(MyClass.get_class_count())
print(MyClass.filterInt('abc'))
print(MyClass.filterInt(1.111))
print(MyClass.filterInt(1111))
