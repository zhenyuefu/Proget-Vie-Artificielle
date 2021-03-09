#!/usr/bin/env python3


from random import *
import pygame                   # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 

class Agent(object):

    def __init__(self, x, y, predator_or_prey, world):

        self.x, self.y = x, y
        self.world = world
        self.predator_or_prey = predator_or_prey
        self.orient = 0
        self.reproduce = 0.03
        self.delai_famine = 14
        self.it_non_mange = 0
        self.predator, self.prey = False, False
        self.alive = True
        self.dir = -1

        if predator_or_prey :

            self.predator = True

        else:

            self.prey = True


    def setDirection(self,d):

        if self.dir == -1 :

            self.dir = d

        if random() < 0.5 :

            self.dir = d

    def reset_mange(self):

        self.it_non_mange = 0

    def reproduce(self):
        return

    def step(self):

        self.it_non_mange += 1

        if self.it_non_mange > self.delai_famine :

            self.alive = False

        self.reproduce()

        if random() < 0.5 :

            self.orient = (self.orient - 1) % 4

        else:

            self.orient = (self.orient - 1 + 4) % 4

        if dir != -1 :

            self.orient = self.dir

        self.dir = -1


        if self.orient == 0 :

            self.y = (self.y - 1 + world.size_factor_X) % world.size_factor_X

            return
        
        if self.orient == 1 :

            self.x = (self.x + 1 + world.size_factor_Y) % world.size_factor_Y

            return

        if self.orient == 2 :

            self.y = (self.y + 1 + world.size_factor_X) % world.size_factor_X

            return

        if self.orient == 3 :

            self.x = (self.x - 1 + world.size_factor_Y) % world.size_factor_Y

            return



class World:
    """
    classe principale du jeux
    """

    def __init__(self, size_factor_X=50, size_factor_Y=37, size_tile_X=32, size_tile_Y=32):
        """
        constructeur de la classe
        size_factor_X et size_factor_Y représentent la taille du plateau de jeux en nombre de tuiles 64*64 pixels
        """



        self.size_factor_X, self.size_factor_Y = size_factor_X, size_factor_Y

        self.size_tile_X, self.size_tile_Y = size_tile_X, size_tile_Y

        # liste temporaire qui va mettre à jour chaque cellule de Case

        self.Tmp = []

        # lists filename

        self.Environment_images=[]

        ################

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

            longueur, largeur = randint(10,11), randint(10,11)

            self.MountainsType.append([x[:] for x in [[1] * largeur] * longueur])

        # Mountains random placement

        nbMountains = randint(10,12)

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

                    self.Map_mountains[y2][x2]=M[y][x]

        #Trees, obstacles, grass random placement

        for x in range(0,len(self.Map_trees[0])):

            for y in range(0,len(self.Map_trees)):

                if self.Map_mountains[y][x]==0:

                    if random() < 0.02 :

                        self.Map_trees[y][x]=1

                        self.Case.append((x, y))

                        continue

                    if random() < 0.01 :

                        self.Map_obtacles[y][x]=1

                        continue

                    if random() < self.p_grass:

                        self.Grass[y][x]=1

                        continue

                    self.Case.append((x, y)) # si aucun objet, un arbre pourra potentiellement poussé


        ###########################

        pygame.init()          
                                                     
        self.screen = pygame.display.set_mode((int(self.size_tile_X*self.size_factor_X), int(self.size_tile_Y*self.size_factor_Y)),DOUBLEBUF)

        pygame.display.set_caption("WORLD TEST")  


    def loadImage(self,filename):

        image = pygame.image.load(filename).convert_alpha()

        image = pygame.transform.scale(image, (int(self.size_tile_X), int(self.size_tile_Y)))

        return image   


    def loadAllImage(self):

        # 0 : backgrounds            
        self.Environment_images.append([self.loadImage('dirt.png')]) 

        # 1 : trees
        self.Environment_images.append([self.loadImage('PNG/tree.png'),self.loadImage('smokeOrange0.png'),self.loadImage('PNG/wooded_tree.png'),self.loadImage('PNG/big_tree.png')])

        # 2 : obstacles
        self.Environment_images.append([self.loadImage('PNG/rock1.png'),self.loadImage('PNG/rock2.png')]) 

        # 3 : herbs
        self.Environment_images.append([self.loadImage('grass.png')])

        # 4 : Mountains
        self.Environment_images.append([self.loadImage('PNG/green_inside.png'),self.loadImage('PNG/green_SW.png'),self.loadImage('PNG/green_NW.png'),
            self.loadImage('PNG/green_SE.png'),self.loadImage('PNG/green_NE.png'),self.loadImage('PNG/green_S.png'),self.loadImage('PNG/green_N.png'),
            self.loadImage('PNG/green_E.png'),self.loadImage('PNG/green_W.png'),self.loadImage('PNG/green_corner_NE.png'),self.loadImage('PNG/green_corner_NW.png'),
            self.loadImage('PNG/green_corner_SE.png'),self.loadImage('PNG/green_corner_SW.png')])


        



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

            self.forestFire()

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe           

            # update de l'environnement : 
            
            #for x in range(0, int(self.size_X*self.scaleMultiplier*self.size_factor_X), int(self.size_X*self.scaleMultiplier)):
            for x in range (0,len(self.Map_trees[0])):
                #for y in range(0, int(self.size_Y*self.scaleMultiplier*self.size_factor_Y), int(self.size_Y*self.scaleMultiplier)):
                for y in range(0,len(self.Map_trees)):

                    self.screen.blit(self.Environment_images[0][0],(x*self.size_tile_X,y*self.size_tile_Y))  # tuile "background" en position (x,y)

                    if self.Map_trees[y][x]==1:

                        self.screen.blit(self.Environment_images[1][0],(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_trees[y][x]==2:

                        self.screen.blit(self.Environment_images[1][1],(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_trees[y][x]==3:

                        self.screen.blit(self.Environment_images[1][2],(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_obtacles[y][x]==1:

                        self.screen.blit(self.Environment_images[2][0],(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Map_mountains[y][x]>0:

                        i = self.Map_mountains[y][x]-1

                        if i>0:

                            self.screen.blit(self.Environment_images[4][0],(x*self.size_tile_X,y*self.size_tile_Y))

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

                        if self.Map_mountains[y_mx][x]<=i: 

                            # Ouest

                            if self.Map_mountains[y][x_mn]<=i:

                                self.screen.blit(self.Environment_images[4][1],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            # Est

                            if self.Map_mountains[y][x_mx]<=i:

                                self.screen.blit(self.Environment_images[4][3],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            self.screen.blit(self.Environment_images[4][5],(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # Nord

                        if self.Map_mountains[y_mn][x]<=i: 

                            # Ouest

                            if self.Map_mountains[y][x_mn]<=i:

                                self.screen.blit(self.Environment_images[4][2],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            # Est

                            if self.Map_mountains[y][x_mx]<=i:

                                self.screen.blit(self.Environment_images[4][4],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                            self.screen.blit(self.Environment_images[4][6],(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # Est 

                        if self.Map_mountains[y][x_mx]<=i:

                            self.screen.blit(self.Environment_images[4][7],(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # Ouest

                        if self.Map_mountains[y][x_mn]<=i:

                            self.screen.blit(self.Environment_images[4][8],(x*self.size_tile_X,y*self.size_tile_Y))

                            continue

                        # SE corner

                        if self.Map_mountains[y_mx][x_mx]==i:

                            if self.Map_mountains[y_mx][x]>i and self.Map_mountains[y][x_mx]>i:

                                self.screen.blit(self.Environment_images[4][11],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                        #SW corner

                        if self.Map_mountains[y_mx][x_mn]==i:

                            if self.Map_mountains[y_mx][x]>i and self.Map_mountains[y][x_mn]>i:

                                self.screen.blit(self.Environment_images[4][12],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                        #NW corner

                        if self.Map_mountains[y_mn][x_mn]==i:

                            if self.Map_mountains[y_mn][x]>i and self.Map_mountains[y][x_mn]>i:

                                self.screen.blit(self.Environment_images[4][10],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue

                        # NE corner

                        if self.Map_mountains[y_mn][x_mx]==i:

                            if self.Map_mountains[y_mn][x]>i and self.Map_mountains[y][x_mx]>i:

                                self.screen.blit(self.Environment_images[4][9],(x*self.size_tile_X,y*self.size_tile_Y))

                                continue



                        self.screen.blit(self.Environment_images[4][0],(x*self.size_tile_X,y*self.size_tile_Y))

                        continue

                    if self.Grass[y][x]==1:

                        self.screen.blit(self.Environment_images[3][0],(x*self.size_tile_X,y*self.size_tile_Y))
                    

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
    world.loadAllImage()
    try:
        world.updateWorld()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
        world.destroy()

        