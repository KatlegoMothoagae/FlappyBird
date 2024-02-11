import pygame
from support import import_folder

class Background(pygame.sprite.Sprite):
    def __init__(self,pos,bg,resize):
        super().__init__()
        image = import_folder('graphics/background/'+ bg)[0].convert_alpha()
        self.image = pygame.transform.scale(image,(resize))
        self.rect = self.image.get_rect(topleft = pos)
    def get_width(self):
        return self.rect.x


