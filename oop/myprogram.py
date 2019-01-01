import sys
def doubleit(x):
    if not  isinstance(x, (int, float)):
        raise TypeError
        
    var = x * 2
    return var

if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print(f"The value of {input_val} is {doubled_val}")
