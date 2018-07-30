import requests
from bs4 import BeautifulSoup
import urllib.request
import os
from tkinter import *
from tkinter import messagebox
import six
import threading
#123
x=0
root=Tk()


def photo():

    def photo_get(page=1):

        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        url='https://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset={}'.format(page)
        response=requests.get(url,headers=header)
        html=response.text
        soup=BeautifulSoup(html,'html.parser')
        girl=soup.find_all('img')


        for i in girl:
            global x
            imgpath=i['src']
            title=i['title']
            path='image'
            if path not in os.listdir():
                os.mkdir(path)
            x += 1



            urllib.request.urlretrieve(imgpath,'image/%s.jpg'%x)


    z = entry.get()
    z = int(z)
    for i in range(1, z + 1):

        photo_get(i)
    messagebox.showinfo('提示', '下载完成，请查看该软件目录下的文件夹 IMAGE')






root.title('爬去豆瓣小姐姐的照片')
root['bg']='black'
root.minsize(550,250)
label=Label(root,text='MK- 鹿皮酱',font=('微软雅黑',10),fg='white',bg='black')
label.place(x=5,y=18)
label1=Label(root,text='PYTHON获取豆瓣小姐姐照片',font=('微软雅黑',20),fg='white',bg='black')
label1.place(x=100,y=5)
label2=Label(root,text='请输入你要获取的页数:',font=('微软雅黑',10),fg='white',bg='black')
label2.place(x=105,y=100)
entry=Entry(root,font=('微软雅黑',10),textvariable=StringVar())
entry.place(x=270,y=100,width=40)
btn=Button(root,text='开始',font=('微软雅黑',10),fg='white',bg='black',command=photo)
btn.place(x=370,y=100,height=25)


mainloop()