import time
import redis
client = redis.StrictRedis()
p = client.pubsub()
p.subscribe('jacky.yao')
#  time.sleep(1)
print(p.get_message())
client.publish('jacky.yao', 'java comes')

#  time.sleep(1)
print(p.get_message())
client.publish('jacky.yao', 'php comes')
#  time.sleep(1)
print(p.get_message())
print(p.get_message())

