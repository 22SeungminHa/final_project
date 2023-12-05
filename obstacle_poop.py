import random

from pico2d import *

import game_framework
import game_world
import stage
import stage_aim_mode
import stage_launch_mode
import math

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 200.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Poop:
    def __init__(self):
        self.image = load_image('./resource/poop' + '%d' % random.randint(1, 3) + '.png')
        self.size = 0
        self.timer = 0

    def update(self):
        if self.size < 1:
            self.size += 0.01
        elif self.timer == 0:
            self.timer = get_time()
        elif get_time() - self.timer > 1.0:
            game_world.remove_object(stage.poop)
            stage.poop_timer = random.randint(500, 1000)

    def draw(self):
        self.image.draw(711, 400, 982 * self.size, 800 * self.size)





