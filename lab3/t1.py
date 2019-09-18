from graph import *

windowSize(500, 500)
width, height = windowSize()

brushColor("#64A8D1")
penColor("#64A8D1")
rectangle(0, 0, 500, 220)

brushColor("#4A11AE")
penColor("#4A11AE")
rectangle(0, 220, 500, 400)

brushColor("yellow")
penColor("yellow")
rectangle(0, 350, 500, 500)

brushColor("white")
penColor("black")

circle(120, 60, 20)
circle(140, 60, 20)
circle(105, 80, 20)
circle(130, 80, 20)
circle(150, 80, 20)
circle(160, 60, 20)
circle(170, 80, 20)

brushColor("yellow")
penColor("yellow")
circle(430, 70, 40)

#зонтик

brushColor("orange")
penColor("orange")
rectangle(85, 470, 95, 290)


#корабль

brushColor("brown")
penColor("brown")
rectangle(185, 250, 395, 290)

brushColor("black")
penColor("black")
rectangle(255, 250, 265, 130)

array = [395, 290, 395, 250, 420, 250]

polygon(points)

brushColor("white")
penColor("black")
penSize("3")
circle(413, 267, 10)
penSize("1")



run()
