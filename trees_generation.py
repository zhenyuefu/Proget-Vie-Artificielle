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

                if random() < 0.5 :
                    
                    self.Map_trees[y][x]=1
                    
                    self.Case.append((x, y, 0, True))

                    continue

                self.Case.append((x, y, 0, False))

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
    
    def trees_gen(self):

        i = randint(0,len(self.Case)-1)

        x, y, state, alive = self.Case[i]

        if state < 16 and alive:

            state += 1

            self.Case[i] = x, y, state, alive


    def update_world(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        

        while True:

            self.trees_gen()

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe           

            # update de l'environnement : 
            
            #for x in range(0, int(self.size_X*self.scaleMultiplier*self.size_factor_X), int(self.size_X*self.scaleMultiplier)):
            for x in range (self.size_factor_X):
                #for y in range(0, int(self.size_Y*self.scaleMultiplier*self.size_factor_Y), int(self.size_Y*self.scaleMultiplier)):
                for y in range(self.size_factor_Y):

                    self.screen.blit(self.Environment_images[0][0],(x*self.size_tile_X,y*self.size_tile_Y))  # tuile "background" en position (x,y)
                    
                    
            for tree in self.Case:
                
                x, y, state, alive = tree
                    
                if alive:
                    
                    self.screen.blit(self.Environment_images[1][state],(x * self.size_tile_X, y * self.size_tile_Y))

            
                        
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
        clock.tick(10000)