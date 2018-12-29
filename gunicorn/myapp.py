def app(envron, start_response):
    data = b'hello world'
    start_response('200 OK', [
        ('Content-Type','text/plain'),
        ('Content-Length',str(len(data)))
    ])
    return iter([data])

