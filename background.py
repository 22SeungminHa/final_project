from pico2d import *
from enum import Enum

import game_world

mode = ('start_background', 'stage_background')

class Background:
    def __init__(self):
        self.image = load_image("./resource/start_background.png")

    def draw(self):
        self.image.draw(711, 400, 1422, 800)

    def change_image(self, t, i):
        if t == 'm':
            self.image = load_image("./resource/" + mode[i] + ".png")
        elif t == 's':
            self.image = load_image("./resource/palace" + "%d" % (i + 1) + ".png")
        elif t == 't':
            self.image = load_image("./resource/Tom_Yum_Goong" + "%d" % (i + 1) + ".png")

    def update(self):
        pass
