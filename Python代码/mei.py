import requests
from bs4 import BeautifulSoup
import urllib.request


x=0
def getImg():


    url = 'http://www.meizitu.com/a/5561.html'
    html = requests.get(url)
    html.encoding = 'gb2312'
    html2 = html.text

    soup = BeautifulSoup(html2,'html.parser')

    gril = soup.find_all('img')
    x=0
    for i in gril:
        imgsrc = i.get('src')
        urllib.request.urlretrieve(imgsrc,'./gril/%d.jpg'%x)
        x+=1
        print('正在下载第%d张图片'%x)

getImg()