"""
GUI定义：
    图形用户界面（Graphical User Interface，简称 GUI），是计算机图形学技术的一种，它一般由窗口、下拉菜单或者对话框等图形化的控件组成。
    用户通过点击菜单栏、按钮或者弹出对话框的形式来实现与机器的交互，GUI 的存在拉近了人与计算机的的距离，让人机交互的过程变得简单舒适、有温度

GUI工具：
    Tkinter
    wxPython
    PyQ
    PyGTK
    Pywin32

Tkinter定义：
    Tkinter（即 tk interface，简称“Tk”）本质上是对 Tcl/Tk 软件包的 Python 接口封装，它是 Python 官方推荐的 GUI 工具包，
    属于 Python 自带的标准库模块，当您安装好 Python 后，就可以直接使用它，而无须另行安装

创建Tkinter程序
    导入 tkinter 模块
    创建主窗口，也称 root 窗口（即根窗口）
    添加人机交互控件，同时编写相应的事件函数
    通过主循环（mainloop）来显示主窗口

创建Tkinter组件
    常用控件及属性
    主窗口及属性
    Lebel控件
    Button控件
    Entry控件
    Text控件
    列表、组合框控件
    单选、多选框控件
    Scale控件
    Canvas画布控件
    Menu控件
    Scrollbar控件
    Event控件
    布局管理方法
    布局管理控件
    对话框控件

案例
    数字时钟



"""
# 创建tk示例

# import tkinter as tk
# # 创建主窗口
# root_window = tk.Tk()
# # 给主窗口起名字
# root_window.title("第一个tk工具")
# # 设置窗口大小
# root_window.geometry("450x300")
# # 设置主窗口背景颜色
# root_window["background"] = "#C9C9C9"
# # 添加文本内，设置字体前景色和背景色，字体类型和大小
# text = tk.Label(root_window, text="初学者，欢迎您", bg="yellow", fg="red", font=("Times", 20, "bold italic"))
# # 将文本内容放置主窗口内
# text.pack()
# # 添加按钮，按钮文本，并通过command参数设置关闭窗口的功能
# button = tk.Button(root_window, text="关闭", command=root_window.quit)
# # 将按钮放置在主窗口库内
# button.pack(side="bottom")
# # 启动循环，让窗口处于显示状态
# root_window.mainloop()


# 时钟案例
from tkinter import *
from time import strftime

root = Tk()
root.geometry("500x350+300+300")
root.title("自制时钟")

# 设置文本标签
lb = Label(root, font=("微软雅黑", 50, "bold"), bg='#87CEEB', fg="#B452CD")
lb.pack(anchor="center", fill="both", expand=1)

# 定义一个mode标志
mode = "time"


# 定义显示事件的函数
def showtime():
    if mode == "time":
        # 格式化时间
        string = strftime("%H:%M:%S %p")
    else:
        string = strftime("%Y-%m-%d")
    lb.config(text=string)
    # 每隔1秒执行一次showtime函数
    lb.after(1000, showtime)


# 定义鼠标处理时间，点击切换日期样式显示
def mouseClick(event):
    global mode
    if mode == "time":
        # 点击切换mode样式为日期样式
        mode = "date"
    else:
        mode = "time"


lb.bind("<Button>", mouseClick)
showtime()
# 显示窗口
mainloop()

