import yaml
import json

class MyClass(object):
    classvar = 10

    def __init__(self, val):
        self.val = val

    def increment(self):
        self.val +=1

x = MyClass(1)
x.increment()
x.increment()
# with open('oop/app.yaml') as fh:
    # config = yaml.load(fh)

with open('oop/app.yaml','w') as fh:
    yaml.dump(x, fh)

with open('oop/app.yaml') as fh:
    config = yaml.load(fh)

print(config)
print(config.val)
#print(json.dumps(config, indent=4 ,separators=(',',':')))
