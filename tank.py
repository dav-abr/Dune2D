import pygame as pg

from bullet import Bullet
from creature import Creature
import sprites
import math

from helpers import closest
from settings import ANGLES


class Tank(Creature):
    def __init__(self, i, j, world_map):
        super().__init__(i, j, world_map)
        self.sprites = sprites.sprites['creatures']['tank']
        self.sprite = self.sprites['straight_left']
        self.hud_image = pg.image.load('./hud/moto.png')

        self.hp = 100
        self.max_hp = 100

    def shoot(self, target):
        deltaX = target[0] - self.i
        deltaY = target[1] - self.j
        angle = math.degrees(-math.atan2(deltaY, deltaX)) - 90
        if angle < 0:
            angle += 360

        self.rotate_to_angle = closest(angle, ANGLES)
        self.world_map.bullets.append(Bullet('', 10, self, target, self.world_map))

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
