import pywifi
from pywifi import const   # 引用一些常量

# 判断是否已经连接盗WiFi
def gic():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取到第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 打印无线网卡的名称
    # print(ifaces.name())
    # 列表
    # print(ifaces)
    # 打印网卡连接的状态   0代表为连接   4表示已连接上了
    # print(ifaces.status())
    # IFACE_CONNECTED 连接状态      connect 连接
    if ifaces.status() == const.IFACE_CONNECTED:
        print("已连接到WiFi")
    else:
        print("未连接到WiFi")

#gic()

# 扫描附近的WiFi
def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 扫描WIFi
    ifaces.scan()
    # 获取扫描结果
    result = ifaces.scan_results()
    for name in result:
        print(name.ssid)
    #print(result)



bies()