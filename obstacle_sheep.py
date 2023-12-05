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


class Sheep:
    def __init__(self):
        self.image = load_image('./resource/sheep.png')
        self.timer = random.randint(1000, 2000)
        self.angle = math.atan2(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0))
        self.x, self.y = 0, 0

    def update(self):
        stage_aim_mode.bow.x += math.cos(self.angle) / 5
        stage_aim_mode.bow.y += math.sin(self.angle) / 5
        self.x = stage_aim_mode.bow.x + math.cos(self.angle) * 64 * stage_aim_mode.bow.size
        self.y = stage_aim_mode.bow.y + math.sin(self.angle) * 64 * stage_aim_mode.bow.size

        self.timer -= 1
        if self.timer == 0:
            game_world.remove_object(stage.sheep)
            stage.sheep = None

    def draw(self):
        self.image.draw(711 + self.x, 400 + self.y)





