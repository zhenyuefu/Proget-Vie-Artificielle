import random

import pygame  # PYGAME package

class Tree(pygame.sprite.Sprite):

    def __init__(self,world,img,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.image = img
        
        self.x, self.y = x, y

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * world.size_tile_X, self.y * world.size_tile_Y)

        self.alive = True

        self.state = 0

        self.time = 0

        self.time_state = 5


    def reset_time(self):

        self.time = 0


    def tree_gen(self):

        self.time += 1

        if self.time >= self.time_state:

            self.reset_time()
            
            if self.state < 16 and self.alive and random.random() < 0.5:
                
                self.state += 1

        self.image = self.world.Environment_images[1][self.state]
        

    def update_tree(self):

        self.tree_gen()