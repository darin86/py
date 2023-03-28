import getpass

name= "student"
passwd = "dvgi"
i=0
while(i < 3):
    username = input("请输入你的用户名：")
    password = getpass.getpass("请输入你的密  码：")
    i+=1
    ''' 这里是密码处理的地方，有两种处理方式:
        1.将输入的密码加密后与passwd比较（这样就非常简单，直接拿加密的代码过来即可）
        2.将原始密码解密后与password比较（这样写需要再次做调试）
        这里我选择了第1种方式，有兴趣的同学自己补解密代码吧
    '''
    crypto =""
    for j in password:
        crypto = crypto + "".join(chr((ord(j)-97+3)%26+97)) 
    if username==name and crypto==passwd:
        print("欢迎{}进入Pyhon学习系统".format(username))
        break
    else:
        print("用户名密码错误，请再试一次！")
else:
    print("你尝试太多次了，谢谢使用，再见！")
