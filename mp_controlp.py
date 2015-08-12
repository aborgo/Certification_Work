"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
"""
from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread
from random import choice
from string import ascii_letters
if __name__ == '__main__':
    WORKERS = 10
    
    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))
    
    ot = OutThread(WORKERS, outq)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    
    instring = ''
    for i in range(1000):
        instring += choice(ascii_letters)
    for work in enumerate(instring):
        inq.put(work)
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control thread terminating")

