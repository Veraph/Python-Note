## Notes of Database
1. 数据库的发展经历了：网状数据库 --> 层次数据库 --> 关系数据库
2. 关系数据库的基础是映射(即基于表的一对多的关系)

### SQLite
1. 要操作关系数据库，首先要连接到数据库，一个数据库连接称为Connection，连接数据库后要打开游标(cursor)，通过游标执行SQL语句获得结果
2. SQLite的特点是轻量级，可嵌入，但是不能承受高并发的访问，适合桌面和移动应用

### Mysql
1. Mysql是为服务器端设计的数据库，能承受高并发访问，但是占用内存也远大于SQLite
2. Mysql内部有多种数据库引擎，最常见的是支持数据库事务的InnoDB
3. 执行改变操作后记得要调用commit()提交事物
4. Object-Relational-Mappinp(ORM)， 把关系数据库的表结构映射到对象上（Python上最有名的ORM框架是SQLAlchemy）