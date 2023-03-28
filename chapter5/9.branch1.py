import math
a=1
b=-3
c=3
delta = b**2-4*a*c
if delta>=0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print(x1,x2)
