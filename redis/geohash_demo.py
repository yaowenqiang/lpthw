# -*- coding: utf-8 -*-
import redis
client = redis.StrictRedis(host='localhost', port=637)
client.delete('company')
# 添加元素
client.geoadd('company', 116.48105, 39.996794, 'juejin')
client.geoadd('company', 116.514203, 39.905409, 'ireader')
client.geoadd('company', 116.489033, 40.007669, 'meituan')
client.geoadd('company', 116.562108, 39.787602, 'jd', 116.334255, 40.027400, 'xiaomei')

# 计算元素距离
print(client.geodist('company', 'juejin', 'ireader', 'km'))
print(client.geodist('company', 'juejin', 'meituan', 'km'))
print(client.geodist('company', 'juejin', 'jd', 'km'))
print(client.geodist('company', 'juejin', 'xiaomei', 'km'))
print(client.geodist('company', 'juejin', 'juejin', 'km'))

# 获取元素位置
print(client.geopos('company', 'juejin' ))
print(client.geopos('company', 'ireader'))
print(client.geopos('company', 'meituan'))
print(client.geopos('company', 'jd'))
print(client.geopos('company', 'xiaomei'))

# 获取元素hash值

print(client.geohash('company', 'juejin'))
# 查找对应坐标
# curl https://geohash.org/wx4gd94yjn0

print(client.georadiusbymember('company', 'ireader', 20, 'km',count=3, sort="DESC"))
print(client.georadiusbymember('company', 'ireader', 20, 'km',count=3, sort="DESC",withdist=True, withcoord=True, withhash=True))

# 查找附近的
print(client.georadius('company', 116.514202, 39.905409, 20, unit='km', withdist=True, withcoord=True, withhash=True, count=3, sort='DESC' ))
