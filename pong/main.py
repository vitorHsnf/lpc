import platform
import turtle
import os
from time import sleep

# Define the OS name 
system = platform.system()

# Audio configs for Windows and Mac system
if system == "Windows":
    import winsound

    bounce_sound = "bounce.wav"
    score_sound = "arcade-bleep-sound.wav"

elif system == "Darwin":
    bounce_sound = "afplay bounce.wav&"
    score_sound = "afplay arcade-bleep-sound.wav&"

# Set the sound effects
def sound_fx(audio):

    if system == "Windows":
        winsound.PlaySound(audio, winsound.SND_ASYNC)
    else:
        os.system(audio)
        
# Draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball speed
ball.dx = 0.7
ball.dy = 0.7

# Score
score_1 = 0
score_2 = 0

# Define a Max Score
max_score = 10

# Create Judge
judge = turtle.Turtle()
judge.color("white")
judge.penup()
judge.hideturtle()

# Head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center",
          font=("Press Start 2P", 30, "normal"))

# Proceeds the game when one of the players points
def hud_remake():

    hud.clear()
    hud.write(f"{score_1} : {score_2}", align="center",
              font=("Press Start 2P", 30, "normal"))
    ball.goto(0, 0)
    ball.dx *= -1

# Draw paddles for player one and player two
def draw_paddle(start_x, start_y):

    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(start_x, start_y)
    return paddle

# Define the moviments that paddles can make
def paddle_1_up():

    y = paddle_1.ycor()
    if y < 250:
        y += 30
    else:
        y = 250

    paddle_1.sety(y)


def paddle_1_down():

    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250

    paddle_1.sety(y)


def paddle_2_up():

    y = paddle_2.ycor()
    if y < 250:
        y += 30
    else:
        y = 250

    paddle_2.sety(y)


def paddle_2_down():

    y = paddle_2.ycor()
    if y > -250:
        y += -30
    else:
        y = -250

    paddle_2.sety(y)

# Draw the paddles and set the positions
paddle_1 = draw_paddle(-340, 0)
paddle_2 = draw_paddle(340, 0)

# Keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

# Run the game
while True:

    screen.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision with the upper wall
    if ball.ycor() > 290:
        sound_fx(bounce_sound)
        ball.sety(290)
        ball.dy *= -1

    # Collision with lower wall 
    if ball.ycor() < -290:
        sound_fx(bounce_sound)
        ball.sety(-290)
        ball.dy *= -1

    # Collision with right wall and player 1 point
    if ball.xcor() > 390:
        score_1 += 1
        hud_remake()
        sound_fx(score_sound)
        sleep(0.5)

    # Collision with left wall and player 2 point
    if ball.xcor() < -390:
        score_2 += 1
        hud_remake()
        sound_fx(score_sound)
        sleep(0.5)

    # Collision with the paddle 1
    if -340 < ball.xcor() < -330:

        if paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
            ball.dx *= -1

        sound_fx(bounce_sound)

    # Collision with the paddle 2
    if 340 > ball.xcor() > 330:

        if paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
            ball.dx *= -1

        sound_fx(bounce_sound)

    # Game Results
    if score_1 == max_score or score_2 == max_score:

        if score_1 > score_2:
            winner = "Player 1"

        else:
            winner = "Player 2"

        judge.write(f"{winner} Wins", align="center",
                    font=("Press Start 2P", 30, "normal"))

        screen.listen()
        screen.exitonclick()
