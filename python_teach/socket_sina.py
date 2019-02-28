#!/user/bin/env python3

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))   #参数为元组

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接受数据
buffer=[]
while True:
    #每次最多接受１K
    ｄ=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data=b''.join(buffer)

s.close()

header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#把接受的数据写入文件
with open('sina.html','wb') as f:
    f.write(html)

        
            