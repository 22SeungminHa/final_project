from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import game_world
import stage
import stage_aim_mode
import stage_result_mode
from background import Background
from object_arrow import Arrow
from object_score_bar import Bar
from object_target import Target


score = 0
aim_x, aim_y = 0, 0

def cal_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def cal_score(x, y):
    global score

    score = 10 - cal_distance(x, y, 0, 0) // 16
    if score < 0:
        score = 0
    stage_result_mode.total_score += score
    # print(score)


def init():
    global arrow
    global target

    arrow = Arrow(aim_x * 300 / 360, aim_y * 300 / 360)
    target = Target('launch')

    cal_score(aim_x, aim_y)

    game_world.add_object(arrow, 2)
    game_world.add_object(target, 1)


def finish():
    game_world.remove_object(target)
    game_world.remove_object(arrow)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


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
