import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("127.0.0.1", 9999))

print("bind udp on 9999")

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print(f"received from {addr}: {addr}")
    s.sendto(b"hello: " + data, addr)
