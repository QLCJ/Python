# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author: Q

      # 需要打开 POP3/SMTO/IMAP 协议    打开要设置授权码
      # 可以更改收信人和发信人，发送文本










import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders

   #                发件人，收信人
def send_mail(server,fro,to,subject='',text='',files=[]):
    '''发送邮箱'''

    #         传入服务器   字典
    assert type(server) ==dict
    assert type(to) == list
    assert type(files) == list

    #创建一个发送邮件的实例
    msg = MIMEMultipart()
    #邮件发件人
    msg['From'] = fro
    #邮件的主题
    msg['Subject'] = subject
    #收件人   可以多个
    msg['To'] = COMMASPACE.join(to)
    #发送时间  若不设置则不显示
    msg['Date'] = formatdate(localtime=True)

    # MIMEText  三个参数：文本，plain设置文本，编码
    msg.attach(MIMEText(text,'plain','utf-8'))

    # 发送附件
    for file in files:
        # 设置字体
        part = MIMEBase('application','octet-stream')
        # 打开附件的位置
        with open(file,'rb') as f:
            # 写入附件
            part.set_payload(f.read())
        # 把part解码
        encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment;filename="%s"' % os.path.basename(file))
        msg.attach(part)

    # 调用协议
    smtp = smtplib.SMTP()

    #connect  1、邮件服务器  2、端口  默认端口
    smtp.connect(server['name'])
    smtp.login(server['user'],server['passwd'])
    #发件人   收信人  发送消息
    smtp.sendmail(fro,to,msg.as_string())



if __name__ == '__main__':
    # 循环
    while True:
        server = {
            'name':'smtp.163.com',       # 协议，有三个，一般用这个
            'user':'fuchuanz@163.com',   # 发信人
            'passwd':'123456f'           # 授权码（注意：不是登陆密码）
        }
        fro = 'fuchuanz@163.com'          # 发信人
        to = ['1054898157@qq.com']       # 收信人
        subject = 'Hello word'            # 邮件标题
        text = '哈哈哈，只是测试。无聊！'   # 邮件内容
        send_mail(server,fro,to,subject,text)
        time.sleep(10)



                                    # to = ['55807975@qq.com']   目标       text = '别 乱惹程序员。'
                                    # to = ['396207123@qq.com']  zlz


