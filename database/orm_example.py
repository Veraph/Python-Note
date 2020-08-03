#!usr/bin/env python3
# -*- coding: utf-8 -*-


from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # table name
    __tablename__ = 'user'

    # table struct
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# create new user object
new_user = User(id='4', name='Mengwei')
# add to session
session.add(new_user)
# save to database
session.commit()
# close session
session.close()

# 查询对象
session = DBSession()

# create Query, filter is the where condition, finally use one() to return one row, if all(), return all rows
user = session.query(User).filter(User, id=='4').one()

# print the type and the name property of the obeject
print('type: ', type(User))
print('name: ', user.name)

# close session
session.close()