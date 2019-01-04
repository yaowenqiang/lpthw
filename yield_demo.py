# https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

def createGenerator():
    mylist = range(10)

    for i in mylist:
        yield i * i


mygenerator = createGenerator()

print(mygenerator)

for i in mygenerator:
    print(i)

for j in mygenerator:
    print(j)
