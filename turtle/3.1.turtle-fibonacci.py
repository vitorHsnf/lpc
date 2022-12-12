# Plotting Fibonacci spiral fractal
# in Python using Turtle
import turtle
from math import pi

turtle.Screen()
turtle.title("Turtle Fibonacci Fractal")

x = turtle.Turtle()


def plot_fibo():

    # The initial values of Fibonacci and the squares
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Setting the color of the plotting pen to red
    x.pencolor("red")

    # Drawing the First Square
    x.forward(b*factor)
    x.left(90)
    x.forward(b*factor)
    x.left(90)
    x.fd(b*factor)
    x.left(90)
    x.fd(b*factor)

    # Proceeding the Fibonacci Series
    temp = square_b
    square_b += square_a
    square_a = temp

    # Drawing the 'n' squares in sequence

    for i in range(1, n):

        x.backward(square_a*factor)
        x.right(90)
        x.fd(square_b*factor)
        x.left(90)
        x.fd(square_b*factor)
        x.left(90)
        x.fd(square_b*factor)

        # Proceeding the Fibonacci Series
        temp = square_b
        square_b += square_a
        square_a = temp

    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.setheading(0)
    x.pendown()

    # Colour of the plotting pen to red
    x.pencolor("blue")

    # Fibonacci Spiral Plot
    x.left(90)

    for i in range(n):

        print(b)
        spiral = pi * b * factor // 2
        spiral /= 90

        for j in range(90):

            x.forward(spiral)
            x.left(1)

        # Proceeding the Fibonacci Sequence for spiral plot
        temp = a
        a = b
        b = temp + b


# The 'factor' signifies the multiplicative factor
# that defines the scale of the plot
factor = 10

# Number of Iterations
n = int(input('Number of Iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# including a validation for n

if n > 0:

    print(f"Fibonacci series for {n} elements:")
    x.speed(10)
    plot_fibo()
    turtle.done()

else:
    print("Number of iterations must be > 0. Try again")
