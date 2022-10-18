"""
IO 输入输出
读取键盘输入
    raw_input() 读取行，返回字符串
    input() 读取行，返回字符串，可以接收一个python表达式并将运算结果返回
打开、关闭文件
    open(filename, mode, code) 打开文件
        filename 文件路径
        mode  打开文件模式
        code 打开文件编码格式
    close() 关闭文件
File 对象属性
    closed 判断文件是否关闭
    mode   打开文件访问呢模式
    name    返回文件名称
    softspace   如果用print输出，后必须跟一个空格符

文件操作
    write() 写入文件，可以是二进制，而不是仅仅是文字
    read()  读取文件

文件定位
    tell() 返回文件内当前所处位置
    seek(offset, from) 改变当前文件位置 offset表示移动字节数，from指定开始移动字节的参考位置
文件操作
    rename(current_file_name, new_file_name) 重命名
    remove(file_name) 删除文件
操作目录
    Python通过os模块进行目录操作
    mkdir() 创建目录
    chdir() 改变当前目录
    getcwd() 获取当前目录
    rmdir() 删除目录

"""
print(input("Your name"))
file = open("test.txt", "r", encoding="utf-8")
print(file.read())
# file.close()
# file.write("aaaaa")
file.read()
file.close()