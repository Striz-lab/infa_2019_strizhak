#!/usr/bin/python3

import turtle


turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

def circle(n, left):


    for i in range(n):
        turtle.forward(5)
        if left:
            turtle.left(180/n)
        else:
            turtle.left(180/n)




k = int(input())
turtle.left(90)

for i in range(k):

    circle(20, 0)

    circle(5, 1)

turtle.exitonclick()

