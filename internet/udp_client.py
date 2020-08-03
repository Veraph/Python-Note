#!usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 不用调用connect()， 直接sendto()
for data in [b'Mengwei', b'Veraph', b'Jiang']:
    #发送数据
    s.sendto(data, ('127.0.0.1', 5555))

    #接收数据
    print(s.recv(1024).decode('utf-8'))

s.close()