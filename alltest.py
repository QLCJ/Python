# /usr/bin/env python3.6.5
# -*- coding: utf-8 -*-
# Author: Q

#      这个脚本的问题在于有些 APK 无法解析，或者解析不全（直解析出几个文件）
#  脚本的位置：      D:\Language Program\Python\Project\APK\ToolScript     脚本名：alltest.py
#  apk 存放位置：D:\Language Program\Python\Project\APK\PaAPK\apk      ，这个目录是总目录，它下面是每个分类的文件夹




# m2  每个 apk 的名称
# Classname  每个 apk 的类别


import os
import elementtree
import time
import xml.etree.ElementTree as ET
from xml.etree import ElementTree as ET


def tool():
    list = []           # 用于存储权限名
    apkNumber = []      # 用于 apk 的数量
    apkName = []  # 用于 apk 的名字
    #m2 = ['腾讯手机管家—微信清理.apk','雷霆战机-- 超人气飞行射击类手游.apk','QQ浏览器-便捷管理手机文件.apk','QQ.apk','QQ空间.apk','微信.apk']
    ClassName = ['安全','飞行射击','工具','社交','视频','网络游戏','新闻','音乐']
    APKNAMELeibiao2 = []


#第一部分    进入个类别的文件夹，解析 APK

  # 计算 共有多少的 APK文件夹   和    计算各类 APK文件夹 中有多少APK。 就是计算有多少 文件夹和 APK 的数量
    # 进入到   各类APK文件夹   的    根目录（PaAPK）
    os.chdir('D:\Language Program\Python\Project\APK\PaAPK')      # 进入根目录(PaAPK)， PaAPK里面有各类 APK文件夹 。
    folderNumber = os.listdir('apk')        # 获取 apk目录 中所有的目录列表（就是以列表的形式输出    apk 中 所有的子目录）。
    #print(len(folderNumber))         # 计算 列表中元素(各类别名)的数量。  为了后面解析。

    # 进入到      APK         的    根目录（apk）
    #for a in range(len(folderNumber)):
    for a in range(len(folderNumber)):
        os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk')  # 进入根目录(apk)， PaAPK里面有各类 APK文件夹 。
        #APKNumber = os.listdir(ClassName[a-1])  # 获取 各类别目录 下的所有的 APK名 列表（就是以列表的形式输出   各类别目录   中 所有的apk名）。
        #print(len(APKNumber))  # 计算 列表中元素(APK名)的数量。  为了后面解析。
        #print(APKNumber)         # 以多个列表输出APK名。
        #apkNumber.append(len(APKNumber))     # 将每个文件夹中的 apk数量进行赋值，为了在进入各类文件夹时能够确定要解析 apk 的数量。
        #apkName.append(APKNumber)
    #print(apkNumber)     # 以列表形式输出 各类文件夹  中apk的数量
    #print(apkName)     # 以列表形式输出 各类文件夹  中apk名字         。问题在这，忘了运行这一步看看

# 上面都是 OOOOOKKKKKK   ,问题是  输出的  APk名字是一列表的形式输出，后面反编译用不了。
# 所以我打算  以及计算 各类文件夹 的 apk数量时，提取apk名



    #利用 for 循环把每个文件夹内的 apk名提取，  和计算apk数量
    for c in range(len(folderNumber)):
    #for c in range(4):   #   用于 TTTTTEEEESSSSSTTTT
        os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk')
        AName = os.listdir(ClassName[c])          # 以多个列表输出 apk名字
        #print(AName)                             # 以多个列表输出 apk名字
        #print(len(AName))                        # 输出每个 文件夹中 apk的数量

    # 分别进入个类别的文件夹
        os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk\\'+ClassName[c])
        #os.system('dir')        # OK ，成功进入各类 APK 的文件夹中
        for f in AName:               # 得到每个 apk的名字
            print(f)

        # 开始解析 APK
        # os.system('apktool.bat d -f QQ.apk -o ASDDD')         # 反编译到 ASDDD 文件夹中
        # os.system('apktool.bat d -f '+m2[c])         # 反编译,   后面跟的是名字
        #os.system('chcp 950')
        os.system('apktool.bat d -f '+f)  # 反编译,   后面跟的是apk名字
        time.sleep(10)




































        # 利用 for 循环把每个文件夹都进入，然后解析。
        # for b in range(len(folderNumber)):
        #     # 分别进入个类别的文件夹
        #     os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk\\'+ClassName[c])
        #     os.system('dir')        # OK ，成功进入各类 APK 的文件夹中

            #以上都 OK


            # 开始解析 APK
            # os.system('apktool.bat d -f QQ.apk -o ASDDD')         # 反编译到 ASDDD 文件夹中
            #os.system('apktool.bat d -f '+m2[c])         # 反编译,   后面跟的是名字
            #os.system('apktool.bat d -f '+AName[len(AName)])  # 反编译,   后面跟的是apk名字























    # #利用 for 循环把每个文件夹都进入，然后解析。
    # #for c in range(len(folderNumber)):
    # for c in range(4):   #   用于 TTTTTEEEESSSSSTTTT
    #     # 分别进入个类别的文件夹
    #     os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk\\'+ClassName[c])
    #     #os.system('dir')  # OK ，成功进入各类 APK 的文件夹中
    #
    #     # 开始解析 APK
    #     # os.system('apktool.bat d -f QQ.apk -o ASDDD')         # 反编译到 ASDDD 文件夹中
    #     #os.system('apktool.bat d -f '+m2[c])         # 反编译,   后面跟的是名字
    #     #os.system('apktool.bat d -f '+m2[c])  # 反编译,   后面跟的是apk名字




        # tree = ET.parse('AndroidManifest.xml')
        # # 获取 root 节点
        # root = tree.getroot()
        #
        # namespace = '{http://schemas.android.com/apk/res/android}'
        # # 查出所有的 user-permission
        # for application in root.iter('uses-permission'):
        #     activityName = application.get(namespace + 'name')  # user-permission
        #     print(activityName)
        #     list.append(activityName)
        # # 查出所有的第三方 库
        # for application2 in root.iter('permission'):
        #     activityName2 = application2.get(namespace + 'name')  # user-permission
        #     print(activityName2)
        #     list.append(activityName2)

    # # 第二部分   将读取到的权限名存入 .xml 文件中
    # root = ET.Element('permission')  # 根节点的名称
    # son = ET.SubElement(root, 'category', {'name': "类别"})  # 第一个节点  ，使用类别名
    # sonson = ET.SubElement(son, 'APK', {'name': "QQ"})
    # for i in range(len(list)):
    #     ET.SubElement(sonson, 'permission', {'name': list[i]})  # 类别名下，  权限名
    # tree = ET.ElementTree(root)  # 解析根节点
    #
    # tree.write("D:\\APKtest\\" + "permission.xml")  # 保存，填写保存的文件名


# 基本实现 ，现在可以 进入 目标文件夹，解析 APK ，在进入解析的 APK文件夹 中 ， 解析 AndroidManifest.xml 文件， 获取权限名， 写入 .xml
#   明天将全部连一边，下载   解析     写入
# 现在写入只能写一个
# 明天将  写入的 .xml 文件的 类别名 ，软件名，利用 for循环 搞定。思路：1、将下载部分的变量名先赋值  2、利用 for循环 解析，写入 .xml
# 目前似乎不需要考虑什么打开文本方式，只需要重新将list追加就行了


# #  写入 txt 文件     。  list是列表 ，存储了所有的权限m名
# # 接下来就是将都出来的数据写入文本文件中。
# filePath = 'D:\\APKtest\\w.txt'   # 要写入的 txt 文件 所在的位置
# file = open(filePath, 'a')        # 以 附写方式 打开，不可读
# for i in range(len(list)):        # list 适用于存储所有的权限名  ，  此处计算存储了 多少个 权限名，   len 是计算字符串的数量
#      s = str(list[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
#      s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
#      file.write(s)
# file.close()
# print("保存文件成功")























# 计算 共有多少的 APK文件夹   和    计算各类 APK文件夹 中有多少APK。 就是计算有多少 文件夹和 APK 的数量
    # 进入到   各类APK文件夹   的    根目录（PaAPK）
    #os.chdir('D:\Language Program\Python\Project\APK\PaAPK')      # 进入根目录(PaAPK)， PaAPK里面有各类 APK文件夹 。
    #folderNumber = os.listdir('apk')        # 获取 apk目录 中所有的目录列表（就是以列表的形式输出    apk 中 所有的子目录）。
    #print(len(folderNumber))         # 计算 列表中元素(各类别名)的数量。  为了后面解析。



    # #利用 for 循环把每个文件夹都进入，然后解析。
    # #for c in range(len(folderNumber)):
    # # 进入到      APK         的    根目录（apk）
    # for a in range(len(folderNumber)):
    #     os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk')  # 进入根目录(apk)， PaAPK里面有各类 APK文件夹 。
    #     APKNameLeibiao = os.listdir(ClassName[a])  # 获取 各类别目录 下的所有的 APK 列表（就是以列表的形式输出   各类别目录 中 所有的apk）。
    #     #print(len(APKNumber))         # 计算 列表中元素(APK名)的数量。  为了后面解析。    #      有有有有用用用用
    #     #print(APKNAME)
    #     apkNumber.append(len(APKNameLeibiao))  # 将每个文件夹中的 apk数量进行赋值，为了在进入各类文件夹时能够确定要解析 apk 的数量。   有有有有用用用用
    #     #print(APKNAMELeibiao)
    #     APKNAMELeibiao2.append(APKNameLeibiao)
    #     #apkNumber.append(APKNumber)
    # print(APKNAMELeibiao2)
    # print(apkNumber)     # 以列表形式输出 各类文件夹  中apk的数量         有有有有用用用用
    #
    #
    #
    # # 开始解析 APK
    #     # os.system('apktool.bat d -f QQ.apk -o ASDDD')         # 反编译到 ASDDD 文件夹中
    #     #os.system('apktool.bat d -f '+apkNumber[len(APKNumber)])         # 反编译
    #
    # for c in range(len(folderNumber)):   #   用于 TTTTTEEEESSSSSTTTT
    #     # 分别进入个类别的文件夹
    #     os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk\\'+ClassName[c])
    #     #os.system('dir')  # OK ，成功进入各类 APK 的文件夹中
    #     print(c)
    #     # 开始解析 APK
    #     # os.system('apktool.bat d -f QQ.apk -o ASDDD')         # 反编译到 ASDDD 文件夹中
    #     #os.system('apktool.bat d -f '+APKNAMELeibiao2[c])  # 反编译





    # for c in range(folderNumber):   #   用于 TTTTTEEEESSSSSTTTT
    #     # 分别进入个类别的文件夹
    #     os.chdir('D:\Language Program\Python\Project\APK\PaAPK\\apk\\'+ClassName[c])
    #     os.system('dir')  # OK ，成功进入各类 APK 的文件夹中
    #
    #     # 开始解析 APK
    #     # os.system('apktool.bat d -f QQ.apk -o ASDDD')         # 反编译到 ASDDD 文件夹中
    #     #os.system('apktool.bat d -f '+m2[apkNumber[]])         # 反编译
















tool()






