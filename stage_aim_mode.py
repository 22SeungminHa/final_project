from pico2d import*

import game_framework
import game_world
import stage_launch_mode
import stage_title_mode
from background import Background
from object_bow import Bow
from object_target import Target


def init():
    global bow
    global target
    global background
    global title_animation

    title_animation = False

    bow = Bow()
    target = Target()
    background = Background()

    game_world.add_object(target, 1)
    game_world.add_object(background, 0)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(stage_launch_mode)


def finish():
    game_world.clear()


def update():
    global title_animation

    if title_animation == False:
        game_framework.push_mode(stage_title_mode)
        title_animation = True
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
