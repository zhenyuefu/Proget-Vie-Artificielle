import random
from abc import abstractmethod
from enum import Enum, auto

import pygame  # PYGAME package 


class AgentState(Enum):
    MOVE = auto()
    PAUSE = auto()


class BasicAgent(pygame.sprite.Sprite):
    def __init__(self, world, img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.world_size_x = self.world.screenWidth
        self.world_size_y = self.world.screenHeight
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.last_x = self.rect.x
        self.last_y = self.rect.y
        self.speed = 2
        self.frame = []
        self.current_frame = 0
        self.x = self.rect.x // self.world.size_tile_X
        self.y = self.rect.y // self.world.size_tile_Y
        self.direction = random.randint(0,3)
        self.alive = True
        self.frame_change_counter = 0
        self.direction_change_counter = 0
        self.direction_change_time = 15
        self.input_direction = -1
        self.next_direction = -1
        self.it_non_mange = 0
        self.state = AgentState.MOVE
        self.move_time = 0
        self.move_time_limit = random.randint(30, 70)
        self.obstacle_direction = -1

    def set_frame(self, frame):
        self.frame = frame

    def reset_mange(self):
        self.it_non_mange = 0

    def set_direction(self, direction):
        if direction != self.obstacle_direction:
            self.next_direction = direction

    def calc_pos(self):
        self.x = self.rect.x // self.world.size_tile_X
        self.y = self.rect.y // self.world.size_tile_Y

    def rand_direction(self,curr_direction):
        d = random.randint(0,3)
        while d == curr_direction:
            d = random.randint(0,3)
        return d

    def turn(self):
        print(self.rect.x)
        self.rect.x = self.last_x
        print(self.rect.x)
        self.rect.y = self.last_y
        self.obstacle_direction = self.direction
        self.direction = self.rand_direction(self.direction)

    def collide(self):
        obstacle = pygame.sprite.spritecollideany(self,self.world.all_object_group,pygame.sprite.collide_rect_ratio(0.7))
        if obstacle:
            self.turn()

    def move(self):
        self.move_time += 1
        if self.move_time >= self.move_time_limit and self.it_non_mange < 20:
            self.state = AgentState.PAUSE
            self.move_time = 0
        self.frame_change_counter += 1
        if self.frame_change_counter > 3:
            self.current_frame += 1
            if self.current_frame > 2:
                self.current_frame = 0
            self.frame_change_counter = 0
        self.image = self.frame[self.direction][self.current_frame]

        self.direction_change_counter += 1
        if self.direction_change_counter > self.direction_change_time:
            self.direction_change_counter = 0
            self.obstacle_direction = -1
            self.direction_change_time = random.randint(30, 150)
            if self.next_direction == -1:
                self.rand_direction(self.direction)

        if self.next_direction != -1:
            self.direction = self.next_direction
            self.next_direction = -1
        if self.direction == self.obstacle_direction:
            self.direction = self.rand_direction(self.direction)
        self.last_x = self.rect.x
        self.last_y = self.rect.y
        # [0] -> up
        # [1] -> right
        # [2] -> down
        # [3] -> left
        if self.direction == 0:
            self.rect.y -= self.speed
            self.collide()
            if self.rect.top < 0:
                self.rect.bottom = self.world_size_y
            return

        if self.direction == 1:
            self.rect.x += self.speed
            self.collide()
            if self.rect.right > self.world_size_x:
                self.rect.right = 0
            return

        if self.direction == 2:
            self.rect.y += self.speed
            self.collide()
            if self.rect.bottom > self.world_size_y:
                self.rect.top = 0
            return

        if self.direction == 3:
            self.rect.x -= self.speed
            self.collide()
            if self.rect.left < 0:
                self.rect.right = self.world_size_x

    @abstractmethod
    def reproduire(self):
        pass

    def pause(self):
        self.image = self.frame[2][0]
        if self.it_non_mange > 20:
            self.state = AgentState.MOVE

    def update(self):
        if self.state is AgentState.MOVE:
            self.move()
            self.reproduire()
        else:
            self.pause()
        self.calc_pos()


class Sheep(BasicAgent):
    p_reproduce = 0.0015
    delai_de_famine = 100

    def __init__(self, world, init_pos):
        super().__init__(world, world.sheep_images[0][0], init_pos)
        self.frame = world.sheep_images
        self.iter = 0

    def reproduire(self):
        if random.random() < Sheep.p_reproduce:
            agent = Sheep(self.world, self.rect.topleft)
            agent.add(self.world.sheep_group)

    def update(self):
        super().update()

        pos = pygame.math.Vector2(self.x, self.y)
        if self.iter > 3:
            self.it_non_mange += 1
            self.iter = 0
        min = 10
        closest = None
        for wolf in self.world.wolf_group:
            distance = pos.distance_to(pygame.math.Vector2(wolf.x, wolf.y))
            if min > distance:
                min = distance
                closest = wolf
        if closest:
            self.state= AgentState.MOVE
            x_distance = closest.x - self.x
            y_distance = closest.y - self.y
            if abs(x_distance) > abs(y_distance):
                if y_distance > 0:
                    self.set_direction(0)
                else:
                    self.set_direction(2)
            elif x_distance > 0:
                self.set_direction(3)
            else:
                self.set_direction(1)
        for grass in self.world.grass_mature_group:
            if pygame.sprite.collide_rect(self, grass):
                grass.kill()
                self.world.Map_grass[grass.y][grass.x] = None
                self.reset_mange()
        if self.it_non_mange > Sheep.delai_de_famine:
            self.kill()


class Wolf(BasicAgent):
    p_reproduce = 0.001
    delai_de_famine = 100

    def __init__(self, world, init_pos):
        super().__init__(world, world.wolf_images[0][0], init_pos)
        self.frame = world.wolf_images
        self.speed = 3
        self.iter = 0

    def reproduire(self):
        if random.random() < Wolf.p_reproduce:
            agent = Wolf(self.world, self.rect.topleft)
            agent.add(self.world.wolf_group)

    def update(self):
        super().update()
        pos = pygame.math.Vector2(self.x, self.y)
        self.iter += 1
        if self.iter > 10:
            self.it_non_mange += 1
            self.iter = 0
        min = 5
        closest = None
        for sheep in self.world.sheep_group:
            if pygame.sprite.collide_rect(self, sheep):
                sheep.kill()
                self.reset_mange()

            distance = pos.distance_to(pygame.math.Vector2(sheep.x, sheep.y))
            if min > distance:
                min = distance
                closest = sheep
        if closest:
            # self.state = AgentState.MOVE
            x_distance = closest.x - self.x
            y_distance = closest.y - self.y
            if abs(x_distance) < abs(y_distance):
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
