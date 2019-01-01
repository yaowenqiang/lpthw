import timeit
def testme(this_dict, key):
    return this_dict[key]
print("by index:  ", timeit.timeit(stmt="mydict['c']", setup="mydict = {'a':5, 'b':6, 'c':7}", number=1000000))
print("by get:  ", timeit.timeit(stmt="mydict.get('c')", setup="mydict = {'a':5, 'b':6, 'c':7}", number=1000000))

print("testme  ", timeit.timeit(stmt="testme(mydict, key)", setup="from __main__ import testme;mydict = {'a':5, 'b':6, 'c':7};key='c';", number=1000000))

