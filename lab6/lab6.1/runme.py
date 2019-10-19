from tkinter import *
from random import randrange as rnd, choice
import time
import math
import array
root = Tk()

updateTime = 30
balls = []
shapes = []


c = Canvas(root, width=960, height=760, bg='white')
c.pack()
root.geometry('960x760')
colors = ['red','orange','yellow','green','blue', 'purple']

ptr = 1
LVL = 1
k = 0
tim = 0
parametr=1

'''
создание класса шаров
'''

class Ball:
    global parametr

    def __init__(self):
        self.x = rnd(60, 700)
        self.y = rnd(60, 700)
        self.dx = rnd (-7*parametr, 7*parametr)
        self.dy = rnd (-7*parametr, 7*parametr)
        self.r = rnd (30, 50)
        
        self.object = c.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill = choice(colors), width=0)
        

    def rebound_ball(self):
        if self.y <= self.r or self.y >= 760-self.r:
            self.dy = -self.dy
        if self.x <= self.r or self.x >= 760-self.r:
            self.dx = -self.dx

      
    def move_ball(self):
        c.move(self.object, self.dx, self.dy)
        self.y += self.dy
        self.x += self.dx


    def detectCatch(self, xe, ye):
        a = ((xe-self.x)**2 + (ye-self.y)**2)**0.5
        return a < self.r
        if a < self.r:
            k += 1
            lvl += 1


    def delete(self):
        self.x = 10000
        self.y = 10000
        c.delete(self.object)
 
'''
создание класса не шаров
'''

class Shape:
    global parametr, ptr
    
    def __init__(self):
        self.x = rnd(70, 690)
        self.y = rnd(130, 530)
        self.dx = rnd (-3*parametr, 3*parametr)
        self.dy = rnd (-3*parametr, 3*parametr)
        self.r = rnd (30, 70)
        self.a1 = rnd(50, 100)
        self.w1 = rnd(1*parametr,100*parametr)
        self.w1 = self.w1/1000
        self.b1 = rnd(50, 100)
        
        
        m = choice(colors)
        self.object = c.create_rectangle(self.x, self.y, self.x+self.r, self.y+2*self.r,fill = m, outline = m, width=3 )


    def move_shape(self):
        c.move(self.object, self.dx, self.dy)
        self.dx = -self.a1*self.w1*math.sin(self.w1*ptr)
        self.dy = self.b1*self.w1*math.cos(self.w1*ptr)
        self.y += self.dy
        self.x += self.dx


    def detectCatch_shape(self, xi, yi):
        return (self.x < xi)*(self.x+self.r > xi)*(self.y < yi)*(self.y+2*self.r > yi) == 1


    def delete(self):
        self.x = 10000
        self.y = 10000
        c.delete(self.object)
        

'''
обновить
'''

def updateScene():
    global ptr
    for b in balls:
        b.move_ball()
        b.rebound_ball()
    for d in shapes:
        d.move_shape()
        
    ptr += 1
    root.after(updateTime, updateScene)
    

#клик мыши


def mouseClick(event):
    global k, LVL, tim, parametr
    
    for i in range(len(balls)):
        if balls[i].detectCatch(event.x, event.y):
            k+=1
            tim +=1
            balls[i].delete()
            c.create_rectangle(925, 205, 773, 235, fill='yellow', outline='yellow')
            c.create_text(873, 225, text=k,
            anchor=SE, fill="black")

        if tim == n+f:
            #c.delete(ALL)
            tim = 0
            LVL += 1
            c.create_rectangle(845, 133, 870, 177, fill='yellow', outline='yellow')
            c.create_text(863, 155, text=LVL,
            anchor=SE, fill="black")
            realise()
            parametr += 1
        
    for j in range(len(shapes)):
        if shapes[j].detectCatch_shape(event.x, event.y):
            k+=10
            tim+=1
            shapes[j].delete()
            c.create_rectangle(925, 205, 773, 235, fill='yellow', outline='yellow')
            c.create_text(873, 225, text=k,
            anchor=SE, fill="black")

        if tim == n+f:
            #c.delete(ALL)
            tim = 0
            LVL += 1
            c.create_rectangle(845, 133, 870, 177, fill='yellow', outline='yellow')
            c.create_text(863, 155, text=LVL,
            anchor=SE, fill="black")
            realise()
            parametr += 1
    if k >= 1000:
        c.delete(ALL)
        c.create_text(500, 350, text= 'YOU WIN',
        anchor=SE, fill="black")
            
 
#самое важное


def realise():
    global n,f, tim
    f = rnd(0,20)
    n = rnd(0, 50)
    c.bind('<Button-1>', mouseClick)
    for i in range(n):
        balls.append(Ball())


    for i in range(f):
        shapes.append(Shape())

    

realise()

'''
создание виджетов:
сначала цветные квадраты, потом тексты, данные обновляются в функции прокликивания
'''

c.create_line(4, 4, 4, 757, 757, 757, 757, 4)

c.create_rectangle(955, 5, 763, 95, fill='orange', outline='green',
                    width=3, activedash=(5, 4))

c.create_rectangle(955, 105, 763, 285, fill='yellow', outline='green',
width=3, activedash=(5, 4))

c.create_rectangle(955, 295, 763, 755, fill='purple', outline='green',
width=3, activedash=(5, 4))

c.create_text(885, 30, text="PLAYER:",
                anchor=SE, fill="black")

c.create_text(873, 125, text="LVL:",
anchor=SE, fill="black")

c.create_text(863, 155, text=1,
anchor=SE, fill="black")

c.create_text(883, 200, text="SCORE:",
anchor=SE, fill="black")

c.create_text(905, 317, text="CHAMPIONS:",
anchor=SE, fill="black")

'''
авторизация пользователя
'''

e = Entry(root, width=18)
b = Button(text="confirm")
l = Label(bg='black', fg='white', width=20)

def strToSortlist(event):
    global name
    name = e.get()
    text_f = open('text.txt', 'a')
    #text_f.write("\n")
    text_f.write(name)
    text_f.write(' ')
    l['text'] = ' '.join(name)

b.bind('<Button-1>', strToSortlist)
e.place(x=772, y=35)
b.place(x=830, y=65)

for i in range(20):
    c.create_text(780, 340+i*20, text = i+1,
    anchor=SW, fill="black")
text_f = open('text.txt', 'r')
i = 0
for line in text_f:
    i+=1
    c.create_text(810, 335+i*20, text = line, anchor=SW, fill="black")
root.after(updateTime, updateScene)


mainloop()
'''
работа с файлом и вывод таблицы лучших игроков на экран
'''

text_f = open('text.txt', 'a')
text_f.write(str(k))

text_f = open('text.txt', 'r')

s=0

for line in text_f:
    s += 1

text_f = open('text.txt', 'r')
Name = [0]*s
BRS = [0]*s
for i in range (s):
    sesc = text_f.readline().split()
    Name[i] = sesc[0]
    BRS[i] = sesc[1]

for i in range (s):
    BRS[i] = int(BRS[i])

for j in range (s-1):
    for i in range (s-j-1 ):
        if (BRS[i+1] > BRS [i]):
            BRS[i], BRS[1+i] = BRS[1+i], BRS[i]
            Name[i], Name[1+i] = Name[1+i], Name[i]

for i in range(s):
    BRS[i] = str(BRS[i])
    
    
text_f = open('text.txt', 'w')
for i in range (s):
    text_f.write(Name[i])
    text_f.write(' ')
    text_f.write(BRS[i])
    text_f.write("\n")


text_f.close()


    
    
    
    
root.mainloop()
