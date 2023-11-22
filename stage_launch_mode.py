from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import game_world
import stage
from background import Background
from object_arrow import Arrow
from object_target import Target


def init():
    global arrow
    global target
    global x, y

    x = stage_aim

    arrow = Arrow()
    target = Target()

    game_world.add_object(arrow, 2)
    game_world.add_object(target, 1)


def finish():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
