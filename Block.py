

import pygame  # PYGAME package


class Block(pygame.sprite.Sprite):

    def __init__(self,world,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.x, self.y = x, y
        self.id = 0
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * self.world.size_block_X, self.y * self.world.size_block_Y)
        self.frame = []
        self.Map = []

    # Changement d'apparence
    def set_image(self):
        self.image = self.frame[self.world.weather.season][self.id]

    # Maj block
    def update(self):
        self.set_id()
        self.set_image()

    # On identifie l'orientation du block
    def set_id(self):
        i = self.Map[self.y][self.x]-1            
        x_mn, y_mn = self.x - 1, self.y - 1        
        x_mx, y_mx = self.x + 1, self.y + 1        
        if x_mn < 0:
            x_mn += len(self.Map[0])
        if x_mx >= len(self.Map[0]):
            x_mx -= len(self.Map[0])
        if y_mn < 0:
            y_mn += len(self.Map)
        if y_mx >= len(self.Map):
            y_mx -= len(self.Map)
            
        # Sud
        if self.Map[y_mx][self.x]<=i: 
            
            # Ouest
            if self.Map[self.y][x_mn]<=i:
                self.id = 1
                return
            
            # Est
            if self.Map[self.y][x_mx]<=i:
                self.id = 3
                return
            self.id = 5
            return
        
        # Nord
        if self.Map[y_mn][self.x]<=i: 
            
            # Ouest
            if self.Map[self.y][x_mn]<=i:
                self.id = 2                
                return
            
            # Est
            if self.Map[self.y][x_mx]<=i:
                self.id = 4                
                return
            self.id = 6           
            return
        
        # Est 
        if self.Map[self.y][x_mx]<=i:
            self.id = 7         
            return
        
         # Ouest
        if self.Map[self.y][x_mn]<=i:
            self.id = 8            
            return
        
        # SE corner
        if self.Map[y_mx][x_mx]==i:            
            if self.Map[y_mx][self.x]>i and self.Map[self.y][x_mx]>i:
                self.id = 11               
                return
            
        #SW corner
        if self.Map[y_mx][x_mn]==i:           
            if self.Map[y_mx][self.x]>i and self.Map[self.y][x_mn]>i:
                self.id = 12                
                return

        #NW corner
        if self.Map[y_mn][x_mn]==i:            
            if self.Map[y_mn][self.x]>i and self.Map[self.y][x_mn]>i:
                self.id = 10                
                return

        # NE corner
        if self.Map[y_mn][x_mx]==i:
            if self.Map[y_mn][self.x]>i and self.Map[self.y][x_mx]>i:
                self.id = 9
                return


class Mountain(Block):
    
    def __init__(self,world,x,y):
        super().__init__(world,x,y,world.Block_images[world.weather.season][0])
        self.frame = world.Block_images
        self.Map = world.Map_mountains
        
    def update(self):
        super().update()

class Lake(Block):

    def __init__(self,world,x,y):
        super().__init__(world,x,y,world.Lake_images[world.weather.season][0])
        self.frame = world.Lake_images
        self.Map = world.Map_lake
        
    def update(self):
        super().update()
