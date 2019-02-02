from threading import Thread

import subprocess
from queue import Queue

num_threads = 3
queue = Queue()

ips = ['10.0.1.1','10.0.1.2','10.0.1.3','10.0.1.4']

def pinger(i,q):
    while True:
        ip = q.get()
        print(f"Thread {i} Ping to {ip}")
        ret = subprocess.run(['ping',"-c 1",f"{ip}"],stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)

        if ret == 0:
            print(f"{ip} is alive")
        else:
            print(f"{ip} did not respond")

        
        q.task_done()


for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()

for ip in ips:
    queue.put(ip)

print("Main Thread waiting")
queue.join()
print("Done")
