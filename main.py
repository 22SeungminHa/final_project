from pico2d import open_canvas, delay, close_canvas

import clear_state
import game_framework
import logo_mode as start_mode

clear_state.read_2d_list_from_file('stage.json')
open_canvas(1422, 800)
game_framework.run(start_mode)
close_canvas()
