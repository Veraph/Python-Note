#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 创建一个socket, AF_INET指定IPv4， SOCK_STREAM指定面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接，小于1024的端口都是internet标准服务的端口，80指web服务的标准端口，25是SMTP，21是FTP
s.connect(('www.sina.com.cn', 80)) # 注意参数是一个tuple

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    d = s.recv(1024) # recv(max)方法决定一次最多接受的字节数
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()

# 打印header，写入html
header, html = data.split(b'\r\n\r\n', 1)
print(header)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)