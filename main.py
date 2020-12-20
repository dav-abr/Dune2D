import pygame as pg

from biulding import Building
from event_handler import EventHandler
from tank import Tank
from settings import *
from map import Map
from hud import Hud
import window

window.init()

target = None

pg.init()
pg.font.init()
sc = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

world_map = Map(sc)
for col in range(COLS):
    world_map.creatures[col][0] = Tank(col, 0, sc, world_map)

world_map.buildings[5][5] = Building(5, 5, sc, world_map, 'windtrap')
world_map.buildings[7][7] = Building(7, 7, sc, world_map, 'construction_yard')

hud = Hud(sc, world_map)

event_handler = EventHandler(world_map, hud)

for col in range(COLS):
    for row in range(ROWS):
        world_map.ground[col][row].add_neighbors()


def handle_key_press():
    keyinput = pg.key.get_pressed()

    if keyinput[pg.K_LEFT]:
        if window.absolute_dx < 0:
            window.absolute_dx = 0
        if window.absolute_dx < 15:
            window.absolute_dx += 1
        window.absolute_x += window.absolute_dx
    elif keyinput[pg.K_RIGHT]:
        if window.absolute_dx > 0:
            window.absolute_dx = 0
        if window.absolute_dx > -15:
            window.absolute_dx -= 1
        window.absolute_x += window.absolute_dx
    else:
        window.absolute_dx = 0

    if keyinput[pg.K_UP]:
        if window.absolute_dy < 0:
            window.absolute_dy = 0
        if window.absolute_dy < 15:
            window.absolute_dy += 1
        window.absolute_y += window.absolute_dy
    elif keyinput[pg.K_DOWN]:
        if window.absolute_dy > 0:
            window.absolute_dy = 0
        if window.absolute_dy > -15:
            window.absolute_dy -= 1
        window.absolute_y += window.absolute_dy
    else:
        window.absolute_dy = 0


def get_click_mouse_pos():
    global target
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = (x - window.absolute_x) // window.cell_size, (y - window.absolute_y) // window.cell_size
    click = pg.mouse.get_pressed()
    if click[0]:
        # for col in range(COLS):
        #     world_map.creatures[col][0].go_to(world_map.ground[col][ROWS - 1])
        if world_map.creatures[grid_x][grid_y] and isinstance(world_map.creatures[grid_x][grid_y], Tank):
            target = world_map.creatures[grid_x][grid_y]
            hud.target = target
        elif world_map.buildings[grid_x][grid_y] and isinstance(world_map.buildings[grid_x][grid_y], Building):
            target = world_map.buildings[grid_x][grid_y]
            if target.name == 'construction_yard':
                hud.building_placement = (Building, 'windtrap')
            hud.target = target
        elif target and isinstance(target, Tank) and not world_map.ground[grid_x][grid_y].wall and (not target.x == grid_x) and (not target.y == grid_y):
            target.go_to(world_map.ground[grid_x][grid_y])
            hud.target = None
            target = None
    return (grid_x, grid_y) if click[0] else False


while True:
    world_map.draw()

    event_handler.draw()

    for col in range(COLS):
        for row in range(ROWS):
            world_map.ground[col][row].draw()

    for col in range(COLS):
        for row in range(ROWS):
            if world_map.buildings[col][row]:
                world_map.buildings[col][row].draw()

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

        # if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP:
        #     if event.button == 4:
        #         window.cell_size += 5
        #     if event.button == 5:
        #         window.cell_size -= 5
