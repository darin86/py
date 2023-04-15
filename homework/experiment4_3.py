from turtle import *
import math

speed(0)
down()
for j in range(0,360,72):
    k=0
    seth(j)
    fd(-10*math.pi*72/180)
    for i in range(10):
        color(1,k,k)
        k+=0.1
        begin_fill() 
        circle(10-i)
        end_fill()
        fd(1)
    home()
exitonclick()
