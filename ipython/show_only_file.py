import os
file_list = !ls
print(file_list.grep(os.path.isfile))
print(file_list.grep(os.path.isdir))
