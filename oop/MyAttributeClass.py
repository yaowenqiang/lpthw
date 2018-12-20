class MyAttribute:
    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value


a = MyAttribute()
b = MyAttribute()

a.set_val(100)
b.set_val(1000)

print(a.get_val())
print(b.get_val())
