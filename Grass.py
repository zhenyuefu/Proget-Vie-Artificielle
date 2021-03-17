import random

import pygame  # PYGAME package

class Grass(pygame.sprite.Sprite):

    def __init__(self,world,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.x, self.y = x, y

        self.image = self.world.Environment_images[2][0]

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * self.world.size_grass_X, self.y * self.world.size_grass_Y)