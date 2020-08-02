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