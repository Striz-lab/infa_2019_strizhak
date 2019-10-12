#!/usr/bin/python3

import turtle


turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)


turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
n = 200
turtle.begin_fill()
for i in range(n):
    turtle.color('black', 'yellow')

    turtle.forward(5)
    turtle.left(360/n)
turtle.end_fill()

k=40
turtle.penup()
turtle.goto (-60, 100)
turtle.pendown()
turtle.begin_fill()
for i in range(k):
    turtle.color('black', 'blue')
    turtle.forward(5)
    turtle.left(360/k)
turtle.end_fill()

k=40
turtle.penup()
turtle.goto (60, 100)
turtle.pendown()
turtle.begin_fill()
for i in range(k):
    turtle.color('black', 'blue')
    turtle.forward(5)
    turtle.left(360/k)
turtle.end_fill()


turtle.penup()
turtle.goto(0, 70)
turtle.pendown()
turtle.color('black', 'black')
turtle.right(90)
turtle.width(7)
turtle.forward(70)


turtle.penup()
turtle.goto(-78, 0)
turtle.pendown()
turtle.color('red')
n = 50
for i in range(n):
    turtle.color('red', 'black')
    
    turtle.forward(5)
    turtle.left(180/n)

turtle.penup()
turtle.forward(5000)
