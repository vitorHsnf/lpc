from settings import *
from modules.render import Render
from modules.character import Character


class Game:
    def __init__(self, screen: tuple[int, int]):
        pygame.init()
        self.screen = pygame.display.set_mode(screen)
        pygame.display.set_caption("Robotron 2084")
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.all_sprites = pygame.sprite.Group()
        self.render = Render(self.screen, self.all_sprites, COLOR_LOOP)
        self.start_logo = pygame.image.load(START_LOGO).convert()
        self.running = True  # Game Loop
        self.game_over = False
        self.player = Character(16, WIDTH//2, HEIGHT//2, 5,
                                PLAYER_SPRITE, self.screen, self.all_sprites)

    def new_game(self):
        self.run()

    def run(self):

        while self.running:
            self.screen.fill(BG_COLOR)
            # Checking for events
            for event in pygame.event.get():
                # Quit Game
                if event.type == pygame.QUIT:
                    self.running = False

            # Update Logic
            if not self.game_over:
                self.clock.tick(FPS)  # 60 FPS
                self.timer += 1
            self.draw_sprites()
            self.update_sprites()

    def update_sprites(self):
        self.all_sprites.update()

    def start_screen(self):
        self.render.start_screen(self.start_logo, WIDTH / 2, 100)
        self.render.text('-Press Any Key', 32, ORANGE, WIDTH/2, 320)
        pygame.display.flip()
        self.standing_by()

    def draw_sprites(self):
        # Changing the general colors on the screen
        self.render.border(WIDTH, HEIGHT, 700, 450, ORANGE, 5)
        self.render.sprites(self.all_sprites)
        pygame.display.flip()

    def standing_by(self):
        standing = True
        while standing:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    standing = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    standing = False

