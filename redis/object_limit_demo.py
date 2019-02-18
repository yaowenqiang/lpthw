import redis

client = redis.StrictRedis()

client.delete('hello')

for i in range(512):
    client.hset('hello', str(i),str(i))

print(client.object('encoding', 'hello'))

client.hset('hello', '512',512)

print(client.object('encoding', 'hello'))

client.delete('world')

for i in range(64):
    client.hset('world', str(i),"0"*(i + 1))

print(client.object('encoding', 'world'))

client.hset('world', '512','0'* 65)

print(client.object('encoding', 'world'))
