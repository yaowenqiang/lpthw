import yaml

mydict = {'a':1, 'b':2, 'c':3}
mylist = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4)

loaded_yaml = yaml.dump(mydict, default_flow_style=False)
print(loaded_yaml)
print(yaml.dump(mylist, default_flow_style=False))
print(yaml.dump(mytuple, default_flow_style=False))
print(yaml.dump(mytuple))

myobj = (
    [1,2,3,4,5],
    {'a':1,'b':2,'c':3,'d':4},
    [
        {'x':98,'y':99,'z':100},
        3,
        4
    ],
    {
        'a':[1,2,3,4],'b':[5,6,7,8],'c':[9,10,11,12]
    }
)

print(yaml.dump(myobj, default_flow_style=False))
