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
