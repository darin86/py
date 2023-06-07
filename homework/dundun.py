import turtle

turtle.speed(0)  # 速度

turtle.screensize(500, 500, "white")

# 最外层
turtle.penup()
turtle.goto(200, 80)
turtle.pencolor("black")
turtle.pensize(5)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(60)
turtle.circle(-47, 180)
turtle.setheading(240)
turtle.circle(-200, 34)
turtle.setheading(260)
turtle.circle(-300, 32)
turtle.setheading(270)
turtle.forward(65)
turtle.circle(-30, 90)
turtle.forward(65)
turtle.circle(-20, 110)
turtle.forward(15)
turtle.circle(20, 120)
turtle.forward(23)
turtle.setheading(250)
turtle.circle(80, 40)
turtle.setheading(250)
turtle.circle(-20, 90)
turtle.setheading(180)
turtle.forward(50)
turtle.circle(-40, 90)
turtle.forward(55)
turtle.setheading(140)
turtle.circle(-200, 33)
turtle.setheading(233)
turtle.circle(-53, 188)
turtle.forward(75)
turtle.setheading(90)
turtle.circle(-280, 34)
turtle.setheading(105)
turtle.circle(-100, 35)
turtle.circle(-50, 120)
turtle.setheading(20)
turtle.circle(-260, 37)
turtle.setheading(27)
turtle.circle(-90, 40)
turtle.circle(-50, 110)
turtle.setheading(310)
turtle.circle(-210, 30)
turtle.end_fill()
turtle.penup()

#内层
turtle.goto(150, 175)
turtle.pencolor("black")
turtle.pensize(8)
turtle.pendown()
turtle.setheading(300)
turtle.circle(-308, 72)
turtle.setheading(204)
turtle.circle(-308, 48)
turtle.setheading(133)
turtle.circle(-300, 74)
turtle.setheading(52)
turtle.circle(-208, 102)
turtle.penup()

#耳朵
turtle.fillcolor("black")
turtle.goto(146, 178)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(68)
turtle.circle(57, 76)
turtle.circle(30, 105)
#turtle.setheading(340)
#turtle.circle(-140, 40)
turtle.penup()
turtle.end_fill()

turtle.goto(-174, 177)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(115)
turtle.circle(-57, 76)
turtle.circle(-30, 110)
#turtle.setheading(340)
#turtle.circle(-140, 40)
turtle.penup()
turtle.end_fill()

#手
turtle.goto(190, -27)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(9)
turtle.circle(100, 74)
turtle.circle(29, 155)
turtle.forward(50)
turtle.penup()
turtle.end_fill()

turtle.goto(-218, 10)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(220)
turtle.forward(70)
turtle.circle(50, 76)
turtle.circle(36, 135)
turtle.forward(30)
turtle.penup()
turtle.end_fill()

#脚
turtle.goto(110, -190)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(270)
turtle.forward(70)
turtle.circle(-20, 90)
turtle.forward(60)
turtle.circle(-10, 120)
turtle.forward(13)
turtle.setheading(90)
turtle.forward(45)
turtle.penup()
turtle.end_fill()

turtle.goto(-133, -190)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(270)
turtle.forward(70)
turtle.circle(20, 90)
turtle.forward(60)
turtle.circle(10, 120)
turtle.forward(13)
turtle.setheading(90)
turtle.forward(45)
turtle.penup()
turtle.end_fill()

#圈圈
turtle.pensize(6)
turtle.goto(-198, 40)
turtle.pendown()
turtle.pencolor("limegreen")
turtle.circle(-180, 92)
turtle.circle(-197, 73)
turtle.circle(-122, 102)
turtle.right(1)
turtle.forward(116)
turtle.circle(-138, 90)
turtle.penup()

turtle.goto(-194, 40)
turtle.setheading(90)
turtle.pendown()
turtle.pencolor("gold")
turtle.circle(-175, 95)
turtle.circle(-193, 75)
turtle.right(5)
turtle.circle(-120, 102)
turtle.left(9)
turtle.forward(95)
turtle.circle(-129, 90)
turtle.penup()

turtle.goto(-189, 40)
turtle.setheading(90)
turtle.pendown()
turtle.pencolor("slateblue")
turtle.circle(-171, 95)
turtle.circle(-185, 73)
turtle.right(3)
turtle.circle(-119, 93)
turtle.right(5)
turtle.forward(120)
turtle.circle(-122, 90)
turtle.penup()

turtle.goto(-184, 40)
turtle.setheading(90)
turtle.pendown()
turtle.pencolor("firebrick")
turtle.circle(-167, 95)
turtle.circle(-179, 73)
turtle.right(2)
turtle.circle(-115, 94)
turtle.right(5)
turtle.forward(120)
turtle.circle(-118, 90)
turtle.penup()

turtle.goto(-179, 40)
turtle.setheading(90)
turtle.pendown()
turtle.pencolor("lightskyblue")
turtle.circle(-163, 95)
turtle.circle(-172, 73)
turtle.right(2)
turtle.circle(-113, 94)
turtle.right(5)
turtle.forward(116)
turtle.circle(-113, 90)
turtle.penup()

#五官
turtle.pencolor("black")
turtle.goto(-87, 140)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(200)
turtle.circle(102, 45)
turtle.circle(38, 134)
turtle.circle(102, 45)
turtle.circle(38, 134)
turtle.end_fill()
turtle.penup()

turtle.pencolor("white")
turtle.goto(-81, 114)
turtle.pendown()
turtle.setheading(180)
turtle.circle(25, 360)
turtle.penup()

turtle.goto(-68, 97)
turtle.pendown()
turtle.setheading(180)
turtle.circle(3, 360)
turtle.penup()


turtle.pencolor("black")
turtle.goto(61, 138)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.setheading(340)
turtle.circle(-102, 45)
turtle.circle(-38, 134)
turtle.circle(-102, 45)
turtle.circle(-38, 134)
turtle.end_fill()
turtle.penup()

turtle.pencolor("white")
turtle.goto(56, 114)
turtle.pendown()
turtle.setheading(180)
turtle.circle(25, 360)
turtle.penup()

turtle.goto(64, 97)
turtle.pendown()
turtle.setheading(180)
turtle.circle(3, 360)
turtle.penup()

turtle.pencolor("black")
turtle.goto(0, 73)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.setheading(263)
turtle.circle(-20, 70)
turtle.right(30)
turtle.circle(-20, 70)
turtle.right(85)
turtle.circle(-120, 12)
turtle.end_fill()
turtle.penup()

turtle.pencolor("black")
turtle.goto(-42, 46)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(220)
turtle.circle(50, 80)
turtle.left(24)
turtle.circle(70, 80)
turtle.left(24)
turtle.circle(50, 82)
turtle.end_fill()
turtle.penup()


turtle.setheading(225)
turtle.fillcolor("white")
turtle.pendown()
turtle.begin_fill()
turtle.circle(-47, 80)
turtle.end_fill()
turtle.penup()

turtle.pencolor("black")
turtle.fillcolor("red")
turtle.goto(-49, -15)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(70)
turtle.circle(-45, 137)
turtle.setheading(220)
turtle.circle(-70, 80)
turtle.end_fill()
turtle.penup()


# 五环
turtle.pensize(3)

turtle.pencolor("red")
turtle.goto(15, -160)
turtle.pendown()
turtle.setheading(0)
turtle.circle(-10, 360)
turtle.penup()

turtle.pencolor("black")
turtle.goto(-9, -160)
turtle.pendown()
turtle.setheading(0)
turtle.circle(-10, 360)
turtle.penup()

turtle.pencolor("skyblue")
turtle.goto(-33, -160)
turtle.pendown()
turtle.setheading(0)
turtle.circle(-10, 360)
turtle.penup()

turtle.pencolor("green")
turtle.goto(3, -170)
turtle.pendown()
turtle.setheading(0)
turtle.circle(-10, 360)
turtle.penup()

turtle.pencolor("gold")
turtle.goto(-21, -170)
turtle.pendown()
turtle.setheading(0)
turtle.circle(-10, 360)
turtle.penup()


turtle.pencolor("black")
turtle.goto(-60, -150)
turtle.write("BEIJING 2022", font=('Arial', 14, 'bold italic'))

# 爱心
turtle.goto(245, 65)
turtle.pencolor("red")
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.setheading(25)
turtle.circle(-10, 180)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.circle(-10, 180)
turtle.penup()
turtle.end_fill()


turtle.goto(230, 140)
turtle.pencolor("black")
turtle.write("黄达林专属墩墩", font=('Quicksand', 26, 'normal'))

turtle.hideturtle()


turtle.exitonclick()