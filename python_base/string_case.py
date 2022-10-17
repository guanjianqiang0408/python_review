"""
若干个字符的集合就是字符串
    字符串必须是双引号或单引号包围，例如
    "aaa" 或 'aaa'
反斜杠进行字符串转义
"""
print("abcd")
print("ab\rcd")

"""
格式化字符串
    使用转换符号。例如%s %d
    f-string方式格式
"""
print("name: %s" % "zhangfei")
print(f"name: {'liubei'}")