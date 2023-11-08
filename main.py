from pico2d import open_canvas, delay, close_canvas
import game_framework

import start_mode as start_mode

open_canvas(1920, 1080)
game_framework.run(start_mode)
close_canvas()