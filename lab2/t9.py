#!/usr/bin/python3

import turtle
import math as m

turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

def DrawPolygon (n, side):
    for i in range (n):
        turtle.forward (side)
        turtle.left(360/n)

def PolygonInside (n, R0, x, y):
    i = 0
    turtle.left(90)
    R = R0
    while i < n:
        side = 2*R*m.sin (m.pi/(i+3))
        turtle.penup()
        turtle.goto(x, y - R)
        turtle.pendown()
        turtle.right ((3+i-2)*180/(2*(i+3)))
        DrawPolygon (i+3, side)
        turtle.left ((3+i-2)*180/(2*(i+3)))
        R += 10
        i += 1

n = int(input())
R0 = int(input())

PolygonInside (n, R0, 0, 0)
turtle.exitonclick()
