from helpers import load_sprite, load_building_sprite


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
        },
        'ground': {
            'concrete': load_sprite('./sprites/concrete.png')
        }
    }
