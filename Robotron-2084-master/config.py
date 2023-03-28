import pygame

pygame.font.init()
pygame.mixer.init()
screen_width = 1265
screen_height = 705
clk = pygame.time.Clock()
fps = 60
shot_time = 15

menuMusic = pygame.mixer.Sound("Sounds/warp.wav")
gameplayMusic = pygame.mixer.Sound("Sounds/gameplayMusic.wav")
gameplayMusic.set_volume(0.0)
gameoverMusic = pygame.mixer.Sound("Sounds/gameover.wav")
#gameWinMusic = pygame.mixer.Sound("Sounds/Yippeee.wav")

shotSoundEffect = pygame.mixer.Sound("Sounds/shot_1.wav")
shotSoundEffect.set_volume(0.50)
explosionSoundEffect = pygame.mixer.Sound("Sounds/death.wav")
explosionSoundEffect.set_volume(0.9)

bossWarningChannel = pygame.mixer.Channel(3)
bossChannel = pygame.mixer.Channel(2)