from pico2d import *

import game_framework
import game_world
from start_background import Background
from start_title import Title


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            # game_framework.change_mode(stage_mode)
            pass


def init():
    global title
    global background
    global announcement
    running = True

    background = Background()
    game_world.add_object(background, 0)

    title = Title()
    game_world.add_object(title, 0)


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
