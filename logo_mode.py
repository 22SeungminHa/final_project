from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
import game_framework
import background_mode


def init():
    global image
    global logo_start_time

    image = load_image('./resource/tuk_credit.png')
    logo_start_time = get_time()
    game_framework.push_mode(background_mode)


def finish():
    global image
    del image


def handle_events():
    events = get_events()


def update():
    global logo_start_time

    if get_time() - logo_start_time >= 2.0:
        game_framework.pop_mode()


def draw():
    clear_canvas()
    image.draw(711, 400, 1422, 800)
    update_canvas()


def pause():
    pass

def resume():
    pass