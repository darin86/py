import getpass

name= "student"
passwd = "asdf"
i=0
while(i < 3):
    username = input("请输入你的用户名：")
    password = getpass.getpass("请输入你的密  码：")
    i+=1
    if username==name and password==passwd:
        print("欢迎{}进入Pyhon学习系统".format(username))
    else:
        print("用户名密码错误，请再试一次！")
else:
    print("你尝试太多次了，谢谢使用，再见！")
