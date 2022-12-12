# Y Fractal tree in Python using Turtle
from turtle import *

speed("fastest")

# The acute angle between the base and branch of the Y
angle = 30

# Turn the turtle-socorro to face upwards
left(90)


# Function to plot a Y
def y(size, level):

    if level > 0:  # The conditional for limit the level and the program not being in loop

        colormode(255)

        # Set the rgb range to green into equal intervals for each level
        # bringing the colour according to the current level
        pencolor(0, 255//level, 0)

        # Draw the base tree
        forward(size)
        left(angle)

        # Track an orange circle for each branch
        # representing a fruit or a flower of the tree
        begin_fill()
        color("orange")
        circle(2)
        end_fill()

        # recursive call for the left subtree
        y(0.8*size, level-1)

        pencolor(0, 255//level, 0)
        right(2*angle)

        # recursive call for the right subtree
        y(0.8*size, level-1)

        pencolor(0, 255//level, 0)
        left(angle)

        backward(size)


y(80, 7)

