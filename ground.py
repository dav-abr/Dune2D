import pygame as pg
from cell import Cell
from helpers import load_sprite


class Ground(Cell):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.sprite = load_sprite('./sprites/concrete.png')
        # self.font = pg.font.SysFont('Comic Sans MS', 15)

    def draw(self):
        super().draw()
