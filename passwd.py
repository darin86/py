import getpass

def encrypto(password):
    crypto=""
    for j in password:
        crypto = crypto+"".join(chr((ord(j)-97+3)%26+97))#凯撒加密
    return crypto
name="root"
passwd="urrw"#root
i=0
while(i<3):
    username = input("请输入你的用户名:")
    password = getpass.getpass("请输入你的密码：")
    i+=1
    if username==name and encrypto(password)==passwd:
        print("欢迎{}进入Python学习系统".format(username))
        break
    else:
        print("用户名或密码错误,请再次输入！")
else:
    print("你尝试超过3次,谢谢使用,再见！")