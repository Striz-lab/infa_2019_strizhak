from tkinter import *
from random import randrange as rnd, choice
import time
import math
import array
root = Tk()


c = Canvas(root, width=760, height=760, bg='white')
c.pack()
root.geometry('760x760')


lvl = 0
k = 0


canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)


'''
создание двух фигур
'''


colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x, y, r, dx, dy, ball, n, x1, y1, r1, dx1, dy1, shape, n1
    c.delete(ALL)
    n = rnd(1,10)    #шарики от 1 до 10
    x = [0]*n
    y = [0]*n
    dx = [0]*n
    dy = [0]*n
    r = [0]*n
    for i in range (n):
        x[i] = rnd(60,700)
        y[i] = rnd(60,700)
        dx[i] = rnd(-10,10)
        dy[i] = rnd(-10,10)
        r[i] = rnd(30,50)
    
    ball = [0]*n
    for i in range(n):
        ball[i] = c.create_oval(x[i]-r[i],y[i]-r[i],x[i]+r[i],y[i]+r[i],fill = choice(colors), width=0)

    root.after(2000,new_ball)


'''
движение шара
'''


def move_ball():
    global x,y,dx,dy,ball,n
    for i in range(n):
        c.move(ball[i],dx[i],dy[i])
        y[i] += dy[i]
        x[i] += dx[i]
    root.after(10, move_ball)
    rebound_ball()


'''
отскок шара
'''


def rebound_ball():
    global x,y,dx,dy,ball,n
    for i in range(n):
        if y[i] <= r[i] or y[i] >= 760-r[i]:
            dy[i] = -dy[i]
        if x[i] <= r[i] or x[i] >= 760-r[i]:
            dx[i] = -dx[i]


'''
функции: *вызываються*
'''



new_ball()
move_ball()


mainloop()
