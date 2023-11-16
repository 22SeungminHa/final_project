from pico2d import *

import game_framework
import stage_aim_mode
import stage_list_mode


class StageAim:
    def __init__(self):
        self.background_image = load_image('./resource/palace7.png')

    def update(self):
        pass

    def draw(self):
        self.background_image.draw(711, 400, 1422, 800)