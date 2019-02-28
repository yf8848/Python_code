import requests
from bs4 import BeautifulSoup
import os
import urllib
import re
from multiprocessing import Pool
import sys
import chardet
from chardet import detect

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Referer": "https://www.meitulu.com/"}

def run(all_url, b):

    start_html = requests.get(all_url, headers=headers)
    e = chardet.detect(start_html.content)['encoding']
    start_html.encoding = e
    Soup = BeautifulSoup(start_html.text, 'lxml')
    all_a = Soup.find('ul', class_='img').find_all('li')
    path = Soup.find('title').text.replace('/','-')




    if not os.path.exists("meitulu/"):
        os.makedirs("meitulu/")
        os.chdir("meitulu/")


    for l in all_a:
        a = l.a
        init = 0
        file_count = 0
        folder_count = 0

        if (a.find('img') == None):
            continue

        else :

            href = a["href"]
            elem = a.img['src']
            number = a.img['alt'].replace('/','-')



            if not os.path.exists("meitulu/"  + number):
                os.makedirs("meitulu/" + number)
                file_count = 0

            else:

                files = next(os.walk("meitulu/" + number))[2]
                file_count = len(files)



            ext = a.next_sibling.next_sibling.text
            start_index = ext.find('(') - 4
            max_span = int(ext[start_index:(start_index+2)])




            if (file_count == max_span):
                continue




            if (file_count == 0): init = 1
            else: init = file_count


            html = requests.get(href, headers=headers, allow_redirects=False)
            n = chardet.detect(html.content)['encoding']
            html.encoding = n
            u = urllib.urlopen(href)
            html_Soup = BeautifulSoup(html.text, 'lxml')




            for page in range(init, max_span + 1):
                page_url = elem[:-5] + str(page) + ".jpg"
                img_html = requests.get(page_url, headers=headers, allow_redirects=False)

                name = number + '-' + str(page)
                print("Downloading:" + page_url)
                os.chdir("meitulu/" + number)
                f = open(name+'.jpg', 'ab')
                f.write(img_html.content)
                f.close()



    if (b == True):
        pages_footer = Soup.find('div', class_='text-c')
        if not (pages_footer == None):
            num_page = int(pages_footer.find_all('a')[-2].get_text())
            for k in range(2, num_page + 1):
                run(all_url + str(k) + '.html', True)

urls = {'https://www.meitulu.com/t/qingdouke/'}


pool = Pool(processes=30)
for url in urls:
    pool.apply_async(run, args=(url, True))

pool.close()
pool.join()
print('finish download.')