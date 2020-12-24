import pygame as pg
from cell import Cell
import sprites


class Building(Cell):
    def __init__(self, i, j, world_map, name):
        super().__init__(i, j, world_map)
        self.name = name
        self.sc = world_map.buildings_sf
        self.width = 2
        self.height = 2
        self.sprite = sprites.sprites['buildings'][self.name]
        self.hud_image = pg.image.load('./hud/{0}.png'.format(self.name))
        self.hp = 100
        self.max_hp = 100
        for w in range(self.width):
            for h in range(self.height):
                self.world_map.buildings[self.i + w][self.j + h] = self
        self.update_neighbors()
        self.world_map.update_buildings_sf()

    def draw(self):
        super().draw()
