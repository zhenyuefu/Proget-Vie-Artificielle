import pygame

class Fire(pygame.sprite.Sprite):

    def __init__(self,tree,x,y,img):

        pygame.sprite.Sprite.__init__(self)

        self.tree = tree

        self.x, self.y = x, y

        self.image = img

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x * self.tree.world.size_tree_X, self.y * self.tree.world.size_tree_Y)


    def set_frame(self,img):

        self.image = img