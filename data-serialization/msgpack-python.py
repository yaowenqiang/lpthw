# pip install msgpack-python

import msgpack
v = msgpack.packb([1,2,3],use_bin_type=True)
print(v)
msgpack.unpackb(v,raw=False)

