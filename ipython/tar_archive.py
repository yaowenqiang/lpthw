import tarfile
import os
f = open('filename', 'wb')

statement = 'some text'

for x in xrange(20000):
    x +=1
    f.write("%s\n"  %statement)


tar = tarfile.open('test.tar', 'w')

tar.add('test.txt')

tar.close()


tar2 = tarfile.open('tmp.tar','w')


for root, dir, files in os.walk('/tmp'):
    for file in files:
        fullpath = os.path.join(root,file)
        tar2.addfile(fullpath)


tar2.close()
