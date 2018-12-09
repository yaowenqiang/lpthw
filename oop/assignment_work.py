from assignment import MaxSizeList

a = MaxSizeList(3)
 
a.push('i ')
a.push('am ')
a.push("ok ")
a.push("thanks")
 
print(a.get_list())

b = MaxSizeList(1)
b.push('hey')
b.push('hi')
b.push("let's ")
b.push("go")
print(b.get_list())
