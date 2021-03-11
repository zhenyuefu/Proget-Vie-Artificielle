#!/usr/bin/env python3


from random import *
import pygame                   # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 


class World:  
    """
    classe principale du jeux
    """

    def __init__(
            self, size_factor_X=35, size_factor_Y=17, size_tile_X=30, size_tile_Y=30
    ):
        """
        constructeur de la classe
        size_factor_X et size_factor_Y représentent la taille du plateau de jeux en nombre de tuiles 64*64 pixels
        """

        self.size_factor_X, self.size_factor_Y = size_factor_X, size_factor_Y

        self.size_tile_X, self.size_tile_Y = size_tile_X, size_tile_Y

        self.Map_trees=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.Case = []

        self.Tmp = []

        for x in range(0,len(self.Map_trees[0])):

            for y in range(0,len(self.Map_trees)):

                if x == self.size_factor_X//2 and y == self.size_factor_Y//2 :

                    self.Map_trees[y][x] = 2

                    self.Case.append((x, y, 16, True, 0, True))

                    continue             

                if random() < 0.2 :
                    
                    self.Map_trees[y][x]=1
                    
                    self.Case.append((x, y, 0, True, 0, False))

                    continue

                #self.Case.append((x, y, 0, False))

        pygame.init()

        self.screen = pygame.display.set_mode(
            (
                int(self.size_tile_X * self.size_factor_X),
                int(self.size_tile_Y * self.size_factor_Y),
            ),
            DOUBLEBUF,
        )
        pygame.display.set_caption("WORLD TEST")

        self.Environment_images = []

        self.Fire_images = []

        self.p2 = 0.001

        self.load_all_image()
        


    def load_image(self, filename):

        image = pygame.image.load(filename).convert_alpha()

        image = pygame.transform.scale(
            image, (int(self.size_tile_X), int(self.size_tile_Y))
        )

        return image

    def load_all_image(self):

        # 0 : backgrounds
        self.Environment_images.append([self.load_image("dirt.png")])

        # 1 : trees
        self.Environment_images.append(
            [
                self.load_image("PNG/split/tree1.png"),
                self.load_image("PNG/split/tree2.png"),
                self.load_image("PNG/split/tree3.png"),
                self.load_image("PNG/split/tree4.png"),
                self.load_image("PNG/split/tree5.png"),
                self.load_image("PNG/split/tree6.png"),
                self.load_image("PNG/split/tree7.png"),
                self.load_image("PNG/split/tree8.png"),
                self.load_image("PNG/split/tree9.png"),
                self.load_image("PNG/split/tree10.png"),
                self.load_image("PNG/split/tree11.png"),
                self.load_image("PNG/split/tree12.png"),
                self.load_image("PNG/split/tree13.png"),
                self.load_image("PNG/split/tree14.png"),
                self.load_image("PNG/split/tree15.png"),
                self.load_image("PNG/split/tree16.png"),
                self.load_image("PNG/split/tree17.png"),
            ]
        )

        # 2 : fire

        self.Fire_images.append(
            [
                self.load_image("PNG/split/fire1.png"),
                self.load_image("PNG/split/fire2.png"),
                self.load_image("PNG/split/fire3.png"),
                self.load_image("PNG/split/fire4.png"),
                self.load_image("PNG/split/fire5.png"),
                self.load_image("PNG/split/fire6.png"),
                self.load_image("PNG/split/fire7.png"),
                self.load_image("PNG/split/fire8.png"),
            ]
        
        )

    def tree_in_fire(self):

        i = randint(0,len(self.Case)-1)
        
        x, y, state, alive, stateF, inFire = self.Case[i]
        
        if inFire:
            
            if stateF == 7 :
                
                inFire = False
                alive = False
                
            if stateF < 7 :
                
                stateF += 1
                 
        self.Case[i] = x, y, state, alive, stateF, inFire



    def trees_gen(self):

        i = randint(0,len(self.Case)-1)
        
        x, y, state, alive, stateF, inFire = self.Case[i]

        if state < 16 and alive:
            
            if random() < 0.3:
                
                state += 1
                
        self.Case[i] = x, y, state, alive, stateF, inFire


    def forestFire(self):

        # on recopie si vide

        if len(self.Tmp)==0:

            self.Tmp = self.Case.copy()

        i = randint(0,len(self.Tmp)-1)

        x, y, _, _, _, _ = self.Tmp[i]

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



    def update_trees(self):
        
        for tree in self.Case:
            
            x, y, state, alive, stateF, inFire = tree
            
            if alive:
                
                self.screen.blit(self.Environment_images[1][state],(x * self.size_tile_X, y * self.size_tile_Y))
                
            if inFire:
                
                self.screen.blit(self.Fire_images[0][stateF],(x * self.size_tile_X, y * self.size_tile_Y))
        


    def update_world(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        

        while True:

            #self.forestFire()

            self.tree_in_fire()

            self.trees_gen()

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe           

            # update de l'environnement : 
            
            for x in range (self.size_factor_X):
                
                for y in range(self.size_factor_Y):

                    self.screen.blit(self.Environment_images[0][0],(x*self.size_tile_X,y*self.size_tile_Y))  # tuile "background" en position (x,y)
                    
                    
            self.update_trees()

            
                        
            pygame.display.update()

    def destroy(self):
        """
        destructeur de la classe
        """
        print('Exit')
        pygame.quit() # ferme la fenêtre principale
        exit()        # termine tous les process en cours

if __name__ == "__main__":
    world = World()
    clock = pygame.time.Clock()
    while True:
        try:
            world.update_world()
        except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy().
            world.destroy()
        clock.tick(20000)