import pygame as pg

from biulding import Building
from creature import Creature
from helpers import load_sprite
from settings import *
import window


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
            self.world_map = world_map
            self.target = None
            self.building_placement = None
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
                can_place = True

                for i in range(2):
                    for j in range(2):
                        if isinstance(self.world_map.buildings[grid_x + i][grid_y + j], Building) or isinstance(self.world_map.creatures[grid_x + i][grid_y + j], Creature):
                            can_place = False

                for i in range(2):
                    for j in range(2):
                        self.sc.blit(self.building_place[0] if can_place else self.building_place[1], (
                            window.cell_size * grid_x + i * window.cell_size,
                            window.cell_size * grid_y + j * window.cell_size,
                            window.cell_size,
                            window.cell_size
                        ))
            else:
                if isinstance(self.target, Creature):
                    if self.target_select_delay_counter % (FPS / 2) < FPS / 4:
                        self.sc.blit(self.creature_select, (
                            self.target.x + window.absolute_x, self.target.y + window.absolute_y, window.cell_size,
                            window.cell_size))

                if isinstance(self.target, Building):
                    if self.target_select_delay_counter % (FPS / 2) < FPS / 4:
                        self.sc.blit(
                            self.building_select[0], (
                                self.target.x + window.absolute_x,
                                self.target.y + window.absolute_y,
                                window.cell_size,
                                window.cell_size
                            )
                        )
                        self.sc.blit(
                            self.building_select[1], (
                                self.target.x + window.absolute_x + window.cell_size * (self.target.width - 1),
                                self.target.y + window.absolute_y,
                                window.cell_size,
                                window.cell_size
                            )
                        )
                        self.sc.blit(
                            self.building_select[2], (
                                self.target.x + window.absolute_x + window.cell_size * (self.target.width - 1),
                                self.target.y + window.absolute_y + window.cell_size * (self.target.height - 1),
                                window.cell_size,
                                window.cell_size
                            )
                        )
                        self.sc.blit(
                            self.building_select[3], (
                                self.target.x + window.absolute_x,
                                self.target.y + window.absolute_y + window.cell_size * (self.target.height - 1),
                                window.cell_size,
                                window.cell_size
                            )
                        )

            self.sc.blit(target_image, (*image_position, window.cell_size, window.cell_size))
            pg.draw.rect(self.sc, pg.Color(hp_color),
                         (*hp_position, target_image.get_rect().size[0] * hp_percentage, 15))
            pg.draw.rect(self.sc, pg.Color('black'),
                         (*hp_position, target_image.get_rect().size[0] * hp_percentage, 15), 3)
