import os
import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, ship, path='enemy_1', w=None, h=None):
        super().__init__()
        self.ship = ship
        self.sprites = []
        self.path = path
        self.load_path(w, h)
        self.current_sprite = 0

    def update(self):
        self.current_sprite = ((self.ship.max_hp - self.ship.hp) / self.ship.max_hp) * len(self.sprites)
        self.current_sprite = min(self.current_sprite, len(self.sprites) - 1)
        self.image = self.sprites[int(self.current_sprite)]

    def load_path(self, w=None, h=None):
        self.sprites = []
        self.image = pygame.image.load(f"Sprites/{self.path}/{self.path}1.png")
        self.rect = self.image.get_rect()
        if w is not None:
            self.rect.width = w
        if h is not None:
            self.rect.height = h
        for i in range(0, len(os.listdir(f"Sprites/{self.path}"))):
            image = pygame.transform.scale(pygame.image.load(f"Sprites/{self.path}/{self.path}{i+1}.png"),
                                           (self.rect.width, self.rect.height))
            self.sprites.append(image)
