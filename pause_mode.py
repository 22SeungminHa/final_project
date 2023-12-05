from pico2d import *

import background
import background_mode
import game_framework
import game_world
import help_mode
import stage
import stage_aim_mode
import stage_list_mode
import stage_result_mode
import stage_title
import stage_title_mode
import thema_list_mode
from background import Background
from pause import Pause
from start import StartTitle

def handle_select(x, y):
    global pause
    for i in range(3):
        if 711 - 300 / 2 <= x <= 711 + 300 / 2 and \
                400 - 125 + 125 * i - 100 / 2 <= y <= 400 - 125 + 125 * i + 100 / 2:
            if pause.size[i] != 1.1:
                pause.size[i] = 1.1
                background_mode.background.on.play()
        else:
            pause.size[i] = 1.0

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            for i in range(3):
                if 711 - 300 / 2 <= event.x <= 711 + 300 / 2 and \
                        400 - 125 + 125 * i - 100 / 2 <= event.y <= 400 - 125 + 125 * i + 100 / 2:
                    background_mode.background.click.play()
                    match i:
                        case 0:
                            for i in range(len(stage_aim_mode.arrow_mark)):
                                game_world.remove_object(stage_aim_mode.arrow_mark[i])
                            game_world.remove_object(stage_aim_mode.bar)
                            game_framework.pop_mode()
                            game_framework.pop_mode()
                            stage.init()
                            stage_title.animation = False
                            stage_aim_mode.arrow_cnt = 4
                            stage_result_mode.total_score = 0
                            stage_aim_mode.arrow_mark.clear()
                            game_framework.push_mode(stage_aim_mode)
                        case 1:
                            game_world.remove_object(stage_aim_mode.bar)
                            for i in range(len(stage_aim_mode.arrow_mark)):
                                game_world.remove_object(stage_aim_mode.arrow_mark[i])
                            game_framework.pop_mode()
                            game_framework.pop_mode()
                            game_framework.push_mode(stage_list_mode)
                        case 2:
                            game_framework.pop_mode()
                            game_framework.push_mode(help_mode)
                    break

        elif event.type == SDL_MOUSEMOTION:
            handle_select(event.x, event.y)




def init():
    global pause

    pause = Pause()
    game_world.add_object(pause, 3)


def finish():
    game_world.remove_object(pause)


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
