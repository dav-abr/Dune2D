import pygame as pg
import math
from creature import Creature
from settings import *
from helpers import load_image

class Tank(Creature):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.tank = True
        self.sprites = {
            'straight_up': load_image('./sprites/moto_straight_up.png'),
            'straight_right': load_image('./sprites/moto_straight_right.png'),
            'straight_down': load_image('./sprites/moto_straight_down.png'),
            'straight_left': load_image('./sprites/moto_straight_left.png'),
            'diagonal_up_right': load_image('./sprites/moto_diagonal_up_right.png'),
            'diagonal_down_right': load_image('./sprites/moto_diagonal_down_right.png'),
            'diagonal_down_left': load_image('./sprites/moto_diagonal_down_left.png'),
            'diagonal_up_left': load_image('./sprites/moto_diagonal_up_left.png'),
            'horizontal_left_down': load_image('./sprites/moto_angle_horizontal_left_down.png'),
            'horizontal_right_down': load_image('./sprites/moto_angle_horizontal_right_down.png'),
            'horizontal_left_up': load_image('./sprites/moto_angle_horizontal_left_up.png'),
            'horizontal_right_up': load_image('./sprites/moto_angle_horizontal_right_up.png'),
            'vertical_down_left': load_image('./sprites/moto_angle_vertical_down_left.png'),
            'vertical_down_right': load_image('./sprites/moto_angle_vertical_down_right.png'),
            'vertical_up_right': load_image('./sprites/moto_angle_vertical_up_right.png'),
            'vertical_up_left': load_image('./sprites/moto_angle_vertical_up_left.png'),
        }
        self.last_sprite = self.sprites['straight_left']

    def draw(self):
        super().draw()
        # pg.draw.rect(self.sc, pg.Color('green' if self.target else 'red'), pg.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))
        # pg.draw.rect(
        #     self.sc,
        #     pg.Color('black'),
        #     pg.Rect(
        #         self.x + CELL_SIZE // 4 + CELL_SIZE // 4 * math.sin(math.radians(self.direction)),
        #         self.y + CELL_SIZE // 4 + CELL_SIZE // 4 * math.cos(math.radians(self.direction)),
        #         CELL_SIZE // 2,
        #         CELL_SIZE // 2
        #     )
        # )

        if self.direction == 0:
            self.last_sprite = self.sprites['straight_up']
        if self.direction == 90:
            self.last_sprite = self.sprites['straight_left']
        if self.direction == 180:
            self.last_sprite = self.sprites['straight_down']
        if self.direction == 270:
            self.last_sprite = self.sprites['straight_right']

        if self.direction == 45:
            self.last_sprite = self.sprites['diagonal_up_left']
        if self.direction == 135:
            self.last_sprite = self.sprites['diagonal_down_left']
        if self.direction == 225:
            self.last_sprite = self.sprites['diagonal_down_right']
        if self.direction == 315:
            self.last_sprite = self.sprites['diagonal_up_right']

        if self.direction == 22.5:
            self.last_sprite = self.sprites['vertical_up_left']
        if self.direction == 157.5:
            self.last_sprite = self.sprites['vertical_down_left']
        if self.direction == 202.5:
            self.last_sprite = self.sprites['vertical_down_right']
        if self.direction == 337.5:
            self.last_sprite = self.sprites['vertical_up_right']

        if self.direction == 67.5:
            self.last_sprite = self.sprites['horizontal_left_down']
        if self.direction == 112.5:
            self.last_sprite = self.sprites['horizontal_left_up']
        if self.direction == 247.5:
            self.last_sprite = self.sprites['horizontal_right_up']
        if self.direction == 292.5:
            self.last_sprite = self.sprites['horizontal_right_down']

        # if self.direction in (67.5, 157.5, 247.5, 337.5):
        #     self.last_sprite = pg.transform.rotate(self.sprites['angle_left'], self.direction - 22.5)
        #     self.last_position = 'angle_left'

        # new_rect = self.last_sprite.get_rect(center=(self.x + CELL_SIZE // 2, self.y + CELL_SIZE // 2))

        self.sc.blit(self.last_sprite, (self.x, self.y, CELL_SIZE, CELL_SIZE))
        # (new_rect[0] - 20, new_rect[1] - 20)
