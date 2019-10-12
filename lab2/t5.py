#!/usr/bin/python3

import turtle


turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

a=10
b=10
turtle.penup()
turtle.pendown()
for i in range(10):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    a += 10
    turtle.penup()
    turtle.right(45)
    turtle.forward(7)
    turtle.left(135)
    turtle.pendown()

turtle.exitonclick()
