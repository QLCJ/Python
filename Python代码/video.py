import requests
import re
from lxml import etree
from urllib.request import urlretrieve
from time import sleep

def download(url):
    # url = 'http://www.pearvideo.com/category_9'

    #获取页面的源代码
    html = requests.get(url).text
    #把文本文件处理成可以解析的对象
    html = etree.HTML(html)
    # // 表示获取这个页面所有的div   @ 表示获取属性
    # 获取这个页面所有的div下的class下的a的href的属性   加""是因为ver...是属性
    video_id = html.xpath('//div[@class="vervideo-bd"]/a/@href')

    #列表
    video_url = []
    starturl = 'http://www.pearvideo.com'
    #
    # #拼接完整的url
    # # id为每一个id
    for id in video_id:
        newurl = starturl + '/'+ id
        video_url.append(newurl)

    #获取视屏播放地址
    for playurl in video_url:
        #获取页面源代码
        html = requests.get(playurl).text
        # 正则匹配   (.*?) 匹配所有
        req = 'srcUrl="(.*?)"'
        #视屏的播放地址 所有的url地址
        purl = re.findall(req,html)
        print(purl)

        # 获取所有的视频名称
        req = '<h1 class="video-tt">(.*?)</h1>'
        videoname = re.findall(req,html)
        videoname2 = re.sub(r'\？|\?|\/|\：|\||\*|\"|\<\>|\！|\:', "",videoname[0])
        print("正在下载视频：%s"%videoname2)
        # 下载的url   下载地址
        urlretrieve(purl[0],'./video/%s.mp4'%videoname2)


#download()


#http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=36
#http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=48


def downloadmore():
    n = 12
    while True:
        if n >48:
            # 跳出循环
            break
        else:
            url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=%d"%n
        n+=12
        sleep(1)
        download(url)


downloadmore()