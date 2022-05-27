import turtle
import os


def drawsun():
    s = turtle.Turtle()
    # MAIN OBJECT DRAWN USING A TURTLE
    # USES A LOOP
    # sun shine(orange)
    for i in range(36):
        s.tracer(6)
        s.pensize(3)
        s.penup()
        s.setpos(200,240)
        s.right(10)
        s.pendown()
        s.color("orange")
        s.forward(90)
    # middle of sun
    s.penup()
    s.setpos(200, 200)
    s.pendown()
    s.fillcolor("yellow")
    s.begin_fill()
    s.color("yellow")
    s.pensize(25)
    s.circle(40, 360)
    s.end_fill()
    # sun shine(yellow)
    for i in range(13):
        s.pensize(6)
        s.setpos(200, 240)
        s.penup()
        s.right(30)
        s.pendown()
        s.color("yellow")
        s.forward(100)


def drawwave(x, y, color):
    waves = turtle.Turtle()
    # USES TRACER
    waves.tracer(7)
    waves.pensize(10)
    waves.penup()
    waves.setpos(x,y)
    waves.pendown()
    waves.color(color)
    for i in range(6):
        # creates waves
        waves.circle(50, 70)
        waves.circle(-60, 90)
        waves.right(125)
        waves.circle(50, 95)
        waves.left(50)
        waves.forward(10)


def drawwaves():
    DARK_BLUE = (72, 206, 219)
    drawwave(-350,0,DARK_BLUE)
    drawwave(-350,-100,DARK_BLUE)
    drawwave(-350, -200, DARK_BLUE)
    drawwave(-350, -300, DARK_BLUE)


# main function starts here
wn = turtle.Screen()
wn.colormode(255)

# background color
# HAS A BACKGROUND
# USES A COLOR FOUND IN PHOTOSHOP
LIGHT_BLUE = (167,209,217)
wn.bgcolor(LIGHT_BLUE)

# draws sun
drawsun()

#square=turtle.Turtle()
# draws waves
drawwaves()
drawwaves()

# USES AN IMPORTED IMAGE
# REFLECTS SOMETHING ABOUT WHO I AM
# I chose this image because I have been swimming since I was 7 and it is a very big part of my life
wn.addshape(os.path.expanduser("giphy.gif"))
image = turtle.Turtle()
image.shape(os.path.expanduser("giphy.gif"))
# had to add this since the image did not render
image.penup()
image.setpos(0,70)
image.circle(1)

turtle.exitonclick()
