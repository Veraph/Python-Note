## Notes of python high-level features

### I/O Programming
同步IO中cpu会等待IO执行的结果，异步IO则不会
#### 同步IO Synchronous I/O
python的IO操作和C兼容，注意在磁盘上读写文件的功能都是由操作系统提供的，不允许普通的程序直接操作磁盘
##### 读文件
小文件使用read()一次性读取，不确定时反复调用read(size)保证内存不爆掉，配置文件调用readlines()

    with open('/path/file', 'r') as f:
        print(f.read())
这么写不用我们手动关闭文件。  
有read()方法的对象统称为file-like Object  
读取二进制文件时使用'rb'模式  
读取非UTF-*编码的文本文件，要给open()传入encoding = 'gbk'参数，如读取GBK编码文件  
open()还可以接收一个errors的参数，可以设置为'ignore'
##### 写文件
传入'w'和‘wb'到open()进行文本文件或二进制文件的编写。  
注意以'w'模式写入时文件如果已存在会被直接覆盖，希望追加到文件末尾应该传入'a'

##### StringIO
在内存中读写str

    from io import StringIO
    f = StringIO()
    #写入
    f.write('Hello\n')
    f.write('world\n')
    print(f.getvalue())

    #读取
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())

##### BytesIO
在内存中操作二进制数据

    from io import BytesIO
    #写入
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())

    #读取
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    f.read()

##### 操作文件和目录
使用os模块，一部分函数放在os中，还有一部分放在os.path中

##### 序列化 pickling/serialization...
把变量从内存中变成可存储或传输的过程称之为序列化，序列化之后可以把内容写入磁盘或传输到别处。  
使用pickle模块的dump()/dumps()和load()/loads()可以实现序列化和反序列化，但是只能用于python

##### JSON（可以被所有语言读取）
使用内置的json模块

    import json

    d = dict(name='Bob', age=20, score=88)
    json.dumps(d) 
    # dumps()返回一个内容为标准JSON的str
    # dump()可以直接把JSON写入一个file-like Object
    
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    json.loads(json_str)
    # loads()把JSON的字符串直接反序列化
    # load()从file-like Object中读取字符串并反序列化

dumps()中拥有可选参数default把任意对象变为可序列化为json的对象，但需要我们自己编写函数

    import json

    class Student(obejct):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age
        }

    s = Student('Bob', 20)
    print(json.dumps(s, default = student2dict))

loads()中也拥有可选参数object_hook帮助进行反序列化

    import json

    def dict2student(d):
        pass

    json_str = '{"age": 20, "name": "Bob"}'
    print(json.loads(json_str, object_hook = dict2student))





#### 异步IO Asynchronous I/O



### 进程(process)和线程(thread)
1. 一个任务就是一个进程，一个进程内部有很多子任务，这些子任务被称为线程
2. 多任务的实现方式：
   1. 多进程模式
   2. 多线程模式
   3. 多进程+多线程模式
3. 实现多任务的时候，通常会设计Master-Worker模式，Master(主进程/主线程)分配任务，Worker执行任务，通常一个Master，多个Workers
4. 多进程最大的优点是稳定性高，一个子进程挂了不会影响其他子进程和父进程(父进程只分配任务，挂掉的概率低）。缺点是创建进程的代价太大，特别是在windows下(没有fork，只能模拟)。
5. 多线程比多进程稍微快一点，但是致命的缺点是一个线程挂了，整个程序都有可能崩溃
6. 多任务一旦多到一定限度，就会消耗掉所有资源，效率急剧下降，操作系统就主要忙着切换任务，没什么时间去执行任务了
7. 是否采用多任务还需要考虑任务的类型
   1. 计算密集型，主要消耗CPU资源，最高效的利用CPU应该使任务数等于CPU核心数，代码效率至关重要，最好用C语言。常见比如计算圆周率，视频高清解码等。
   2. IO密集型，CPU资源消耗很少，大部分时间都在等待IO完成，此时，在一定限度内任务越多，CPU效率越高。常见比如Web应用，代码效率不重要的情况下，使用python等开发效率最高(代码少)的脚本语言是首选，C语言反而不行(甚至最差)
#### 多进程
1. 使用fork调用，当一个进程接到新任务时就可以复制出一个子进程来处理新任务  
2. 也可使用跨平台版本的多进程模块multiprocessing编写多进程（在unix/linux中封装了fork）
3. 如果要启用大量子进程，可以用进程池Pool的方式批量创建
4. subprocess模块可以启动一个子进程，然后控制其输入和输出
5. multiprocessing模块中的Queue，Pipes等多种方式可以用来交换数据
#### 多线程
1. 使用高级模块threading(是对低级模块_thread的封装)
2. 任何进程默认启动一个线程，该线程被称为主线程(MainThread)，主线程可以启动新的线程
3. 多线程与多进程最大的不同在于
   1. 多进程中，同一个变量各自有一份拷贝存在于每个进程中，互不影响
   2. 多线程中，所有变量都有所有线程共享，所以变量容易被任何一个线程修改
4. 所以我们需要给方法上Lock，当某个线程开始执行某个方法时，该线程获得了锁，其他线程不能同时执行该方法，同一时刻只有一个线程可以拥有该锁
##### 锁的实现

    lock = threading.Lock()

    def run_thread(n):
        for i in range(10000):
            lock.acquire() # 获得锁
            try:
                func()
            finally:
                lock.release()
5. 锁的坏处：
   1. 阻止了多线程并发执行，包含锁的代码实际上只能以单线程模式执行
   2. 由于可以存在多个锁，不同的线程持有不同的锁且试图获取其他锁时可能造成死锁，线程会全部挂起，不能执行不能结束，只能等系统强行终止
##### 多线程的并发在python不能实现

    import threading, multiprocessing

    def loop():
        x = 0
        while True:
            x = x ^ 1
    
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop)
        t.start()

    # 以上代码企图启动N(cpu核数)个死循环线程
    # 但监控时cpu占用率只有102%，即仅使用到一核，(4核心跑满应该为400%)
发生上述情况的原因是：  
python的线程虽然是真正的线程(Posix Thread)，但官方解释器CPython解释代码时，有一个Global Interpreter Lock(GIL)锁，任何Python线程执行前都要先获得GIL锁，然后每执行100字节，解释器就会自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都上了锁，所以多线程在Python中只能交替执行，不能实现多线程的并发。  
这是历史遗留问题，要真正利用多核实现多线程，除非重写一个不带GIL的解释器或者通过C扩展来实现。  
好在Python是可以通过多进程实现多核任务的，因为每个进程有各自独立的GIL锁，互不影响。

#### ThreadLocal
多线程环境下使用局部变量好于全局变量，因为局部变量不会影响其他线程，而全局变量的修改必须加锁。  
但是局部变量调用的时候传递起来很麻烦。  
ThreadLocal作为全局变量，解决了参数在一个线程中各个函数之间互相传递的问题，最常用的地方是为每个线程绑定一个数据库连接，HTTP请求，用户信息等。  
其本质是本身为全局变量，是一个dict，里面的每个属性都是线程的局部变量，可以任意读写，互不干扰，也不用担心锁的问题。  
例子见thread_local.py

#### 分布式进程
在线程和进程中，优先选择进程，因为进程更稳定而且可以分步到多台及其，而线程最多只能分布在同一台机器的多个CPU。

### 正则表达式regular expression
用以匹配字符串
1. \d --- 匹配一个数字
2. \w --- 匹配一个字母或数字
3. \s --- 匹配一个空格
4. . --- 匹配任意字符
5. *，+，？--- 表示任意个，至少一个，0或1个字符
6. {n}，{n,m} --- 表示n个，n-m个字符
7. ‘-’这样的特殊字符，需要用'\'在前面转义  
更精确的表达  
1. 用[]表示范围, [0-9a-zA-Z\_]表示一个数字，字母或下划线
2. [0-9a-zA-Z\_]+表示至少一个数字，字母或下划线组成的字符串
3. [a-zA-Z\_][0-9a-zA-Z\_]*匹配由一个字母开头，后面接任意个数字，字母或下划线的字符串（即python的合法变量）
4. [a-zA-Z\_][0-9a-zA-Z\_]{0,19}限制了变量长度为1-20个
5. (P|p)ython匹配Python或python
6. ^表示行的开头，^\d即必须以数字开头；\$表示行的结束，\d$即必须以数字结尾
7. ^python$是整行匹配，只匹配python
#### re模块
python提供的re模块包含所有正则表达式的功能  

    # re.match判断正则表达式是否匹配
    import re
    re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
    # 如果match会返回一个match对象，不match返回None
#### 切分
用来把不规范的输入转化为正确的数组

    import re
    re.split(r'[\s\,\;]+', 'a,b;;  c   d')
#### 分组
用()可以进行分组，使用group()则可以提取，group(0)永远是原始字符串

    import re
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345') # 注意使用括号的情况下，-前面没有转义也可以
    m.group(0)
    m.group(1)
    m.group(2)
#### 正则匹配默认贪婪匹配

    re.match(r'^(\d+)(0*)$', '1023000').groups()
    # 会发现\d+把后面的0都匹配了，0*只返回一个空字符串，
    # 采用非贪婪匹配(尽可能少匹配)，可以在\d+后面加上?
#### 编译正则表达式
如果要重复使用某个正则表达式，我们可以预编译，然后后面直接使用

    import re
    re_tele = re.compile(r'^(\d{3})-(\d{3,8})$')
    re_tele.match('010-12345').groups()