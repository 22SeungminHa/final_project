from pico2d import *

import background_mode
import game_framework
import game_world
import stage
import stage_aim_mode
import stage_launch_mode
import stage_list
import stage_list_mode
import stage_title
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
    global total_score

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 711 - 157 - 90 <= event.x <= 711 - 157 + 90 and \
                    400 + 155 - 90 <= event.y <= 400 + 155 + 90:
                stage.init()
                stage_title.animation = False
                stage_aim_mode.arrow_cnt = 4
                total_score = 0
                stage_aim_mode.arrow_mark.clear()
                game_framework.pop_mode()
                game_framework.push_mode(stage_aim_mode)
            elif 711 + 157 - 90 <= event.x <= 711 + 157 + 90 and \
                    400 + 155 - 90 <= event.y <= 400 + 155 + 90:
                if stage_list_mode.stage_list.select == 7 and thema_list_mode.thema_list.select == 4:
                    game_framework.pop_mode()
                    game_framework.push_mode(thema_list_mode)
                elif stage_list_mode.stage_list.select == 7:
                    stage_list_mode.stage_list.select = 0
                    thema_list_mode.thema_list.select += 1
                    stage.init()
                    stage_title.animation = False
                    stage_aim_mode.arrow_cnt = 4
                    total_score = 0
                    stage_aim_mode.arrow_mark.clear()
                    game_framework.pop_mode()
                    game_framework.push_mode(stage_aim_mode)
                else:
                    stage_list_mode.stage_list.select += 1
                    stage.init()
                    stage_title.animation = False
                    stage_aim_mode.arrow_cnt = 4
                    total_score = 0
                    stage_aim_mode.arrow_mark.clear()
                    game_framework.pop_mode()
                    game_framework.push_mode(stage_aim_mode)
        elif event.type == SDL_MOUSEMOTION:
            handle_select(event.x, event.y)


def finish():
    game_world.remove_object(result)


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
