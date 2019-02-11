def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
        
    except OSError as e:
        sys.stderr.write(f"fork #1 failed: {e.errno} {e.stderr} \n")
        sys.exit(1)
    
    os.chdir('/')
    os.umask(0)
    os.setsid()
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"fork #2 failed: {e.errno} {e.stderr} \n")
        sys.exit(1)

for f in sys..stdout, sys.stderr:f.flush()

si = file(stdin, 'r')
so = file(stdout, 'a+')
se = file(stderr, 'a+',0)
os.dump2(si.fileno(), sys.stdin.fileno())
os.dump2(si.fileno(), sys.stdout.fileno())
os.dump2(si.fileno(), sys.stderr.fileno())


