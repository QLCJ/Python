# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author: Q

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders

def send_mail(server,fro,to,subject='',text='',files=[]):
    '''发送邮箱'''

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
    #发送时间  若不设置则不现实
    msg['Date'] = formatdate(localtime=True)

    # MIMEText  三个参数： 1、文本  2、plain设置文本   3、编码
    msg.attach(MIMEText(text,'plain','utf-8'))

    #附件
    for file in files:
        part = MIMEBase('application','octet-stream')

        with open(file,'rb') as f:
            part.set_payload(f.read())

        encoders.encode_base64(part)

        part.add_header('Content-Disposition','attachment;filename="%s"' % os.path.basename(file))
        msg.attach(part)

    smtp = smtplib.SMTP()

    #connect  1、邮件服务器  2、端口  默认端口
    smtp.connect(server['name'])
    smtp.login(server['user'],server['passwd'])
    #发件人   收信人  发送消息
    smtp.sendmail(fro,to,msg.as_string())



if __name__ == '__main__':

    while True:
        server = {
            'name':'smtp.163.com',
            'user':'fuchuanz@163.com',
            'passwd':'123456f'
        }
        fro = 'fuchuanz@163.com'
                                 # to = ['55807975@qq.com']
        to = ['2546877050@qq.com']
        subject = '来自啊飘的攻击'
                                     # text = '别TM乱惹程序员。'
        text = '我真诚吗？'
        send_mail(server,fro,to,subject,text)



                                    # to = ['55807975@qq.com']   目标
                                    # to = ['396207123@qq.com']  zlz


