from settings import *


class Cell:
    def __init__(self, i, j, sc, world_map):
        self.i = i
        self.j = j
        self.sc = sc
        self.world_map = world_map
        self.x = i * CELL_SIZE
        self.y = j * CELL_SIZE
        self.f = 0
        self.g = 0
        self.h = 0
        self.wall = False
        self.tank = False
        self.neighbors = []
        self.previous = None

    def __str__(self):
        return '{0} {1}'.format(self.i, self.j)

    def add_neighbors(self):
        ground = self.world_map.ground
        creatures = self.world_map.creatures
        i, j = self.i, self.j
        self.neighbors = []

        if i < COLS - 1:
            self.neighbors.append([ground[i + 1][j], creatures[i + 1][j]])
        if i > 0:
            self.neighbors.append([ground[i - 1][j], creatures[i - 1][j]])
        if j < ROWS - 1:
            self.neighbors.append([ground[i][j + 1], creatures[i][j + 1]])
        if j > 0:
            self.neighbors.append([ground[i][j - 1], creatures[i][j - 1]])
        if i > 0 and j > 0:
            self.neighbors.append([ground[i - 1][j - 1], creatures[i - 1][j - 1]])
        if i < COLS - 1 and j > 0:
            self.neighbors.append([ground[i + 1][j - 1], creatures[i + 1][j - 1]])
        if i > 0 and j < ROWS - 1:
            self.neighbors.append([ground[i - 1][j + 1], creatures[i - 1][j + 1]])
        if i < COLS - 1 and j < ROWS - 1:
            self.neighbors.append([ground[i + 1][j + 1], creatures[i + 1][j + 1]])

    def update_neighbors(self):
        self.add_neighbors()
        for neighbor in self.neighbors:
            neighbor[0].add_neighbors()
            neighbor[1].add_neighbors()

    def draw(self):
        pass
