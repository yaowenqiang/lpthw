class  MyDict(dict):
    def __setitem__(self, key, val):
        print("setting a key and value!")
        # self[key] = val
        dict.__setitem__(self, key, val)

dd = MyDict()

dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print(f"{key}={dd[key]}")


