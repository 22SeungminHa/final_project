from pico2d import *

import background_mode
import clear_state
import game_framework
import game_world
import stage
import stage_aim_mode
import stage_list_mode
import stage_result_mode
import stage_title
import stage_title_mode
import start_mode
from background import Background
from thema_list import ThemaList


def handle_select(x, y):
    for i in range(5):
        if thema_list.x[i] - 300 / 2 <= x <= thema_list.x[i] + 300 / 2 and \
                thema_list.y[i] - 300 / 2 <= y <= thema_list.y[i] + 300 / 2:
            thema_list.select = i
            return
    thema_list.select = -1
    # print('False')


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            background_mode.background.change_image('m', 0)
            game_framework.pop_mode()
            game_framework.push_mode(start_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            clear_state.init_state()

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 0 <= thema_list.select < 5:
                game_framework.pop_mode()
                game_framework.push_mode(stage_list_mode)
            # print('selected')
        elif event.type == SDL_MOUSEMOTION:
            handle_select(event.x, event.y)


def init():
    global thema_list

    background_mode.background.change_image('m', 1)

    thema_list = ThemaList()
    game_world.add_object(thema_list, 1)


def finish():
    game_world.remove_object(thema_list)


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
