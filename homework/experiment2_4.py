import math
dayup=1.01
dayup=pow(dayup,365)
daydown=0.99
daydown=pow(daydown,365)
while(1):
    a=input("输入UP or DOWN:")
    if a=='UP':
        print("每天学习，一年后的知识:{}".format(dayup))
        break
    if a=='DOWN':
        print("每天不学习，一年后的知识:{}".format(daydown))
        break
    else:
        print("输入有误请再次输入!")
print("电气224 202213290429 黄达林")