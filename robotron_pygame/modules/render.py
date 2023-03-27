import settings
import random
import pygame


class Render:
    def __init__(self, screen: pygame.Surface, sprites: pygame.sprite.Group, colors: list):
        self.screen = screen
        self.all_sprites = sprites
        self.colors = colors

    def sprites(self, sprites):
        sprites.draw(self.screen)

    def start_screen(self, file: pygame.image, x, y):
        file_rect = file.get_rect()
        file_rect.midtop = (x, y)
        self.screen.blit(file, file_rect)

    def border(self, width: int, height: int, x: int, y: int, color: int, border: int):

        # Desenhando as bordas do jogo na forma de retângulo, não sei se dá problema na colisão:
        # pygame.draw.rect(self.screen, color, (width, height, x, y), border)

        # Desenhando as bordas do jogo um por um
        # width_0: 30, width_1: width-40, height_0: 40, height_1: height-40
        pygame.draw.line(self.screen, color, (30, 40), (width-40, 40), border)
        pygame.draw.line(self.screen, color, (width-40, 40), (width-40, height-40), border)
        pygame.draw.line(self.screen, color, (width-40, height-40), (30, height-40), border)
        pygame.draw.line(self.screen, color, (30, height-40), (30, 40), border)

    def text(self, text: str, size, color, x, y):
        font = pygame.font.match_font(settings.FONT)
        text_font = pygame.font.Font(font, size)
        text = text_font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text, text_rect)


