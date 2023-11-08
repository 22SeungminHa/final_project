from pico2d import *

import game_framework
import game_world
import play_mode
import start_mode
from stage_list import StageList
from stage_list_background import StageListBackground


def handle_select(x, y):
    for i in range(5):
        if x <= stage_list.x[i] + stage_list.w[i] / 2 and x >= stage_list.x[i] - stage_list.w[i] / 2 and y <= stage_list.y[i] + stage_list.h[i] / 2 and y >= stage_list.y[i] - stage_list.h[i] / 2:
            stage_list.select = i
            return
    stage_list.select = -1


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.clear()
            game_framework.change_mode(start_mode)
        elif event.type == SDL_MOUSEMOTION:
            handle_select(event.x, event.y)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.key == SDL_BUTTON_LEFT:
            if stage_list.select >= 0:
                game_world.clear()
                game_framework.change_mode(play_mode)


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
