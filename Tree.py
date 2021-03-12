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

        self.delai = 0


    def reset_delai(self):

        self.delai = 0


    def tree_gen(self):

        self.delai += 1

        if self.delai == 50:

            self.reset_delai()
            
            if self.state < 16 and self.alive:
                
                self.state += 1

        self.image = self.world.Environment_images[1][self.state]
        

    def update_tree(self):

        self.tree_gen()