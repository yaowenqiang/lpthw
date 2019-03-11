# https://www.cnblogs.com/linkenpark/p/7841608.html
import redis

from redis.sentinel import Sentinel

sentinel = Sentinel([('192.168.10.10',5001),
                    ('192.168.10.11',5001),
                    ('192.168.10.12',5001),
                     ],socket_timeout=0.5)

master = sentinel.discover_master('mymaster')

print(master)

slave = sentinel.discover_master('mymaster')

print(master)


