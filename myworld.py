#!/usr/bin/env python3


from random import *
import pygame                   # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 

class World:
    """
    classe principale du jeux
    """

    def __init__(self, size_factor_X=45, size_factor_Y=26, size_tile_X=25, size_tile_Y=25):
        """
        constructeur de la classe
        size_factor_X et size_factor_Y représentent la taille du plateau de jeux en nombre de tuiles 64*64 pixels
        """



        self.size_factor_X, self.size_factor_Y = size_factor_X, size_factor_Y

        self.size_tile_X, self.size_tile_Y = size_tile_X, size_tile_Y

        # liste temporaire qui va mettre à jour chaque cellule de Case

        self.Tmp = []

        self.Case=[]

        self.MountainsType=[]

        self.Grass=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.Map_trees=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.Map_obtacles=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.Map_mountains=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.p_grass = 0.09

        self.p1 = 0.003

        self.p2 = 0.001


        # Type de montagnes


        for i in range(5):

            longueur, largeur = randint(3,7), randint(3,7)

            self.MountainsType.append([x[:] for x in [[1] * largeur] * longueur])

        # Mountains random placement

        nbMountains = randint(2,7)

        for i in range(nbMountains):

            x_offset, y_offset = randint(0,self.size_factor_X-1), randint(0,self.size_factor_Y-1)

            M = self.MountainsType[randint(0,len(self.MountainsType)-1)]

            for x in range(len(M[0])):

                for y in range(len(M)):

                    x2, y2 = x + x_offset, y + y_offset

                    if x2 < 0:

                        x2 += self.size_factor_X

                    if x2 >= self.size_factor_X:

                        x2 -= self.size_factor_X

                    if y2 < 0:

                        y2 += self.size_factor_Y

                    if y2 >= self.size_factor_Y:

                        y2 -= self.size_factor_Y

                    self.Map_mountains[y2][x2]=1

        #Trees, obstacles, grass random placement

        for x in range(0,len(self.Map_trees[0])):

            for y in range(0,len(self.Map_trees)):

                if self.Map_mountains[y][x]==0:

                    if random() < 0.4 :

                        self.Map_trees[y][x]=1

                        self.Case.append((x, y))

                        continue

                    if random() < 0.05 :

                        self.Map_obtacles[y][x]=1

                        continue

                    if random() < self.p_grass:

                        self.Grass[y][x]=1

                        continue

                    self.Case.append((x, y)) # si aucun objet, un arbre pourra potentiellement poussé


        # image filename
                                            
        self.background_image_filename = 'dirt.png'   # image backgound 
        self.tree_image_filename = 'PNG/tree.png' 
        self.burn_tree_image_filename = 'smokeOrange0.png' 
        self.wooded_tree_image_filename = 'PNG/wooded_tree.png'
        self.rock_image_filename = 'PNG/rock2.png'  
        self.grass_image_filename = 'grass.png' 

        self.green_SW_image_filename = 'PNG/green_SW.png'  
        self.green_NW_image_filename = 'PNG/green_NW.png'  
        self.green_SE_image_filename = 'PNG/green_SE.png' 
        self.green_NE_image_filename = 'PNG/green_NE.png'
        self.green_center_image_filename = 'PNG/green_inside.png'
        self.green_S_image_filename = 'PNG/green_S.png'
        self.green_N_image_filename = 'PNG/green_N.png'
        self.green_E_image_filename = 'PNG/green_E.png'
        self.green_W_image_filename = 'PNG/green_W.png'
        self.green_corner_NE_image_filename = 'PNG/green_corner_NE.png'
        self.green_corner_NW_image_filename = 'PNG/green_corner_NW.png'
        self.green_corner_SE_image_filename = 'PNG/green_corner_SE.png'
        self.green_corner_SW_image_filename = 'PNG/green_corner_SW.png'


        

        pygame.init()          
                                                     
        self.screen = pygame.display.set_mode((int(self.size_tile_X*self.size_factor_X), int(self.size_tile_Y*self.size_factor_Y)),DOUBLEBUF)

        pygame.display.set_caption("WORLD TEST")     
                     
        self.background = pygame.image.load(self.background_image_filename).convert_alpha()   # tuile pour le background
        self.background = pygame.transform.scale(self.background, (int(self.size_tile_X), int(self.size_tile_Y)))


        self.tree = pygame.image.load(self.tree_image_filename).convert_alpha()
        self.tree = pygame.transform.scale(self.tree, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.burn_tree = pygame.image.load(self.burn_tree_image_filename).convert_alpha()
        self.burn_tree = pygame.transform.scale(self.burn_tree, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.wooded_tree = pygame.image.load(self.wooded_tree_image_filename).convert_alpha()
        self.wooded_tree = pygame.transform.scale(self.wooded_tree, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.rock = pygame.image.load(self.rock_image_filename).convert_alpha()
        self.rock = pygame.transform.scale(self.rock, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.grass = pygame.image.load(self.grass_image_filename).convert_alpha()
        self.grass = pygame.transform.scale(self.grass, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_SW = pygame.image.load(self.green_SW_image_filename).convert_alpha()
        self.green_SW = pygame.transform.scale(self.green_SW, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_NW = pygame.image.load(self.green_NW_image_filename).convert_alpha()
        self.green_NW = pygame.transform.scale(self.green_NW, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_SE = pygame.image.load(self.green_SE_image_filename).convert_alpha()
        self.green_SE = pygame.transform.scale(self.green_SE, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_NE = pygame.image.load(self.green_NE_image_filename).convert_alpha()
        self.green_NE = pygame.transform.scale(self.green_NE, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_S = pygame.image.load(self.green_S_image_filename).convert_alpha()
        self.green_S = pygame.transform.scale(self.green_S, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_N = pygame.image.load(self.green_N_image_filename).convert_alpha()
        self.green_N = pygame.transform.scale(self.green_N, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_E = pygame.image.load(self.green_E_image_filename).convert_alpha()
        self.green_E = pygame.transform.scale(self.green_E, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_W = pygame.image.load(self.green_W_image_filename).convert_alpha()
        self.green_W = pygame.transform.scale(self.green_W, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_corner_SW = pygame.image.load(self.green_corner_SW_image_filename).convert_alpha()
        self.green_corner_SW = pygame.transform.scale(self.green_corner_SW, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_corner_NW = pygame.image.load(self.green_corner_NW_image_filename).convert_alpha()
        self.green_corner_NW = pygame.transform.scale(self.green_corner_NW, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_corner_SE = pygame.image.load(self.green_corner_SE_image_filename).convert_alpha()
        self.green_corner_SE = pygame.transform.scale(self.green_corner_SE, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_corner_NE = pygame.image.load(self.green_corner_NE_image_filename).convert_alpha()
        self.green_corner_NE = pygame.transform.scale(self.green_corner_NE, (int(self.size_tile_X), int(self.size_tile_Y)))

        self.green_center = pygame.image.load(self.green_center_image_filename).convert_alpha()
        self.green_center = pygame.transform.scale(self.green_center, (int(self.size_tile_X), int(self.size_tile_Y)))



    def forestFire(self):

        # on recopie si vide

        if len(self.Tmp)==0:

            self.Tmp = self.Case.copy()

        i = randint(0,len(self.Tmp)-1)

        x, y = self.Tmp[i]

        if self.Map_trees[y][x]==3:

            self.Map_trees[y][x]=0

        # probabilité qu'un arbre repousse

        if self.Map_trees[y][x]==0 and random() < self.p1:

            self.Map_trees[y][x]=1

        # probabilité qu'un arbre s'embrase 

        if self.Map_trees[y][x]==1 and random() < self.p2:

            self.Map_trees[y][x]=2

        # le feu se propage d'abre en arbre 

        if self.Map_trees[y][x]==2:

            for x2 in range(x-1,x+2):

                for y2 in range(y-1,y+2):

                    x3 = x2

                    y3 = y2

                    if x3 < 0:

                        x3 += self.size_factor_X

                    if x3 >= self.size_factor_X:

                        x3 -= self.size_factor_X

                    if y3 < 0:

                        y3 += self.size_factor_Y

                    if y3 >= self.size_factor_Y:

                        y3 -= self.size_factor_Y

                    if self.Map_trees[y3][x3] == 1:

                        self.Map_trees[y3][x3] = 2

            self.Map_trees[y][x] = 3


        del self.Tmp[i]
        

        
            
                

    def updateWorld(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        while True:

            #self.forestFire()

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe           

            # update de l'environnement : 
            
            #for x in range(0, int(self.size_X*self.scaleMultiplier*self.size_factor_X), int(self.size_X*self.scaleMultiplier)):
            for x in range (0,len(self.Map_trees[0])):
                #for y in range(0, int(self.size_Y*self.scaleMultiplier*self.size_factor_Y), int(self.size_Y*self.scaleMultiplier)):
                for y in range(0,len(self.Map_trees)):

                    self.screen.blit(self.background,(x*self.size_tile_X,y*self.size_tile_Y))  # tuile "background" en position (x,y)

                    if self.Map_trees[y][x]==1:

                        self.screen.blit(self.tree,(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_trees[y][x]==2:

                        self.screen.blit(self.burn_tree,(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_trees[y][x]==3:

                        self.screen.blit(self.wooded_tree,(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_obtacles[y][x]==1:

                        self.screen.blit(self.rock,(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_mountains[y][x]>=1:

                        i = self.Map_mountains[y][x]-1

                        x_mn, y_mn = x - 1, y - 1
                        x_mx, y_mx = x + 1, y + 1

                        if x_mn < 0:

                            x_mn += self.size_factor_X

                        if x_mx >= self.size_factor_X:

                            x_mx -= self.size_factor_X

                        if y_mn < 0:

                            y_mn += self.size_factor_Y

                        if y_mx >= self.size_factor_Y:

                            y_mx -= self.size_factor_Y

                        # Sud

                        if self.Map_mountains[y_mx][x]==i: 

                            # Ouest

                            if self.Map_mountains[y][x_mn]==i:

                                self.screen.blit(self.green_SW,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            # Est

                            if self.Map_mountains[y][x_mx]==i:

                                self.screen.blit(self.green_SE,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            self.screen.blit(self.green_S,(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # Nord

                        if self.Map_mountains[y_mn][x]==i: 

                            # Ouest

                            if self.Map_mountains[y][x_mn]==i:

                                self.screen.blit(self.green_NW,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            # Est

                            if self.Map_mountains[y][x_mx]==i:

                                self.screen.blit(self.green_NE,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            self.screen.blit(self.green_N,(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # Est 

                        if self.Map_mountains[y][x_mx]==i:

                            self.screen.blit(self.green_E,(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # Ouest

                        if self.Map_mountains[y][x_mn]==i:

                            self.screen.blit(self.green_W,(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # SE corner

                        if self.Map_mountains[y_mx][x_mx]==i:

                            if self.Map_mountains[y_mx][x]>i and self.Map_mountains[y][x_mx]>i:

                                self.screen.blit(self.green_corner_SE,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                        #SW corner

                        if self.Map_mountains[y_mx][x_mn]==i:

                            if self.Map_mountains[y_mx][x]>i and self.Map_mountains[y][x_mn]>i:

                                self.screen.blit(self.green_corner_SW,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                        #NW corner

                        if self.Map_mountains[y_mn][x_mn]==i:

                            if self.Map_mountains[y_mn][x]>i and self.Map_mountains[y][x_mn]>i:

                                self.screen.blit(self.green_corner_NW,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                        # NE corner

                        if self.Map_mountains[y_mn][x_mx]==i:

                            if self.Map_mountains[y_mn][x]>i and self.Map_mountains[y][x_mx]>i :

                                self.screen.blit(self.green_corner_NE,(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                        self.screen.blit(self.green_center,(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Grass[y][x]==1:

                        self.screen.blit(self.grass,(x*self.size_tile_X,y*self.size_tile_Y))
                    

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
        world.updateWorld()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
        world.destroy()

        