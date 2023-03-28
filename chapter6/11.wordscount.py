text = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


## 首先将这段文字预处理，全部转换为小写字母，对其中的标点符合转为空格（便于我们词频分隔）
def getText(text):
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        text = text.replace(ch, "")
    return text
## 分隔出一个一个的单词来
txt = getText(text)
words = txt.split()
counts = {}
## 循环统计词语出现次数
for word in words:
    if word not in counts:     # 第一次出现的单词要加入字典的键值中去
        counts.setdefault(word,0)
    counts[word] = counts[word]+1     # 计数
items = list(counts.items())   # 转成列表，方便排序
items.sort(key = lambda X:X[1], reverse = True)
for i in range(10):    # 输出top10的单词
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
