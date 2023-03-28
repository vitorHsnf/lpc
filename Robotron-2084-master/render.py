import os
import pygame.math
from animated_sprite import AnimatedSprite
from config import *


class Ship(AnimatedSprite):
    def __init__(self):
        super().__init__(0.1, False)
        self.damage = 1
        self.max_hp = 1
        self.hp = 1
        self.img_ship = []
        self.shot_speed = 4
        self.shot_time = 0
        self.shot_sprites = pygame.sprite.Group()
        self.shot_sprite = pygame.image.load(os.path.join("Sprites", "testeball.png"))
        self.shot_h = 30
        self.shot_w = 30
        self.shoot = False
        self.shoot_time = 0
        self.dead = False
        self.boss = False
        self.explosion_sound_effect = explosionSoundEffect

    def make_ship(self, path, shot=None):
        self.load_path(path)
        if shot is not None:
            self.shot_sprite = shot

    def shoot_(self):
        self.shoot = True

    def create_shots(self):
        pass

    def lose_hp(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
            self.explosion_sound_effect.play()
            self.dead = True
            return True
        return False

    def move(self):
        pass

    def update(self):
        super().update()
        if self.dead:
            return
        self.move()
        if self.shoot_time > 0:
            self.shoot_time -= 1
        if self.shoot and self.shoot_time <= 0:
            self.shoot_time = self.shot_time
            shots = self.create_shots()
            if shots is not None:
                for shot in shots:
                    self.shot_sprites.add(shot)
            self.shoot = False
