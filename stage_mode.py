from pico2d import *

import game_framework
import game_world
import start_mode
from stage import Stage
from stage_background import StageBackground


def handle_select(x, y):
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.clear()
            game_framework.change_mode(start_mode)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.key == SDL_BUTTON_LEFT:
            handle_select(event.x, event.y)


def init():
    global stage_background
    global stage
    running = True

    stage_background = StageBackground()
    game_world.add_object(stage_background, 0)

    stage = Stage()
    game_world.add_object(stage, 0)


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
