from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
import game_framework
import background_mode


def init():
    global image
    image = load_image('./resource/tuk_credit.png')


def finish():
    global image
    del image


def handle_events():
    events = get_events()


def update():
    pass


def draw():
    clear_canvas()
    image.draw(711, 350, 1600, 1200)
    update_canvas()
    game_framework.pop_mode()
    game_framework.push_mode(background_mode)


def pause():
    pass

def resume():
    pass