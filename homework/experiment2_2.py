import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
delta = b**2-4*a*c
print(int(delta))
if delta==0:
    x1=-b/(2*a)
    print(x1)
elif delta>0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print(x1,x2)
else:
    print("此方程没有实数解")
print("电气224 202213290414 吴华煜")