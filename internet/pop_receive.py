#!usr/bin/env python3
# -*- coding: utf-8 -*-

# 收取邮件分两步
# 1. 使用poplib把邮件的原始文本下载到本地
# 2. 用email解析原始文本，还原为邮件对象

import poplib

email = '524930140@qq.com'
password = 'jmw199704033531!'
pop3_server = 'pop.qq.com'

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, mails, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')

msg = Parser().parsestr(msg_content)

server.quit()