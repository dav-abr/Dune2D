import pygame as pg
from tank import Tank
from settings import *
from map import Map

pg.init()
sc = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

world_map = Map(CELL_SIZE, sc)

for col in range(COLS):
    for row in range(ROWS):
        world_map.grid[col][row].add_neighbors()

world_map.grid[10][10] = Tank(10, 10, sc, world_map)
target = None


def get_click_mouse_pos():
    global target
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
    click = pg.mouse.get_pressed()
    if click[0]:
        if world_map.grid[grid_x][grid_y].tank:
            target = world_map.grid[grid_x][grid_y]
        elif target and not world_map.grid[grid_x][grid_y].wall and (not target.x == grid_x) and (not target.y == grid_y):
            target.go_to(world_map.grid[grid_x][grid_y])
            target = None
    return (grid_x, grid_y) if click[0] else False


while True:
    world_map.draw()

    get_click_mouse_pos()

    for col in range(COLS):
        for row in range(ROWS):
            world_map.grid[col][row].draw()

    clock.tick(FPS)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
