class  MyDict(dict):
    pass

dd = MyDict()

dd['a'] = 5
dd['b'] = 6


for key in dd.keys():
    print(f"{key}={dd[key]}")


