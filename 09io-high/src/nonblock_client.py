import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("127.0.0.1", 9655))
server.setblocking(False)
while True:
    try:
        msg = server.recv(100) #BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
    except BlockingIOError as e:
        print("做些别的")
    else:
        print(msg)
        break

