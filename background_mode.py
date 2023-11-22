from pico2d import *
from enum import Enum

import game_framework
import game_world
import start_mode
from background import Background

def init():
    global background

    background = Background('m', 0)
    game_world.add_object(background, 0)
    game_framework.push_mode(start_mode)


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