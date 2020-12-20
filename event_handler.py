import pygame as pg
import window
from biulding import Building
from tank import Tank


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
            #     world_map.creatures[col][0].go_to(world_map.ground[col][ROWS - 1])
            if self.world_map.creatures[grid_x][grid_y] and isinstance(self.world_map.creatures[grid_x][grid_y], Tank):
                self.target = self.world_map.creatures[grid_x][grid_y]
                self.hud.target = self.target
            elif self.world_map.buildings[grid_x][grid_y] and isinstance(self.world_map.buildings[grid_x][grid_y], Building):
                self.target = self.world_map.buildings[grid_x][grid_y]
                if self.target.name == 'construction_yard':
                    self.hud.building_placement = (Building, 'windtrap')
                    self.building_placement = 'windtrap'
                self.hud.target = self.target
            elif self.target and isinstance(self.target, Tank) and not self.world_map.ground[grid_x][grid_y].wall and (not self.target.x == grid_x) and (not self.target.y == grid_y):
                print('kajshd')
                self.target.go_to(self.world_map.ground[grid_x][grid_y])
                self.hud.target = None
                self.target = None

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