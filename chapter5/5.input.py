welcome='''
欢迎使用Python学习系统
请选择以下功能数字：
1.播放学习视频
2.做练习题
3.自由练习
4.结束
'''
print(welcome)
c=input("你的选择是：")
if int(c)>=1 and int(c)<=4:
    print("你的选择是第"+c+"项菜单")
else:
    c=input("你输入的有误，请再次输入：")