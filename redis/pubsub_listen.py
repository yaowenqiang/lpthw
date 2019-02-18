import redis

client = redis.StrictRedis()

p = client.pubsub()

p.subscribe('jacky.yao')

for msg in p.listen():
    print(msg)
