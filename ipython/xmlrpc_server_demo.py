from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import os

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

with SimpleXMLRPCServer(('localhost',8000),
            requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(pow)

    def adder_function(x,y):
        return x + y

    server.register_function(adder_function, 'add')


    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs)

    server.serve_forever()

#def ls(directory):
#    try:
#        return os.listdir(directory)
#    except OSError:
#        return []
#
#def ls_boom(directory):
#    return os.listdir(directory)
#    
#def cb(obj):
#   print("OBJECT:: {obj}") 
#   print("OBJECT.__class__:: {obj.__class__}") 
#   return obj.cb()
#   
#  
#if __name__ == '__main__':
#    s = SimpleXMLRPCServer(('127.0.0.1',8765))
#    
#    s.register_function(ls)
#    s.register_function(ls_boom)
#    s.register_function(cb)
#    s.serve_forever()
