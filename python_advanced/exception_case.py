"""
什么是异常：
    程序运行过程中发生的事件，影响了程序正常执行。当发生时，我们需要捕获，否则
程序就会终止执行
python提供了两个重要的功能处理运行中的异常
异常处理
    捕获异常，使用try...except...语句，检测try中的错误，让except捕获异常
信息并处理
    try工作原理： 开始一个try，python就在上下文中做标记，当异常发生的时候
回到try语句
    如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
    如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
    如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
断言
    如果结果为False，终止程序执行抛出异常。如果结果为True，程序继续执行
自定义异常
    通过创建一个新的异常类，程序可以命名他们自己的异常，通过直接或间接的方式继承Exception

"""
try:
    pass
except:
    assert RuntimeError("运行中发生了错误")
finally:
    pass


# 自定义异常
class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args

try:
    pass
except CustomException:
    assert CustomException("自定义异常")

