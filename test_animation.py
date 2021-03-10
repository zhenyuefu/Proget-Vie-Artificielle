from random import *
import pygame  # PYGAME package
from pygame.locals import *  # PYGAME constant & functions
from sys import exit  # exit script

class BasicAgent(pygame.sprite.Sprite):

    def __init__(self,img,init_pos,world):

        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.world = world
        self.speed_x = -5
        self.speed_y = 0
        self.frame = []
        self.current_frame = 0
    
    def set_frame(self,frame):

        self.frame = frame
    
    def move(self):

        self.current_frame+=1

        if self.current_frame > 2:
            self.current_frame = 0

        self.image = self.frame[self.current_frame]
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > world.size_factor_Y * world.size_tile_Y:

            self.rect.bottom = 0

        if self.rect.y < -(world.size_tile_Y):

            self.rect.top = (world.size_factor_Y * world.size_tile_Y) 

            #self.rect.bottom = (world.size_factor_Y * world.size_tile_Y) + world.size_tile_Y

        if self.rect.x > world.size_factor_X * world.size_tile_X:

            self.rect.left = -(world.size_factor_X)

        if self.rect.x < -(world.size_factor_X) :

            self.rect.right = (world.size_factor_X * world.size_tile_X) + world.size_tile_X

            #self.rect.left = (world.size_factor_X * world.size_tile_X)
        
        

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
        self.Agent_images = []
        self.loadAllImage()
        self.agent = BasicAgent(self.Agent_images[0][0],(randint(0,self.size_factor_X*size_tile_X),randint(0,self.size_tile_Y * self.size_factor_Y)),self)
        self.agent.set_frame([self.Agent_images[0][0],self.Agent_images[0][1],self.Agent_images[0][2]])
        self.agent_group = pygame.sprite.Group()
        self.agent_group.add(self.agent)
        
        

    def loadImage(self, filename):

        image = pygame.image.load(filename).convert_alpha()

        image = pygame.transform.scale(
            image, (int(self.size_tile_X), int(self.size_tile_Y))
        )

        return image

    def loadAllImage(self):

        # 0 : backgrounds
        self.Environment_images.append([self.loadImage("dirt.png")])

        # 1 : trees
        self.Environment_images.append(
            [
                self.loadImage("PNG/tree.png"),
                self.loadImage("smokeOrange0.png"),
                self.loadImage("PNG/wooded_tree.png"),
                self.loadImage("PNG/big_tree.png"),
            ]
        )

        # 2 : obstacles
        self.Environment_images.append(
            [self.loadImage("PNG/rock1.png"), self.loadImage("PNG/rock2.png")]
        )

        # 3 : herbs
        self.Environment_images.append([self.loadImage("grass.png")])

        # 4 : Mountains
        self.Environment_images.append(
            [
                self.loadImage("PNG/green_inside.png"),
                self.loadImage("PNG/green_SW.png"),
                self.loadImage("PNG/green_NW.png"),
                self.loadImage("PNG/green_SE.png"),
                self.loadImage("PNG/green_NE.png"),
                self.loadImage("PNG/green_S.png"),
                self.loadImage("PNG/green_N.png"),
                self.loadImage("PNG/green_E.png"),
                self.loadImage("PNG/green_W.png"),
                self.loadImage("PNG/green_corner_NE.png"),
                self.loadImage("PNG/green_corner_NW.png"),
                self.loadImage("PNG/green_corner_SE.png"),
                self.loadImage("PNG/green_corner_SW.png"),
            ]
        )

        # agents [0] : sheep
        self.Agent_images.append(
            [
                self.loadImage("PNG/Agent/sheep/sheep_front_1.png"),
                self.loadImage("PNG/Agent/sheep/sheep_front_2.png"),
                self.loadImage("PNG/Agent/sheep/sheep_front_3.png"),
            ]
        )

    def updateWorld(self):
        """
        boucle de lecture infinie événementielles du jeux

        """
        
       
        # self.forestFire()

        # lecture des événements Pygame
        for event in pygame.event.get():
            if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                self.destroy()  # dans ce cas on appelle le destructeur de la classe
        for x in range(0, self.size_factor_X):
            # for y in range(0, int(self.size_Y*self.scaleMultiplier*self.size_factor_Y), int(self.size_Y*self.scaleMultiplier)):
            for y in range(0, self.size_factor_Y):

                self.screen.blit(
                    self.Environment_images[0][0],
                    (x * self.size_tile_X, y * self.size_tile_Y),
                )  # tuile "background" en position (x,y)
        
        self.agent.move()
        self.agent_group.draw(self.screen)
        pygame.display.update()

    def destroy(self):
        """
        destructeur de la classe
        """
        print("Exit")
        pygame.quit()  # ferme la fenêtre principale
        exit()  # termine tous les process en cours


if __name__ == "__main__":
    world = World()
    clock = pygame.time.Clock()
    #a1 = BasicAgent(world.Agent_images[0][0],(1,1))
    while True:
        try:
            world.updateWorld()
        except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
            world.destroy()
        clock.tick(10)
