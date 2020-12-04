import pygame as pg
from tank import Tank
from helpers import load_sprite
from settings import *


class Hud:
    def __init__(self, sc):
        self.target = None
        self.sc = sc
        self.target_select_delay_counter = 0

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
            if type(self.target) == Tank:
                target_image = pg.image.load('./hud/moto.png')
                target_select = load_sprite('./hud/target_select.png')
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

                if self.target_select_delay_counter % (FPS / 2) < FPS / 4:
                    self.sc.blit(target_select, (self.target.x, self.target.y, CELL_SIZE, CELL_SIZE))

                self.sc.blit(target_image, (*image_position, CELL_SIZE, CELL_SIZE))
                pg.draw.rect(self.sc, pg.Color(hp_color), (*hp_position, target_image.get_rect().size[0] * hp_percentage, 15))
                pg.draw.rect(self.sc, pg.Color('black'), (*hp_position, target_image.get_rect().size[0] * hp_percentage, 15), 3)
