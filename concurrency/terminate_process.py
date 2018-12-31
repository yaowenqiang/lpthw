import multiprocessing
import time

def do_work():
    '''do work'''
    print("Starting do_work funciton")
    time.sleep(5)
    print("Finished do_work function")

if __name__ == "__main__":
    p = multiprocessing.Process(target=do_work)
    print("[Running] Process is alive:{}".format(p.is_alive()))
    p.start()
    print("[Running] Process is alive:{}".format(p.is_alive()))
    p.terminate()
    p.join()
    print("[After Termination] Process is alive:{}".format(p.is_alive()))
    print("Process exit code {}".format(p.exitcode))
