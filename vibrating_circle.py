
#   importing the library to our workspace so that
#   we can use the funcitonalities which are present
#   in them.

from turtle import *
from random import *

#   setting up the background color for our drawing-board
bgcolor('black')

#   declare variable for movement and direction of the cursor
forwrd=0
rght=0

#   setting up the speed of cursor
speed(0)

#   it is used to define the shape of the cursor
shape('classic')

#   goto() is used for positioning the cursor over the user window
goto(-window_width()//15,150)

#   created this array for making vibrating circle colorfull!
array_of_colors=['blue','green','orange','red','cyan','chocolate','deeppink','white']

#   DESIGNING OF VIBRATING-CIRCLE
while(True):
    # here i use choice() of RANDOM which randomly choose the color from
    # array_of_colors and then pass them to color() of TURTLE
    color(choice(array_of_colors))

    # this is used for the forward movement of the cursor
    forward(forwrd)
    # this is used for changing the direction of the cursor
    right(rght)

    forwrd+=3
    rght+=1

    # this is used to stop the circle when the angle becomes equal to 200
    if(rght==200):
        break

# this is used to start the event
done()

# CodeBy:RahulMahajan
# CF:anonymous3107
# CC:anonymous0201
# CSES:rahulmahajan