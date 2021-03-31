
import pygame

class Image:

    def __init__(self,world):

        self.world = world


    def load_image(self, filename, tile_size_X, tile_size_Y):

        image = pygame.image.load(filename).convert_alpha()

        image = pygame.transform.scale(
            image, (int(tile_size_X), int(tile_size_Y))
        )

        return image

    def load_all_image(self):

        self.world.Environment_images = [
            [
                self.load_image("PNG/background/summer.png", self.world.size_bg_X, self.world.size_bg_Y),
                self.load_image("PNG/background/fall.png", self.world.size_bg_X, self.world.size_bg_Y),
                self.load_image("PNG/background/winter.png", self.world.size_bg_X, self.world.size_bg_Y),
                self.load_image("PNG/background/spring.png", self.world.size_bg_X, self.world.size_bg_Y), 
                self.load_image("PNG/background/night.png", self.world.size_bg_X, self.world.size_bg_Y),

            ],
            [
                self.load_image("PNG/split/tree1.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree2.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree3.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree4.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree5.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree6.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree7.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree8.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree9.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree10.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree11.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree12.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree13.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree14.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree15.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree16.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/tree17.png", self.world.size_tree_X, self.world.size_tree_Y),
            ],
            [
                self.load_image("PNG/split/grass_repousse.png", self.world.size_grass_X, self.world.size_grass_Y),
                self.load_image("PNG/split/grass.png", self.world.size_grass_X, self.world.size_grass_Y),

            ],
            [
                self.load_image("PNG/split/rock.png", self.world.size_obstacle_X, self.world.size_obstacle_Y),
            ],
            [
                self.load_image("PNG/split/cloud.png", 128, 128)
            ]

        ]

        self.world.Fire_images.append(
            [
                self.load_image("PNG/split/fire4.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/fire5.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/fire6.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/fire7.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/fire8.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/cendre3.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/cendre1.png", self.world.size_tree_X, self.world.size_tree_Y),
                self.load_image("PNG/split/cendre2.png", self.world.size_tree_X, self.world.size_tree_Y),
                
            ]

        )

        self.world.Block_images = [

            [
                self.load_image("PNG/Block/sand_inside.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_SW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_S.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_N.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_E.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_W.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_corner_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_corner_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_corner_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/sand_corner_SW.png", self.world.size_block_X, self.world.size_block_Y),
            ],
            [
                self.load_image("PNG/Block/orange_inside.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_SW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_S.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_N.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_E.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_W.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_corner_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_corner_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_corner_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/orange_corner_SW.png", self.world.size_block_X, self.world.size_block_Y),
            ],
            [
                self.load_image("PNG/Block/ice_inside.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_SW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_S.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_N.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_E.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_W.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_corner_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_corner_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_corner_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/ice_corner_SW.png", self.world.size_block_X, self.world.size_block_Y),
            ],
            [
                self.load_image("PNG/Block/green_inside.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_SW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_S.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_N.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_E.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_W.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_corner_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_corner_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_corner_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/green_corner_SW.png", self.world.size_block_X, self.world.size_block_Y),
            ],
            [
                self.load_image("PNG/Block/night_inside.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_SW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_S.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_N.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_E.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_W.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_corner_NE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_corner_NW.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_corner_SE.png", self.world.size_block_X, self.world.size_block_Y),
                self.load_image("PNG/Block/night_corner_SW.png", self.world.size_block_X, self.world.size_block_Y),
            ]
        ]

        # sheep_images[0] -> up
        # sheep_images[1] -> right
        # sheep_images[2] -> down
        # sheep_images[3] -> left
        self.world.sheep_images = [
            [
                self.load_image("PNG/Agent/sheep/sheep_back_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/sheep/sheep_back_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/sheep/sheep_back_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
            [
                self.load_image("PNG/Agent/sheep/sheep_right_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/sheep/sheep_right_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/sheep/sheep_right_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
            [
                self.load_image("PNG/Agent/sheep/sheep_front_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/sheep/sheep_front_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/sheep/sheep_front_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
            [
                self.load_image("PNG/Agent/sheep/sheep_left_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/sheep/sheep_left_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/Sheep/sheep_left_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
        ]

        # wolf_images[0] -> up
        # wolf_images[1] -> right
        # wolf_images[2] -> down
        # wolf_images[3] -> left
        self.world.wolf_images = [
            [
                self.load_image("PNG/Agent/wolf/wolf_back_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_back_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_back_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
            [
                self.load_image("PNG/Agent/wolf/wolf_right_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_right_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_right_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
            [
                self.load_image("PNG/Agent/wolf/wolf_front_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_front_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_front_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
            [
                self.load_image("PNG/Agent/wolf/wolf_left_1.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_left_2.png", self.world.size_tile_X, self.world.size_tile_Y),
                self.load_image("PNG/Agent/wolf/wolf_left_3.png", self.world.size_tile_X, self.world.size_tile_Y),
            ],
        ]

