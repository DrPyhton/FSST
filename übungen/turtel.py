import random
import turtle
from turtle import *

def Haus():

    print(turtle.window_width())
    print(turtle.window_height())
    turtle.speed(0)
    turtle.colormode(255)

    while True:

        haus = random.randint(10, 100)

        corx = random.randint(int(-turtle.window_width()/2), int(turtle.window_width()/2-haus))
        cory = random.randint(int(-turtle.window_height()/2+haus), int(turtle.window_height()/2-haus))
        up()
        setpos(corx, cory)
        down()
        turtle.fillcolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.begin_fill()



        for i in range(4):
            turtle.forward(haus)
            right(90)

        left(60)
        forward(haus)

        right(120)
        forward(haus)

        left(60)
        turtle.end_fill()

Haus()
