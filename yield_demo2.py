# https://www.cnblogs.com/zhenlingcn/p/8337788.html

def fun():
    for i in range(10):
        x = yield i
        print("good", x)

if __name__ == '__main__':
    a = fun()
    b = a
    a.__next__()

    x = a.send(5)

    print(x)

    for i in b:
        print(i)
