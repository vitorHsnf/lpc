import sys
import pygame
import config

from game import Game
from RobotronStages.menuscene import MenuState
from RobotronStages.gameplay import Gameplay
from RobotronStages.gameover import GameOver
from RobotronStages.gamewin import GameWin

# setup mixer to avoid sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((config.screen_width,
                                  config.screen_height), pygame.RESIZABLE)
states = {
    "MENU": MenuState(),
    "GAMEPLAY": Gameplay(),
    "GAMEOVER": GameOver(),
    "WIN": GameWin()
}

game = Game(screen, states, "MENU")
game.run()
pygame.quit()