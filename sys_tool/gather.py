#!/usr/bin/env python
import subprocess

#  command 1
uname = 'uname'
uname_arg = '-a'
print(f"gathering system information with command: {uname}")
subprocess.call([uname, uname_arg])

print

## command 2
diskspace = 'df'
diskspace_arg = '-h'
print(f"gathering system information with command: {diskspace}")
subprocess.call([diskspace, diskspace_arg])

input("press Enter")

