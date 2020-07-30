# coding:utf-8
"""
@author: mcfee
@description:
@file: select_server.py
@time: 2020/7/30 下午2:29
"""
import select, socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9655))
server.listen(10)
server.setblocking(False)
read_ls = [server]
write_ls =[]
while True:
    # 阻塞在这里
    r_l, w_l, x_l = select.select(read_ls, write_ls, [])
    for r in r_l:
        if r == server:
            new_socket, address=r.accept()
            read_ls.append(new_socket)
        else:
            value = r.recv(100)
            write_ls.append(r)
            r.send(bytes("已收到".encode("utf-8")))
            read_ls.remove(r)
    for w in w_l:
        print("wwww")
        w.close()
        write_ls.remove(w)


