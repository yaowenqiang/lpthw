import pdb

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mysum = 0

for val in values:
    mysum += val
    pdb.set_trace()



print(mysum)
