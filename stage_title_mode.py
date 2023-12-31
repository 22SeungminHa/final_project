from pico2d import *

import game_framework
import game_world
import stage_aim_mode
import stage_launch_mode
import thema_list_mode
from background import Background
from object_bow import Bow
from object_target import Target
from stage_title import StageTitle




def init():
    global title
    global bow

    title = StageTitle()
    game_world.add_object(title, 3)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_mode()


def finish():
    game_world.remove_object(title)


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
