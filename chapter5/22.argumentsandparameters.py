##   形参与实参
def changed(a,b):
	# 形参在内存中是指向实参地址的
    print("形参a的地址{},b的地址{}".format(id(a),id(b)))
    t=a
    a=b
    b=t    # 交换形参实际上的内存地址的交换，而不是地址中的值的交换
    print("交换后，形参a的地址{},b的地址{}".format(id(a),id(b)))
    print("inner changed,a={},b={}".format(a,b))

a=3
b=4     # 实参在内存中是存在地址的
print("实参a的地址{},b的地址{}".format(id(a),id(b)))
changed(a,b)
print("outer changed,a={},b={}".format(a,b))
