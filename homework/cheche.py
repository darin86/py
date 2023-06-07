import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

# 创建一个图形和坐标轴
fig, ax = plt.subplots()

# 绘制车身
body = Rectangle((-3, -1), 6, 2, facecolor='red')
ax.add_patch(body)

# 绘制轮胎
front_tire = Circle((-2.5, -1), 0.5, facecolor='black')
rear_tire = Circle((2.5, -1), 0.5, facecolor='black')
ax.add_patch(front_tire)
ax.add_patch(rear_tire)

# 绘制车顶
roof = Rectangle((-2, 1), 4, 1, facecolor='red')
ax.add_patch(roof)

# 设置坐标轴范围和纵横比例
ax.set_xlim(-4, 4)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()
