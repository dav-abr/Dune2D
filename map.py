import pygame as pg
from settings import *
from cell import Cell
from ground import Ground


def create_cell(col, row, sc, map):
    return Cell(col, row, sc, map)# if random() > 0.5 else Wall(col, row, sc, map)


def create_ground(col, row, sc, map):
    return Ground(col, row, sc, map)# if random() > 0.5 else Wall(col, row, sc, map)


class Map:
    def __init__(self, cell_size, sc, ground=[], creatures=[]):
        self.cell_size = cell_size
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

    def drawGrid(self):
        for x in range(COLS):
            for y in range(ROWS):
                rect = pg.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pg.draw.rect(self.sc, pg.Color('white'), rect, 1)

    def draw(self):
        self.sc.fill((166, 130, 66))
