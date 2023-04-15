import turtle

# 设置画布大小和背景颜色
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('black')

# 定义蟒蛇颜色列表
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# 创建画笔对象
pen = turtle.Turtle()
pen.speed(10)  # 设置画笔速度

# 绘制彩色蟒蛇
for i in range(360):
    pen.pencolor(colors[i % len(colors)])  # 循环选择颜色
    pen.width(i/100 + 1)  # 线宽随角度增大而增大
    pen.forward(i)  # 向前移动
    pen.left(59)  # 向左转59度

turtle.done()