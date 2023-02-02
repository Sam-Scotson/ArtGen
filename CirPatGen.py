import turtle
import math
import random
ts=turtle.Screen()
ts.bgcolor('#000000')
tur=turtle.Turtle()
tur.speed(0)
tur.color('#ffffff')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(tur,100,10)
zx=turtle.Turtle()
zx.speed(0)
zx.color('#F800FF')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(zx,100,10)
xc=turtle.Turtle()
xc.speed(0)
xc.color('#C400ff')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCircles(t,size)
        t.right(360/repeat)
