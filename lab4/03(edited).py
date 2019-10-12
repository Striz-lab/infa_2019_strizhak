from graph import*
windowSize(720, 500)
canvasSize(2000, 2000)

brushColor(100, 200, 200)
rectangle(0, 0, 720, 500)

brushColor(20, 200, 0)
penColor(20, 200, 0)
rectangle(0, 300, 720, 720)
penColor(0, 0, 0)


def ellipsee(x, y, a, b, fi):
    penColor('orange')
    c=math.cos(fi)
    d=math.sin(fi)
    penSize(2)
    
    for i in range (-a,a):
        v = (b**2-(i*b/a)**2)**0.5
        for j in range (-b,b):
            
            if  abs(j) <= v:
                x1 = i*c+j*d
                y1 = j*c-i*d
                x2 = x1+x
                y2 = y1+y
                
                point (x2, y2, -1)

def ellipseee(x, y, a, b, fi):
    penColor('black')
    c=math.cos(fi)
    d=math.sin(fi)
    penSize(2)
    
    for i in range (-a,a):
        v = (b**2-(i*b/a)**2)**0.5
        for j in range (-b,b):
            
            if  abs(j) <= v:
                x1 = i*c+j*d
                y1 = j*c-i*d
                x2 = x1+x
                y2 = y1+y
                
                point (x2, y2, -1)


def ellipse(x0, y0, a, b):
	x=x0-b
	y=y0
	N=100
	dx=2*b/N
	penSize(0)
	brushColor(130, 130, 130)
	while (x<x0+b) :
		rectangle(x, y, x+dx, 2*y0-y)
		x=x+dx
		y=y0+a*(1-(x-x0)**2/b**2)**0.5
		
	brushColor(180,180,180)
	circle(x0, y0-(a+10), 20)
	
	penSize(2)
	line(x0-15, y0-35, x0-50, y0+20)
	line(x0+15, y0-35, x0+50, y0+20)
	polyline([(x0-10, y0+45), (x0-20, y0+80), (x0-30, y0+80)])
	polyline([(x0+10, y0+45), (x0+20, y0+80), (x0+30, y0+80)])
	penSize(1)
	#byket(x0-100, y0+10)
	
def woman(x0, y0):
    brushColor(150, 10, 100)
    penColor(150, 10, 100)
    polygon([(x0, y0), (x0+25, y0+100), (x0-25, y0+100)])
    penSize(0)
    brushColor(180,180,180)
    penColor(180,180,180)
    penColor(0,0,0)
    circle(x0, y0, 15)
    penSize(1)
    polyline([(x0-10, y0+100), (x0-10, y0+130), (x0-20, y0+130)])
    polyline([(x0+10, y0+100), (x0+10, y0+130), (x0+20, y0+130)])

	
def love(x0, y0):
    line(x0, y0, x0-2, y0-30)
    x0-=2;y0-=30
    brushColor(250, 0, 0)
    penColor(250,0,0)
    penSize(0)
    polygon([(x0, y0), (x0, y0-80), (x0-30, y0-70)])
    circle(x0-23, y0-70,10)
    circle(x0-8, y0-75,10)
    penColor(0,0,0)
	
def byket1(x0, y0):
    brushColor('yellow')
    penColor('yellow')
    polygon([(x0, y0), (x0+30, y0-10), (x0+10, y0-30)])
    brushColor(150, 10, 10)
    penColor(150, 10, 10)
    circle(x0+25, y0-15, 7.5)
    brushColor(250, 0, 0)
    penColor(250,0,0)
    circle(x0+15, y0-25, 7.5)
    brushColor(250, 250, 250)
    penColor(250,250,250)
    circle(x0+25, y0-25, 7.5)
    penColor(0,0,0)


def byket2(x0, y0):
    brushColor('yellow')
    penColor('yellow')
    polygon([(x0, y0), (x0+20, y0-30), (x0-20, y0-30)])
    brushColor(150, 10, 10)
    penColor(150,10,10)
    circle(x0-10, y0-35, 12)
    brushColor(250, 0, 0)
    penColor(250, 0, 0)
    circle(x0+10, y0-35, 12)
    brushColor(250, 250, 250)
    penColor(250, 250, 250)
    circle(x0, y0-45, 12)
    penColor(0,0,0)



def family(x,y,h):
    ellipse (100, 1.635*x, 2*h, h)
    love(50,320)
    woman(190, 250)
    line(x, y, 150, 320)
    woman(300, 250)
    ellipse(390, 1.635*x, 2*h, h)
    line(305, 270, 340, 320)
    byket1(440, 320)

def kit(x,y,h):
    
    
    penColor('orange')
    brushColor('orange')
    polygon([(x-1.5*h,y),(x-1.3*h,y+1.5*h),(x-1.7*h,y+2*h),(x-2.5*h,y+1.7*h),(x-2.25*h,y+0.3*h)])
    ellipsee(x-(2.25*h+2.5*h)/2, y+h, int(h/5), int(5*h/6), -19*3.14/180)
    ellipsee(x-(1.7*h+2.5*h)/2, y+(1.7*h+2*h)/2, int(2*h/3), int(h/5), (-20)*3.14/180)
    brushColor(20, 200, 0)
    penColor(20, 200, 0)
    polygon([(x-1.3*h,y+1.5*h),(x-2.1*h,y+2.5*h),(x-1.2*h, y+2.1*h)])
    
    brushColor('white')
    penColor('white')
    ellipsee(x,y,int(2*h),h,0)
    
    brushColor('orange')
    penColor('orange')
    polygon([(x+h/7,y-7*h/6),(x+h/7,y+7*h/6),(x,y+14*h/7),(x-h/2,y+17*h/7),(x-5*h/6,y+10*h/7)])
    brushColor('orange')
    penColor('orange')
    circle(x-h/8,y+2*h/3-h/8,h/4)
    polygon([(x,y+2*h/3),(x,y-2*h/3),(x-h,y-1.5*h),(x-2*h,y-2*h/3),(x-2*h, y+5*h/6)])
    ellipsee(x-(h/2+5*h/6)/2, y+(27*h/7)/2, int(1.2*h/2), int(h/2), 12*3.14/180)
    
    ellipsee(x, y, int(h/4), int(2*h/3), 0)
    
    ellipsee(x-h/2, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3+h/10), -40)
    ellipsee(x-1.5*h, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3), 40)
    ellipsee(x-2*h, y-(2*h/3-5*h/6)/2, int(h/4), int(2*h/3+h/7), 0)
    ellipsee(x-h, y+(5*h/6+2*h/3)/2, int(h/4), int(2*h/3+h/3), -88*3.14/180)
    
    
    circle(x-h-h/10, y+h/3-2*h/10, h/3)
    ellipseee(x-2*h, y+h/3-1.5*h/5, int(h/4), int(h/3), 0 )
    ellipseee(x-2*h+h/10, y+h-h/5, int(h/3), int(h/4), 0 )
    brushColor('black')
    ellipseee(x-2*h+h/10, y-(5*h/6+2*h/3)/2-h/3, int(h/4), int(h/3+h/3), -40*3.14/180)
    ellipseee(x, y-(5*h/6+2*h/3)/2-h/15, int(h/4), int(h/3+h/3), 30*3.14/180)
    
    circle(x-1.1*h,y+0.25*h,h/4)
    
    ellipseee(x+1.2*h,y+1.3*h,int(1.3*h),int(0.5*h), 60*3.14/180)
    ellipseee(x+1.6*h,y-1.1*h,int(1.3*h),int(0.3*h), 30)


    polyline([(195, 270),(220, 260), (245, 240), (270, 260), (295, 270)])
    line(245, 240, 260, 140)
    byket2(260, 140)


family(185, 270, 25)
ellipse(600, 400, 50, 25)
ellipse(500, 400, 50, 25)
byket1(650, 420)
woman(650, 200)
line(660,240, 660+35, 50+240)
line(640,240, 640+35, 50+240)
kit(680,270,15)
penColor('yellow')
brushColor('yellow')
circle(720, 0, 150)


#ellipse(500, 300, 50,20)



run()
