import redis
import time
import json

def delay(msg):
    msg.id = str(uuid.uuid4())
    value = json.dumps(msg)
    retry_ts = time.time() + 5
    redis.zadd("delay-queue", msg_id, value)

def loop9):
    while true:
        values = redis.zrangebyscore('delay-queue', 0, time.time(), start=1, num=1)
        if not  values:
            time.sleep(1)
            continue

        value = values[0]
        success = redis.zrem('delay-queue', value)
        if success:
            msg = json.loads(value)
            handle_msg(msg)
        
