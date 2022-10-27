"""
    定义
        计算机网络就是把各个计算机连接到一起，让网络中的计算机可以互相通信。网络编程就是如何在程序中实现两台计算机的通信。
        更确切地说，网络通信是两台计算机上的两个进程之间的通信

    TCP/IP简介
        为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，
        互联网协议簇（Internet Protocol Suite）就是通用协议标准。有了Internet，任何私有网络，只要支持这个协议，就可以联入互联网。
        因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议

    TCP编程
        Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
        而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

        客户端
            大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器
            TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
            例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端

        服务端
            服务器进程首先要绑定一个端口并监 听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，
            随后的通信就靠这个Socket连接了。一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
            服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接。
            每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接

            连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接

    UDP编程
        TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
        使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
        虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

        指定socket类型是SOCK_DGRAM, 绑定端口和TCP一样，但是不需要listen()方法，而是直接接收来自任何客户端的数据
        recvfrom()方法返回数据和客户端的地址和端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发送给客户端
        客户端使用UDP，创建UDP的socket，然后不需要调用connect，直接通过sendto()给服务器发数据，从服务器接收数据仍然调用recv()方法
        服务器绑定UDP端口和TCP端口不冲突，也即是各自绑定
"""

# TCP
import socket
# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立链接
s.connect(("www.sina.com.cn", 80))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据
buffer = []
while True:
    # 每次最多接收1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b"".join(buffer)
print(data)

# 关闭链接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode("utf-8"))
# 将接收数据写入文件
with open("sina.html", "wb") as f:
    f.write(html)
