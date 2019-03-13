import redis

client = redis.StrictRedis()

result = client.execute_command('slotsscan 0 1')

print(result)
