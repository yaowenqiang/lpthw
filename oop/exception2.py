class MyClass():
    @staticmethod
    def make_error():
        print("entering make_error()")
        5/0
        print("    leaving make_error()")

    def do_something(self):
        print("entering do_shometing()")
        self.make_error()
        print("    leaving do_something()")


def some_util_func():
    print("entering some_util_func()")
    cc = MyClass()
    cc.do_something()
    print("    leaving some_util_func()")


def some_major_func():
    print("entering some_major_func()")
    some_util_func()
    print("    leaving some_major_func()")
def main():
    print("entering main()")
    some_major_func()
    print("    leaving main()")
try:
    main()
except ZeroDivisionError:
    print("OOPS!")
