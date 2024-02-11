import pygame
import random
from settings import *
from pipes import Pipe
from player import Player
from background import Background
class Level:

    def __init__(self,surface):
        self.surface = surface
        self.world_shift = -1
        self.start_pos_x = 500
        self.setup_level()

    def setup_level(self):
        self.background = pygame.sprite.GroupSingle()
        self.base = pygame.sprite.GroupSingle()
        self.pipes = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        x = self.start_pos_x
        player = Player((50, screen_width//2))
        self.player.add(player)

        background = Background((0, 0), 'day', dimensions)
        self.background.add(background)

        base = Background((0, screen_height-8), 'base', (screen_width, 50))
        self.base.add(base)
        for pipes in range(3):
            y = random.randrange(50, screen_height - screen_height//4 -180 )
            Upper_pipe = Pipe((x,y),True)
            Lower_pipe = Pipe((x,screen_height + y),False)
            self.pipes.add(Upper_pipe)
            self.pipes.add(Lower_pipe)
            x += 250

    def update_level(self):
        player = self.player.sprite
        base = self.base.sprite

        if base.rect.colliderect(player.rect):
            self.world_shift = 0
            self.player.sprite.rect.y = screen_height - 28
            self.player.sprite.jump_speed = 0
            self.player.sprite.gravity = 0
            self.player.sprite.frame_index = 0
            self.player.sprite.alive = False
        for pipe in self.pipes.sprites():
            x = self.pipes.sprites()[-1].rect.x + 250

            if pipe.rect.x <= -64:
               self.pipes.remove(pipe)
               y = random.randrange(50, screen_height - screen_height//4 -150 )
               Upper_pipe = Pipe((x,y),True)
               Lower_pipe = Pipe((x,screen_height + y),False)
               self.pipes.add(Upper_pipe)
               self.pipes.add(Lower_pipe)

            if pipe.rect.colliderect(player.rect):
                self.player.sprite.alive = False
                self.world_shift = 0
                self.player.sprite.jump_speed = 0


    def run(self):
       self.background.draw(self.surface)

       self.pipes.draw(self.surface)
       self.pipes.update(self.world_shift)

       self.base.draw(self.surface)
       self.update_level()

       self.player.draw(self.surface)
       self.player.update()

