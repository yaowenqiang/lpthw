from redlock import RedLock
addrs = [
    {
        'host':'localhost',
        'port': 6379,
        'db':0 
     },
    {
        'host':'localhost',
        'port': 6479,
        'db':0 
     },
    {
        'host':'localhost',
        'port': 6579,
        'db':0 
     },
    {
        'host':'localhost',
        'port': 6679,
        'db':0 
     }
]

lock_key = 'user-lck-laoqian'

lock = RedLock(lock_key)

lock.acquire()

print("i am locked")

lock.release()

