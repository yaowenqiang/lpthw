import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://localhost:8000")

print(s.pow(2,3))
print(s.add(2,3))

# TODO mul 应该只传两个参数，此处有bug
print(s.mul(2,3,4))

print(s.system.listMethods())
