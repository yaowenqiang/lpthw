import redis

client = redis.StrictRedis()

pipeline = client.pipeline(transaction=True)

pipeline.multi()

pipeline.set('books','mybook')
pipeline.incr('books')
pipeline.incr('books')
pipeline.set('count',1)
pipeline.incr('count')
pipeline.incr('count')
try:
    values = pipeline.execute()
    print(values)
except Exception as e:
    print(e)
