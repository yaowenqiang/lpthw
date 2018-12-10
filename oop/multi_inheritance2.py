class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass

class C(A):
    def dothis(self):
        print("doing this in C")

class D(B,C):
    pass

d_inst = D()
d_inst.dothis()

print(D.mro())
