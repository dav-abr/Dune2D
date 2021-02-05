import pygame as pg

from biulding import Building
from settings import *
from cell import Cell
from ground import Ground
import window
from tank import Tank


class Map:
    def __init__(self, sc, ground=[], creatures=[], buildings=[]):
        self.sc = sc
        self.creatures = creatures
        self.ground_sf = pg.Surface((COLS * window.cell_size, ROWS * window.cell_size), pg.SRCALPHA, 32).convert_alpha()
        self.buildings_sf = pg.Surface((COLS * window.cell_size, ROWS * window.cell_size), pg.SRCALPHA, 32).convert_alpha()
        self.creatures_sf = pg.Surface((COLS * window.cell_size, ROWS * window.cell_size), pg.SRCALPHA, 32).convert_alpha()

        self.__update_ground_sf = True
        self.__update_buildings_sf = True
        self.__update_creatures_sf = True

        if len(ground) > 0:
            self.ground = ground
        else:
            self.ground = [[Ground(col, row, self) for row in range(ROWS)] for col in range(COLS)]

        if len(creatures) > 0:
            self.creatures = creatures
        else:
            self.creatures = [[Cell(col, row, self) for row in range(ROWS)] for col in range(COLS)]

        if len(buildings) > 0:
            self.buildings = buildings
        else:
            self.buildings = [[Cell(col, row, self) for row in range(ROWS)] for col in range(COLS)]

        # for col in range(COLS):
        #     self.creatures[col][0] = Tank(col, 0, self)

        self.creatures[1][1] = Tank(1, 1, self)
        self.buildings[5][5] = Building(5, 5, self, 'windtrap')
        self.buildings[7][7] = Building(7, 7, self, 'construction_yard')

    def update_ground_sf(self):
        self.__update_ground_sf = True

    def update_buildings_sf(self):
        self.__update_buildings_sf = True

    def update_creatures_sf(self):
        self.__update_creatures_sf = True

    def draw(self):
        self.sc.fill((166, 130, 66))
        Building.draw2()

        for col in range(COLS):
            for row in range(ROWS):
                self.ground[col][row].draw()

        for col in range(COLS):
            for row in range(ROWS):
                if self.buildings[col][row]:
                    self.buildings[col][row].draw()

        for col in range(COLS):
            for row in range(ROWS):
                if self.creatures[col][row]:
                    self.creatures[col][row].draw()

        if self.__update_ground_sf:
            self.ground_sf.fill(pg.Color(0, 0, 0, 0))

            for col in range(COLS):
                for row in range(ROWS):
                    self.ground[col][row].blit()

            self.__update_ground_sf = False

        if self.__update_buildings_sf:
            self.buildings_sf.fill(pg.Color(0, 0, 0, 0))

            for col in range(COLS):
                for row in range(ROWS):
                    if self.buildings[col][row]:
                        self.buildings[col][row].blit()

            self.__update_buildings_sf = False

        if self.__update_creatures_sf:
            self.creatures_sf.fill(pg.Color(0, 0, 0, 0))

            for col in range(COLS):
                for row in range(ROWS):
                    if self.creatures[col][row]:
                        self.creatures[col][row].blit()

            self.__update_creatures_sf = False

        self.sc.blit(self.ground_sf, (window.absolute_x, window.absolute_y))
        self.sc.blit(self.buildings_sf, (window.absolute_x, window.absolute_y))
        self.sc.blit(self.creatures_sf, (window.absolute_x, window.absolute_y))
