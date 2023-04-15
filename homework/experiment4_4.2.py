from turtle import * 
import random
import math
colors =['red', 'yellow', 'blue', 'green', 'pink', 'purple']
up()
bk(141)
down()
for j in range(4):
    color(random.choice(colors))
    begin_fill()
    left(45)
    fd(50)
    right(90)
    fd(50)
    left(225)
    for i in range(4):		
        fd(math.sqrt(2)*50)
        if i==0:
            end_fill()
            color(random.choice(colors))
            begin_fill()
        left(90)
    right(180)
    end_fill()
hideturtle()
exitonclick()