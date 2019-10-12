#!/usr/bin/python3

import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

def star(n):

    for i in range(int(2*n)):
        turtle.forward(200)
        turtle.left(180-180/n)

n = int(input())

star(n)

turtle.exitonclick()
