class YourClass(object):
    classy = 10 # class attributes

    def set_val(self):
        self.insty = 100 instance attributes

dd = YourClass()
#print(dd.insty) error
dd.set_val()
print(dd.classy)
print(dd.insty)

dd.classy = "my Classy Value"
print(dd.classy)
del dd.classy
print(dd.classy)
