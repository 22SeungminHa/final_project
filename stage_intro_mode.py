from pico2d import*

import game_framework
import game_world
import stage_aim_mode
from stage_intro import StageIntro


def init():
    global intro
    intro = StageIntro()
    game_world.add_object(intro, 0)


def finish():
    game_world.remove_object(intro)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(stage_aim_mode)