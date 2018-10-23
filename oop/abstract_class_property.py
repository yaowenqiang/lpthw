from abc import ABC, abstractmethod


class C(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        pass

    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):
        pass


class D(C):
    @property
    def my_abstract_property(self):
        return self.val

    @my_abstract_property.setter
    def my_abstract_property(self, val):
        if not isinstance(val, int):
            raise ValueError("val must be integer!")

        self.val = val


C.register(tuple)

d = D()
d.my_abstract_property = 1000
print(d.my_abstract_property)

d.my_abstract_property = "abc"
print(d.my_abstract_property)

print(isinstance(d, D))
print(isinstance(d, C))

print(issubclass(tuple, C))
print(issubclass(D, C))
print(isinstance((), C))

# print(dir(C))
