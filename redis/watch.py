import redis

def key_for(user_id):
    return f"account_{user_id}"

def double_account(client, account_id):
    key = key_for(account_id)

    while True:
        client.watch()
        value = int(client.get(key))
        value *= 2
        pipe = client.pipeline(transaction=True)
        pipe.multi()
        pipe.set(key, value)

        try:
            pipe.execute()
            break
        except  redis.WatchError:
            continue

    return int(client.get(key))



client = redis.StrictRedis()
account_id = 'jacky'

client.setnx(key_for(account_id), 5)
print(double_account(client, account_id))
