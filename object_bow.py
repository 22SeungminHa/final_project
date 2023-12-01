import random

from pico2d import *
import math

import game_framework
import stage_title

r = 1

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')
        self.x = 275.0
        self.y = -182.5625
        self.size = 0.7335
        self.animation = 'start'
        self.vx, self.vy = 0, 0
        self.size_v = 0

    def update(self):
        if self.animation == 'start':
            self.size -= 0.0005
            self.x -= 0.75
            self.y = 50 + -0.01 * (self.x - 122.5) ** 2
            if self.x <= 0:
                self.animation = None
                if stage_title.animation == True:
                    game_framework.pop_mode()
        elif self.animation == 'zoom in':
            if self.size < 1.0:
                self.size += 0.005
            else:
                self.animation = 'zoom out'
        elif self.animation == 'zoom out' and self.size > 0.95:
                self.size_v += 0.00005
                self.size -= self.size_v

        self.x += self.vx * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.vy * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.draw(711 + self.x, 400 + self.y, 1466 * self.size, 1866 * self.size)
