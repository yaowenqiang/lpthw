import redis
# redis-benchmark  -t set -q without pipeline
# redis-benchmark  -t set -q -P 2 with pipeline 2

client = redis.StrictRedis()

pipe = client.pipeline()

pipe.set('aaa','bbb')
pipe.set('ccc','ddd')
pipe.execute()
