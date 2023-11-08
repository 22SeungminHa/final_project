from pico2d import *

import game_framework
import game_world
import play_mode
import start_mode
from stage_list import StageList
from stage_list_background import StageListBackground


def handle_select(x, y):
    for i in range(5):
        if stage_list.x[i] - stage_list.w[i] / 2 <= x <= stage_list.x[i] + stage_list.w[i] / 2 and stage_list.y[i] - stage_list.h[i] / 2 <= y <= stage_list.y[i] + stage_list.h[i] / 2:
            stage_list.select = i
            return
    stage_list.select = -1
    print('False')


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(start_mode)

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            print('selected')
            if 0 <= stage_list.select < 5:
                game_framework.change_mode(play_mode)
        elif event.type == SDL_MOUSEMOTION:
            handle_select(event.x, event.y)


def init():
    global background
    global stage_list

    background = StageListBackground()
    game_world.add_object(background, 0)

    stage_list = StageList()
    game_world.add_object(stage_list, 0)


def finish():
    game_world.clear()


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
