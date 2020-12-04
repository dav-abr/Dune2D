import pygame as pg
from tank import Tank
from settings import *
from map import Map
from wall import Wall
from hud import Hud

pg.init()
pg.font.init()
sc = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

world_map = Map(CELL_SIZE, sc)
world_map.creatures[3][3] = Tank(3, 3, sc, world_map)
world_map.creatures[4][4] = Tank(4, 4, sc, world_map)
world_map.ground[5][5] = Wall(5, 5, sc, world_map)

hud = Hud(sc)

for col in range(COLS):
    for row in range(ROWS):
        world_map.ground[col][row].add_neighbors()

target = None


def get_click_mouse_pos():
    global target
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
    click = pg.mouse.get_pressed()
    if click[0]:
        if world_map.creatures[grid_x][grid_y] and world_map.creatures[grid_x][grid_y].tank:
            target = world_map.creatures[grid_x][grid_y]
            hud.target = target
            target.target = True
        elif target and not world_map.ground[grid_x][grid_y].wall and (not target.x == grid_x) and (not target.y == grid_y):
            target.go_to(world_map.ground[grid_x][grid_y])
            target.target = False
            hud.target = None
            target = None
        # elif not target:
        #     world_map.ground[grid_x][grid_y] = Wall(grid_x, grid_y, sc, world_map)
        #     world_map.ground[grid_x][grid_y].update_neighbors()
    return (grid_x, grid_y) if click[0] else False


while True:
    world_map.draw()

    get_click_mouse_pos()

    # for e in pg.event.get():
    #     if e.type == pg.MOUSEBUTTONDOWN:
    #         if e.button == 4:
    #             CELL_SIZE += 1
    #         if e.button == 5:
    #             CELL_SIZE -= 1

    for col in range(COLS):
        for row in range(ROWS):
            world_map.ground[col][row].draw()

    for col in range(COLS):
        for row in range(ROWS):
            if world_map.creatures[col][row]:
                world_map.creatures[col][row].draw()

    hud.draw()

    clock.tick(FPS)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
