import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, size: int, pos_x: int, pos_y: int,
                 speed: int, image: str, screen: pygame.surface, *groups):
        super().__init__(*groups)
        self.size = size
        self.speed = speed
        self.sprite_sheet = pygame.image.load(image).convert_alpha(screen)
        self.image = self.sprite_sheet.subsurface((0, 0), (self.size, self.size))
        self.image = pygame.transform.scale(self.image, (self.size*2, self.size*2))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        """self.animation_list = self.load_images(image)
        self.frame_index = 0
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()"""

    def load_images(self, sprites: str) -> list:
        sprites_list = []
        sprite_sheet_image = pygame.image.load(sprites)
        current_img = sprite_sheet_image.subsurface(0, 0, self.size, self.size)
        sprites_list.append(current_img)

        return sprites_list

    def update(self) -> None:
        pass
