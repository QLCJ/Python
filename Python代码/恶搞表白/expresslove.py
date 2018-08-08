from tkinter import *
from tkinter import messagebox

def closeallwindow():
    window.destroy()
def closewindow():
    messagebox.showinfo(message='关闭失败')
    return
def Love():
    love = Toplevel(window)
    love.geometry("300x100+520+260")
    love.title('一言为定')
    label=Label(love,text='真的吗?答应我了?')
    label.pack()
    btn=Button(love,text='是的',command=A)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)
def closelove():
    messagebox.showinfo(message='关闭失败')
    return
def A():
    a = Toplevel(window)
    a.geometry("300x100+520+260")
    a.protocol("WM_DELETE_WINDOW", closea)
    a.title('一言为定')
    label = Label(a, text='给我发个消息吧，爱你')
    label.pack()
    btn=Button(a,text='好的',command=closeallwindow)
    btn.pack()
def closea():
    messagebox.showinfo(message='关闭失败')

def Nolove():
    nolove = Toplevel(window)
    nolove.geometry("300x100+520+260")
    nolove.title(' ')
    label = Label(nolove, text='家务全包')
    label.pack()
    btn = Button(nolove, text='ok', command=B)
    btn.pack()
    nolove.protocol("WM_DELETE_WINDOW", closenolove)
    window.closs()
def closenolove():
    messagebox.showinfo(message='关闭失败')
    return


def B():
    b = Toplevel(window)
    b.geometry("300x100+520+260")
    b.protocol("WM_DELETE_WINDOW", closeb)
    b.title('')
    label = Label(b, text='房产证写你名字')
    label.pack()
    btn = Button(b, text='ok', command=C)
    btn.pack()


def closeb():
    messagebox.showinfo(message='关闭失败')
def C():
    c = Toplevel(window)
    c.geometry("300x100+520+260")
    c.protocol("WM_DELETE_WINDOW", closec)
    c.title('')
    label = Label(c, text='房产证写你名字')
    label.pack()
    btn = Button(c, text='ok', command=D)
    btn.pack()
def closec():
    messagebox.showinfo(message='关闭失败')

def D():
        d= Toplevel(window)
        d.geometry("300x100+520+260")
        d.protocol("WM_DELETE_WINDOW", closed)
        d.title('')
        label = Label(d, text='答应我吧')
        label.pack()
        btn = Button(d, text='ok',command=Love)
        btn.pack()

def closed():
    messagebox.showinfo(message='关闭失败')

window = Tk()
# 窗口标题
window.title('小姐姐，我观察你很久了')
# 窗口大小
window.geometry('380x420+500+240')
# 几何 窗口位置
window.geometry('+500+240')
# protocol
window.protocol("WM_DELETE_WINDOW",closewindow)
#标签对象
label =Label(window,text="喜欢我吗？",font=('微软雅黑',15),fg='red')
# 定位    网格式布局 pack包 place位置
label.grid(row=0,column=0)
label1=Label(window,text = "做我女朋友好不好？",font=("微软雅黑",15),fg='green')
# sticky  对齐方式  N S W E
label1.grid(row=1,column=1,sticky=E)
# 显示图片   column 组件跨越的列数
photo=PhotoImage(file="./FASHION.png")
imageLabel=Label(window,image=photo)
imageLabel.grid(row=2,columnspan=2)
# 按钮控件  点击触发的事件command
btn=Button(window,text="好",font="微软雅黑",width=15,height=2,command=Love)
btn.grid(row=3,column=0,sticky=W)
but1=Button(window,text="不好",command=Nolove)
but1.grid(row=3,column=1,sticky=E)
btn2=Button(window,text='quit',command=closeallwindow)
btn2.grid(row=4,column=1,sticky=E)
window.mainloop()
























