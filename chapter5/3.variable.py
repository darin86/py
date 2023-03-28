t=100                 #将100赋值给t
print(t,type(t))      #打印t的值和类型
k=100.0
print(k,type(k))
print(id(t))           #打印t的地址
print(id(k))           #打印k的地址
id(t) == id(k)         #打印判断t，k地址是否相等