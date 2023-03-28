import math
import pygame.math
from animated_sprite import AnimatedSprite
from config import screen_width, screen_height


class Shot(AnimatedSprite):
    def __init__(self, ship, offset_x, offset_y, vel_x, vel_y):
        super().__init__(0.1, False, ship.shot_sprite, ship.shot_w, ship.shot_h, 0)
        self.ship = ship
        self.vel = pygame.math.Vector2(vel_x, vel_y) * self.ship.shot_speed
        self.pos = pygame.math.Vector2(ship.rect.centerx + offset_x, ship.rect.centery + offset_y)
        self.rect.center = self.pos
        self.group = pygame.sprite.Group()

    def update(self):
        super().update()
        self.move()

    def move(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if not (0 <= self.rect.x <= screen_width - self.rect.width and 0 <= self.rect.y <= screen_height - self.rect.height):
            self.kill()

    def get_angle_of_velocity(self):
        return self.vel.angle_to(pygame.math.Vector2(0, 1))


class TimedShot(Shot):
    def __init__(self, ship, offset_x, offset_y, vel_x, vel_y, speed):
        super().__init__(ship, offset_x, offset_y, vel_x, vel_y)
        self.speed = speed
        self.play_once = True


class BounceShot(Shot):
    def __init__(self, ship, offset_x, offset_y, vel_x, vel_y, bounce):
        super().__init__(ship, offset_x, offset_y, vel_x, vel_y)
        self.bounce = bounce

    def move(self):
        super().move()
        if not 20 <= self.pos.x <= 1580:
            self.vel.x *= -1
            self.bounce -= 1
        if not self.rect.h / 2 <= self.pos.y <= 900:
            self.vel.y *= -1
            self.bounce -= 1
        if self.bounce < 0:
            self.kill()


class SplitShot(Shot):
    def __init__(self, ship, offset_x, offset_y, vel_x, vel_y, time, split):
        super().__init__(ship, offset_x, offset_y, vel_x, vel_y)
        self.timer = time
        self.split = split
        self.shot_speed = self.ship.shot_speed
        self.shot_sprite = self.ship.shot_sprite
        self.shot_w = self.ship.shot_w * 3/4
        self.shot_h = self.ship.shot_h * 3/4

    def update(self):
        super().update()
        if self.timer > 0:
            self.timer -= 1
        else:
            shots = [Shot(self, 10 * math.cos(i * 2 * math.pi / self.split + math.pi / self.split),
                          10 * math.sin(i * 2 * math.pi / self.split + math.pi / self.split),
                          math.cos(i * 2 * math.pi / self.split + math.pi / self.split),
                          math.sin(i * 2 * math.pi / self.split + math.pi / self.split))
                     for i in range(self.split)]
            self.ship.shot_sprites.add(*shots)
            self.kill()
