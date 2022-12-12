# Program Triangle in Python Turtle
import turtle

# Get s screen on a new window
s = turtle.Screen()

# Create t object
t = turtle.Turtle()


def make_triangle(x, y):
    # drawing out the pen
    t.penup()

    # move object at x and y position
    t.goto(x, y)

    # drawing in the pen
    t.pendown()

    for i in range(3):
        # move object 100 unit forward
        t.forward(100)

        # turn object 120 degree left
        t.left(120)

        # again movie object 100 unit forward
        t.forward(100)


# Built-in function that when left-click
# the object will move to current position
# of the cursor and make a triangle
turtle.onscreenclick(make_triangle, 1)

turtle.listen()  # Set the events of click to occur on turtle-socorro screen

# Hold the screen
turtle.done()
