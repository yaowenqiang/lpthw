import redis
client = redis.StrictRedis(host='localhost', port=637)
# CL.THROTTLE <key> <max_burst> <count per period> <period> [<quantity>]
client.execute_command('cl.throttle user 15 30 60 1 ')
