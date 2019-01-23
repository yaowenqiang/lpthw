import hashlib

def create_checksum(path):
    '''
    reads in file, creates checksum of files line by line
    '''
    fp = open(path,'rb')

    checksum = hashlib.md5()


    while True:
        buffer = fp.read(8192)

        if not buffer: break

        checksum.update(buffer)


    fp.close()

    #  checksum = checksum.digest()
    checksum = checksum.hexdigest()

    return checksum




print(create_checksum('traceback.txt'))
