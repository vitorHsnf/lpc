from config import *
from opponents import *
from dobale import Wave

class Levels:
    def __init__(self, level):
        self.group = pygame.sprite.Group()
        self.rounds = []
        self.progress = 0
        self.wave_progress = 0
        self.wall_color = 0, 0, 0
        self.bg_color = 0, 0, 0
        self.get_level(level)

    def get_group(self):
        return self.group

    def get_bg_color(self):
        return self.bg_color

    def get_level(self, level):
        self.progress = 0
        self.wave_progress = 0
        self.rounds = []

        if level == 0:
            waves = [Wave(0, 3), Wave(1, 10)]
            self.rounds.append(waves)
            waves = [Wave(0, 6), Wave(1, 2), Wave(1, 2)]
            self.rounds.append(waves)
            waves = [Wave(2, 10)]
            self.rounds.append(waves)
            waves = [Wave(1, 3), Wave(2, 6)]
            self.rounds.append(waves)
            waves = [Wave(0, 6), Wave(2, 6), Wave(1, 2), Wave(1, 2)]
            self.rounds.append(waves)

    @staticmethod
    def make_enemy(number):
        if number == 0:
            return Human()
        elif number == 1:
            return Grunt()
        elif number == 2:
            return Hulk()
        else:
            return None
