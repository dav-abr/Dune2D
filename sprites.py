from helpers import load_sprite, load_building_sprite
import window


def init():
    global sprites
    sprites = {
        'creatures': {
            'tank': {
                'straight_up': load_sprite('./sprites/moto_straight_up.png'),
                'straight_right': load_sprite('./sprites/moto_straight_right.png'),
                'straight_down': load_sprite('./sprites/moto_straight_down.png'),
                'straight_left': load_sprite('./sprites/moto_straight_left.png'),
                'diagonal_up_right': load_sprite('./sprites/moto_diagonal_up_right.png'),
                'diagonal_down_right': load_sprite('./sprites/moto_diagonal_down_right.png'),
                'diagonal_down_left': load_sprite('./sprites/moto_diagonal_down_left.png'),
                'diagonal_up_left': load_sprite('./sprites/moto_diagonal_up_left.png'),
                'horizontal_left_down': load_sprite('./sprites/moto_angle_horizontal_left_down.png'),
                'horizontal_right_down': load_sprite('./sprites/moto_angle_horizontal_right_down.png'),
                'horizontal_left_up': load_sprite('./sprites/moto_angle_horizontal_left_up.png'),
                'horizontal_right_up': load_sprite('./sprites/moto_angle_horizontal_right_up.png'),
                'vertical_down_left': load_sprite('./sprites/moto_angle_vertical_down_left.png'),
                'vertical_down_right': load_sprite('./sprites/moto_angle_vertical_down_right.png'),
                'vertical_up_right': load_sprite('./sprites/moto_angle_vertical_up_right.png'),
                'vertical_up_left': load_sprite('./sprites/moto_angle_vertical_up_left.png'),
            }
        },
        'buildings': {
            'windtrap': load_building_sprite('./houses/{0}.png'.format('windtrap'), 2, 2),
            'construction_yard': load_building_sprite('./houses/{0}.png'.format('construction_yard'), 2, 2),
            'building_indicator_0': load_sprite('./houses/building_indicator_straight_up.png', window.cell_size / 2 - window.cell_size / 30),
            'building_indicator_90': load_sprite('./houses/building_indicator_straight_right.png', window.cell_size / 2 - window.cell_size / 30),
            'building_indicator_180': load_sprite('./houses/building_indicator_straight_down.png', window.cell_size / 2 - window.cell_size / 30),
            'building_indicator_270': load_sprite('./houses/building_indicator_straight_left.png', window.cell_size / 2 - window.cell_size / 30),
            'building_indicator_45': load_sprite('./houses/building_indicator_angle_up_right.png', window.cell_size / 2 - window.cell_size / 30),
            'building_indicator_135': load_sprite('./houses/building_indicator_angle_down_right.png', window.cell_size / 2 - window.cell_size / 30),
            'building_indicator_225': load_sprite('./houses/building_indicator_angle_down_left.png', window.cell_size / 2 - window.cell_size / 30),
            'building_indicator_315': load_sprite('./houses/building_indicator_angle_up_left.png', window.cell_size / 2 - window.cell_size / 30)
        },
        'ground': {
            'concrete': load_sprite('./sprites/concrete.png')
        },
        'hud': {
            'cursor': load_sprite('./hud/cursor.png'),
            'cursor_selected': load_sprite('./hud/cursor_selected.png'),
        }
    }
