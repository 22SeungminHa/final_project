from pico2d import *

import background
import background_mode
import game_framework
import game_world
import thema_list_mode
from background import Background
from start import StartTitle


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_mode()
            game_framework.push_mode(thema_list_mode)


def init():
    global title

    title = StartTitle()
    game_world.add_object(title, 0)


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
