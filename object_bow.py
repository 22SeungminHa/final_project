import random

from pico2d import *
import math

import game_framework
import stage
import stage_title

r = 1

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')
        self.icon_image = [load_image('./resource/thema_icon' + "%d" % (i + 1) + '.png') for i in range(stage.thema_num + 1)]
        self.wind_image = load_image('./resource/direction.png')

        self.sound = load_wav('./sound/bow.wav')
        self.sound.set_volume(128)

        self.x = 275.0
        self.y = -182.5625
        self.size = 0.7335
        self.animation = 'start'
        self.vx, self.vy = 0, 0
        self.size_v = 0

    def update(self):
        if self.animation == 'start':
            if self.size > 0.55:
                self.size -= 0.0005
            self.x -= 0.75
            self.y = 80 + -0.01 * (self.x - 122.5) ** 2
            if self.x <= 0:
                self.animation = None
                if stage_title.animation == True:
                    game_framework.pop_mode()
        elif self.animation == 'zoom in' and self.size_v < 0.6 * math.pi:
            self.size_v += 0.01
            self.size = 0.55 + math.sin(self.size_v) / 3

        self.x += self.vx * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.vy * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.draw(711 + self.x, 400 + self.y, 1466 * self.size, 1866 * self.size)

        for i in range(len(self.icon_image)):
            self.icon_image[i].draw(60 + 100 * i, 800 - 60, 100, 100)

        if stage.thema_num == 1 or stage.thema_num == 4:
            self.wind_image.clip_composite_draw(0, 0, 150, 80, stage.wind_angle, 'h', 1422 - 100, 800 - 150)


