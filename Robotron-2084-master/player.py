import math
import pygame
from pygame.math import Vector2

from render import Ship
from attribute import Shot
from config import *


class PlayerShip(Ship):
    def __init__(self, sheet, pos):
        super().__init__()
        self.score = 0
        self.shot_time = 10
        self.shot_speed = 10
        self.move_speed = 6
        self.damage = 1
        self.max_hp = 5
        self.hp = 5
        self.make_ship(sheet, 'Sprites/fire')
        self.rect.center = pos
        self.invincibility_time = 100
        self.invincible_timer = 0
        self.vel = Vector2(0, 0)
        self.store = Vector2(0, 0)

    def go(self, axis, speed):
        if self.vel[axis] == -speed:
            self.store[axis] = self.vel[axis]
        self.vel[axis] = speed

    def stop(self, axis, speed):
        if self.vel[axis] == speed:
            self.vel[axis] = self.store[axis]
            self.store[axis] = 0
        elif speed == self.store[axis]:
            self.store[axis] = 0

    def lose_hp(self, damage):
        if self.invincible_timer <= 0:
            super().lose_hp(damage)
            self.invincible_timer = self.invincibility_time

    def shoot_(self):
        self.shoot = True

    def create_shots(self):
        mouse_pos = pygame.mouse.get_pos()
        vector = Vector2(mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y)
        vector.normalize_ip()
        angle = math.radians(Vector2(1, 0).angle_to(vector))
        angle = round(angle / (math.pi / 4)) * math.pi / 4
        shots = [
            Shot(
                self,
                40 * math.cos(angle) + 8,
                40 * math.sin(angle) + 15,
                math.cos(angle),
                math.sin(angle)
            )
        ]
        shotSoundEffect.play()
        return shots

    def move(self):
        speed = self.vel.copy()
        if speed.length() > 0:
            speed.normalize()
        new_pos = self.rect.move(speed * self.move_speed)
        if 0 <= new_pos.x <= screen_width - self.rect.width and \
           0 <= new_pos.y <= screen_height - self.rect.height:
            self.rect = new_pos


    def update(self):
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
        self.alpha = 255 - 255 * self.invincible_timer / 100
        super().update()
