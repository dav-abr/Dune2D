import pygame as pg
import math
from creature import Creature
from settings import *


class Tank(Creature):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.tank = True

    def draw(self):
        super().draw()
        pg.draw.rect(self.sc, pg.Color('green' if self.target else 'red'), pg.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))
        pg.draw.rect(
            self.sc,
            pg.Color('black'),
            pg.Rect(
                self.x + CELL_SIZE // 4 + CELL_SIZE // 4 * math.sin(math.radians(self.direction)),
                self.y + CELL_SIZE // 4 + CELL_SIZE // 4 * math.cos(math.radians(self.direction)),
                CELL_SIZE // 2,
                CELL_SIZE // 2
            )
        )
        font = pg.font.SysFont(None, 24)
        img = font.render('{0} {1}'.format(self.i, self.j), True, pg.Color('white'))
        self.sc.blit(img, (self.x, self.y))
