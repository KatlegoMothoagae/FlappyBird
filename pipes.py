import pygame
from support import import_folder

class Pipe(pygame.sprite.Sprite):
    def __init__(self,pos,flip_status):
        super().__init__()
        self.flip_status = flip_status
        self.flip(self.flip_status)
        self.rect = self.image.get_rect(bottomleft = pos)
        self.speed = -1

    def flip(self,Bool):
        if Bool:
           self.image = pygame.transform.flip(import_folder('graphics/pipes/green')[0],True,True)
        else:
           self.image = import_folder('graphics/pipes/green')[0]

    def update(self,speed):
        self.rect.x += speed

