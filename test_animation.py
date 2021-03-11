from sys import exit  # exit script

import pygame  # PYGAME package
from pygame.locals import *  # PYGAME constant & functions

import Agent


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
        self.sheep_images = []
        self.wolf_images = []
        self.load_all_image()
        self.agent = Agent.Sheep(self, self.sheep_images[0][0], (50, 50))
        self.agent2 = Agent.Sheep(self, self.sheep_images[0][0], (100, 50))
        self.agent2.direction = 1
        self.agent3 = Agent.Wolf(self, self.wolf_images[0][0],(100,100))
        self.agent3.direction = 0
        self.agent_group = pygame.sprite.Group()
        self.agent_group.add(self.agent)
        self.agent_group.add(self.agent2)
        self.agent_group.add(self.agent3)

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
                self.load_image("PNG/tree.png"),
                self.load_image("smokeOrange0.png"),
                self.load_image("PNG/wooded_tree.png"),
                self.load_image("PNG/big_tree.png"),
            ]
        )

        # 2 : obstacles
        self.Environment_images.append(
            [self.load_image("PNG/rock1.png"), self.load_image("PNG/rock2.png")]
        )

        # 3 : herbs
        self.Environment_images.append([self.load_image("grass.png")])

        # 4 : Mountains
        self.Environment_images.append(
            [
                self.load_image("PNG/green_inside.png"),
                self.load_image("PNG/green_SW.png"),
                self.load_image("PNG/green_NW.png"),
                self.load_image("PNG/green_SE.png"),
                self.load_image("PNG/green_NE.png"),
                self.load_image("PNG/green_S.png"),
                self.load_image("PNG/green_N.png"),
                self.load_image("PNG/green_E.png"),
                self.load_image("PNG/green_W.png"),
                self.load_image("PNG/green_corner_NE.png"),
                self.load_image("PNG/green_corner_NW.png"),
                self.load_image("PNG/green_corner_SE.png"),
                self.load_image("PNG/green_corner_SW.png"),
            ]
        )

        # sheep_images[0] -> up
        # sheep_images[1] -> right
        # sheep_images[2] -> down
        # sheep_images[3] -> left
        self.sheep_images = [
            [
                self.load_image("PNG/Agent/sheep/sheep_back_1.png"),
                self.load_image("PNG/Agent/sheep/sheep_back_2.png"),
                self.load_image("PNG/Agent/sheep/sheep_back_3.png"),
            ],
            [
                self.load_image("PNG/Agent/sheep/sheep_right_1.png"),
                self.load_image("PNG/Agent/sheep/sheep_right_2.png"),
                self.load_image("PNG/Agent/sheep/sheep_right_3.png"),
            ],
            [
                self.load_image("PNG/Agent/sheep/sheep_front_1.png"),
                self.load_image("PNG/Agent/sheep/sheep_front_2.png"),
                self.load_image("PNG/Agent/sheep/sheep_front_3.png"),
            ],
            [
                self.load_image("PNG/Agent/sheep/sheep_left_1.png"),
                self.load_image("PNG/Agent/sheep/sheep_left_2.png"),
                self.load_image("PNG/Agent/Sheep/sheep_left_3.png"),
            ],
        ]

        # wolf_images[0] -> up
        # wolf_images[1] -> right
        # wolf_images[2] -> down
        # wolf_images[3] -> left
        self.wolf_images = [
            [
                self.load_image("PNG/Agent/wolf/wolf_back_1.png"),
                self.load_image("PNG/Agent/wolf/wolf_back_2.png"),
                self.load_image("PNG/Agent/wolf/wolf_back_3.png"),
            ],
            [
                self.load_image("PNG/Agent/wolf/wolf_right_1.png"),
                self.load_image("PNG/Agent/wolf/wolf_right_2.png"),
                self.load_image("PNG/Agent/wolf/wolf_right_3.png"),
            ],
            [
                self.load_image("PNG/Agent/wolf/wolf_front_1.png"),
                self.load_image("PNG/Agent/wolf/wolf_front_2.png"),
                self.load_image("PNG/Agent/wolf/wolf_front_3.png"),
            ],
            [
                self.load_image("PNG/Agent/wolf/wolf_left_1.png"),
                self.load_image("PNG/Agent/wolf/wolf_left_2.png"),
                self.load_image("PNG/Agent/wolf/wolf_left_3.png"),
            ],
        ]

    def update_world(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        # self.forestFire()

        # lecture des événements Pygame
        for event in pygame.event.get():
            if event.type == QUIT:  # évènement click sur fermeture de fenêtre
                self.destroy()  # dans ce cas on appelle le destructeur de la classe
        for x in range(0, self.size_factor_X):
            # for y in range(0, int(self.size_Y*self.scaleMultiplier*self.size_factor_Y),
            # int(self.size_Y*self.scaleMultiplier)):
            for y in range(0, self.size_factor_Y):
                self.screen.blit(
                    self.Environment_images[0][0],
                    (x * self.size_tile_X, y * self.size_tile_Y),
                )  # tuile "background" en position (x,y)

        self.agent_group.update()
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
    while True:
        try:
            world.update_world()
        except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy().
            world.destroy()
        clock.tick(30)
