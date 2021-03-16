import random

import pygame  # PYGAME package

class Tree(pygame.sprite.Sprite):

    def __init__(self,world,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.state = 16

        self.image = self.world.Environment_images[1][self.state]
        
        self.x, self.y = x, y

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * world.size_tile_X, self.y * world.size_tile_Y)

        self.alive = True

        self.inFire = False

        self.stateF = -1

        self.time = 0

        self.time_state = 5


    def reset_time(self):

        self.time = 0

    def tree_in_fire(self):

        if not self.inFire:

            self.inFire = random.random() < 0.001

        if self.stateF == 4:

            self.alive = False

            self.inFire = False

            self.stateF = -1

            self.state = -1

        if self.inFire and self.alive:

            self.stateF += 1

            #self.world.screen.blit(self.world.Environment_images[1][self.state],(self.x * self.world.size_tile_X, self.y * self.world.size_tile_Y))

            self.image = self.world.Fire_images[0][self.stateF]


    def tree_gen(self):

        if not self.alive:

            self.alive = random.random() < 0.001

            self.image = self.world.Environment_images[0][0]

        else:
            
            if not self.inFire:
                
                self.time += 1
                
                if self.time >= self.time_state:
                    
                    self.reset_time()
                    
                    if self.state < 16 and random.random() < 0.5:
                        
                        self.state += 1
                        
                        self.image = self.world.Environment_images[1][self.state]
            
            
        

    def update_tree(self):

        self.tree_gen()
        self.tree_in_fire()