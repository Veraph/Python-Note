#!usr/bin/env python3
# -*- coding: utf-8 -*-


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 5555))

# 不需要调用listen()进行监听，直接接收来自任何客户端的数据
print('Bind UDP on 5555...')
while True:
    data, addr = s.recvfrom(1024) # recvfrom 返回数据和客户端的地址与端口
    print('Received from %s:%s' % addr) # addr是(IP, 端口)类型的tuple
    s.sendto(b'Hello, %s!' % data, addr) # 直接调用sendto把数据用UDP发给客户端

# 注意这个例子省略了多线程