# 创建字典
>>> d = {}    # 创建空字典
>>> d
{}
>>> d = {'name':"Bob","age":40}    # 用{}创建字典
>>> d
{'name': 'Bob', 'age': 40}
>>> empl = {"market_manage":{'name':'Bob',"age":40},'CEO':{'Name':'Toddy','age':52}}    # 用{}创建多维字典
>>> e
{'market_manage': {'name': 'Bob', 'age': 40}, 'CEO': {'Name': 'Toddy', 'age': 52}}
>>> d = dict([('name', 'Toddy'), ('age', 51)])    # 用dict函数和列表参数创建字典
>>> d
{'name': 'Toddy', 'age': 51}
>>> d = dict(name='Toddy', age=40)    # 用dict函数和赋值参数法创建字典
>>> d
{'name': 'Toddy', 'age': 40}
>>> names = ["Alice","Bob","Trudy","Jerry","Tom","Tracy"]
>>> ages = [23,40,35,46,52,39]
>>> d = dict(zip(names,ages))    # 用dict函数和键列表和值列表创建字典
>>> d
{'Alice': 23, 'Bob': 40, 'Trudy': 35, 'Jerry': 46, 'Tom': 52, 'Tracy': 39}

# 删除字典
>>> del(d)         # 删除字典对象`

# 字典元素的访问
>>> d
{'Alice': 23, 'Bob': 40, 'Trudy': 35, 'Jerry': 46, 'Tom': 52, 'Tracy': 39}
>>> d['Alice']     # 键名访问
23
>>> empl
{'market_manage': {'name': 'Bob', 'age': 40}, 'CEO': {'Name': 'Toddy', 'age': 52}}
>>> empl['CEO']['Name']    # 二维字典键名访问
'Toddy'
>>> 'age' in empl    # 判断键是否存在字典中，这里失败是因为empl只有'market_manage'和'CEO'两个键名
False
>>> 'age' in empl['CEO']    # 判断键是否存在字典中，这里成功是对于empl['CEO']也是字典，并且这个字典中存在'age'这个键
True
>>> empl.keys()    # 读取字典中的所有键
dict_keys(['market_manage', 'CEO'])
>>> empl.values()    # 读取字典中的所有值
dict_values([{'name': 'Bob', 'age': 40}, {'Name': 'Toddy', 'age': 52}])
>>> empl.items()    # 读取字典中的所有键和值
dict_items([('market_manage', {'name': 'Bob', 'age': 40}), ('CEO', {'Name': 'Toddy', 'age': 52})])
>>> empl.get('CEO')    # 获取empl['CEO']的值
{'Name': 'Toddy', 'age': 52}
>>> empl.setdefault('engineer_manange')    # 增加一个名为'engineer_manange'字典项，值默认为空
>>> empl    # 查看字典中刚才增加的项目已经显示出来了
{'market_manage': {'name': 'Bob', 'age': 40}, 'CEO': {'Name': 'Toddy', 'age': 52}, 'engineer_manange': None}
>>> empl.pop('engineer_manange')    # 删除键名为'engineer_manange'字典项
>>> empl
{'market_manage': {'name': 'Bob', 'age': 40}, 'CEO': {'Name': 'Toddy', 'age': 52}}
>>> len(empl)    # 字典长度
2
