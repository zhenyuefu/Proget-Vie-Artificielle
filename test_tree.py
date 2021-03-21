from sys import exit  # exit script

import pygame  # PYGAME package
from pygame.locals import *  # PYGAME constant & functions
import random
from Tree import *
from Grass import *
from Obstacle import *
from Block import *

class World:
    """
    classe principale du jeux
    """

    def __init__(
            self, screenWidth=1188, screenHeight=800
    ):
        """
        constructeur de la classe
        """

        self.screenWidth, self.screenHeight = screenWidth, screenHeight

        self.size_tree_X, self.size_tree_Y = 36, 32

        self.size_grass_X, self.size_grass_Y = self.size_tree_X // 2, self.size_tree_Y // 2

        self.size_obstacle_X, self.size_obstacle_Y = self.size_tree_X, self.size_tree_Y

        self.size_block_X, self.size_block_Y = self.size_tree_X, self.size_tree_Y

        self.Map_trees = [x[:] for x in [[None] * (self.screenWidth // self.size_tree_X)] * (self.screenHeight // self.size_tree_Y)]

        self.Map_grass = [x[:] for x in [[None] * (self.screenWidth // self.size_grass_X)] * (self.screenHeight // self.size_grass_Y)]

        self.Map_mountains=[x[:] for x in [[0] * (self.screenWidth // self.size_block_X)] * (self.screenHeight // self.size_block_Y)]

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

        self.MountainsType=[]

        self.Fire_images = []

        self.Trees = []

        self.Tmp = []

        self.load_all_image()

        self.tree_group = pygame.sprite.Group()

        self.grass_group = pygame.sprite.Group()

        self.obstacle_group = pygame.sprite.Group()

        self.block_group = pygame.sprite.Group()


        # Type de montagnes

        for i in range(3):

            longueur, largeur = random.randint(10,11), random.randint(10,11)

            self.MountainsType.append([x[:] for x in [[1] * largeur] * longueur])


        # Mountains random placement

        nbMountains = random.randint(2,4)

        for i in range(nbMountains):

            x_offset, y_offset = random.randint(0,len(self.Map_mountains[0])-1), random.randint(0,len(self.Map_mountains)-1)

            M = self.MountainsType[random.randint(0,len(self.MountainsType)-1)]

            for x in range(len(M[0])):

                for y in range(len(M)):

                    x2, y2 = x + x_offset, y + y_offset

                    if x2 < 0:

                        x2 += len(self.Map_mountains[0])

                    if x2 >= len(self.Map_mountains[0]):

                        x2 -= len(self.Map_mountains[0])

                    if y2 < 0:

                        y2 += len(self.Map_mountains)

                    if y2 >= len(self.Map_mountains):

                        y2 -= len(self.Map_mountains)

                    self.Map_mountains[y2][x2]=M[y][x]

                    self.block_group.add(Block(self,x2,y2))


        # Tree and obstacle random placment

        for x in range(len(self.Map_trees[0])):

            for y in range(len(self.Map_trees)):

                if self.Map_mountains[y][x]==0:
                    
                    if random.random() < 0.1:
                        
                        self.Map_trees[y][x] = Tree(self,x,y)
                        
                        self.Trees.append((x, y))
                        
                        self.tree_group.add(self.Map_trees[y][x])
                        
                        continue
                    
                    if random.random() < 0.01:
                        
                        self.obstacle_group.add(Obstacle(self,x,y))

                        continue

                    #self.Trees.append((x, y))


        # set frame block

        for block in self.block_group:

            block.update_block()


        # Grass random placment


        for x in range(len(self.Map_grass[0])):

            for y in range(len(self.Map_grass)):

                 if random.random() < 0.1:

                     self.Map_grass[y][x] = Grass(self,x,y)

                     self.grass_group.add(self.Map_grass[y][x])

            

        # Collision between grass and tree / obstacle

        for tree in self.tree_group:
            
            for obstacle in self.obstacle_group:
                
                for grass in self.grass_group:
                    
                    if tree.rect.colliderect(grass.rect) or obstacle.rect.colliderect(grass.rect):
                        
                        grass.kill()



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
                # self.load_image("PNG/split/fire1.png", 10, 10),
                # self.load_image("PNG/split/fire2.png", 10, 10),
                # self.load_image("PNG/split/fire3.png", 10, 10),
                self.load_image("PNG/split/fire4.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire5.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire6.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire7.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/fire8.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/cendre1.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/cendre2.png", self.size_tree_X, self.size_tree_Y),
                self.load_image("PNG/split/cendre3.png", self.size_tree_X, self.size_tree_Y),
            ]
        
        )

        # 3 : grass

        self.Environment_images.append(
            
            [
                self.load_image("PNG/split/grass.png", self.size_grass_X, self.size_grass_Y),
                self.load_image("PNG/split/grass_repousse.png", self.size_grass_X, self.size_grass_Y),
            ]

        )

        # 4 : obstacle

        self.Environment_images.append(
            
            [
                self.load_image("PNG/split/rock.png", self.size_obstacle_X, self.size_obstacle_Y),
            ]

        )

        # 5 : Block

        self.Environment_images.append(
            [
                self.load_image("PNG/green_inside.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_SW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_NW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_SE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_NE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_S.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_N.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_E.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_W.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_corner_NE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_corner_NW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_corner_SE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/green_corner_SW.png", self.size_block_X, self.size_block_Y),
            ]
        )



    def update_object(self):

        # TREE

        if not self.Tmp:
            
            self.Tmp = self.Trees.copy()


        i = random.randint(0,len(self.Tmp)-1)
            
        x, y = self.Tmp[i]

        if self.Map_trees[y][x] == None:
            
            if random.random() < 0.0001 :
                
                self.Map_trees[y][x] = Tree(self,x,y)
                
                self.tree_group.add(self.Map_trees[y][x])

                self.Map_trees[y][x].update_tree()


        else:
            
            self.Map_trees[y][x].update_tree()



        # Collision between grass and tree / obstacle

        # for tree in self.tree_group:
            
        #     for obstacle in self.obstacle_group:
                
        #         for grass in self.grass_group:
                    
        #             if tree.rect.colliderect(grass.rect) or obstacle.rect.colliderect(grass.rect): -----> Ralenti le programme
                        
        #                 grass.kill()

        # BLOCK

        self.block_group.update()
        
        self.block_group.draw(self.screen)

        # TREE

        self.tree_group.update()
            
        self.tree_group.draw(self.screen)

        del self.Tmp[i]

        # GRASS

        self.grass_group.update()

        self.grass_group.draw(self.screen)

        # OBSTACLE
        
        self.obstacle_group.update()
        
        self.obstacle_group.draw(self.screen)

        

        
   

    def update_world(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        

        while True:

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  
                    self.destroy()                
            
            for x in range (self.screenWidth // 32 + 1):
                
                for y in range(self.screenHeight // 32 + 1):

                    self.screen.blit(self.Environment_images[0][0],(x*32,y*32))  

            self.update_object()
            
            pygame.display.update()



    def destroy(self):
        """
        destructeur de la classe
        """
        print('Exit')
        pygame.quit() # ferme la fenêtre principale
        exit()       

if __name__ == "__main__":
    world = World()
    clock = pygame.time.Clock()
    try:
        world.update_world()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy().
        world.destroy()
    clock.tick(20)

