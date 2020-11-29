from cell import Cell
from helpers import load_image
from settings import CELL_SIZE


class Ground(Cell):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.sprite = load_image('./sprites/concrete.png')

    def draw(self):
        self.sc.blit(self.sprite, (self.x, self.y, CELL_SIZE, CELL_SIZE))
