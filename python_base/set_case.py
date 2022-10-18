"""
集合
    元素不重复，元素只能是不可变数据类型
创建
    s1 = {}
    s1 = set()
元素访问
    循环遍历
删除
    del 删除堆栈中的指向
添加元素
    add() 添加元素
    remove() 删除元素
    s1 & s2 取两个集合公共元素
    s1 | s2 取两个集合全部元素
    s1 - s2 取一个集合中另一个集合没有的元素
    s1 ^ s2 取两个集合中都没有的公共元素
方法
   add() 添加元素
   clear() 清空元素
   copy() 复制集合
   difference() 差集
   pop() 删除元素
   remove() 删除元素
   update() 添加元素
"""
s1 = {1, 2}
s2 = {1, 3}
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)