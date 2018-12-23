import sys
mydict = {'a':1,'b':2,'c':3,'d':4}
try:
    key = input("please input a key: ")
    print(f"the value for{key} is {mydict[key]}")
except KeyError:
    print("trapped error")
    print(f"the key {key} does not exist")

print("program continues...")

try:
    arg = sys.argv[1]
    num = int(arg)
except (IndexError, ValueError):
    exit("please inter an integer on the command line")

print("thinks for the int")
