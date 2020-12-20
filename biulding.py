import pygame as pg
from cell import Cell
from helpers import load_building_sprite


class Building(Cell):
    def __init__(self, i, j, sc, world_map, name):
        super().__init__(i, j, sc, world_map)
        self.name = name
        self.width = 2
        self.height = 2
        self.sprite = load_building_sprite('./houses/{0}.png'.format(self.name), self.width, self.height)
        self.hud_image = pg.image.load('./hud/{0}.png'.format(self.name))
        self.hp = 100
        self.max_hp = 100
        for w in range(self.width):
            for h in range(self.height):
                self.world_map.buildings[self.i + w][self.j + h] = self

    def draw(self):
        super().draw()
