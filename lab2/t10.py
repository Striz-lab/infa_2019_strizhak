#!/usr/bin/python3

import turtle


turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

def circle():
    n = 30

    for i in range(n):
        turtle.forward(10)
        turtle.left(360/n)

k = int(input())

for i in range(k):
    turtle.left(360/k)
    circle()

turtle.exitonclick()
