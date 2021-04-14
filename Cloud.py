import pygame
import random

SPEED_X = random.randint(-1,1)
SPEED_Y = random.randint(-1,1)
SPEED_FACTOR = random.randint(1,4)

class Cloud(pygame.sprite.Sprite):

    def __init__(self,world,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.image = self.world.cloud_images[random.randint(0,1)]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.loop = 0

    def update(self):
        if self.loop == SPEED_FACTOR:
            self.move()
            self.loop = 0
            return
        self.loop += 1


    def move(self):

        #réapparaît à gauche

        if self.rect.x > self.world.screenWidth:
            self.rect.left = -(self.world.size_cloud_X)

        #réapparaît à droite

        if self.rect.x < -(self.world.size_cloud_X) :
            self.rect.left = self.world.screenWidth

        #réapparaît en bas

        if self.rect.y < -(self.world.size_cloud_Y):
            self.rect.top = self.world.screenHeight

        #réapparaît en haut

        if self.rect.y > self.world.screenHeight:
            self.rect.bottom = 0
            
        self.rect.x += SPEED_X
        self.rect.y += SPEED_Y

            

        

