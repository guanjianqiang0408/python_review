"""
列表
定义：
    一组数据存储到一起，通过下标获取指定元素的容器就是列表
创建：
    l = [1, 2, 3]
    l = list()
    l = []
访问元素：
    l[index]
    l[start: end: step]
删除：
    删除列表 del list 默认python会自动回收，如果手动回收后再调用该变量则会报错: name "l" is not defined
元素操作：
    翻转：
        reverse() 翻转列表元素
        list[::-1] 翻转列表元素
    添加元素
        append() 末尾添加元素
        extend() 追加另外一个元组或列表
        insert(index, value) 指定位置添加元素
    删除元素
        del list[index] 删除指定下标位置的元素
        del list[start: end] 删除指定区间的元素
        pop(index) 如果给定索引则删除指定索引元素，未指定则末尾删除
        remove(value) 删除指定值的元素
        clear() 清空所有元素
    修改元素
        list[index] = value 修改指定索引的元素
        list[start: end] = [v1, ..., vn] 修改指定索引区间的元素,区间值和修改值元素个数要一致
    查找元素
        index() 元素在列表中出现的位置
        count() 元素在列表中出现的个数

"""
l = list(range(4))
print(l)
print(l[2])
print(l[0:3:2])
del l
# 添加元素
list = list(range(2))
print(list)
list.append(3)
print(list)
list.extend([4, 5])
print(list)
list.insert(0, 6)
print(list)
print(list[::-1])
# 删除
del list[0]
del list[0:2]
print(list)
list.pop(0)
print(list)
list.remove(4)
print(list)
list.clear()
print(list)
list.extend([0, 1, 2, 3])
print(list)
list.pop()
print(list)
# 修改
list[0] = 1
print(list)
list[0:3] = [0, 1, 2, 3]
print(list)
