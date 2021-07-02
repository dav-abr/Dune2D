import pygame as pg
from random import randint
import window
from biulding import Building
from bulding_part import BuildingPart
from tank import Tank
from settings import *


class EventHandler:
    def __init__(self, world_map, hud):
        self.world_map = world_map
        self.hud = hud
        self.target = None
        self.building_placement = None

    def draw(self):
        x, y = pg.mouse.get_pos()
        grid_x, grid_y = (x - window.absolute_x) // window.cell_size, (y - window.absolute_y) // window.cell_size
        click = pg.mouse.get_pressed()

        if click[0]:
            # for col in range(COLS):
            #     self.world_map.creatures[col][0].go_to(self.world_map.ground[randint(0, COLS - 1)][randint(0, ROWS - 1)])
            if self.building_placement and self.hud.can_place:
                self.world_map.buildings[grid_x][grid_y] = Building(grid_x, grid_y, self.world_map,
                                                                    self.building_placement)
                self.target = None
                self.building_placement = None
                self.hud.building_placement = None

            if self.target:
                if isinstance(self.target, Tank) and not self.world_map.ground[grid_x][
                    grid_y].wall and self.target.x != grid_x and self.target.y != grid_y:
                    self.target.go_to(self.world_map.ground[grid_x][grid_y])
                    self.hud.target = None
                    self.target = None
                # elif isinstance(self.target, Building):
                #     pass
            if self.world_map.creatures[grid_x][grid_y] and isinstance(self.world_map.creatures[grid_x][grid_y], Tank):
                self.target = self.world_map.creatures[grid_x][grid_y]
                self.hud.target = self.target
            elif self.world_map.buildings[grid_x][grid_y] and \
                    (isinstance(self.world_map.buildings[grid_x][grid_y], Building) or
                     isinstance(self.world_map.buildings[grid_x][grid_y], BuildingPart)):
                building = self.world_map.buildings[grid_x][grid_y]

                if isinstance(building, BuildingPart):
                    building = building.parent

                self.target = building
                if self.target.name == 'construction_yard':
                    self.hud.building_placement = (Building, 'windtrap')
                    self.building_placement = 'windtrap'
                self.hud.target = self.target

        keyinput = pg.key.get_pressed()

        if keyinput[pg.K_LEFT]:
            if window.absolute_dx < 0:
                window.absolute_dx = 0
            if window.absolute_dx < 30:
                window.absolute_dx += 1
            window.absolute_x += window.absolute_dx
        elif keyinput[pg.K_RIGHT]:
            if window.absolute_dx > 0:
                window.absolute_dx = 0
            if window.absolute_dx > -30:
                window.absolute_dx -= 1
            window.absolute_x += window.absolute_dx
        else:
            window.absolute_dx = 0

        if keyinput[pg.K_UP]:
            if window.absolute_dy < 0:
                window.absolute_dy = 0
            if window.absolute_dy < 30:
                window.absolute_dy += 1
            window.absolute_y += window.absolute_dy
        elif keyinput[pg.K_DOWN]:
            if window.absolute_dy > 0:
                window.absolute_dy = 0
            if window.absolute_dy > -30:
                window.absolute_dy -= 1
            window.absolute_y += window.absolute_dy
        else:
            window.absolute_dy = 0
