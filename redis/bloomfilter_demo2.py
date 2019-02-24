import redis
import random
import pprint

client = redis.StrictRedis(host='localhost', port=637)

CHARS = ''.join(chr(ord('a') + i) for i in range(26))
#  print(CHARS)
def random_string(n):
    chars = []
    for i in range(n):
        idx = random.randint(0, len(CHARS)-1)
        #  pprint.pprint(idx)
        chars.append(CHARS[idx])
        #  pprint.pprint(chars)

    return_str =  ''.join(chars)
    #  pprint.pprint(return_str)
    #if return_str != '':
    return return_str
    #klse:
    #    return random_string(n)
    

users = list(set([random_string(i) for i in range(100000)]))
#  pprint.pprint(users)
print(f"total {len(users)} users")
users_train_count = int(len(users)/2)
#  pprint.pprint(users_train_count)
users_train = users[:users_train_count]
#  pprint.pprint(users_train)
users_test = users[users_train_count:]

client.delete('users:train')

for i in users_train:
    if i != '':
        command = "bf.add  users:train  " + i
        client.execute_command(command)
    
print("all trained")
falses = 0
for user in users_test:
    ret = client.execute_command(f'bf.exists users:train {user}')
    if ret == 1:
        falses += 1

print(falses / len(users_test))


