import requests,re,os

def getXiaUrl(url):
    #url = "https://www.meitulu.com/t/xiameijiang/"
    r = requests.get(url)
    reg=re.compile('<a href="(.*?)" target="_blank"><img')
    urls = re.findall(reg,r.text)
    return urls

def get_img(urls):
    for u in urls:
        imgid = u.split('/')[-1][:-5]
        for i in range(1,50):
            imgurl = "https://mtl.ttsqgs.com/images/img/{}/{}.jpg".format(imgid,i)
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
                    'Referer':'https://www.meitulu.com/img.html?img='+imgurl}
            r = requests.get(imgurl,headers=headers)
            path = "./mm/"+imgid+'/'
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path+imgurl.split('/')[-1],'wb') as ff:
                ff.write(r.content)

def main():
    urls_list={'https://www.meitulu.com/item/12984.html'}
    for url in urls_list:
        get_img(getXiaUrl(url))

if __name__ == '__main__':
    main()
