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



class Arrow:
    def __init__(self, index):
        self.image = load_image('./resource/arrow.png')
        self.index = index

    def update(self):
        pass

    def draw(self):
        # 화살
        self.image.clip_composite_draw(0, 0, 1030, 73, 70 * (math.pi / 180), 'h', (self.index + 1) * 50, 0, 1030 * 0.5, 73 * 0.5)




