import pygame.math

from RobotronStages.game_state import GameState
from config import *


class MenuState(GameState):
    def __init__(self):
        super().__init__()
        self.done = False
        self.next_state = "GAMEPLAY"
        self.background = pygame.image.load("Sprites/UI/jp.jpg")
        self.background_rect = self.background.get_rect(topleft=(-25, 0))
        self.press = pygame.image.load("Sprites/UI/zx1.jpg")
        self.press_rect = self.press.get_rect(topleft=(225, 440))
        """self.logo = pygame.image.load("Sprites/UI/robotron.jpg")
        self.logo_rect = self.logo.get_rect(topleft=(125, 150))"""
        menuMusic.play(-1)

    # Check if an event happens
    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               self.done = True
               menuMusic.fadeout(3000)

    def draw(self, screen):
        screen.blit(self.background, self.background_rect)
        screen.blit(self.press, self.press_rect)
        #screen.blit(self.logo, self.logo_rect)
