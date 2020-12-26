import pygame as pg
from cell import Cell
import sprites
import window


class Building(Cell):
    indicator_angle = 0

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

    @staticmethod
    def draw2():
        Building.indicator_angle = (Building.indicator_angle + 5) % 360

    def draw(self):
        super().draw()

        if Building.indicator_angle in (0, 45, 90, 135, 180, 225, 270, 315):
            sprite = sprites.sprites['buildings']['building_indicator_{0}'.format(Building.indicator_angle)]
            position = (self.x + window.cell_size / 30, self.y + (self.height - 1) * window.cell_size + int(window.cell_size / 2) + window.cell_size / 30)
            pg.draw.rect(self.sc, pg.Color(0, 0, 0, 0), (*position, sprite.get_width(), sprite.get_height()))
            self.sc.blit(sprite, position)

