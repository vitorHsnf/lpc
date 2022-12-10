import turtle
from random import randint
from time import sleep
screen = turtle.Screen()
screen.bgcolor('light blue')
screen.setup(1.0,1.0)
screen.title('Turtle Race Game')


def createTurtlePlayer(color, startx, starty):
    player = turtle.Turtle()
    player.color(color)
    player.shape("turtle")
    player.penup()
    player.goto(startx, starty)
    player.pendown()
    return player

pen = turtle.Turtle()
pen.speed(1)


pen.penup()
pen.goto(-200, 200)
pen.pendown()

finishLineX=250
# Race Tracks

for i in range(1, 11):
    pen.write(i, font=('Arial', 10))
    pen.setheading(-90)
    pen.forward(250)

    if i == 10:
        pen.write(" FINISH")

    pen.back(250)
    pen.penup()
    pen.setheading(0)
    pen.forward(50)
    pen.down()

p1 = createTurtlePlayer('red', -210, 150)
p2 = createTurtlePlayer('green', -210, 100)
p3 = createTurtlePlayer('purple', -210, 50)

while True:

    p1.forward(randint(5, 10))
    if p1.pos()[0] >= finishLineX:
        p1.write('WINNER!', font=('Arial', 30))
        break
    p2.forward(randint(5, 10))
    if p2.pos()[0] >= finishLineX:
        p2.write('WINNER!', font=('Arial', 30))
        break
    p3.forward(randint(5, 10))
    if p3.pos()[0] >= finishLineX:
        p3.write('WINNER!', font=('Arial', 30))
        break






turtle.done()
dados = [1, 2, 3, 4, 5, 6]