from turtle import *

### Function that draws stars of different sizes
# Do not modify code in this section

def star(size):
    for i in range(5):
        forward(size)
        right(144)


### Main code area
# Modify code below this line

penup()
goto(100,0)
pendown()

star(25)

penup()
goto(150,0)
pendown()

star (50)

penup()
goto(250,0)
pendown()
star(100)

done()

