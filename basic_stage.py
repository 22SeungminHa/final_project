from pico2d import *

import game_framework
import game_world
import stage_list_mode
from arrow import Arrow
from bow import Bow
from stage1_background import Stage1Background
from target import Target


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.clear()
            game_framework.change_mode(stage_list_mode)
        else:
            pass


def init():
    global background
    global arrow
    global bow
    global target

    background = Stage1Background()
    game_world.add_object(background, 0)

    arrow = Arrow()
    game_world.add_object(arrow, 0)

    bow = Bow()
    game_world.add_object(bow, 0)

    target = Target()
    game_world.add_object(target, 0)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
