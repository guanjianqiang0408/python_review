"""
生成器
    生成器是一种迭代器，拥有next方法并且行为和迭代器相同，都可以用于for循环
创建
    两种方式创建生成器
     -生成器函数
        如果一个函数内出现yield关键字，该函数就是生成器函数，调用生成器函数就会得到一个生成器
     -生成器表达式
"""


# 生成器函数
def cus_generator(n):
    index = 0
    while index < n:
        yield index
        index += 1


generator = cus_generator(5)
print(type(generator))
for i in generator:
    print(i)
"""
迭代器

装饰器

闭包

递归

"""
