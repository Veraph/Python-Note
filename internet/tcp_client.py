#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 与指定ip和指定端口的服务器主动建立连接
s.connect(('127.0.0.1', 9999))

# 接收信息
print(s.recv(1024).decode('utf-8'))

# 发送数据
for data in [b'Mengwei', b'Veraph', b'Jiang']:
    s.send(data)
    # 再接收信息
    print(s.recv(1024).decode('utf-8'))

# 发送退出请求（发送空也行）
s.send(b'') # b'exit' 也可以
s.close