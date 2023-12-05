from pico2d import *

import background_mode
import game_framework
import game_world
import stage
import stage_aim_mode
import stage_result_mode
import stage_title
import stage_title_mode
import start_mode
import thema_list_mode
from background import Background
from stage_list import StageList


def handle_select(x, y):
    for i in range(8):
        if stage_list.x[i] - 200 / 2 <= x <= stage_list.x[i] + 200 / 2 and \
                stage_list.y[i] - 200 / 2 <= y <= stage_list.y[i] + 200 / 2:
            stage_list.select = i
            return
    stage_list.select = -1
    # print('False')


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            game_framework.push_mode(thema_list_mode)

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 0 <= stage_list.select < 8:
                stage.init()
                game_framework.pop_mode()
                game_framework.push_mode(stage_aim_mode)
                stage_title.animation = False
                stage_aim_mode.arrow_cnt = 1
                stage_result_mode.total_score = 0
                stage_aim_mode.arrow_mark.clear()
            # print('selected')
        elif event.type == SDL_MOUSEMOTION:
            handle_select(event.x, event.y)


def init():
    global stage_list

    stage_list = StageList()
    game_world.add_object(stage_list, 1)


def finish():
    game_world.remove_object(stage_list)


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
