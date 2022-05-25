import time
import turtle

uhr = turtle.Turtle()
screen = uhr.getscreen()
turtle.tracer(0)

def blatt():
    global uhr
    uhr.pensize(20)
    uhr.pencolor('black')
    uhr.penup()
    uhr.goto(0, -300)
    uhr.setheading(0)
    uhr.pendown()
    uhr.circle(300)
    for i in range(0, 360, 30):
        uhr.penup()
        uhr.goto(0, 0)
        uhr.setheading(90 - i)
        uhr.forward(280)
        uhr.pendown()
        uhr.forward(20)


def zeiger():
    global uhr
    uhr.penup()
    uhr.goto(0, 0)
    sek = int(time.strftime('%S'))
    min = int(time.strftime('%M'))
    h = int(time.strftime('%I'))

    uhr.setheading(90 - 30 * h)
    uhr.pendown()
    uhr.pensize(20)
    uhr.pencolor('blue')
    uhr.forward(220)

    uhr.penup()
    uhr.goto(0,0)
    uhr.setheading(90 - 6 * min)
    uhr.pendown()
    uhr.pensize(20)
    uhr.forward(260)

    uhr.up()
    uhr.goto(0, 0)
    uhr.setheading(90 - 6 * sek)
    uhr.down()
    uhr.pencolor('red')
    uhr.pensize(10)
    uhr.forward(280)


if __name__ == "__main__":
    while True:
        blatt()
        zeiger()
        screen.update()
        uhr.clear()









