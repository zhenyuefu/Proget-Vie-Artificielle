#!/usr/bin/env python3


from random import *
from cellule import *
import pygame                   # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 

class World:
    """
    classe principale du jeux
    """

    def __init__(self, size_factor_X=50, size_factor_Y=28, size_tile_X=23, size_tile_Y=23):
        """
        constructeur de la classe
        size_factor_X et size_factor_Y représentent la taille du plateau de jeux en nombre de tuiles 64*64 pixels
        """



        self.size_factor_X, self.size_factor_Y = size_factor_X, size_factor_Y

        self.size_tile_X, self.size_tile_Y = size_tile_X, size_tile_Y

        self.Case=[]

        self.MountainsType=[]

        self.Map_trees=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.Map_obtacles=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.Map_mountains=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        #Type de montagnes

        self.Mountain1=[[1,1,1],
                        [1,1,1],
                        [1,1,1]]

        self.Mountain2=[[1,1,1,1,1,1],
                        [1,1,1,1,1,1]]

        self.MountainsType.append(self.Mountain1)
        self.MountainsType.append(self.Mountain2)

        # Mountains random placement

        self.x_offset = randint(0,self.size_factor_X-1)
        self.y_offset = randint(0,self.size_factor_Y-1)
        self.M = self.MountainsType[randint(0,len(self.MountainsType)-1)]

        for x in range( len( self.M[0] ) ):

            for y in range( len( self.M ) ):

                self.Map_mountains[y+self.y_offset][x+self.x_offset]=1

        #Trees random placement

        for x in range(0,len(self.Map_trees[0])):

            for y in range(0,len(self.Map_trees)):

                cellule = Cellule(y,x)

                self.Case.append(cellule)

                if not self.Map_mountains[y][x]==1:

                    p = randint(0,10)

                    if p < 5 :

                        self.Map_trees[y][x]=1

        #self.Map_trees[self.size_factor_Y//2][self.size_factor_X//2]=2

        # self.Map_trees = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]


        # Obstacles random placement

        for x in range(0,len(self.Map_trees[0])):

            for y in range(0,len(self.Map_trees)):

                if not y==self.size_tile_Y//2 and not x==self.size_factor_X//2:

                    if not self.Map_trees[y][x]==1 and not self.Map_mountains[y][x]==1:

                        p = randint(0,10)

                        if p < 5 :

                            self.Map_obtacles[y][x]=1

        

    
        #self.size_X, self.size_Y = 128,128


        # self.scaleMultiplier_X = self.size_tile_X / self.size_X  

        # self.scaleMultiplier_Y = self.size_tile_Y / self.size_Y
                                            
        self.background_image_filename = 'dirt.png'   # image backgound 
        self.tree_image_filename = 'treeSmall.png' 
        self.burn_tree_image_filename = 'smokeOrange0.png' 
        self.sandbag_image_filename = 'sandbagBrown.png'        
        

        pygame.init()          
                                                     
        self.screen = pygame.display.set_mode((int(self.size_tile_X*self.size_factor_X), int(self.size_tile_Y*self.size_factor_Y)),DOUBLEBUF)

        pygame.display.set_caption("FOREST FIRE")     
                     
        self.background = pygame.image.load(self.background_image_filename).convert_alpha()   # tuile pour le background
        self.background = pygame.transform.scale(self.background, (int(self.size_tile_X), int(self.size_tile_Y)))


        self.tree = pygame.image.load(self.tree_image_filename).convert_alpha()
        self.tree = pygame.transform.scale(self.tree, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.burn_tree = pygame.image.load(self.burn_tree_image_filename).convert_alpha()
        self.burn_tree = pygame.transform.scale(self.burn_tree, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.sandbag = pygame.image.load(self.sandbag_image_filename).convert_alpha()
        self.sandbag = pygame.transform.scale(self.sandbag, (int(self.size_tile_X), int(self.size_tile_Y)))


        self.Tmp = self.Case


    def forestFire(self):

        if (len(self.Tmp))==0:
            self.Tmp = self.Case

        i = randint(0,len(self.Tmp)-1)
        cell = self.Tmp[i]
        #del self.Tmp[i]
        x = cell.getY()
        y = cell.getX()

        if (self.Map_trees[y][x]==2):
            for x2 in range(x-1,x+2):
                for y2 in range(y-1,y+2):
                    x3 = x2
                    y3 = y2
                    if (x3 < 0):
                        x3 += self.size_factor_X
                    if (x3 >= self.size_factor_X):
                        x3 -= self.size_factor_X
                    if (y3 < 0):
                        y3 += self.size_factor_Y
                    if (y3 >= self.size_factor_Y):
                        y3 -= self.size_factor_Y
                    if (self.Map_trees[y3][x3] == 1):
                        self.Map_trees[y3][x3] = 2

            self.Map_trees[y][x] = 3
        

        
            
                

    def stepWorld(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        while True:

            self.forestFire()

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe           

            #affichage répété de la tuile de background en parcourant la fenêtre par pas de la taille des tuiles: 
            
            #for x in range(0, int(self.size_X*self.scaleMultiplier*self.size_factor_X), int(self.size_X*self.scaleMultiplier)):
            for x in range (0,len(self.Map_trees[0])):
                #for y in range(0, int(self.size_Y*self.scaleMultiplier*self.size_factor_Y), int(self.size_Y*self.scaleMultiplier)):
                for y in range(0,len(self.Map_trees)):
                    self.screen.blit(self.background,(x*self.size_tile_X,y*self.size_tile_Y))  # tuile "background" en position (x,y)
                    # if (self.Map_trees[y][x]==1):
                    #     self.screen.blit(self.tree,(x*self.size_tile_X,y*self.size_tile_Y))
                    # if (self.Map_trees[y][x]==2):
                    #     self.screen.blit(self.burn_tree,(x*self.size_tile_X,y*self.size_tile_Y))
                    # if (self.Map_obtacles[y][x]==1):
                    #     self.screen.blit(self.sandbag,(x*self.size_tile_X,y*self.size_tile_Y))
                    if (self.Map_mountains[y][x]==1):
                        self.screen.blit(self.sandbag,(x*self.size_tile_X,y*self.size_tile_Y))
                    

            pygame.display.update()                  


    def destroy(self):
        """
        destructeur de la classe
        """
        print('Exit')
        pygame.quit() # ferme la fenêtre principale
        exit()        # termine tous les process en cours
            
if __name__ == '__main__':
    world=World()
    try:
        world.stepWorld()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
        world.destroy()