from pico2d import*

import game_framework
import game_world
import stage
import stage_launch_mode
import stage_title_mode
from background import Background
from object_bow import Bow
from object_target import Target


def init():
    global target
    global title_animation

    title_animation = False

    target = Target()
    game_world.add_object(target, 1)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            game_framework.pop_mode()
            game_framework.push_mode(stage_launch_mode)


def finish():
    game_world.remove_object(target)


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
