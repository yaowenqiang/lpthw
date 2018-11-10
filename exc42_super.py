class A:
    def __init__(self):
        print("i am class A")
        pass


class B(A):
    def __init__(self):
        super().__init__()
        print("i am class B")

b = B()

