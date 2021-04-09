import random

import pygame  # PYGAME package

from Fire import *
import Cloud

P_FIRE = 0
P_REPOUSSE = 0

class Tree(pygame.sprite.Sprite):

    def __init__(self,world,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.state = len(self.world.Environment_images[1])-1

        self.image = self.world.Environment_images[1][self.state]
        
        self.x, self.y = x, y

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * self.world.size_tree_X, self.y * self.world.size_tree_Y)

        self.inFire = False

        self.fire = None

        self.stateF = -1

        self.step_state = 0

        self.time_state = 3 # nb d'itérations avant de passer à le prochain state

        self.loop = 0 # itérateur boucle de feu


    def reset_step_state(self):

        self.step_state = 0
        

    def in_Fire(self):

        self.inFire = True
        
        self.fire = Fire(self,self.x,self.y,self.world.Fire_images[0][0])

        self.world.fire_group.add(self.fire)


    def tree_in_fire(self):

        if not self.inFire:

            if random.random() < P_FIRE:

                self.in_Fire()
            
        if self.stateF == len(self.world.Fire_images[0]) - 1:

            self.fire.kill()

            self.world.Map_trees[self.y][self.x] = None

        if self.inFire and self.stateF < len(self.world.Fire_images[0]) - 1:

            # Le feu se propage dans la direction du vent

            # Aucun vent
            if Cloud.SPEED_X == 0 and Cloud.SPEED_Y == 0:
                xm = self.x-1
                xp = self.x+2
                ym = self.y-1
                yp = self.y+2
            
            # Vent NORD 
            elif Cloud.SPEED_X > 0:
                xm = self.x
                xp = self.x+2

                # Vent NE 
                if Cloud.SPEED_Y > 0:
                    ym = self.y
                    yp = self.y+2

                # Vent NW
                elif Cloud.SPEED_Y < 0:
                    ym = self.y-1
                    yp = self.y+1
                    
                else:   
                    xm = self.x+1
                    ym = self.y-1
                    yp = self.y+2

            # Vent SUD
            elif Cloud.SPEED_X < 0:
                xm = self.x-1
                xp = self.x+1

                # Vent SE
                if Cloud.SPEED_Y > 0:
                    ym = self.y
                    yp = self.y+2
                
                # Vent SW
                elif Cloud.SPEED_Y < 0:
                    ym = self.y-1
                    yp = self.y+1
                
                else:
                    xp = self.x
                    ym = self.y-1
                    yp = self.y+2

            # Vent EST
            elif Cloud.SPEED_Y > 0:
                ym = self.y
                yp = self.y+2

                # Vent NE
                if Cloud.SPEED_X > 0:
                    xm = self.x
                    xp = self.x+2

                # Vent SE
                elif Cloud.SPEED_X < 0:
                    xm = self.x-1
                    xp = self.x+1

                else:
                    xm = self.x-1
                    xp = self.x+2
                    ym = self.y+1

            # Vent WEST
            elif Cloud.SPEED_Y < 0:
                ym = self.y-1
                yp = self.y+1

                # Vent NW
                if Cloud.SPEED_X > 0:
                    xm = self.x
                    xp = self.x+2

                # Vent SW
                elif Cloud.SPEED_X < 0:
                    xm = self.x-1
                    xp = self.x+1

                else:
                    xm = self.x-1
                    xp = self.x+2
                    yp = self.y 
            
            for x2 in range(xm,xp):

                for y2 in range(ym,yp):

                    x3, y3 = x2, y2

                    if x3 < 0:

                        x3 += len(self.world.Map_trees[0])

                    if x3 >= len(self.world.Map_trees[0]):

                        x3 -= len(self.world.Map_trees[0])

                    if y3 < 0:

                        y3 += len(self.world.Map_trees)

                    if y3 >= len(self.world.Map_trees):

                        y3 -= len(self.world.Map_trees)

                    if self.world.Map_trees[y3][x3] != None and not self.world.Map_trees[y3][x3].inFire:

                        self.world.Map_trees[y3][x3].in_Fire()


            if self.stateF == 4:
                
                if self.loop < 4:
                    
                    self.stateF = -1
                    
                    self.loop += 1

                else:
                    
                    self.kill()


            self.stateF += 1

            self.fire.set_frame(self.world.Fire_images[0][self.stateF])


    def tree_gen(self):
        
        if not self.inFire and self.state < len(self.world.Environment_images[1]) - 1:
            
            self.step_state += 1
            
            if self.step_state >= self.time_state:
                
                self.reset_step_state()
                
                self.state += 1
                
                self.image = self.world.Environment_images[1][self.state]
            
            
        

    def update_tree(self):

        self.tree_in_fire()
        self.tree_gen()
        