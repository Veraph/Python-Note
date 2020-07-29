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