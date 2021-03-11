import random

import pygame  # PYGAME package


class BasicAgent(pygame.sprite.Sprite):
    def __init__(self, world, img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.world_size_x = self.world.size_factor_X * self.world.size_tile_X
        self.world_size_y = self.world.size_factor_Y * self.world.size_tile_Y
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 2
        self.frame = []
        self.current_frame = 0
        self.x = self.rect.x // self.world.size_tile_X
        self.y = self.rect.y // self.world.size_tile_Y
        self.direction = 3
        self.alive = True
        self.frame_change_counter = 0
        self.direction_change_counter = 0
        self.direction_change_time = 15
        self.input_direction = -1
        self.next_direction = -1
        self.it_non_mange = 0

    def set_frame(self, frame):
        self.frame = frame

    def reset_mange(self):
        self.it_non_mange = 0

    def set_direction(self, direction):
        self.input_direction = direction

    def calc_pos(self):
        self.x = self.rect.x // self.world.size_tile_X
        self.y = self.rect.y // self.world.size_tile_Y

    def move(self):
        self.frame_change_counter += 1
        if self.frame_change_counter > 3:
            self.current_frame += 1
            if self.current_frame > 2:
                self.current_frame = 0
            self.frame_change_counter = 0
            if self.input_direction != -1:
                self.next_direction = self.input_direction
                self.input_direction = -1
        self.image = self.frame[self.direction][self.current_frame]

        self.direction_change_counter += 1
        if self.direction_change_counter > self.direction_change_time:
            self.direction_change_counter = 0
            self.direction_change_time = random.randint(30,150)
            if self.next_direction == -1:
                if random.random() > 0.5:
                    self.next_direction = (self.direction + 1) % 4
                else:
                    self.next_direction = (self.direction - 1 + 4) % 4

        if self.next_direction != -1 and self.rect.top % self.world.size_tile_X == 0 and self.rect.left % self.world.size_tile_Y == 0:
            self.direction = self.next_direction
            self.next_direction = -1
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
        self.calc_pos()


class Sheep(BasicAgent):
    p_reproduce = 0.00
    delai_de_famine = 10

    def __init__(self, world, init_pos):
        super().__init__(world, world.sheep_images[0][0], init_pos)
        self.frame = world.sheep_images

    def update(self):
        super().update()
        pos = pygame.math.Vector2(self.x, self.y)
        min = 6
        cloest = None
        for wolf in self.world.wolf_group:
            distance = pos.distance_to(pygame.math.Vector2(wolf.x, wolf.y))
            if min > distance:
                min = distance
                cloest = wolf
        if cloest:
            x_distance = cloest.x - self.x
            y_distance = cloest.y - self.y
            if abs(x_distance) > abs(y_distance):
                if y_distance > 0:
                    self.set_direction(0)
                else:
                    self.set_direction(2)
            elif x_distance > 0:
                self.set_direction(3)
            else:
                self.set_direction(1)


class Wolf(BasicAgent):
    p_reproduce = 0.00
    delai_de_famine = 100

    def __init__(self, world, init_pos):
        super().__init__(world, world.wolf_images[0][0], init_pos)
        self.frame = world.wolf_images
        self.speed = 3
        self.iter = 0

    def update(self):
        super().update()
        pos = pygame.math.Vector2(self.x, self.y)
        self.iter += 1
        if self.iter > 10:
            self.it_non_mange += 1
            self.iter = 0
        min = 5
        cloest = None
        for sheep in self.world.sheep_group:
            if pygame.sprite.collide_rect(self, sheep):
                sheep.kill()
                self.reset_mange()
            distance = pos.distance_to(pygame.math.Vector2(sheep.x, sheep.y))
            if min > distance:
                min = distance
                cloest = sheep
        if cloest:
            x_distance = cloest.x - self.x
            y_distance = cloest.y - self.y
            if abs(x_distance) < abs(y_distance) :
                if y_distance > 0:
                    self.set_direction(2)
                if y_distance < 0:
                    self.set_direction(0)
            elif x_distance > 0:
                self.set_direction(1)
            elif x_distance < 0:
                self.set_direction(3)
        # list_collide = pygame.sprite.spritecollide(self, self.world.sheep_group, True)
        # if list_collide:
        #     self.reset_mange()
        if self.it_non_mange > Wolf.delai_de_famine:
            self.kill()
