
import pygame  # PYGAME package


class Obstacle(pygame.sprite.Sprite):

    def __init__(self,world,x,y,img,f_x,f_y):

        pygame.sprite.Sprite.__init__(self)

        self.world = world

        self.x, self.y = x, y

        self.frame = []

        self.image = img

        self.rect = self.image.get_rect()

        self.factor_x, self.factor_y = f_x, f_y

        self.rect.topleft = (self.x * self.factor_x, self.y * self.factor_y)

    def update(self):

        self.image = self.frame[self.world.weather.season]

class Rock(Obstacle):

    def __init__(self,world,x,y):
        super().__init__(world,x,y,world.Environment_images[3][world.weather.season],world.size_obstacle_X,world.size_obstacle_Y)
        self.frame=world.Environment_images[3]

    def update(self):
        super().update()

class Trunk(Obstacle):

    def __init__(self,world,x,y):
        super().__init__(world,x,y,world.Environment_images[4][world.weather.season],world.size_trunk_X,world.size_trunk_Y)
        self.frame=world.Environment_images[4]

    def update(self):
        super().update()