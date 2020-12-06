import pygame as pg
from settings import *
from cell import Cell
from ground import Ground
import window


def create_cell(col, row, sc, map):
    return Cell(col, row, sc, map)# if random() > 0.5 else Wall(col, row, sc, map)


def create_ground(col, row, sc, map):
    return Ground(col, row, sc, map)# if random() > 0.5 else Wall(col, row, sc, map)


class Map:
    def __init__(self, sc, ground=[], creatures=[]):
        self.sc = sc
        self.creatures = creatures

        if len(ground) > 0:
            self.ground = ground
        else:
            self.ground = [[create_ground(col, row, sc, self) for row in range(ROWS)] for col in range(COLS)]

        if len(creatures) > 0:
            self.creatures = creatures
        else:
            self.creatures = [[Cell(col, row, sc, self) for row in range(ROWS)] for col in range(COLS)]

    # def drawGrid(self):
    #     for x in range(COLS):
    #         for y in range(ROWS):
    #             rect = pg.Rect(x * window.cell_size, y * window.cell_size, window.cell_size, window.cell_size)
    #             pg.draw.rect(self.sc, pg.Color('white'), rect, 1)

    def draw(self):
        self.sc.fill((166, 130, 66))
