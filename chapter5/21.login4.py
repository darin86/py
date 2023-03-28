import getpass

## 首先将加密的程序用函数定义出来
def encrypto(password):
    crypto =""
    for j in password:
        crypto = crypto + "".join(chr((ord(j)-97+3)%26+97))
    return crypto


name= "root"
passwd = "urrw"
i=0
while(i < 3):
    username = input("请输入你的用户名：")
    password = getpass.getpass("请输入你的密  码：")
    i+=1   
    if username==name and encrypto(password)==passwd:
        print("欢迎{}进入Pyhon学习系统".format(username))
        break
    else:
        print("用户名密码错误，请再试一次！")
else:
    print("你尝试太多次了，谢谢使用，再见！")
