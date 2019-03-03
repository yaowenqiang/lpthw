import redis

client = redis.StrictRedis()

for i in range(100000):
    client.set(f'key{i}',i )

keys = client.scan( cursor=0, match='key100*', count=10)
# scan 0 match key99* count 1000
print(keys)
