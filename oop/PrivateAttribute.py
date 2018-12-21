class PrivateAttribute(object):
    instance_count = 0

    __mangled_name = "No privacy!"

    def __init__(self, value):
        self._attrval = value
        PrivateAttribute.instance_count += 1

    @property
    def var(self):
        print('getting the "var" attribute')
        return self._attrval


    
    @var.setter
    def var(self, value):
        print("setting the 'var' attribute")
        self._attrval = value

    @var.deleter
    def var(self):
        print("deleting the 'var' attribute")
        self._attrval = None

cc = PrivateAttribute(10000);
print(cc._attrval)
cc.var = 100
print(cc.var)
del cc.var
print(cc.var)
#print(cc.__mangled_name)
print(cc._PrivateAttribute__mangled_name)
