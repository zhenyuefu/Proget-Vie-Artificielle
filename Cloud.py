import pygame

import random

class Cloud(pygame.sprite.Sprite):

    def __init__(self,world):
        
        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.image = self.world.Environment_images[4][0]

        self.rect = self.image.get_rect()

        self.rect.topleft = (random.randint(0,self.world.screenWidth),random.randint(0,self.world.screenHeight))

        self.speed = random.uniform(float(1),float(1.5))

    def move(self):

        if self.rect.x > self.world.screenWidth:

            self.rect.left = -(self.world.size_cloud_X)

        if self.rect.x < -(self.world.size_cloud_X) :

            self.rect.right = self.world.screenWidth

        if self.rect.y < -(self.world.size_cloud_Y):

            self.rect.top = self.world.screenHeight

        if self.rect.y > self.world.screenHeight:

            self.rect.bottom = -(self.world.size_cloud_Y)

        self.rect.x += self.speed
        #self.rect.y += self.speed
