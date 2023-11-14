from pico2d import *

import stage1_play_mode
import game_world
import stage_aim_mode
import stage_intro_mode
import stage_launch_mode
import stage_list_mode
import stage_result_mode

stage = [stage_intro_mode, stage_intro_mode, stage_intro_mode, stage_intro_mode, stage_intro_mode]
mode = [stage_intro_mode, stage_aim_mode, stage_launch_mode, stage_result_mode]


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