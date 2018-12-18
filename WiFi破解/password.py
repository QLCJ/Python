import  itertools as its   #迭代器    as是重命名


words = "1234567890"
r = its.product(words,repeat=4)
# 保存在文件中
dic = open("pass.txt","a")

for i in r:
    # i是元祖
    # 原始密码是('a','a','a') 这是元祖,不能写入文件中
    # join是使元祖形成字符串  aaa
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()