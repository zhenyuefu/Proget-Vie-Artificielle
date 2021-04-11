import pygame

class Fire(pygame.sprite.Sprite):

    def __init__(self,x,y,img,f_x,f_y):

        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.f_x, self.f_y = f_x, f_y
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * self.f_x, self.y * self.f_y)


    def set_frame(self,img):
        
        self.image = img