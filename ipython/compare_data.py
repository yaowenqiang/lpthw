import filecmp
import os
filecmp.cmp('file1','file2')
filecmp.dircmp('cir1','dir2').same_files
filecmp.dircmp('cir1','dir2').report()

dira = set(os.listdir('/tmp'))
dirb = set(os.listdir('/home/vagrant/'))

dira - dirb
dirb - dira
