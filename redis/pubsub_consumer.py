import redis
import time

client = redis.StrictRedis()
p = client.pubsub()
p.subscribe('jacky.yao')

while True:
    message = p.get_message()
    if not message:
        time.sleep(1)
        continue
    print(message)
