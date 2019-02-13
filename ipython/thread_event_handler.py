from threading import Timer
import sys
import time
import copy
import os
from subprocess import call


class EventLoopDelaySpawn(object):
    def __init__(self, poll=10, wait=1, verbose=True, dir1="/tmp/dir1/", dir2="/tmp/dir2/"):
        self.poll = int(poll)
        self.wait = int(wait)
        self.verbose = verbose
        self.dir1 = dir1
        self.dir2 = dir2

    def poller(self):
        time.sleep(self.poll)
        if self.verbose:
            print(f"Polling at {self.poll} seconds interval")

    def action(self):
        if self.verbose:
            print(f"waiting {self.wait} seconds to run Action")

        ret = call(f"rsync -av --delete {self.dir1}/ {self.dir2}", shell = True)

    def eventHandler(self):
        # if 2 directories contain same file names

        if os .listdir(self.dir1) != os.listdir(self.dir2):
            print(os.listdir(self.dir1))
            t = Timer(self.wait, self.action)

            t.start()

            if self.verbose:
                print(f"Event Registered")

        else:
            if self.verbose:
                print(f"No Event Registered")


    def run(self):
        try:
            while True:
                self.eventHandler()
                self.poller()
        except Exception as err:
            print(f"Error : {err}")

        finally:
            sys.exit(0)

e = EventLoopDelaySpawn()
e.run()
                




