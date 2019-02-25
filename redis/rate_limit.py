import redis
import time

client = redis.StrictRedis(host='localhost', port=637)

def is_action_allowed(user_id, action_key, period, max_count):
    key = f'hint:{user_id}:{action_key}'
    new_ts = int(time.time() * 1000)

    with client.pipeline() as pipe:
        pipe.zadd(key, {new_ts: str(new_ts)})
        pipe.zremrangebyscore(key, 0, new_ts - period * 1000)
        pipe.zcard(key)
        pipe.expire(key, period + 1)
        _, _, current_count, _ = pipe.execute()
        return current_count <= max_count


for i in range(20):
    print(i, is_action_allowed('jack','post', 300, 5 ))
