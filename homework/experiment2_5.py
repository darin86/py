while(1):
    a=input("请输入你的百分制成绩:")
    if a>=80 and a<=100:
        print("A")
        break
    elif a>=60 and a<=80:
        print("B")
        break
    elif a>=40 and a<=60:
        print("C")
        break
    elif a>=20 and a<=40:
        print("D")
        break
    elif a>=0 and a<=20:
        print("E")
        break
    else:
        print("输入有误，请再次输入:")