import math
a=1
b=-4
c=4
delta = b**2-4*a*c
if delta==0:
    x1=-b/(2*a)
    print(x1)
elif delta>0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print(x1,x2)
else:
    print("此方程没有实数解")
