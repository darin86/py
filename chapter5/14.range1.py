a=3
b=10
c=0
txt = '''
a={0}
b={1}
c={2}
a in range(10):{3}
b in range(10):{4}
c in range(10):{5}
'''.format(a,b,c,(a in range(10)),(b in range(10)),(c in range(10)))

print(txt)
