import redis
client = redis.StrictRedis()
key = 'myusers'
client.delete(key)
for i in range(10000):
    client.pfadd(key, f"user_{i}")
    total = client.pfcount(key)
    #print("total:", total + 1)
   # if total != i + 1:
   #     print("total:", total + 1)
   #     break
print(10000)
print(total)
