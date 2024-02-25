from turtle import *

### Functions
# Modify code in this section
speed(0)

def star():
    fillcolor("black")
    begin_fill()
    for _ in range (5):
        forward(25)
        right(144)
    end_fill


### The main code that gets run
# Do not modify anything after this line

for i in range(13):
    star()
    penup()
    right(360/13)
    forward(50)
    pendown()

done()
