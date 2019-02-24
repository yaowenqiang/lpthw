import redis
client = redis.StrictRedis(host='localhost', port=637)
key = 'user_history'
client.delete(key)
for i in range(100000):
    client.execute_command('bf.add', key, f'user_id:{i}')
    # 判断不存在的元素是否存在时会误判
    ret = client.execute_command('bf.exists', key, f"user_id:{i+1}")
    if ret == 1:
        print(i)
        break
    # 判断已存在的元素是否存在时不会误判
    #ret = client.execute_command('bf.exists', key, f"user_id:{i}")
    #if ret == 0:
    #    print(i)
    #    break

