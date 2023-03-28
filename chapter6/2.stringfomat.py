name='Trace Ma'
age=40
job='teacher'
salary=8000
print("简单拼接")
info = '''
------info of ''' + name + '''---------
name: ''' + name + '''
age: ''' + str(age) + '''
job: ''' + job + '''
salary: ''' + str(salary) +'''
'''
print(info)


print("格式化输出1")
info = '''
------info of %s---------
name: %s
age: %d
job: %s
salary: %f
'''%(name, name, age, job, salary)
print(info)

print("格式化输出2")
info = '''
------info of {_name}---------
name: {_name}
age: {_age}
job: {_job}
salary: {_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
print(info)


print("格式化输出3")
info = '''
------info of {0}---------
name: {0}
age: {1}
job: {2}
salary: {3}
'''.format(name, age, job, salary)
print(info)
