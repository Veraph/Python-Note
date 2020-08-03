#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, threading, time
# 服务器不会自己退出，需要手动关闭

# 创建一个基于IPv4和TCP协议的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定要监听的地址和端口(这个端口还是服务器端口，客户端端口在accept()那里接收)
# 同一个端口被一个socket绑定后就不能被别的socket绑定了
s.bind(('127.0.0.1', 9999)) # 127.0.0.1是一个特殊的IP地址，表示本机， 0.0.0.0表示绑定到所有网络地址

# 调用listen()监听端口
s.listen(5) # 指定等待连接的最大数量
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr) 
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 循环接受来自客户端的连接
while True:
    # 接受新连接
    sock, addr = s.accept() # addr包含客户端的一个ip地址和一个端口号
    # 每个连接都必须创建新线程（或进程）
    t = threading.Thread(target = tcplink, args=(sock, addr))
    t.start()




