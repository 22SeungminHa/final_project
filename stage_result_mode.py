from pico2d import *

import background_mode
import game_framework
import game_world
import stage
import stage_launch_mode
import thema_list_mode
import stage_title_mode
from background import Background
from object_arrow_load import LoadArrow
from object_bow import Bow
from object_target import Target
from stage_result import Result

total_score = 0


def init():
    global result
    result = Result(total_score)
    game_world.add_object(result, 1)


def handle_select(x, y):
    if 711 - 157 - 90 <= x <= 711 - 157 + 90 and \
            400 + 155 - 90 <= y <= 400 + 155 + 90:
        result.retry_size = 1.1
    else:
        result.retry_size = 1.0
    if 711 + 157 - 90 <= x <= 711 + 157 + 90 and \
            400 + 155 - 90 <= y <= 400 + 155 + 90:
        result.next_size = 1.1
    else:
        result.next_size = 1.0


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if result.retry_size > 1.0:
                pass
            elif result.next_size > 1.0:
                pass
        elif event.type == SDL_MOUSEMOTION:
            handle_select(event.x, event.y)


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
