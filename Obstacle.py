
import pygame  # PYGAME package


class Obstacle(pygame.sprite.Sprite):

    def __init__(self,world,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.x, self.y = x, y

        self.image = self.world.Environment_images[3][self.world.weather.season]

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * self.world.size_tree_X, self.y * self.world.size_tree_Y)

    def update(self):

        self.image = self.world.Environment_images[3][self.world.weather.season]