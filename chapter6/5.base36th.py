ch = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
      'q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5',
      '6','7','8','9')
## 输入一个字符串
code = input('输入一个字符串')
t=0
## 将字符串转换为一个长整数
for i in code:
   t = t * 256 + ord(i)
s = ''
## 36进制转换
while(t!=0):
    s = s.join(ch[t%len(ch)]+' ').rstrip()  # 分隔符插入，第一个字母，则在开头插入，第二个在结尾
    t=t//len(ch)
print(s)
