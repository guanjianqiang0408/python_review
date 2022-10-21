"""
面向对象
    定义：
        不同对象有不同特征，同一类对象总是有相似或相同特征

    面向过程与面向对象：
        面向过程是一种以事件为中心的编程思想，会将每个步骤差为小部分，然后逐步执行。当相似需求越来越多的时候，
    代码量就会越来越多，重复代码也越来越多。而且复杂场景下，是无法写出完整的面向过程代码
        面向对象的主要思想是以对象为主，将一个问题抽象出具体对象，并且将抽象出来的对象和对象的属性和方法封装为
    一个类（任何脱离面向过程空谈面向对象都是流氓）。面向对象本质上还是面向过程服务，因为计算机解决问题的方法永远
    都是面向过程。面向对象只是为了让程序看起来更符合人的思考方式

    类与对象：
        类是一组相关属性和行为的集合
        对象是类的实例，由类创造

    Python面向对象：
        类定义：
            class 关键字定义类，后面跟着类名，类名通过首字母大写，紧跟着是(object),表示该类从那个类集成下来的。
        类中的函数称为类方法
            class Person(object):
                def function():
                    pass

        创建对象
            person = Person() person是Person类的实例对象

        对象属性
            class Person(object):
                def __init__(self, name, gender):
                    self.name = name
                    self.gender = gender

                def talk(self):
                    print(f"My name is {self.name}, gender is {self.gender}")

            __init__() 是一个特殊方法，创建对象时进行初始化操作，自动执行，第一个参数永远是self，代表实例本身

            xiaoming = Person("小明", "男")
            print(xiaoming.name)
            print(xiaoming.talk())

            对象实例可以依据对象属性和方法无限创建

        self是什么：
            self不是关键字，在类中，可以不用self而使用其他名字，命名self只是程序员之间的一种约定习惯，遵守约定，可以
        使编写的代码具有更好的可读性。

            self在类中表示对象本身。类的内部通过self访问自己内部的属性和方法

            # 这个类中，self表示一个类范围内的全局变量，在这个类中任何方法中，都能访问self绑定的变量，同时也能访问self绑定的行数
            class Person(object):
                def __init__(self, name, gender):
                    self.name = name
                    self.gender = gender
                    self.talk() # 访问self绑定的方法

                def talk(self): # 参数为self，这个函数是对象的方法
                    print(self.name)

    面向对象的三大特性
        封装：
            将客观事物封装成抽象的类，隐藏属性和方法实现细节，仅对外公开接口
            封装可以把计算机中的数据跟操作这些数据的方法组装在一起，封装在一个模块中，也就是一个类中

            class Box():
                def open_door():
                    pass

                def close_door():
                    pass

        继承：
            子类可以使用父类所有功能，并且对这些功能进行拓展。继承的过程就是从一般到特殊的过程。
            继承简单说就是一种层次模型，这种层次模型能够被重用。层次结构的上层具有通用性，但是下层结构则具有特殊性。在继承的过程中
        类则可以从最顶层的部分继承一些方法和变量。类除了可以继承以外同时还能够进行修改或者添加。通过这样的方式能够有效提高工作效率。
            继承一个父类是单一继承，继承多个父类是组合继承，同时用用多个父类的方法和属性，如果多个父类有相同的方法，调用顺序是按照继承参数
        的顺序调用，谁排在第一个就调用谁的方法

            单一继承
                class Father:
                    def talk():
                        print("我会说明)

                    def breathe():
                        print("我会呼吸")

                class Me(Father):
                    pass

                me = Me()
                me.talk()
                me.breathe()

            组合继承
                class Father:
                    def talk_english():
                        print("我会说英语")

                class Mother:
                    def talk_chinese():
                        print("我会说中文")

                class Me(Father, Monther):
                    pass

                me = Me()
                me.talk_english()
                me.talk_chinese()

        多态：
            多态指的是一类事物有多种形态（一个抽象类有多个子类，因而多态的概念依赖继承）

            class Father:
                def talk(self):
                    print("我会说中文")

            class Me(Father):
                def talk(self):
                    print("我会说英语")

            class Son(Father):
                def talk(self):
                    print("我会说俄语")

            Father().talk()
            Me().talk()
            Son().talk()

            多态存在的三个必要条件
                要有继承
                要有重写
                父类引用指向子类对象

    属性访问权限：
        如果想让内部属性不被外部访问，可以把属性名前加上两个下划线，Python中，实例变量名如果以双下划线开头，
    就变成了私有变量，只有内部可以访问，外部无法访问

        前置单下划线_xx
            前置单下划线只有约定含义。对python解释器没有特殊含义, 外部可以正常访问
            class Person:
                def __init__():
                    self._name = ""

        前置双下划线__xx
            实例变量名如果双下划线开头，就变成了私有变量，只有内部可以访问，外部不能访问,如果想要访问需要使用这种格式p._Person()__name，
        但是不建议这样实现
            class Person:
                def __init__():
                    self.__name = ""

    内置的特殊方法
        __xxx__ 前后均有双下划线的方法是python内置的特殊方法

        __init__(self)
            该方法在类的一个对象被创建时，自动执行，不需要调用，可以使用该方法操作实例化对象进行初始化操作，相当于构造函数。
        向类中传递参数，就在这个函数接收，并且该防范只能返回None，不能返回其他对象
            class Person:
                def __init__(self, name):
                    self.name = name

        __new__(cls, *args, **kwargs)
            该方法在__init__()之前调用，是真正的类构造方法，用于产生实例化对象。该方法必须返回一个对象，该防范产生一个
        实例化对象，然后我们实例对象才会调用__init__()方法进行初始化


        __init__ 和 __new__ 区别
            1. __init__ 通常用于初始化一个新实例，控制初始化过程，例如添加属性，做其他操作，发生在类实例被创建完以后
        它是实例级别的方法
            2.__new__ 通常用于控制生成一个新实例的过程。它是类级别的方法，这个方法产生的实例其实也就是__init__中的self

        __del__(self)
            析构方法，当对象在内存中被释放时，自动触发此方法，通常用来清理工作。
            此方法一般不需要定义，因为python自带内存分配和释放机制，除非需要在释放的时候指定一些动作。析构函数的调用是由
        解释器在进行垃圾回收时自动触发执行

        __call__(self, *args, **kwargs)
            该方法不是内置方法，需要我们实现这个方法。 如果类中实现了这个方法，该类的实例就可以被执行，执行的就是这个方法
            class Person:
                def __init__():
                    pass
            p = Person()
            p() # 抛出异常，类对象不可调用

            通过__call__使类对象可调用
            class Person:
                def __init__():
                    pass

                def __call__():
                    pass
            p = Person()
            p() # 可以直接调用类的对象，因为类实现了__call__(),调用的就是实现的__call__()

        __str__(self)
            该方法返回对象的字符串表达式
                str()方法可以将一个对象转换为字符串。实际上，执行的就是对象的__str__()方法
            class Person:
                def __init__():
                    pass

                def __str__(self):
                    return ""
            该方法主要是用于str(对象)的时候，返回一个字符串

        __repr__(self)
            该方法作用和str()很像，两个函数都是将一个实例转成字符串。不同的是，使用场景不同
            __str__ 更侧重展示。所以当我们print输出给用户或使用str函数进行类型转换时，Python会默认优先调用__str__函数
            __repr__更侧重实例报告，除了实例当中的内容外，往往还会附加类相关信息，因为这些内容都是给开发者看的
            class Person:
                def __init__():
                    pass

                def __str__():
                    return ""

                def __repr__():
                    return ""

            p = Person()
            print(p) # my name is baozi age is 20
            print(repr(p)) # Person("baozi", 20)

        __eq__
            该方法判断两个对象的值是否相等
            class Person:
                def __init__():
                    pass

                def __eq__(self, other):
                    return self.__dict__ == other.__dict__

            p1 = Person(23)
            p2 = Person(20)
            print(p1 == p2) # 判断两个独享是否相等，触发__eq__函数

            其他比较方法
                __lt__() 大于
                __gt__() 小于
                __le__() 大于等于
                __ge__() 小于等于
                __eq__() 等于
                __ne__() 不等于

        __getitem__()  __setitem__()  __delitem__()
            它们是字典取值、赋值、删值的方法，它们并不是内置方法
            class Person:
                def __init__():
                    pass

                def __getitem__(self, key)
                    return ""

                def __setitem__(self, key, value):
                    return ""

                def __delitem__(self, key):
                    return ""

            p = Person()
            p["name"] = "zhangfei"
            p["name"]
            del p["name"]
            这样定义的类就可以实现字典的功能了

        __setattr__() __delattr__() __getattribute__()
            操作对象属性的方式，取值、赋值、删除，这三个属性是内置方法，通常不需要重写
            class Person:
                def __init__(self):
                    pass

                def __getattribute__(self, key):
                    return ""

                def __setattr__(self, key):
                    return ""

            p = Person()
            p.name = "zhangsan"
            print(p.name)
            del p.name

        __getattr__
            该方法和__getattribute__()类似，取值时候调用，但有前置条件：只有当访问不存在属性时，调用它。__getattribute__在
        访问任意属性都被调用
            class Person:
                def __init__(self):
                    pass

                def __getattr__(self, key):
                    return ""

            p = Person()
            p.name # 访问不存在属性，调用__getattr__方法

    内置特殊属性
        __slots__

        __dict__

        __doc__

        __class__

        __module__

    内置装饰器
        @property

        @staticmethod

        @classmethod


    理解OOP，总结


        https://zhuanlan.zhihu.com/p/437925568
"""