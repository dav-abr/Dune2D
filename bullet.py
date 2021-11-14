import pygame as pg
import time
import sprites
import math
import window
from creature import Creature
from helpers import get_cell
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

from cell import Cell


class Bullet:
    def __init__(self, _type: str, speed: float, from_: Cell, target: iter, world_map):
        self.type = _type
        self.x = from_.x + window.cell_size / 2
        self.y = from_.y + window.cell_size / 2
        self.speed = speed
        self.from_ = from_
        self.target = tuple(map(lambda x: x * window.cell_size + window.cell_size / 2, target))
        self.world_map = world_map
        self.sc = world_map.bullets_sf
        self.__t1 = time.time()
        self.__tick = True
        self.sprite = sprites.sprites['creatures']['bullet']

        x_diff = self.target[0] - self.from_.x - window.cell_size / 2
        y_diff = self.target[1] - self.from_.y - window.cell_size / 2
        angle = math.atan2(y_diff, x_diff)
        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed
        print(self.target)

    def draw(self):
        if self.change_x >= 0:
            if self.x + self.change_x > self.target[0]:
                self.x = self.target[0]
            else:
                self.x += self.change_x
        else:
            if self.x + self.change_x < self.target[0]:
                self.x = self.target[0]
            else:
                self.x += self.change_x

        if self.change_y >= 0:
            if self.y + self.change_y > self.target[1]:
                self.y = self.target[1]
            else:
                self.y += self.change_y
        else:
            if self.y + self.change_y < self.target[1]:
                self.y = self.target[1]
            else:
                self.y += self.change_y

        # self.x += self.change_x
        # self.y += self.change_y

        i, j = get_cell(self.x, self.y)

        if 0 < self.x < WINDOW_WIDTH and 0 < self.y < WINDOW_HEIGHT:
            if isinstance(self.world_map.creatures[i][j], Creature) and self.world_map.creatures[i][j] != self.from_:
                self.world_map.creatures[i][j].hit()
                self.world_map.bullets.remove(self)

            if self.x == self.target[0] and self.y == self.target[1]:
                self.world_map.bullets.remove(self)
        else:
            self.world_map.bullets.remove(self)
        self.sc.blit(self.sprite, (self.x, self.y))
