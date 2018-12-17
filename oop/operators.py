var = 'hello'
var2 = 'world'
print(var + var2)

print(var.__add__(var2))

var3 = 3
var4 = 4
print(var3 + var4)
print(var3.__add__(var4))

var5 = ['a','b']
var6 = ['c','d']

print(var5.__add__(var6))

class SumList(object):
    def __init__(self, this_list):
        self.mylist = this_list
        
    
    def __add__(self, other):
        new_list = [x + y for x,y in zip(self.mylist, other.mylist)]
        
        # following 4 lines same as line above
        # new_list = []
        # zippd_list = zip(self.mylist,other.mylist)
        # for tup in zipped_list:
        #     new_list.append(tup[0] + tup[1])
        
        return SumList(new_list)
    
    def __repr__(self):
        return  str(self.mylist)
    
cc = SumList([1,2,3,4,5])
dd = SumList([100,200,300,400,500])
ee = cc + dd
print(ee)
