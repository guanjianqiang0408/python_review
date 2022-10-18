"""
 条件语句
"""
age = int(input("please input your age"))
if age > 100:
    assert "input age error"
if age > 80:
    print("old man")
elif age < 20:
    print("child man")
else:
    print("younger man")

"""
assert 断言，如果为真继续执行，否则抛出异常
"""