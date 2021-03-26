import random

import pygame  # PYGAME package


class Tree(pygame.sprite.Sprite):

    def __init__(self,world,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.state = 0

        self.image = self.world.Environment_images[1][self.state]
        
        self.x, self.y = x, y

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * self.world.size_tree_X, self.y * self.world.size_tree_Y)

        self.inFire = False

        self.stateF = -1

        self.step_state = 0

        self.time_state = 5

        self.loop = 0


    def reset_step_state(self):

        self.step_state = 0
        

    def in_Fire(self):

        self.inFire = True


    def tree_in_fire(self):

        if not self.inFire:

            self.inFire = random.random() < 0.001
            
        if self.stateF == len(self.world.Fire_images[0]) - 1:

            self.kill()

            self.world.Map_trees[self.y][self.x] = None

        if self.inFire and self.stateF < len(self.world.Fire_images[0]) - 1:

            for x2 in range(self.x-1,self.x+2):

                for y2 in range(self.y-1,self.y+2):

                    x3 = x2

                    y3 = y2

                    if x3 < 0:

                        x3 += len(self.world.Map_trees[0])

                    if x3 >= len(self.world.Map_trees[0]):

                        x3 -= len(self.world.Map_trees[0])

                    if y3 < 0:

                        y3 += len(self.world.Map_trees)

                    if y3 >= len(self.world.Map_trees):

                        y3 -= len(self.world.Map_trees)

                    if self.world.Map_trees[y3][x3] != None:

                        self.world.Map_trees[y3][x3].in_Fire()


            if self.stateF == 4 and self.loop < 4:

                self.stateF = -1

                self.loop += 1


            self.stateF += 1

            self.image = self.world.Fire_images[0][self.stateF]


    def tree_gen(self):
        
        if not self.inFire:
            
            self.step_state += 1
            
            if self.step_state >= self.time_state:
                
                self.reset_step_state()
                
                if self.state < len(self.world.Environment_images[1]) - 1: #and random.random() < 0.5:
                    
                    self.state += 1
                    
                    self.image = self.world.Environment_images[1][self.state]
            
            
        

    def update_tree(self):

        self.tree_gen()
        self.tree_in_fire()