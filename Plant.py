import random
import math

import pygame  # PYGAME package

from Fire import *
import Cloud

P_FIRE = 0
P_REPOUSSE = 0

class Plant(pygame.sprite.Sprite):

    def __init__(self,world,x,y,img,f_x,f_y):

        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.factor_x, self.factor_y = f_x,f_y
        self.frame = []
        self.fire_frame = []
        self.state = 0#len(self.frame)-1
        self.image = img
        self.Map = []     
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * self.factor_x, self.y * self.factor_y)
        self.inFire = False
        self.fire = None
        self.stateF = -1
        self.step_state = 0
        self.time_state = 10 # nb d'itérations avant de passer à le prochain state
        self.loop = 0 # itérateur boucle de feu
        self.fire_loop = 4


    def reset_step_state(self):

        self.step_state = 0
        

    def in_Fire(self):

        self.inFire = True
        self.world.fire_group.add(self.fire)


    def plant_in_fire(self):

        if not self.inFire:
            if random.random() < P_FIRE:
                self.in_Fire()
            
        if self.stateF == len(self.fire_frame) - 1:
            self.fire.kill()
            self.Map[self.y][self.x] = None

        if self.inFire and self.stateF < len(self.fire_frame) - 1:

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
                        x3 += len(self.Map[0])

                    if x3 >= len(self.Map[0]):
                        x3 -= len(self.Map[0])

                    if y3 < 0:
                        y3 += len(self.Map)

                    if y3 >= len(self.Map):
                        y3 -= len(self.Map)

                    if self.Map[y3][x3] != None and not self.Map[y3][x3].inFire:
                        self.Map[y3][x3].in_Fire()


            if self.stateF == 4:          
                if self.loop < self.fire_loop:    
                    self.stateF = -1                   
                    self.loop += 1

                else:                   
                    self.kill()


            self.stateF += 1
            self.fire.set_frame(self.fire_frame[self.stateF])


    def plant_gen(self):
        
        if not self.inFire and self.state < len(self.frame) - 1:       
            self.step_state += 1    
            if self.step_state >= self.time_state:       
                self.reset_step_state()       
                self.state += 1         
                self.image = self.frame[self.state]
            
            
        

    def update_plant(self):

        self.plant_in_fire()
        self.plant_gen()


class Tree(Plant):

    def __init__(self,world,x,y):
        super().__init__(world,x,y,world.Environment_images[1][0],world.size_tree_X,world.size_tree_Y)
        self.frame=world.Environment_images[1]
        self.fire_frame=world.Fire_images[0]
        self.Map=world.Map_trees
        self.fire=Fire(x,y,self.fire_frame[0],self.factor_x,self.factor_y)
        self.set_time_state(5)

    def distance(self,x,y):
        return abs(self.x-x)+abs(self.y-y)

    def set_time_state(self,rayon):
        d=self.time_state
        for x in range(self.x-rayon,self.x+(rayon+1)):
            for y in range(self.y-rayon,self.y+(rayon+1)):
                x2,y2=x,y
                if x2 < 0:
                    x2 += len(self.world.Map_lake[0])

                if x2 >= len(self.world.Map_lake[0]):
                    x2 -= len(self.world.Map_lake[0])

                if y2 < 0:
                    y2 += len(self.world.Map_lake)

                if y2 >= len(self.world.Map_lake):
                    y2 -= len(self.world.Map_lake)

                if self.world.Map_lake[y2][x2]:
                    d=min(d,self.distance(x2,y2))
        self.time_state-=(rayon-d)

		
    def update(self):
        super().update_plant()

class Grass(Plant):

    def __init__(self,world,x,y):
        super().__init__(world,x,y,world.Environment_images[2][0],world.size_grass_X,world.size_grass_Y)
        self.frame=world.Environment_images[2]
        self.fire_frame=world.Fire_images[1]
        self.Map=world.Map_grass
        self.fire=Fire(x,y,self.fire_frame[0],self.factor_x,self.factor_y)
        self.fire_loop=1
        self.time_state=1

    def update(self):
        super().update_plant()
        if self.world.weather.season == 2 and self.state == 1:
            self.image = self.world.Environment_images[6][0]
        else:
            self.image = self.frame[self.state]
