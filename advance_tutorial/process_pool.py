from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('The task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 同时跑的进程数，默认大小时CPU核数
    for i in range(5):
        p.apply_async(long_time_task, args = (i, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join() #对pool对象调用join会等待所有子进程执行完毕，但是之前必须调用close，且close后不能添加新的process了
    print('All subprocesses done.')