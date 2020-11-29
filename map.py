import pygame as pg
from settings import *
from cell import Cell
from wall import Wall
from random import random


def create_cell(col, row, sc, map):
    return Cell(col, row, sc, map)# if random() > 0.5 else Wall(col, row, sc, map)


class Map:
    def __init__(self, cell_size, sc, grid=[]):
        self.cell_size = cell_size
        self.sc = sc

        if grid:
            self.grid = grid
        else:
            self.grid = [[create_cell(col, row, sc, self) for row in range(ROWS)] for col in range(COLS)]

    def get_circle(self, x, y):
        return (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2), self.cell_size // 4

    def drawGrid(self):
        for x in range(WINDOW_WIDTH // CELL_SIZE):
            for y in range(WINDOW_HEIGHT // CELL_SIZE):
                rect = pg.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pg.draw.rect(self.sc, pg.Color('white'), rect, 1)

    def draw(self):
        self.sc.fill(pg.Color('black'))

        self.drawGrid()
