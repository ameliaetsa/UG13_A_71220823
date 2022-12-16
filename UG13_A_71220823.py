import turtle
s = turtle.Screen()
#turtle object
a = turtle.Turtle()

#draw N
a.penup()
a.goto(-350,0)
a.pendown()
a.left(90)
a.forward(100)
a.left(-135)
a.forward(140)
a.right(225)
a.forward(103)
a.penup()

#draw 8
a.goto(-180,60)
a.pendown()
a.right(90)
a.pendown()
a.circle(25)
a.circle(-30)
a.penup()

#draw 2
a.goto(-125,105)
a.pendown()
a.left(-360)
a.forward(50)
a.right(90)
a.forward(50)
a.left(-90)
a.forward(50)
a.left(90)
a.forward(50)
a.right(-90)
a.forward(50)
a.penup()

#draw 3
a.goto(-30,105)
a.pendown()
a.left(-360)
a.forward(50)
a.right(90)
a.forward(50)
a.left(-90)
a.forward(50)
a.right(180)
a.forward(50)
a.right(90)
a.forward(50)
a.right(90)
a.forward(50)
a.penup()

#draw A
a.goto(90,105)
a.pendown()
a.left(70)
a.forward(110)
a.right(180)
a.forward(60)
a.right(70)
a.forward(50)
a.left(120)
a.forward(60)
a.right(180)
a.forward(130)
a.penup()





s.exitonclick()