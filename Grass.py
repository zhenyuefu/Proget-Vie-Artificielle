import random

import pygame  # PYGAME package


class Grass(pygame.sprite.Sprite):

    def __init__(self,world,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.x, self.y = x, y

        self.state = 0

        self.image = self.world.Environment_images[2][self.state]

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * self.world.size_grass_X, self.y * self.world.size_grass_Y)

        self.step_state = 0

        self.time_state = 0

    
    def reset_step_state(self):

        self.step_state = 0


    def grass_gen(self):

        if self.state < len(self.world.Environment_images[2]) - 1:
            
            self.step_state += 1
            
            if self.step_state >= self.time_state:
                
                self.reset_step_state()
                
                self.state += 1
                
                self.image = self.world.Environment_images[2][self.state]


    def update_grass(self):

        self.grass_gen()

