from pico2d import *

import game_framework
import stage_aim_mode
import stage_launch_mode
import math

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 200.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Mark:
    def __init__(self, x, y):
        self.image = load_image('./resource/arrow_mark.png')
        self.x, self.y = x, y
        self.ratio = 1

    def update(self):
        pass


    def draw(self):
        self.image.draw(self.x * self.ratio + 711, self.y * self.ratio + 400, 10, 10)





