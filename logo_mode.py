from pico2d import*
import game_framework
import background_mode


def init():
    global image
    global logo_start_time
    image = load_image('./resource/tuk_credit.png')
    logo_start_time = get_time()


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
            game_framework.change_mode(background_mode)


def update():
    global logo_start_time

    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(background_mode)


def draw():
    clear_canvas()
    image.draw(711, 350, 1600, 1200)
    update_canvas()


def pause():
    pass

def resume():
    pass