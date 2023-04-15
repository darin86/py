from turtle import *
import random
colors =['red', 'yellow', 'blue', 'green', 'pink', 'purple']
color(random.choice(colors), random.choice(colors))
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
penup()
goto(-150,50)
pendown()
color("black")
write("电气224黄达林202213290429")
hideturtle()
exitonclick()