import turtle
from time import sleep
import random
    
tela = turtle.getscreen()

dice = [1, 2, 3, 4, 5, 6]

# Jogador um, e tals
player_one = turtle.Turtle()
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
sleep(1)

# Jogador dois
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# Linha de chegada (jogador 1)
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

# Linha de chegada (jogador 2)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

for i in range(20):  #Nº de partidas
    if player_one.pos() >= (300, 100):
        print("Player One Wins!!!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins !!!")
        break
    else:
        print('Vez do jogador um')
        player_one_turn = input("Pressione 'Enter' para jogar os dados")
        dice_outcome = random.choice(dice)
        print('Os dados deram:')
        print(dice_outcome)
        sleep(1)
        print('-'*30)
        print(f'Andando {20*dice_outcome} passos:')
        sleep(1)
        player_one.forward(dice_outcome*20)

        print('-'*30)
        print('Vez do jogador 2')
        print('-'*30)
        player_two_turn = input("Pressione 'Enter' para girar os dados")
        dice_outcome = random.choice(dice)
        print('Os dados deram:')
        print(dice_outcome)
        sleep(1)
        print('-'*30)
        print(f'Andando {20*dice_outcome} passos:')
        sleep(1)
        player_two.forward(dice_outcome*20)

