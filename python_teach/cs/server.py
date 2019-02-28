#!/usr/bin/env python3

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))

#监听端口，参数为最大链接数
s.listen(5)
print("waiting for connection...")

while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=())


    print("accept new connection from %s:%s..." % addr)

