#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header


msg=MIMEText('你好,python...','plain','utf-8')

#输如ｅｍａｉｌ地址和口令
#from_addr=input("From: ")
#passwd=input('Password: ')
#to_addr=input('To: ')
from_addr='gaofeng4280@163.com'
to_addr='1071380275@qq.com'
smtp_server='smtp.163.com'

passwd=input('Password: ')

#smtp_server=input('SMTP server: ')


server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr,[to_addr],msg.as_string())

server.quit()