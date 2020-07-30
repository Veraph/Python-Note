# decor.py -- show how to write and use a decorator
# 装饰器用来增强函数的功能，如写一个计算函数运行时间的装饰器，可以把它运用在任意一个函数上而不用逐个重写

import functools # because we want to use the wraps function to pass __name__ etc properties to wrapper()
import time

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def time_calc(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        f = func(*args, **kw)
        exec_time = time.time() - start_time
        print('%s() function excuted in %s ms' % (func.__name__, exec_time))
        return func(*args, **kw)
    return wrapper

@log # equal to: now = log(now)
@time_calc 
def now():
    print('2020')

now() # now 会被return两次，所以结果会有两个2020