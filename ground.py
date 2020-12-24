import pygame as pg
from cell import Cell
from helpers import load_sprite
import sprites


class Ground(Cell):
    def __init__(self, i, j, world_map):
        super().__init__(i, j, world_map)
        self.sc = world_map.ground_sf
        self.sprite = sprites.sprites['ground']['concrete']
        # self.font = pg.font.SysFont('Comic Sans MS', 15)

    def draw(self):
        super().draw()
