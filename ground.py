import pygame as pg
from cell import Cell
from helpers import load_sprite
from settings import CELL_SIZE


class Ground(Cell):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.sprite = load_sprite('./sprites/concrete.png')
        self.font = pg.font.SysFont('Comic Sans MS', 15)


    def draw(self):
        self.sc.blit(self.sprite, (self.x, self.y, CELL_SIZE, CELL_SIZE))
        # for neighbor in self.neighbors:
        #     textsurface = self.font.render(type(neighbor[1]).__name__, False, (0, 0, 0))
        #     self.sc.blit(
        #         textsurface,
        #         (
        #             self.x + CELL_SIZE // 2 + (neighbor[1].i * CELL_SIZE - self.x) // 3 - 15,
        #             self.y + CELL_SIZE // 2 + (neighbor[1].j * CELL_SIZE - self.y) // 3 - 10,
        #         )
        #     )
