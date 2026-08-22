'''from turtle import *
import colorsys
speed(0)
hideturtle()
bgcolor('black')
tracer(5)
width(2)
h = 0.001
for i in range (90):
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(50)
    left(240)
    forward(100)
    left(60)
    forward(100)
    h +=0.02
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    right(120)
    forward(100)
    left(120)
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)
    h +=0.02
done()'''


          
    
import math
from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
         math.cos(2*k)-2*\
         math.cos(3*k)-\
         math.cos(4*k)
speed(100000)
bgcolor('black')
for i in range(600000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f734a9")
    goto(0,0)
done()        
