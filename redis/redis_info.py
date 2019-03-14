import redis

client = redis.StrictRedis()

print(client.info('stats')['instantaneous_ops_per_sec'])

print(client.info('clients')['connected_clients'])

print(client.execute_command('client list'))

print(client.info('stats')['rejected_connections'])

print(client.info('memory')['used_memory_human'])

print(client.info('memory')['used_memory_rss_human'])

print(client.info('memory')['used_memory_peak_human'])

print(client.info('memory')['used_memory_lua_human'])

print(client.info('replication'))

print(client.info('sync'))
