from sys import exit  # exit script

import pygame  # PYGAME package
from pygame.locals import *  # PYGAME constant & functions
import random
from Tree import *
from Grass import *

class World:
    """
    classe principale du jeux
    """

    def __init__(
            self, screenWidth=1200, screenHeight=800
    ):
        """
        constructeur de la classe
        """

        self.screenWidth, self.screenHeight = screenWidth, screenHeight

        self.size_tree_X, self.size_tree_Y = 40, 40

        self.size_grass_X, self.size_grass_Y = 20, 20

        self.Map_trees = [x[:] for x in [[None] * (self.screenWidth // self.size_tree_X)] * (self.screenHeight // self.size_tree_Y)]

        self.Map_grass = [x[:] for x in [[None] * (self.screenWidth // self.size_grass_X)] * (self.screenHeight // self.size_grass_Y)]

        pygame.init()

        self.screen = pygame.display.set_mode(
            (
                int(self.screenWidth),
                int(self.screenHeight),
            ),
            DOUBLEBUF,
        )
        pygame.display.set_caption("WORLD TEST")

        self.Environment_images = []

        self.Fire_images = []

        self.Trees = []

        self.Tmp = []

        self.load_all_image()

        self.tree_group = pygame.sprite.Group()

        self.grass_group = pygame.sprite.Group()

        for x in range(len(self.Map_trees[0])):

            for y in range(len(self.Map_trees)):

                if random.random() < 0.09:
                    
                    self.Map_trees[y][x] = Tree(self,x,y)

                    self.Trees.append((x, y))
                    
                    self.tree_group.add(self.Map_trees[y][x])


        for x in range(len(self.Map_grass[0])):

            for y in range(len(self.Map_grass)):

                 if random.random() < 0.1:

                     self.Map_grass[y][x] = Grass(self,x,y)

                     self.grass_group.add(self.Map_grass[y][x])



    def load_image(self, filename, tile_size_X, tile_size_Y):

        image = pygame.image.load(filename).convert_alpha()

        image = pygame.transform.scale(
            image, (int(tile_size_X), int(tile_size_Y))
        )

        return image

    def load_all_image(self):

        # 0 : backgrounds

        self.Environment_images.append([self.load_image("dirt.png", 32, 32)])

        # 1 : trees

        self.Environment_images.append(
            [
                self.load_image("PNG/split/tree1.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree2.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree3.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree4.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree5.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree6.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree7.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree8.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree9.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree10.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree11.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree12.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree13.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree14.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree15.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree16.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/tree17.png", self.size_tree_X, self.size_tree_Y),
            ]
        )

        # 2 : fire

        self.Fire_images.append(
            [
                self.load_image("PNG/split/fire4.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire5.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire6.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire7.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire8.png", self.size_tree_X, self.size_tree_Y),
            ]
        
        )

        # 3 : grass

        self.Environment_images.append(
            
            [
                self.load_image("PNG/split/grass.png", self.size_grass_X, self.size_grass_Y),
                self.load_image("PNG/split/grass_repousse.png", self.size_grass_X, self.size_grass_Y),
            ]

        )

    def forestFire(self):

        if not self.Tmp:
            
            self.Tmp = self.Trees.copy()


        i = random.randint(0,len(self.Tmp)-1)
            
        x, y = self.Tmp[i]

        if self.Map_trees[y][x].inFire:

            for x2 in range(x-1,x+2):

                for y2 in range(y-1,y+2):

                    x3 = x2

                    y3 = y2

                    if x3 < 0:

                        x3 += len(self.Map_trees[0])

                    if x3 >= len(self.Map_trees[0]):

                        x3 -= len(self.Map_trees[0])

                    if y3 < 0:

                        y3 += len(self.Map_trees)

                    if y3 >= len(self.Map_trees):

                        y3 -= len(self.Map_trees)

                    if self.Map_trees[y3][x3] != None and self.Map_trees[y3][x3].alive:

                        self.Map_trees[y3][x3].inFire

                        self.Map_trees[y3][x3].update_tree()

        
        self.Map_trees[y][x].update_tree()

        self.tree_group.update()
            
        self.tree_group.draw(self.screen)

        del self.Tmp[i]

        




        

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
            
            for x in range (self.screenWidth // 32 + 1):
                
                for y in range(self.screenHeight // 32 + 1):

                    self.screen.blit(self.Environment_images[0][0],(x*32,y*32))  # tuile "background" en position (x,y)

            self.forestFire()

            self.grass_group.update()

            self.grass_group.draw(self.screen)
            
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

