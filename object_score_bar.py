import random

from pico2d import *
import math

import game_framework
import stage
import stage_result_mode
import stage_title

class Bar:
    def __init__(self):
        self.image = load_image('./resource/score_bar.png')
        self.degree_image = load_image('./resource/score_degree.png')
        self.shirimp_image = load_image('./resource/shirimp.png')
        self.animation_degree = 0
        self.w = stage_result_mode.total_score

    def update(self):
        if self.w < stage_result_mode.total_score:
            self.w += 0.05
        else:
            self.w = stage_result_mode.total_score

    def draw(self):
        self.degree_image.draw(902 + 14 + 250 * self.w / 40, 800 - 16 - 17, 500 * self.w / 40, 30)

        self.image.draw(902 + 250, 800 - 16 - 17)
        for i in range(3):
            self.shirimp_image.draw(902 + 14 + 500 * stage.target_score[i] / 40, 800 - 16 - 17)