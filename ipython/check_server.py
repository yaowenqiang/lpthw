import socket
import sys
import re

def check_server(address, port, resource):
    # build up HTTP request string
    if not resource.startswith('/') :
        resource = '/' + resource

    # request_string = b"GET {resource} HTTP/1.1\r\nHost : {address}\r\n\n"
    request_string = b"GET / HTTP/1.1\n\n"

    print("HTTP request:")
    print(f"|||{request_string}|||")

    s = socket.socket()
    print(f"Attempting to connect to {address} on port {port}")
    try:
        s.connect((address, port))
        print(f"Connected to connect to {address} on port {port}")
        s.send(request_string)
        rsp = s.recv(100)
        print(f"Recieved 100 bytes  of HTTP response")

    except socket.error:
        print(f"Connection to {address} on port {port} failed: ")
        return False
    finally:
        print(f"Closing the connection ")
        s.close()

    lines = rsp.splitlines()

    print(f"First line of HTTP response : {lines[0]}")

    try:
        version, status, message = re.split(r'\s+', lines[0], 2)
        print(f"version: {version}, Status:{status}, Message: {message}")

    except ValueError:
        print("Failed to split status line")
        return False


    if status in ['200', '301']:
        print(f"Success - Status was {status}")
        return True
    else:
        print(f"Status was {status}")
        return False

if __name__ == '__main__':
    check_server('localhost',80,'/')
