import requests  #获取网页数据模块
from bs4 import BeautifulSoup   #解析heml标签文档
import urllib.request   #打开或获取网页数据，urllib,request,urlretrieve下载网络数据到本地


x=0
def getImg(page = 1):


    response = requests.get('https://www.dbmeinv.com/dbgroup/show.htm?cid=4&pager_offset={}'.format(page))
    html = response.text   #获取网页源代码，数据类型为str字符串

    soup = BeautifulSoup(html,'html.parser')  #解析html，解析结果soup数据类型为bs4.BeautifulSoup对象

    gril = soup.find_all('img')   #gril类型为ResultSet,就是列表

    for i in gril:   #i为gril列表中的一项，实际为一个<img>标签内容
        global x
        imgsrc = i.get('src')  #筛选提取每个<img>标签中的“src”属性值
        urllib.request.urlretrieve(imgsrc,'./gril/%s.jpg'%x)   #下载图片到geil文件夹下
        x+=1
        print('正在下载第%d张图片'%x)

for i in range(1,11):   #设置下载页数
            print('正在下载第{}页图片'.format(i))
            getImg(i)