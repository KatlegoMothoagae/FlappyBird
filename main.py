import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
level = Level(screen)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    level.run()
    pygame.display.update()
    clock.tick(FPS)