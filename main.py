import pygame as pg
import window

window.init()

from event_handler import EventHandler
from settings import *
from map import Map
from hud import Hud
import sprites
from pygame.locals import *


target = None

pg.init()
pg.font.init()
pg.mouse.set_visible(False)

flags = DOUBLEBUF
sc = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), flags)
sc.set_alpha(None)
sprites.init()

clock = pg.time.Clock()


world_map = Map(sc)
hud = Hud(sc, world_map)

event_handler = EventHandler(world_map, hud)

for col in range(COLS):
    for row in range(ROWS):
        world_map.ground[col][row].add_neighbors()

while True:
    world_map.draw()

    event_handler.draw()

    hud.draw()

    clock.tick(FPS)
    pg.display.flip()
    fps = str(int(clock.get_fps()))
    pg.display.set_caption(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)

        # if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP:
        #     if event.button == 4:
        #         window.cell_size += 5
        #     if event.button == 5:
        #         window.cell_size -= 5
