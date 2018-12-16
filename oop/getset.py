import abc
class GetSetParent():
    __metaclass__ = abc.ABCMeta
    def __init__(self, value):
        self.val = 0
    
    def set_val(self, value):
        self.val = value
    
    def get_val(self):
        return self.val
    
    @abc.abstractmethod
    def showdoc(self):
        return
    

class GetSetInt(GetSetParent):
    def set_val(self, value=0):
        if not isinstance(value, int):
            value = 0
    
        super(GetSetInt, self).set_val(value)
        #super().set_val(value)
    
    def showdoc(self):
        print(f"GetSetInt object ({id(self)}, only accepts integer values")
    

class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]
    
    def get_val(self):
        return self.vallist[-1]
    
    def set_val(self, val):
        self.vallist.append(val)
    
    def showdoc(self):
        print(f"GetSetList object, len {len(self.vallist)}, stores history of values set")

int_val = GetSetInt(1)
int_val.set_val(100)
int_val.showdoc()
print(int_val.get_val())
int_val.set_val('abc')
print(int_val.get_val())

list_val = GetSetList()
list_val.showdoc()
