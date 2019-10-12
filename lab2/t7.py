#!/usr/bin/python3

import turtle
import math as m
turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)


def DrawSpiral (n, k, alpha):
    i = 0
    while i < (n*360/alpha):
        turtle.left(alpha)
        i += 1
        turtle.forward (k*m.radians(alpha)*m.sqrt(1+(m.radians(i*alpha)**2)))
a = int(input())
b = int(input())


DrawSpiral(a, b, 10)
turtle.exitonclick()
