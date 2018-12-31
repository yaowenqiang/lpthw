a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("First four: ", a[:4])
# a[:5] == a[0:5]

print("Last four: ", a[-4:])
# a[5:] == a[5:len(a)]
print("Middle ow ", a[3:-3])
print(a[:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[:5])  # ['a', 'b', 'c', 'd', 'e',]
print(a[4:])  # ['e', 'f', 'g', 'h']
print(a[-3:])  # ['f', 'g', 'h']
print(a[-0:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[0:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[2:5])  # ['c', 'd', 'e']
print(a[2:-1])  # ['c', 'd', 'e', 'f', 'g']
print(a[-3:-1])  # ['f', 'g']
