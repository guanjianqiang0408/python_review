import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(("127.0.0.1", 9999))
s.listen(5)
print("waiting for connection")


def tcplink(sock, addr):
    print(f"accept new connection from {addr}: {addr}")
    sock.send(b"welcome")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print(f"connection from  {addr}: {addr}closed")


while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程处理TCP链接
    t = threading.Thread(target=tcplink, args=(sock, addr,))
    t.start()

