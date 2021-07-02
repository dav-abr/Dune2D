import pygame as pg
import time
from biulding import Building
from creature import Creature
from ground import Ground
from helpers import load_sprite
from settings import *
import window
import sprites
from wall import Wall


def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = float(value - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)


class Hud:
    __instance = None

    @staticmethod
    def get_instance(self, sc=None, world_map=None):
        if Hud.__instance is None:
            Hud(sc, world_map)
        return Hud.__instance

    def __init__(self, sc, world_map):
        if Hud.__instance is None:
            self.sc = sc
            self.sf = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SRCALPHA, 32).convert_alpha()
            self.minimap_sf = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SRCALPHA, 32).convert_alpha()
            self.cursor_sf = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SRCALPHA, 32).convert_alpha()
            self.world_map = world_map
            self.target = None
            self.building_placement = None
            self.can_place = None
            self.target_select_delay_counter = 0
            self.creature_select = load_sprite('./hud/creature_select.png')
            self.building_select = [
                load_sprite('./hud/building_select_up_left.png'),
                load_sprite('./hud/building_select_up_right.png'),
                load_sprite('./hud/building_select_down_right.png'),
                load_sprite('./hud/building_select_down_left.png')
            ]
            self.building_place = [
                load_sprite('./hud/building_place_accept.png'),
                load_sprite('./hud/building_place_not_accept.png')
            ]
            self.minimap = []
            self.minimap_update = 0
            self.minimap_last_update = time.time()
            self.minimap_update_line = 0

            Hud.__instance = self
        else:
            raise Exception('Hud can only have one instance.')

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target):
        self.__target = target

        if not target:
            self.target_select_delay_counter = 0

    def draw(self):
        self.sf.fill(pg.Color(0, 0, 0, 0))

        if self.target:
            target_image = self.target.hud_image
            image_position = [WINDOW_WIDTH - target_image.get_rect().size[0] - 48, 168]
            hp_position = [image_position[0], target_image.get_rect().size[1] + 168 + 10]

            self.target_select_delay_counter += 1
            self.target_select_delay_counter %= FPS

            hp_color = '#00A300'
            hp_percentage = self.target.hp / self.target.max_hp

            if hp_percentage < 0.2:
                hp_color = '#840000'
            elif hp_percentage < 0.7:
                hp_color = '#E8A300'

            if self.building_placement:
                x, y = pg.mouse.get_pos()
                grid_x, grid_y = (x - window.absolute_x) // window.cell_size, (y - window.absolute_y) // window.cell_size
                self.can_place = True

                for i in range(2):
                    for j in range(2):
                        if isinstance(self.world_map.buildings[grid_x + i][grid_y + j], Wall) or isinstance(self.world_map.creatures[grid_x + i][grid_y + j], Creature):
                            self.can_place = False

                for i in range(2):
                    for j in range(2):
                        self.sf.blit(self.building_place[0] if self.can_place else self.building_place[1], (
                            window.cell_size * grid_x + i * window.cell_size + window.absolute_x,
                            window.cell_size * grid_y + j * window.cell_size + window.absolute_y,
                            window.cell_size,
                            window.cell_size
                        ))
            else:
                if isinstance(self.target, Creature):
                    if self.target_select_delay_counter % (FPS / 2) < FPS / 4:
                        self.sf.blit(self.creature_select, (
                            self.target.x + window.absolute_x, self.target.y + window.absolute_y, window.cell_size,
                            window.cell_size))

                if isinstance(self.target, Building):
                    if self.target_select_delay_counter % (FPS / 2) < FPS / 4:
                        self.sf.blit(
                            self.building_select[0], (
                                self.target.x + window.absolute_x,
                                self.target.y + window.absolute_y,
                                window.cell_size,
                                window.cell_size
                            )
                        )
                        self.sf.blit(
                            self.building_select[1], (
                                self.target.x + window.absolute_x + window.cell_size * (self.target.width - 1),
                                self.target.y + window.absolute_y,
                                window.cell_size,
                                window.cell_size
                            )
                        )
                        self.sf.blit(
                            self.building_select[2], (
                                self.target.x + window.absolute_x + window.cell_size * (self.target.width - 1),
                                self.target.y + window.absolute_y + window.cell_size * (self.target.height - 1),
                                window.cell_size,
                                window.cell_size
                            )
                        )
                        self.sf.blit(
                            self.building_select[3], (
                                self.target.x + window.absolute_x,
                                self.target.y + window.absolute_y + window.cell_size * (self.target.height - 1),
                                window.cell_size,
                                window.cell_size
                            )
                        )

            self.sf.blit(target_image, (*image_position, window.cell_size, window.cell_size))
            pg.draw.rect(self.sf, pg.Color(hp_color),
                         (*hp_position, target_image.get_rect().size[0] * hp_percentage, 15))
            pg.draw.rect(self.sf, pg.Color('black'),
                         (*hp_position, target_image.get_rect().size[0] * hp_percentage, 15), 3)

        minimap_position = [WINDOW_WIDTH - 200 - 48, 168 + WINDOW_HEIGHT - 400]
        minimap_cell_size = 200 // COLS
        mouse_x, mouse_y = pg.mouse.get_pos()

        pg.draw.rect(self.sf, pg.Color('blue'),
                     (*minimap_position, 200, 200), 3)

        for col in range(COLS):
            color = 'black'

            if isinstance(self.world_map.creatures[col][self.minimap_update_line], Creature):
                color = 'blue'
            elif isinstance(self.world_map.buildings[col][self.minimap_update_line], Wall):
                color = 'blue'
            elif isinstance(self.world_map.ground[col][self.minimap_update_line], Ground):
                color = 'grey'
            pg.draw.rect(self.minimap_sf, pg.Color(color),
                         (
                             minimap_position[0] + minimap_cell_size * col,
                             minimap_position[1] + minimap_cell_size * self.minimap_update_line,
                             minimap_cell_size,
                             minimap_cell_size
                         ),
                         0
                        )

        pg.draw.rect(self.minimap_sf, pg.Color('red'),
                         (
                             minimap_position[0] + translate(mouse_x - window.absolute_x, 0, CELL_SIZE * COLS, 0,
                                                             minimap_cell_size * COLS) - minimap_cell_size // 2,
                             minimap_position[1] + translate(mouse_y - window.absolute_y, 0, CELL_SIZE * ROWS, 0,
                                                             minimap_cell_size * ROWS) - minimap_cell_size // 2,
                             minimap_cell_size,
                             minimap_cell_size
                         ),
                        0
                     )
        self.minimap_update_line = (self.minimap_update_line + 1) % ROWS

        self.sc.blit(self.sf, (0, 0))
        self.sc.blit(self.minimap_sf, (0, 0))

        if not self.building_placement:
            self.cursor_sf.fill(pg.Color(0, 0, 0, 0))
            self.cursor_sf.blit(sprites.sprites['hud']['cursor_selected'] if isinstance(self.target, Creature) else sprites.sprites['hud']['cursor'], (mouse_x - window.cell_size / 2, mouse_y - window.cell_size / 2))
            self.sc.blit(self.cursor_sf, (0, 0))
