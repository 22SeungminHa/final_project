from pico2d import *

import game_framework
import game_world
import stage_list_mode
from start_background import StartBackground
from start_title import StartTitle


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_world.clear()
            game_framework.change_mode(stage_list_mode)


def init():
    global title
    global background
    global announcement

    background = StartBackground()
    game_world.add_object(background, 0)

    title = StartTitle()
    game_world.add_object(title, 0)


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
