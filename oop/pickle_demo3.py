import pickle
class MyClass():
    def __init__(self, init_val):
        self.val = init_val
    def increment(self):
        self.val += 1

cc = MyClass(1)
cc.increment()
cc.increment()
with open('datafile.txt','wb+') as fh:
    pickle.dump(cc, fh)
    
with open('datafile.txt','rb') as fh:
    unpacked_cc = pickle.load(fh)

print(unpacked_cc)
print(unpacked_cc.val)
