#!/bin/env python3

import urllib.request
import json
import string

print('++++++联网使用，仅供娱乐+++++++')

if __name__=='__main__':
    while True:
        target=r'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
        print('---------------------------------')
        key_word=input('想聊点什么？')
        if key_word == 'exit' or key_word == '退出':
            print('再见～')
            x=input('按任意键退出')
            break
        else:
            tmp=target+key_word
            url=urllib.parse.quote(tmp,safe=string.printable)
            print(url)
            page=urllib.request.urlopen(url)

            # 此处非常重要，ignore表示忽略非法字符，否则出现非法字符会导致报错
            html=page.read().decode("utf-8",'ignore')

            res=json.loads(html)
            print(res['content'])
