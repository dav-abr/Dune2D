import pygame as pg
from settings import *
from cell import Cell


class Wall(Cell):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.wall = True

    def draw(self):
        pg.draw.rect(self.sc, pg.Color('blue'),
                     pg.Rect(self.i * window.cell_size, self.j * window.cell_size, window.cell_size, window.cell_size))
