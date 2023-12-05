from pico2d import *

import background
import background_mode
import game_framework
import game_world
import stage
import stage_aim_mode
import stage_list_mode
import stage_result_mode
import stage_title
import thema_list_mode
from background import Background
from help import Help
from pause import Pause
from start import StartTitle

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()


def init():
    global help

    help = Help()
    game_world.add_object(help, 3)


def finish():
    game_world.remove_object(help)


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
