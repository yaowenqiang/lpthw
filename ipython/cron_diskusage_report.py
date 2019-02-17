import smtplib
import subprocess
import string

p = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE)
MSG = p.stdout.read()
FROM = "python-systems-admin@example.com"
TO = "staff@example.com"
SUBJECT = "Nightly Disk Report"
