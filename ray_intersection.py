import math
import pygame as pg


HEIGHT = 8
WIDTH = 8
GRID = [
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
]
CELL_SIZE = 100

pg.init()
pg.font.init()
sc = pg.display.set_mode(((WIDTH + 1) * CELL_SIZE, (HEIGHT + 1) * CELL_SIZE))
clock = pg.time.Clock()


class Ray:
    def __init__(self, x, y, dir_x, dir_y):
        self.start_x = x
        self.start_y = y
        self.dir_x = dir_x
        self.dir_y = dir_y


def get_helpers(pos, dir_):
    tile = math.floor(pos / CELL_SIZE)

    if dir_ > 0:
        d_tile = 1
        dt = ((tile + 0) * CELL_SIZE - pos) / dir_
    else:
        d_tile = -1
        dt = ((tile - 1) * CELL_SIZE - pos) / dir_

    return tile, d_tile, dt, d_tile * CELL_SIZE / dir_


def ray_intersections(ray):
    tile_x, dtile_x, dt_x, ddt_x = get_helpers(ray.start_x, ray.dir_x)
    tile_y, dtile_y, dt_y, ddt_y = get_helpers(ray.start_y, ray.dir_y)
    t = 0

    if ray.dir_x * ray.dir_x + ray.dir_y * ray.dir_y > 0:
        while 0 <= tile_x <= WIDTH and 0 <= tile_y <= HEIGHT and (tile_x != ray.dir_x or tile_y != ray.dir_y):
            # print(tile_x, tile_y)

            GRID[tile_y][tile_x] = '*'
            # print(ray.start_x + ray.dir_x * t, ray.start_y + ray.dir_y * t)
            # print(dt_x, dt_y, t)

            if dt_x < dt_y:
                tile_x += dtile_x
                dt = dt_x
                t = t + dt
                dt_x = dt_x + ddt_x - dt
                dt_y = dt_y - dt
            else:
                tile_y += dtile_y
                dt = dt_y
                t = t + dt
                dt_y = dt_y + ddt_y - dt
                dt_x = dt_x - dt
    else:
        # pass
        GRID[tile_y][tile_x] = '*'


ray = Ray(200, 200, 7, 1)
ray_intersections(ray)

for i in GRID:
    print(''.join(i))

while True:
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if GRID[j][i] == '_':
                pg.draw.rect(sc, pg.Color('white'), (i * CELL_SIZE, j * CELL_SIZE, (i + 1) * CELL_SIZE, (j + 1) * CELL_SIZE))
            else:
                pg.draw.rect(sc, pg.Color('red'),
                             (i * CELL_SIZE, j * CELL_SIZE, (i + 1) * CELL_SIZE, (j + 1) * CELL_SIZE))

    for i in range(WIDTH):
        for j in range(HEIGHT):
            pg.draw.rect(sc, pg.Color('black'),
                         (i * CELL_SIZE, j * CELL_SIZE, (i + 1) * CELL_SIZE, (j + 1) * CELL_SIZE), 1)

    pg.draw.line(
        sc,
        pg.Color('green'),
        (
            ray.start_x + CELL_SIZE / 2,
            ray.start_y + CELL_SIZE / 2
        ),
        (
            ray.dir_x * CELL_SIZE + CELL_SIZE / 2,
            ray.dir_y * CELL_SIZE + CELL_SIZE / 2
        ),
        2
    )

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
