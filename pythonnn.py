import turtle
mypen = turtle.Turtle()
mypen.penup()
mypen.forward(100)
mypen.pendown()
mypen.color("gold2")
mypen.speed(100)
mypen.begin_fill()
for i in range(1):
    mypen.right(90)
    mypen.left(0)
    mypen.backward(300)
    mypen.left(90)
    mypen.backward(150)
    mypen.right(90)
    mypen.forward(300)
    mypen.left(90)
    mypen.forward(150)
mypen.end_fill()
mypen.right(90)
mypen.left(0)
mypen.backward(300)
mypen.left(90)
mypen.backward(150)
mypen.right(90)
mypen.forward(300)
mypen.left(90)
mypen.forward(150)
mypen.color("green")
mypen.penup()
mypen.goto(25, 225)
mypen.pendown()
mypen.fillcolor("black")
mypen.begin_fill()
for i in range(1):
    mypen.circle(35)
mypen.end_fill()
mypen.fillcolor("green")
mypen.begin_fill()
for i in range(1):
    mypen.circle(30)
mypen.end_fill()
mypen.circle(30)
mypen.penup()
mypen.goto(25, 125)
mypen.pendown()
mypen.fillcolor("black")
mypen.begin_fill()
for i in range(1):
    mypen.circle(35)
mypen.end_fill()
mypen.goto(25, 125)
mypen.color("yellow")
mypen.goto(25, 125)
mypen.pendown()
mypen.begin_fill()
for i in range(1):
    mypen.circle(30)
mypen.end_fill()
mypen.circle(30)
mypen.penup()
mypen.goto(25, 25)
mypen.pendown()
mypen.fillcolor("black")
mypen.begin_fill()
for i in range(1):
    mypen.circle(35)
mypen.end_fill()
mypen.pendown()
mypen.color("red")
mypen.begin_fill()
for i in range(1):
    mypen.circle(30)
mypen.end_fill()
mypen.circle(30)
mypen.penup()
mypen.color("white")
mypen.goto(-80, 225)
