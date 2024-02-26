from turtle import *
speed(0)
setup(600,400)

def bar(color_name, width, height):
    color(color_name)
    begin_fill()
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    end_fill()

def star():
    fillcolor("black")
    begin_fill()
    for _ in range(5):
        forward(80)
        right(144)
    end_fill()

penup()
goto(-300,200)
pendown()

bar("red", 600, 133)

penup()
goto(-300,66)
pendown()
bar("yellow", 600, 133)


penup()
goto(-300, -67)
pendown()
bar("dark green", 600, 133)

penup()
goto(-50, 20)
pendown()
star()

done()