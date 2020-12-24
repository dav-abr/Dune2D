import pygame as pg
from settings import *
import window


class Cell:
    def __init__(self, i, j, world_map):
        self.i = i
        self.j = j
        self.sc = None
        self.world_map = world_map
        self.x = i * window.cell_size
        self.y = j * window.cell_size
        self.f = 0
        self.g = 0
        self.h = 0
        self.wall = False
        self.neighbors = []
        self.previous = None
        self.sprite = None

    def __str__(self):
        return '{0} {1} {2}'.format(self.i, self.j, type(self).__name__)

    def __repr__(self):
        return '{0} {1} {2}'.format(self.i, self.j, type(self).__name__)

    def fill(self):
        self.isFilled = True

    def add_neighbors(self):
        ground = self.world_map.ground
        creatures = self.world_map.creatures
        buildings = self.world_map.buildings
        i, j = self.i, self.j
        self.neighbors = []

        if i < COLS - 1:
            self.neighbors.append([ground[i + 1][j], creatures[i + 1][j], buildings[i + 1][j]])
        if i > 0:
            self.neighbors.append([ground[i - 1][j], creatures[i - 1][j], buildings[i - 1][j]])
        if j < ROWS - 1:
            self.neighbors.append([ground[i][j + 1], creatures[i][j + 1], buildings[i][j + 1]])
        if j > 0:
            self.neighbors.append([ground[i][j - 1], creatures[i][j - 1], buildings[i][j - 1]])
        if i > 0 and j > 0:
            self.neighbors.append([ground[i - 1][j - 1], creatures[i - 1][j - 1], buildings[i - 1][j - 1]])
        if i < COLS - 1 and j > 0:
            self.neighbors.append([ground[i + 1][j - 1], creatures[i + 1][j - 1], buildings[i + 1][j - 1]])
        if i > 0 and j < ROWS - 1:
            self.neighbors.append([ground[i - 1][j + 1], creatures[i - 1][j + 1], buildings[i - 1][j + 1]])
        if i < COLS - 1 and j < ROWS - 1:
            self.neighbors.append([ground[i + 1][j + 1], creatures[i + 1][j + 1], buildings[i + 1][j + 1]])

    def update_neighbors(self):
        self.add_neighbors()
        for neighbor in self.neighbors:
            neighbor[0].add_neighbors()
            neighbor[1].add_neighbors()

    def blit(self):
        if self.sc and self.sprite:
            self.sc.blit(self.sprite, (self.x, self.y, window.cell_size, window.cell_size))

    def draw(self):
        pass
