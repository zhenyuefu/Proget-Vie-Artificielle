

import pygame  # PYGAME package


class Block(pygame.sprite.Sprite):

    def __init__(self,world,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.x, self.y = x, y

        self.image = self.world.Environment_images[0][0]

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * self.world.size_block_X, self.y * self.world.size_block_Y)

    
    def update_block(self):

        self.set_frame()


    def set_frame(self):

        i = self.world.Map_mountains[self.y][self.x]-1
        
        if i>0:
            
            self.image = self.world.Block_images[self.world.weather.get_season()][0]
            
        x_mn, y_mn = self.x - 1, self.y - 1
        
        x_mx, y_mx = self.x + 1, self.y + 1
        
        if x_mn < 0:
            
            x_mn += len(self.world.Map_mountains[0])
            
        if x_mx >= len(self.world.Map_mountains[0]):
            
            x_mx -= len(self.world.Map_mountains[0])
            
        if y_mn < 0:
            
            y_mn += len(self.world.Map_mountains)
            
        if y_mx >= len(self.world.Map_mountains):
            
            y_mx -= len(self.world.Map_mountains)
            
        # Sud

        if self.world.Map_mountains[y_mx][self.x]<=i: 
            
            # Ouest

            if self.world.Map_mountains[self.y][x_mn]<=i:
                
                self.image = self.world.Block_images[self.world.weather.get_season()][1]
                
                return
            
            # Est

            if self.world.Map_mountains[self.y][x_mx]<=i:
                
                self.image = self.world.Block_images[self.world.weather.get_season()][3]
                
                return
            
            self.image = self.world.Block_images[self.world.weather.get_season()][5]

            return
        
        # Nord

        if self.world.Map_mountains[y_mn][self.x]<=i: 
            
            # Ouest

            if self.world.Map_mountains[self.y][x_mn]<=i:
                
                self.image = self.world.Block_images[self.world.weather.get_season()][2]
                
                return
            
            # Est

            if self.world.Map_mountains[self.y][x_mx]<=i:
                
                self.image = self.world.Block_images[self.world.weather.get_season()][4]
                
                return
            
            self.image = self.world.Block_images[self.world.weather.get_season()][6]
            
            return
        
        # Est 

        if self.world.Map_mountains[self.y][x_mx]<=i:
            
            self.image = self.world.Block_images[self.world.weather.get_season()][7]
            
            return
        
         # Ouest

        if self.world.Map_mountains[self.y][x_mn]<=i:
            
            self.image = self.world.Block_images[self.world.weather.get_season()][8]
            
            return
        
        # SE corner

        if self.world.Map_mountains[y_mx][x_mx]==i:
            
            if self.world.Map_mountains[y_mx][self.x]>i and self.world.Map_mountains[self.y][x_mx]>i:
                
                self.image = self.world.Block_images[self.world.weather.get_season()][11]
                
                return
            
        #SW corner

        if self.world.Map_mountains[y_mx][x_mn]==i:
            
            if self.world.Map_mountains[y_mx][self.x]>i and self.world.Map_mountains[self.y][x_mn]>i:
                
                self.image = self.world.Block_images[self.world.weather.get_season()][12]
                
                return

        #NW corner

        if self.world.Map_mountains[y_mn][x_mn]==i:
            
            if self.world.Map_mountains[y_mn][self.x]>i and self.world.Map_mountains[self.y][x_mn]>i:
                
                self.image = self.world.Block_images[self.world.weather.get_season()][10]
                
                return

        # NE corner

        if self.world.Map_mountains[y_mn][x_mx]==i:

            if self.world.Map_mountains[y_mn][self.x]>i and self.world.Map_mountains[self.y][x_mx]>i:

                self.image = self.world.Block_images[self.world.weather.get_season()][9]

                return
            
        self.image = self.world.Block_images[self.world.weather.get_season()][0]

        return

