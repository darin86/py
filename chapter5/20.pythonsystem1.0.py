import getpass

name= "student"
passwd = "dvgi"

## 首先将加密的程序用函数定义出来
def encrypto(password):
    crypto =""
    for j in password:
        crypto = crypto + "".join(chr((ord(j)-97+3)%26+97))
    return crypto

## 播放视频
def playvideo():
    pass

## 播放视频
def doexercise():
    pass

## 播放视频
def freeexercise():
    pass


## 选择菜单
def menu():
    welcome = '''
	欢迎使用Python学习系统
	请选择以下功能数字：
	1.播放学习视频
	2.做练习题
	3.自由练习
	4.结束
    '''
    print(welcome)
    c = input("你的选择是：")
    # 菜单选择
    while(int(c)<1 or int(c)>4):
        print("你输入有误，请重新选择.")
        print(welcome)
        c = input("你的选择是：")
    if int(c)==1:
        print("你选择了观看视频，好好学习，加油！")
    elif int(c)==2:
        print("你选择了做练习题，好好学习，加油！")
    elif int(c)==3:
        print("你选择了自由练习，好好学习，加油！")
    elif int(c)==4:
        print("你选择了退出，好好学习，期待你下次访问！")
        exit()
        
## 登录系统
def login():
    i=0
    while(i < 3):
        username = input("请输入你的用户名：")
        password = getpass.getpass("请输入你的密  码：")
        i+=1   
        if username==name and encrypto(password)==passwd:
            print("欢迎{}进入Pyhon学习系统".format(username))
            menu()
            break
        else:
            print("用户名密码错误，请再试一次！")
    else:
        print("你尝试太多次了，谢谢使用，再见！")
## 主函数
def main():
    login()

main()
