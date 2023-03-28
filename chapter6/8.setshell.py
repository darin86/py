
## 创建集合
>>> a={3,5}    # 创建集合，使用一对{}来创建集合
>>> a
{3, 5}
>>> a2=set(range(5,13))    # 创建集合，使用set和range函数创建集合
>>> a2
{5, 6, 7, 8, 9, 10, 11, 12}
>>> b = set([1,3,5,7,9])    # 创建集合，使用列表创建集合
>>> b
{1, 3, 5, 7, 9}
>>> x=set()    # 创建空集合
>>> x
set()

## 集合重复元素的处理
>>> c=set('hello')    # 利用字符串创建集合
>>> c
{'h', 'e', 'o', 'l'}   # 得到的是没有重复的字母集合（自动去掉重复的元素）
>>> import random     # 导入随机数对象，以便后面代码下使用
>>> d = {random.randint(1,100) for i in range(20)}    #利用推导式创建集合
>>> d    # 显示这个集合
{6, 11, 12, 13, 22, 26, 29, 40, 44, 45, 51, 56, 57, 61, 67, 71, 72, 90, 94, 100}
>>> len(d)    # 集合的长度，这里显示20 ，说明随机数没有重复
20
>>> d = {random.randint(1,10) for i in range(20)}    # 再次通过推导式创建集合，这里创建集合，调整了随机数的范围，使随机数能重复
>>> d    # 显示这个集合，这次明显看到这个集合短很多
{1, 2, 3, 4, 6, 7, 8, 9}
>>> len(d)    # 集合长度，也明显没有20这个长度
8

## 删除元素

>>> a    # 显示a集合中的内容
{3, 5}
>>> dir(a)    # 显示a的所有内置函数及常量
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a.add(4)    # 增加元素4
>>> a
{3, 4, 5}
>>> a.add(5)    # 增加已存在的元素5
>>> a
{3, 4, 5}
>>> a.add(1)    # 增加元素1
>>> a
{1, 3, 4, 5}
>>> a.pop(3)    # pop()不接收参数
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.pop(3)
TypeError: pop() takes no arguments (1 given)
>>> a.pop()    # 删除并返回一个元素
1
>>> a.remove(3)    # 删除指定的元素
>>> a
{4, 5}

## 集合的运算
>>> a = set(range(1,10))    # 创建集合a
>>> b = set(range(7,15))    # 创建集合b
>>> a    # 显示集合a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> b    # 显示集合b
{7, 8, 9, 10, 11, 12, 13, 14}
>>> a+b    # 集合没有加运算
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a|b    # 集合a与b的并集
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
>>> a&b    # 集合a与b的交集
{8, 9, 7}
>>> a-b    # 集合a与b的差集
{1, 2, 3, 4, 5, 6}
>>> b-a    # 集合b与a的差集
{10, 11, 12, 13, 14}
>>> a^b    # 集合a与b的对称差集
{1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14}
>>> a<b    # 判断集合a是b的子集
False
>>> c=set(range(9,12))    #创建集合c
>>> c<b    # 判断集合c是b的子集
True
