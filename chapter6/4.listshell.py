# 定义列表的常用方式 问题file
l = []              # 定义空列表
l
[]
l = [123,'aa',12.3, {}]   # 定义一个一维列表
l
[123, 'aa', 12.3, {}]
l = ['Bob', 40,['dev', 'mgr']]   # 定义一个多维列表
l
['Bob', 40, ['dev', 'mgr']]
l = list('Hello')      # 用list内置函数定义一个列表
l
['H', 'e', 'l', 'l', 'o']
l = list(range(-4,4))      # 用list和range内置函数定义列表
l
[-4, -3, -2, -1, 0, 1, 2, 3]

# 删除列表
del(l)
l


# 添加列表中的元素
l = list(range(0,10))
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.append(11)       # 在列表最后追加数字11
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
l.extend([10.11,12])       # 在列表最后增加列表
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10.11, 12]
l.insert(5,13)       # 在列表中指定的5的位置插入数字13
l
[0, 1, 2, 3, 4, 13, 5, 6, 7, 8, 9, 11, 10.11, 12]

# 删除列表中的元素
l.clear()      # 清空列表中所有元素
l
[]
l = list(range(0,10))
l.pop(8)      # 弹出列表中指定的元素
8
l
[0, 1, 2, 3, 4, 5, 6, 7, 9]
l.remove(4)      # 移除列表中指定的元素
l
[0, 1, 2, 3, 5, 6, 7, 9]

# 列表的应用
l    # 原始列表
[0, 1, 2, 3, 5, 6, 7, 9]
len(l)    # 列表长度
8
l+l    # 列表相加
[0, 1, 2, 3, 5, 6, 7, 9, 0, 1, 2, 3, 5, 6, 7, 9]
l*3    # 列表乘法
[0, 1, 2, 3, 5, 6, 7, 9, 0, 1, 2, 3, 5, 6, 7, 9, 0, 1, 2, 3, 5, 6, 7, 9]
3 in l    # 判断3是否为列表的元素
True
for x in l:    # 循环打印l列表中的元素
	print(x)

	
l = [x**2 for x in range(8)]    # 生成列表的推导式
l
[0, 1, 4, 9, 16, 25, 36, 49]
s = "ABCDE"     # 字符串
l = list(s)     # 字符列表
print(s,l)      # 输出字符串

l[2] = 'c'      # 修改列表中的元素
s[2] = 'c'      # 修改字符串中的元素，这样做会报错的


# 切片应用
names = ["Alice","Bob","Trudy","Jerry","Tom","Tracy"]     # 定义一个列表
len(names)     # 返回列表长度
6
names[1:4]     # 切取names列表序号为1到3之间的元素
['Bob', 'Trudy', 'Jerry']
names[:3]     # 切取names列表序号为0到2之间的元素
['Alice', 'Bob', 'Trudy']
names[3:]     # 切取names列表序号为3到结束之间的元素
['Jerry', 'Tom', 'Tracy']

# 切片应用2
names[3:-1]   # 切片起始位是3，结束位为最后一个
['Jerry', 'Tom']
names[::-1]   # 切片起始位是0，结束位为长度，步长为-1（将列表倒序）
['Tracy', 'Tom', 'Jerry', 'Trudy', 'Bob', 'Alice']
names[-1::-1]   # 切片起始位是最后一个元素，结束位为长度，步长为-1（将列表倒序），同上
['Tracy', 'Tom', 'Jerry', 'Trudy', 'Bob', 'Alice']
