from multiprocessing import  Process, Queue, Pool
import time
import subprocess
from IPy import IP

import sys

q = Queue()

ips = IP('10.0.1.0/24')

def f(i,q):
    while(True):
        if q.empty():
            sys.exit()

        ip = q.get()

        ret = subprocess.call(['ping', f'-c 1 , {ip}'], shell=True, stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)

        if ret == 0:
            print(f"{ip} is alive")
        else:
            print(f"Process Number: {i} didn't find a response for {ip} ")


for i in ips:
    q.put(i)

for i in range(50):
    p = Process(target=f, args=(i,q))
    p.start()

    print("main process joins on queue")

    p.join()
    print("main process finished")

