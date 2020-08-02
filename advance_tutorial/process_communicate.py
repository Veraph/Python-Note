# 在Unix/Linux系统下，multiprocessing封装了fork()调用，不用关心细节
# 在windows里，父进程所有对象都必须通过pickle序列化再传到子进程里去，如果失败优先考虑是不是pickle失败
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    '''写数据进程执行的代码'''
    print('Process to wirte: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    '''读数据进程执行的代码'''
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程
    pw.start()
    pr.start()
    pw.join()
    pr.terminate() # pr子进程是无限循环，必须强行终止