import  redis
import threading

locks = threading.local()
locks.redis = {}

def key_for(user_id):
    return "account_{}".format(user_id)

def _lock(client, key):
    return bool(client.set(key, "True", nx=True, ex=5))

def _unlock(client, key):
    client.delete(key)

def lock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] += 1
        return True

    ok = _lock(client, key)
    if not ok:
        return False

    locks.redis[key] = 1
    return True

def unlock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] -= 1
        if locks.redis[key] <= 1:
            del locks.redis[key]

        return True

    return False

client = redis.StrictRedis()
print("lock", str(lock(client, "codehole")))
print("lock", str(lock(client, "codehole")))
print("unlock", str(unlock(client, "codehole")))
print("unlock", str(unlock(client, "codehole")))
