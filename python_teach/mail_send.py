from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,'UTF-8').encode(), addr))

from_addr='gaofeng4280@163.com'
to_addr='1071380275@qq.com'
smtp_server='smtp.163.com'

passwd=input('Password: ')

msg=MIMEText('hello, send by Python...','plain','utf-8')
msg['From']=_format_addr('Python 爱好者<%s>' % from_addr)
msg['To']=_format_addr('开发者<%s>' % to_addr)
msg['Subject']=Header('来自ＳＭＴＰ的邮件...','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login()
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

