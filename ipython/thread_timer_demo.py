from threading import Timer

import sys
import time
import copy

if len(sys.argv) != 2:
    print(f"Must enter an interval")
    sys.exit(1)


def hello():
    print(f"Hello, i just get called after a {call_time} sec delay")

delay = sys.argv[1]

call_time = copy.copy(delay)

t = Timer(int(delay), hello)

t.start()

print(f"waiting {delay} seconds to run function")

for x in range(int(delay)):
    print(f"Main program is still running for {delay} more sec")
    delay = int(delay) - 1
    time.sleep(1)


