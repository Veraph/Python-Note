from multiprocessing import Process
import os

def run_proc(name):
    '''子进程要执行的代码'''
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start.')
    p.start()
    p.join() # join()方法可以等待子进程接受再继续往下运行
    print('Child process end.')

