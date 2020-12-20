import pygame as pg
import math
from creature import Creature
from settings import *
from helpers import load_sprite
import window


class Tank(Creature):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.sprites = {
            'straight_up': load_sprite('./sprites/moto_straight_up.png'),
            'straight_right': load_sprite('./sprites/moto_straight_right.png'),
            'straight_down': load_sprite('./sprites/moto_straight_down.png'),
            'straight_left': load_sprite('./sprites/moto_straight_left.png'),
            'diagonal_up_right': load_sprite('./sprites/moto_diagonal_up_right.png'),
            'diagonal_down_right': load_sprite('./sprites/moto_diagonal_down_right.png'),
            'diagonal_down_left': load_sprite('./sprites/moto_diagonal_down_left.png'),
            'diagonal_up_left': load_sprite('./sprites/moto_diagonal_up_left.png'),
            'horizontal_left_down': load_sprite('./sprites/moto_angle_horizontal_left_down.png'),
            'horizontal_right_down': load_sprite('./sprites/moto_angle_horizontal_right_down.png'),
            'horizontal_left_up': load_sprite('./sprites/moto_angle_horizontal_left_up.png'),
            'horizontal_right_up': load_sprite('./sprites/moto_angle_horizontal_right_up.png'),
            'vertical_down_left': load_sprite('./sprites/moto_angle_vertical_down_left.png'),
            'vertical_down_right': load_sprite('./sprites/moto_angle_vertical_down_right.png'),
            'vertical_up_right': load_sprite('./sprites/moto_angle_vertical_up_right.png'),
            'vertical_up_left': load_sprite('./sprites/moto_angle_vertical_up_left.png'),
        }
        self.sprite = self.sprites['straight_left']
        self.hud_image = pg.image.load('./hud/moto.png')

        self.hp = 10
        self.max_hp = 100

    def draw(self):
        super().draw()

        if self.direction == 0:
            self.sprite = self.sprites['straight_up']
        if self.direction == 90:
            self.sprite = self.sprites['straight_left']
        if self.direction == 180:
            self.sprite = self.sprites['straight_down']
        if self.direction == 270:
            self.sprite = self.sprites['straight_right']

        if self.direction == 45:
            self.sprite = self.sprites['diagonal_up_left']
        if self.direction == 135:
            self.sprite = self.sprites['diagonal_down_left']
        if self.direction == 225:
            self.sprite = self.sprites['diagonal_down_right']
        if self.direction == 315:
            self.sprite = self.sprites['diagonal_up_right']

        if self.direction == 22.5:
            self.sprite = self.sprites['vertical_up_left']
        if self.direction == 157.5:
            self.sprite = self.sprites['vertical_down_left']
        if self.direction == 202.5:
            self.sprite = self.sprites['vertical_down_right']
        if self.direction == 337.5:
            self.sprite = self.sprites['vertical_up_right']

        if self.direction == 67.5:
            self.sprite = self.sprites['horizontal_left_down']
        if self.direction == 112.5:
            self.sprite = self.sprites['horizontal_left_up']
        if self.direction == 247.5:
            self.sprite = self.sprites['horizontal_right_up']
        if self.direction == 292.5:
            self.sprite = self.sprites['horizontal_right_down']
