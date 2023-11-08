from pico2d import *

import basic_stage
import game_world
import stage_list


def handle_events():
    match stage_list.select:
        case 0:
            basic_stage.handle_events()
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass


def init():
    match stage_list.select:
        case 0:
            basic_stage.init()
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
