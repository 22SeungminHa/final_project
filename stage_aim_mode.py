from pico2d import *

import game_framework
import game_world
import stage
import stage_launch_mode
import stage_list_mode
import stage_title_mode
from background import Background
from object_bow import Bow
from object_target import Target


def calculate_win(x, y):
    return (2 * x - 1422) / 2, -(2 * y - 800) / 2


def init():
    global target

    target = Target()
    game_world.add_object(target, 0)
    game_framework.push_mode(stage_title_mode)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            game_framework.push_mode(stage_list_mode)
        elif event.type == SDL_MOUSEMOTION:
            bow.mx, bow.my = calculate_win(event.x, event.y)
            # print(bow.mx, bow.my)
        elif event.button == SDL_BUTTON_LEFT:
            if event.type == SDL_MOUSEBUTTONDOWN:
                bow.animation = 'zoom in'
            else:
                game_framework.pop_mode()
                game_framework.push_mode(stage_launch_mode)


def finish():
    game_world.remove_object(target)
    game_world.remove_object(bow)


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    global bow

    bow = Bow()
    game_world.add_object(bow, 1)


def resume():
    pass
