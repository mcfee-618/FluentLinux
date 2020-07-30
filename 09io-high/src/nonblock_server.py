import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9655))
server.listen(10)
while True:
    new_socket,address=server.accept()
    print(address)
    new_socket.send(bytes("22".encode("utf-8")))
    new_socket.close()