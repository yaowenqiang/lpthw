class Instancecounter(object):
    count = 0
    def __init__(self, val):
        self.val = val
        Instancecounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return Instancecounter.count

a = Instancecounter(5)
print(a.get_count())
b = Instancecounter(15)
print(b.get_count())
c = Instancecounter(25)
print(c.get_count())

for obj in (a,b,c):
    print(f"val of obj {obj.get_val()}")
    print(f"ount  {obj.get_count()}")

