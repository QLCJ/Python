import requests
from bs4 import BeautifulSoup
from tkinter import *
from urllib.request import urlretrieve
# 获取页面源代码
# 获取ID
# 下载音乐
def download_song():
    # 获取用户输入的URL
    url=entry.get()
    # url='https://music.163.com/song/media/oouter/url?id='
    # 获取源代码
    # https://music.163.com/discover/toplist?id=19723756'
    # 请求头
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    res=requests.get(url,headers=header).text
    # 创建对象 解析网页
    r=BeautifulSoup(res,'html.parser')
    #获取ID
    #song_url = 'https://music.163.com/song/media/outer/url?id=%s'
    music_dict={}
    result=r.find('ul',{'class','f-hide'}).find_all('a')
    # print(result)
    for music in result:
        music_id=music.get('href').strip('/song?id=')
        # print(music_id)
        music_name=music.text
        music_dict[music_id]=music_name
        # print(music_dict)
    for song_id in music_dict:
         song_url = 'https://music.163.com/song/media/outer/url?id=%s'%song_id
         # 下载的路径
         path='D:\\songs\\%s.mp3 '%music_dict[song_id]
    #    添加数据
         text.insert(END,'正在下载：%s'%music_dict[song_id])
    #   文本框向下滚动
         text.see(END)
         text.update()
         urlretrieve(song_url,path)
# 创建窗口
windows=Tk()
#窗口标题
windows.title("网易云音乐")
# 窗口大小  位置
windows.geometry('550x400+450+250')
# 标签控件
label=Label(windows,text='请输入要下载的歌单URL',font=('华文行楷',10))
# 定位 grid 网格式布局
label.grid()
#
entry=Entry(windows,font=('微软雅黑',10))
entry.grid(row=0,column=1, )
# 列表框控件
text=Listbox(windows,font='微软雅黑,10',width=54,height=15)
text.grid(row=1,columnspan=2)
# 点击方式
btn=Button(windows,text='开始下载',font=('微软雅黑,10'),command=download_song)
# sticky方式
btn.grid(row=2,column=0,sticky=W)
but1=Button(windows,text='退出',font=('微软雅黑,10'),command=windows.quit)
but1.grid(row=2,column=1,sticky=E)
# 显示窗口，消息循环
windows.mainloop()
# 搭建界面