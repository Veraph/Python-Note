## Notes of useful modules
### 内建  
1. collections
   1. namedtuple创建带名字的tuple
   2. deque实现高效插入和删除的双向列表，适用于队列和栈
   3. OrderedDict创建有序dict，按插入顺序排列FIFO
   4. Counter统计字符出现的个数
2. hashlib(提供摘要算法/哈希算法)
   1. 如md5，sha1等
3. hmac(增加了一个口令，使即使相同的输入也得不到一样的哈希)
4. urllib(提供操作url的功能)
5. HTMLParser（用于解析网页中的文本、图像等）
### 第三方
1. requests，相比于urllib更好用
2. psutil，用于实现系统监控

### virtualenv
可以为每一个应用创建一套独立的python运行环境

    virtualenv --no-site-packages venv # 创建一个环境，不包括第三方包
    source venv/bin/activate # 进入该环境
    deactivate # 退出该环境，回到系统环境

### 海龟绘图(turtle)
结合递归，循环等可以画出复杂图形