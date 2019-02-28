#!/usr/bin/env python3

import urllib.request
#from urllib.request import Request 


def handler_proxy():
    proxy_handler = urllib.request.ProxyHandler({'http': 'https://www.jianshu.com/p/d4ebace4ddcf'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        print("status: ", f.status, f.reaseon)


if __name__=="__main__":
    handler_proxy()