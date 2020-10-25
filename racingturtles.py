import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.penup()
andy.penup()
lance.color('orange')
andy.color('yellow')
lance.shape('turtle')
andy.shape('turtle')

 # 4.  Move the turtles to their starting point

andy.setpos(-100,20)
lance.setpos(-100,-20)


# your code goes here

for i in range(30):
    x = random.randrange(1,10)
    y = random.randrange(1,10)
    andy.forward(x)
    lance.forward(y)

wn.exitonclick()
