#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# 记得每次使用完都要关闭游标和连接
# 如果文件不存在会自动在当前目录创建
conn = sqlite3.connect('test.db')
# 创建一个cursor
cursor = conn.cursor()

# 执行语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 执行语句，插入记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

# 获取插入的行数
cursor.rowcount

# 关闭Cursor
cursor.close()

# 提交事务
conn.commit()

# 中断连接
conn.close()