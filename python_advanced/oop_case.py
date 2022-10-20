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
                https://zhuanlan.zhihu.com/p/437925568
"""