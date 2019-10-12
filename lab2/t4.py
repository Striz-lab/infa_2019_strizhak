#!/usr/bin/python3

import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

n = int(input())

for i in range(n):
    turtle.forward(1)
    turtle.left(360/n)

turtle.exitonclick()
