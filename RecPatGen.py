import turtle
from turtle import*

tv=turtle.Screen()
tur=turtle.Turtle()
speed(0)

tur.penup()
tur.goto(-400,250)
tur.pendown()

tur.color("blue")
tur.begin_fill()
tur.forward(800)
tur.right(90)
tur.forward(167)
tur.right(90)
tur.forward(800)
tur.end_fill()
tur.left(90)
tur.forward(167)

tur.color("red")
tur.begin_fill()
tur.forward(167)
tur.left(90)
tur.forward(800)
tur.left(90)
tur.forward(167)
tur.end.fill()

tur.penup()
tur.goto(70,0)
tur.pendown()