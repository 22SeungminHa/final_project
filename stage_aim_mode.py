from pico2d import *

import background_mode
import game_framework
import game_world
import stage
import stage_launch_mode
import thema_list_mode
import stage_result_mode
import stage_title_mode
from background import Background
from object_arrow_load import LoadArrow
from object_arrow_mark import Mark
from object_bow import Bow
from object_score_bar import Bar
from object_target import Target

arrow_cnt = 4
arrow_mark = []

def calculate_win(x, y):
    return (2 * x - 1422) / 2, -(2 * y - 800) / 2


def normalize_vector(x, y):
    magnitude = (x ** 2 + y ** 2) ** 0.5
    vx, vy = 0, 0
    if magnitude != 0:
        vx, vy = x / magnitude, y / magnitude
    return vx, vy


def init():
    global target
    global bar

    background_mode.background.size = 1
    stage.init_wind()

    if arrow_cnt == 4:
        bar = Bar()
        game_world.add_object(bar, 0)

    if arrow_cnt == 0:
        for i in range(len(arrow_mark) - 1):
            game_world.remove_object(arrow_mark[i])
        game_framework.pop_mode()
        game_framework.push_mode(stage_result_mode)
    else:
        target = Target('aim')
        game_world.add_object(target, 0)
        game_framework.push_mode(stage_title_mode)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        # 마우스 이동
        elif event.type == SDL_MOUSEMOTION and bow.animation == 'zoom in':
            bow.vx, bow.vy = calculate_win(event.x, event.y)
            bow.vx, bow.vy = normalize_vector(bow.vx, bow.vy)

        elif event.button == SDL_BUTTON_LEFT:
            # 마우스 클릭
            if event.type == SDL_MOUSEBUTTONDOWN:
                bow.animation = 'zoom in'

            # 화살 발사
            elif bow.animation == 'zoom in':
                stage_launch_mode.aim_x = (bow.x - target.x) / target.size + math.cos(stage.wind_angle) * 20
                stage_launch_mode.aim_y = (bow.y - target.y) / target.size + math.sin(stage.wind_angle) * 20
                background_mode.background.size = 300 / (target.size * 360)

                for i in range(len(arrow_mark)):
                    arrow_mark[i].ratio = 300 / 360
                    arrow_mark[i].mx, arrow_mark[i].my = 0, 0
                arrow_mark.append(Mark(stage_launch_mode.aim_x, stage_launch_mode.aim_y))

                game_framework.pop_mode()
                game_framework.push_mode(stage_launch_mode)


def finish():
    global arrow_cnt

    if arrow_cnt > 0:
        game_world.remove_object(target)
        game_world.remove_object(bow)
        for i in range(arrow_cnt):
            game_world.remove_object(load_arrow[i])
        arrow_cnt -= 1
    else:
        game_world.remove_object(bar)

def update():
    game_world.update()



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    global bow
    global load_arrow
    global arrow_mark

    bow = Bow()
    game_world.add_object(bow, 1)

    load_arrow = []
    for i in range(arrow_cnt):
        load_arrow.append(LoadArrow(i))
        game_world.add_object(load_arrow[i], 1)

    if len(arrow_mark) > 0:
        game_world.add_object(arrow_mark[len(arrow_mark) - 1], 2)

    # print(len(arrow_mark))
    for i in range(len(arrow_mark)):
        arrow_mark[i].ratio = 0.45



def resume():
    pass
