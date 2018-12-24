import json

with open("backup_config.json") as fh:
    conf = json.load(fh)

print(conf)
print(type(conf))

conf['newKey'] = 5.00005

with open("backup_config.json", 'w')  as fh:
    #json.dump(conf, fh)
    json.dump(conf, fh, indent=4, separators=(',',': '))


x = json.dumps({'a':[1,2,3],'c':[7,8,9], 'b':[4,5,6]})
print(x)


myobject = json.loads(x)
for key in myobject:
    print(key)
    for item in myobject[key]:
        print(f"    {item}")



