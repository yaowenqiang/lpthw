class A:
    def __init__():
        print("i am class A")


class B(A):
    def __init():
        super().__init__()
        print("i am class B")

b = B()
b.__init()

