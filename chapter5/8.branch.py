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
if int(c)==1:
    print("你选择了观看视频，好好学习，加油！")
elif int(c)==2:
    print("你选择了做练习题，好好学习，加油！")
elif int(c)==3:
    print("你选择了自由练习，好好学习，加油！")
elif int(c)==4:
    print("你选择了退出，好好学习，期待你下次访问！")
    exit()
else:
    c = input("你输入有误，请重新选择，你的选择是：")
    
