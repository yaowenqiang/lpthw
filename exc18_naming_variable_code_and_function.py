def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1},arg2: {arg2}")

def print_tow_again(arg1,arg2):
    print(f"arg1: {arg1},arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing'.")

print_two(1,2)
print_tow_again(3,4)
print_one(5)
print_none()
