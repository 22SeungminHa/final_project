from pico2d import*

import game_framework
import game_world
import stage_aim_mode
from background import Background
from stage_title import StageTitle


def init():
    global stage_intro
    global background
    stage_intro = StageTitle()
    background = Background()
    game_world.add_object(stage_intro, 1)
    game_world.add_object(background, 0)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(stage_aim_mode)


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
