# https://www.cnblogs.com/linkenpark/p/7841608.html
import redis

from redis.sentinel import Sentinel

sentinel = Sentinel([('localhost',26376),
                    ('localhost',26377),
                    ('localhost',26378),
                    ('localhost',26379),
                     ],socket_timeout=0.5)

master = sentinel.discover_master('mymaster')

print(master)

slave = sentinel.discover_master('mymaster')

print(master)


