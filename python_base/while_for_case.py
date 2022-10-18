"""
while 循环
"""
count = 1
while True:
    if count == 3:
        # 结束循环
        break
    print(count)
    count += 1

"""
for 循环
"""
for item in range(4):
    if item == 1:
        # 占位符，什么都不做
        pass
    if item == 2:
        # 跳过当前，继续执行
        continue
    print(item)
