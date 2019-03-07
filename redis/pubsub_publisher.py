import redis
import time

client = redis.StrictRedis()
while True:
    client.publish('jacky.yao', 'message')
    time.sleep(1)
