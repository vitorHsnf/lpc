import math
import random
from render import Ship
from attribute import Shot
from config import *


class Npc(Ship):
    def __init__(self):
        super().__init__()
        self._set_random_position()
        self.aimed = False
        self.friend = False

    def update(self):
        self.shoot = True
        super().update()

    def _set_random_position(self):
        self.rect.x = random.randint(200, 1400)
        self.rect.y = random.randint(200, 700)
