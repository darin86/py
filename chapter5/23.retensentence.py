def max(a,b):    # 求两数最大值
	if a>=b:
		return a
	else:
		return b

def min(a,b):    # 求两数最小值
	if a<b:
		return a
	else:
		return b

a=int(input("请输入a,b："))
b=int(input())
print("max={max},min={min}".format(max=max(a,b),min=min(a,b)))
