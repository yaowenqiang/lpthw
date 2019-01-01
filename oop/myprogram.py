import sys
def doubleit(x):
    if not  isinstance(x, (int, float)):
        raise TypeError
    var = x * 2
    return var

def doublelines(filename):
    with open(filename, 'r') as fh:
        newlist = [str(doubleit(int(val))) for val in fh]
    
    with open(filename, 'w') as fh:
        fh.write("\n".join(newlist))

if __name__ == '__main__':
    input_val = int(sys.argv[1])
    doubled_val = doubleit(input_val)

    doublelines('testnums_template.txt')

    print(f"The value of {input_val} is {doubled_val}")
