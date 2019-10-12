#!/usr/bin/python3

import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

n = int(input())

for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.penup()
    turtle.backward(100)
    turtle.right(360/n)
    turtle.pendown()
turtle.exitonclick()
