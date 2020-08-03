#!usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import threading

async def hello():
    print('Hello, world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(1) # 把这里换成真正的IO操作，多个coroutine就可以由一个线程并发执行
    print('Hello again! (%s)' % threading.currentThread())



# 获取Event loop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()