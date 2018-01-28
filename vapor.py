import turtle
import random as r

#turtle config
t = turtle.Turtle()
s = turtle.Screen()
t.speed(1000)
t.pencolor("#ffffff")
s.bgcolor("#000000")


#geometrics
LEFT    = 1.0
FORWARD = 5
frw_acc = 1
shape   = r.randrange(2,6) #{ 2- linear, 3 - triangle, 4 - square, 5 - pentagon, 6 - hexagon, ...}

#random color
colors = []
for i in range(0,shape):
    color = str('#{0:06x}'.format(r.randrange(0x1,0xffffff)))
    colors.append(color)

#drawwning
for i in range(0,1000):
    for j in range(0,shape):
        t.pencolor(colors[j])
        t.forward(frw_acc)
        t.left((360/shape) + LEFT)
    frw_acc += FORWARD
