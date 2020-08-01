## Notes for advanced tutorial

### 迭代
在Python中迭代通过for...in完成，可以通过collections模块重的Iterable类型判断（e.g. isinstance('abc', Iterable))。  

### 生成器(Generator)
第一种生成器方法  
L是列表：

    L = [x * x for x in range(10)]

G是生成器：

    G = (x * x for x in range(10))
生成器元素可用next()函数逐个获得，但一般不用。一般用for循环，因为generator可迭代。


第二种生成器方法，当函数定义中包含yield关键字，那函数变成一个生成器函数，调用next()时执行，遇到yield语句返回。

### 迭代器(Iterator)
可以被next()函数调用并不断返回下一个值的对象就是迭代器，所以生成器都是迭代器对象。  
迭代器对象表示一个数据流，不能提前知道长度，只有接受next()函数时按需计算，所以其计算时惰性的，也因为如此迭代器可以表示一个无限大的数据流。

### 高阶函数
#### map()
map()接受一个函数和一个可迭代对象作为参数，然后返回一个生成器

    def f(x):
        return x * x
    r = map(f, [1, 2, 3, 4])
    list(r)
值得注意的是，r是一个生成器，我们可以用list()将整个序列计算出来并返回

#### reduce()
reduce()接受一个函数(必须是接受两个参数的函数)和一个序列，将函数作用在序列上，使其不断地把结果和序列的下一个元素计算，效果如下：

    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
实例将序列转换成整数：

    from functools import reduce
    def fn(x, y):
        return x * 10 + y
    reduce(fn, [1, 2, 3, 4]) # 结果是1234

结合map()和reduce()，我们可以写出一个将str转换为int的函数

    from functools import reduce

    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(s):
        return DIGITS[s]
    
    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#### filter()
filter()是内建函数，接受一个函数和一个序列，把传入函数作用于每个元素，返回True保留，False则丢弃。

    # 删除偶数的操作
    def is_odd(n):
        return n % 2 == 1

    list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8]))


可以结合埃及筛法得到素数

    def _odd_iter(): # 前面的下划线代表声明这是私有函数，勿动
        '''it is a generator'''
        n = 1
        while True:
            n += 2
            yield n
    
    def _not_divisible(n):
        '''used to filter elements'''
        return lambda x : x % n > 0
    
    def primes():
        '''it is a generator for continuelly return next primer number'''
        yield 2
        it = _odd_iter()
        while True:
            n = next(it)
            yield n
            it = filter(_not_divisible(n), it) # 构建一个新序列使其元素都不是n的倍数
    # 注意调用此函数时要设置一个退出循环的条件！因为primes是一个无限序列

#### sorted()
sorted()也是一个高阶函数，能够接受一个key函数来实现自定义排序，还能正常接受reverse进行反向，其原理是用key函数把原序列映射为我们想要的序列，如：

    sorted(['bob', 'Alex', 'Veraph', 'venant'], key = str.lower)

这里sorted先按照key把原字符串映射为一个全为小写的序列，对此序列进行排序

#### 函数作为返回值
当函数作为返回值，即函数不马上发生作用，而可以根据需要再计算

    def lazy_sums(*args):
    '''
    *args 代表接受数量可变的非关键字参数列表
    **kwargs 代表接受数量可变的关键字参数pair
    '''
        def sum():
            ax = 0
            for n in args:
                ax += n
            return ax
        return sum
    # 现在当我们调用lazy_sum()时，返回的是一个求和函数f，只有真正调用求和函数f()时才会计算

        f = lazy_sum(1, 2, 3)
        f   # 这个只会返回一个函数
        f() # 这个才会返回结果

#### 闭包
如上个程序，lazy_sum返回函数sum，相关参数和变量都被保存在这个返回的函数中，这就时被称为闭包(Closure)的一种程序结构，另外每次调用lazy_sum都会返回一个新函数且调用结果互不影响即使传入了相同的参数。  

    # 返回闭包时不要使用循环变量或后续会发生变化的变量
    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i * i
            fs.append(f)
        return fs
    f1, f2, f3 = count()
    f1()    # 这里三个结果都变成了9，这是因为返回的函数引用了循环变量i，
    f2()    # 但是返回的函数并没有立即执行f1()...时，等到三个函数都返回时
    f3()    # i已经变成了3，所以结果都是9
如果一定要引用循环变量，可以再创建一个函数，用参数绑定循环变量的当前值

    def count():
        def f(j):
            def g():
                return j*j
            return g
        fs = []
        for i in range(1, 4):
            fs.append(f(i))
        return fs
    f1, f2, f3 = count() # 现在f1(), f2(), f3()分别是1,4,9

#### 匿名函数
匿名函数只能有一个表达式，且返回值就是该表达式的效果.  
匿名函数还可以作为返回值返回，自身也是一个函数对象，可以把匿名函数赋值给一个变量。  
等效表示如下：

    lambda x: x * x

    def f(x):
        return x * x


#### 装饰器（decorator)
在函数代码运行期间动态增加功能的方式称之为装饰器，其本质是一个返回函数的高阶函数（接受函数作为参数）。

    func.__name__ #__name__是函数对象的属性，可以通过其拿到函数的名字

具体调用见decor文件

#### 偏函数
当函数的参数个数过多需要简化的时候，使用functools.partial可以创建一个新的函数，这个新函数可以固定原函数的部分参数，实例如下：

    int('1000', base=2)
    int2 = functools.partial(int, base = 3) 
    int2('1000') # 就等价于上面的函数

    '''下面为原理'''
    kw = {'base': 2}
    int('1000', **kw) 

#### 模块和包
一个py文件可以看成一个模块module，很多py文件可以组成一个包package，顶层包名要特殊，另外__init__.py必须存在  
外部不需要引用的函数应全部定义为private， 即在函数名前加_， 只有外部需要引用的才定义为public，即正常命名

#### 面向对象编程
面向对象的抽象程度比函数要高，因为一个class即包含数据又包含操作数据的方法  
面向对象的三大特点：
1. 数据封装
在类里面定义函数，所以数据和逻辑都被封装，可以很容易的调用，但是不用知道内部实现的细节
##### 设置访问限制

    class Student():
        def __init__(self, name, score):
            '''在属性名称前加入两个下划线，使之不能从外部访问'''
            self.__name = name
            self.__score = score

        def print_score(self):
            print(self.__score) # 内部还是可以访问的

        def get_name(self):
            '''要获得似有变量，可以在类里面创建函数'''
            return self.__name

        def set_score(self, score):
            '''如果要允许外部代码修改，也是在类里面增加方法, 且可以更加灵活，比如添加参数检查'''
            if 0 < score:
                self.__score = socre
            else:
                raise ValueError('invalid score')
            # 以上的实现方式比简单的student.score = 99更为科学
    ‘’‘ 注意：
    前后都有下划线的是特殊变量，可以直接访问，
    前面只有一个下划线的虽然不是private变量，但是约定俗成视为私有变量不要随意访问
    而实际上私有变量也不是完全不能访问，使用student._Student__name就可以访问（解释器将__name变量改成了_Student__name变量）
    ‘’‘

2. 继承
子类和父类存在同名方法时，子类会覆盖父类
3. 多态
class Animal() 这样的定义，Animal就成了一种数据类型，如果class Dog(Animal)，即Dog继承了Animal，那么Dog类的对象既是Dog类型又是Animal类型。  
当我们传入Dog，Cat等子类，只需要接受Animal类型，当我们调用类型里的函数时，调用子类还是父类Animal里的同名函数由对象决定。所以调用方法只管调用， 不管细节。  
开闭原则：
    对扩展开放：允许新增父类的子类
    对修改封闭：不需要修改依赖父类类型的函数  
Python是动态语言，要对某种对象调用某种方法，只要保证该对象实现了该方法就可，不一定要传入具体类型

##### 获取对象的信息
可以用type()判断基本类型，它返回对应的Class类型。  
判断一个对象是否是函数可以使用types模块

    import types
    
    def fn():
        pass
    type(fn) == types.FunctionType
    type(abs) == types.BuiltinFunctionType
    ## above all return true

判断class类型，可以使用isinstance()  

    class Animal():
        pass
    class Dog(Animal):
        pass

    a = Animal()
    b = Dog()
    isinstance(b, Animal) # return True
    isinstance(a, Dog) # return False

dir()可以获得一个对象的所有属性和方法， 配合getattr()，setattr()和hasattr()可以获取属性，设置属性和询问属性是否存在

##### 类属性和实例属性
除了在__init__()中给实例绑定属性外，也可以直接在class下给类绑定类属性，当实例访问该属性时，如果实例未绑定则返回类属性，否则优先返回实例属性，
不过还是可以通过类直接访问，如Animal.name

#### 面向对象高级编程
1. 除了给实例绑定属性，还可以给实例绑定方法，但是给A实例绑定的方法不能在B实例上实现，解决方法是直接给类绑定方法
##### __slots__
定义class的时候，可以定义特殊变量__slots__来限制该class实例可以添加的属性

    class Student():
        __slots__ = ('name', 'age')
要注意的是__slots__仅对当前类实例起作用，对继承的子类不起作用

    class Student(Graduate):
        pass
    # Graduate类实例是可以绑定除了name和age之外的属性的

##### 内置装饰器@property
@property 装饰器把一个方法变成属性，这个属性是只读属性  
@func.setter 装饰器把一个方法变成属性赋值，这个属性是可读写的

    class Student():
        
        @property
        def birth(self):
            return self._birth

        @birth.setter # 这个装饰器，要在之前使用过@property之后才能使用，因为是前一个生成的
        def birth(self, value):
            self._birth = value
        
        @property
        def age(self):
            return 2015 - self._birth

##### 多重继承
通过多重继承，一个子类可以同时获得多个父类的所有功能，这种设计称为MixIn  
    
    class Animal():
        pass
    
    class Runable():
        def run(self):
            print('running')

    class Dog(Animal, Runable):
        pass

##### 定制类
__str__(self)方法帮助返回好看的打印数据，要调用print
__repr__(self)方法帮助返回好看的开发者字符串，直接输入

    class Student():
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return 'Student Object (name: %s)' % self.name

        __repr__ = __str__ #偷懒写法

__iter__(self)方法返回一个迭代对象，结合__next__对象进行迭代  

__getitem__(self)方法能表现得像list那样下标去处元素  
__delitem__(self)用于删除某个元素  

__getattr__(self, attr)方法作用于当调用不存在属性时，解释器会试图调用getattr尝试获得  

__call__(self) 方法帮助在实例本身调用方法  
函数都是callable的

##### 枚举类

    from enum import Enum, unique

    Month = Enum('Month', ('Jan', 'Feb', 'Mar'))

    for name, member in Month.__members__.items():
        print(name, member, member.value) # value 属性是自动赋给成员的int常量，默认从1开始计数

    # 还可以更精确的控制

    @unique # 这个装饰器帮助检查有无重复值
    class Weekday(Enum):
        Sun = 0
        Mon = 1

##### 元类
创建class的本质是使用type()函数创建出class

    #使用type()动态创建类
    def fn(self, name = 'World'):
        print('Hello, %s.' % name)
    Hello = type('Hello', (object,), dict(hello = fn)) #创建出Hello class,依次传入class名称，父类集合，class方法名字和函数绑定

MetaClass元类，是类的类


