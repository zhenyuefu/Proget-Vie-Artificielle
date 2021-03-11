import pygame  # PYGAME package


class BasicAgent(pygame.sprite.Sprite): 
    def __init__(self, world, img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.world_size_x = self.world.size_factor_X * self.world.size_tile_X
        self.world_size_y = self.world.size_factor_Y * self.world.size_tile_Y
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 2
        self.frame = []
        self.current_frame = 0
        self.x = self.rect.x // self.world.size_tile_X
        self.y = self.rect.y // self.world.size_tile_Y
        self.direction = 3
        self.alive = True
        self.iter = 0
        self.it_non_mange = 0

    def set_frame(self, frame):
        self.frame = frame

    def move(self):
        self.iter += 1
        if self.iter > 3:
            self.current_frame += 1
            if self.current_frame > 2:
                self.current_frame = 0
            self.iter = 0
        self.image = self.frame[self.direction][self.current_frame]
        self.x = self.rect.x // self.world.size_tile_X
        self.y = self.rect.y // self.world.size_tile_Y
        # [0] -> up
        # [1] -> right
        # [2] -> down
        # [3] -> left
        if self.direction == 0:
            self.rect.y -= self.speed
            if self.rect.bottom < 0:
                self.rect.top = self.world_size_y
            return

        if self.direction == 1:
            self.rect.x += self.speed
            if self.rect.left > self.world_size_x:
                self.rect.right = 0
            return

        if self.direction == 2:
            self.rect.y += self.speed
            if self.rect.top > self.world_size_y:
                self.rect.bottom = 0
            return

        if self.direction == 3:
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.rect.left = self.world_size_x

    def update(self):
        self.move()


class Sheep(BasicAgent):
    p_reproduce = 0.00
    delai_de_famine = 10

    def __init__(self, world, img, init_pos):
        super().__init__(world, img, init_pos)
        self.frame = world.sheep_images


class Wolf(BasicAgent):
    p_reproduce = 0.00
    delai_de_famine = 10

    def __init__(self, world, img, init_pos):
        super().__init__(world, img, init_pos)
        self.frame = world.wolf_images
