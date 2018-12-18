import requests
from bs4 import BeautifulSoup
import urllib.request


x=0
def getImg(page = 1):


    response = requests.get('https://www.dbmeinv.com/dbgroup/show.htm?cid=4&pager_offset={}'.format(page))
    html = response.text

    soup = BeautifulSoup(html,'html.parser')

    gril = soup.find_all('img')

    for i in gril:
        global x
        imgsrc = i.get('src')
        urllib.request.urlretrieve(imgsrc,'./gril/%s.jpg'%x)
        x+=1
        print('正在下载第%d张图片'%x)

for i in range(1,11):
            print('正在下载第{}页图片'.format(i))
            getImg(i)