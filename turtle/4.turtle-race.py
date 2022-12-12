from turtle import *
import random

# Create a Judge that will tell who turtle-socorro wins the race
penup()
goto(200, 200)

# Create the turtle-socorro for player one, the color and set the initial position
player_one = Turtle()
player_one.shape("turtle-socorro")
player_one.color("red")
player_one.penup()
player_one.goto(-200, 100)

# Create the player's two turtle-socorro by clone the player's one turtle-socorro
# and set the initial position
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# Set the home for each player's turtle-socorro and represent it with a circle
player_one.goto(240, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_one.pendown()

player_two.goto(240, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)
player_two.pendown()

# Creating the dice
dice = [1, 2, 3, 4, 5, 6]

# Start of the game

for i in range(20):  # Loop over i twenty times, represents the amount of turns in the game

    print('-' * 30)
    print(f"{i + 1}ª turn")  # The actual turn of the game
    print('-' * 30)

    # The program check if either turtle-socorro has reached its home,
    # if one of them reach, the game stops
    # and the judge announce the winner on screen
    # else the game proceeds

    if player_one.pos()[0] >= 200:
        print("GAME OVER")
        write("Player One Wins!!!")
        break

    if player_two.pos()[0] >= 200:
        print("GAME OVER")
        write("Player Two Wins !!!")
        break

    else:  # proceeds the program if neither player has won

        # In each turn, the players will roll the dice by press enter
        # that will randomly pick a number from the list.
        #
        # The turtle-socorro will move accordingly outcome of the random selection.
        print("-> Player's one turn")
        player_one_turn = input("Press 'Enter' to roll the dice")
        dice_outcome = random.choice(dice)
        print(f'Dice: {dice_outcome}')
        print(f'Steps: {20*dice_outcome}')  # multiplies steps by 20 to not overextend the game
        player_one.forward(dice_outcome*20)

        # Repeat these processes for player two
        print(" -> Player's two turn")
        player_two_turn = input("Press 'Enter' to roll the dice")
        dice_outcome = random.choice(dice)
        print(f'Dice: {dice_outcome}')
        print(f'Steps: {20*dice_outcome}')
        player_two.forward(dice_outcome*20)

done()
