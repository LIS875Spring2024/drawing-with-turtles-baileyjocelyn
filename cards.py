from turtle import *
speed(0)
setup(1000,400)

#####  Functions that draw card shapes
# Note: Do not modify any code in this section

def diamond():
    fillcolor("red")
    begin_fill()
    setheading(90)
    left(30)
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    forward(50)
    end_fill()
    setheading(0)

def heart():
    fillcolor("red")
    begin_fill()
    setheading(90)
    right(30)
    forward(72)
    left(30)
    circle(18, 180)
    left(180)
    circle(18, 180)
    left(30)
    forward(72)
    end_fill()
    setheading(0)

def club():
    fillcolor("black")
    begin_fill()
    setheading(0)
    forward(8)
    left(105)
    forward(30)
    left(150)
    forward(30)
    left(105)
    forward(8)
    end_fill()
    
    setheading(90)
    forward(50)
    right(90)
    begin_fill()
    circle(18)
    end_fill()
    begin_fill()
    left(120)
    circle(18)
    end_fill()
    begin_fill()
    left(120)
    circle(18)
    end_fill()
    setheading(270)
    forward(50)
    setheading(0)


def spade():
    fillcolor("black")
    setheading(0)
    begin_fill()
    forward(15)
    left(120)
    forward(30)
    left(120)
    forward(30)
    left(120)
    forward(15)
    end_fill()

    setheading(90)
    forward(25)
    left(180)
    left(45)
    begin_fill()
    circle(18,180)
    forward(36)
    left(90)
    forward(36)
    circle(18, 180)
    end_fill()
    left(45)
    back(25)
    setheading(0)


#### The main code that gets run
# Only modify code below this line
def move_next():
    setheading(0)
    penup()
    forward(200)
    pendown()

penup()
goto(-200,0)
pendown()
club()
move_next()

penup()
goto(0,0)
pendown()
heart()
move_next()

penup()
goto(200,0)
pendown()
diamond()

penup()
goto(400,0)
pendown()
spade()

done()
