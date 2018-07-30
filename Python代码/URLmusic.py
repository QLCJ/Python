from tkinter import *
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


#爬取网易云音乐
def downlaod_song():
    # 获取用户输入的URl
    url = entry.get()
    # url = 'https://music.163.com/playlist?id=2269661190'
    # http://music.163.com/song/media/outer/url?id=543710263
    # https://music.163.com/playlist?id=2269661190
    # 获取页面源代码  若无.text则值获取到状态码
    # 请求头 模拟浏览器访问服务器
    header = {
        'Host':'music.163.com',
        'Referer':'https://music.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    }
    res = requests.get(url,headers = header).text
    #创建对象  解析网页     lxml 也可以
    r = BeautifulSoup(res,"html.parser")
    # print(type(r))


    # 获取ID
    music_dict = { }
    result = r.find('ul',{'class','f-hide'}).find_all('a')
    # print(result)
    for music in result:
        music_id = music.get('href').strip("/song?id=")
        music_name = music.text
        # 拼接
        music_dict[music_id] = music_name
    # print(music_dict)

    for song_id in music_dict:
        song_url = "http://music.163.com/song/media/outer/url?id=%s"%song_id
        # 下载路径                        根据ID获取音乐名称
        path = r"D:\PHPprogram\text\music\%s.mp3"%music_dict[song_id]

        # 添加数据
        text.insert(END,"正在下载：%s"%music_dict[song_id])
        # 文本框向下
        text.see(END)
        # 更新
        text.update()
        # 下载地址           下载路径
        urlretrieve(song_url,path)



# 创建窗口
root = Tk()
# 窗口的标题
root.title("网易云音乐")
# 窗口的大小   用小写的x连接
root.geometry("550x400")
# 窗口的位置   两个使用同一个函数所以前面有个加号  ("550x400+540+230")
root.geometry("+550+230")
# 标签控件
label = Label(root,text = "请输入要下载的歌单URL:",font = ('宋体',10))
# label 定位  grid 网格式布局 pack 包    place 位置
label.grid(row = 0,column= 0)
# 输入框
entry = Entry(root,font = ('微软雅黑',25))
entry.grid(row = 0,column = 1)


# 列表框控件
text = Listbox(root,font = ('微软雅黑',15),width =45,height = 10)
# columnspan 组件可跨越的列数
text.grid(row = 2,columnspan = 2)
# 点击按钮
button = Button(root,text = "开始下载",font = ('微软雅黑',15),command = downlaod_song)
# sticky 对齐方式  E W S N
button.grid(row = 3,column = 0,sticky = W)
# command 点击触发的方法
button2 = Button(root,text = "退出",font = ('微软雅黑',15),command = root.quit)
button2.grid(row = 3,column = 1,sticky = E)

# 显示窗口
root.mainloop()




