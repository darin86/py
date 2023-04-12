import turtle

# Create the turtle object
t = turtle.Turtle()

# Set the background color
turtle.bgcolor("white")

# Set the pen color to pink
t.pencolor("#ff69b4") # This is the hex code for pink

# Draw the body of the rooster
t.begin_fill()
t.fillcolor("#ffc0cb") # This is a lighter shade of pink
t.circle(100)
t.end_fill()

# Draw the head of the rooster
t.up()
t.goto(0, 200)
t.down()
t.begin_fill()
t.fillcolor("#ffc0cb")
t.circle(50)
t.end_fill()

# Draw the comb of the rooster
t.up()
t.goto(0, 240)
t.down()
t.begin_fill()
t.fillcolor("#ff1493") # This is the hex code for deep pink
t.forward(25)
t.right(120)
t.forward(25)
t.right(120)
t.forward(25)
t.right(60)
t.forward(25)
t.right(60)
t.forward(25)
t.right(120)
t.forward(25)
t.right(60)
t.forward(25)
t.right(60)
t.forward(25)
t.right(120)
t.forward(25)
t.end_fill()

# Draw the eyes
t.up()
t.goto(-25, 220)
t.down()
t.begin_fill()
t.fillcolor("#ffffff") # This is the color for the eyes
t.circle(10)
t.end_fill()

t.up()
t.goto(25, 220)
t.down()
t.begin_fill()
t.fillcolor("#ffffff")
t.circle(10)
t.end_fill()

# Draw the beak
t.up()
t.goto(0, 200)
t.down()
t.pencolor("#ffa500") # This is the hex code for orange
t.fillcolor("#ffa500")
t.begin_fill()
t.right(30)
t.forward(40)
t.right(120)
t.forward(40)
t.right(150)
t.forward(30)
t.end_fill()

# Draw the legs
t.up()
t.goto(-35, 0)
t.down()
t.pencolor("#ffa500")
t.fillcolor("#ffa500")
t.begin_fill()
t.right(120)
t.forward(50)
t.right(90)
t.forward(10)
t.right(90)
t.forward(50)
t.right(90)
t.forward(10)
t.end_fill()

t.up()
t.goto(35, 0)
t.down()
t.pencolor("#ffa500")
t.fillcolor("#ffa500")
t.begin_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(10)
t.right(90)
t.forward(50)
t.right(90)
t.forward(10)
t.end_fill()

# Hide the turtle object
t.hideturtle()

# Keep the turtle window open
turtle.done()