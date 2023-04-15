from turtle import *
import math
import random
pensize(18)
colors =['red', 'yellow', 'blue', 'green', 'pink', 'purple']
up()
bk(350)
color(random.choice(colors))
down()
fd(50)
for j in range(5):
    color(random.choice(colors))   
    for i in range(0,360,30):           
        goto(i/3+120*j-300,15*math.sin(math.pi*i/180))
color(random.choice(colors))
fd(50)
color(random.choice(colors)) 
circle(20,180)   
fd(20)             
(x,y)=pos()
setpos((x+5,y))
color("black")
pensize(5)
dot()             
hideturtle()
exitonclick()