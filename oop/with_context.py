with open("filename.txt") as fh:
    for line in fh:
        #line = line.rstrip()
        line = line.lstrip()
        print(line)



fh = open("filename.txt")
for line in fh:
    print(line)

fh.close()

class MyClass(object):
    def __enter__(self):
        print('we have entered "with"')
        return self

    def __exit__(self, type, value, traceback):
        print(f"error type: {type}")
        print(f"error value: {value}")
        print(f"error traceback: {traceback}")
        print('we are leaving "with"')

    def sayhi(self):
        print(f"Hi, instance of {id(self)}")


with MyClass() as cc:
    cc.sayhi()
    #cc.sayhello()
    5/0

print("after the 'with' block")
