import time
import redis
client = redis.StrictRedis()
p = client.pubsub()
p.subscribe('jacky.yao')
time.sleep(1)
print(p.get_message())
client.publish('jack', 'java comes')

time.sleep(1)
print(p.get_message())
client.publish('jack', 'php comes')
time.sleep(1)
print(p.get_message())
print(p.get_message())

