import pickle
#mylist = ['a','b','c','d']
#with open('datafile.txt','wb+') as fh:
#    pickle.dump(mylist, fh)


with open('datafile.txt', 'rb') as fh:
    unpacklist = pickle.load(fh)
    print(unpacklist)
