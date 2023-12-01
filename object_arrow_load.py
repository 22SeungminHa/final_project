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


class LoadArrow:
    def __init__(self, index):
        self.image = load_image('./resource/arrow.png')
        self.index = index
        self.y = -200
        self.animation = True
        self.t = 0

    def update(self):
        if self.animation:
            self.t += 0.01
            self.y = -200 + math.sin(self.t) * 230
            if math.sin(self.t) * 230 - math.sin(self.t - 0.01) * 230 < 0 and self.y <= -25:
                self.animation = False


    def draw(self):
        self.image.clip_composite_draw(0, 0, 1030, 73, 75 * (math.pi / 180), 'a', (self.index) * 30 + 10, self.y, 1030 * 0.4, 73 * 0.4)





