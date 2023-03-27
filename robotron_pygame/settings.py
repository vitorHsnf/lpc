import os
import pygame
from modules.character import Character

# Screen Size
WIDTH = 840
HEIGHT = 540
SIZE = (WIDTH, HEIGHT)

# Colors
BG_COLOR = (0, 0, 0)  # Black
PINK = (255, 192, 203)
ORANGE = (242, 139, 22)
GREEN = (3, 252, 19)
BLUE = (3, 40, 252)
RED = (252, 57, 3)
COLOR_LOOP = [RED, GREEN, BLUE]

# Fonts
FONT = 'robotron2084regular'

# FPS
FPS = 30

# Images and Directory
DIR_IMAGE = os.path.join(os.getcwd(), 'assets', 'images')
DIR_AUDIO = os.path.join(os.getcwd(), 'assets', 'audio')
ROBOTRON_LOGO = 'Robotron_2084_logo.png'
START_LOGO = os.path.join(DIR_IMAGE, ROBOTRON_LOGO)
PLAYER_IMG = "hero.bmp"
PLAYER_2 = pygame.image.load("assets/images/hero.bmp")
PLAYER_SPRITE = os.path.join(DIR_IMAGE, PLAYER_IMG)

# Player
# PLAYER = Character(16, WIDTH//2, HEIGHT//2, 5, PLAYER_SPRITE,)


