import pygame as pg
import math

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

        self.creatures_sfs = []
        self.__update_creatures_sfs = []

        for i in range(COLS // CHUNK_SIZE):
            self.creatures_sfs.append([])
            self.__update_creatures_sfs.append([])
            for j in range(ROWS // CHUNK_SIZE):
                self.creatures_sfs[i].append(pg.Surface((CHUNK_SIZE * window.cell_size, CHUNK_SIZE * window.cell_size), pg.SRCALPHA, 32).convert_alpha())
                self.__update_creatures_sfs[i].append(True)

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

        self.creatures[0][0] = Tank(0, 0, self)
        self.buildings[5][5] = Building(5, 5, self, 'windtrap')
        self.buildings[7][7] = Building(7, 7, self, 'construction_yard')

    def update_ground_sf(self):
        self.__update_ground_sf = True

    def update_buildings_sf(self):
        self.__update_buildings_sf = True

    def update_creatures_sf(self):
        self.__update_creatures_sf = True

    def update_creatures_sfs(self, creature):
        chunk_i, chunk_j = math.floor(creature.i / CHUNK_SIZE), math.floor(creature.j / CHUNK_SIZE)
        self.__update_creatures_sfs[chunk_i][chunk_j] = True

    def in_window(self, position):
        x, y = position
        window_x, window_y = window.absolute_x, window.absolute_y
        return window_x < x < window_x + WINDOW_WIDTH and window_y < y < window_y + WINDOW_HEIGHT

    def draw(self):
        # self.sc.fill((166, 130, 66))
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

            self.sc.blit(self.ground_sf, (window.absolute_x, window.absolute_y))
            self.__update_ground_sf = False

        if self.__update_buildings_sf:
            self.buildings_sf.fill(pg.Color(0, 0, 0, 0))

            for col in range(COLS):
                for row in range(ROWS):
                    if self.buildings[col][row]:
                        self.buildings[col][row].blit()

            self.sc.blit(self.buildings_sf, (window.absolute_x, window.absolute_y))
            self.__update_buildings_sf = False

        # if self.__update_creatures_sf:
        #     self.creatures_sf.fill(pg.Color(0, 0, 0, 0))
        #
        #     for col in range(COLS):
        #         for row in range(ROWS):
        #             if self.creatures[col][row]:
        #                 self.creatures[col][row].blit()
        #
        #     self.__update_creatures_sf = False

        for i in range(len(self.__update_creatures_sfs)):
            for j in range(len(self.__update_creatures_sfs[0])):
                position = (i * CHUNK_SIZE * window.cell_size, j * CHUNK_SIZE * window.cell_size)

                if self.__update_creatures_sfs[i][j] and self.in_window(position):
                    self.__update_creatures_sfs[i][j] = False
                    self.creatures_sfs[i][j].fill(pg.Color(0, 0, 0, 0))
                    if self.creatures[i][j].sprite:
                        self.creatures_sfs[i][j].blit(self.creatures[i][j].sprite, (0, 0))
                    self.sc.blit(self.creatures_sfs[i][j], position)
                    print(i, j)

        # self.sc.blit(self.creatures_sf, (window.absolute_x, window.absolute_y))
