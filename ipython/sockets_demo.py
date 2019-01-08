import socket
import sys
import re

def check_server(address, port):
    s = socket.socket()
    print(f"Attemping to connect to {address} on port {port}")
    try:
        s.connect((address, port))
        print(f"Connected to {address} on port {port}")
        return True
        #  s.send('GET / HTTP/1.1\n\n')
        #  result = s.recv(200)
        #  print(result)
        #  s.close()
    except socket.error as e:
        print(f"Connection to {address} on port {port} failed:")
        return False

if __name__  == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-a', '--address', dest='address', default='localhost', help="ADDRESS for server", metavar="ADDRESS")
    parser.add_option('-p', '--port', dest='port', type="int",default=80, help="PORT  for server", metavar="PORT")
    (options, args) = parser.parse_args()

    print(f"Options {options}, args: {args}")
    check = check_server(options.address, options.port)
    print(f"Check server returned : {check}")

    sys.exit(not check)
