import turtle
from turtle import *

wn = turtle.Screen()
turtle.title("I LOVE YOU JULIA!")
wn.bgcolor('black')

t = turtle.Turtle()
t.pencolor('white')

def curve():
    for i in range(200):
        t.speed(100)
        t.rt(1)
        t.fd(1)

def heart():
    t.speed(100)
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write(message, pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style = ('Stencil Std', 18, 'italic')
    t.write(message,font=style)

write('I',(-68,95))
write('L',(-55,95))
write('O',(-42,95))
write('V',(-30,95))
write('E',(-14,95))
write('Y',(10,95))
write('O',(26,95))
write('U',(45,95))

write('B',(-130,180))
write('E',(-117,180))

write('M',(-93,180))
write('Y',(-75,180))

write('V',(-56,180))
write('A',(-43,180))
write('L',(-30,180))
write('E',(-17,180))
write('N',(-4,180))
write('T',(9,180))
write('I',(22,180))
write('N',(30,180))
write('E',(48,180))
write('?',(61,180))

wn.mainloop()
