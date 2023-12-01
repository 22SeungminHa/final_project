from pico2d import *

import background_mode
import game_framework
import game_world
import stage
import stage_launch_mode
import stage_list_mode
import stage_title_mode
from background import Background
from object_arrow_load import LoadArrow
from object_bow import Bow
from object_target import Target

total_score = 0


def init():
    print(total_score)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def finish():
    pass


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
