from sys import exit  # exit script

import pygame  # PYGAME package
from pygame.locals import *  # PYGAME constant & functions
import random

import Agent
from Tree import *
from Grass import *
from Obstacle import *
from Block import *
from Image import *
from Weather import *
from Cloud import *


class World:
    """
    classe principale du jeux
    """

    def __init__(
            self, screenWidth=1476, screenHeight=1088
    ):
        """
        constructeur de la classe
        """

        self.screenWidth, self.screenHeight = screenWidth, screenHeight

        self.size_tile_X, self.size_tile_Y = 32,32

        self.size_tree_X, self.size_tree_Y = 36, 32

        self.size_bg_X, self.size_bg_Y = self.size_tree_X, self.size_tree_Y

        self.size_cloud_X, self.size_cloud_Y = 128, 128

        self.size_grass_X, self.size_grass_Y = self.size_tree_X // 2, self.size_tree_Y // 2

        self.size_obstacle_X, self.size_obstacle_Y = self.size_tree_X, self.size_tree_Y

        self.size_block_X, self.size_block_Y = self.size_tree_X, self.size_tree_Y

        self.Map_trees = [x[:] for x in
                          [[None] * (self.screenWidth // self.size_tree_X)] * (self.screenHeight // self.size_tree_Y)]

        self.Map_grass = [x[:] for x in
                          [[None] * (self.screenWidth // self.size_grass_X)] * (self.screenHeight // self.size_grass_Y)]

        self.Map_mountains = [x[:] for x in [[0] * (self.screenWidth // self.size_block_X)] * (
                self.screenHeight // self.size_block_Y)]

        pygame.init()

        self.screen = pygame.display.set_mode(
            (
                int(self.screenWidth),
                int(self.screenHeight),
            ),
            DOUBLEBUF,
        )
        pygame.display.set_caption("WORLD TEST")

        self.weather = Weather()

        self.Environment_images = []

        self.sheep_images = []

        self.wolf_images = []

        self.Block_images = []

        self.Fire_images = []

        self.image = Image(self)

        self.image.load_all_image()

        self.MountainsType = []

        self.Trees = []

        self.Grass = []

        self.Tmp1 = []

        self.Tmp2 = []

        self.tree_group = pygame.sprite.Group()

        self.fire_group = pygame.sprite.Group()

        self.grass_group = pygame.sprite.Group()

        self.obstacle_group = pygame.sprite.Group()

        self.block_group = pygame.sprite.Group()

        self.wolf_group = pygame.sprite.Group()

        self.sheep_group = pygame.sprite.Group()

        self.cloud_group = pygame.sprite.Group()

        self.all_object_group = pygame.sprite.Group()

        self.object_placment()

        



    # Type de montagnes

    def create_mountain(self):

        for _ in range(3):

            longueur, largeur = random.randint(5, 8), random.randint(5, 8)

            self.MountainsType.append([x[:] for x in [[1] * largeur] * longueur])

        self.MountainsType.append([[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,2,2,2,2,2,2,2,2,2,2,2,2,1],
                                    [1,2,3,3,3,3,3,3,3,3,3,3,2,1],
                                    [1,2,3,3,3,3,3,3,3,3,3,3,2,1],
                                    [1,2,2,2,2,2,2,2,2,2,2,2,2,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        ])


    # Mountains random placement

    def object_placment(self):

        self.create_mountain()

        nbMountains = random.randint(2, 4)

        for _ in range(nbMountains):

            x_offset, y_offset = random.randint(0, len(self.Map_mountains[0]) - 1), random.randint(0, len(self.Map_mountains) - 1)

            M = self.MountainsType[random.randint(0, len(self.MountainsType) - 1)]

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

                    if not self.Map_mountains[y2][x2]:
                        
                        self.Map_mountains[y2][x2] = M[y][x]
                        
                        block = Block(self, x2,y2)
                        
                        self.block_group.add(block)
                        
                        self.all_object_group.add(block)

        # Tree and obstacle random placment

        for x in range(len(self.Map_trees[0])):

            for y in range(len(self.Map_trees)):

                x_mn, y_mn = x - 1, y - 1
                
                x_mx, y_mx = x + 1, y + 1
                
                if x_mn < 0:
                    
                    x_mn += len(self.Map_mountains[0])
                    
                if x_mx >= len(self.Map_mountains[0]):
                    
                    x_mx -= len(self.Map_mountains[0])
                    
                if y_mn < 0:
                    
                    y_mn += len(self.Map_mountains)
                    
                if y_mx >= len(self.Map_mountains):
                    
                    y_mx -= len(self.Map_mountains)

                if not self.Map_mountains[y][x] or (self.Map_mountains[y_mx][x] > 0 and self.Map_mountains[y_mn][x] > 0 and self.Map_mountains[y][x_mx] > 0 and self.Map_mountains[y][x_mn] > 0):

                    if random.random() < 0.01:

                        self.Map_trees[y][x] = Tree(self, x, y)

                        self.Trees.append((x, y))

                        self.tree_group.add(self.Map_trees[y][x])

                        self.all_object_group.add(self.Map_trees[y][x])

                        continue

                    if random.random() < 0.01:

                        obstacle = Obstacle(self,x,y)

                        self.obstacle_group.add(obstacle)

                        self.all_object_group.add(obstacle)

                        continue

                    #self.Trees.append((x, y))

        # set frame block

        for block in self.block_group:

            block.update_block()

        # Grass random placment

        for x in range(len(self.Map_grass[0])):

            for y in range(len(self.Map_grass)):

                grass = Grass(self, x, y)

                if not pygame.sprite.spritecollideany(grass,self.all_object_group):
                    
                    if random.random() < 0.1:
                        
                        self.Map_grass[y][x] = grass
                        
                        self.Grass.append((x, y))
                        
                        self.grass_group.add(self.Map_grass[y][x])

        # Générer des agents
        for i in range(10):
            sheep = Agent.Sheep(self, (
                random.randint(0, self.screenWidth // self.size_tile_X) * self.size_tile_X,
                random.randint(0, self.screenHeight // self.size_tile_Y) * self.size_tile_Y))
            collide = pygame.sprite.spritecollideany(sheep,self.all_object_group)
            if collide:
                sheep.kill()
                i-=1
                continue
            self.sheep_group.add(sheep)
        for i in range(5):
            wolf = Agent.Wolf(self, (
                random.randint(0, self.screenWidth // self.size_tile_X) * self.size_tile_X,
                random.randint(0, self.screenHeight // self.size_tile_Y) * self.size_tile_Y))
            collide = pygame.sprite.spritecollideany(wolf, self.all_object_group)
            if collide:
                wolf.kill()
                i -= 1
                continue
            self.wolf_group.add(wolf)

        
        #générer nuages

        for _ in range(15):
            cloud = Cloud(self)
            self.cloud_group.add(cloud)

    

    def update_object(self):

        
        
        # BLOCK

        for block in self.block_group:

            block.set_frame()
        
        self.block_group.draw(self.screen)

        # TREE

        if not self.Tmp1:

            self.Tmp1 = self.Trees.copy()

        i = random.randint(0, len(self.Tmp1) - 1)

        x, y = self.Tmp1[i]

        if self.Map_trees[y][x] == None:

            if random.random() < 0.001: #probabilté qu'un arbre repousse (change par rapport à la saison et température)

                self.Map_trees[y][x] = Tree(self, x, y)

                self.tree_group.add(self.Map_trees[y][x])

                self.all_object_group.add(self.Map_trees[y][x])

                self.Map_trees[y][x].update_tree()
        else:

            self.Map_trees[y][x].update_tree()

        self.tree_group.update()

        self.tree_group.draw(self.screen)

        del self.Tmp1[i]

        # FIRE

        self.fire_group.update()

        self.fire_group.draw(self.screen)

        # GRASS

        if not self.Tmp2:

            self.Tmp2 = self.Grass.copy()

        i = random.randint(0, len(self.Tmp2) - 1)

        x, y = self.Tmp2[i]

        if self.Map_grass[y][x] == None:

            if random.random() < 0.004: #probabilté que de l'herbe repousse (change par rapport à la saison et température)

                self.Map_grass[y][x] = Grass(self, x, y)

                self.grass_group.add(self.Map_grass[y][x])

                self.Map_grass[y][x].update_grass()

        else:
            
            self.Map_grass[y][x].update_grass()

        self.grass_group.update()

        self.grass_group.draw(self.screen)

        del self.Tmp2[i]

        # agents
        self.wolf_group.update()
        self.sheep_group.update()
        self.wolf_group.draw(self.screen)
        self.sheep_group.draw(self.screen)

        # OBSTACLE

        self.obstacle_group.draw(self.screen)

        # Weather

        self.weather.update_weather()

        # CLOUD

        for cloud in self.cloud_group:

            cloud.update()

        self.cloud_group.update()

        self.cloud_group.draw(self.screen)


    def update_world(self):
        """
        lecture événementielles du jeux

        """

        # lecture des événements Pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                self.destroy()
 
        for x in range(self.screenWidth // self.size_bg_X + 1):

            for y in range(self.screenHeight // self.size_bg_Y + 1):
                
                self.screen.blit(self.Environment_images[0][self.weather.get_season()], (x * self.size_bg_X, y * self.size_bg_Y))

        self.update_object()

        pygame.display.update()

    def destroy(self):
        """
        destructeur de la classe
        """
        print('Exit')
        pygame.quit()  # ferme la fenêtre principale
        exit()


if __name__ == "__main__":
    world = World()
    clock = pygame.time.Clock()
    while True:
        try:
            world.update_world()
        except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy().
            world.destroy()
        clock.tick(30)
