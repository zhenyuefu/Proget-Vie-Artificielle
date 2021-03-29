import pygame

import random

class Cloud(pygame.sprite.Sprite):

    def __init__(self,world):
        
        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.image = self.world.Environment_images[4][0]

        self.rect = self.image.get_rect()

        self.rect.topleft = (random.randint(0,self.world.screenWidth),random.randint(0,self.world.screenHeight))

        self.speed = 1

        self.wind = 1

        self.loop = 0

    def move(self):

        if self.rect.x > self.world.screenWidth:

            self.rect.left = -(self.world.size_cloud_X)

        if self.rect.x < -(self.world.size_cloud_X) :

            self.rect.right = self.world.screenWidth

        if self.rect.y < -(self.world.size_cloud_Y):

            self.rect.top = self.world.screenHeight

        if self.rect.y > self.world.screenHeight:

            self.rect.bottom = -(self.world.size_cloud_Y)

        if self.loop == self.wind:
            
            self.rect.x += self.speed

            self.loop = 0

        self.loop += 1
     
