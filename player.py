import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.images = import_folder('graphics/player/yellow')

        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.images[self.frame_index].convert_alpha()

        self.alive = True
        self.rect = self.image.get_rect(topleft = pos)

        # Player Movement
        self.direction = 0
        self.gravity = 0.8
        self.jump_speed = -10

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images):
            self.frame_index = 0

        self.image = self.images[int(self.frame_index)]
        self.rotate()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.direction > 0:
           self.jump()

    def apply_gravity(self):
        self.direction += self.gravity
        self.rect.y += self.direction

    def jump(self):
        self.direction = self.jump_speed

    def rotate(self):
        self.image = pygame.transform.rotate(self.image,-self.direction*3)

    def update(self):
        if self.alive:
           self.get_input()
        self.apply_gravity()
        self.animate()
