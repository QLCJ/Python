import requests
import time
import random
import re
import os


# 访问主页URL
# 找到并循环所有分类
# 创建分类文件夹
# 访问分类的URl
# 找到页码构建循环分类所有页，  循环页面内的所有的图集
# 创建图集文件夹，  找到图集内所有的图片URL，   保存到对应的文件夹


def new_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    new_title = re.sub(rstr,"_",title)
    return new_title

url = 'http://www.meizitu.com/'
html = requests.get(url)
html.encoding = 'gb2312'
infos = re.findall(r'a href="(http://www.meizitu.com/.*?html)"  target="_blank" title="(.*?)"',html.text)
i=1
for sor_url,sor in infos:
    sor = new_title(sor)
    path = 'G://meizitu/%s/'%sor
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    time.sleep(random.random())
    sor_html = requests.get(sor_url)
    sor_html.encoding = 'gb2312'
    atlas = set(re.findall(r"<li><a href='(。*?html)'>\d+</a></li>",sor_html.text))
    atlas_lis = []
    atlas_lis.append(sor_url)
    atlas_lis += [url+'a/'+x for x in list(atlas)]
    for atla in atlas_lis:
        atla_html = requests.get(atla).text
        at_url_list = re.findall(r'h3 class="tit"><a href="(http://www.meizitu.com/.*?html)"  targe',atla_html)
        for at_url in at_url_list:
            at_html = requests.get(at_url)
            at_html.encoding = 'gb2312'
            atlas_title = ''.join(re.findall(r'<title>(.*?)</title>',at_html.text))
            atlas_title = new_title(atlas_title)
            img_path = 'G://meizitu/%s/%s/'%(sor,atlas_title)
            if os.path.exists(img_path):
                pass
            else:
                os.mkdir(img_path)
            img_urls = re.findall(r'src="(http://mm.chinasareview.com/.*?jpg)" /><br />', at_html.text)
            k=1
            for img_url in img_urls:
                header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
                data = requests.get(img_url,headers= header).content
                print(img_url)
                # with open('%s%s'%(img_path,img_url.split('/')[-1]),'wb') as f:
                #     f.write(data)
                # print("正在下载 {%s}的第%d张图片，一共下载了%d张图片"%(atlas_title,k,i))
                # i +=1
                # k +=1