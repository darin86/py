str1='ababcd'
str2='123456'
s = 'name\tage\nTom\t25\nJerry\t22\n'
print(s)


p=25
print("欢迎使用Python学习系统,您是第"+str(p)+"位访问者")


path="c:\new\text"
print(path)


path=r"c:\new\text"
print(path)

a="hello world "
a.find('or')
7
a="hello world    "
a.rstrip()
'hello world'
a="hello world "
a.replace("or","OR")
'hello wORld'
a.split(' ')
['hello', 'world', '']
a = "123456"
a.isdigit()
True
a="HELLO WORLD"
a.lower()
'hello world'
a.endswith('d')
False
a.endswith('D')
True
strlist=['A','B','C']
' hello '.join(strlist)
'A hello B hello C'
b=a.encode("utf-8")
b
b'HELLO WORLD'
b.decode("utf-8")
'HELLO WORLD'

dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

