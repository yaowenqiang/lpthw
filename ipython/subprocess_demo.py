import subprocess
# subprocess.call(['df','-hk'])
# subprocess.call(['df','-kh'])
# subprocess.call(['du','-hs']) # show current directory size in human readble format
# subprocess.call('df -k', shell=True) for python 2

subprocess.run(['ls','-lh'], 
                       #shell=True, 
                       # stdout=open('/dev/null','w'),
                        stderr=subprocess.STDOUT)

subprocess.run(['ping','-c 10','baidu.com'], 
                       # shell=True, 
                       # stdout=open('/dev/null','w'),
                       stderr=subprocess.STDOUT)

p = subprocess.Popen('ls -lh', 
                       shell=True, 
                       stdout=subprocess.PIPE)

out = p.stdout.readlines()

for line in out:
    print(line.decode('utf-8').strip())

