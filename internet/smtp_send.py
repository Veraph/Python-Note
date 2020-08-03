#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置对SMTP的支持，其中的smtplib模块负责发送邮件，email模块负责构造邮件
from email.mime.text import MIMEText
import smtplib

msg = MIMEText('Hello, send by Python', 'plain', 'utf-8') # plain表示纯文本

# 发件人信息
from_addr = input('From: ')
password = input('Password: ')

# 收件人地址
to_addr = input('To: ')

# 输入SMTP服务器地址：
smtp_server = 'smtp.office365.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()