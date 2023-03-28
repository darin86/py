a=10
b=20
# ---------------算术表达式------------
print("---------------算术表达式------------")
print(a+b)
# 30    把10和20分别代替a和b，求和得到30
print(a-b)
# -10   把10和20分别代替a和b，相减得到-10
print(a*b)
# 200   把10和20分别代替a和b，相乘得到200
print(b/a)
# 2.0   把10和20分别代替a和b，求商得到2.0
print(b%a)
# 0     把10和20分别代替a和b，取得到30
print(a**b)
# 100000000000000000000         把10和20分别代替a和b，求和得到30
print(9//2)
# 4     把10和20分别代替a和b，求和得到30
print(5.0//3)
# 1.0   浮点数5.0除以3得到结果的整数部分1.0
print("hello"+"world")
# 'helloworld'
print("a"*3)
# 'aaa'
hello="hello,python toy"
print(hello)
# ---------------赋值运算符----------
print("---------------赋值表达式------------")
c = a + b        # c 被赋值为30
print(c)
c += a           # c 被赋值为40
print(c)
c -= b           # c 被赋值为20
print(c)
c *= a           # c 被赋值为200
print(c)
c /= b           # c 被赋值为10.0
print(c)
c %= a           # c 被赋值为0
print(c)
c = 10
c **= a           # c 被赋值为10000000000
print(c)
c //= a           # c 被赋值为1000000000
print(c)
# ---------------比较运算符----------
print("---------------比较表达式------------")
print(a == b)    # 输出False
print(a != b)    # 输出True
print(a > b)     # 输出False
print(a < b)     # 输出True
print(a >= b)    # 输出False
print(a <= b)    # 输出True
# ---------------逻辑运算符----------
print("---------------逻辑表达式------------")
x = True
y = False
print(x and y)   # 输出False
print(x or y)    # 输出True
print(not y)     # 输出True
# ---------------位运算符------------
print("---------------位运算符------------")
a=56
b=13
print(bin(a),bin(b))
c = a & b
print(bin(c))
c = a | b
print(bin(c))
c = a ^ b
print(bin(c))
c = ~ a
print(bin(c))
c = a >> 2
print(bin(c))
c = b << 1
print(bin(c))
# ---------------身份运算符------------
print("---------------身份运算符------------")
d="object"
e=d
print(e is d)
print(e is not d)
e="object"
print(e is d)
# ---------------成员运算符------------
print("---------------成员运算符------------")
f = 'e'
print(f in d)
print(f not in d)

