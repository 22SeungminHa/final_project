from pico2d import *

import stage1_play
import game_world
import stage_list_mode

stage = [stage1_play, stage1_play, stage1_play, stage1_play, stage1_play]


def handle_events():
    stage[stage_list_mode.stage_list.select].handle_events()


def init():
    stage[stage_list_mode.stage_list.select].init()


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
