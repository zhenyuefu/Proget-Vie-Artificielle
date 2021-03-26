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

        self.size_bg_X, self.size_bg_Y = self.size_tree_X, self.size_tree_Y

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

        self.saison = 1

        self.Environment_images = []

        self.Block_images = []

        self.MountainsType=[]

        self.Fire_images = []

        self.Trees = []

        self.Grass = []

        self.Tmp1 = []

        self.Tmp2 = []

        self.load_all_image()

        self.tree_group = pygame.sprite.Group()

        self.grass_group = pygame.sprite.Group()

        self.obstacle_group = pygame.sprite.Group()

        self.block_group = pygame.sprite.Group()

        self.all_object_group = pygame.sprite.Group()

        self.object_placment()


    # Type de montagnes

    def create_mountain(self):
            
        for i in range(3):
                
            longueur, largeur = random.randint(5,8), random.randint(5,8)
                
            self.MountainsType.append([x[:] for x in [[1] * largeur] * longueur])


    # Mountains random placement

    def object_placment(self):

        self.create_mountain()
            
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

                    self.all_object_group.add(Block(self,x2,y2))

                        
        # Tree and obstacle random placment

        for x in range(len(self.Map_trees[0])):
                
            for y in range(len(self.Map_trees)):
                    
                if self.Map_mountains[y][x]==0:
                        
                    if random.random() < 0.05:
                            
                        self.Map_trees[y][x] = Tree(self,x,y)
                            
                        self.Trees.append((x, y))
                            
                        self.tree_group.add(self.Map_trees[y][x])

                        self.all_object_group.add(Tree(self,x,y))
                            
                        continue
                        
                    if random.random() < 0.01:
                            
                        self.obstacle_group.add(Obstacle(self,x,y))

                        self.all_object_group.add(Obstacle(self,x,y))
                            
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

                    self.Grass.append((x,y))

                    self.grass_group.add(self.Map_grass[y][x])

            

        # Collision between grass and tree / obstacle

        for object in self.all_object_group:

            for grass in self.grass_group:
                
                if object.rect.colliderect(grass.rect):
                    
                    grass.kill()

                    

    def load_image(self, filename, tile_size_X, tile_size_Y):

        image = pygame.image.load(filename).convert_alpha()

        image = pygame.transform.scale(
            image, (int(tile_size_X), int(tile_size_Y))
        )

        return image

    def load_all_image(self):

        # 0 : backgrounds [0][]

        self.Environment_images.append(
            [
                self.load_image("PNG/background/bg1.png", self.size_bg_X, self.size_bg_Y),
                self.load_image("PNG/background/bg2.png", self.size_bg_X, self.size_bg_Y),
                self.load_image("PNG/background/bg3.png", self.size_bg_X, self.size_bg_Y),
                self.load_image("PNG/background/bg4.png", self.size_bg_X, self.size_bg_Y),
                self.load_image("PNG/background/bg5.png", self.size_bg_X, self.size_bg_Y),
                
            ]
            
        )

        # 1 : trees [1][]

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

        # 2 : fire =============== [0][]

        self.Fire_images.append(
            [
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

        # 3 : grass =============== [2][]

        self.Environment_images.append(
            
            [
                self.load_image("PNG/split/grass_repousse.png", self.size_grass_X, self.size_grass_Y),
                self.load_image("PNG/split/grass.png", self.size_grass_X, self.size_grass_Y),
                
            ]
            
        )

        # 4 : obstacle =============== [3][]

        self.Environment_images.append(
            
            [
                self.load_image("PNG/split/rock.png", self.size_obstacle_X, self.size_obstacle_Y),
            ]

        )

        # 5 : Block =============== [0][]

        self.Block_images.append(
            [
                self.load_image("PNG/Block/green_inside.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_SW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_NW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_SE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_NE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_S.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_N.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_E.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_W.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_corner_NE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_corner_NW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_corner_SE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/green_corner_SW.png", self.size_block_X, self.size_block_Y),
            ],
        )

        # Block =============== [1][]    

        self.Block_images.append(
            [
                self.load_image("PNG/Block/ice_inside.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_SW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_NW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_SE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_NE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_S.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_N.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_E.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_W.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_corner_NE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_corner_NW.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_corner_SE.png", self.size_block_X, self.size_block_Y),
                self.load_image("PNG/Block/ice_corner_SW.png", self.size_block_X, self.size_block_Y),
            ]
        )



    def update_object(self):

        # TREE

        if not self.Tmp1:
            
            self.Tmp1 = self.Trees.copy()


        i = random.randint(0,len(self.Tmp1)-1)
            
        x, y = self.Tmp1[i]

        if self.Map_trees[y][x] == None:
            
            if random.random() < 0.001 :
                
                self.Map_trees[y][x] = Tree(self,x,y)
                
                self.tree_group.add(self.Map_trees[y][x])

                self.Map_trees[y][x].update_tree()


        else:
            
            self.Map_trees[y][x].update_tree()


        # BLOCK

        #self.block_group.update()
        
        self.block_group.draw(self.screen)

        # TREE

        self.tree_group.update()
            
        self.tree_group.draw(self.screen)

        del self.Tmp1[i]

        # GRASS

        if not self.Tmp2:
            
            self.Tmp2 = self.Grass.copy()

        i = random.randint(0,len(self.Tmp2)-1)
            
        x, y = self.Tmp2[i]

        self.Map_grass[y][x].update_grass()

        self.grass_group.update()

        self.grass_group.draw(self.screen)

        del self.Tmp2[i]

        # OBSTACLE
        
        self.obstacle_group.update()
        
        self.obstacle_group.draw(self.screen)

        

        
   

    def update_world(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        #lecture des événements Pygame 
        for event in pygame.event.get():  
            if event.type == QUIT:  
                self.destroy()                
            
        for x in range (self.screenWidth // self.size_bg_X + 1):
                
            for y in range(self.screenHeight // self.size_bg_Y + 1):

                self.screen.blit(self.Environment_images[0][2],(x*self.size_bg_X,y*self.size_bg_Y))  

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
    while True:
        try:
            world.update_world()
        except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy().
            world.destroy()
        clock.tick(0)

