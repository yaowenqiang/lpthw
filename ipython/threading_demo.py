import threading
import time

count = 1
class KissThread(threading.Thread):
    def run(self):
        global count
        print(f"Thread {count} : Pretending to do stuff.")
        count += 1
        
        time.sleep(2)
        print("donw with stuff")

for i in range(5):
    KissThread().start()
