from sys import exit  # exit script

import pygame  # PYGAME package
from pygame.locals import *  # PYGAME constant & functions
import random
from Tree import *

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

        self.Map_trees=[x[:] for x in [[None] * self.size_factor_X] * self.size_factor_Y]

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

        self.Trees = []

        self.Tmp = []

        self.load_all_image()

        self.tree_group = pygame.sprite.Group()

        for x in range(self.size_factor_X):

            for y in range(self.size_factor_Y):

                if random.random() < 0.1:
                    
                    self.Map_trees[y][x] = Tree(self,self.Environment_images[1][0],x,y)

                    self.Trees.append((x, y))
                    
                    self.tree_group.add(self.Map_trees[y][x])



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

    def update_world(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        

        while True:

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe           

            # update de l'environnement : 
            
            for x in range (self.size_factor_X):
                
                for y in range(self.size_factor_Y):

                    self.screen.blit(self.Environment_images[0][0],(x*self.size_tile_X,y*self.size_tile_Y))  # tuile "background" en position (x,y)

            if not self.Tmp:

                self.Tmp = self.Trees.copy()

            i = random.randint(0,len(self.Tmp)-1)
            
            x, y = self.Tmp[i]

            self.Map_trees[y][x].update_tree()

            del self.Tmp[i]

            self.tree_group.update()
            
            self.tree_group.draw(self.screen)
            
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
    try:
        world.update_world()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy().
        world.destroy()
    clock.tick(20000)

