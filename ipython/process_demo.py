from multiprocessing import Process, Queue
import time

def f(q):
    x = q.get()
    print(f"Process number {x}, sleeps for {x} seconds")
    time.sleep(x)
    print(f"Process number {x} finished")

q = Queue()

for i in range(10):
    q.put(i)
    i = Process(target=f, args=[q])

    i.start()
    print("main process joins on queue")
    i.join()
    print("main process joins on queue")
