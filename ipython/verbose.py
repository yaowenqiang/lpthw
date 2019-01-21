import os
path = '/tmp'

def enumeratepaths(path=path):
    '''returns the path to all the files in a directory recurisvely'''
    path_collection = []

    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)


    return path_collection



def enumeratefiles(path=path):
    file_collections = []
    '''returns all the files in a directory as a list'''
    for dirpath, dirnames, files  in os.walk(path):
        for file in files:
            file_collections.append(file)

    return file_collections

def enumeratedirs(path=path):
    dir_collections = []
    '''returns all the directories in a directory as a list'''
    for dirpath, dirnames, files in os.walk(path):
        for d in dirnames:
            dir_collections.append(d)
    

    return dir_collections
    

if __name__ == '__main__':
    print("\Recursive listing  fuul path of all files in a dir:")
    for p in enumeratepaths(path):
        print(p)

    print("\Listing of all files in a dir:")
    for f in enumeratefiles(path):
        print(f)

    print("listing of all directories in a dir:")
    for d in enumeratedirs(path):
        print(d)
