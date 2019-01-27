import tarfile
tar = tarfile.open('test.tar.bzip2','w|bz2')
tar.add('test.txt')
tar.close()

tar = tarfile.open('test.tar.bzip2','r|bz2')
tar.list()

