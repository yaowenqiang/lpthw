import os
import sys
import pprint
import pyinotify
from  pyinotify import WatchManager, Notifier, ProcessEvent, EventsCodes

class PClose(ProcessEvent):
    def __init__(self, path):
        self.path = path
    
    def process_IN_CLOSE(self, event):
        path = self.path
        
        if event.name:
            self.file = f"{os.path.join(event.path, event.name)}"
            
        else:
            self.file = f"{event.path}"
            
        print(f"{self.file} Closed")
        print(f"Performing pretend action on {self.file}")
        
        import time
        time.sleep(2)
        print(f"{self.file} has been process")
        
    
class Controller(object):
    
    def __init__(self, path='/tmp'):
        self.path = path
    
    def run(self):
        self.pclose = PClose(self.path)
        # PC = self.pclose
        # mask = EventsCodes.IN_CLOSE_WRITE | EventsCodes.IN_CLOSE_NOWRITE
        mask = pyinotify.ALL_EVENTS
        wm = WatchManager()
        
        
        notifier = Notifier(wm,pyinotify.ALL_EVENTS)
        
        print(f"mointioring of {self.path} started")
        
        added_flag = False
        
        while True:
            try:
                if not added_flag:
                    wm.add_watch(self.path, mask)
                    added_flag = True
                
                notifier.process_events()
                
                if notifier.check_events():
                    notifier.read_events()
            except KeyboardInterrupt:
                print("stop monitoring...")
                
                notifier.stop()
                
            except Exception as  err:
                pprint.pprint(err)
                print("error happend!") 
    
def main():
    monitor  = Controller()
    
    monitor.run()


if __name__ == '__main__':
    main()
