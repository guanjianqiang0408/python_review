"""
迭代器(Iterator)
    可以遍历的容器对象， 然而迭代器遍历读取容器元素的时候，并不会执行一个迭代
    只要定义了next()或__next__方法，它就是一个的迭代器
    
可迭代对象(Iterable)
    任意对象，只要定义了可以返回一个迭代器__iter__方法，或定义可以支持索引的__getitem__方法
那它就是一个可迭代对象。可迭代对象就是能够供迭代器使用的对象

迭代(Iteration)
    循环遍历某个东西时，这个过程就是迭代

生成器(Generators)
    定义：
        生成器也是一种迭代器，但是只能迭代一次。因为生成器没有把所有值存在内存中，而是运行过程中产生。
    生成器大多时候通过函数实现。不是返回一个值，而是yield一个值

    应用场景：
        当不想同一时间将所有计算出来的大量结果集分配到内存中，特别是结果集中还包含循环。当产生大量数据的时候会占用
    很大的内存资源，
    异常：
        当yield所有值时候，如果继续返回生成器内容，会抛出StopIteration异常。表示生成器所有内容均被yield
"""


# 生成器case
def generator_function():
    for i in range(10):
        yield i


for item in generator_function():
    print(item)


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for item in fibon(5):
    print(item)
"""
装饰器
    定义：
        装饰器是修改其他函数功能的函数
    作用：
        有助于代码更简短，且更Pythonic
    函数装饰器：
        函数包裹（嵌套）：
            函数内可以调用函数内包裹的函数，函数外不能调用被函数所包裹的函数.
        函数执行域传递：
            函数后面+()，表示执行函数；函数后面没有()，表示传递函数，可以赋值给变量而不是执行函数
        函数作参数传递：
            引文函数给以赋值给一个变量，将这个变量就可以作为实参传递给其他函数使用
        定义装饰器：
            封装一个函数，用来修改其他函数的行为。可以直接将被装饰函数作为参数传递给装饰器。也可以使用语法糖，
        直接在被装饰函数使用@<装饰器名>进行函数装饰
            但是function.__name__查看函数名称却不是执行函数的名称，需要使用functools.wraps装饰器进行处理
        functools.wraps装饰器作用
            @wraps接受一个函数进行装饰，并加入了赋值函数名称、文档、参数列表等功能。可以让我们在装饰器里面访问装饰之前的函数属性
        使用场景
            授权装饰器函数
            from functools import wraps
            def requires_auth(func):
                @wraps(func) 
                def decorated(*args, **kwargs):
                    auth = request.authorization
                    if not auth or not check_auth(auth.username, auth.password):
                        authenticate()
                    return func(*args, **kwargs)
                return decorated
            日志装饰器函数
            def login(func):
                @wraps(func)
                def with_logging(*args, **kwargs):
                    print(func.__name__ + "was called")
                    return func(*args, **kwargs)
                return with_logging
            @login
            def addition_func(x):
                return x + x
            result = addition_func(4)
        带参数的装饰器
            函数中嵌入装饰器, 参数传递就和普通函数一样
    类装饰器：
        函数装饰器通常处理事项比较简单，如果想要通过装饰器同时执行多个事项的时候，就要用到类装饰器。
    同时类装饰比嵌套函数更加整洁，而且包裹函数和函数装饰器语法一致
"""


# 函数包裹
def hi(name=None):
    print("now you are inside the hi() function")

    def greet():
        return "now you are inside the greet() function"

    def welcome():
        return "now you are inside the welcome() function"
    if name == "greet":
        return greet
    else:
        return welcome


local = hi("greet")
print(local)
print(local())


# 函数参数传递
def hello():
    return "this is hello function"


def doSthBeforeHello(func):
    print("I am doing some boring work before executing hello()")
    func()


doSthBeforeHello(hello)

from functools import wraps


# 第一个装饰器
def new_decorator(func):
    @wraps(func)
    def wrap_function():
        print("I am doing some boring work before executing a_func()")
        func()
        print("I am doing some boring work after executing a_func()")
    return wrap_function


@new_decorator
def function_requiring_decorator():
    print("I am the function which needs some decoration to remove my foul smell")


function_requiring_decorator()


# 带参数的装饰器
def logit(logfile="out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            log_string = func.__name__ + "was called" + logfile
            print(log_string)
            return func(*args, **kwargs)
        return wrapper_func
    return logging_decorator


@logit()
def func1():
    pass


func1()


@logit(logfile="func2.log")
def func2():
    pass


func2()


# 类装饰器
class logitc:
    def __init__(self, log_file="out.log"):
        self.log_file = log_file

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + "was called" + self.log_file
            print(log_string)
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        """
        logit只打印日志，不做其他动作
        :return:
        """
        pass


# 创建email子类，添加email功能
class email_logit(logitc):
    """
        logit实现版，可以在函数调用时发送邮件给管理员
    """
    def __init__(self, email="admin@qq.com", *args, **kwargs):
        self.email = email
        super().__init__(*args, **kwargs)

    def notify(self):
        """
        执行发送邮件的动作
        :return:
        """
        pass


@logitc
def func3():
    pass


"""
递归
    定义：
        直接或间接调用自身的函数就是递归。
        递归一定要控制递归的层数，当符合某一条件的时候要终止递归,如果没有终止条件，就会无限递归
        几乎所有递归都能用while实现
    优点：
        将问题简单化，思路更清晰，代码更简介
    缺点：
        递归深度过大时，可能会得到不可预知的结果
    递归函数
"""


def fx(n):
    print(f"递归第{n}层")
    if n == 3:
        print(f"执行第{n}层退出")
        return
    fx(n+1)


fx(1)
print("程序结束")


# 递归函数实现10以内数字累加
def mysum(x):
    if x <= 1:
        return 1
    return x + mysum(x-1)


v = mysum(10)
print(v)


"""
闭包
    定义：
        将内嵌函数语句和这些语句执行环境打包在一起，得到的对象就是闭包
    条件：
        必须有一个内嵌函数
        内嵌函数必须引用外部函数中的变量
        外部函数返回值必须是内嵌函数
    
"""
def make_power(y):
    """
    计算arg的平方
    :param y:
    :return:
    """
    def fx(arg):
        return arg ** y
    return fx


pow2 = make_power(2)
print(pow2(3))

