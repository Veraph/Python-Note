#!usr/bin/env python3
# -*- coding: utf-8 -*-

# 以下代码用于理解协程
def consumer():
    '''a generator'''
    r = ''
    while True:
        n = yield r # yield r先执行，执行完后进入暂停， yield可以接受调用者发出的参数
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 ok'

def produce(c):
    c.send(None) # start the generator，send()在接受None参数的情况下，等同于next(generator)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 功能类似于next(c)，赋值语句中等号右边的先执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)