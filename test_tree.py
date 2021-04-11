from sys import exit  # exit script

import pygame  # PYGAME package
from pygame.locals import *  # PYGAME constant & functions
import random

import Agent
import Plant
import Obstacle
import Block
from Image import *
import Weather
import Cloud


class World:
    """
    classe principale du jeux
    """

    def __init__(self, screenWidth=1476, screenHeight=1088):
        """
        constructeur de la classe
        """

        # Taille fenêtre

        self.screenWidth, self.screenHeight = screenWidth, screenHeight

        # Initialisation de la taille des tuiles

        self.size_tile_X, self.size_tile_Y = 32, 32

        self.size_tree_X, self.size_tree_Y = 36, 32

        self.size_bg_X, self.size_bg_Y = self.size_tree_X, self.size_tree_Y

        self.size_cloud_X, self.size_cloud_Y = 128, 128

        self.size_grass_X, self.size_grass_Y = (
            self.size_tree_X // 2,
            self.size_tree_Y // 2,
        )

        self.size_obstacle_X, self.size_obstacle_Y = self.size_tree_X, self.size_tree_Y

        self.size_trunk_X, self.size_trunk_Y = 36, 22

        self.size_block_X, self.size_block_Y = self.size_tree_X, self.size_tree_Y

        # Création des Maps

        self.Map_trees = [
            x[:]
            for x in [[None] * (self.screenWidth // self.size_tree_X)]
            * (self.screenHeight // self.size_tree_Y)
        ]

        self.Map_grass = [
            x[:]
            for x in [[None] * (self.screenWidth // self.size_grass_X)]
            * (self.screenHeight // self.size_grass_Y)
        ]

        self.Map_mountains = [
            x[:]
            for x in [[0] * (self.screenWidth // self.size_block_X)]
            * (self.screenHeight // self.size_block_Y)
        ]

        self.Map_lake = [
            x[:]
            for x in [[0] * (self.screenWidth // self.size_block_X)]
            * (self.screenHeight // self.size_block_Y)
        ]

        # Carte d'altitude (placement des points d'eau)

        self.altitude = []

        for i in range(self.screenHeight // self.size_block_Y):
            m=[]
            for j in range(self.screenWidth // self.size_block_X):
                m.append(random.randint(0,2000))
            
            self.altitude.append(m)

        pygame.init()

        self.screen = pygame.display.set_mode(
            (
                int(self.screenWidth),
                int(self.screenHeight),
            ),
            DOUBLEBUF,
        )
        pygame.display.set_caption("WORLD TEST")

        # Météo

        self.weather = Weather.Weather()

        # Frame

        self.Environment_images = []
        self.sheep_images = []
        self.wolf_images = []
        self.Block_images = []
        self.Lake_images = []
        self.Fire_images = []

        # Initialisation des tuiles

        self.image = Image(self)
        self.image.load_all_image()

        # Position de chaque sprite (arbre et herbe)

        #self.BlockType = []

        self.Trees = []
        self.Grass = []

        # Liste temporaire

        self.Tmp1 = [] # ---> Tree
        self.Tmp2 = [] # ---> Grass

        # Group Lists

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

    # def create_block(self):

    #     for _ in range(3):
    #         longueur, largeur = random.randint(8, 10), random.randint(8, 10)

    #         self.BlockType.append([x[:] for x in [[1] * largeur] * longueur])

    # Mountains random placement

    def object_placment(self):

        # self.create_block()

        # i = 0

        # for _ in range(6):

        #     x_offset, y_offset = (
        #         random.randint(0, len(self.Map_mountains[0]) - 1),
        #         random.randint(0, len(self.Map_mountains) - 1),
        #     )

        #     M = self.BlockType[random.randint(0, len(self.BlockType) - 1)]

        #     for x in range(len(M[0])):

        #         for y in range(len(M)):

        #             x2, y2 = x + x_offset, y + y_offset

        #             if x2 < 0:
        #                 x2 += len(self.Map_mountains[0])

        #             if x2 >= len(self.Map_mountains[0]):
        #                 x2 -= len(self.Map_mountains[0])

        #             if y2 < 0:
        #                 y2 += len(self.Map_mountains)

        #             if y2 >= len(self.Map_mountains):
        #                 y2 -= len(self.Map_mountains)

        #             if not self.Map_mountains[y2][x2] and not self.Map_lake[y2][x2]:
                        
        #                 if i%2==0:
                            
        #                     self.Map_mountains[y2][x2] = M[y][x]
                            
        #                     block = Block.Mountain(self, x2, y2)
                            
        #                     self.block_group.add(block)
                            
        #                     self.all_object_group.add(block)
                            
        #                 else:
                            
        #                     self.Map_lake[y2][x2] = M[y][x]
                            
        #                     block = Block.Lake(self, x2, y2)
                            
        #                     self.block_group.add(block)

        #                     self.all_object_group.add(block)
                            
                            
        #     i += 1

        n = 20

        for x in range(len(self.altitude[0])):
            for y in range(len(self.altitude)):

                if self.altitude[y][x] <= n and not self.Map_lake[y][x]:

                    for x2 in range(x-2,x+3):
                        for y2 in range(y-2,y+3):
                            
                            x3, y3 = x2, y2
                            
                            if x3 < 0:
                                x3+= len(self.altitude[0])
                                
                            if x3 >= len(self.altitude[0]):
                                x3 -= len(self.altitude[0])
                                
                            if y3< 0:
                                y3 += len(self.altitude)
                                
                            if y3 >= len(self.altitude):
                                y3 -= len(self.altitude)
                                
                            if not self.Map_lake[y3][x3]:
                                
                                self.Map_lake[y3][x3]=1


        for x in range(len(self.Map_lake[0])):
            for y in range(len(self.Map_lake)):

                if self.Map_lake[y][x]:
                    x_mn, y_mn = x - 1, y - 1
                    x_mx, y_mx = x + 1, y + 1

                    if x_mn < 0:
                        x_mn += len(self.Map_lake[0])
                    
                    if x_mx >= len(self.Map_lake[0]):
                        x_mx -= len(self.Map_lake[0])
                        
                    if y_mn < 0:
                        y_mn += len(self.Map_lake)
                        
                    if y_mx >= len(self.Map_lake):
                        y_mx -= len(self.Map_lake)

                    if ((not self.Map_lake[y_mn][x_mn] and not self.Map_lake[y_mx][x_mx]) and (self.Map_lake[y_mx][x_mn] and self.Map_lake[y_mn][x_mx])) or ((self.Map_lake[y_mn][x_mn] and self.Map_lake[y_mx][x_mx]) and (not self.Map_lake[y_mx][x_mn] and not self.Map_lake[y_mn][x_mx])):
                        self.Map_lake[y][x]=0

                    else:
                        block = Block.Lake(self,x,y)
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

                if not self.Map_mountains[y][x] and not self.Map_lake[y][x] or (
                    self.Map_mountains[y_mx][x] > 0
                    and self.Map_mountains[y_mn][x] == self.Map_mountains[y_mx][x]
                    and self.Map_mountains[y][x_mx] == self.Map_mountains[y_mx][x]
                    and self.Map_mountains[y][x_mn] == self.Map_mountains[y_mx][x]
                ):

                    if random.random() < 0.03:
                        self.Map_trees[y][x] = Plant.Tree(self, x, y)
                        self.Trees.append((x, y))
                        self.tree_group.add(self.Map_trees[y][x])
                        self.all_object_group.add(self.Map_trees[y][x])
                        continue

                    if random.random() < 0.01:
                        if random.random() < 0.5:
                            obstacle = Obstacle.Rock(self, x, y)
                        else:
                            obstacle = Obstacle.Trunk(self, x, y)
                        self.obstacle_group.add(obstacle)
                        self.all_object_group.add(obstacle)
                        continue

                    # self.Trees.append((x, y))

        # Grass random placment

        for x in range(len(self.Map_grass[0])):
            for y in range(len(self.Map_grass)):
                grass = Plant.Grass(self, x, y)
                if not pygame.sprite.spritecollideany(grass, self.all_object_group):
                    if random.random() < 0.1:
                        self.Map_grass[y][x] = grass
                        self.Grass.append((x, y))
                        self.grass_group.add(self.Map_grass[y][x])

        # Générer des agents
        for i in range(1):
            sheep = Agent.Sheep(
                self,
                (
                    random.randint(0, self.screenWidth // self.size_tile_X)
                    * self.size_tile_X,
                    random.randint(0, self.screenHeight // self.size_tile_Y)
                    * self.size_tile_Y,
                ),
            )
            collide = pygame.sprite.spritecollideany(sheep, self.all_object_group)
            if collide:
                sheep.kill()
                i -= 1
                continue
            self.sheep_group.add(sheep)
        for i in range(1):
            wolf = Agent.Wolf(
                self,
                (
                    random.randint(0, self.screenWidth // self.size_tile_X)
                    * self.size_tile_X,
                    random.randint(0, self.screenHeight // self.size_tile_Y)
                    * self.size_tile_Y,
                ),
            )
            collide = pygame.sprite.spritecollideany(wolf, self.all_object_group)
            if collide:
                wolf.kill()
                i -= 1
                continue
            self.wolf_group.add(wolf)

        # générer nuages

        for _ in range(25):
            cloud = Cloud.Cloud(self)
            self.cloud_group.add(cloud)

    def update_object(self):

        # Weather

        self.weather.update_weather()

        if self.weather.delay == 1:
            print("p_fire=", Plant.P_FIRE)
            print("p_gen=", Plant.P_REPOUSSE)
            print("saison=", self.weather.season)

        # BLOCK
        
        if self.weather.delay == 1:
            self.block_group.update()
        
        self.block_group.draw(self.screen)

        # TREE

        if not self.Tmp1:
            self.Tmp1 = self.Trees.copy()

        else:
            i = random.randint(0, len(self.Tmp1) - 1)
            x, y = self.Tmp1[i]
            
            if self.Map_trees[y][x] == None:
                
                if (random.random() < Plant.P_REPOUSSE):  # probabilté qu'un arbre repousse (change par rapport à la saison et température)
                    
                    self.Map_trees[y][x] = Plant.Tree(self, x, y)
                    self.tree_group.add(self.Map_trees[y][x])
                    self.all_object_group.add(self.Map_trees[y][x])
                    self.Map_trees[y][x].update()
            else:
                self.Map_trees[y][x].update()

            del self.Tmp1[i]

        self.tree_group.draw(self.screen)


        # GRASS

        if not self.Tmp2:
            self.Tmp2 = self.Grass.copy()
        else:
            i = random.randint(0, len(self.Tmp2) - 1)
            x, y = self.Tmp2[i]
            
            if self.Map_grass[y][x] == None:
                
                if (
                    random.random() < Plant.P_REPOUSSE
                    ):  # probabilté que de l'herbe repousse (change par rapport à la saison et température)
                    
                    self.Map_grass[y][x] = Plant.Grass(self, x, y)
                    self.grass_group.add(self.Map_grass[y][x])
                    self.Map_grass[y][x].update()
                    
            else:
                self.Map_grass[y][x].update()

            del self.Tmp2[i]


        self.grass_group.draw(self.screen)

        # FIRE

        self.fire_group.draw(self.screen)

        # agents
        self.wolf_group.update()
        self.sheep_group.update()
        self.wolf_group.draw(self.screen)
        self.sheep_group.draw(self.screen)

        # OBSTACLE

        if self.weather.delay == 1:
            self.obstacle_group.update()

        self.obstacle_group.draw(self.screen)

        # CLOUD

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
                self.screen.blit(
                    self.Environment_images[0][self.weather.get_season()],
                    (x * self.size_bg_X, y * self.size_bg_Y),
                )

        self.update_object()

        pygame.display.update()

    def destroy(self):
        """
        destructeur de la classe
        """
        print("Exit")
        pygame.quit()  # ferme la fenêtre principale
        exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.destroy()


if __name__ == "__main__":
    world = World()
    clock = pygame.time.Clock()
    while True:
        world.events()
        try:
            world.update_world()
        except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy().
            world.destroy()
        clock.tick(30)
